# Ara — Technology Architecture

This document describes the major technologies powering Ara's platform and why each was chosen.

---

## Frontend

**[Next.js](https://nextjs.org)** — App Router, server components, and edge rendering for `chat.ara.so`. Chosen for streaming support and React Server Components that keep the AI chat experience snappy.

**[React 19](https://react.dev)** — Used across all web surfaces. The concurrent features and improved `use()` hook pair well with streaming LLM responses.

**[Tailwind CSS v4](https://tailwindcss.com)** — Utility-first CSS with zero-runtime, native CSS variables, and the new `@layer` cascade. Keeps design tokens consistent across the app and marketing site.

**[Vite](https://vitejs.dev)** — Bundler for `ara.so` (marketing / landing). Fast HMR during development.

---

## Backend

**[Bun](https://bun.sh)** — Runtime for all API services and workers. Faster cold starts than Node and native TypeScript support without a build step.

**[Hono](https://hono.dev)** — Lightweight HTTP framework running on Bun. Handles routing for `AraWeb/api` and the internal `hq/` admin service.

---

## Data & Auth

**[Supabase](https://supabase.com)** — Managed Postgres, Row-Level Security, Auth (magic link + OAuth), and Realtime channels used for live agent-status streaming. Currently at 48+ migrations.

---

## Infrastructure & Hosting

**[Vercel](https://vercel.com)** — Deploys `ara.so` and `chat.ara.so`. Preview deployments on every PR.

**[Railway](https://railway.app)** — Runs `AraWeb/api` and other persistent services. Picked for simplicity, zero-config deploys from GitHub, and first-class Bun support.

**[Infisical](https://infisical.com)** — Secrets manager (root of trust). Environment variables for all Railway and Vercel services are synced from Infisical rather than set in platform dashboards.

---

## Observability

**[Sentry](https://sentry.io)** — Error tracking and performance monitoring across frontend and backend. Session replays are enabled on `chat.ara.so`.

**[PostHog](https://posthog.com)** — Product analytics, feature flags, and event capture. Used to track activation funnel, agent run metrics, and feature adoption.

---

## Payments

**[Stripe](https://stripe.com/docs)** — Billing, subscriptions, and usage-based metering. Stripe webhooks feed into Supabase to gate feature access by plan.

---

## Desktop

**Swift / SwiftUI / AppKit** — `AraDesktop` is a native macOS app. Uses AppKit for window management and low-level OS hooks; SwiftUI for declarative UI surfaces.

---

## CLI Agents (dev tooling)

Ara developers integrate with several AI CLI agents locally:

- [Claude Code](https://www.anthropic.com/claude) (`claude`)
- [OpenAI Codex CLI](https://github.com/openai/codex) (`codex`)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) (`gemini`)
- [Cursor Agent](https://www.cursor.com) (`cursor-agent`)

---

## Summary

```
chat.ara.so       Next.js 16 + React 19 + Tailwind 4   → Vercel
ara.so            Vite + React                          → Vercel
AraWeb/api        Bun + Hono                            → Railway + Infisical
AraDesktop        Swift + SwiftUI + AppKit              → macOS native
supabase/         Postgres + Auth + Realtime            → Supabase cloud
```
