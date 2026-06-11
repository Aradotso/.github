# Ara — Developer Setup

This guide covers cloning the Ara development environment, required tools, cross-repo workflows, and common tasks.

---

## Required Tools

| Tool | Version / Notes |
|------|----------------|
| macOS | 14.0+ (Sonoma or later) |
| Xcode | Latest stable — required for AraDesktop (Swift) |
| [Bun](https://bun.sh) | Latest — used by `AraWeb/api`, `hq/`, and `chat.ara.so` tests |
| Node.js | 20+ — used by `chat.ara.so` (Next.js) and `AraWeb/ara.so` (Vite) |
| [pnpm](https://pnpm.io) | Latest — used by select web packages |
| [Supabase CLI](https://supabase.com/docs/guides/cli) | For running local DB / migrations |
| [Railway CLI](https://docs.railway.app/guides/cli) | For API deployments |
| [Infisical CLI](https://infisical.com/docs/cli/overview) | Secrets — required before running any service locally |
| [Vercel CLI](https://vercel.com/docs/cli) | For `ara.so` front-end deploys |
| [GitHub CLI (`gh`)](https://cli.github.com) | For branch/PR workflows |
| Apple Developer ID | Required to build and sign AraDesktop |

Install Bun, Infisical, and Supabase CLI via their respective official docs. Everything else is available via Homebrew:

```bash
brew install node pnpm supabase/tap/supabase infisical gh
brew install --cask railway
```

---

## Repositories

All production code lives in the `Aradotso` org. Start with the monorepo:

| Repo | What it is |
|------|-----------|
| [`Aradotso/ara-cua`](https://github.com/Aradotso/ara-cua) | Main monorepo — AraDesktop, AraWeb, chat.ara.so, hq, supabase |
| [`Aradotso/.github`](https://github.com/Aradotso/.github) | Org profile and shared docs (this repo) |

---

## Cloning and Initial Setup

```bash
# Clone the monorepo
git clone https://github.com/Aradotso/ara-cua.git
cd ara-cua

# Authenticate secrets (run once — fetches all env from Infisical)
infisical login
```

Then install dependencies per subproject (see below).

---

## Subprojects

### AraDesktop (Swift macOS app)

Requires macOS 14+, Xcode, and a valid Apple Developer ID certificate.

```bash
cd AraDesktop

# Build and launch against production API
./run.sh

# Build and launch against dev API (api-dev.ara.so)
./run.sh --dev

# Wipe local state and re-run (resets onboarding, UserDefaults)
./reset-and-run.sh
```

See [`AraDesktop/README.md`](https://github.com/Aradotso/ara-cua/blob/main/AraDesktop/README.md) for full details.

### AraWeb/api (Bun + Hono — Railway)

```bash
cd AraWeb/api
bun install

# Run locally with secrets injected from Infisical
bun run dev
```

Deploys to `api.ara.so` (prod) and `api-dev.ara.so` (dev) via Railway. See `CLAUDE.md` in the monorepo root for the deploy runbook.

### AraWeb/ara.so (Vite + React — Vercel)

```bash
cd AraWeb/ara.so
bun install   # or pnpm install

bun run dev   # local dev server
bun run build # production build
vercel --prod # deploy to Vercel
```

### chat.ara.so (Next.js — standalone)

```bash
cd chat.ara.so
bun install

next dev      # local dev server (port 3000)
bun run build # production build
bun test      # run tests
```

### hq (Bun + Hono — localhost admin)

```bash
cd hq
bun install
bun run dev   # localhost only — requires Infisical for service-role keys
```

### supabase (Postgres migrations)

```bash
cd supabase

# Start a local Supabase stack (Postgres + Auth + Storage)
supabase start

# Apply all migrations
supabase db push

# Stop when done
supabase stop
```

---

## Linking Repos / Running Together

For full end-to-end local dev:

1. Start Supabase locally: `cd supabase && supabase start`
2. Start `AraWeb/api`: `cd AraWeb/api && bun run dev` (defaults to port 3002)
3. Start `chat.ara.so`: `cd chat.ara.so && next dev` (port 3000)
4. Launch AraDesktop with `./run.sh --dev` to point it at `api-dev.ara.so` or your local API

Each subproject reads secrets from Infisical at startup — no manual `.env` copying needed.

---

## Common Workflows

### Running Tests

```bash
# AraWeb/api
cd AraWeb/api && bun test

# chat.ara.so
cd chat.ara.so && bun test

# AraWeb/ara.so (type-check)
cd AraWeb/ara.so && bun run typecheck
```

### Building

```bash
# AraDesktop — local production DMG
cd AraDesktop && ./build.sh

# AraWeb/ara.so — production bundle
cd AraWeb/ara.so && bun run build

# chat.ara.so
cd chat.ara.so && next build
```

### Deploying

| Target | Command | Notes |
|--------|---------|-------|
| `AraWeb/api` | `railway up --environment production` | Read deploy runbook in `CLAUDE.md` first |
| `AraWeb/ara.so` | `vercel --prod` | From `AraWeb/ara.so/` |
| Supabase migrations | `supabase db push` | Against the target project |

### Environment Readiness Check

Before touching external services, run the readiness probe from the monorepo root:

```bash
.claude/skills/ara-cua-dev-verify-clis-and-mcps-ready/scripts/ara-ready.sh
```

This checks Infisical, Supabase, Railway, Stripe, PostHog, Sentry, Vercel, GitHub, and more. Exits 0 on success.

---

## Secrets Policy

All secrets live in **Infisical** — never in `.env` files, Railway env vars, or GitHub Actions secrets. Running `infisical run -- <command>` (or `bun run dev` which wraps this) injects secrets automatically.

---

## Further Reading

- [`ara-cua/AGENTS.md`](https://github.com/Aradotso/ara-cua/blob/main/AGENTS.md) — workspace/browser control playbook and commit conventions
- [`ara-cua/CLAUDE.md`](https://github.com/Aradotso/ara-cua/blob/main/CLAUDE.md) — full subproject table, skills index, deploy guide
- [`ara-cua/OVERVIEW.md`](https://github.com/Aradotso/ara-cua/blob/main/OVERVIEW.md) — architecture diagram and repo map
- [`ara-cua/AraDesktop/README.md`](https://github.com/Aradotso/ara-cua/blob/main/AraDesktop/README.md) — AraDesktop-specific setup
