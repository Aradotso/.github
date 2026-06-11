# Architecture

Ara is a five-part monorepo. Each part deploys independently.

## 1. AraDesktop

Native Swift/AppKit macOS application. Handles the notch bar, workspace views, agent runtime, voice, session recording, and local file access. Distributed via a Sparkle appcast. Talks to AraWeb/api over WebSocket and REST.

## 2. AraWeb/api

Cloud backend built with Bun + Hono. Runs on Railway with secrets managed by Infisical. Owns auth (Supabase), billing (Stripe), the hosted ACP agent runtime, voice proxy, and the phone↔Mac WebSocket relay. Also serves the Sparkle appcast for desktop auto-update.

## 3. ara.so (marketing site)

Vite + React static site deployed on Vercel. No server-side logic. References shared `packages/` components where needed.

## 4. chat.ara.so

Standalone Next.js 16 / React 19 / Tailwind 4 chat surface. Deploys independently on Vercel. Talks to AraWeb/api for auth and agent execution. Can be embedded or opened as a standalone tab.

## 5. hq (admin)

Internal Bun + Hono admin service running on localhost. Not publicly exposed. Provides ops tooling: usage dashboards, feature flags, manual billing adjustments, and Supabase query shortcuts.

## Shared infrastructure

- Database & auth: Supabase (48+ migrations)
- Error tracking: Sentry
- Analytics: PostHog
- Package manager: pnpm workspaces
- Agents: Claude (Anthropic), Codex (OpenAI), Gemini (Google), routed through Ara AI Gateway
