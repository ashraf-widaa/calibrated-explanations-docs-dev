"""Every reproduced entry on docs/get-started/troubleshooting.md must still happen as documented (WP-6).

Each test triggers the behaviour through the public API and checks that the message the
library produces is the message the page quotes, so the page cannot drift from CE.
"""

from __future__ import annotations

import warnings
from pathlib import Path

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

from calibrated_explanations import GuardedOptions, WrapCalibratedExplainer
from calibrated_explanations.utils.exceptions import (
    ConfigurationError,
    NotFittedError,
    ValidationError,
)

ROOT = Path(__file__).resolve().parents[3]
PAGE = (ROOT / "docs/get-started/troubleshooting.md").read_text(encoding="utf-8").replace("\r\n", "\n")
FLAT_PAGE = " ".join(PAGE.split())


def _documented(message: str) -> None:
    assert " ".join(message.split()) in FLAT_PAGE, f"page does not quote: {message!r}"


@pytest.fixture(scope="module")
def data():
    X, y = load_breast_cancer(return_X_y=True)
    X_tr, X_te, y_tr, _ = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    X_pr, X_cal, y_pr, y_cal = train_test_split(
        X_tr, y_tr, test_size=0.33, random_state=42, stratify=y_tr
    )
    return X_pr, y_pr, X_cal, y_cal, X_te


def _calibrated(data, **calibrate_kwargs):
    X_pr, y_pr, X_cal, y_cal, _ = data
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=20, random_state=0))
    w.fit(X_pr, y_pr)
    w.calibrate(X_cal, y_cal, **calibrate_kwargs)
    return w


def test_calls_in_wrong_order(data) -> None:
    X_pr, y_pr, X_cal, y_cal, X_te = data
    fresh = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=5, random_state=0))
    with pytest.raises(NotFittedError) as before_fit:
        fresh.calibrate(X_cal, y_cal)
    with pytest.raises(NotFittedError) as explain_unfitted:
        fresh.explain_factual(X_te[:1])
    fresh.fit(X_pr, y_pr)
    with pytest.raises(NotFittedError) as explain_uncalibrated:
        fresh.explain_factual(X_te[:1])
    _documented(str(before_fit.value))
    assert str(explain_unfitted.value).endswith("must be fitted and calibrated before explaining.")
    _documented("must be fitted and calibrated before explaining.")
    assert str(explain_uncalibrated.value).endswith("must be calibrated before explaining.")
    _documented("must be calibrated before explaining.")


def test_classifier_without_predict_proba(data) -> None:
    X_pr, y_pr, X_cal, y_cal, _ = data
    w = WrapCalibratedExplainer(LinearSVC(random_state=0, max_iter=5000))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        w.fit(X_pr, y_pr)
        with pytest.raises(ConfigurationError) as caught:
            w.calibrate(X_cal, y_cal)
    _documented(str(caught.value))


def test_nan_in_calibration_data(data) -> None:
    X_pr, y_pr, X_cal, y_cal, _ = data
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=5, random_state=0))
    w.fit(X_pr, y_pr)
    bad = X_cal.copy()
    bad[0, 0] = np.nan
    with pytest.raises(ValidationError) as caught:
        w.calibrate(bad, y_cal)
    _documented(str(caught.value))


def test_threshold_with_classifier(data) -> None:
    w = _calibrated(data)
    with pytest.raises(ValidationError) as caught:
        w.predict_proba(data[4][:1], threshold=0.5)
    _documented(str(caught.value))


def test_numpy_integer_index(data) -> None:
    w = _calibrated(data)
    explanations = w.explain_factual(data[4][:3])
    with pytest.raises(ValidationError) as caught:
        explanations[np.int64(0)]
    _documented(str(caught.value))
    assert explanations[int(np.int64(0))] is not None


def test_guarded_with_fast_explainer(data) -> None:
    w = _calibrated(data, fast=True)
    with pytest.raises(ConfigurationError) as caught:
        w.explain_factual(data[4][:1], guarded_options=GuardedOptions())
    _documented(str(caught.value))


def test_dataframe_then_array_feature_name_warning(data) -> None:
    pd = pytest.importorskip("pandas")
    X_pr, y_pr, X_cal, y_cal, X_te = data
    columns = [str(name) for name in load_breast_cancer().feature_names]
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=5, random_state=0))
    w.fit(pd.DataFrame(X_pr, columns=columns), y_pr)
    w.calibrate(pd.DataFrame(X_cal, columns=columns), y_cal)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        w.predict(X_te[:1])
    messages = [str(item.message) for item in caught if issubclass(item.category, UserWarning)]
    expected = "X does not have valid feature names, but RandomForestClassifier was fitted with feature names"
    assert expected in messages
    _documented(expected)


def test_multiclass_upper_bound_above_one() -> None:
    X, y = load_iris(return_X_y=True)
    a, b, ya, _ = train_test_split(X, y, test_size=0.5, random_state=0, stratify=y)
    p, c, yp, yc = train_test_split(a, ya, test_size=0.5, random_state=0, stratify=ya)
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=50, random_state=0))
    w.fit(p, yp)
    w.calibrate(c, yc)
    probs, (_, high) = w.predict_proba(b, uq_interval=True)
    assert round(float(np.max(high)), 2) == 1.18
    assert np.allclose(probs.sum(axis=1), 1.0)
    _documented("(1.18 in our reproduction with the iris data)")


def test_known_issue_explaining_again_after_features_to_ignore(data) -> None:
    w = _calibrated(data)
    ignored = w.explain_factual(data[4][:2], features_to_ignore=[0])
    ignored.add_conjunctions()  # the result of the ignore call itself works
    with pytest.raises(ConfigurationError) as caught:
        w.explain_factual(data[4][:2])
    assert isinstance(caught.value.__cause__, KeyError)
    _documented(str(caught.value))


def test_known_issue_filter_features(data) -> None:
    w = _calibrated(data)
    explanations = w.explain_factual(data[4][:2])
    with pytest.raises(TypeError) as caught:
        explanations.filter_features(exclude_features=[0])
    _documented(str(caught.value))


def test_runtime_telemetry_fills_after_an_explanation(data) -> None:
    w = _calibrated(data)
    assert dict(w.runtime_telemetry) == {}
    w.predict_proba(data[4][:1])
    assert dict(w.runtime_telemetry) == {}
    w.explain_factual(data[4][:1])
    assert dict(w.runtime_telemetry)


def test_every_lookup_row_points_to_an_entry() -> None:
    import re

    targets = re.findall(r"\{ref\}`[^`<]+<(ts-[a-z-]+)>`", PAGE)
    labels = set(re.findall(r"^\((ts-[a-z-]+)\)=$", PAGE, flags=re.MULTILINE))
    assert targets and set(targets) == labels
