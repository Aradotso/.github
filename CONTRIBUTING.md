# Contributing to the Ara GitHub profile

This repository owns the public GitHub organization profile shown from `profile/README.md`. Treat it as a generated marketing surface, not as a standalone source of truth: the profile should mirror canonical Ara messaging and assets from `ara.so` or the current internal company docs.

## Profile sync architecture

Profile updates should flow from canonical sources into this repository in a small, reviewable change:

1. Start from the source of truth. Use `ara.so` for public copy, positioning, product links, and active brand assets. Use internal docs for private launch timing, team changes, or messaging decisions that have not been published yet.
2. Translate only the profile-specific subset into `profile/README.md`. Keep the GitHub profile short, centered on Ara, and limited to public-facing links.
3. Copy only approved images into `profile/`. The current layout expects `hero.png` for the top hero image and `logo.png` for the square logo mark.
4. Run the local validation before committing so the rendered profile stays compatible with GitHub's Markdown renderer.
5. Open the change for review and link the canonical source used for the update in the PR body when it is available to reviewers.

When an automated background agent performs this sync, it should follow the documentation patterns from Ara skills such as [`ara-bg-agent-write-repo-docs`](https://github.com/Aradotso/ara-cua/tree/main/.claude/skills/ara-bg-agent-write-repo-docs), [`ara-bg-agent-docs-task`](https://github.com/Aradotso/ara-cua/tree/main/.claude/skills/ara-bg-agent-docs-task), and [`ara-bg-agent-coding-task`](https://github.com/Aradotso/ara-cua/tree/main/.claude/skills/ara-bg-agent-coding-task). Those skills are the right place to look for repeatable repo-doc structure, commit hygiene, profile-maintenance patterns, and how to preserve the source-of-truth trail in PR notes.

## Health-check validation rules

Profile health checks should fail fast on issues that would make the public org profile stale, broken, or visually inconsistent:

- Logo size: `profile/logo.png` must be a PNG and exactly `512x512`. The README renders it at `120px`, but the source asset should remain high-resolution and square.
- Hero size: `profile/hero.png` must be a PNG and at least `1200x600` so it renders crisply on GitHub.
- Required social links: `profile/README.md` must include `https://www.ara.so`, and every profile link must be an absolute `https://` URL.
- Markdown linting: the README must end with a newline, avoid trailing whitespace, keep exactly one centered `<h1>`, and reference both `./hero.png` and `./logo.png`.
- Public-only content: do not include private docs, launch plans, non-public teammate details, or links that require authentication.

## Run validation locally

Run the bundled validator from the repository root:

```sh
python3 scripts/validate-profile.py
```

For an extra Markdown pass, run a Markdown linter if you have one installed:

```sh
npx --yes markdownlint-cli2 "README.md" "profile/README.md" "CONTRIBUTING.md"
```

The Python validator has no third-party dependencies and is the minimum required local check before committing profile changes.

## CI/CD and approval flow

This repository is intentionally small, so the release flow is review-first:

1. Create changes on a feature or background-agent branch. Do not push directly to `main`.
2. Run `python3 scripts/validate-profile.py` locally and include the result in the PR testing notes.
3. CI should run the same validator and any configured Markdown lint checks on every PR.
4. A human reviewer verifies the profile still matches the canonical source, the linked source is appropriate to share with reviewers, and the assets are approved for public use.
5. After approval and merge to `main`, GitHub automatically serves the updated `profile/README.md` as the organization profile.

For background-agent branches, the agent should push the branch only. Ara's PR automation opens the pull request with the agent-provided title and body, and reviewers approve before merge.

## Common profile updates

### New team member

Use internal docs as the source of truth for names, roles, and timing. Only add a teammate if the profile intentionally lists people publicly. Prefer linking to public pages or leaving the profile company-focused if the canonical public site does not expose the team change yet.

Validation checklist:

- The person and role are approved for public display.
- Any link is an absolute `https://` URL.
- The README still stays short enough for a GitHub org profile.

### New logo

Export the approved logo mark as `profile/logo.png` at exactly `512x512`. If the hero also changes, export it as `profile/hero.png` at `1200x600` or larger. Keep the README references unchanged unless the file names intentionally change and the validator is updated in the same PR.

Validation checklist:

- `python3 scripts/validate-profile.py` passes.
- The logo remains legible when rendered at `width="120"`.
- The asset source is noted in the PR body.

### Messaging refresh

Start from `ara.so` or the approved internal messaging doc. Update the profile copy with the smallest public-facing version of the new message rather than copying long-form web sections. Keep the primary link pointed at `https://www.ara.so` unless the canonical call to action changes.

Validation checklist:

- The profile copy matches the canonical source's current positioning.
- No private roadmap, customer, investor, or launch information was copied into the public README.
- Markdown and link validation pass locally.
