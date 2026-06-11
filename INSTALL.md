# Ara — Local Setup

Quick-start guide for setting up the Ara development environment. Each sub-repo has a README with deeper details; this doc covers the prerequisites and cross-repo workflows.

---

## Required tools

| Tool | Purpose | Install |
|------|---------|---------|
| macOS 14+ | AraDesktop (Swift app) | — |
| Xcode (latest) | Build AraDesktop Swift target | App Store / `xcode-select --install` |
| [Node.js](https://nodejs.org) ≥ 20 | chat.ara.so (Next.js) | `brew install node` |
| [pnpm](https://pnpm.io) | Package management (ara.so site) | `brew install pnpm` |
| [Bun](https://bun.sh) ≥ 1.1 | AraWeb/api, hq, acp-bridge | `curl -fsSL https://bun.sh/install \| bash` |
| [Docker](https://www.docker.com) | chat.ara.so container builds | Docker Desktop |
| [Supabase CLI](https://supabase.com/docs/guides/cli) | DB migrations | `brew install supabase/tap/supabase` |
| [Infisical CLI](https://infisical.com/docs/cli) | Secrets injection (hq, api) | `brew install infisical/get-cli/infisical` |
| [GitHub CLI](https://cli.github.com) | PRs, repo ops | `brew install gh` |
| Apple Developer ID cert | Code-sign AraDesktop builds | developer.apple.com |

---

## Clone and bootstrap

The main workspace is the **ara-cua** monorepo.

```bash
git clone https://github.com/Aradotso/ara-cua
cd ara-cua
```

Then set up each sub-package you need (see sections below). There is no root-level `install` command; each folder is independent.

---

## Sub-repos and how to run them

### AraDesktop — Swift macOS app

Docs: `AraDesktop/README.md`

```bash
cd AraDesktop

# Run dev build (builds Swift target, starts backend, launches app)
./run.sh

# Clean-slate run (resets onboarding, UserDefaults, permissions)
./reset-and-run.sh
```

Requirements: macOS 14+, Xcode, Apple Developer ID for code signing.

### AraWeb/api — Cloud API (Bun + Hono)

```bash
cd AraWeb/api
bun install
bun run dev        # hot-reloads; wraps infisical run internally
```

Secrets come from Infisical. Run `infisical login` once before first use.

### chat.ara.so — Hosted chat UI (Next.js 16 + React 19 + Tailwind 4)

```bash
cd chat.ara.so
npm install        # or: pnpm install
npm run dev        # starts on :3000
```

Needs `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY` in `.env.local`.

### AraWeb/ara.so — Marketing site (Vite + React)

```bash
cd AraWeb/ara.so
pnpm install
pnpm dev
```

Deploys to Vercel automatically on push to main.

### hq — Localhost admin dashboard (Bun + Hono)

```bash
cd hq
bun install
bun run dev        # binds to 127.0.0.1:8888 — never expose publicly
```

Docs: `hq/README.md`. Requires Infisical login.

### supabase — Database migrations

```bash
cd supabase
supabase link --project-ref <ref>
supabase db push       # apply pending migrations
supabase db diff       # preview local vs remote schema
```

---

## Linking repos / running together

The repos are independent services. For a full local stack:

1. Start `AraWeb/api` (`bun run dev` on its default port).
2. Start `chat.ara.so` (`npm run dev` on :3000) — point `NEXT_PUBLIC_API_URL` at the local api.
3. Launch `AraDesktop` via `./run.sh` — it connects to the local api or the Railway-deployed one depending on build flags.
4. Optionally start `hq` on :8888 for admin reads.

There is no docker-compose for the full stack. Each service can be developed independently against the shared Supabase project.

---

## Common workflows

### Run tests

```bash
# AraWeb/api (Bun test runner)
cd AraWeb/api && bun test

# chat.ara.so (Next.js — no test runner configured by default, add as needed)
```

### Type-check without running

```bash
# Any TypeScript package
bun run typecheck    # or: npx tsc --noEmit
```

### Build for production

```bash
# chat.ara.so
npm run build && npm start

# AraWeb/api
bun run start

# AraDesktop (signed DMG for distribution)
cd AraDesktop && ./build.sh
```

### Deploy

- **AraWeb/api** — auto-deploys to Railway on push to main.
- **chat.ara.so** — Docker-based Railway deployment (`Dockerfile` at root of `chat.ara.so/`).
- **AraWeb/ara.so** — auto-deploys to Vercel on push to main.
- **AraDesktop** — Sparkle appcast; use `./distribute.sh` after tagging a release.

### Database migrations

```bash
cd supabase
supabase migration new <description>   # scaffold a new migration
supabase db push                       # apply to linked project
```

---

## Secrets management

All secrets live in [Infisical](https://infisical.com). After cloning:

```bash
infisical login                        # one-time browser auth
```

Each package's `package.json` dev script already wraps `infisical run` with the correct project ID. For chat.ara.so, copy `.env.local.example` to `.env.local` and fill in Supabase keys from the Infisical dashboard.

---

## Per-repo READMEs

- [`AraDesktop/README.md`](https://github.com/Aradotso/ara-cua/blob/main/AraDesktop/README.md) — Swift build details, run flags, backend architecture
- [`hq/README.md`](https://github.com/Aradotso/ara-cua/blob/main/hq/README.md) — admin dashboard, why it exists, how secrets flow
- [`supabase/`](https://github.com/Aradotso/ara-cua/tree/main/supabase) — migration history
