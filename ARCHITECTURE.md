# Architecture

This document describes the high-level layout of the Ara monorepo, explains the key architectural decisions, and provides a template for recording future decisions.

## Monorepo layout

```
ara-cua/
├── AraDesktop/        Swift/SwiftUI macOS app. Native desktop agent surface.
├── AraWeb/
│   ├── api/           Bun + Hono API server. Deployed on Railway.
│   └── ara.so/        Vite + React marketing site. Deployed on Vercel.
├── chat/              Next.js app for chat.ara.so. Deployed on Vercel.
├── hq/                Internal tooling and admin surface (Bun + Hono).
├── supabase/          Database schema, migrations, and seed data.
├── profile/           GitHub org profile (README, brand assets).
├── .github/           CI workflows, issue templates, PR templates.
├── CONTRIBUTING.md    This contributing guide.
└── ARCHITECTURE.md    This document.
```

### Key dependencies

- Runtime: Bun (server-side JS), Swift 6 (macOS app).
- Database: Supabase (Postgres + Auth + Storage + Realtime).
- Secrets: Infisical (injected at deploy time on Railway; env for Vercel).
- Payments: Stripe.
- Observability: Sentry (errors), PostHog (product analytics), Axiom (logs).
- CI: GitHub Actions (auto-merge, auto-release, version promote, claude-review).

### Deployment targets

| Package      | Platform | Notes                        |
|-------------|----------|------------------------------|
| AraWeb/api  | Railway  | Secrets via Infisical         |
| AraWeb/ara.so | Vercel | Static + Edge Functions      |
| chat/        | Vercel   | SSR via Next.js Edge Runtime |
| AraDesktop   | Direct   | Distributed as .app bundle   |

## Decision log

Use the template below for any significant architectural or infrastructure decision. Add new entries at the top of the log, newest first.

### Decision log template

```
## ADR-NNN: <short title>

Date: YYYY-MM-DD
Status: proposed | accepted | superseded | deprecated

### Context
What situation or problem prompted this decision?

### Decision
What was decided?

### Consequences
What are the expected trade-offs, risks, or follow-up actions?
```

---

## Decision log entries

### ADR-001: Monorepo with per-package deployment

Date: 2024-01-01
Status: accepted

#### Context
Ara has a native macOS app, a web API, a marketing site, a chat app, and internal tooling. Keeping them in a single repository simplifies cross-cutting changes and dependency management while still allowing independent deployments.

#### Decision
Adopt a monorepo structure where each package is independently deployable. CI workflows are scoped to the packages they affect using path filters.

#### Consequences
Developers need to be aware of which package they are editing. PRs touching multiple packages should be reviewed for unintended cross-package side effects. Path-filtered CI reduces noise but requires discipline when moving shared code.
