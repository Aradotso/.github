# Org security audit

Generated: 2026-06-13 08:23 UTC
Organization: `Aradotso`
Plan: `enterprise`

## Summary

- Repositories audited: 35 (34 active, 1 archived)
- Active repositories with gaps: 34
- Org owners visible to this audit: 2
- Outside collaborators visible to this audit: 0

## Org-level security settings

- Advanced Security enabled for new repositories: `False`
- Dependabot alerts enabled for new repositories: `False`
- Dependabot security updates enabled for new repositories: `False`
- Secret scanning enabled for new repositories: `False`
- Secret scanning push protection enabled for new repositories: `False`

Gap: secret scanning is not enabled org-wide for new repositories, or the setting was not exposed by the API token used for this audit.
Gap: secret-scanning push protection is not enabled org-wide for new repositories, or the setting was not exposed by the API token used for this audit.
Gap: Dependabot security updates are not enabled org-wide for new repositories, or the setting was not exposed by the API token used for this audit.

## Admin access review

Org owners visible to the auditing token:
- `adisinghstudent`
- `svemyh`

Gap: this audit can identify org owners and repo admins, but it cannot determine which humans are essential without a maintained access roster. Create or link an owner/admin access roster and review it quarterly.

## Outside collaborators

No outside collaborators were visible to the auditing token.

## Repository findings

### `.github`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `ai-agent-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `App`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `Ara`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `Ara-backend`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `ara-connectors`

- Private: yes
- Archived: yes
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps: none found by this audit

### `ara-cua`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `ara-drive`

- Private: yes
- Archived: no
- Default branch: `master`
- Main branch protection: `not audited: default branch is master`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - default branch is not `main`; manual branch-protection review needed
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `ara-examples`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor

### `ara-plugin`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor

### `ara-python-sdk`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `enabled`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - branch protection does not require PR review
  - branch protection does not require status checks
  - branch protection does not dismiss stale reviews
  - CODEOWNERS file not found on default branch

### `ara.engineer`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `Astack`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor

### `bmux`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `claude-code-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `clipfarming`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: `svemyh`
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `codex-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `content-tiktok-carousels`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `coshot`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `data-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `design-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `devtools-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `email-outreach`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `hermes-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `hq`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `image.ara.so`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `marketing-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `mcp-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `OpenAra`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `CODEOWNERS`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `picoclaw`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `routines`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `security-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

### `Swift`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `text.ara.so`

- Private: yes
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `disabled`
- Secret-scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing
  - secret scanning is not enabled or was not visible to the auditor
  - secret-scanning push protection is not enabled or was not visible to the auditor
  - Dependabot alerts are disabled or inaccessible

### `trending-skills`

- Private: no
- Archived: no
- Default branch: `main`
- Main branch protection: `missing`
- Requires PR review: no (0 approvals)
- Requires status checks: no (0 checks)
- Dismisses stale reviews: no
- CODEOWNERS file: `not found`
- Requires code-owner review: no
- Secret scanning: `enabled`
- Secret-scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Admin teams: none visible
- Direct admin users: none visible
- Gaps:
  - `main` branch protection is missing

## Recommended follow-ups

- Enable org-wide secret scanning, push protection, Dependabot alerts, and Dependabot security updates for new repositories in GitHub organization security settings.
- Apply a repository ruleset or branch protection template to every active repository with `main`: require PR review, status checks, stale-review dismissal, and CODEOWNERS review where a CODEOWNERS file exists.
- Add CODEOWNERS files where ownership is missing, then require code-owner review in branch protection/rulesets.
- Create or update an access roster covering org owners, repo admins, and outside collaborators with owner, reason, and review/expiration date.
- Re-run `python3 scripts/audit-org-security.py` after settings changes and commit the refreshed report.
