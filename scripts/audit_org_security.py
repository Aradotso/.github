#!/usr/bin/env python3
"""Audit GitHub organization security settings with the GitHub CLI.

The script intentionally reports inaccessible settings as unknown instead of
claiming compliance. It uses `gh api` so it can run with the reviewer/operator's
existing GitHub authentication and scopes.
"""

from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import quote


ORG_DEFAULTS = [
    "advanced_security_enabled_for_new_repositories",
    "dependabot_alerts_enabled_for_new_repositories",
    "dependabot_security_updates_enabled_for_new_repositories",
    "secret_scanning_enabled_for_new_repositories",
    "secret_scanning_push_protection_enabled_for_new_repositories",
]

CODEOWNERS_PATHS = ["CODEOWNERS", ".github/CODEOWNERS", "docs/CODEOWNERS"]
TRACKING_ISSUE_TERMS = "security baseline branch protection secret scanning dependabot"


@dataclass
class ApiResult:
    ok: bool
    status: int | None
    data: Any
    stderr: str


def run_gh(args: list[str], *, expect_json: bool = True) -> ApiResult:
    proc = subprocess.run(
        ["gh", *args],
        text=True,
        capture_output=True,
        check=False,
    )
    status: int | None = None
    stderr = proc.stderr.strip()
    for line in stderr.splitlines():
        if "HTTP " in line:
            try:
                status = int(line.rsplit("HTTP ", 1)[1].split()[0])
            except (IndexError, ValueError):
                pass
    if proc.returncode != 0:
        return ApiResult(False, status, None, stderr)
    if not expect_json:
        return ApiResult(True, status, proc.stdout, stderr)
    if not proc.stdout.strip():
        return ApiResult(True, status, None, stderr)
    try:
        return ApiResult(True, status, json.loads(proc.stdout), stderr)
    except json.JSONDecodeError as exc:
        return ApiResult(False, status, None, f"JSON parse failed: {exc}; {stderr}")


def gh_api(endpoint: str, *, paginate: bool = False, method: str = "GET", fields: dict[str, str] | None = None) -> ApiResult:
    args = ["api"]
    if paginate:
        args.append("--paginate")
    if method != "GET":
        args.extend(["--method", method])
    if fields:
        for key, value in fields.items():
            args.extend(["-f", f"{key}={value}"])
    args.append(endpoint)
    return run_gh(args)


def endpoint_status(endpoint: str) -> str:
    result = gh_api(endpoint)
    if result.ok:
        return "enabled"
    if result.status in {403, 404, 451} or result.status is None:
        return "disabled_or_inaccessible"
    return f"unknown_http_{result.status}"


def list_items(endpoint: str) -> tuple[list[dict[str, Any]], str | None]:
    result = gh_api(endpoint, paginate=True)
    if not result.ok:
        return [], result.stderr or "request failed"
    if result.data is None:
        return [], None
    if isinstance(result.data, list):
        return result.data, None
    return [result.data], None


def check_codeowners(org: str, repo: dict[str, Any]) -> tuple[bool, str | None]:
    default_branch = repo.get("default_branch") or "main"
    for path in CODEOWNERS_PATHS:
        encoded = quote(path, safe="")
        result = gh_api(f"repos/{org}/{repo['name']}/contents/{encoded}?ref={quote(default_branch, safe='')}")
        if not result.ok or not isinstance(result.data, dict):
            continue
        content = result.data.get("content")
        if result.data.get("encoding") == "base64" and isinstance(content, str):
            try:
                decoded = base64.b64decode(content).decode("utf-8", errors="replace")
            except Exception:
                decoded = ""
            if decoded.strip():
                return True, path
        elif content:
            return True, path
    return False, None


def branch_protection(org: str, repo_name: str) -> tuple[dict[str, Any], str | None]:
    result = gh_api(f"repos/{org}/{repo_name}/branches/main/protection")
    if not result.ok or not isinstance(result.data, dict):
        reason = result.stderr or "branch protection missing or inaccessible"
        return {
            "main_protected": False,
            "requires_pr_review": False,
            "dismisses_stale_reviews": False,
            "requires_status_checks": False,
            "requires_code_owner_reviews": False,
        }, reason

    data = result.data
    reviews = data.get("required_pull_request_reviews") or {}
    status_checks = data.get("required_status_checks") or {}
    return {
        "main_protected": True,
        "requires_pr_review": bool(reviews),
        "dismisses_stale_reviews": bool(reviews.get("dismiss_stale_reviews")),
        "requires_status_checks": bool(status_checks and status_checks.get("contexts") is not None),
        "required_status_check_contexts": status_checks.get("contexts") or [],
        "requires_code_owner_reviews": bool(reviews.get("require_code_owner_reviews")),
        "required_approving_review_count": reviews.get("required_approving_review_count"),
    }, None


