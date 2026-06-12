#!/usr/bin/env python3
"""Audit baseline GitHub security settings for an organization.

This script uses the authenticated GitHub CLI (`gh`) instead of storing tokens.
It is read-only: it generates a Markdown report with gaps and recommended
follow-up issues/PRs, but does not mutate org or repository settings.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class ApiResult:
    ok: bool
    data: Any = None
    error: str | None = None


def gh_json(args: list[str], *, allow_error: bool = True) -> ApiResult:
    proc = subprocess.run(
        ["gh", *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        if allow_error:
            return ApiResult(False, error=proc.stderr.strip() or proc.stdout.strip())
        print(proc.stderr or proc.stdout, file=sys.stderr)
        raise SystemExit(proc.returncode)
    out = proc.stdout.strip()
    if not out:
        return ApiResult(True, data=None)
    try:
        return ApiResult(True, data=json.loads(out))
    except json.JSONDecodeError as exc:
        if allow_error:
            return ApiResult(False, error=f"JSON decode failed: {exc}")
        raise


def gh_api(path: str, *, paginate: bool = False) -> ApiResult:
    args = ["api", path, "--jq", "."]
    if paginate:
        args.insert(2, "--paginate")
    return gh_json(args)


def status(value: bool | None) -> str:
    if value is True:
        return "pass"
    if value is False:
        return "gap"
    return "unknown"


def bool_from_status(obj: dict[str, Any] | None, key: str) -> bool | None:
    if not isinstance(obj, dict):
        return None
    value = obj.get(key)
    if isinstance(value, dict):
        raw = value.get("status")
        if raw == "enabled":
            return True
        if raw == "disabled":
            return False
    return None


def fetch_all_repos(org: str) -> list[dict[str, Any]]:
    result = gh_json([
        "repo",
        "list",
        org,
        "--limit",
        "1000",
        "--json",
        "name,nameWithOwner,isArchived,isPrivate,defaultBranchRef,url",
    ], allow_error=False)
    repos = result.data or []
    return sorted(repos, key=lambda repo: repo["nameWithOwner"].lower())


def get_codeowners(owner: str, repo: str, branch: str) -> tuple[bool, str | None]:
    for candidate in (".github/CODEOWNERS", "CODEOWNERS", "docs/CODEOWNERS"):
        res = gh_api(f"repos/{owner}/{repo}/contents/{candidate}?ref={branch}")
        if res.ok:
            return True, candidate
    return False, None


def audit_repo(owner: str, repo: dict[str, Any]) -> dict[str, Any]:
    name = repo["name"]
    branch_ref = repo.get("defaultBranchRef") or {}
    branch = branch_ref.get("name")
    row: dict[str, Any] = {
        "name": repo["nameWithOwner"],
        "url": repo["url"],
        "private": repo["isPrivate"],
        "archived": repo["isArchived"],
        "default_branch": branch,
    }

    if repo.get("isArchived"):
        row["skipped"] = "archived"
        return row
    if not branch:
        row["skipped"] = "no default branch"
        return row

    protection = gh_api(f"repos/{owner}/{name}/branches/{branch}/protection")
    if protection.ok and isinstance(protection.data, dict):
        data = protection.data
        reviews = data.get("required_pull_request_reviews") or {}
        status_checks = data.get("required_status_checks") or {}
        row["branch_protection"] = True
        row["requires_pr_review"] = bool((reviews.get("required_approving_review_count") or 0) >= 1)
        row["dismisses_stale_reviews"] = bool(reviews.get("dismiss_stale_reviews"))
        row["requires_code_owner_reviews"] = bool(reviews.get("require_code_owner_reviews"))
        contexts = status_checks.get("contexts") or []
        checks = status_checks.get("checks") or []
        row["requires_status_checks"] = bool(status_checks and (contexts or checks))
    else:
        row["branch_protection"] = False
        row["requires_pr_review"] = False
        row["dismisses_stale_reviews"] = False
        row["requires_code_owner_reviews"] = False
        row["requires_status_checks"] = False
        row["branch_protection_error"] = protection.error

    repo_details = gh_api(f"repos/{owner}/{name}")
    security = (repo_details.data or {}).get("security_and_analysis") if repo_details.ok else None
    row["secret_scanning"] = bool_from_status(security, "secret_scanning")
    row["push_protection"] = bool_from_status(security, "secret_scanning_push_protection")

    autofix = gh_api(f"repos/{owner}/{name}/automated-security-fixes")
    if autofix.ok and isinstance(autofix.data, dict):
        row["dependabot_security_updates"] = bool(autofix.data.get("enabled"))
    else:
        row["dependabot_security_updates"] = None
        row["dependabot_error"] = autofix.error

    has_codeowners, codeowners_path = get_codeowners(owner, name, branch)
    row["has_codeowners"] = has_codeowners
    row["codeowners_path"] = codeowners_path

    outside = gh_api(f"repos/{owner}/{name}/collaborators?affiliation=outside", paginate=True)
    if outside.ok and isinstance(outside.data, list):
        row["outside_collaborators"] = sorted(c.get("login") for c in outside.data if c.get("login"))
    else:
        row["outside_collaborators"] = None
        row["outside_collaborators_error"] = outside.error

    return row


def audit_org(org: str) -> dict[str, Any]:
    admins = gh_api(f"orgs/{org}/members?role=admin&per_page=100", paginate=True)
    members = gh_api(f"orgs/{org}/members?per_page=100", paginate=True)
    org_details = gh_api(f"orgs/{org}")
    code_security_configs = gh_api(f"orgs/{org}/code-security/configurations?per_page=100", paginate=True)

    repos = fetch_all_repos(org)
    audited_repos = [audit_repo(org, repo) for repo in repos]

    return {
        "org": org,
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "org_details_available": org_details.ok,
        "org_security_and_analysis": (org_details.data or {}).get("security_and_analysis") if org_details.ok else None,
        "code_security_configurations_available": code_security_configs.ok,
        "code_security_configurations": code_security_configs.data if code_security_configs.ok else None,
        "code_security_configurations_error": code_security_configs.error if not code_security_configs.ok else None,
        "admins_available": admins.ok,
        "admins": sorted(m.get("login") for m in (admins.data or []) if m.get("login")) if admins.ok else None,
        "admins_error": admins.error if not admins.ok else None,
        "members_available": members.ok,
        "member_count": len(members.data or []) if members.ok else None,
        "repos": audited_repos,
    }


def repo_gaps(row: dict[str, Any]) -> list[str]:
    if row.get("skipped"):
        return []
    checks = [
        ("branch_protection", "default branch is not protected"),
        ("requires_pr_review", "PR review is not required"),
        ("requires_status_checks", "status checks are not required"),
        ("dismisses_stale_reviews", "stale PR reviews are not dismissed"),
        ("requires_code_owner_reviews", "CODEOWNERS reviews are not required"),
        ("has_codeowners", "CODEOWNERS file is missing"),
    ]
    gaps = [message for key, message in checks if row.get(key) is not True]
    if row.get("secret_scanning") is not True:
        gaps.append("secret scanning is not confirmed enabled")
    if row.get("dependabot_security_updates") is not True:
        gaps.append("Dependabot security updates are not confirmed enabled")
    outside = row.get("outside_collaborators")
    if outside:
        gaps.append(f"outside collaborators present: {', '.join(outside)}")
    return gaps


def render_report(audit: dict[str, Any]) -> str:
    repos = audit["repos"]
    active = [repo for repo in repos if not repo.get("skipped")]
    rows_with_gaps = [(repo, repo_gaps(repo)) for repo in active]
    rows_with_gaps = [(repo, gaps) for repo, gaps in rows_with_gaps if gaps]

    lines = [
        "# Aradotso GitHub security baseline audit",
        "",
        f"Generated: {audit['generated_at']}",
        f"Organization: `{audit['org']}`",
        "",
        "## Scope and assumptions",
        "",
        "- Audited all non-archived repositories visible to the authenticated GitHub CLI account.",
        "- Treated the default branch as the branch that must be protected; all visible active repos currently use `main` except repos that explicitly report another default branch.",
        "- The audit is read-only. It records gaps and recommended follow-up work instead of mutating org/repo security settings directly.",
        "- Org-wide secret scanning and code-security policy support depends on GitHub API visibility for the authenticated account; repo-level secret scanning was checked where the API exposed it.",
        "",
        "## Executive summary",
        "",
        f"- Repositories visible: {len(repos)} total, {len(active)} active, {len(repos) - len(active)} archived/skipped.",
        f"- Repositories with one or more gaps: {len(rows_with_gaps)}.",
        f"- Org admin list visible: {status(audit.get('admins_available'))}.",
        f"- Org member count visible: {audit.get('member_count') if audit.get('members_available') else 'unknown'}.",
        f"- Org code-security configurations visible: {status(audit.get('code_security_configurations_available'))}.",
        "",
    ]

    if audit.get("admins") is not None:
        lines.extend([
            "## Org admin access",
            "",
            "Visible org admins:",
            "",
            *[f"- `{admin}`" for admin in audit["admins"]],
            "",
            "Gap criterion: confirm each listed admin is still essential and document the owner/justification in an access review issue.",
            "",
        ])
    else:
        lines.extend([
            "## Org admin access",
            "",
            f"Could not list org admins: {audit.get('admins_error') or 'unknown API error'}",
            "",
        ])

    if audit.get("code_security_configurations_available"):
        configs = audit.get("code_security_configurations") or []
        lines.extend([
            "## Org-wide secret scanning / code security",
            "",
            f"Visible code-security configurations: {len(configs)}.",
        ])
        for config in configs:
            name = config.get("name", "unnamed")
            target = config.get("target_type", "unknown target")
            default_for_new = config.get("default_for_new_repos")
            lines.append(f"- `{name}` target `{target}`, default for new repos: `{default_for_new}`")
        lines.extend([
            "",
            "Gap criterion: ensure a configuration with secret scanning, push protection, and Dependabot security updates applies by default to all new repos and is attached to all active repos.",
            "",
        ])
    else:
        lines.extend([
            "## Org-wide secret scanning / code security",
            "",
            "The code-security configuration API was not visible to this token, so org-wide enforcement could not be conclusively verified.",
            f"API response: {audit.get('code_security_configurations_error') or 'unknown error'}",
            "",
            "Gap: perform an owner-level check in GitHub org settings and enable a default code-security configuration if missing.",
            "",
        ])

    lines.extend([
        "## Repository gaps",
        "",
    ])
    if not rows_with_gaps:
        lines.append("No repository-level gaps found.")
    else:
        for repo, gaps in rows_with_gaps:
            lines.extend([
                f"### {repo['name']}",
                "",
                f"URL: {repo['url']}",
                f"Default branch: `{repo.get('default_branch')}`",
                "Gaps:",
                *[f"- {gap}" for gap in gaps],
                "",
            ])

    outside_rows = [repo for repo in active if repo.get("outside_collaborators")]
    lines.extend([
        "## Outside collaborators",
        "",
    ])
    if outside_rows:
        for repo in outside_rows:
            people = ", ".join(f"`{login}`" for login in repo["outside_collaborators"])
            lines.append(f"- {repo['name']}: {people}")
        lines.extend([
            "",
            "Gap criterion: document business owner, repo scope, expiration date, and access level for each outside collaborator.",
            "",
        ])
    else:
        lines.extend(["No outside collaborators were visible on active repos.", ""])

    lines.extend([
        "## Recommended follow-up issues",
        "",
        "1. Enable/enforce an org default code-security configuration for all active and new repos: secret scanning, push protection, Dependabot alerts, and Dependabot security updates.",
        "2. Apply branch protection to every active default branch with PR review, required status checks, stale-review dismissal, and required CODEOWNERS reviews.",
        "3. Add CODEOWNERS files to repositories missing them and verify branch protection requires CODEOWNERS approval.",
        "4. Run a quarterly org access review for admins and outside collaborators, documenting owner/justification/expiry for every elevated or external access grant.",
        "",
        "## Raw machine-readable summary",
        "",
        "```json",
        json.dumps(audit, indent=2, sort_keys=True),
        "```",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--org", default="Aradotso")
    parser.add_argument("--output", default="profile/security-audit/SECURITY_BASELINE_AUDIT.md")
    args = parser.parse_args()

    audit = audit_org(args.org)
    report = render_report(audit)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
