"""Beta V3 visual changes: V-6 output-types figure and phone-friendly tables."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

DOCS = Path(__file__).resolve().parents[2] / "docs"
FIGURE = DOCS / "_static" / "figures" / "ce-output-types.svg"


def _text(rel: str) -> str:
    return (DOCS / rel).read_text(encoding="utf-8").replace("\r\n", "\n")


def test_output_types_figure_is_accessible_and_labels_each_mode() -> None:
    svg = FIGURE.read_text(encoding="utf-8")
    assert "<title" in svg and "<desc" in svg
    for label in ("A · Classification", "B · Interval regression", "C · Probabilistic regression"):
        assert label in svg, label
    assert "not a confidence" in svg
    assert "on average over" in svg


def test_output_types_numbers_come_from_published_outputs() -> None:
    svg = FIGURE.read_text(encoding="utf-8")
    walkthrough = _text("get-started/quickstart_walkthrough.md")
    regression = _text("get-started/quickstart_regression.md")
    for number in ("0.286", "0.167", "0.333"):
        assert number in svg and number in walkthrough, number
    for number in ("273.4", "186.5", "409.2", "321", "0.077", "0.000", "0.083"):
        assert number in svg and number in regression, number


def test_output_types_figure_sits_on_the_guarantees_page_not_quick_start() -> None:
    assert "ce-output-types.svg" in _text("foundations/concepts/calibrated_interval_semantics.md")
    assert "(ce-output-types)=" in _text("foundations/concepts/calibrated_interval_semantics.md")
    for page in ("index", "ml-foundations", "why-ce", "ce-by-example", "ce-tasks-and-modes", "apply-overview"):
        assert "ce-output-types.svg" not in _text(f"get-started/{page}.md"), page


@pytest.mark.parametrize(
    ("page", "header"),
    [
        ("get-started/ce-tasks-and-modes.md", "| Mode | Output | Read it as |"),
        ("get-started/ce-tasks-and-modes.md", "| Term | Means | Examples | How you choose it |"),
        ("get-started/ce-tasks-and-modes.md", "| Capability | Binary |"),
        ("get-started/ml-foundations.md", "| Model family | How it works, in one line | Strengths | Watch out for |"),
    ],
)
def test_wide_tables_use_the_phone_layout(page: str, header: str) -> None:
    text = _text(page)
    start = text.index(header)
    assert text[:start].rstrip().endswith(":::{div} ce-table-compact"), header
    assert re.search(r"\.ce-table-compact table", (DOCS / "_static" / "ce-docs.css").read_text(encoding="utf-8"))
