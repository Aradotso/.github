#!/usr/bin/env python3
"""
Ara org profile health checker.

Validates:
  1. Logo size (logo.png must be exactly 512×512, RGBA).
  2. Hero image size (hero.png, 1280×768 or wider, RGB).
  3. Social links in profile/README.md are reachable (HTTP 2xx or 3xx).
  4. README markup is valid HTML (no unclosed tags in the key blocks).
  5. CHANGELOG.md exists and was updated within MAX_CHANGELOG_AGE_DAYS.

On failure, either files a GitHub issue (if GITHUB_TOKEN + GITHUB_REPO set) or
posts to Slack (if SLACK_WEBHOOK_URL set).

Exit code: 0 = all checks passed, 1 = one or more failed.
"""

from __future__ import annotations

import os
import re
import sys
import json
import urllib.request
import urllib.error
import datetime
import struct
import zlib
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

PROFILE_DIR = Path(__file__).parent.parent / "profile"
LOGO_PATH = PROFILE_DIR / "logo.png"
HERO_PATH = PROFILE_DIR / "hero.png"
README_PATH = PROFILE_DIR / "README.md"
CHANGELOG_PATH = Path(__file__).parent.parent / "CHANGELOG.md"

LOGO_EXPECTED_SIZE = (512, 512)
LOGO_EXPECTED_MODE = "RGBA"
HERO_MIN_WIDTH = 1280
HERO_MIN_HEIGHT = 640

MAX_CHANGELOG_AGE_DAYS = 90  # flag if no entry within this many days

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO = os.environ.get("GITHUB_REPO", "Aradotso/.github")  # owner/repo
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")

# ── Minimal PNG size reader (no Pillow required) ───────────────────────────────

def read_png_dimensions(path: Path) -> tuple[int, int, str]:
    """Return (width, height, mode_str) by reading PNG IHDR chunk directly."""
    with open(path, "rb") as f:
        sig = f.read(8)
        if sig != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"{path} is not a valid PNG")
        # IHDR is always the first chunk
        length_bytes = f.read(4)
        chunk_type = f.read(4)
        if chunk_type != b"IHDR":
            raise ValueError(f"{path} IHDR chunk missing")
        data = f.read(struct.unpack(">I", length_bytes)[0])
        width = struct.unpack(">I", data[0:4])[0]
        height = struct.unpack(">I", data[4:8])[0]
        bit_depth = data[8]
        color_type = data[9]
        color_type_map = {0: "L", 2: "RGB", 3: "P", 4: "LA", 6: "RGBA"}
        mode = color_type_map.get(color_type, f"unknown({color_type})")
    return width, height, mode


# ── Individual checks ─────────────────────────────────────────────────────────

def check_logo() -> list[str]:
    issues = []
    if not LOGO_PATH.exists():
        issues.append(f"logo.png not found at {LOGO_PATH}")
        return issues
    try:
        w, h, mode = read_png_dimensions(LOGO_PATH)
    except Exception as e:
        issues.append(f"logo.png unreadable: {e}")
        return issues
    if (w, h) != LOGO_EXPECTED_SIZE:
        issues.append(
            f"logo.png size is {w}×{h}, expected {LOGO_EXPECTED_SIZE[0]}×{LOGO_EXPECTED_SIZE[1]}"
        )
    if mode != LOGO_EXPECTED_MODE:
        issues.append(f"logo.png color mode is {mode}, expected {LOGO_EXPECTED_MODE} (needs alpha channel)")
    return issues


def check_hero() -> list[str]:
    issues = []
    if not HERO_PATH.exists():
        issues.append(f"hero.png not found at {HERO_PATH}")
        return issues
    try:
        w, h, mode = read_png_dimensions(HERO_PATH)
    except Exception as e:
        issues.append(f"hero.png unreadable: {e}")
        return issues
    if w < HERO_MIN_WIDTH:
        issues.append(f"hero.png width {w}px < minimum {HERO_MIN_WIDTH}px")
    if h < HERO_MIN_HEIGHT:
        issues.append(f"hero.png height {h}px < minimum {HERO_MIN_HEIGHT}px")
    return issues


def check_social_links() -> list[str]:
    issues = []
    if not README_PATH.exists():
        issues.append(f"README.md not found at {README_PATH}")
        return issues
    content = README_PATH.read_text(encoding="utf-8")
    # Extract all URLs from href= and src= attributes plus bare Markdown links
    urls = re.findall(r'href=["\']([^"\']+)["\']', content)
    urls += re.findall(r'\]\(([^)]+)\)', content)
    # Keep only http(s) links
    urls = [u for u in urls if u.startswith("http")]
    # Deduplicate preserving order
    seen: set[str] = set()
    unique_urls = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            unique_urls.append(u)

    for url in unique_urls:
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Ara-Profile-Health-Check/1.0"},
                method="HEAD",
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                code = resp.status
        except urllib.error.HTTPError as e:
            code = e.code
        except Exception as e:
            issues.append(f"Link unreachable — {url}: {e}")
            continue
        if code >= 400:
            issues.append(f"Link returned HTTP {code}: {url}")
    return issues


