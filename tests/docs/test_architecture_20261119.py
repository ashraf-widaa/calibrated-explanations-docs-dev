"""Guards for the 2026-11-19 navigation architecture.

The sidebar root is Home, Get Started, the four documentation sections and
Project & Resources. Get Started links to the complete Python journey and
the browser Quick Start. Each section hub parents its pages through a real toctree,
no page has two sidebar parents, and no compulsory ML-essentials step remains.
"""

from __future__ import annotations

import posixpath
import re
from collections import Counter
from pathlib import Path

DOCS = Path(__file__).resolve().parents[2] / "docs"
TOCTREE = re.compile(r"^```\{toctree\}\n(.*?)^```", re.DOTALL | re.MULTILINE)


def _text(rel: str) -> str:
    return (DOCS / rel).read_text(encoding="utf-8").replace("\r\n", "\n")


def _entries(rel: str) -> list[tuple[str | None, str]]:
    found = []
    for block in TOCTREE.findall(_text(rel)):
        for line in block.splitlines():
            line = line.strip()
            if not line or line.startswith(":") or line.endswith("<self>"):
                continue
            m = re.match(r"(.*?)\s*<([^>]+)>$", line)
            label, target = (m.group(1), m.group(2)) if m else (None, line)
            if "://" not in target:
                target = posixpath.normpath(posixpath.join(posixpath.dirname(rel), target))
            found.append((label, target))
    return found


def test_sidebar_root_is_home_quick_start_four_sections_and_project() -> None:
    assert [label for label, _ in _entries("index.md")] == [
        "Get Started",
        "CE: What & Why",
        "How CE Works",
        "CE in Practice",
        "CE Software & Integration",
        "Project & Resources",
    ]
    assert "Home <self>" in _text("index.md")


def test_section_hubs_parent_their_pages_in_reading_order() -> None:
    expected = {
        "sections/what-and-why.md": [
            "what-is-ce", "get-started/why-ce", "get-started/ce-tasks-and-modes", "compare",
        ],
        "sections/how-ce-works.md": [
            "foundations/concepts/ce_workflow",
            "foundations/concepts/calibration_methods",
            "foundations/concepts/alternatives",
            "foundations/concepts/calibrated_interval_semantics",
        ],
        "sections/in-practice.md": [
            "https://calibrated-explanations-demo.ju.se/expert",
            "https://games.grejna.ai/",
            "practitioner/index",
            "tutorials/index",
            "tasks/index",
        ],
        "sections/software-integration.md": [
            "get-started/installation",
            "get-started/troubleshooting",
            "get-started/quick_api",
            "get-started/apply-to-your-data",
            "foundations/how-to/integrate_with_pipelines",
            "api/index",
            "foundations/how-to/configure_runtime",
            "plugins",
        ],
        "sections/project-evolution.md": ["glossary/index", "researcher/index", "contributor/index"],
    }
    for hub, pages in expected.items():
        targets = [target for _, target in _entries(hub)]
        assert [target for target in targets if target in pages] == pages, hub


def test_no_page_has_two_sidebar_parents() -> None:
    counts = Counter()
    for path in DOCS.rglob("*.md"):
        rel = path.relative_to(DOCS).as_posix()
        if rel.startswith(("_", "_build")):
            continue
        counts.update(target for _, target in _entries(rel))
    assert [t for t, n in counts.items() if n > 1] == []


def test_ml_essentials_is_optional_not_a_navigation_step() -> None:
    assert _text("get-started/ml-foundations.md").startswith("---\norphan: true\n---")
    for path in DOCS.rglob("*.md"):
        rel = path.relative_to(DOCS).as_posix()
        assert "get-started/ml-foundations" not in [t for _, t in _entries(rel)], rel


def test_get_started_links_to_browser_and_python_journeys() -> None:
    assert _entries("get-started/index.md") == [
        ("Quick Start: Try CE in Your Browser", "get-started/try-in-browser"),
        ("Quickstart", "get-started/quickstart"),
        ("Read Your First Explanation", "foundations/how-to/interpret_explanations"),
        ("Evaluate CE", "practitioner/evaluate_ce"),
        ("CE by Example (No Code)", "get-started/ce-by-example"),
        ("Coming from SHAP or LIME", "get-started/coming-from-shap-lime"),
    ]
