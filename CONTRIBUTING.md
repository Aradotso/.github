# Contributing to Ara

## Branching

- `main` is the stable trunk. Never push directly to `main`.
- Feature branches: `feat/<short-description>`
- Bug fixes: `fix/<short-description>`
- Background agent branches: `ara/bg/<task-id>` (auto-created by the Ara agent runtime; do not create these manually)

## Background Agent Rules

Background agents run headless inside isolated git worktrees. They must:

1. Never ask questions or wait for human input.
2. Make all changes directly in their assigned worktree.
3. Commit atomically with clear messages using the relevant package prefix, e.g. `(AraDesktop)`, `(api)`, `(chat)`, `(hq)`, `(supabase)`.
4. Push their branch (`git push -u origin HEAD`) when done.
5. Write a PR title and body to the temp file provided by the runtime — Ara opens the PR on their behalf.
6. Never open a PR themselves (`gh pr create` is off-limits for background agents).
7. Never push to `main` or `master`.

## PR Flow

1. Push a feature/fix branch.
2. Open a pull request into `main` with a concise title and a body that lists what changed and how to verify it.
3. Request review from a relevant owner.
4. Squash-merge once approved; delete the branch.

## Commit Style

Use a package prefix in parentheses followed by a short imperative sentence:

```
(AraDesktop) Fix window focus after agent handoff
(api) Add /v1/agents POST endpoint
(chat) Render streaming tool-call deltas inline
```
