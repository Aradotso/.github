# Aradotso GitHub security baseline audit

Generated: 2026-06-12T11:23:16+00:00
Organization: `Aradotso`

## Scope and assumptions

- Audited all non-archived repositories visible to the authenticated GitHub CLI account.
- Treated the default branch as the branch that must be protected; all visible active repos currently use `main` except repos that explicitly report another default branch.
- The audit is read-only. It records gaps and recommended follow-up work instead of mutating org/repo security settings directly.
- Org-wide secret scanning and code-security policy support depends on GitHub API visibility for the authenticated account; repo-level secret scanning was checked where the API exposed it.

## Executive summary

- Repositories visible: 35 total, 34 active, 1 archived/skipped.
- Repositories with one or more gaps: 34.
- Org admin list visible: pass.
- Org member count visible: 2.
- Org code-security configurations visible: pass.

## Org admin access

Visible org admins:

- `adisinghstudent`
- `svemyh`

Gap criterion: confirm each listed admin is still essential and document the owner/justification in an access review issue.

## Org-wide secret scanning / code security

Visible code-security configurations: 1.
- `GitHub recommended` target `global`, default for new repos: `None`

Gap criterion: ensure a configuration with secret scanning, push protection, and Dependabot security updates applies by default to all new repos and is attached to all active repos.

## Repository gaps

### Aradotso/.github

URL: https://github.com/Aradotso/.github
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/ai-agent-skills

URL: https://github.com/Aradotso/ai-agent-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/App

URL: https://github.com/Aradotso/App
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/Ara

URL: https://github.com/Aradotso/Ara
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/Ara-backend

URL: https://github.com/Aradotso/Ara-backend
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/ara-cua

URL: https://github.com/Aradotso/ara-cua
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/ara-drive

URL: https://github.com/Aradotso/ara-drive
Default branch: `master`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/ara-examples

URL: https://github.com/Aradotso/ara-examples
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/ara-plugin

URL: https://github.com/Aradotso/ara-plugin
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/ara-python-sdk

URL: https://github.com/Aradotso/ara-python-sdk
Default branch: `main`
Gaps:
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/ara.engineer

URL: https://github.com/Aradotso/ara.engineer
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/Astack

URL: https://github.com/Aradotso/Astack
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/bmux

URL: https://github.com/Aradotso/bmux
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/claude-code-skills

URL: https://github.com/Aradotso/claude-code-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/clipfarming

URL: https://github.com/Aradotso/clipfarming
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/codex-skills

URL: https://github.com/Aradotso/codex-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/content-tiktok-carousels

URL: https://github.com/Aradotso/content-tiktok-carousels
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/coshot

URL: https://github.com/Aradotso/coshot
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/data-skills

URL: https://github.com/Aradotso/data-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/design-skills

URL: https://github.com/Aradotso/design-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/devtools-skills

URL: https://github.com/Aradotso/devtools-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/email-outreach

URL: https://github.com/Aradotso/email-outreach
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/hermes-skills

URL: https://github.com/Aradotso/hermes-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/hq

URL: https://github.com/Aradotso/hq
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/image.ara.so

URL: https://github.com/Aradotso/image.ara.so
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/marketing-skills

URL: https://github.com/Aradotso/marketing-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/mcp-skills

URL: https://github.com/Aradotso/mcp-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/OpenAra

URL: https://github.com/Aradotso/OpenAra
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- Dependabot security updates are not confirmed enabled

### Aradotso/picoclaw

URL: https://github.com/Aradotso/picoclaw
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/routines

URL: https://github.com/Aradotso/routines
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/security-skills

URL: https://github.com/Aradotso/security-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

### Aradotso/Swift

URL: https://github.com/Aradotso/Swift
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/text.ara.so

URL: https://github.com/Aradotso/text.ara.so
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- secret scanning is not confirmed enabled
- Dependabot security updates are not confirmed enabled

### Aradotso/trending-skills

URL: https://github.com/Aradotso/trending-skills
Default branch: `main`
Gaps:
- default branch is not protected
- PR review is not required
- status checks are not required
- stale PR reviews are not dismissed
- CODEOWNERS reviews are not required
- CODEOWNERS file is missing
- Dependabot security updates are not confirmed enabled

## Outside collaborators

No outside collaborators were visible on active repos.

## Recommended follow-up issues

Tracking issue filed: https://github.com/Aradotso/.github/issues/1

1. Enable/enforce an org default code-security configuration for all active and new repos: secret scanning, push protection, Dependabot alerts, and Dependabot security updates.
2. Apply branch protection to every active default branch with PR review, required status checks, stale-review dismissal, and required CODEOWNERS reviews.
3. Add CODEOWNERS files to repositories missing them and verify branch protection requires CODEOWNERS approval.
4. Run a quarterly org access review for admins and outside collaborators, documenting owner/justification/expiry for every elevated or external access grant.

