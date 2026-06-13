# Aradotso organization security audit

Generated: 2026-06-13

## Scope and method

This report was generated with `scripts/audit_org_security.py` using the authenticated GitHub CLI against the `Aradotso` organization. Settings that the current token could not read are reported as `unknown` or `disabled_or_inaccessible` rather than assumed compliant.

## Summary

- Repositories checked: 35
- Repositories with one or more gaps: 35
- Repositories with `main` branch protection visible: 3/35
- Repositories requiring PR review on `main`: 2/35
- Repositories requiring status checks on `main`: 2/35
- Repositories dismissing stale reviews on `main`: 2/35
- Repositories where CODEOWNERS is present and enforced: 0/35
- Repositories with Dependabot security updates enabled: 35/35

## Organization defaults

- `advanced_security_enabled_for_new_repositories`: `no`
- `dependabot_alerts_enabled_for_new_repositories`: `no`
- `dependabot_security_updates_enabled_for_new_repositories`: `no`
- `secret_scanning_enabled_for_new_repositories`: `no`
- `secret_scanning_push_protection_enabled_for_new_repositories`: `no`

Gap: org-level security defaults for new repositories are not fully enabled. Enable Advanced Security where licensed, Dependabot alerts, Dependabot security updates, secret scanning, and secret scanning push protection for new repositories.

## Admin access review

- Org owners visible to the token: `adisinghstudent`, `svemyh`
- Review required: confirm each org owner is essential and protected by strong authentication.

## Outside collaborators

- No outside collaborators visible to the token.

## Existing tracking issues

- [Close GitHub security baseline gaps](https://github.com/Aradotso/.github/issues/1)

## Per-repository findings

### `Aradotso/.github`

- URL: https://github.com/Aradotso/.github
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `yes`
- Requires PR review: `yes`
- Dismisses stale reviews: `yes`
- Requires status checks: `yes`
- Required status checks: `profile-health-check`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - CODEOWNERS missing

### `Aradotso/App`

- URL: https://github.com/Aradotso/App
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/Ara`

- URL: https://github.com/Aradotso/Ara
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/Ara-backend`

- URL: https://github.com/Aradotso/Ara-backend
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/Astack`

- URL: https://github.com/Aradotso/Astack
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/OpenAra`

- URL: https://github.com/Aradotso/OpenAra
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `CODEOWNERS`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS exists but code-owner reviews are not required
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/Swift`

- URL: https://github.com/Aradotso/Swift
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/ai-agent-skills`

- URL: https://github.com/Aradotso/ai-agent-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/ara-connectors`

- URL: https://github.com/Aradotso/ara-connectors
- Private: `yes`; archived: `yes`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/ara-cua`

- URL: https://github.com/Aradotso/ara-cua
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `yes`
- Requires PR review: `yes`
- Dismisses stale reviews: `yes`
- Requires status checks: `yes`
- Required status checks: `AraWeb API, AraWeb ara.so, chat.ara.so, hq`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled

### `Aradotso/ara-drive`

- URL: https://github.com/Aradotso/ara-drive
- Private: `yes`; archived: `no`; default branch: `master`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not found (HTTP 404)`

### `Aradotso/ara-examples`

- URL: https://github.com/Aradotso/ara-examples
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/ara-plugin`

- URL: https://github.com/Aradotso/ara-plugin
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/ara-python-sdk`

- URL: https://github.com/Aradotso/ara-python-sdk
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `yes`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing

### `Aradotso/ara.engineer`

- URL: https://github.com/Aradotso/ara.engineer
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/bmux`

- URL: https://github.com/Aradotso/bmux
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/claude-code-skills`

- URL: https://github.com/Aradotso/claude-code-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/clipfarming`

- URL: https://github.com/Aradotso/clipfarming
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/codex-skills`

- URL: https://github.com/Aradotso/codex-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/content-tiktok-carousels`

- URL: https://github.com/Aradotso/content-tiktok-carousels
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/coshot`

- URL: https://github.com/Aradotso/coshot
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/data-skills`

- URL: https://github.com/Aradotso/data-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/design-skills`

- URL: https://github.com/Aradotso/design-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/devtools-skills`

- URL: https://github.com/Aradotso/devtools-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/email-outreach`

- URL: https://github.com/Aradotso/email-outreach
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/hermes-skills`

- URL: https://github.com/Aradotso/hermes-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/hq`

- URL: https://github.com/Aradotso/hq
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/image.ara.so`

- URL: https://github.com/Aradotso/image.ara.so
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/marketing-skills`

- URL: https://github.com/Aradotso/marketing-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/mcp-skills`

- URL: https://github.com/Aradotso/mcp-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/picoclaw`

- URL: https://github.com/Aradotso/picoclaw
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/routines`

- URL: https://github.com/Aradotso/routines
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/security-skills`

- URL: https://github.com/Aradotso/security-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/text.ara.so`

- URL: https://github.com/Aradotso/text.ara.so
- Private: `yes`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `disabled`
- Secret scanning push protection: `disabled`
- Dependabot alerts: `disabled_or_inaccessible`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
  - Dependabot alerts disabled/inaccessible
  - secret scanning disabled
  - secret scanning push protection disabled
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

### `Aradotso/trending-skills`

- URL: https://github.com/Aradotso/trending-skills
- Private: `no`; archived: `no`; default branch: `main`
- `main` protected: `no`
- Requires PR review: `no`
- Dismisses stale reviews: `no`
- Requires status checks: `no`
- Required status checks: `none`
- CODEOWNERS path: `missing`
- Requires CODEOWNER reviews: `no`
- Secret scanning: `enabled`
- Secret scanning push protection: `enabled`
- Dependabot alerts: `enabled`
- Dependabot security updates: `enabled`
- Repo admin collaborators visible to the token: `adisinghstudent`, `svemyh`
- Gaps:
  - main branch protection missing/inaccessible
  - main does not require PR review
  - main does not require status checks
  - main does not dismiss stale reviews
  - CODEOWNERS missing
- Branch protection read note: `gh: Branch not protected (HTTP 404)`

## Recommended follow-ups

- Enable org defaults for Dependabot alerts, Dependabot security updates, secret scanning, and secret scanning push protection for new repositories.
- Add or update `main` branch protection on every active repository to require PR reviews, dismiss stale reviews, require status checks, and require CODEOWNER reviews when CODEOWNERS exists.
- Add CODEOWNERS files for repositories that lack one, then enable required code-owner reviews in branch protection.
- Review visible org owners and repo admins, document why each admin is essential, and remove elevated access where it is not required.
- Keep outside collaborators at zero where possible; if any are added, document scope, owner, justification, and expiration.
- Re-run `python3 scripts/audit_org_security.py --org Aradotso --output docs/security/org-security-audit-$(date +%F).md` after remediation to verify closure.
