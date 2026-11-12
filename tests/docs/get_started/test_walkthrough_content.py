"""Scientific wording guards for the generated Quick Start walkthrough.

The walkthrough follows the teaching-first specification
(``learning-reports/quickstart-walkthrough-audit/05-content-specification.md``, rev. 2).
Its open author questions must keep neutral wording, and the ten core sections must stay
in order. The page is generated: edit ``scripts/docs/build_quickstart_walkthrough.py``.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PAGE = ROOT / "docs" / "get-started" / "quickstart_walkthrough.md"
GENERATOR = ROOT / "scripts" / "docs" / "build_quickstart_walkthrough.py"

CORE_SECTIONS = [
    "## 1. The prediction problem and the case we follow",
    "## 2. Data and the three data roles",
    "## 3. Train the model and evaluate it",
    "## 4. Why calibration matters",
    "## 5. How Venn–Abers calibration works, and what its output means",
    "## 6. How CE builds an explanation",
    "## 7. The factual explanation of our case",
    "## 8. Alternative explanations of our case",
    "## 9. What we can and cannot conclude about case 2",
    "## 10. Recap and next steps",
]

# Spec rev. 2, "Unresolved points": phrases the page must not use (Q1, Q2, Q4, Q7) and
# overclaims (calibration always improving scores; ranges as confidence intervals).
MUST_NOT_SAY = [
    "joint effect",
    "matter more together",
    "matter more than either",
    "negligible",
    "confidence interval for the weight",
    "no guarantee exists",
    "green",
    "purple",
    "always improves",
]


def page_text() -> str:
    return " ".join(PAGE.read_text(encoding="utf-8").split())


def test_core_sections_appear_in_order() -> None:
    text = PAGE.read_text(encoding="utf-8")
    positions = [text.index(heading) for heading in CORE_SECTIONS]
    assert positions == sorted(positions)


def test_unresolved_points_keep_neutral_wording() -> None:
    text = page_text().lower()
    for phrase in MUST_NOT_SAY:
        assert phrase not in text, phrase


def test_guarantee_statements_are_qualified() -> None:
    text = page_text()
    assert "The guarantee belongs to the pair." in text
    assert "The merged estimate has no exact guarantee." in text
    assert "is not a confidence interval" in text
    assert text.count("Wording under review by the CE authors.") >= 2
    assert "no guarantee is claimed for them" in text


def test_calibration_is_not_presented_as_improving_scores() -> None:
    text = page_text()
    assert "the calibrated probabilities scored *worse* than the raw ones" in text
    assert re.search(r"Brier score, raw: +0\.\d{4}", text)


def test_generator_guards_prose_numbers() -> None:
    source = GENERATOR.read_text(encoding="utf-8")
    assert "PROSE_NUMBERS" in source
    assert "prose numbers not found in generated outputs" in source