def repo_admins(org: str, repo_name: str) -> tuple[list[str], str | None]:
    admins, error = list_items(f"repos/{org}/{repo_name}/collaborators?permission=admin&per_page=100")
    return sorted(item.get("login", "unknown") for item in admins), error


def repo_security_analysis(repo: dict[str, Any], key: str) -> str:
    security = repo.get("security_and_analysis")
    if not isinstance(security, dict):
        return "unknown"
    setting = security.get(key)
    if not isinstance(setting, dict):
        return "unknown"
    return str(setting.get("status") or "unknown")


def audit(org: str) -> dict[str, Any]:
    org_result = gh_api(f"orgs/{org}")
    if not org_result.ok or not isinstance(org_result.data, dict):
        raise SystemExit(f"Unable to read organization {org}: {org_result.stderr}")

    repos, repos_error = list_items(f"orgs/{org}/repos?per_page=100&type=all")
    repos = sorted(repos, key=lambda item: item.get("full_name", ""))

    owners, owners_error = list_items(f"orgs/{org}/members?role=admin&per_page=100")
    outside, outside_error = list_items(f"orgs/{org}/outside_collaborators?per_page=100")

    repo_findings: list[dict[str, Any]] = []
    for repo in repos:
        name = repo["name"]
        protection, protection_error = branch_protection(org, name)
        has_codeowners, codeowners_path = check_codeowners(org, repo)
        admins, admins_error = repo_admins(org, name)
        dependabot_alerts = endpoint_status(f"repos/{org}/{name}/vulnerability-alerts")
        dependabot_security_updates = endpoint_status(f"repos/{org}/{name}/automated-security-fixes")

        gaps: list[str] = []
        if not protection["main_protected"]:
            gaps.append("main branch protection missing/inaccessible")
        if not protection["requires_pr_review"]:
            gaps.append("main does not require PR review")
        if not protection["requires_status_checks"]:
            gaps.append("main does not require status checks")
        if not protection["dismisses_stale_reviews"]:
            gaps.append("main does not dismiss stale reviews")
        if has_codeowners and not protection["requires_code_owner_reviews"]:
            gaps.append("CODEOWNERS exists but code-owner reviews are not required")
        if not has_codeowners:
            gaps.append("CODEOWNERS missing")
        if dependabot_alerts != "enabled":
            gaps.append("Dependabot alerts disabled/inaccessible")
        if dependabot_security_updates != "enabled":
            gaps.append("Dependabot security updates disabled/inaccessible")
        if repo_security_analysis(repo, "secret_scanning") not in {"enabled", "unknown"}:
            gaps.append("secret scanning disabled")
        if repo_security_analysis(repo, "secret_scanning_push_protection") not in {"enabled", "unknown"}:
            gaps.append("secret scanning push protection disabled")

        repo_findings.append(
            {
                "name": name,
                "full_name": repo.get("full_name"),
                "private": repo.get("private"),
                "archived": repo.get("archived"),
                "default_branch": repo.get("default_branch"),
                "html_url": repo.get("html_url"),
                "protection": protection,
                "protection_error": protection_error,
                "codeowners": codeowners_path if has_codeowners else None,
                "secret_scanning": repo_security_analysis(repo, "secret_scanning"),
                "secret_scanning_push_protection": repo_security_analysis(repo, "secret_scanning_push_protection"),
                "dependabot_alerts": dependabot_alerts,
                "dependabot_security_updates": dependabot_security_updates,
                "admin_collaborators": admins,
                "admin_collaborators_error": admins_error,
                "gaps": gaps,
            }
        )

    issue_search = gh_api(
        f"search/issues?q={quote(TRACKING_ISSUE_TERMS + ' org:' + org + ' is:issue is:open', safe='')}"
    )
    existing_issues = []
    if issue_search.ok and isinstance(issue_search.data, dict):
        existing_issues = [
            {
                "title": item.get("title"),
                "html_url": item.get("html_url"),
                "repository_url": item.get("repository_url"),
            }
            for item in issue_search.data.get("items", [])[:5]
        ]

    return {
        "org": org,
        "generated_on": date.today().isoformat(),
        "org_defaults": {key: org_result.data.get(key) for key in ORG_DEFAULTS},
        "repos_error": repos_error,
        "owners": sorted(item.get("login", "unknown") for item in owners),
        "owners_error": owners_error,
        "outside_collaborators": sorted(item.get("login", "unknown") for item in outside),
        "outside_collaborators_error": outside_error,
        "repo_findings": repo_findings,
        "existing_tracking_issues": existing_issues,
    }


