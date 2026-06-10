# Contributing to Ara

Thanks for your interest in contributing. We move fast and value decisiveness — small, well-scoped changes land faster than large ones.

## Code of Conduct

Be direct and constructive. Assume good intent. We won't tolerate harassment, discrimination, or bad-faith engagement. Violations can be reported to sven@ara.so.

## Development Setup

Most repos in this org are one of three shapes:

- **Desktop (Swift/Xcode)** — `AraDesktop/` in ara-cua. Open the Xcode workspace; build with `./AraDesktop/run.sh --id <slug>`.
- **Web/API (Bun/Hono or Next.js)** — `pnpm install && pnpm dev`. Secrets are in Infisical; pull with the Infisical CLI before running.
- **Profile/docs** — Markdown only. `npm install && npm run lint` if a `package.json` is present.

Check the repo-level README for the exact setup steps.

## PR Workflow

1. Fork or branch from `main`. Name branches descriptively: `fix/short-desc` or `feat/short-desc`.
2. Background/agent tasks run in isolated git worktrees (e.g. `~/.ara/worktrees/<id>`). Each task gets its own throwaway branch — never commit directly to `main`.
3. Open PRs as **drafts** via `gh pr create --draft` unless they are ready for immediate merge.
4. Keep PRs focused. One logical change per PR. Split unrelated fixes into separate PRs.
5. Push early; update the PR description as work progresses.

## Commit Message Conventions

Use a **folder prefix** that matches the subproject you changed, followed by a colon and an imperative description:

```
(AraDesktop) fix crash when chat stream is interrupted
(AraWeb) add sandbox timeout guard with PostHog telemetry
(chat.ara.so) surface error state on conversation load failure
web(changelog): add June release notes (en/zh-CN/es)
```

Rules:
- Imperative mood: "fix", "add", "remove", "update" — not "fixed" or "adds".
- No period at the end of the subject line.
- Keep the subject under 72 characters.
- Add a body paragraph when the why isn't obvious from the title.
- Atomic commits: each commit should leave the repo in a working state and represent one logical unit of change.
- `git add -A && git commit` — don't leave half-staged states.

## Testing Requirements

- **Swift:** run the relevant unit/UI test targets in Xcode before opening a PR. CI will run them again on push.
- **Bun/Node:** `pnpm test` (or `bun test`) must pass. Add or update tests for any new logic.
- **Markdown/docs:** run `npm run lint` if a linter is configured. Proofread links.
- For agent-generated PRs, note in the PR body which tests were run and their outcome.

## Review Process

- Tag a reviewer when the PR is ready (move from draft to open).
- Address review comments with new commits rather than force-pushing, unless the reviewer explicitly asks for a rebase.
- Two approvals are preferred for user-facing changes; one is sufficient for internal tooling and docs.
- Ara's background agents open PRs automatically after pushing a task branch. These go through the same review process — a human must approve before merge.
- Squash-merge is preferred to keep `main` history clean. The merge commit title should follow the same prefix conventions above.
