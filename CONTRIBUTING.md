# Contributing to Ara

Thanks for helping build Ara. This document covers git flow, branch naming, background agent rules, and the PR review checklist.

## Git flow

`main` is always deployable. All work happens on short-lived topic branches that merge into `main` via pull request.

1. Branch off `main` (or the active feature branch for a stack).
2. Make focused, atomic commits — one logical change per commit.
3. Open a pull request and request review.
4. Squash or rebase before merging; never merge with a merge commit.
5. Delete the branch after merge.

Never push directly to `main` or `master`. Branch protection is enforced.

## Branch naming

| Type | Pattern | Example |
|---|---|---|
| Feature | `feat/<slug>` | `feat/worktree-lazy-create` |
| Bug fix | `fix/<slug>` | `fix/bg-builds-timeouts` |
| Chore / refactor | `chore/<slug>` | `chore/rename-profile-keys` |
| Documentation | `docs/<slug>` | `docs/architecture-overview` |
| Background agent | `ara/bg/<uuid-slug>` | `ara/bg/2bf32847-…` |

Slugs use lowercase letters, numbers, and hyphens only. Keep them short and meaningful.

## Commit messages

Use the imperative mood (`Add`, `Fix`, `Remove`, not `Added`, `Fixed`).
Prefix with the component when the repo is a monorepo: `(AraDesktop)`, `(AraWeb)`, `(AraAPI)`.
If a task was ambiguous, note the assumption in the commit message after a blank line.

Example:
```
(AraDesktop) Add lazy worktree creation on first message

Assumption: worktrees spin up from `main` by default and switch to a
temporary slot only after the first chat message is submitted.
```

## Background agent rules

Background agents run fully headless inside an isolated git worktree. They follow these rules without exception:

- Never push to `main` or `master`.
- Never open a PR with `gh pr create` — Ara opens the PR automatically after the branch is pushed.
- Never ask questions or wait for approval. Make a reasonable assumption and note it in the commit message.
- Commit as you go. Partial work should still be pushed and noted.
- Write PR metadata (title + body) to the temp file path supplied in the task prompt. Use a Python one-liner via `terminal()` — `write_file` is blocked on `/var/folders/…` paths.
- Do not paste reasoning, terminal logs, or the task prompt into the PR body.

## PR review checklist

Before approving a pull request, confirm the following:

**Correctness**
- [ ] The change does what the PR description says.
- [ ] No unintended side effects on adjacent features.
- [ ] Edge cases and error paths are handled.

**Code quality**
- [ ] Naming is clear and consistent with the surrounding code.
- [ ] No dead code, debug output, or temporary hacks left in.
- [ ] No hardcoded secrets, tokens, or environment-specific values.

**Tests**
- [ ] New behavior is covered by tests, or the PR explains why tests are not applicable.
- [ ] Existing tests pass (CI green).

**Documentation**
- [ ] Public APIs, config keys, and non-obvious decisions are documented.
- [ ] `ARCHITECTURE.md` decision log is updated if a significant design choice was made.

**Background agent PRs** (opened by `ara-bot`)
- [ ] Commit messages note any assumptions made.
- [ ] PR body is concise and does not contain task prompt text or terminal output.
- [ ] Changes are scoped to the stated task — no unrelated edits.