## Raw machine-readable summary

```json
{
  "admins": [
    "adisinghstudent",
    "svemyh"
  ],
  "admins_available": true,
  "admins_error": null,
  "code_security_configurations": [
    {
      "advanced_security": "enabled",
      "code_scanning_default_setup": "enabled",
      "code_scanning_default_setup_options": null,
      "code_scanning_delegated_alert_dismissal": "not_set",
      "created_at": "2023-12-04T15:58:07Z",
      "dependabot_alerts": "enabled",
      "dependabot_delegated_alert_dismissal": null,
      "dependabot_security_updates": "not_set",
      "dependency_graph": "enabled",
      "dependency_graph_autosubmit_action": "not_set",
      "dependency_graph_autosubmit_action_options": {
        "labeled_runners": false
      },
      "description": "Suggested settings for Dependabot, secret scanning, and code scanning.",
      "enforcement": "unenforced",
      "html_url": "https://github.com/organizations/Aradotso/settings/security_products/configurations/view/17",
      "id": 17,
      "name": "GitHub recommended",
      "private_vulnerability_reporting": "enabled",
      "secret_scanning": "enabled",
      "secret_scanning_delegated_alert_dismissal": "not_set",
      "secret_scanning_delegated_bypass": "not_set",
      "secret_scanning_extended_metadata": "enabled",
      "secret_scanning_generic_secrets": "not_set",
      "secret_scanning_non_provider_patterns": "enabled",
      "secret_scanning_push_protection": "enabled",
      "secret_scanning_validity_checks": "enabled",
      "target_type": "global",
      "updated_at": "2025-03-04T20:57:43Z",
      "url": "https://api.github.com/orgs/Aradotso/code-security/configurations/17"
    }
  ],
  "code_security_configurations_available": true,
  "code_security_configurations_error": null,
  "generated_at": "2026-06-12T11:23:16+00:00",
  "member_count": 2,
  "members_available": true,
  "org": "Aradotso",
  "org_details_available": true,
  "org_security_and_analysis": null,
  "repos": [
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/.github",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/.github"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/ai-agent-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/ai-agent-skills"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/App",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/App"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/Ara",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/Ara"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/Ara-backend",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/Ara-backend"
    },
    {
      "archived": true,
      "default_branch": "main",
      "name": "Aradotso/ara-connectors",
      "private": true,
      "skipped": "archived",
      "url": "https://github.com/Aradotso/ara-connectors"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/ara-cua",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/ara-cua"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "master",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/ara-drive",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/ara-drive"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/ara-examples",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/ara-examples"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/ara-plugin",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/ara-plugin"
    },
    {
      "archived": false,
      "branch_protection": true,
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/ara-python-sdk",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/ara-python-sdk"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/ara.engineer",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/ara.engineer"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/Astack",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/Astack"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/bmux",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/bmux"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/claude-code-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/claude-code-skills"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/clipfarming",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/clipfarming"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/codex-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/codex-skills"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/content-tiktok-carousels",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/content-tiktok-carousels"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/coshot",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/coshot"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/data-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/data-skills"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/design-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/design-skills"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/devtools-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/devtools-skills"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/email-outreach",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/email-outreach"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/hermes-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/hermes-skills"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/hq",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/hq"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/image.ara.so",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/image.ara.so"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/marketing-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/marketing-skills"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/mcp-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/mcp-skills"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": "CODEOWNERS",
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": true,
      "name": "Aradotso/OpenAra",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/OpenAra"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/picoclaw",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/picoclaw"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/routines",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/routines"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/security-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/security-skills"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/Swift",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/Swift"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/text.ara.so",
      "outside_collaborators": [],
      "private": true,
      "push_protection": false,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": false,
      "url": "https://github.com/Aradotso/text.ara.so"
    },
    {
      "archived": false,
      "branch_protection": false,
      "branch_protection_error": "gh: Branch not protected (HTTP 404)",
      "codeowners_path": null,
      "default_branch": "main",
      "dependabot_security_updates": false,
      "dismisses_stale_reviews": false,
      "has_codeowners": false,
      "name": "Aradotso/trending-skills",
      "outside_collaborators": [],
      "private": false,
      "push_protection": true,
      "requires_code_owner_reviews": false,
      "requires_pr_review": false,
      "requires_status_checks": false,
      "secret_scanning": true,
      "url": "https://github.com/Aradotso/trending-skills"
    }
  ]
}
```
