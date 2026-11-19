"""WP-14: How CE Works reads as a levelled progression along task -> mode -> method -> output -> assumptions.

Also guards the scientific distinctions added to the workflow page and the removal of the
telemetry walkthrough from the interpretation guide.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
# 2026-11-19 redesign: How CE Works is the second half of the Understand CE landing.
LANDING = DOCS / "sections" / "understand-ce.md"
WORKFLOW = DOCS / "foundations" / "concepts" / "ce_workflow.md"
INTERPRET = DOCS / "foundations" / "how-to" / "interpret_explanations.md"
METHODS = DOCS / "foundations" / "concepts" / "calibration_methods.md"


def _flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def test_landing_states_the_chain_without_learning_level_labels() -> None:
    text = _flat(LANDING)
    assert "task → CE mode → statistical method → output and what its range means → assumptions and guarantees" in text
    assert not re.search(r"\bL[123]\b", text)
    for label in ("ce-workflow-methods", "ce-workflow-guarantees", "ce-workflow-explanations"):
        assert f"<{label}>`" in text
        assert f"({label})=" in WORKFLOW.read_text(encoding="utf-8")


def test_sidebar_preserves_the_existing_reference_order() -> None:
    index = (DOCS / "index.md").read_text(encoding="utf-8")
    assert "Understand CE <sections/understand-ce>" in index
    assert 'href="sections/understand-ce.html#how-ce-works"' in index
    group = LANDING.read_text(encoding="utf-8").split("```{toctree}")[1].split("```")[0]
    order = [
        "foundations/concepts/ce_workflow",
        "foundations/concepts/calibration_methods",
        "foundations/concepts/calibrated_interval_semantics",
        "foundations/concepts/alternatives",
        "foundations/index",
    ]
    positions = [group.index(f"<../{page}>") for page in order]
    assert positions == sorted(positions)
    assert "Guarantees and Limits by Mode <../foundations/concepts/calibrated_interval_semantics>" in group


def test_workflow_table_separates_the_three_output_meanings() -> None:
    text = _flat(WORKFLOW)
    assert "Bounds of a probability, not a confidence interval" in text
    assert "holds on average over many cases, not for each case" in text
    assert "Bounds of the probability of an event, not an interval for the value" in text
    assert "explanation types**, not modes" in text
    assert "teaching view of CE" in text


def test_workflow_keeps_the_guarantee_distinctions_apart() -> None:
    text = _flat(WORKFLOW)
    for phrase in (
        "class or event probability",
        "numeric target",
        "explanation weight",
        "not formal per-feature coverage guarantees",
        "semantics reference <calibrated_interval_semantics>",
    ):
        assert phrase in text, phrase
    # Open author questions keep their markers (SR-07, SR-15).
    assert "aleatoric or epistemic uncertainty remains under author review" in text
    assert "threshold events in probabilistic regression is under review by the CE authors" in text


def test_interpretation_guide_links_telemetry_instead_of_teaching_it() -> None:
    text = INTERPRET.read_text(encoding="utf-8")
    assert "{doc}`configure_telemetry`" in text
    assert 'telemetry["plot_source"]' not in text
    assert "ce-reading-an-output.svg" in text
    assert "ensures calibrated explanations drive safe" not in text
    assert "advanced/demo_under_the_hood.ipynb" in text


def test_wide_theory_tables_use_the_phone_layout() -> None:
    assert METHODS.read_text(encoding="utf-8").count(":::{div} ce-table-compact") == 4
    assert WORKFLOW.read_text(encoding="utf-8").count(":::{div} ce-table-compact") == 1
