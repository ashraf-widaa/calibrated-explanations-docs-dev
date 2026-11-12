"""Check every internal link and anchor in a built Sphinx HTML site.

Usage::

    python scripts/docs/check_internal_links.py <html-build-dir> [<baseline-build-dir>]

Exits with status 1 if any relative ``href`` points to a missing page or to a
missing ``#anchor``. With a baseline build, it also reports pages that were
removed or added, so navigation changes can be reviewed.
External links (``http(s):``, ``mailto:``) are not checked.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


def pages(root: Path) -> set[str]:
    return {
        p.relative_to(root).as_posix()
        for p in root.rglob("*.html")
        if "_static" not in p.parts and "_sources" not in p.parts
    }


def broken_links(root: Path) -> list[tuple[str, str]]:
    found = pages(root)
    ids = {p: set(re.findall(r'id="([^"]+)"', (root / p).read_text(encoding="utf-8"))) for p in found}
    broken = []
    for page in found:
        for href in re.findall(r'href="([^"]+)"', (root / page).read_text(encoding="utf-8")):
            href = html.unescape(href)
            if re.match(r"^[a-z]+:", href) or href.startswith("//"):
                continue
            url = urlsplit(href)
            target = (PurePosixPath(page).parent / unquote(url.path)).as_posix() if url.path else page
            parts: list[str] = []
            for segment in target.split("/"):
                if segment == "..":
                    if parts:
                        parts.pop()
                elif segment not in (".", ""):
                    parts.append(segment)
            resolved = "/".join(parts)
            missing_page = not (root / resolved).exists()
            missing_anchor = bool(url.fragment) and resolved in ids and url.fragment not in ids[resolved]
            if missing_page or missing_anchor:
                broken.append((page, href))
    return broken


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    root = Path(argv[0])
    broken = broken_links(root)
    print(f"pages={len(pages(root))} broken_links={len(broken)}")
    for page, href in broken[:50]:
        print(f"  {page} -> {href}")
    if len(argv) > 1:
        before, after = pages(Path(argv[1])), pages(root)
        print(f"removed={sorted(before - after)}")
        print(f"added={sorted(after - before)}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