def check_readme_markup() -> list[str]:
    """Basic sanity: every opening tag has a matching close (for the tags we care about)."""
    issues = []
    if not README_PATH.exists():
        issues.append(f"README.md not found at {README_PATH}")
        return issues
    content = README_PATH.read_text(encoding="utf-8")
    # Check paired HTML tags used in the Ara profile README
    for tag in ("p", "h1", "h2", "picture"):
        opens = len(re.findall(rf"<{tag}[\s>]", content, re.IGNORECASE))
        closes = len(re.findall(rf"</{tag}>", content, re.IGNORECASE))
        if opens != closes:
            issues.append(
                f"README.md: <{tag}> tag mismatch — {opens} open, {closes} close"
            )
    # Check for bare HTTP links (not wrapped in anchor tags) — style drift
    bare = re.findall(r'(?<!["\(])https?://[^\s"\')<>]+', content)
    # Exclude ones that are already inside href/src
    in_attr = set(re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content))
    loose = [u for u in bare if u not in in_attr]
    if loose:
        issues.append(
            f"README.md has {len(loose)} bare URL(s) not wrapped in anchors: {loose[:3]}"
        )
    return issues


def check_changelog() -> list[str]:
    issues = []
    if not CHANGELOG_PATH.exists():
        issues.append(
            "CHANGELOG.md missing — create one to track profile changes over time"
        )
        return issues
    content = CHANGELOG_PATH.read_text(encoding="utf-8")
    # Look for a date stamp in the format YYYY-MM-DD
    dates = re.findall(r"\b(\d{4}-\d{2}-\d{2})\b", content)
    if not dates:
        issues.append("CHANGELOG.md has no dated entries (expected YYYY-MM-DD format)")
        return issues
    try:
        latest = max(datetime.date.fromisoformat(d) for d in dates)
    except ValueError:
        issues.append("CHANGELOG.md has unparseable date entries")
        return issues
    age = (datetime.date.today() - latest).days
    if age > MAX_CHANGELOG_AGE_DAYS:
        issues.append(
            f"CHANGELOG.md last entry is {age} days old (>{MAX_CHANGELOG_AGE_DAYS}). "
            "Please add an entry for recent profile changes."
        )
    return issues


# ── Reporting ─────────────────────────────────────────────────────────────────

def file_github_issue(title: str, body: str) -> None:
    if not GITHUB_TOKEN or not GITHUB_REPO:
        print("[skip] GitHub issue filing skipped — GITHUB_TOKEN or GITHUB_REPO not set")
        return
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    payload = json.dumps(
        {
            "title": title,
            "body": body,
            "labels": ["profile-health", "automated"],
        }
    ).encode()
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
            print(f"[github] Issue filed: {data.get('html_url', '(no url)')}")
    except Exception as e:
        print(f"[github] Failed to file issue: {e}")


def post_slack(text: str) -> None:
    if not SLACK_WEBHOOK_URL:
        print("[skip] Slack notification skipped — SLACK_WEBHOOK_URL not set")
        return
    payload = json.dumps({"text": text}).encode()
    req = urllib.request.Request(
        SLACK_WEBHOOK_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10):
            print("[slack] Notification sent")
    except Exception as e:
        print(f"[slack] Failed to send notification: {e}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    checks = [
        ("Logo size/mode", check_logo),
        ("Hero image", check_hero),
        ("Social links", check_social_links),
        ("README markup", check_readme_markup),
        ("CHANGELOG", check_changelog),
    ]

    all_issues: list[str] = []
    for name, fn in checks:
        result = fn()
        if result:
            print(f"[FAIL] {name}:")
            for issue in result:
                print(f"  • {issue}")
            all_issues.extend(result)
        else:
            print(f"[OK]   {name}")

    if all_issues:
        summary_lines = "\n".join(f"- {i}" for i in all_issues)
        issue_title = "🚨 Org profile health check failed"
        issue_body = (
            "The automated profile health check detected the following issues:\n\n"
            + summary_lines
            + "\n\nPlease review [`profile/`](./profile/) and update accordingly."
        )
        slack_text = (
            f":warning: *Ara org profile health check failed* "
            f"({len(all_issues)} issue(s)):\n{summary_lines}"
        )
        file_github_issue(issue_title, issue_body)
        post_slack(slack_text)
        print(f"\n{len(all_issues)} issue(s) found.")
        return 1

    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
