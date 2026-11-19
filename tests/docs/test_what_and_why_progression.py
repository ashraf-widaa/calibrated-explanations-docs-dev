"""WP-13: the What & Why landing is an ordered progression, and What CE Is answers each step.

Checks the reading order, the relabelled regulation entry, the calibration-vs-accuracy
section, the worked example numbers (taken from the walkthrough output) and the phone
layout of the wide tables.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# 2026-11-19 redesign: What & Why is the first half of the Understand CE landing.
LANDING = ROOT / "docs" / "sections" / "understand-ce.md"
WHAT_IS = ROOT / "docs" / "what-is-ce.md"
INDEX = ROOT / "docs" / "index.md"


def _flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def test_reading_order_targets_exist() -> None:
    what_is = WHAT_IS.read_text(encoding="utf-8")
    for label in ("wic-problem", "wic-calibration", "wic-adds", "wic-guarantees", "wic-fit", "wic-compare"):
        assert f"({label})=" in what_is, label
    assert "(ml-a1)=" in (ROOT / "docs/get-started/ml-foundations.md").read_text(encoding="utf-8")


def test_overview_connects_prediction_to_ce_without_a_navigation_inventory() -> None:
    text = LANDING.read_text(encoding="utf-8")
    assert text.index("## CE: What & Why") < text.index("## How CE Works")
    assert "calibrates the model's outputs" in text
    assert "grid-item-card" not in text
    assert "| # | Question |" not in text


def test_regulation_entry_is_relabelled_and_not_a_compliance_claim() -> None:
    # 2026-11-19 architecture: the regulation playbook is practical, legal-review
    # material, so it sits with the other playbooks; What & Why still points to it.
    index = INDEX.read_text(encoding="utf-8")
    landing_raw = LANDING.read_text(encoding="utf-8")
    howto = (ROOT / "docs/foundations/how-to/index.md").read_text(encoding="utf-8")
    assert "eu-ai-act-compliance" in howto.split("```{toctree}")[1]
    assert "Trustworthy AI <" not in index + landing_raw
    landing = _flat(LANDING)
    assert "not evidence of compliance" in landing
    assert "eu-ai-act-compliance" in landing
    group = landing_raw.split("```{toctree}")[1].split("```")[0]
    assert group.index("why-ce") < group.index("ce-tasks-and-modes") < group.index("compare")


def test_calibration_is_distinguished_from_accuracy_and_correctness() -> None:
    body = _flat(WHAT_IS)
    assert "accurate but miscalibrated" in body
    assert "calibrated but of little use" in body
    assert "says nothing about whether one individual prediction is correct" in body
    assert "proceedings.mlr.press/v70/guo17a.html" in body


def test_example_numbers_come_from_the_walkthrough() -> None:
    walkthrough = (ROOT / "docs/get-started/quickstart_walkthrough.md").read_text(encoding="utf-8")
    assert "Raw P(benign), cases 0-4: [0.   1.   0.16 0.21 0.  ]" in walkthrough
    assert "0.286" in walkthrough and "[0.167, 0.333]" in walkthrough
    body = _flat(WHAT_IS)
    assert "is benign is 0.16" in body
    assert "0.286 with the range [0.167, 0.333]" in body


def test_fit_list_is_not_presented_as_demonstrated_benefit() -> None:
    assert "It is not a list of demonstrated benefits" in _flat(WHAT_IS)


def test_wide_tables_use_the_phone_layout() -> None:
    text = WHAT_IS.read_text(encoding="utf-8")
    assert text.count(":::{div} ce-table-compact") == 2
