# Architecture

This document describes the monorepo layout for the Ara platform and provides a running decision log.

## Monorepo layout

The Ara platform lives across several repositories under the [Aradotso](https://github.com/Aradotso) GitHub org. The main projects and their locations:

**ara-cua** — core agent runtime  
Local path: `~/code/amp`  
Branch: `fix/bg-builds-timeouts` (active development)  
Stack: Swift (AraDesktop), Bun + Hono (AraWeb/api, AraWeb/ara.so), Next.js + React (chat.ara.so), Supabase

Sub-directories inside ara-cua:
- `AraDesktop/` — native macOS Swift/SwiftUI app (`./run.sh --id <slug>`)
- `AraWeb/api/` — Bun + Hono backend, deployed on Railway, secrets via Infisical
- `AraWeb/ara.so/` — Vite + React marketing site, deployed on Vercel
- `chat/` — Next.js 16 + React 19 + Tailwind 4 chat interface, deployed on Vercel
- `hq/` — Bun + Hono internal admin server (localhost only)
- `supabase/` — Supabase project with 48+ migrations

**Aradotso/.github** — GitHub org profile  
This repository. Contains `profile/README.md` (auto-rendered as the org landing page at github.com/Aradotso) and root-level community health files (`CONTRIBUTING.md`, `ARCHITECTURE.md`, `SECURITY.md`).

**myhre-co** — personal site  
Local path: `~/rnd/myhre-co`  
Stack: Next.js 15, pnpm

## External services

| Service | Purpose |
|---|---|
| Vercel | Frontend deploys (ara.so, chat.ara.so) |
| Railway | Backend API deploy |
| Supabase | Postgres database + auth |
| Infisical | Secrets management (root of trust) |
| Stripe | Billing |
| Sentry | Error monitoring |
| PostHog | Product analytics |

## Decision log

The decision log records significant architectural choices — what was decided, why, and what alternatives were considered. Add an entry any time a meaningful design decision is made.

### Template

```
### YYYY-MM-DD — <short title>

**Context:** What problem or situation prompted the decision.

**Decision:** What was decided.

**Alternatives considered:** What else was on the table and why it was not chosen.

**Consequences:** Expected trade-offs, risks, or follow-on work.
```

---

### 2026-06 — Lazy worktree creation for New Chat

**Context:** The desktop app's New Chat flow needed to support isolated git worktrees per conversation without slowing down the UI.

**Decision:** Show `main` as the initial branch selection and spin up a temporary worktree slot (e.g. `main-aebs3d`) only after the first message is submitted.

**Alternatives considered:** Eagerly creating the worktree on chat open — rejected because it added latency to the New Chat UI with no benefit if the user never sends a message.

**Consequences:** Worktree creation is deferred; the first message submission has a small added cost. Slots are throwaway and cleaned up after the chat closes.

---

### 2026-06 — Background agents never open PRs directly

**Context:** Background agent tasks push code branches but PR authorship should be consistent and tied to the Ara GitHub bot identity.

**Decision:** Background agents push their branch and write PR metadata to a temp file. Ara reads that file and opens the PR as the `ara-bot` GitHub app.

**Alternatives considered:** Agents calling `gh pr create` directly — rejected because it would use the developer's personal GitHub token and bypass the bot identity, making PR authorship inconsistent.

**Consequences:** Agents must never call `gh pr create`. The PR title and body must be written to the designated temp file path before the agent exits.

---

### 2026-06 — x-ara-conversation-id must be sanitized to UUID

**Context:** `AnthropicMessagesClient` and `AnthropicMessagesSender` pass `x-ara-conversation-id` as an HTTP header. Non-UUID values (e.g. numeric IDs) caused downstream parsing errors.

**Decision:** Always sanitize the conversation ID to a valid UUID format before sending. Both client and sender must apply this sanitization independently.

**Alternatives considered:** Sanitizing only at the API gateway — rejected because it moved the responsibility too far from the source and made the contract implicit.

**Consequences:** Any code path that constructs an `AnthropicMessagesClient` must ensure the conversation ID is a valid UUID or explicitly convert it.
