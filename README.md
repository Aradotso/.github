# Aradotso/.github

This is the **GitHub organization profile repository** for [Ara](https://ara.so) — the agent-building agent, backed by Y Combinator.

## What is this repo?

GitHub renders `profile/README.md` automatically on the organization's public page at [github.com/Aradotso](https://github.com/Aradotso). Anything you commit to that file goes live there — no deploy step, no CI required. Think of it as Ara's front door on GitHub.

This repo also holds org-wide defaults: community health files (`SECURITY.md`, and eventually `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, etc.) that GitHub surfaces across every public repo under the Aradotso org when those repos don't have their own copies.

## Repository structure

```
.github/               # (this repo)
├── profile/
│   ├── README.md      # Renders at github.com/Aradotso — edit here to update the org page
│   ├── hero.png       # Banner image shown at the top of the org profile
│   └── logo.png       # Ara square logo used inline
└── SECURITY.md        # Org-wide security policy (applies to all Aradotso repos by default)
```

## How changes here reach the live org page

1. Edit `profile/README.md` in this repo.
2. Commit and push to `main`.
3. GitHub picks up the change immediately — no cache busting needed. The org page at [github.com/Aradotso](https://github.com/Aradotso) reflects the new content within seconds.

To preview locally before pushing, open `profile/README.md` in any Markdown renderer (VS Code preview, Marked 2, etc.). Images reference paths relative to `profile/`, so `./hero.png` resolves correctly both locally and on GitHub.

## Quick start for contributors

```bash
# Clone
git clone https://github.com/Aradotso/.github.git
cd .github

# Make your edits
# The main file to change is profile/README.md

# Preview (VS Code)
code profile/README.md   # Cmd+Shift+V to open preview

# Commit and push
git add -A
git commit -m "profile: <describe your change>"
git push
```

PRs are welcome. Background agents (Ara's own automated coding agents) open PRs into `main` using the `ara/bg/*` branch namespace — these are auto-reviewed and auto-merged after passing review.

## Org-wide community health files

GitHub automatically uses files in this repo as defaults for any Aradotso repo that doesn't define its own:

- `SECURITY.md` — how to report vulnerabilities (contact: security@ara.so)

Adding `CONTRIBUTING.md` or `CODE_OF_CONDUCT.md` here will propagate them org-wide the same way.

## Links

- Website: [ara.so](https://ara.so)
- Org page: [github.com/Aradotso](https://github.com/Aradotso)
- Security contact: security@ara.so
