# Contributing to Ara

Thanks for contributing. This document covers the conventions we follow across the Ara org.

## Brand and design

Before producing UI copy, visuals, or marketing materials, read [BRAND_GUIDELINES.md](./BRAND_GUIDELINES.md). It covers the color palette, typography, logo usage rules, tone of voice, and imagery style.

## Code conventions

- Use the language and framework already present in the package you are editing.
- Keep commits atomic: one logical change per commit.
- Write commit messages in the imperative present tense: "Add X", "Fix Y", "Remove Z".
- Prefix commits with the component or package they touch, e.g. `(AraDesktop) Fix scroll jitter` or `(AraWeb) Add rate-limit header`.

## Pull requests

- Branch from `main`. Name branches `fix/`, `feat/`, or `chore/` followed by a short slug.
- Write a one-line summary in the PR title, then a short description of what changed and how to verify it.
- Keep PRs small and reviewable. If a change is large, split it.

## Questions

Open an issue or reach out in the internal Slack. Do not guess at design or architecture decisions — ask first.
