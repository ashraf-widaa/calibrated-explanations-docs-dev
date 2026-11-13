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


def test_one_sided_intervals_are_version_aware() -> None:
    regression = _text("tasks/regression.md")
    assert "v1.0.2" in regression and "From v1.1.0" in regression
    assert "`-inf` or `inf`" in regression
    methods = _text("foundations/concepts/calibration_methods.md")
    assert "a placeholder in v1.0.2; `-inf`/`inf` from v1.1.0" in methods


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
