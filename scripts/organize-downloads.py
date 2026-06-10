#!/usr/bin/env python3
"""
organize-downloads.py
=====================
Scans ~/Downloads, generates a manifest (MANIFEST.md), and optionally
auto-files loose items into the correct subdirectory.

Usage
-----
  # Dry-run: generate manifest only, no moves
  python3 scripts/organize-downloads.py

  # Auto-file loose items (moves files into correct subdirectories)
  python3 scripts/organize-downloads.py --auto-file

  # Point at a different Downloads root
  python3 scripts/organize-downloads.py --root /path/to/folder

Output
------
  - scripts/MANIFEST.md   (written next to this script)
  - stdout summary
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DOWNLOADS_ROOT = Path.home() / "Downloads"

# Canonical subdirectories and their purpose tags
CATEGORIES: dict[str, dict] = {
    "Legal-Docs": {
        "tag": "legal",
        "description": "Delaware incorporation, contribution agreements, CIIA, consulting contracts, invoices, and ACH receipts.",
        "patterns": [
            r"(?i)(legal|agreement|contract|invoice|receipt|incorporat|CIIA|board.consent|contribution|attorney|law|notary|certificate|annual.report|bookface|yc.company|y.combinator.batch|mercury|edumame|filing|letter.*advocacy|letter.*administration|letter.*committee)",
            r"(?i)(SIGNED|DRAFT).*\.(pdf|docx?)$",
        ],
    },
    "Evidence-Bundles": {
        "tag": "evidence",
        "description": "Resend email evidence exports and epieos reports — compliance and audit trails.",
        "patterns": [
            r"(?i)(evidence|resend|epieos|epistios|share_resend|email.proof|audit)",
        ],
    },
    "Analytics": {
        "tag": "analytics",
        "description": "QA reports, browser automation report ZIPs, team CSVs, and payment analytics exports.",
        "patterns": [
            r"(?i)(analytics|browser.qa.report|qa.report|Report\.pdf|team.member|unified.payment|payments\.csv|\.csv$)",
        ],
    },
    "Media": {
        "tag": "media",
        "description": "Marketing assets, product demo recordings, GIFs, screenshots, and visual content.",
        "patterns": [
            r"(?i)\.(mp4|mov|webm|webp|gif|jpg|jpeg|png|heic|svg|m4a|mp3|avif)$",
        ],
    },
    "Brand-Assets": {
        "tag": "brand",
        "description": "Ara logo packages, brand kit, marketing PDFs, favicons, and header images.",
        "patterns": [
            r"(?i)(logo|brand.kit|brand.asset|marketing.campaign|favicon|openara.header)",
        ],
    },
    "Ara-Builds": {
        "tag": "builds",
        "description": "AraDesktop .dmg installers and build artifacts.",
        "patterns": [
            r"(?i)(Ara_\d+\.\d+|ara.so.demo.result|ara.so.morph.result|\.dmg$)",
        ],
    },
    "Misc": {
        "tag": "misc",
        "description": "Bundled app skills, research papers, archived exports, and miscellaneous downloads.",
        "patterns": [],  # catch-all — used only when nothing else matches
    },
}

# Files / dirs that live at root and should stay there
ROOT_KEEPERS = {".git", ".gitignore", ".DS_Store", ".localized", "README.md", "ASSET-USAGE-MAP.md"}

SKIP_EXTENSIONS = {".app", ""}  # directories or extensionless entries handled separately


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def human_size(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def creation_date(path: Path) -> str:
    try:
        stat = path.stat()
        ts = getattr(stat, "st_birthtime", stat.st_mtime)
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    except OSError:
        return "unknown"


def dir_size(path: Path) -> int:
    total = 0
    try:
        for p in path.rglob("*"):
            if p.is_file():
                try:
                    total += p.stat().st_size
                except OSError:
                    pass
    except PermissionError:
        pass
    return total


def categorize(path: Path) -> str:
    """Return the best category name for a loose root-level item."""
    name = path.name
    for cat, meta in CATEGORIES.items():
        if cat == "Misc":
            continue
        for pat in meta["patterns"]:
            if re.search(pat, name):
                return cat
    return "Misc"


# ---------------------------------------------------------------------------
# Scanner
# ---------------------------------------------------------------------------

def scan(root: Path) -> tuple[dict, list[Path]]:
    """Walk root, collect per-category stats and per-file metadata."""
    data: dict[str, dict] = {
        cat: {"files": [], "total_bytes": 0, "file_count": 0}
        for cat in CATEGORIES
    }
    loose: list[Path] = []  # items at root that aren't in a category dir

    for entry in sorted(root.iterdir()):
        if entry.name.startswith(".") or entry.name in ROOT_KEEPERS:
            continue

        if entry.name in CATEGORIES:
            # It IS a category directory — walk it
            cat = entry.name
            for path in sorted(entry.rglob("*")):
                if path.name.startswith("."):
                    continue
                if path.is_file():
                    try:
                        size = path.stat().st_size
                    except OSError:
                        size = 0
                    data[cat]["files"].append({
                        "path": str(path.relative_to(root)),
                        "size": size,
                        "created": creation_date(path),
                    })
                    data[cat]["total_bytes"] += size
                    data[cat]["file_count"] += 1
        else:
            # Loose item at root
            loose.append(entry)

    # Classify loose items into their best category bucket for reporting
    for item in loose:
        cat = categorize(item)
        if item.is_file():
            try:
                size = item.stat().st_size
            except OSError:
                size = 0
            data[cat]["files"].append({
                "path": item.name,
                "size": size,
                "created": creation_date(item),
                "loose": True,
            })
            data[cat]["total_bytes"] += size
            data[cat]["file_count"] += 1
        elif item.is_dir():
            sz = dir_size(item)
            data[cat]["files"].append({
                "path": item.name + "/",
                "size": sz,
                "created": creation_date(item),
                "loose": True,
                "is_dir": True,
            })
            data[cat]["total_bytes"] += sz
            data[cat]["file_count"] += 1

    return data, loose


# ---------------------------------------------------------------------------
# Manifest generator
# ---------------------------------------------------------------------------

def generate_manifest(root: Path, data: dict, loose: list[Path], out_path: Path) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M %Z").strip()
    lines = [
        f"# Downloads Manifest",
        f"",
        f"_Generated: {now}_  ",
        f"_Root: `{root}`_",
        f"",
        "---",
        "",
        "## Summary",
        "",
    ]

    total_files = sum(v["file_count"] for v in data.values())
    total_bytes = sum(v["total_bytes"] for v in data.values())
    lines += [
        f"| Category | Files | Size | Tag |",
        f"|----------|------:|-----:|-----|",
    ]
    for cat, meta in CATEGORIES.items():
        d = data[cat]
        tag = meta["tag"]
        lines.append(
            f"| {cat} | {d['file_count']} | {human_size(d['total_bytes'])} | `{tag}` |"
        )
    lines += [
        f"| **Total** | **{total_files}** | **{human_size(total_bytes)}** | — |",
        "",
        "---",
        "",
    ]

    if loose:
        lines += [
            f"## Loose Root Items ({len(loose)} items — not yet filed)",
            "",
            "| Name | Suggested Category | Size | Created |",
            "|------|-------------------|-----:|---------|",
        ]
        for item in sorted(loose, key=lambda p: p.name.lower()):
            sz = item.stat().st_size if item.is_file() else dir_size(item)
            suggested = categorize(item)
            created = creation_date(item)
            name = item.name + ("/" if item.is_dir() else "")
            lines.append(f"| `{name}` | {suggested} | {human_size(sz)} | {created} |")
        lines += ["", "---", ""]

    for cat, meta in CATEGORIES.items():
        d = data[cat]
        if d["file_count"] == 0:
            continue
        lines += [
            f"## {cat}  ·  `{meta['tag']}`",
            f"",
            f"_{meta['description']}_",
            f"",
            f"**{d['file_count']} files · {human_size(d['total_bytes'])}**",
            f"",
            f"| File | Size | Created | Loose? |",
            f"|------|-----:|---------|--------|",
        ]
        for f in d["files"]:
            loose_flag = "⚠️ at root" if f.get("loose") else ""
            lines.append(
                f"| `{f['path']}` | {human_size(f['size'])} | {f['created']} | {loose_flag} |"
            )
        lines += ["", "---", ""]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[manifest] Written → {out_path}")


# ---------------------------------------------------------------------------
# Auto-filer
# ---------------------------------------------------------------------------

def auto_file(root: Path, loose: list[Path], dry_run: bool = False) -> None:
    """Move loose root items into their suggested category subdirectory."""
    moved = 0
    skipped = 0
    for item in loose:
        cat = categorize(item)
        dest_dir = root / cat
        dest_dir.mkdir(exist_ok=True)
        dest = dest_dir / item.name

        # Don't overwrite
        if dest.exists():
            print(f"[skip] {item.name} → {cat}/ (destination exists)")
            skipped += 1
            continue

        action = "MOVE" if not dry_run else "WOULD MOVE"
        print(f"[{action}] {item.name} → {cat}/")
        if not dry_run:
            shutil.move(str(item), str(dest))
            moved += 1

    print(f"\n[auto-file] {'Moved' if not dry_run else 'Would move'} {moved} items. Skipped {skipped}.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Downloads folder organizer")
    parser.add_argument("--root", default=str(DOWNLOADS_ROOT), help="Path to Downloads folder")
    parser.add_argument("--auto-file", action="store_true", help="Move loose root items into subdirs")
    parser.add_argument("--dry-run", action="store_true", help="Preview moves without executing (implies --auto-file preview)")
    parser.add_argument("--manifest-out", default=None, help="Where to write MANIFEST.md (default: next to this script)")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        print(f"Error: {root} is not a directory", file=sys.stderr)
        sys.exit(1)

    script_dir = Path(__file__).parent
    manifest_out = Path(args.manifest_out) if args.manifest_out else script_dir / "MANIFEST.md"

    print(f"[scan] Scanning {root} …")
    data, loose = scan(root)

    total_files = sum(v["file_count"] for v in data.values())
    total_bytes = sum(v["total_bytes"] for v in data.values())
    print(f"[scan] {total_files} files · {human_size(total_bytes)} total")
    print(f"[scan] {len(loose)} loose items at root")

    generate_manifest(root, data, loose, manifest_out)

    if args.auto_file or args.dry_run:
        if not loose:
            print("[auto-file] Nothing loose to file.")
        else:
            auto_file(root, loose, dry_run=args.dry_run)

    print("\nDone.")


if __name__ == "__main__":
    main()
