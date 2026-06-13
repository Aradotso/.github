#!/usr/bin/env python3
"""Generate a GitHub organization security baseline audit report.

The script uses the authenticated GitHub CLI and reports inaccessible settings as
unknown/disabled_or_inaccessible instead of over-claiming compliance.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
from pathlib import Path
from typing import Any


CODEOWNERS_PATHS = ["CODEOWNERS", ".github/CODEOWNERS", "docs/CODEOWNERS"]


def run_gh(args: list[str], *, json_output: bool = True) -> tuple[bool, Any, str]:
    proc = subprocess.run(
        ["gh", *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        return False, None, proc.stderr.strip()
    if not json_output:
        return True, proc.stdout, ""
    text = proc.stdout.strip()
    if not text:
        return True, None, ""
    try:
        return True, json.loads(text), ""
    except json.JSONDecodeError as exc:
        return False, None, f"could not parse gh JSON output: {exc}"


def api_json(path: str, *extra: str) -> tuple[bool, Any, str]:
    return run_gh(["api", *extra, path], json_output=True)


def api_ok(path: str) -> bool:
    ok, _, _ = run_gh(["api", "--silent", path], json_output=False)
    return ok


def paginated(path: str) -> list[dict[str, Any]]:
    ok, data, err = api_json(path, "--paginate", "--slurp")
    if not ok:
        raise RuntimeError(f"gh api {path} failed: {err}")
    if data is None:
        return []
    if isinstance(data, list) and data and all(isinstance(page, list) for page in data):
        return [item for page in data for item in page]
    if isinstance(data, list):
        return data
    raise RuntimeError(f"unexpected paginated response for {path}: {type(data).__name__}")


def bool_status(value: Any) -> str:
    if value is True:
        return "enabled"
    if value is False:
        return "disabled"
    return "unknown"


def check_codeowners(org: str, repo: str, default_branch: str) -> dict[str, Any]:
    for path in CODEOWNERS_PATHS:
        ok, data, _ = api_json(f"repos/{org}/{repo}/contents/{path}?ref={default_branch}")
        if ok and isinstance(data, dict) and data.get("path"):
            return {"exists": True, "path": path}
    return {"exists": False, "path": None}


def check_branch_protection(org: str, repo: str, branch: str) -> dict[str, Any]:
    ok, protection, err = api_json(f"repos/{org}/{repo}/branches/{branch}/protection")
    if not ok or not isinstance(protection, dict):
        return {
            "state": "missing_or_inaccessible",
            "requires_pr_review": False,
            "dismisses_stale_reviews": False,
            "requires_code_owner_reviews": False,
            "requires_status_checks": False,
            "error": err or "not available",
        }

    reviews = protection.get("required_pull_request_reviews") or {}
    status_checks = protection.get("required_status_checks") or {}
    contexts = status_checks.get("contexts") or []
    checks = status_checks.get("checks") or []
    requires_status_checks = bool(status_checks and (contexts or checks or status_checks.get("strict") is not None))

    return {
        "state": "enabled",
        "requires_pr_review": bool(reviews),
        "dismisses_stale_reviews": bool(reviews.get("dismiss_stale_reviews")),
        "requires_code_owner_reviews": bool(reviews.get("require_code_owner_reviews")),
        "requires_status_checks": requires_status_checks,
        "error": None,
    }


def check_repo_security(org: str, repo: str) -> dict[str, str]:
    return {
        "dependabot_alerts": "enabled" if api_ok(f"repos/{org}/{repo}/vulnerability-alerts") else "disabled_or_inaccessible",
        "dependabot_security_updates": "enabled" if api_ok(f"repos/{org}/{repo}/automated-security-fixes") else "disabled_or_inaccessible",
    }


def analysis_status(repo: dict[str, Any], key: str) -> str:
    analysis = repo.get("security_and_analysis") or {}
    setting = analysis.get(key) or {}
    status = setting.get("status")
    if status in {"enabled", "disabled"}:
        return status
    return "unknown"


def permission_names(collab: dict[str, Any]) -> list[str]:
    permissions = collab.get("permissions") or {}
    return sorted(name for name, enabled in permissions.items() if enabled)


def check_repo_admins(org: str, repo: str) -> tuple[list[str], str | None]:
    ok, data, err = api_json(f"repos/{org}/{repo}/collaborators?affiliation=direct&permission=admin&per_page=100")
    if not ok or not isinstance(data, list):
        return [], err or "not visible"
    return sorted(item.get("login", "unknown") for item in data), None


def summarize_repo(repo: dict[str, Any], org: str) -> dict[str, Any]:
    name = repo["name"]
    default_branch = repo.get("default_branch") or "main"
    archived = bool(repo.get("archived"))
    branch = check_branch_protection(org, name, default_branch)
    codeowners = check_codeowners(org, name, default_branch)
    security = check_repo_security(org, name)
    security["secret_scanning"] = analysis_status(repo, "secret_scanning")
    security["secret_scanning_push_protection"] = analysis_status(repo, "secret_scanning_push_protection")
    admins, admin_error = check_repo_admins(org, name)

    gaps: list[str] = []
    if default_branch != "main":
        gaps.append(f"default branch is {default_branch}, not main")
    if branch["state"] != "enabled":
        gaps.append("default branch protection missing or inaccessible")
    if not branch["requires_pr_review"]:
        gaps.append("PR review requirement missing")
    if not branch["requires_status_checks"]:
        gaps.append("status checks requirement missing")
    if not branch["dismisses_stale_reviews"]:
        gaps.append("stale review dismissal missing")
    if codeowners["exists"] and not branch["requires_code_owner_reviews"]:
        gaps.append("CODEOWNERS exists but code-owner review is not required")
    if not codeowners["exists"]:
        gaps.append("CODEOWNERS not found")
    if security["dependabot_alerts"] != "enabled":
        gaps.append("Dependabot alerts disabled or inaccessible")
    if security["dependabot_security_updates"] != "enabled":
        gaps.append("Dependabot security updates disabled or inaccessible")
    if security["secret_scanning"] != "enabled":
        gaps.append("secret scanning disabled or unknown")
    if security["secret_scanning_push_protection"] != "enabled":
        gaps.append("secret scanning push protection disabled or unknown")
    if admins:
        gaps.append("direct repo admins require owner review")
    if admin_error:
        gaps.append("repo admin visibility unavailable")

    return {
        "name": name,
        "visibility": repo.get("visibility", "unknown"),
        "archived": archived,
        "default_branch": default_branch,
        "branch_protection": branch,
        "codeowners": codeowners,
        "security": security,
        "direct_admins": admins,
        "direct_admin_error": admin_error,
        "gaps": gaps,
    }


def render_report(org: str, org_settings: dict[str, Any], repos: list[dict[str, Any]], owners: list[str], outside_collaborators: list[dict[str, Any]]) -> str:
    generated = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    active_repos = [repo for repo in repos if not repo["archived"]]
    repos_with_gaps = [repo for repo in active_repos if repo["gaps"]]
    protected = [repo for repo in active_repos if repo["branch_protection"]["state"] == "enabled"]
    pr_reviews = [repo for repo in active_repos if repo["branch_protection"]["requires_pr_review"]]
    status_checks = [repo for repo in active_repos if repo["branch_protection"]["requires_status_checks"]]
    stale = [repo for repo in active_repos if repo["branch_protection"]["dismisses_stale_reviews"]]
    codeowner_review = [repo for repo in active_repos if repo["branch_protection"]["requires_code_owner_reviews"]]
    dependabot_updates = [repo for repo in active_repos if repo["security"]["dependabot_security_updates"] == "enabled"]
    secret_scanning = [repo for repo in active_repos if repo["security"]["secret_scanning"] == "enabled"]
    push_protection = [repo for repo in active_repos if repo["security"]["secret_scanning_push_protection"] == "enabled"]

    lines: list[str] = []
    lines.append(f"# {org} GitHub security baseline audit")
    lines.append("")
    lines.append(f"Generated: {generated}")
    lines.append("")
    lines.append("## Scope and assumptions")
    lines.append("")
    lines.append(f"- Target organization: `{org}`, inferred from the repository remote.")
    lines.append("- Checks use the authenticated GitHub CLI. Settings hidden by token scope or plan restrictions are reported as `unknown` or `disabled_or_inaccessible`.")
    lines.append("- The baseline expects active repositories to use `main`, require PR reviews, require status checks, dismiss stale reviews, enforce CODEOWNERS reviews when CODEOWNERS exists, enable secret scanning/push protection defaults, limit admin access, document outside collaborators, and enable Dependabot security updates.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Repositories checked: {len(repos)} total, {len(active_repos)} active, {len(repos) - len(active_repos)} archived.")
    lines.append(f"- Active repositories with at least one gap: {len(repos_with_gaps)}.")
    lines.append(f"- Active repositories with default-branch protection visible: {len(protected)}/{len(active_repos)}.")
    lines.append(f"- Active repositories requiring PR review: {len(pr_reviews)}/{len(active_repos)}.")
    lines.append(f"- Active repositories requiring status checks: {len(status_checks)}/{len(active_repos)}.")
    lines.append(f"- Active repositories dismissing stale reviews: {len(stale)}/{len(active_repos)}.")
    lines.append(f"- Active repositories requiring CODEOWNERS review: {len(codeowner_review)}/{len(active_repos)}.")
    lines.append(f"- Active repositories with secret scanning visible as enabled: {len(secret_scanning)}/{len(active_repos)}.")
    lines.append(f"- Active repositories with secret scanning push protection visible as enabled: {len(push_protection)}/{len(active_repos)}.")
    lines.append(f"- Active repositories with Dependabot security updates visible as enabled: {len(dependabot_updates)}/{len(active_repos)}.")
    lines.append("")
    lines.append("## Organization security defaults")
    lines.append("")
    org_fields = [
        "advanced_security_enabled_for_new_repositories",
        "dependabot_alerts_enabled_for_new_repositories",
        "dependabot_security_updates_enabled_for_new_repositories",
        "secret_scanning_enabled_for_new_repositories",
        "secret_scanning_push_protection_enabled_for_new_repositories",
    ]
    for field in org_fields:
        lines.append(f"- `{field}`: {bool_status(org_settings.get(field))}.")
    lines.append("")
    lines.append("## Admin access review")
    lines.append("")
    if owners:
        lines.append(f"- Organization owners visible to this token: {', '.join(f'`{owner}`' for owner in owners)}.")
    else:
        lines.append("- Organization owners were not visible to this token; review in GitHub organization settings.")
    repo_admins = [(repo["name"], repo["direct_admins"]) for repo in active_repos if repo["direct_admins"]]
    if repo_admins:
        lines.append("- Direct repository admins requiring owner review:")
        for repo_name, admins in repo_admins:
            lines.append(f"  - `{repo_name}`: {', '.join(f'`{admin}`' for admin in admins)}")
    else:
        lines.append("- No direct repository admins were visible, or visibility was unavailable.")
    lines.append("")
    lines.append("## Outside collaborators")
    lines.append("")
    if outside_collaborators:
        lines.append("- Outside collaborators visible to this token:")
        for collab in outside_collaborators:
            perms = ", ".join(permission_names(collab)) or "unknown permissions"
            lines.append(f"  - `{collab.get('login', 'unknown')}` ({perms})")
    else:
        lines.append("- No outside collaborators were visible to this token. Keep an owner-maintained access register for exceptions.")
    lines.append("")
    lines.append("## Per-repository findings")
    lines.append("")
    for repo in sorted(repos, key=lambda item: item["name"].lower()):
        branch = repo["branch_protection"]
        codeowners = repo["codeowners"]
        security = repo["security"]
        lines.append(f"### `{repo['name']}`")
        lines.append("")
        lines.append(f"- Visibility: {repo['visibility']}; archived: {repo['archived']}; default branch: `{repo['default_branch']}`.")
        lines.append(f"- Branch protection: {branch['state']}; PR reviews: {branch['requires_pr_review']}; status checks: {branch['requires_status_checks']}; dismiss stale reviews: {branch['dismisses_stale_reviews']}; require code-owner reviews: {branch['requires_code_owner_reviews']}.")
        lines.append(f"- CODEOWNERS: {'found at `' + codeowners['path'] + '`' if codeowners['exists'] else 'not found'}.")
        lines.append(f"- Secret scanning: {security['secret_scanning']}; push protection: {security['secret_scanning_push_protection']}.")
        lines.append(f"- Dependabot alerts: {security['dependabot_alerts']}; security updates: {security['dependabot_security_updates']}.")
        if repo["direct_admins"]:
            lines.append(f"- Direct admins: {', '.join(f'`{admin}`' for admin in repo['direct_admins'])}.")
        if repo["direct_admin_error"]:
            lines.append(f"- Direct admin visibility: {repo['direct_admin_error']}.")
        if repo["gaps"]:
            lines.append("- Gaps: " + "; ".join(repo["gaps"]) + ".")
        else:
            lines.append("- Gaps: none detected by this audit.")
        lines.append("")
    lines.append("## Recommended follow-ups")
    lines.append("")
    lines.append("- Enable organization defaults for secret scanning, secret scanning push protection, Dependabot alerts, and Dependabot security updates for new repositories.")
    lines.append("- Apply a ruleset or branch protection template to every active `main` branch requiring PR review, status checks, stale-review dismissal, and CODEOWNERS review where applicable.")
    lines.append("- Add CODEOWNERS to repositories missing it, then require code-owner review in branch protection or rulesets.")
    lines.append("- Review visible org owners, direct repo admins, and outside collaborators; keep a short written access register with business justification and review date.")
    lines.append("- Re-run `python3 scripts/github_org_security_audit.py --org {org}` after remediation and update the tracking issue with the new counts.")
    lines.append("")
    return "\n".join(lines).format(org=org)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--org", required=True, help="GitHub organization login to audit")
    parser.add_argument("--output", default="docs/github-security-audit.md", help="Markdown report path")
    args = parser.parse_args()

    ok, org_settings, err = api_json(f"orgs/{args.org}")
    if not ok or not isinstance(org_settings, dict):
        raise SystemExit(f"Could not read org settings for {args.org}: {err}")

    repos_raw = paginated(f"orgs/{args.org}/repos?per_page=100&type=all")
    owners_raw = paginated(f"orgs/{args.org}/members?role=admin&per_page=100")
    outside_raw = paginated(f"orgs/{args.org}/outside_collaborators?per_page=100")

    repos = [summarize_repo(repo, args.org) for repo in repos_raw]
    owners = sorted(member.get("login", "unknown") for member in owners_raw)
    report = render_report(args.org, org_settings, repos, owners, outside_raw)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"Wrote {output} with {len(repos)} repositories checked.")


if __name__ == "__main__":
    main()