def yes_no(value: Any) -> str:
    if value is True:
        return "yes"
    if value is False:
        return "no"
    if value is None:
        return "unknown"
    return str(value)


def render_markdown(data: dict[str, Any]) -> str:
    repos = data["repo_findings"]
    repo_count = len(repos)
    gap_repos = [repo for repo in repos if repo["gaps"]]
    protected = sum(1 for repo in repos if repo["protection"].get("main_protected"))
    pr_reviews = sum(1 for repo in repos if repo["protection"].get("requires_pr_review"))
    status_checks = sum(1 for repo in repos if repo["protection"].get("requires_status_checks"))
    stale = sum(1 for repo in repos if repo["protection"].get("dismisses_stale_reviews"))
    codeowners_respected = sum(
        1
        for repo in repos
        if repo["codeowners"] and repo["protection"].get("requires_code_owner_reviews")
    )
    dependabot_security = sum(1 for repo in repos if repo["dependabot_security_updates"] == "enabled")

    lines: list[str] = []
    lines.append(f"# {data['org']} organization security audit")
    lines.append("")
    lines.append(f"Generated: {data['generated_on']}")
    lines.append("")
    lines.append("## Scope and method")
    lines.append("")
    lines.append(
        f"This report was generated with `scripts/audit_org_security.py` using the authenticated GitHub CLI against the `{data['org']}` organization. Settings that the current token could not read are reported as `unknown` or `disabled_or_inaccessible` rather than assumed compliant."
    )
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Repositories checked: {repo_count}")
    lines.append(f"- Repositories with one or more gaps: {len(gap_repos)}")
    lines.append(f"- Repositories with `main` branch protection visible: {protected}/{repo_count}")
    lines.append(f"- Repositories requiring PR review on `main`: {pr_reviews}/{repo_count}")
    lines.append(f"- Repositories requiring status checks on `main`: {status_checks}/{repo_count}")
    lines.append(f"- Repositories dismissing stale reviews on `main`: {stale}/{repo_count}")
    lines.append(f"- Repositories where CODEOWNERS is present and enforced: {codeowners_respected}/{repo_count}")
    lines.append(f"- Repositories with Dependabot security updates enabled: {dependabot_security}/{repo_count}")
    lines.append("")
    lines.append("## Organization defaults")
    lines.append("")
    for key, value in data["org_defaults"].items():
        lines.append(f"- `{key}`: `{yes_no(value)}`")
    lines.append("")
    if any(data["org_defaults"].get(key) is False for key in ORG_DEFAULTS):
        lines.append(
            "Gap: org-level security defaults for new repositories are not fully enabled. Enable Advanced Security where licensed, Dependabot alerts, Dependabot security updates, secret scanning, and secret scanning push protection for new repositories."
        )
        lines.append("")

    lines.append("## Admin access review")
    lines.append("")
    if data.get("owners_error"):
        lines.append(f"- Org owner inventory: `unknown` ({data['owners_error']})")
    else:
        owners = ", ".join(f"`{owner}`" for owner in data["owners"]) or "none visible"
        lines.append(f"- Org owners visible to the token: {owners}")
        lines.append("- Review required: confirm each org owner is essential and protected by strong authentication.")
    lines.append("")

    lines.append("## Outside collaborators")
    lines.append("")
    if data.get("outside_collaborators_error"):
        lines.append(f"- Outside collaborator inventory: `unknown` ({data['outside_collaborators_error']})")
    elif data["outside_collaborators"]:
        collaborators = ", ".join(f"`{user}`" for user in data["outside_collaborators"])
        lines.append(f"- Outside collaborators visible to the token: {collaborators}")
        lines.append("- Gap: document owner, business justification, repository scope, and expiration date for each outside collaborator.")
    else:
        lines.append("- No outside collaborators visible to the token.")
    lines.append("")

    if data["existing_tracking_issues"]:
        lines.append("## Existing tracking issues")
        lines.append("")
        for issue in data["existing_tracking_issues"]:
            lines.append(f"- [{issue['title']}]({issue['html_url']})")
        lines.append("")

    lines.append("## Per-repository findings")
    lines.append("")
    for repo in repos:
        protection = repo["protection"]
        lines.append(f"### `{repo['full_name']}`")
        lines.append("")
        lines.append(f"- URL: {repo['html_url']}")
        lines.append(f"- Private: `{yes_no(repo['private'])}`; archived: `{yes_no(repo['archived'])}`; default branch: `{repo['default_branch']}`")
        lines.append(f"- `main` protected: `{yes_no(protection.get('main_protected'))}`")
        lines.append(f"- Requires PR review: `{yes_no(protection.get('requires_pr_review'))}`")
        lines.append(f"- Dismisses stale reviews: `{yes_no(protection.get('dismisses_stale_reviews'))}`")
        lines.append(f"- Requires status checks: `{yes_no(protection.get('requires_status_checks'))}`")
        lines.append(f"- Required status checks: `{', '.join(protection.get('required_status_check_contexts') or []) or 'none'}`")
        lines.append(f"- CODEOWNERS path: `{repo['codeowners'] or 'missing'}`")
        lines.append(f"- Requires CODEOWNER reviews: `{yes_no(protection.get('requires_code_owner_reviews'))}`")
        lines.append(f"- Secret scanning: `{repo['secret_scanning']}`")
        lines.append(f"- Secret scanning push protection: `{repo['secret_scanning_push_protection']}`")
        lines.append(f"- Dependabot alerts: `{repo['dependabot_alerts']}`")
        lines.append(f"- Dependabot security updates: `{repo['dependabot_security_updates']}`")
        if repo.get("admin_collaborators_error"):
            lines.append(f"- Repo admin collaborator inventory: `unknown` ({repo['admin_collaborators_error']})")
        else:
            admins = ", ".join(f"`{admin}`" for admin in repo["admin_collaborators"]) or "none visible"
            lines.append(f"- Repo admin collaborators visible to the token: {admins}")
        if repo["gaps"]:
            lines.append("- Gaps:")
            for gap in repo["gaps"]:
                lines.append(f"  - {gap}")
        else:
            lines.append("- Gaps: none visible")
        if repo["protection_error"]:
            lines.append(f"- Branch protection read note: `{repo['protection_error']}`")
        lines.append("")

    lines.append("## Recommended follow-ups")
    lines.append("")
    lines.append("- Enable org defaults for Dependabot alerts, Dependabot security updates, secret scanning, and secret scanning push protection for new repositories.")
    lines.append("- Add or update `main` branch protection on every active repository to require PR reviews, dismiss stale reviews, require status checks, and require CODEOWNER reviews when CODEOWNERS exists.")
    lines.append("- Add CODEOWNERS files for repositories that lack one, then enable required code-owner reviews in branch protection.")
    lines.append("- Review visible org owners and repo admins, document why each admin is essential, and remove elevated access where it is not required.")
    lines.append("- Keep outside collaborators at zero where possible; if any are added, document scope, owner, justification, and expiration.")
    lines.append("- Re-run `python3 scripts/audit_org_security.py --org Aradotso --output docs/security/org-security-audit-$(date +%F).md` after remediation to verify closure.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit GitHub organization security settings")
    parser.add_argument("--org", default="Aradotso", help="GitHub organization login")
    parser.add_argument("--output", default=None, help="Markdown report output path")
    parser.add_argument("--json-output", default=None, help="Optional raw JSON output path")
    args = parser.parse_args()

    data = audit(args.org)
    markdown = render_markdown(data)

    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8")
        print(f"Wrote {path}")
    else:
        print(markdown)

    if args.json_output:
        path = Path(args.json_output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"Wrote {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
