# Downloads — Organization Guide

_Last updated: 2026-06-11_

This directory is the organized artifact store for Sven / ara.so. Seven top-level categories hold all tracked files. Each category is described below along with naming conventions and maintenance tips.

## Legal-Docs

**37 files — 6 MB**

Delaware incorporation, contribution agreements, CIIA, consulting contracts, invoices, ACH receipts, and YC batch documents for Ara Software Inc.

_Naming convention:_ Keep originals as received. Add a date prefix (`YYYY-MM-DD-`) when filing new invoices or signed agreements.

- Signed PDF versions take precedence over `.docx` drafts.
- Archive receipts in the form `Receipt-<ID>.pdf`.
- YC and Delaware filings live at root level (do not sub-nest).

## Evidence-Bundles

**53 files — 12 MB**

Resend email campaign exports, epieos reports, and audit snapshots — used for compliance, shareholder record, and potential litigation support.

_Naming convention:_ Bundle directories follow the pattern `share_<service>_<MMMYY>/` (e.g. `share_resend_may21/`). Top-level PDFs use the source tool name as prefix.

- Never modify files inside a bundle after sealing.
- Add a `README.md` to each new bundle describing its scope.
- Sensitive CSVs should be gitignored if they contain PII.

## Analytics

**24 files — 4 MB**

QA browser-automation reports, PostHog/Amplitude CSV exports, payment analytics, and team-member snapshots.

_Naming convention:_ Zip bundles from CI follow `browser-qa-reports-<run-id>/`. Exported CSVs keep the tool-generated filename.

- Unzip bundles immediately; keep the source zip for reference.
- Add the export date to any manually renamed file.

## Media

**377 files — 3 GB**

Product demo recordings, changelog GIFs, marketing mockups, brand animations, and stock photography for ara.so.

_Naming convention:_ Dated demos: `YYYY-MM-DD-<feature>.(mp4|gif|webp)`. Screenshots: `Media/screenshots/YYYY-MM/`. Stock photos: `Media/stock-images/`. Unclassified video: `Media/video/`.

- Large files (>10 MB) are gitignored — track by path in MANIFEST.md.
- Prefer WebP/WebM over PNG/MP4 for marketing assets.
- Keep raw `.MOV` recordings separate from edited exports.

## Brand-Assets

**48 files — 15 MB**

Ara logo packages, brand kit zip, marketing PDFs, favicons, and OpenAra header variants.

_Naming convention:_ Logo variants: `ara-logo-<color>.png`. Zips: `ara-brand-kit.zip`, `Ara logo assets.zip`.

- The canonical brand kit lives in `ara-brand-kit/` (unzipped).
- Favicons go in `favicon_io/` — do not scatter them at root.
- Marketing PDFs (campaigns, decks) can stay at category root.

## Ara-Builds

**48 files — 4 GB**

AraDesktop `.dmg` installers, build artifact zips, and third-party app installers downloaded for evaluation.

_Naming convention:_ Ara releases: `Ara_<version>_<arch>.dmg`. Third-party: keep original installer name.

- Binary files are gitignored — only `.gitkeep` is committed.
- Delete superseded Ara DMGs once v+1 is stable.
- Evaluation DMGs from other vendors live here temporarily.

## Misc

**1267 files — 7 GB**

Bundled app skill archives, research papers, web templates, Raycast configs, personal docs, and items pending classification.

_Naming convention:_ No strict convention. Add a date or short context prefix for anything not obviously self-describing.

- Review Misc quarterly and promote files to a real category or delete.
- Commit log files (commit-summary-*.md) only if they need long-term audit.
- The `yes/` sub-folder holds photography exports — migrate to Media/photos/.

## Tooling

All scripts live in `scripts/` and require only the Python 3 stdlib (no pip installs, except optional `pyyaml` for project-override support).

| Script | Purpose |
|--------|---------|
| `organize-downloads.py` | All-in-one: scan, manifest, auto-file, README. Run `python3 organize-downloads.py --help` for full usage. |
| `catalog-downloads.py` | Deep CSV manifest with SHA-1 hashes; designed for launchd cron. |
| `tag-projects.py` | Assigns `project` labels (ara-cua, ara-so-site, …) to manifest rows. |
| `build-catalog-site.py` | Generates a static HTML search UI from the CSV manifest. |

### Quick-start

```bash
# Full refresh: scan → markdown manifest → README
python3 scripts/organize-downloads.py

# Preview what auto-filing would move (no changes)
python3 scripts/organize-downloads.py auto-file

# Actually move loose root files into categories
python3 scripts/organize-downloads.py auto-file --execute

# Deep CSV manifest + project tags (for the catalog site)
python3 scripts/catalog-downloads.py && python3 scripts/tag-projects.py
```

## Git Policy

The Downloads folder is a git repo (`github.com/Aradotso/ara-cua` mirror branch or standalone). The `.gitignore` excludes large binaries (`.dmg`, loose images, video), so only text-based artifacts and small assets are tracked.

Run `git add -A && git commit -m 'chore: refresh downloads catalog'` after significant additions or after running the organizer.
