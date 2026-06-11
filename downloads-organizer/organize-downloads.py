#!/usr/bin/env python3
"""
organize-downloads.py — All-in-one Downloads folder organizer.

Modes
-----
  scan        Recursively scan Downloads, print a summary, and write a manifest.
  manifest    Write (or refresh) the markdown manifest to <out-dir>/MANIFEST.md.
  auto-file   Move unorganized files at the root level into category subdirs
              based on regex/extension rules (dry-run by default).
  readme      (Re)generate <out-dir>/ORGANIZED-README.md describing the layout.
  all         Run scan → manifest → readme in sequence (default).

Usage
-----
  python3 organize-downloads.py [MODE] [OPTIONS]

  python3 organize-downloads.py                           # all modes, default paths
  python3 organize-downloads.py scan
  python3 organize-downloads.py manifest --out /tmp/out
  python3 organize-downloads.py auto-file --execute       # actually move files
  python3 organize-downloads.py all --downloads ~/Downloads --out ~/Downloads/docs

Options
-------
  --downloads PATH   Root of the Downloads folder  (default: ~/Downloads)
  --out PATH         Output directory for manifest + README (default: <downloads>/docs)
  --execute          For auto-file: actually move files (default is dry-run)
  --no-hash          Skip SHA-1 computation (faster on large trees)
  -q / --quiet       Suppress per-file output, only print summary

Design notes
------------
• The manifest is a Markdown file with a summary table (file counts, sizes,
  creation/modification dates) followed by a full file listing with purpose tags.
• Auto-filing uses the CATEGORY_RULES mapping; add new regex patterns there.
• Does not require any third-party libraries — stdlib only.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import os
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Category definitions
# ---------------------------------------------------------------------------

CATEGORIES: list[str] = [
    "Legal-Docs",
    "Evidence-Bundles",
    "Analytics",
    "Media",
    "Brand-Assets",
    "Ara-Builds",
    "Misc",
]

# Purpose tags applied in the manifest (path substring → tag)
PURPOSE_TAGS: list[tuple[str, str]] = [
    ("Legal-Docs",       "legal"),
    ("Evidence-Bundles", "evidence"),
    ("Analytics",        "analytics"),
    ("Media/screenshots","screenshot"),
    ("Media/stock",      "stock-image"),
    ("Media/video",      "video"),
    ("Media",            "media"),
    ("Brand-Assets",     "brand"),
    ("Ara-Builds",       "build"),
    ("Misc/logs",        "log"),
    ("Misc",             "misc"),
]

# Rules for auto-filing loose root-level files into category subdirs.
# Each entry: (pattern, destination_subdir)
# Patterns are matched against the filename (case-insensitive).
CATEGORY_RULES: list[tuple[str, str]] = [
    # Legal / financial
    (r"(?i)(invoice|receipt|contract|agreement|ciia|certificate|incorporation"
     r"|consent|letter|legal|notari|board|amendment|delaware|ycombinator)",
     "Legal-Docs"),
    # Evidence / audit
    (r"(?i)(evidence|resend|redacted|session|bundle|epieos)", "Evidence-Bundles"),
    # Analytics / data
    (r"(?i)(analytics|report|csv|qa|metric|dashboard|payment|unified)", "Analytics"),
    # Brand
    (r"(?i)(logo|brand|icon|favicon|header|marketing|campaign|openara)",
     "Brand-Assets"),
    # Builds / installers
    (r"(?i)(\.dmg$|\.zip$|installer|setup|build|release)", "Ara-Builds"),
    # Media (images, video, gifs)
    (r"(?i)(screenshot|\.(png|jpg|jpeg|gif|webp|svg|mp4|mov|webm|heic)$)",
     "Media"),
]

IGNORE_NAMES: frozenset[str] = frozenset({
    ".DS_Store", ".localized", ".git", "Thumbs.db",
})
IGNORE_DIRS: frozenset[str] = frozenset({
    ".git", ".github", "__pycache__", "node_modules",
    "docs", "scripts", "logs",
})


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def human_size(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.0f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def sha1_prefix(path: Path, nbytes: int = 65536) -> str:
    h = hashlib.sha1()
    try:
        with path.open("rb") as f:
            while chunk := f.read(nbytes):
                h.update(chunk)
        return h.hexdigest()[:8]
    except OSError:
        return "err"


def infer_purpose(rel_path: str) -> str:
    for substring, tag in PURPOSE_TAGS:
        if substring in rel_path:
            return tag
    return "misc"


def infer_category(filename: str) -> str | None:
    """Return the best category for a loose file, or None if no rule matches."""
    for pattern, category in CATEGORY_RULES:
        if re.search(pattern, filename):
            return category
    return None


def iso_date(ts: float) -> str:
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")


def iso_datetime(ts: float) -> str:
    return datetime.datetime.fromtimestamp(ts).isoformat(timespec="seconds")


# ---------------------------------------------------------------------------
# Scanning
# ---------------------------------------------------------------------------

class FileRecord:
    __slots__ = (
        "path", "rel_path", "name", "ext", "category",
        "size", "mtime", "ctime", "purpose", "sha1",
    )

    def __init__(
        self,
        path: Path,
        rel_path: str,
        category: str,
        compute_hash: bool,
    ) -> None:
        self.path = path
        self.rel_path = rel_path
        self.name = path.name
        self.ext = path.suffix.lower() or "(none)"
        self.category = category
        stat = path.stat()
        self.size: int = int(stat.st_size)
        self.mtime: float = stat.st_mtime
        self.ctime: float = stat.st_birthtime if hasattr(stat, "st_birthtime") else stat.st_ctime
        self.purpose: str = infer_purpose(rel_path)
        self.sha1: str = sha1_prefix(path) if compute_hash else ""


def scan(root: Path, compute_hash: bool = True, quiet: bool = False) -> list[FileRecord]:
    records: list[FileRecord] = []
    for category in CATEGORIES:
        cat_dir = root / category
        if not cat_dir.exists():
            continue
        for entry in sorted(cat_dir.rglob("*")):
            if not entry.is_file():
                continue
            if entry.name in IGNORE_NAMES:
                continue
            # Skip files inside ignored dirs
            if any(part in IGNORE_DIRS for part in entry.relative_to(root).parts[1:]):
                continue
            try:
                rel = str(entry.relative_to(root))
                rec = FileRecord(entry, rel, category, compute_hash)
                records.append(rec)
                if not quiet:
                    print(f"  {rel}")
            except (OSError, PermissionError):
                continue
    return records


def summarize(records: list[FileRecord]) -> dict:
    by_cat: dict[str, dict] = defaultdict(lambda: {"count": 0, "size": 0})
    by_ext: dict[str, int] = defaultdict(int)
    for r in records:
        by_cat[r.category]["count"] += 1
        by_cat[r.category]["size"] += r.size
        by_ext[r.ext] += 1
    total_size = sum(r.size for r in records)
    return {
        "total_files": len(records),
        "total_size": total_size,
        "by_category": dict(by_cat),
        "by_ext": dict(by_ext),
    }


# ---------------------------------------------------------------------------
# Manifest generation
# ---------------------------------------------------------------------------

def generate_manifest(records: list[FileRecord], root: Path) -> str:
    today = datetime.date.today().isoformat()
    summary = summarize(records)
    lines: list[str] = []

    lines.append(f"# Downloads Manifest")
    lines.append(f"")
    lines.append(f"Generated: {today}  ")
    lines.append(f"Root: `{root}`  ")
    lines.append(f"Total files: {summary['total_files']}  ")
    lines.append(f"Total size: {human_size(summary['total_size'])}")
    lines.append("")

    # --- Summary table ---
    lines.append("## Summary by Category")
    lines.append("")
    lines.append("| Category | Files | Total Size | Oldest | Newest |")
    lines.append("|----------|------:|-----------:|--------|--------|")

    for cat in CATEGORIES:
        info = summary["by_category"].get(cat)
        if not info:
            lines.append(f"| {cat} | 0 | — | — | — |")
            continue
        cat_records = [r for r in records if r.category == cat]
        oldest = iso_date(min(r.ctime for r in cat_records))
        newest = iso_date(max(r.mtime for r in cat_records))
        lines.append(
            f"| {cat} | {info['count']} | {human_size(info['size'])} | {oldest} | {newest} |"
        )

    lines.append("")

    # --- Extension breakdown ---
    top_exts = sorted(summary["by_ext"].items(), key=lambda x: x[1], reverse=True)[:15]
    lines.append("## Top File Extensions")
    lines.append("")
    lines.append("| Extension | Count |")
    lines.append("|-----------|------:|")
    for ext, count in top_exts:
        lines.append(f"| `{ext}` | {count} |")
    lines.append("")

    # --- Full file listing ---
    lines.append("## File Listing")
    lines.append("")
    lines.append("| Category | File | Size | Modified | Purpose | SHA1 prefix |")
    lines.append("|----------|------|-----:|----------|---------|-------------|")

    current_cat = None
    for r in sorted(records, key=lambda x: (x.category, x.rel_path)):
        if r.category != current_cat:
            current_cat = r.category
        sha_col = f"`{r.sha1}`" if r.sha1 else "—"
        lines.append(
            f"| {r.category} | `{r.name}` | {human_size(r.size)} "
            f"| {iso_date(r.mtime)} | {r.purpose} | {sha_col} |"
        )

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Auto-filing
# ---------------------------------------------------------------------------

def auto_file(root: Path, execute: bool = False, quiet: bool = False) -> list[tuple[Path, Path]]:
    """
    Find loose files at the Downloads root and propose (or execute) moves
    into category subdirs.  Returns list of (src, dst) pairs.
    """
    moves: list[tuple[Path, Path]] = []
    for entry in sorted(root.iterdir()):
        if not entry.is_file():
            continue
        if entry.name in IGNORE_NAMES:
            continue
        # Skip already-organized files (they live inside a subdir)
        category = infer_category(entry.name)
        if category is None:
            if not quiet:
                print(f"  [skip] {entry.name}  — no rule matched")
            continue
        dst_dir = root / category
        dst = dst_dir / entry.name
        # Avoid clobbering
        if dst.exists():
            stem = entry.stem
            suffix = entry.suffix
            i = 1
            while dst.exists():
                dst = dst_dir / f"{stem} ({i}){suffix}"
                i += 1
        moves.append((entry, dst))
        action = "MOVE" if execute else "would move"
        if not quiet:
            print(f"  [{action}] {entry.name}  →  {category}/{dst.name}")

    if execute:
        for src, dst in moves:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))

    return moves


# ---------------------------------------------------------------------------
# README generation
# ---------------------------------------------------------------------------

def generate_readme(root: Path, records: list[FileRecord]) -> str:
    today = datetime.date.today().isoformat()
    summary = summarize(records)
    lines: list[str] = []

    lines.append("# Downloads — Organization Guide")
    lines.append("")
    lines.append(f"_Last updated: {today}_")
    lines.append("")
    lines.append(
        "This directory is the organized artifact store for Sven / ara.so. "
        "Seven top-level categories hold all tracked files. "
        "Each category is described below along with naming conventions and "
        "maintenance tips."
    )
    lines.append("")

    category_docs: dict[str, dict] = {
        "Legal-Docs": {
            "desc": "Delaware incorporation, contribution agreements, CIIA, consulting "
                    "contracts, invoices, ACH receipts, and YC batch documents for "
                    "Ara Software Inc.",
            "naming": "Keep originals as received. Add a date prefix (`YYYY-MM-DD-`) "
                      "when filing new invoices or signed agreements.",
            "tips": [
                "Signed PDF versions take precedence over `.docx` drafts.",
                "Archive receipts in the form `Receipt-<ID>.pdf`.",
                "YC and Delaware filings live at root level (do not sub-nest).",
            ],
        },
        "Evidence-Bundles": {
            "desc": "Resend email campaign exports, epieos reports, and audit "
                    "snapshots — used for compliance, shareholder record, and "
                    "potential litigation support.",
            "naming": "Bundle directories follow the pattern `share_<service>_<MMMYY>/` "
                      "(e.g. `share_resend_may21/`). Top-level PDFs use the source "
                      "tool name as prefix.",
            "tips": [
                "Never modify files inside a bundle after sealing.",
                "Add a `README.md` to each new bundle describing its scope.",
                "Sensitive CSVs should be gitignored if they contain PII.",
            ],
        },
        "Analytics": {
            "desc": "QA browser-automation reports, PostHog/Amplitude CSV exports, "
                    "payment analytics, and team-member snapshots.",
            "naming": "Zip bundles from CI follow `browser-qa-reports-<run-id>/`. "
                      "Exported CSVs keep the tool-generated filename.",
            "tips": [
                "Unzip bundles immediately; keep the source zip for reference.",
                "Add the export date to any manually renamed file.",
            ],
        },
        "Media": {
            "desc": "Product demo recordings, changelog GIFs, marketing mockups, "
                    "brand animations, and stock photography for ara.so.",
            "naming": "Dated demos: `YYYY-MM-DD-<feature>.(mp4|gif|webp)`. "
                      "Screenshots: `Media/screenshots/YYYY-MM/`. "
                      "Stock photos: `Media/stock-images/`. "
                      "Unclassified video: `Media/video/`.",
            "tips": [
                "Large files (>10 MB) are gitignored — track by path in MANIFEST.md.",
                "Prefer WebP/WebM over PNG/MP4 for marketing assets.",
                "Keep raw `.MOV` recordings separate from edited exports.",
            ],
        },
        "Brand-Assets": {
            "desc": "Ara logo packages, brand kit zip, marketing PDFs, favicons, "
                    "and OpenAra header variants.",
            "naming": "Logo variants: `ara-logo-<color>.png`. "
                      "Zips: `ara-brand-kit.zip`, `Ara logo assets.zip`.",
            "tips": [
                "The canonical brand kit lives in `ara-brand-kit/` (unzipped).",
                "Favicons go in `favicon_io/` — do not scatter them at root.",
                "Marketing PDFs (campaigns, decks) can stay at category root.",
            ],
        },
        "Ara-Builds": {
            "desc": "AraDesktop `.dmg` installers, build artifact zips, "
                    "and third-party app installers downloaded for evaluation.",
            "naming": "Ara releases: `Ara_<version>_<arch>.dmg`. "
                      "Third-party: keep original installer name.",
            "tips": [
                "Binary files are gitignored — only `.gitkeep` is committed.",
                "Delete superseded Ara DMGs once v+1 is stable.",
                "Evaluation DMGs from other vendors live here temporarily.",
            ],
        },
        "Misc": {
            "desc": "Bundled app skill archives, research papers, web templates, "
                    "Raycast configs, personal docs, and items pending classification.",
            "naming": "No strict convention. Add a date or short context prefix "
                      "for anything not obviously self-describing.",
            "tips": [
                "Review Misc quarterly and promote files to a real category or delete.",
                "Commit log files (commit-summary-*.md) only if they need long-term audit.",
                "The `yes/` sub-folder holds photography exports — migrate to Media/photos/.",
            ],
        },
    }

    for cat in CATEGORIES:
        info = summary["by_category"].get(cat, {"count": 0, "size": 0})
        doc = category_docs.get(cat, {})
        lines.append(f"## {cat}")
        lines.append("")
        lines.append(
            f"**{info['count']} files — {human_size(info['size'])}**"
        )
        lines.append("")
        if doc.get("desc"):
            lines.append(doc["desc"])
            lines.append("")
        if doc.get("naming"):
            lines.append(f"_Naming convention:_ {doc['naming']}")
            lines.append("")
        if doc.get("tips"):
            for tip in doc["tips"]:
                lines.append(f"- {tip}")
            lines.append("")

    # --- Tooling section ---
    lines.append("## Tooling")
    lines.append("")
    lines.append(
        "All scripts live in `scripts/` and require only the Python 3 stdlib "
        "(no pip installs, except optional `pyyaml` for project-override support)."
    )
    lines.append("")
    lines.append("| Script | Purpose |")
    lines.append("|--------|---------|")
    lines.append(
        "| `organize-downloads.py` | All-in-one: scan, manifest, auto-file, README. "
        "Run `python3 organize-downloads.py --help` for full usage. |"
    )
    lines.append(
        "| `catalog-downloads.py` | Deep CSV manifest with SHA-1 hashes; "
        "designed for launchd cron. |"
    )
    lines.append(
        "| `tag-projects.py` | Assigns `project` labels (ara-cua, ara-so-site, …) "
        "to manifest rows. |"
    )
    lines.append(
        "| `build-catalog-site.py` | Generates a static HTML search UI from the CSV manifest. |"
    )
    lines.append("")

    lines.append("### Quick-start")
    lines.append("")
    lines.append("```bash")
    lines.append("# Full refresh: scan → markdown manifest → README")
    lines.append("python3 scripts/organize-downloads.py")
    lines.append("")
    lines.append("# Preview what auto-filing would move (no changes)")
    lines.append("python3 scripts/organize-downloads.py auto-file")
    lines.append("")
    lines.append("# Actually move loose root files into categories")
    lines.append("python3 scripts/organize-downloads.py auto-file --execute")
    lines.append("")
    lines.append("# Deep CSV manifest + project tags (for the catalog site)")
    lines.append("python3 scripts/catalog-downloads.py && python3 scripts/tag-projects.py")
    lines.append("```")
    lines.append("")

    lines.append("## Git Policy")
    lines.append("")
    lines.append(
        "The Downloads folder is a git repo (`github.com/Aradotso/ara-cua` mirror "
        "branch or standalone). The `.gitignore` excludes large binaries (`.dmg`, "
        "loose images, video), so only text-based artifacts and small assets are "
        "tracked."
    )
    lines.append("")
    lines.append(
        "Run `git add -A && git commit -m 'chore: refresh downloads catalog'` "
        "after significant additions or after running the organizer."
    )
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="organize-downloads — scan, catalog, auto-file, and document ~/Downloads",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument(
        "mode",
        nargs="?",
        default="all",
        choices=["scan", "manifest", "auto-file", "readme", "all"],
        help="What to do (default: all)",
    )
    p.add_argument(
        "--downloads",
        metavar="PATH",
        default=str(Path.home() / "Downloads"),
        help="Root of the Downloads folder (default: ~/Downloads)",
    )
    p.add_argument(
        "--out",
        metavar="PATH",
        default=None,
        help="Output directory for manifest + README (default: <downloads>/docs)",
    )
    p.add_argument(
        "--execute",
        action="store_true",
        help="For auto-file: actually move files (default is dry-run)",
    )
    p.add_argument(
        "--no-hash",
        action="store_true",
        help="Skip SHA-1 computation (faster on large trees)",
    )
    p.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress per-file output",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(args.downloads).expanduser().resolve()
    if not root.exists():
        print(f"ERROR: Downloads root not found: {root}", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(args.out).expanduser().resolve() if args.out else root / "docs"

    mode = args.mode

    # ---- scan / all ----
    records: list[FileRecord] = []
    if mode in ("scan", "manifest", "readme", "all"):
        print(f"Scanning {root} …")
        records = scan(root, compute_hash=not args.no_hash, quiet=args.quiet)
        s = summarize(records)
        print(f"\nTotal: {s['total_files']} files, {human_size(s['total_size'])}")
        print("By category:")
        for cat in CATEGORIES:
            info = s["by_category"].get(cat, {"count": 0, "size": 0})
            print(f"  {cat:<20} {info['count']:>5} files   {human_size(info['size']):>10}")
        print()

    # ---- manifest ----
    if mode in ("manifest", "all"):
        print("Generating MANIFEST.md …")
        manifest_text = generate_manifest(records, root)
        out_dir.mkdir(parents=True, exist_ok=True)
        manifest_path = out_dir / "MANIFEST.md"
        manifest_path.write_text(manifest_text, encoding="utf-8")
        print(f"  Written → {manifest_path}")

    # ---- auto-file ----
    if mode == "auto-file":
        label = "Executing" if args.execute else "Previewing (dry-run)"
        print(f"{label} auto-file for loose root files in {root} …")
        moves = auto_file(root, execute=args.execute, quiet=args.quiet)
        if not moves:
            print("  No loose files matched any category rule.")
        else:
            print(f"\n  {len(moves)} file(s) {'moved' if args.execute else 'would be moved'}.")
            if not args.execute:
                print("  Re-run with --execute to apply.")

    # ---- readme ----
    if mode in ("readme", "all"):
        if not records:
            print("Scanning for README generation …")
            records = scan(root, compute_hash=False, quiet=True)
        print("Generating ORGANIZED-README.md …")
        readme_text = generate_readme(root, records)
        out_dir.mkdir(parents=True, exist_ok=True)
        readme_path = out_dir / "ORGANIZED-README.md"
        readme_path.write_text(readme_text, encoding="utf-8")
        print(f"  Written → {readme_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
