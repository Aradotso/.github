# Org Profile Shipping Status

_Last audited: June 12, 2026_

## What's live on the org profile page (origin/main)

Three human-authored commits have merged:

1. `c967bcc` — Add org profile README (initial sparse version)
2. `4598706` — Reorder profile README and drop tagline
3. `da218fc` — Update org profile header image (hero.png, ~588 KB)

**Live content:** hero banner image, `<h1>Ara</h1>`, link to ara.so, logo mark. No tagline, no social links, no badges, no description.

## Background-agent branch history (never merged)

75 branches were pushed to `origin` under the `ara/bg/c2c734d9-*` and `ara/bg/2bf32847-*` namespaces. None were opened as PRs; GitHub PR history is empty. Themes covered across these branches:

- README rewrites with mission statement, capabilities, and quick links
- YC S26 / Seed / TechCrunch badges
- Social links (X, Blog, Status page)
- CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md
- LICENSE and LEGAL.md
- TECH_STACK.md, ROADMAP.md, issue templates
- Branding assets directory (logos, color tokens, typography)
- CI/CD workflows (profile health-check, image optimization, lint)
- INSTALL.md developer setup guide
- Dark/light theme image variants
- CHANGELOG

**Decision:** All 75 stale branches are superseded by this PR. They overlap heavily and were never reviewed. A single clean commit with the best consolidated content is preferable to cherry-picking across 75 divergent branches.

## This PR

Updates `profile/README.md` to the canonical version: hero image, title, one-line mission, nav links (Website · Docs · Blog · @ara_so), YC S26 badge, and a short description paragraph. Minimal and shippable today; future PRs can layer in branding assets, contributing docs, and CI as needed.
