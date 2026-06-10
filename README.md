# Ara

**Ara** is an agent-building agent — a platform that lets you design, build, run, and refine automated agents directly on your Mac.

## What's here

This workspace covers the full Ara product surface:

- **AraDesktop** — Swift macOS app (the thing users install). Notch bar, workspace views, agent runtime, voice, and session recording.
- **AraWeb** — Cloud backend (Next.js + Bun relay sidecar, Supabase, Stripe). Auth, billing, hosted ACP runtime, voice proxy, phone↔Mac WebSocket relay, Sparkle appcast.
- **chat.ara.so** — Standalone Next.js chat surface. Deploys independently.
- **packages/** — Shared TypeScript utilities, types, and UI components used across apps.
- **apps/** — Additional standalone apps or micro-frontends.

## Stack

- **Desktop:** Swift, AppKit, WebKit
- **Web/API:** Next.js 16, React 19, Bun, Hono, TypeScript
- **Infrastructure:** Railway (API), Vercel (web), Supabase (DB + auth), Stripe (billing), Sentry (errors), PostHog (analytics)
- **Package manager:** pnpm workspaces
- **Agents:** Claude (Anthropic), Codex (OpenAI), Gemini (Google), Ara AI Gateway

## Getting started

```bash
# Install dependencies
pnpm install

# Run all dev servers in parallel
pnpm dev

# Type-check everything
pnpm typecheck

# Lint
pnpm lint

# Format
pnpm format
```

## Commit convention

All commits use a folder prefix:

```
(AraDesktop) short description
(AraWeb) short description
(chat.ara.so) short description
(ara-cua) workspace-level change
```

## License

Private — © Ara, Inc. All rights reserved.
