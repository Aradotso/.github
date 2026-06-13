#!/usr/bin/env python3
"""Audit GitHub org security settings for Ara.

The script uses the authenticated GitHub CLI (`gh`) so it does not read or print
credentials. It writes a Markdown report with gaps and supporting evidence.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ORG = "Aradotso"
DEFAULT_OUTPUT = Path("docs/security/org-security-audit.md")
CODEOWNERS_LOCATIONS = ("CODEOWNERS", ".github/CODEOWNERS", "docs/CODEOWNERS")


@dataclass
class RepoFinding:
    name: str
    private: bool
    archived: bool
    default_branch: str | None
    branch_protection: str = "unknown"
    requires_pr_review: bool = False
    required_approvals: int = 0
    dismisses_stale_reviews: bool = False
    requires_status_checks: bool = False
    status_check_count: int = 0
    requires_code_owner_reviews: bool = False
    codeowners_file: str | None = None
    secret_scanning: str = "unknown"
    push_protection: str = "unknown"
    dependabot_alerts: str = "unknown"
    dependabot_security_updates: str = "unknown"
    admin_teams: list[str] = field(default_factory=list)
    admin_users: list[str] = field(default_factory=list)
    gaps: list[str] = field(default_factory=list)


def run_gh(args: list[str], *, accept_404: bool = False) -> tuple[int, str, str]:
    proc = subprocess.run(
        ["gh", *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0 and not accept_404:
        raise RuntimeError(f"gh {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.returncode, proc.stdout, proc.stderr


def gh_json(args: list[str], *, accept_404: bool = False) -> Any:
    code, out, _ = run_gh(args, accept_404=accept_404)
    if code != 0 or not out.strip():
        return None
    return json.loads(out)


def gh_status(args: list[str]) -> int:
    code, _, _ = run_gh(["api", "-i", *args], accept_404=True)
    return code


def paginate(path: str, jq: str | None = None) -> list[Any]:
    args = ["api", "--paginate", path]
    if jq:
        args.extend(["--jq", jq])
    _, out, _ = run_gh(args)
    if not out.strip():
        return []
    rows: list[Any] = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        parsed = json.loads(line)
        if isinstance(parsed, list):
            rows.extend(parsed)
        else:
            rows.append(parsed)
    return rows


def get_org_settings(org: str) -> dict[str, Any]:
    return gh_json([
        "api",
        f"orgs/{org}",
        "--jq",
        "{login, plan: .plan.name, advanced_security_enabled_for_new_repositories, dependabot_alerts_enabled_for_new_repositories, dependabot_security_updates_enabled_for_new_repositories, secret_scanning_enabled_for_new_repositories, secret_scanning_push_protection_enabled_for_new_repositories}",
    ]) or {}


def get_repos(org: str) -> list[dict[str, Any]]:
    return paginate(f"orgs/{org}/repos?per_page=100&type=all")


def get_org_admins(org: str) -> list[str]:
    admins = paginate(f"orgs/{org}/members?per_page=100&role=admin")
    return sorted(str(admin["login"]) for admin in admins if isinstance(admin, dict) and admin.get("login"))


def get_outside_collaborators(org: str) -> list[str]:
    collabs = paginate(f"orgs/{org}/outside_collaborators?per_page=100")
    return sorted(str(collab["login"]) for collab in collabs if isinstance(collab, dict) and collab.get("login"))


def get_repo_admins(owner: str, repo: str) -> tuple[list[str], list[str]]:
    teams = gh_json([
        "api",
        f"repos/{owner}/{repo}/teams?per_page=100",
        "--jq",
        '[.[] | select(.permission == "admin") | .name] | sort',
    ], accept_404=True) or []
    users = gh_json([
        "api",
        f"repos/{owner}/{repo}/collaborators?per_page=100&affiliation=direct",
        "--jq",
        '[.[] | select(.permissions.admin == true) | .login] | sort',
    ], accept_404=True) or []
    return [str(team) for team in teams], [str(user) for user in users]


def get_content_path(owner: str, repo: str, ref: str, locations: tuple[str, ...]) -> str | None:
    for location in locations:
        code, _, _ = run_gh(["api", f"repos/{owner}/{repo}/contents/{location}?ref={ref}"], accept_404=True)
        if code == 0:
            return location
    return None


def audit_repo(org: str, repo: dict[str, Any]) -> RepoFinding:
    name = repo["name"]
    default_branch = repo.get("default_branch")
    finding = RepoFinding(
        name=name,
        private=bool(repo.get("private")),
        archived=bool(repo.get("archived")),
        default_branch=default_branch,
    )

    security = repo.get("security_and_analysis") or {}
    finding.secret_scanning = (security.get("secret_scanning") or {}).get("status", "unknown")
    finding.push_protection = (security.get("secret_scanning_push_protection") or {}).get("status", "unknown")

    if default_branch:
        finding.codeowners_file = get_content_path(org, name, default_branch, CODEOWNERS_LOCATIONS)

    if default_branch == "main":
        protection = gh_json(["api", f"repos/{org}/{name}/branches/main/protection"], accept_404=True)
        if protection:
            finding.branch_protection = "enabled"
            reviews = protection.get("required_pull_request_reviews") or {}
            status_checks = protection.get("required_status_checks") or {}
            contexts = status_checks.get("contexts") or []
            checks = status_checks.get("checks") or []
            finding.required_approvals = int(reviews.get("required_approving_review_count") or 0)
            finding.requires_pr_review = finding.required_approvals > 0
            finding.dismisses_stale_reviews = bool(reviews.get("dismiss_stale_reviews"))
            finding.requires_code_owner_reviews = bool(reviews.get("require_code_owner_reviews"))
            finding.status_check_count = len(contexts) + len(checks)
            finding.requires_status_checks = finding.status_check_count > 0
        else:
            finding.branch_protection = "missing"
    elif default_branch:
        finding.branch_protection = f"not audited: default branch is {default_branch}"
    else:
        finding.branch_protection = "not audited: no default branch"

    # Status-only endpoints return 204 when enabled and non-zero when disabled or inaccessible.
    if gh_status([f"repos/{org}/{name}/vulnerability-alerts"]) == 0:
        finding.dependabot_alerts = "enabled"
    else:
        finding.dependabot_alerts = "disabled_or_inaccessible"

    if gh_status([f"repos/{org}/{name}/automated-security-fixes"]) == 0:
        finding.dependabot_security_updates = "enabled"
    else:
        finding.dependabot_security_updates = "disabled_or_inaccessible"

    teams, users = get_repo_admins(org, name)
    finding.admin_teams = teams
    finding.admin_users = users

    if finding.archived:
        return finding

    if default_branch != "main":
        finding.gaps.append("default branch is not `main`; manual branch-protection review needed")
    elif finding.branch_protection != "enabled":
        finding.gaps.append("`main` branch protection is missing")
    else:
        if not finding.requires_pr_review:
            finding.gaps.append("branch protection does not require PR review")
        if not finding.requires_status_checks:
            finding.gaps.append("branch protection does not require status checks")
        if not finding.dismisses_stale_reviews:
            finding.gaps.append("branch protection does not dismiss stale reviews")
        if finding.codeowners_file and not finding.requires_code_owner_reviews:
            finding.gaps.append("CODEOWNERS exists but branch protection does not require code-owner review")
        if not finding.codeowners_file:
            finding.gaps.append("CODEOWNERS file not found on default branch")

    if finding.secret_scanning != "enabled":
        finding.gaps.append("secret scanning is not enabled or was not visible to the auditor")
    if finding.push_protection != "enabled":
        finding.gaps.append("secret-scanning push protection is not enabled or was not visible to the auditor")
    if finding.dependabot_alerts != "enabled":
        finding.gaps.append("Dependabot alerts are disabled or inaccessible")
    if finding.dependabot_security_updates != "enabled":
        finding.gaps.append("Dependabot security updates are disabled or inaccessible")

    return finding


def md_bool(value: bool) -> str:
    return "yes" if value else "no"


def render_report(org: str, org_settings: dict[str, Any], admins: list[str], outside_collabs: list[str], findings: list[RepoFinding]) -> str:
    generated = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    active_findings = [f for f in findings if not f.archived]
    repos_with_gaps = [f for f in active_findings if f.gaps]
    lines: list[str] = []
    lines.append("# Org security audit")
    lines.append("")
    lines.append(f"Generated: {generated}")
    lines.append(f"Organization: `{org}`")
    lines.append(f"Plan: `{org_settings.get('plan', 'unknown')}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Repositories audited: {len(findings)} ({len(active_findings)} active, {len(findings) - len(active_findings)} archived)")
    lines.append(f"- Active repositories with gaps: {len(repos_with_gaps)}")
    lines.append(f"- Org owners visible to this audit: {len(admins)}")
    lines.append(f"- Outside collaborators visible to this audit: {len(outside_collabs)}")
    lines.append("")
    lines.append("## Org-level security settings")
    lines.append("")
    org_checks = [
        ("Advanced Security enabled for new repositories", org_settings.get("advanced_security_enabled_for_new_repositories")),
        ("Dependabot alerts enabled for new repositories", org_settings.get("dependabot_alerts_enabled_for_new_repositories")),
        ("Dependabot security updates enabled for new repositories", org_settings.get("dependabot_security_updates_enabled_for_new_repositories")),
        ("Secret scanning enabled for new repositories", org_settings.get("secret_scanning_enabled_for_new_repositories")),
        ("Secret scanning push protection enabled for new repositories", org_settings.get("secret_scanning_push_protection_enabled_for_new_repositories")),
    ]
    for label, value in org_checks:
        lines.append(f"- {label}: `{value}`")
    lines.append("")
    if org_settings.get("secret_scanning_enabled_for_new_repositories") is not True:
        lines.append("Gap: secret scanning is not enabled org-wide for new repositories, or the setting was not exposed by the API token used for this audit.")
    if org_settings.get("secret_scanning_push_protection_enabled_for_new_repositories") is not True:
        lines.append("Gap: secret-scanning push protection is not enabled org-wide for new repositories, or the setting was not exposed by the API token used for this audit.")
    if org_settings.get("dependabot_security_updates_enabled_for_new_repositories") is not True:
        lines.append("Gap: Dependabot security updates are not enabled org-wide for new repositories, or the setting was not exposed by the API token used for this audit.")
    lines.append("")
    lines.append("## Admin access review")
    lines.append("")
    lines.append("Org owners visible to the auditing token:")
    if admins:
        for admin in admins:
            lines.append(f"- `{admin}`")
    else:
        lines.append("- None visible")
    lines.append("")
    lines.append("Gap: this audit can identify org owners and repo admins, but it cannot determine which humans are essential without a maintained access roster. Create or link an owner/admin access roster and review it quarterly.")
    lines.append("")
    lines.append("## Outside collaborators")
    lines.append("")
    if outside_collabs:
        for collab in outside_collabs:
            lines.append(f"- `{collab}`")
        lines.append("")
        lines.append("Gap: outside collaborators exist. Confirm each collaborator has an owner, expiration date, and business justification in the access roster.")
    else:
        lines.append("No outside collaborators were visible to the auditing token.")
    lines.append("")
    lines.append("## Repository findings")
    lines.append("")
    for f in sorted(findings, key=lambda item: item.name.lower()):
        lines.append(f"### `{f.name}`")
        lines.append("")
        lines.append(f"- Private: {md_bool(f.private)}")
        lines.append(f"- Archived: {md_bool(f.archived)}")
        lines.append(f"- Default branch: `{f.default_branch or 'none'}`")
        lines.append(f"- Main branch protection: `{f.branch_protection}`")
        lines.append(f"- Requires PR review: {md_bool(f.requires_pr_review)} ({f.required_approvals} approvals)")
        lines.append(f"- Requires status checks: {md_bool(f.requires_status_checks)} ({f.status_check_count} checks)")
        lines.append(f"- Dismisses stale reviews: {md_bool(f.dismisses_stale_reviews)}")
        lines.append(f"- CODEOWNERS file: `{f.codeowners_file or 'not found'}`")
        lines.append(f"- Requires code-owner review: {md_bool(f.requires_code_owner_reviews)}")
        lines.append(f"- Secret scanning: `{f.secret_scanning}`")
        lines.append(f"- Secret-scanning push protection: `{f.push_protection}`")
        lines.append(f"- Dependabot alerts: `{f.dependabot_alerts}`")
        lines.append(f"- Dependabot security updates: `{f.dependabot_security_updates}`")
        lines.append(f"- Admin teams: {', '.join(f'`{team}`' for team in f.admin_teams) if f.admin_teams else 'none visible'}")
        lines.append(f"- Direct admin users: {', '.join(f'`{user}`' for user in f.admin_users) if f.admin_users else 'none visible'}")
        if f.gaps:
            lines.append("- Gaps:")
            for gap in f.gaps:
                lines.append(f"  - {gap}")
        else:
            lines.append("- Gaps: none found by this audit")
        lines.append("")
    lines.append("## Recommended follow-ups")
    lines.append("")
    lines.append("- Enable org-wide secret scanning, push protection, Dependabot alerts, and Dependabot security updates for new repositories in GitHub organization security settings.")
    lines.append("- Apply a repository ruleset or branch protection template to every active repository with `main`: require PR review, status checks, stale-review dismissal, and CODEOWNERS review where a CODEOWNERS file exists.")
    lines.append("- Add CODEOWNERS files where ownership is missing, then require code-owner review in branch protection/rulesets.")
    lines.append("- Create or update an access roster covering org owners, repo admins, and outside collaborators with owner, reason, and review/expiration date.")
    lines.append("- Re-run `python3 scripts/audit-org-security.py` after settings changes and commit the refreshed report.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit GitHub organization security posture.")
    parser.add_argument("--org", default=ORG)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    org_settings = get_org_settings(args.org)
    repos = get_repos(args.org)
    admins = get_org_admins(args.org)
    outside_collabs = get_outside_collaborators(args.org)

    findings = [audit_repo(args.org, repo) for repo in repos]
    report = render_report(args.org, org_settings, admins, outside_collabs, findings)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")

    gap_count = sum(1 for finding in findings if not finding.archived and finding.gaps)
    print(f"Wrote {args.output} for {len(findings)} repositories; {gap_count} active repositories have gaps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
