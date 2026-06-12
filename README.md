# Aradotso / .github

This is the **[Aradotso](https://github.com/Aradotso)** org-profile repository — the special `.github` repo that GitHub uses to render the public face of [Ara](https://ara.so) at [github.com/Aradotso](https://github.com/Aradotso).

## What is amp?

`amp` (short for "Aradotso meta/profile") is the internal name for this repository. It holds the content and assets that power the Ara GitHub organisation's public landing page. Anything committed to `profile/README.md` on the default branch automatically renders as the org homepage at github.com/Aradotso — no deployment step needed; GitHub picks it up within seconds.

## Repository structure

```
.github/                ← this repo (special org-profile repo)
├── profile/
│   ├── README.md       ← rendered live on github.com/Aradotso
│   ├── hero.png        ← full-width banner image (displayed at the top)
│   └── logo.png        ← square logo mark (displayed below the heading)
└── README.md           ← you are here (contributor docs, not rendered by GitHub)
```

`profile/README.md` is the only file GitHub renders publicly. Everything else in this repo is for contributors.

## How changes go live

1. Edit `profile/README.md` (and/or swap out the images in `profile/`).
2. Commit and push to `main`.
3. GitHub re-renders the org page automatically — no CI, no deploy, no manual step.

Images referenced with relative paths (e.g. `./hero.png`) resolve correctly because GitHub serves them from the same `profile/` directory.

## Quick start for contributors

```bash
# Clone
git clone https://github.com/Aradotso/.github.git amp
cd amp

# Make your change
# Edit profile/README.md, then optionally replace profile/hero.png or profile/logo.png

# Preview locally (optional — any Markdown renderer works)
open profile/README.md   # macOS Quick Look / VS Code preview

# Commit and open a PR — do NOT push directly to main
git checkout -b profile/my-change
git add -A
git commit -m "(profile) describe your change"
git push -u origin HEAD
# Then open a PR via github.com or `gh pr create`
```

Ara's background agents (running as the `Ara GitHub Bot`) also push branches and open draft PRs against this repo as part of automated org-profile updates.

## Related links

- Live org page: [github.com/Aradotso](https://github.com/Aradotso)
- Ara product site: [ara.so](https://ara.so)
