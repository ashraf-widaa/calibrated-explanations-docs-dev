"""Guards for the 2026-11-18 documentation refinement.

They keep the first-run instructions installable as written, keep the range wording
consistent with the Batch 1 semantics, and keep the new evaluation checks qualified.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

DOCS = Path(__file__).resolve().parents[2] / "docs"
GENERATED = {"get-started/quickstart_walkthrough.md"}  # written by scripts/docs/build_quickstart_walkthrough.py


def _text(rel: str) -> str:
    return (DOCS / rel).read_text(encoding="utf-8").replace("\r\n", "\n")


def _pages() -> list[str]:
    return sorted(p.relative_to(DOCS).as_posix() for p in DOCS.rglob("*.md") if "_build" not in p.parts)


@pytest.mark.parametrize("page", ["get-started/quickstart_classification.md",
                                  "get-started/quickstart_guarded.md",
                                  "get-started/apply-to-your-data.md"])
def test_pages_that_plot_install_the_viz_extra(page: str) -> None:
    text = _text(page)
    assert ".plot(" in text
    installs = re.findall(r"^pip install .*$", text, flags=re.MULTILINE)
    assert installs, page
    assert all("[viz]" in line for line in installs), installs


def test_ranges_are_not_described_as_how_firmly_the_data_support_a_value() -> None:
    offenders = [p for p in _pages() if p not in GENERATED and "how firmly" in _text(p)]
    assert offenders == []


def test_quick_api_states_when_prediction_bounds_are_returned() -> None:
    text = _text("get-started/quick_api.md")
    row = next(line for line in text.splitlines() if line.startswith("| What comes back?"))
    assert "uq_interval=True" in row
    assert "How do I install it?" in text and "[viz]" in text


def test_evaluation_checks_are_empirical_and_keep_open_review_items() -> None:
    text = _text("practitioner/evaluate_ce.md")
    for heading in ("## 3. Check intervals (regression)", "### Threshold events (probabilistic regression)",
                    "## 4. Common mistakes", "## 5. When not to trust the outputs", "### Checking a subgroup"):
        assert heading in text, heading
    flat = " ".join(text.split())
    assert "exact validity statement for these event probabilities is under review by the CE authors" in flat
    assert "What Mondrian calibration guarantees within each group" in flat
    assert "can arise by chance" in flat


def test_tutorial_hub_gives_a_reading_order() -> None:
    text = _text("tutorials/index.md")
    assert "**Suggested order.**" in text
    assert "most tutorials draw plots" in text
