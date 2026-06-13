# Aradotso GitHub security baseline audit

Generated: 2026-06-13 09:55 UTC

## Scope and assumptions

- Target organization: `Aradotso`, inferred from the repository remote.
- Checks use the authenticated GitHub CLI. Settings hidden by token scope or plan restrictions are reported as `unknown` or `disabled_or_inaccessible`.
- The baseline expects active repositories to use `main`, require PR reviews, require status checks, dismiss stale reviews, enforce CODEOWNERS reviews when CODEOWNERS exists, enable secret scanning/push protection defaults, limit admin access, document outside collaborators, and enable Dependabot security updates.

## Summary

- Repositories checked: 35 total, 34 active, 1 archived.
- Active repositories with at least one gap: 34.
- Active repositories with default-branch protection visible: 1/34.
- Active repositories requiring PR review: 0/34.
- Active repositories requiring status checks: 0/34.
- Active repositories dismissing stale reviews: 0/34.
- Active repositories requiring CODEOWNERS review: 0/34.
- Active repositories with secret scanning visible as enabled: 16/34.
- Active repositories with secret scanning push protection visible as enabled: 16/34.
- Active repositories with Dependabot security updates visible as enabled: 34/34.

## Organization security defaults

- `advanced_security_enabled_for_new_repositories`: disabled.
- `dependabot_alerts_enabled_for_new_repositories`: disabled.
- `dependabot_security_updates_enabled_for_new_repositories`: disabled.
- `secret_scanning_enabled_for_new_repositories`: disabled.
- `secret_scanning_push_protection_enabled_for_new_repositories`: disabled.

## Admin access review

- Organization owners visible to this token: `adisinghstudent`, `svemyh`.
- Direct repository admins requiring owner review:
  - `clipfarming`: `svemyh`

## Outside collaborators

- No outside collaborators were visible to this token. Keep an owner-maintained access register for exceptions.

## Per-repository findings

### `.github`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `ai-agent-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `App`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `Ara`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `Ara-backend`

- Visibility: internal; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `ara-connectors`

- Visibility: private; archived: True; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `ara-cua`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `ara-drive`

- Visibility: private; archived: False; default branch: `master`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch is master, not main; default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `ara-examples`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `ara-plugin`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `ara-python-sdk`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: enabled; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `ara.engineer`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `Astack`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `bmux`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `claude-code-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `clipfarming`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Direct admins: `svemyh`.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown; direct repo admins require owner review.

### `codex-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `content-tiktok-carousels`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `coshot`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `data-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `design-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `devtools-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `email-outreach`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `hermes-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `hq`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `image.ara.so`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `marketing-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `mcp-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `OpenAra`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: found at `CODEOWNERS`.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS exists but code-owner review is not required.

### `picoclaw`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `routines`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `security-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

### `Swift`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `text.ara.so`

- Visibility: private; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: disabled; push protection: disabled.
- Dependabot alerts: disabled_or_inaccessible; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found; Dependabot alerts disabled or inaccessible; secret scanning disabled or unknown; secret scanning push protection disabled or unknown.

### `trending-skills`

- Visibility: public; archived: False; default branch: `main`.
- Branch protection: missing_or_inaccessible; PR reviews: False; status checks: False; dismiss stale reviews: False; require code-owner reviews: False.
- CODEOWNERS: not found.
- Secret scanning: enabled; push protection: enabled.
- Dependabot alerts: enabled; security updates: enabled.
- Gaps: default branch protection missing or inaccessible; PR review requirement missing; status checks requirement missing; stale review dismissal missing; CODEOWNERS not found.

## Recommended follow-ups

- Enable organization defaults for secret scanning, secret scanning push protection, Dependabot alerts, and Dependabot security updates for new repositories.
- Apply a ruleset or branch protection template to every active `main` branch requiring PR review, status checks, stale-review dismissal, and CODEOWNERS review where applicable.
- Add CODEOWNERS to repositories missing it, then require code-owner review in branch protection or rulesets.
- Review visible org owners, direct repo admins, and outside collaborators; keep a short written access register with business justification and review date.
- Re-run `python3 scripts/github_org_security_audit.py --org Aradotso` after remediation and update the tracking issue with the new counts.
