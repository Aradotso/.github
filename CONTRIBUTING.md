# Contributing to the Aradotso Org Profile

This repo holds the GitHub organisation profile (`profile/README.md`, `profile/hero.png`, `profile/logo.png`) and org-level meta files. Changes here are public-facing — they appear on the Aradotso GitHub org page — so every change goes through a draft PR review before merge.

## Workflow for any org profile change

### 1. Create a topic branch

Branch from `main` using a short, descriptive slug:

```
git checkout main && git pull
git checkout -b profile/<short-description>
```

Examples: `profile/add-contributing`, `profile/update-hero-image`, `profile/new-badge`.

### 2. Make your change

Edit or add files directly. Common targets:

- `profile/README.md` — the public org profile page
- `profile/hero.png` / `profile/logo.png` — brand images
- `CONTRIBUTING.md` — this file
- `.github/ISSUE_TEMPLATE/` — issue templates
- `.github/PULL_REQUEST_TEMPLATE.md` — PR template

### 3. Commit with a folder prefix

Use the folder that owns the change as the commit prefix:

```
git add -A
git commit -m "profile: <what changed and why>"
```

Multi-file changes that span folders get a compound prefix:

```
git commit -m "profile(.github): add issue templates and PR template"
```

### 4. Push and open a draft PR

```
git push -u origin HEAD
gh pr create --draft \
  --title "profile: <what changed>" \
  --body "## Summary
<one-line description>

## Changes
- ...

## How to verify
- View the org profile page after merge: https://github.com/Aradotso
- Check rendered Markdown locally with \`npx --yes github-markdown-cli profile/README.md\`"
```

Draft status signals the change is ready for eyes but not yet approved for merge.

### 5. Review check before merge

Before converting a draft to ready (or merging), confirm:

- Rendered Markdown looks correct (no broken image refs, no stray HTML)
- Image files are not accidentally stripped of content (check file size > 0)
- No EXIF metadata leaking from design-tool exports in PNG files
- CI lint passes (if configured)

Convert to ready and merge only after at least one approval or a self-review sign-off.

### 6. Post-merge

Delete the topic branch:

```
git branch -d profile/<short-description>
git push origin --delete profile/<short-description>
```

## Commit message conventions

| Prefix | Use for |
|---|---|
| `profile:` | `profile/README.md` or image assets |
| `profile(.github):` | Both profile and `.github/` files in one commit |
| `.github:` | Templates, workflows, labels — no profile files changed |
| `docs:` | Root-level docs like `CONTRIBUTING.md`, `ROADMAP.md` |

## Quick reference

```
# Full happy path for a small text change
git checkout -b profile/fix-typo
# ... edit profile/README.md ...
git add -A && git commit -m "profile: fix typo in tagline"
git push -u origin HEAD
gh pr create --draft --title "profile: fix typo in tagline" --body "Fixes a typo."
# After review:
gh pr merge --squash
```
