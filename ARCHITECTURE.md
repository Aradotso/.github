# Architecture

Ara is a five-part monorepo. Each package is independently deployable and communicates over well-defined API boundaries.

## AraDesktop

Swift/AppKit native Mac application. Hosts the Ara agent runtime, manages worktrees, renders panes (chat, browser, terminal, canvas), and orchestrates background agents. Built with `./run.sh --id <slug>`.

## AraWeb/api

Bun + Hono backend. Handles authentication, billing (Stripe), agent session state, and the REST/streaming APIs consumed by both the desktop app and the web front-ends. Deployed on Railway with secrets managed through Infisical.

## AraWeb/ara.so (marketing site)

Vite + React static site deployed to Vercel. Public-facing landing pages, docs, and changelog. Lives under `AraWeb/ara.so/`.

## chat.ara.so

Next.js 16 + React 19 + Tailwind 4 conversational interface. Provides the browser-based chat experience for users who are not on the Mac app. Deployed to Vercel. Lives under `chat/`.

## hq (admin)

Bun + Hono internal admin dashboard running on localhost. Used by the Ara team for ops, feature flags, and support tooling. Lives under `hq/`.

---

All packages share a single Supabase project (PostgreSQL + Storage + Auth). Database migrations live under `supabase/migrations/` and are applied in order. Secrets are never committed; all environments pull from Infisical at build/runtime.
