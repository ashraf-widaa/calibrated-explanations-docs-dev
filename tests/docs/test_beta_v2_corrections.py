"""Beta V2 corrections (2026-11-13 audit, findings A-01 to A-13) must not regress.

See development/reports/beta-versions-20261113/01-master-audit-official-vs-beta.md.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

DOCS = Path(__file__).resolve().parents[2] / "docs"


def _text(rel: str) -> str:
    return (DOCS / rel).read_text(encoding="utf-8").replace("\r\n", "\n")


def test_one_sided_intervals_identify_source_revision_and_open_side() -> None:
    """The same development version identifies two different endpoint implementations."""
    regression = _text("tasks/regression.md")
    assert "This Beta's source at `2bc637bc`" in regression
    assert "official source at `371bd806`" in regression
    assert "finite value is a placeholder only, not a coverage endpoint" in regression
    assert "`-inf` or `inf`" in regression
    assert "Both source revisions identify as `1.1.0-dev`" in regression
    methods = _text("foundations/concepts/calibration_methods.md")
    assert "finite placeholder" in methods and "`371bd806`" in methods
    assert "Treat the side as open" in methods
    assert "from v1.1.0" not in methods


def test_percentiles_are_not_called_confidence_levels() -> None:
    assert "arbitrary confidence levels" not in _text("tasks/regression.md")


@pytest.mark.parametrize("phrase", ["(counterfactuals)", "necessary to flip", "epistemic and aleatoric explanation envelopes"])
def test_classification_task_page_avoids_causal_or_undefined_wording(phrase: str) -> None:
    assert phrase not in _text("tasks/classification.md")


def test_probabilistic_regression_threshold_is_the_event_y_le_t() -> None:
    text = _text("tasks/probabilistic_regression.md")
    assert "treated as a binary classification boundary" not in text
    assert "aleatoric + epistemic uncertainty on the score" not in text


def test_agent_guide_uses_supported_calls() -> None:
    text = _text("get-started/ce_first_agent_guide.md")
    assert "ensure_coverage" not in text and "ensure_order" not in text
    assert "DifficultyEstimator().fit(" in text


@pytest.mark.parametrize("page", ["contributor/plugin-contract.md", "contributor/extending/plugin-advanced-contract.md"])
def test_plugin_meta_examples_declare_data_modalities(page: str) -> None:
    text = _text(page)
    assert "_EXPLANATION_PLUGINS" not in text
    for match in re.finditer(r"plugin_meta\s*=\s*\{\n(.*?)\n\s*\}", text, re.DOTALL):
        assert "data_modalities" in match.group(1), match.group(0)[:80]


def test_retrieval_examples_use_existing_entry_points() -> None:
    text = _text("practitioner/advanced/explanation_retrieval.md")
    assert "expl.factual" not in text and "expl.alternative" not in text
    assert "explainer.explain_factual(x_test[:1])[0]" in text


def test_schema_sketch_is_not_a_python_block() -> None:
    assert '```python\n{\n    "core": {' not in _text("foundations/concepts/explanation_structures.md")


def test_tutorials_state_the_verified_versions() -> None:
    assert "CE 1.0.2" in _text("tutorials/index.md")


def test_should_not_present_probability_containment_as_outcome_coverage() -> None:
    """N-07: checking p inside its own bounds is not observed-target coverage."""
    page = _text("practitioner/playbooks/eu-ai-act-compliance.md")
    assert "in_interval.mean()" not in page
    assert "certifiable bound" not in page
    assert "**Covered**" not in page
    assert "does not measure" in page and "coverage of observed outcomes" in page


def test_should_identify_withdrawn_proposal_in_status_and_checklist() -> None:
    """Verified legislative status must agree across the existing playbook."""
    page = _text("practitioner/playbooks/eu-data-liability-compliance.md")
    assert "6 October 2025" in page
    assert "In legislative process" not in page
    assert "AI Act compliance defeats presumption" not in page
    assert "**Covered**" not in page
    assert "Art. 27 Recommender system transparency" in page


def test_should_keep_pair_and_explanation_guarantees_separate() -> None:
    """SR-03/SR-07: removing an overclaim must not erase the review boundary."""
    semantics = _text("foundations/concepts/calibrated_interval_semantics.md")
    assert "must not be transferred to the" in semantics
    assert "merged probability" in semantics and "SR-03" in semantics
    assert "SR-02" in semantics and "SR-15" in semantics
    ensured = _text("practitioner/playbooks/ensured-explanations.md")
    assert "actively reduce epistemic uncertainty" not in ensured
    assert "Proceed with confidence" not in ensured
    assert "uncertainty_high" not in ensured
    assert "under review" in ensured and "no wider" in ensured
