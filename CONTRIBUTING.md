# Contributing to Ara

Thanks for contributing. This document covers the git workflow, branch naming conventions, background agent rules, and the PR review checklist.

## Git workflow

Ara uses a trunk-based flow with short-lived feature branches off `main`.

1. Fork or clone the relevant repository.
2. Create a branch from `main` (see naming below).
3. Make focused, atomic commits. One logical change per commit.
4. Push your branch and open a pull request against `main`.
5. A reviewer approves and merges. Merges to `main` are squash-merged.

Avoid long-lived branches. If work spans more than a few days, rebase onto `main` regularly to keep the diff small.

## Branch naming

All branches follow this pattern:

```
<type>/<short-description>
```

Common types:

- `feat/` — new feature or behaviour
- `fix/` — bug fix
- `chore/` — tooling, dependency updates, CI changes
- `docs/` — documentation only
- `refactor/` — code restructuring with no behaviour change
- `test/` — test additions or fixes

Background agents use the reserved namespace `ara/bg/<task-id>`. Never create branches under `ara/bg/` manually.

Examples:

```
feat/workspace-sidebar-resize
fix/auth-token-refresh-race
docs/contributing-guide
ara/bg/2bf32847-2a57-4eb8-8006-beac6631-a0a723
```

## Background agent rules

Ara background agents run headless inside isolated git worktrees. If you are authoring or maintaining an automated task that will be executed by an agent, follow these rules:

1. **Never push to `main`.** Agents push only to their own branch (`ara/bg/<task-id>`).
2. **Never open PRs manually.** The Ara orchestrator opens the PR on behalf of the GitHub bot once the branch is pushed.
3. **Commit early and often.** Partial progress committed and pushed is recoverable. Uncommitted work is not.
4. **No interactive prompts.** Agents run non-interactively. Any tooling invoked by an agent must be fully scriptable and must not block waiting for user input.
5. **Atomic commits with clear messages.** Prefix the message with the relevant folder or component, e.g. `(AraDesktop) fix crash on window close`.
6. **Touch only the assigned worktree.** Do not modify files outside the worktree root or other worktrees.
7. **Write PR metadata to the temp file** provided in the task prompt so the orchestrator can create a properly titled, well-described PR.

## PR review checklist

Before approving a pull request, verify:

- [ ] The change does what the PR description says it does.
- [ ] New behaviour is covered by tests or has a clear reason for being exempt.
- [ ] No secrets, tokens, or API keys are committed (check `.env` additions and hardcoded strings).
- [ ] The diff is scoped to the stated purpose — no unrelated drive-by changes.
- [ ] Public APIs, config shapes, and environment variable names are documented if changed.
- [ ] The branch is up-to-date with `main` (no unresolved merge conflicts).
- [ ] CI is green.

For infrastructure changes (database migrations, deployment config, secrets rotation), request a second reviewer.
