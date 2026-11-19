"""Guards for the 2026-11-19 section organisation.

Each section hub states its pages in reading order and hands over to the next
section; the canonical semantics page keeps one visible list of the questions
reserved for the CE authors.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

DOCS = Path(__file__).resolve().parents[2] / "docs"


def _flat(rel: str) -> str:
    return " ".join((DOCS / rel).read_text(encoding="utf-8").split())


def test_open_author_questions_stay_listed_on_the_canonical_page() -> None:
    text = _flat("foundations/concepts/calibrated_interval_semantics.md")
    assert "(open-author-questions)=" in text
    for item in ("SR-01", "SR-02", "SR-03 / SR-13", "SR-15", "SR-08 / SR-10 / SR-14", "SR-07 / SR-09", "SR-16", "SR-06", "Legal", "Versions"):
        assert f"| {item} |" in text, item
    assert "none of them is resolved by this documentation" in text


@pytest.mark.parametrize(("hub", "next_target"), [
    ("sections/understand-ce.md", "in-practice"),
    ("sections/in-practice.md", "software-integration"),
    ("sections/software-integration.md", "project-evolution"),
])
def test_section_hubs_hand_over_to_the_next_section(hub: str, next_target: str) -> None:
    text = _flat(hub)
    assert "**Next" in text and f"<{next_target}>`" in text, hub


def test_understand_ce_lists_its_pages_in_one_numbered_order() -> None:
    """The What & Why and How CE Works halves share one numbered reading order (1-8)."""
    raw = (DOCS / "sections/understand-ce.md").read_text(encoding="utf-8")
    listed = raw.split("(ce-what-why)=", 1)[1].split("**Next section:**", 1)[0]
    numbers = [int(n) for n in re.findall(r"^(\d)\. ", listed, flags=re.MULTILINE)]
    assert numbers == list(range(1, 9))
    assert raw.index("(ce-what-why)=") < raw.index("(how-ce-works)=")


@pytest.mark.parametrize("old", ["sections/what-and-why.md", "sections/how-ce-works.md"])
def test_old_section_landings_keep_their_url_and_point_to_understand_ce(old: str) -> None:
    raw = (DOCS / old).read_text(encoding="utf-8")
    assert raw.startswith("---\norphan: true\n---")
    assert "<understand-ce>`" in raw


def test_how_to_index_describes_every_guide() -> None:
    text = _flat("foundations/how-to/index.md")
    for guide in ("interpret_explanations", "conditional_calibration", "to_narrative", "export_explanations",
                  "plot_with_plotspec", "integrate_with_pipelines", "configure_runtime", "safe-defaults",
                  "configure_telemetry", "tune_runtime_performance"):
        assert f"{{doc}}`{guide}`:" in text, guide
