# scripts/organize-downloads

Reusable tooling for scanning and organizing `~/Downloads` (or any folder with a similar
category layout). Works alongside the Downloads git repo at `~/Downloads/.git`.

## Files

- `organize-downloads.py` — main script (scan, manifest, auto-file)
- `MANIFEST.md` — generated snapshot of current folder contents (re-run to refresh)

## Quick start

```bash
# From the ara-cua repo root — dry scan, no moves
python3 scripts/organize-downloads.py

# Preview what would be moved (loose root items only)
python3 scripts/organize-downloads.py --dry-run

# Actually file loose items into their subdirectory
python3 scripts/organize-downloads.py --auto-file
```

## What the script does

1. Scans the Downloads root recursively, respecting the seven canonical subdirectories:
   `Legal-Docs`, `Evidence-Bundles`, `Analytics`, `Media`, `Brand-Assets`, `Ara-Builds`, `Misc`.

2. Writes `scripts/MANIFEST.md` with:
   - A summary table: category, file count, total size, purpose tag
   - A "Loose Root Items" table listing anything sitting outside a subdirectory,
     with a suggested destination for each
   - Per-category file tables (path, size, creation date)

3. Optionally auto-files loose root items into the correct subdirectory using
   regex patterns defined in the `CATEGORIES` dict. Skips if destination exists.

## Category rules

| Category | Tag | Pattern examples |
|---|---|---|
| Legal-Docs | `legal` | `agreement`, `contract`, `invoice`, `SIGNED`, `DRAFT …`, `CIIA`, `Delaware LLC` |
| Evidence-Bundles | `evidence` | `epieos`, `share_resend`, `email.proof`, `audit` |
| Analytics | `analytics` | `browser-qa-report`, `\.csv$`, `payments`, `team-member` |
| Media | `media` | `.mp4`, `.mov`, `.gif`, `.jpg`, `.png`, `.webp`, `.heic` |
| Brand-Assets | `brand` | `logo`, `brand-kit`, `marketing-campaign`, `favicon`, `openara-header` |
| Ara-Builds | `builds` | `Ara_0.x.y`, `ara-so-demo-result`, `.dmg` |
| Misc | `misc` | catch-all |

To tune rules, edit the `CATEGORIES` dict in `organize-downloads.py`.

## Re-generating the manifest

Run the script any time new files land in Downloads:

```bash
python3 scripts/organize-downloads.py
git -C ~/Downloads add MANIFEST.md && git -C ~/Downloads commit -m "chore: refresh manifest"
```

Or do it from the ara-cua repo (manifest is also committed here under `scripts/`):

```bash
python3 scripts/organize-downloads.py
git add scripts/MANIFEST.md && git commit -m "(ara-cua) chore: refresh downloads manifest"
```

## Options

| Flag | Default | Description |
|---|---|---|
| `--root PATH` | `~/Downloads` | Override the folder to scan |
| `--auto-file` | off | Move loose root items into subdirs |
| `--dry-run` | off | Preview moves without executing |
| `--manifest-out PATH` | `scripts/MANIFEST.md` | Override manifest output path |

## Maintenance notes

- `Media/` and `Ara-Builds/` contain large binary files; those are gitignored in
  `~/Downloads/.gitignore`. The manifest still tracks them for size reporting.
- New screenshots go into `Media/screenshots/YYYY-MM/`.
- Stock images (Pexels, etc.) go into `Media/stock-images/`.
- Unclassified videos go into `Media/videos/`.
- Temporary scratch files belong in `Misc/` — prune periodically.
- The Downloads git repo (`~/Downloads`) is separate from this (ara-cua) repo. Both
  can carry a copy of the manifest; use whichever is more convenient.
