```
 ╔══════════════════════════════════════════════════════╗
 ║  ✿  ✿  ✿   ✦  A  R  A  ✦   ✿  ✿  ✿                ║
 ║  ꩜  The Agent-Building Agent  ꩜                     ║
 ╚══════════════════════════════════════════════════════╝
```

# 🌸 Ara

> ✨ **The agent-building agent.** Build, run, and refine automated agents on your Mac.

[![TypeScript](https://img.shields.io/badge/TypeScript-5.8-hotpink?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Next.js](https://img.shields.io/badge/Next.js-16-pink?style=flat-square&logo=nextdotjs)](https://nextjs.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.0-ffd6e7?style=flat-square&logo=tailwindcss)](https://tailwindcss.com/)

---

## 🌷 Overview

Ara is a next-generation agent platform for macOS that lets you **build**, **run**, and **refine** automated agents — all with a dreamy pink-pastel interface that makes automation feel delightful instead of daunting.

Whether you're automating repetitive tasks, orchestrating multi-step workflows, or building fully autonomous agents, Ara provides the scaffolding, intelligence, and style to make it happen.

---

## 💅 Tech Stack

| Layer | Technology |
|---|---|
| 🎨 **Framework** | Next.js 16 (App Router) |
| 💜 **Language** | TypeScript 5.8 (strict mode) |
| 🌸 **Styling** | Tailwind CSS 4 |
| 🧹 **Linting** | ESLint 9 (flat config) |
| 💄 **Formatting** | Prettier 3 + prettier-plugin-tailwindcss |
| 🪄 **PostCSS** | @tailwindcss/postcss |

---

## 🚀 Getting Started

### Prerequisites

- 🍎 macOS 13+
- 🟢 Node.js 20+ (recommend [nvm](https://github.com/nvm-sh/nvm))
- 📦 npm 10+ or pnpm 9+

### Install

```bash
# Clone the repo
git clone https://github.com/Aradotso/ara-cua.git
cd ara-cua

# Install dependencies (grab a snack, it's quick ✨)
npm install
```

### Development

```bash
# Start the dev server 🌸
npm run dev
```

Then open [http://localhost:3000](http://localhost:3000) — welcome to your pink-pastel command center! 🎀

Other useful commands:

```bash
npm run build       # Production build
npm run start       # Serve production build
npm run lint        # ESLint check
npm run format      # Prettier format
npm run type-check  # TypeScript type checking
```

---

## 🗂️ Project Structure

```
ara-project/
├── 🌸 app/
│   ├── layout.tsx      # Root layout with Inter font & pink gradient
│   ├── page.tsx        # Landing page with Ara branding
│   └── globals.css     # Tailwind 4 + pink/pastel CSS variables
├── 📄 package.json
├── 🔷 tsconfig.json
├── 🎨 postcss.config.mjs
├── ✨ eslint.config.js
├── 💄 .prettierrc
├── 🙈 .gitignore
└── 📖 README.md        ← you are here!
```

---

## 🤝 Contributing

We welcome contributions with open arms and pink confetti! 🎉

Before you open a PR, please keep these vibes in mind:

- 🌸 **Embrace the aesthetic** — Ara has a deliberate pink/pastel visual identity. New UI components should lean into the palette defined in `app/globals.css` (think `--pink-blush`, `--pink-hot`, `--lavender`). We are *not* a boring grey-scale app.
- 🔷 **TypeScript strictly** — no `any`, no skipping type-check.
- 💅 **Format before committing** — run `npm run format` so Prettier + the Tailwind class sorter keep things tidy.
- 🧹 **Lint passes** — `npm run lint` must be green before opening a PR.
- 📝 **Describe your change** — a short but vivid PR description goes a long way.

```
Step 1: Fork & clone 🍴
Step 2: Branch off main  →  git checkout -b feat/your-sparkle
Step 3: Make your magic ✨
Step 4: npm run format && npm run lint && npm run type-check
Step 5: Open a PR with pastel enthusiasm 🌷
```

---

<p align="center">Made with 💖 and a lot of pink</p>
