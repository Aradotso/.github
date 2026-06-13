#!/usr/bin/env python3
"""Validate the public GitHub organization profile before merge."""

from __future__ import annotations

import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PROFILE_DIR = ROOT / "profile"
README = PROFILE_DIR / "README.md"
LOGO = PROFILE_DIR / "logo.png"
HERO = PROFILE_DIR / "hero.png"

MIN_README_BYTES = 20
LOGO_EXPECTED_SIZE = (512, 512)
LOGO_MAX_BYTES = 500_000
HERO_MIN_WIDTH = 1000
HERO_MIN_ASPECT_RATIO = 1.3
HERO_MAX_BYTES = 2_000_000
REQUIRED_TAGS = {"h1", "a", "img"}

failures: list[str] = []
warnings: list[str] = []


class ProfileHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: set[str] = set()
        self.hrefs: list[str] = []
        self.image_sources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.add(tag.lower())
        values = dict(attrs)
        if tag.lower() == "a" and values.get("href"):
            self.hrefs.append(values["href"] or "")
        if tag.lower() == "img" and values.get("src"):
            self.image_sources.append(values["src"] or "")


def fail(message: str) -> None:
    failures.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def png_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or not header.startswith(b"\x89PNG\r\n\x1a\n"):
        fail(f"{path.relative_to(ROOT)} is not a valid PNG")
        return None
    return struct.unpack(">II", header[16:24])


def check_image(path: Path, *, expected: tuple[int, int] | None = None, min_width: int | None = None, min_ratio: float | None = None, max_bytes: int) -> None:
    rel = path.relative_to(ROOT)
    if not path.exists():
        fail(f"{rel} is missing")
        return
    size = path.stat().st_size
    if size > max_bytes:
        fail(f"{rel} is {size:,} bytes; limit is {max_bytes:,} bytes")
    dimensions = png_size(path)
    if not dimensions:
        return
    width, height = dimensions
    if expected and dimensions != expected:
        fail(f"{rel} is {width}x{height}; expected {expected[0]}x{expected[1]}")
    if min_width and width < min_width:
        fail(f"{rel} width is {width}px; minimum is {min_width}px")
    if min_ratio and height and width / height < min_ratio:
        fail(f"{rel} aspect ratio is {width / height:.2f}; minimum is {min_ratio:.2f}")


def check_markdown_balance(content: str) -> None:
    fence_count = len(re.findall(r"^```", content, flags=re.MULTILINE))
    if fence_count % 2:
        fail("profile/README.md has an unclosed fenced code block")

    for marker in ("**", "__"):
        if content.count(marker) % 2:
            fail(f"profile/README.md has unbalanced {marker} emphasis markers")

    for marker in ("[", "]", "(", ")"):
        if content.count(marker) != content.count({"[": "]", "]": "[", "(": ")", ")": "("}[marker]):
            fail("profile/README.md has unbalanced link punctuation")
            break


def check_local_image_reference(src: str) -> None:
    if src.startswith(("http://", "https://", "data:")):
        return
    target = (PROFILE_DIR / src).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(f"profile/README.md image escapes repository: {src}")
        return
    if not target.exists():
        fail(f"profile/README.md references missing image: {src}")


def check_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return
    request = Request(url, headers={"User-Agent": "Ara-Profile-Health-Check/1.0"}, method="GET")
    try:
        with urlopen(request, timeout=15) as response:
            status = getattr(response, "status", 200)
            if status >= 400:
                fail(f"profile/README.md link returned HTTP {status}: {url}")
    except HTTPError as exc:
        if 300 <= exc.code < 400 and exc.headers.get("Location"):
            return
        fail(f"profile/README.md link returned HTTP {exc.code}: {url}")
    except (TimeoutError, URLError) as exc:
        fail(f"profile/README.md link is unreachable: {url} ({exc})")


def check_readme() -> None:
    if not README.exists():
        fail("profile/README.md is missing")
        return
    content = README.read_text(encoding="utf-8")
    if len(content.strip()) < MIN_README_BYTES:
        fail("profile/README.md is empty or too small")

    parser = ProfileHtmlParser()
    parser.feed(content)
    missing_tags = sorted(REQUIRED_TAGS - parser.tags)
    if missing_tags:
        fail(f"profile/README.md is missing required HTML tags: {', '.join(missing_tags)}")
    if not parser.hrefs:
        fail("profile/README.md does not include any outbound profile link")
    if not parser.image_sources:
        fail("profile/README.md does not include any image")

    check_markdown_balance(content)
    for src in parser.image_sources:
        check_local_image_reference(src)
    for href in parser.hrefs:
        check_url(href)


def main() -> int:
    check_readme()
    check_image(LOGO, expected=LOGO_EXPECTED_SIZE, max_bytes=LOGO_MAX_BYTES)
    check_image(HERO, min_width=HERO_MIN_WIDTH, min_ratio=HERO_MIN_ASPECT_RATIO, max_bytes=HERO_MAX_BYTES)

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    if failures:
        print("Profile health check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Profile health check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
