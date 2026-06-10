# Ara Roadmap

This document tracks the near-term product direction for [Ara](https://ara.so) — the agent-building agent for your Mac.

Last updated: June 2026

---

## Vision

Ara runs fully automated, multi-step work on your Mac: coding agents, browser tasks, app control, and memory that survives across sessions — all without context-switching away from what you're doing.

---

## Milestones

### M1 — Foundation (shipped)
- Org profile and public presence on GitHub
- Background agent infrastructure (worktrees, headless task execution)
- AraDesktop notch view + session recordings
- AraWeb API on Railway with Infisical secrets management

### M2 — Agent Reliability (current)
- Improve bg agent task triage and staleness detection
- Git discipline: atomic commits, no pushes to `main`, draft PRs via bot
- Timeout and cancellation improvements in sandbox runtime
- Stale worktree / branch pruning automation

### M3 — Intelligence Layer (next)
- Project Brain: synthesize git history, sessions, memory into proactive suggestions
- Cross-session memory improvements (compact, declarative, preference-aware)
- Skill auto-discovery: agent learns new procedures and saves them without prompting
- Issue/PR awareness: Ara reads open issues and surfaces relevant ones in context

### M4 — Surface & UX
- Ara notch view: richer workspace switching and live agent status
- Browser pane improvements: DOM interaction, scraping, form fill
- Computer Use: full macOS native accessibility + vision model integration
- Mobile companion: lightweight iOS app for reviewing and approving agent work

### M5 — Ecosystem
- Plugin marketplace: community-contributed MCP connectors
- Multi-agent orchestration: spawn parallel agents and merge their results
- Shareable skills: export/import SKILL.md bundles across teams
- Billing and usage dashboard

---

## Top 5 features shipping next

1. **Project Brain synthesis** — proactive New Chat suggestions from git + sessions + memory signals
2. **Skill auto-save** — agent detects a non-trivial completed workflow and offers to save it as a skill without user prompting
3. **Issue/PR awareness** — Ara reads open GitHub issues and threads them into context when working on related code
4. **Stale branch pruning** — automated cleanup of accumulated `ara/bg/*` worktrees and branches
5. **Sandbox timeout + cancellation** — tick-based `waitForEngineWithTimeout` with `AbortSignal` sweep to prevent runaway bg tasks

---

## How to contribute

Open an issue using one of the templates in `.github/ISSUE_TEMPLATE/`. Use labels to help triage:

- `feature` — new capability
- `bug` — something broken
- `dx` — developer experience improvement
- `agent` — relates to bg agent infrastructure
- `milestone:M2` / `milestone:M3` — milestone tag

Pull requests are welcome. Background agent tasks run automatically on pushes and can be assigned via the Ara interface.
