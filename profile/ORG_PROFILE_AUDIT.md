# Aradotso/.github — Org Profile Audit

**Date:** 2026-06-12  
**Auditor:** Ara background agent

---

## What is Live on main

`main` has 3 commits. The live org profile page shows:

- Hero banner image (`profile/hero.png`)
- "Ara" heading (centered)
- Single link: `ara.so`
- Secondary logo image (`profile/logo.png`, 120px)

That's it. No mission statement, no social links, no download CTA, no badges, no CONTRIBUTING, SECURITY, or CODE_OF_CONDUCT files at the repo root. The profile is effectively a bare placeholder.

---

## What is in Stale Background-Agent Branches (Never Merged)

There are **115 remote branches** — all `ara/bg/*` — and **0 open or merged PRs** in this repo. Every background-agent task that touched the org profile pushed a branch but Ara never opened a PR for any of them. None of the work reached main.

Grouping the stale branch content by theme:

### Profile README improvements (60+ branches)
Multiple agents wrote enhanced versions of `profile/README.md` with:
- Mission statement ("The agent-building agent. Design, run, and refine automated agents on your Mac.")
- Social links: X/Twitter, LinkedIn, GitHub Discussions
- Quick-links bar: Website · Download · Docs · Blog · Status
- YC S26 badge
- Founding story blurb (Sven + Adi, backed by YC)
- Download CTA ("Download for free →")

Best consolidated version: `ara/bg/c2c734d9-cf03-4d29-8d87-68fa521b-eacae4` (the prior audit branch from 2026-06-11).

### Branding assets (8+ branches)
- `branding/` directory with multi-size PNGs (16–512px), SVG icon, wordmark SVGs
- `profile/logo-dark.png` + `profile/logo-light.png` for GitHub theme-aware `<picture>` element
- `branding/BRAND.md` style guide and `tokens.css`

Best version: `ara/bg/c2c734d9-cf03-4d29-8d87-68fa521b-3a3265` (the prior sync branch from 2026-06-11).

### Root docs (CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, CHANGELOG) — multiple branches
- `CONTRIBUTING.md`: PR process, commit conventions, changelog requirement
- `SECURITY.md`: responsible disclosure to security@ara.so, 90-day window
- `CODE_OF_CONDUCT.md`: Contributor Covenant v2.1 (conduct@ara.so)
- `CHANGELOG.md`: Keep a Changelog format

### CI / automation (5+ branches)
- GitHub Actions workflows for profile health-check and README validation
- Node.js CI template, automated asset optimization scripts

### Other docs (multiple branches each)
- `ROADMAP.md` with issue templates and label definitions
- `TECH_STACK.md`
- `INSTALL.md` / developer setup guide
- `LEGAL.md` + `LICENSE`

---

## Assessment

### What should be merged
The most impactful and lowest-risk change is the **profile README upgrade**. It adds mission statement, social links, download CTA, and YC badge — none of which require binary assets. This alone makes the org profile page materially more useful to anyone who lands on it.

The **root community docs** (CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, CHANGELOG) are standard GitHub org hygiene and should land with the profile update.

### What is deferred
Binary branding assets (logo variants, multi-size PNGs, SVGs) are additive and correct but add bulk. They can come in a follow-up PR once the text content is live.

CI/automation workflows also belong in a separate PR — they need review before running on the org.

### Stale branch verdict: close all 115
Every branch is a 1-commit snapshot. There is no incremental work to salvage — the best content has been cherry-picked into this audit. Recommended action: bulk-delete all `ara/bg/*` branches after this PR merges.

---

## Recommended Next PRs

1. **This PR** — profile README + community docs (CONTRIBUTING, SECURITY, COC, CHANGELOG)
2. Branding assets: `branding/` directory, theme-aware logo, hi-DPI hero
3. CI: profile health-check workflow
4. Bulk branch cleanup: delete all 115 `ara/bg/*` branches
