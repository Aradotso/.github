# Ara — Tech Stack & Architecture

A reference document covering the major technologies used across Ara's org repos.

---

## Frontend

| Layer | Technology | Notes |
|---|---|---|
| Framework | [Next.js](https://nextjs.org) | App Router, RSC, used for `chat.ara.so` |
| UI library | [React 19](https://react.dev) | Server Components + Actions |
| Styling | [Tailwind CSS v4](https://tailwindcss.com) | CSS-first config, used org-wide |
| Build/bundler | [Vite](https://vitejs.dev) | Used for `ara.so` marketing site (Vite + React) |

## Backend & Runtime

| Layer | Technology | Notes |
|---|---|---|
| Runtime | [Bun](https://bun.sh) | JavaScript/TypeScript runtime for API servers |
| API framework | [Hono](https://hono.dev) | Lightweight web framework on top of Bun |
| Database | [Supabase](https://supabase.com) | Postgres + Auth + Realtime; 48+ migrations |
| Hosting | [Railway](https://railway.app) | API and backend service deployments |
| Secrets | [Infisical](https://infisical.com) | Centralised secret management for all services |

## Payments & Billing

| Technology | Docs |
|---|---|
| [Stripe](https://stripe.com) | Subscriptions and one-off payments; Stripe CLI for local webhook testing |

## Observability

| Technology | Docs |
|---|---|
| [Sentry](https://sentry.io) | Error tracking and performance monitoring |
| [PostHog](https://posthog.com) | Product analytics and feature flags |

## Desktop & Agent Runtime

| Technology | Notes |
|---|---|
| Swift / AppKit / SwiftUI | macOS desktop app (`AraDesktop`) |
| [Bun](https://bun.sh) + [Hono](https://hono.dev) | HQ admin server (localhost) |

## CI / Dev Tools

| Technology | Notes |
|---|---|
| [GitHub Actions](https://github.com/features/actions) | CI/CD pipelines across all repos |
| [Vercel](https://vercel.com) | Frontend deployments (`ara.so`, `chat.ara.so`) |
| pnpm / Bun workspaces | Package management |

---

> This document reflects the state of the stack as of mid-2025. Update it whenever a major dependency is added or retired.
