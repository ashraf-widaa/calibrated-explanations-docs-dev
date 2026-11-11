"""Documentation tests for ``docs/tasks/classification.md``.

The "Calibrated probabilities with uncertainty" example is read from the page and
executed unchanged (``docs/foundations/governance/test_policy.md``: copy code
verbatim). It once indexed the binary interval bounds as ``low[0, 1]``, which
raises ``IndexError`` because binary bounds are one-dimensional.
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from calibrated_explanations import WrapCalibratedExplainer

PAGE = Path(__file__).resolve().parents[3] / "docs" / "tasks" / "classification.md"
SECTION = "### 1. Calibrated probabilities with uncertainty"


def published_example() -> str:
    """Return the first python code block under the example heading, as published."""
    text = PAGE.read_text(encoding="utf-8")
    assert SECTION in text, f"Heading {SECTION!r} not found in {PAGE}"
    section = text.split(SECTION, 1)[1]
    match = re.search(r"```python\n(.*?)```", section, re.DOTALL)
    assert match, f"No python code block under {SECTION!r}"
    return match.group(1)


def calibrated_explainer(loader):
    """Fit and calibrate a WrapCalibratedExplainer on proper training/calibration splits."""
    x, y = loader(return_X_y=True)
    x_train, x_test, y_train, _ = train_test_split(
        x, y, test_size=0.2, random_state=0, stratify=y
    )
    x_proper, x_cal, y_proper, y_cal = train_test_split(
        x_train, y_train, test_size=0.3, random_state=0, stratify=y_train
    )
    explainer = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=20, random_state=0))
    explainer.fit(x_proper, y_proper)
    explainer.calibrate(x_cal, y_cal)
    return explainer, x_test


@pytest.fixture(scope="module")
def binary_setup():
    return calibrated_explainer(load_breast_cancer)


def test_binary_uncertainty_example_runs_unchanged(binary_setup, capsys):
    explainer, x_test = binary_setup
    namespace = {"explainer": explainer, "x_test": x_test}

    exec(published_example(), namespace)  # noqa: S102 - executes the published docs example

    n_samples = x_test.shape[0]
    assert namespace["probs"].shape == (n_samples, 2)
    assert np.shape(namespace["low"]) == (n_samples,)
    assert np.shape(namespace["high"]) == (n_samples,)
    assert re.fullmatch(
        r"Probability: \d\.\d{3} \(Interval: \d\.\d{3} – \d\.\d{3}\)\n", capsys.readouterr().out
    )


def test_multiclass_bounds_have_one_column_per_class():
    # The page states that multiclass bounds have shape (n_samples, n_classes).
    explainer, x_test = calibrated_explainer(load_iris)

    probs, (low, high) = explainer.predict_proba(x_test, uq_interval=True)

    assert probs.shape == (x_test.shape[0], 3)
    assert np.shape(low) == probs.shape
    assert np.shape(high) == probs.shape
