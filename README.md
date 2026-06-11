# Aradotso/.github — Ara's public org profile

This repository powers **Ara's public face on GitHub**. Any file you edit here is automatically reflected at [github.com/Aradotso](https://github.com/Aradotso) — no deploy step required.

## What is this repo?

GitHub treats `.github` repositories in an organization as special: the `profile/README.md` file inside one is rendered verbatim as the organization's landing page. That means:

- Edit `profile/README.md` → the org page at github.com/Aradotso updates immediately after the commit is merged.
- Add images to `profile/` → reference them with relative paths (e.g. `./hero.png`) and they show up on the org page.
- No CI, no build, no publish step. GitHub does the rendering.

## Repository layout

```
.github/
├── profile/
│   ├── README.md   ← org landing page (github.com/Aradotso)
│   ├── hero.png    ← full-width hero banner shown at the top
│   └── logo.png    ← Ara logo mark used inline
└── README.md       ← this file (for contributors browsing the repo)
```

### profile/README.md

The public landing page for the Ara GitHub org. Keep it short and welcoming — it is the first thing external developers, users, and investors see when they land on github.com/Aradotso.

### profile/hero.png

Full-width banner image. Replace it with a new PNG and commit — the org page picks it up immediately.

### profile/logo.png

Ara logo mark. Used inline, currently displayed at 120 px width below the hero.

## Quick-start for contributors

1. **Clone the repo**
   ```bash
   git clone https://github.com/Aradotso/.github.git
   cd .github
   ```

2. **Create a branch**
   ```bash
   git checkout -b your-name/describe-change
   ```

3. **Edit what you need**
   - Org landing page → `profile/README.md`
   - Banner image → replace `profile/hero.png` (PNG, ideally ≥ 1200 px wide)
   - Logo → replace `profile/logo.png`

4. **Preview locally**
   Open `profile/README.md` in any Markdown renderer (GitHub's web editor, VS Code preview, etc.). What you see is approximately what the org page will look like.

5. **Push and open a PR**
   ```bash
   git push -u origin HEAD
   # then open a PR into main on GitHub
   ```
   Once merged, changes are live at [github.com/Aradotso](https://github.com/Aradotso) instantly.

## Notes

- Only the `profile/README.md` file is rendered as the org page. Files at the repo root (like this one) are visible to anyone browsing the repository but are not shown on the org landing page.
- Keep images reasonably sized — large PNGs slow down the org page load.
- Ara's product site is at [ara.so](https://www.ara.so). Keep links there consistent with what's on the org page.
