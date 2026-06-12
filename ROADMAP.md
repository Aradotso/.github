# Roadmap — Aradotso

This document tracks where the [Ara](https://ara.so) GitHub org is headed. Items are grouped by time horizon and ordered by their impact on external contributors and org discoverability.

---

## Short-term (next 30 days)

**Expand the org profile**

- Add a _Team_ section to `profile/README.md` with brief bios and GitHub handles for core contributors.
- Embed a tech-stack visualization (shields.io badges or a hand-crafted SVG grid) so visitors can immediately see what we build with.
- Pin the most important public repos so the org landing page surfaces them first.
- Add social preview images to key repos so link-unfurls look polished.

**Contributor on-ramp**

- Publish a root-level `CONTRIBUTING.md` with a quick-start guide, branching conventions, commit-message format, and the PR checklist.
- Add a `CODE_OF_CONDUCT.md` (Contributor Covenant v2 is fine as a base).
- Create an issue template directory (`.github/ISSUE_TEMPLATE/`) with at least a bug report and a feature request template.
- Create a pull-request template (`.github/pull_request_template.md`) that reminds contributors to fill in the test plan and link related issues.

---

## Medium-term (60–90 days)

**GitHub Discussions**

- Enable Discussions on the org's main repos and seed the initial categories: _Announcements_, _Q&A_, _Ideas_, and _Show & Tell_.
- Publish a "Discussions charter" pinned post that explains norms and response-time expectations.

**Workflow automation for new repos**

- Write a reusable GitHub Actions workflow (`org-defaults.yml`) that any new repo can call: branch-protection enforcement, auto-labeler, stale-issue bot, and welcome-bot for first-time contributors.
- Create a repository template (`template-repo`) that ships with the Actions workflow, issue templates, PR template, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md` pre-populated so new repos start right.

**Improved discoverability**

- Add `CODEOWNERS` files to active repos so review assignments are automatic.
- Write an org-level `FUNDING.yml` once a sponsorship/open-source funding channel exists.
- Tag all public repos with consistent topic labels (`ara`, `ai`, `agent`, `macos`, etc.) and audit descriptions for clarity.

---

## Long-term (6+ months)

**Org-wide security policy**

- Publish a `SECURITY.md` in this repo (and mirror it to all major repos) with a responsible-disclosure process, PGP contact, and expected response SLA.
- Enable Dependabot across all repos via org-level settings.
- Set up CodeQL analysis as a required check on all repos that ship production code.
- Document the secret-scanning and branch-protection policies so contributors know the baseline.

**Contributor recognition program**

- Build or adopt a contributor-recognition workflow (e.g., All Contributors bot) that adds contributors to a `CONTRIBUTORS.md` automatically when a PR is merged.
- Publish periodic release notes that credit every contributor by name.
- Create a "Contributor Spotlight" section in the org profile README, rotated monthly.

**Community health metrics**

- Track open/close ratios for issues and PRs, first-response time, and contributor retention using an open-source dashboard (e.g., Cauldron, Orbit, or a custom GitHub Actions report).
- Set public health targets and review them quarterly.

---

## How to contribute to this roadmap

Open an issue with the label `roadmap` and describe the item you want to add or reprioritize. Pull requests against this file are also welcome — see [CONTRIBUTING.md](./CONTRIBUTING.md) for the process.
