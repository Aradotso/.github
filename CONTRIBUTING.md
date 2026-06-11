# Contributing

## Branching

- `main` is always shippable. Never push directly to it.
- Feature branches: `<component>/<short-description>` (e.g. `AraDesktop/notch-resize-fix`).
- Background agent branches: `ara/bg/<uuid>` — opened automatically; do not create these manually.
- Keep branches short-lived. Merge or close within a few days.

## Commit messages

All commits use a folder prefix that matches the monorepo component:

```
(AraDesktop) short description
(AraWeb) short description
(chat.ara.so) short description
(ara.so) short description
(hq) short description
```

Use the imperative mood ("add", "fix", "remove") and keep the subject under 72 characters.

## Background agent rules

- Background agents (`ara/bg/*` branches) run fully headless with no human in the loop.
- Agents must commit partial work and push even if they cannot complete the full task.
- Agents must never push to `main` or open PRs themselves — Ara opens the PR from the pushed branch.
- All agent assumptions must be documented in the commit message.

## Pull request flow

1. Open a PR from your feature branch into `main`.
2. Provide a one-line summary and a short bullet list of changes.
3. Include a "how to test" note so reviewers can verify quickly.
4. At least one approval is required before merging.
5. Squash-merge is preferred to keep `main` history clean.
