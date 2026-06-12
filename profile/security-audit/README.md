# GitHub security baseline audit

This directory contains a read-only audit for the Aradotso GitHub organization security baseline.

## What it checks

- Default branch protection on every visible active repository.
- Required PR review, required status checks, stale review dismissal, and CODEOWNERS review enforcement.
- Repo-level secret scanning visibility and push protection where exposed by the GitHub API.
- Org-level code-security configuration visibility.
- Org admins visible to the authenticated account.
- Outside collaborators visible on active repositories.
- Dependabot automated security fixes for each active repository.

## Run

```bash
python3 profile/security-audit/audit_github_security.py --org Aradotso --output profile/security-audit/SECURITY_BASELINE_AUDIT.md
```

The script requires an authenticated GitHub CLI session with enough org and repo read access to inspect repository protection, collaborators, members, and security settings. It does not mutate GitHub settings.

## Current follow-up

The generated report is checked in at `SECURITY_BASELINE_AUDIT.md`. Remediation is tracked in https://github.com/Aradotso/.github/issues/1.
