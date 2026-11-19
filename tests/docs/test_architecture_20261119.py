"""Guards for the five-section navigation architecture (redesign of 2026-11-19).

The sidebar root is Home and five sections: Get started, Understand CE, Use CE,
Software Architecture & Integration, and Project. Get started is one path with the
browser Quick Start before installation. Each section hub parents its pages through a
real toctree, no page has two sidebar parents, ML foundations close Understand CE, and
API Reference and Contribute in 4 steps are direct children of the software section.
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


def test_sidebar_root_is_home_and_five_sections() -> None:
    assert _entries("index.md") == [
        ("Get Started", "get-started/index"),
        ("Understand CE", "sections/understand-ce"),
        ("Use CE", "sections/in-practice"),
        ("Software Architecture & Integration", "sections/software-integration"),
        ("Project", "sections/project-evolution"),
    ]
    assert "Home <self>" in _text("index.md")


def test_section_hubs_parent_their_pages_in_reading_order() -> None:
    expected = {
        "get-started/index.md": [
            "what-is-ce", "get-started/try-in-browser", "get-started/installation",
            "foundations/how-to/interpret_explanations", "get-started/apply-to-your-data",
        ],
        "sections/understand-ce.md": [
            "get-started/why-ce", "get-started/ce-tasks-and-modes",
            "foundations/concepts/ce_workflow", "foundations/concepts/calibration_methods",
            "foundations/concepts/calibrated_interval_semantics",
            "foundations/concepts/alternatives", "compare", "foundations/index",
        ],
        "sections/in-practice.md": [
            "https://games.grejna.ai/",
            "https://calibrated-explanations-demo.ju.se/expert",
            "practitioner/index",
            "tutorials/index",
            "tasks/index",
            "foundations/how-to/index",
        ],
        "sections/software-integration.md": [
            "integrate/consume-output",
            "get-started/quick_api",
            "api/index",
            "foundations/concepts/parameter-reference",
            "schema_v1",
            "upgrade/index",
            "contributor/index",
            "foundations/concepts/architecture",
        ],
        "sections/project-evolution.md": [
            "researcher/index", "citing", "ROADMAP", "foundations/governance/index",
        ],
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


def test_ml_foundations_close_understand_ce_and_are_not_a_get_started_step() -> None:
    assert not _text("get-started/ml-foundations.md").startswith("---\norphan: true")
    assert "get-started/ml-foundations" not in [t for _, t in _entries("get-started/index.md")]
    understand = [t for _, t in _entries("sections/understand-ce.md")]
    assert understand[-1] == "foundations/index" and understand.index("compare") == len(understand) - 2
    assert [t for _, t in _entries("foundations/index.md")] == [
        "get-started/ml-foundations", "foundations/concepts/index",
    ]


def test_get_started_is_one_path_with_the_browser_quick_start_before_installation() -> None:
    assert _entries("get-started/index.md") == [
        ("What CE Is", "what-is-ce"),
        ("Quick Start", "get-started/try-in-browser"),
        ("Your First CE Explanation in Python", "get-started/first-explanation-python"),
        ("Installation", "get-started/installation"),
        ("Read Your First Explanation", "foundations/how-to/interpret_explanations"),
        ("Apply CE to Your Own Data", "get-started/apply-to-your-data"),
        ("Coming from SHAP or LIME", "get-started/coming-from-shap-lime"),
        ("CE by Example (No Code)", "get-started/ce-by-example"),
    ]


def test_api_reference_and_contribute_are_direct_children_of_software_section() -> None:
    labels = {target: label for label, target in _entries("sections/software-integration.md")}
    assert labels["api/index"] == "API Reference"
    assert labels["contributor/index"] == "Contribute in 4 Steps"
