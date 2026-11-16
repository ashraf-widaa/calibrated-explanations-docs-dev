"""WP-13: the What & Why landing is an ordered progression, and What CE Is answers each step.

Checks the reading order, the relabelled regulation entry, the calibration-vs-accuracy
section, the worked example numbers (taken from the walkthrough output) and the phone
layout of the wide tables.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANDING = ROOT / "docs" / "sections" / "what-and-why.md"
WHAT_IS = ROOT / "docs" / "what-is-ce.md"
INDEX = ROOT / "docs" / "index.md"


def _flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def test_reading_order_covers_the_seven_questions_in_sequence() -> None:
    text = LANDING.read_text(encoding="utf-8")
    rows = re.findall(r"^\| (\d) \| ", text, flags=re.MULTILINE)
    assert rows == ["1", "2", "3", "4", "5", "6", "7"]
    for target in ("ml-a1", "wic-problem", "wic-calibration", "wic-adds", "wic-fit", "wic-guarantees"):
        assert f"<{target}>`" in text, target


def test_reading_order_targets_exist() -> None:
    what_is = WHAT_IS.read_text(encoding="utf-8")
    for label in ("wic-problem", "wic-calibration", "wic-adds", "wic-guarantees", "wic-fit", "wic-compare"):
        assert f"({label})=" in what_is, label
    assert "(ml-a1)=" in (ROOT / "docs/get-started/ml-foundations.md").read_text(encoding="utf-8")


def test_cards_are_ordered_as_a_progression() -> None:
    titles = re.findall(r"grid-item-card\} (.+)", LANDING.read_text(encoding="utf-8"))
    assert titles == [
        "Understanding AI Models",
        "Can We Trust AI Outputs?",
        "What Is CE & What Does It Add?",
        "The Explainability Gap",
        "Regulation Context (EU AI Act)",
    ]


def test_regulation_entry_is_relabelled_and_not_a_compliance_claim() -> None:
    index = INDEX.read_text(encoding="utf-8")
    assert "Regulation Context (EU AI Act) <practitioner/playbooks/eu-ai-act-compliance>" in index
    assert "Trustworthy AI <" not in index
    landing = _flat(LANDING)
    assert "not evidence of compliance" in landing
    group = index.split(':caption: "CE: What & Why"')[1].split("```")[0]
    assert group.index("what-is-ce") < group.index("compare") < group.index("eu-ai-act-compliance")


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
