# Contributing to Ara

Thank you for your interest in contributing to Ara. This guide covers how to report bugs, request features, submit code changes, and reach the team.

---

## Reporting bugs and requesting features

Open a GitHub issue in the relevant repository:

- **ara-cua** (desktop app & platform): https://github.com/Aradotso/ara-cua/issues

When filing a bug, include:
1. A short description of what went wrong.
2. Steps to reproduce.
3. What you expected to happen vs what actually happened.
4. Version number (visible in the Ara desktop app under About).

For security vulnerabilities, **do not open a public issue**. Email [security@ara.so](mailto:security@ara.so) instead.

---

## Contributing code

### Prerequisites

- Node.js ≥ 20, Bun ≥ 1.1, and pnpm for web packages.
- Xcode 15+ for the Swift desktop app.
- `gh` CLI for interacting with pull requests.

### Branch naming

Use the format `<scope>/<short-description>` where scope is one of:

- `feat/` — new feature
- `fix/` — bug fix
- `chore/` — maintenance, dependency updates
- `docs/` — documentation only

Examples: `feat/chat-export`, `fix/toolbar-focus-loss`, `docs/contributing-guide`.

### Pull request flow

1. Fork the repo (external contributors) or create a branch from `main` (team members).
2. Make focused, atomic commits. Prefix the commit message with the affected area in parentheses, e.g. `(AraDesktop) fix: toolbar focus restoration`.
3. Open a PR against `main`. Fill in the PR template — summary, what changed, how to test.
4. CI runs automatically: linting, type checks, and tests must pass before merge.
5. At least one review approval is required to merge.

### CI checks

All PRs must pass:

- Type checking (`tsc --noEmit` for TypeScript packages).
- Lint (`eslint` / `swiftlint` depending on the package).
- Unit tests (`bun test` or `pnpm test`).

If CI is red on your PR, fix it before requesting review.

---

## Reaching the team

| Channel | Use for |
|---|---|
| [GitHub Issues](https://github.com/Aradotso/ara-cua/issues) | Bug reports, feature requests |
| [founders@ara.so](mailto:founders@ara.so) | General enquiries, partnerships |
| [security@ara.so](mailto:security@ara.so) | Security disclosures (private) |

We do not have a public Discord or Slack at this time. Watch this space — community channels may be added as Ara grows.

---

## A note on org discussions

GitHub Discussions for the Aradotso org are not enabled yet. If community interest grows, we will enable them as the primary async forum for questions and RFCs.
