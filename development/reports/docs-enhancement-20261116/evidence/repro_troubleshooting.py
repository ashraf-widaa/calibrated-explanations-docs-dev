"""Reproduce candidate troubleshooting entries against the Beta src/ (WP-6, Prompt 3b)."""
import sys
import traceback
import warnings

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

import calibrated_explanations as ce
from calibrated_explanations import WrapCalibratedExplainer

print("CE", ce.__version__, "| Python", sys.version.split()[0])


def run(label, fn):
    print(f"\n=== {label}")
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            out = fn()
            print("OK ->", repr(out)[:300])
        except Exception as exc:  # noqa: BLE001
            print("RAISED", type(exc).__module__ + "." + type(exc).__name__, "|", str(exc)[:400])
            if exc.__cause__ is not None:
                print("  cause:", type(exc.__cause__).__name__, str(exc.__cause__)[:200])
    for w in caught:
        print("  WARNING", w.category.__name__, "|", str(w.message)[:250])


X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
X_pr, X_cal, y_pr, y_cal = train_test_split(X_tr, y_tr, test_size=0.33, random_state=42, stratify=y_tr)


def calibrated_rf():
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=50, random_state=42))
    w.fit(X_pr, y_pr)
    w.calibrate(X_cal, y_cal)
    return w


# 0. explain before fit / before calibrate
def explain_unfitted():
    w = WrapCalibratedExplainer(RandomForestClassifier(random_state=0))
    return w.explain_factual(X_te[:1])


def explain_uncalibrated():
    w = WrapCalibratedExplainer(RandomForestClassifier(random_state=0))
    w.fit(X_pr, y_pr)
    return w.explain_factual(X_te[:1])


def calibrate_unfitted():
    w = WrapCalibratedExplainer(RandomForestClassifier(random_state=0))
    return w.calibrate(X_cal, y_cal)


run("0a explain_factual before fit", explain_unfitted)
run("0b explain_factual after fit, before calibrate", explain_uncalibrated)
run("0c calibrate before fit", calibrate_unfitted)


# 1. classifier without predict_proba
def no_proba():
    w = WrapCalibratedExplainer(LinearSVC(random_state=0, max_iter=5000))
    w.fit(X_pr, y_pr)
    w.calibrate(X_cal, y_cal)
    return ("mode", w.explainer.mode, "predict", w.predict(X_te[:2]))


def no_proba_explicit_mode():
    w = WrapCalibratedExplainer(LinearSVC(random_state=0, max_iter=5000))
    w.fit(X_pr, y_pr)
    w.calibrate(X_cal, y_cal, mode="classification")
    return w.predict_proba(X_te[:2])


def no_proba_predict_proba():
    w = WrapCalibratedExplainer(LinearSVC(random_state=0, max_iter=5000))
    w.fit(X_pr, y_pr)
    w.calibrate(X_cal, y_cal)
    return w.predict_proba(X_te[:2])


run("1a LinearSVC (no predict_proba), default calibrate", no_proba)
run("1b LinearSVC, calibrate(mode='classification')", no_proba_explicit_mode)
run("1c LinearSVC, default calibrate, then predict_proba", no_proba_predict_proba)


# 2. indexing explanations with a NumPy integer
def numpy_index():
    w = calibrated_rf()
    f = w.explain_factual(X_te[:3])
    return f[np.int64(0)]


def python_index():
    w = calibrated_rf()
    f = w.explain_factual(X_te[:3])
    return type(f[0]).__name__


run("2a explanations[np.int64(0)]", numpy_index)
run("2b explanations[0]", python_index)


# 4. pipeline fitted on DataFrame, explained with ndarray
def dataframe_then_array():
    df = pd.DataFrame(X_pr, columns=load_breast_cancer().feature_names)
    dfc = pd.DataFrame(X_cal, columns=load_breast_cancer().feature_names)
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=20, random_state=0))
    w.fit(df, y_pr)
    w.calibrate(dfc, y_cal)
    return w.predict(X_te[:2])


run("4 fit on DataFrame, predict on ndarray", dataframe_then_array)


# 5. guarded + fast
def guarded_fast():
    from calibrated_explanations import GuardedOptions

    w = calibrated_rf()
    w.explain_fast(X_te[:1])  # initialise fast mode
    return w.explain_factual(X_te[:1], guarded_options=GuardedOptions())


def guarded_fast_init():
    from calibrated_explanations import GuardedOptions

    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=20, random_state=0))
    w.fit(X_pr, y_pr)
    w.calibrate(X_cal, y_cal, fast=True)
    return w.explain_factual(X_te[:1], guarded_options=GuardedOptions())


run("5a explain_fast then guarded explain_factual", guarded_fast)
run("5b calibrate(fast=True) then guarded explain_factual", guarded_fast_init)


# 6. multiclass upper bounds above 1
def multiclass_bounds():
    Xi, yi = load_iris(return_X_y=True)
    a, b, ya, yb = train_test_split(Xi, yi, test_size=0.5, random_state=0, stratify=yi)
    p, c, yp, yc = train_test_split(a, ya, test_size=0.5, random_state=0, stratify=ya)
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=50, random_state=0))
    w.fit(p, yp)
    w.calibrate(c, yc)
    probs, (low, high) = w.predict_proba(b, uq_interval=True)
    return ("max high", float(np.max(high)), "row sums max", float(np.max(probs.sum(axis=1))))


run("6 multiclass bounds", multiclass_bounds)


# 7. NaN input
def nan_input():
    w = calibrated_rf()
    bad = X_te[:1].copy()
    bad[0, 0] = np.nan
    return w.explain_factual(bad)


run("7 NaN in explained case", nan_input)


# 8. known issue: features_to_ignore then add_conjunctions
def ignore_then_conj():
    w = calibrated_rf()
    w.explain_factual(X_te[:2], features_to_ignore=[0])
    f = w.explain_factual(X_te[:2])
    return f.add_conjunctions()


run("8 features_to_ignore then add_conjunctions", ignore_then_conj)


# 9. known issue: filter_features after the fact
def filter_after():
    w = calibrated_rf()
    f = w.explain_factual(X_te[:2])
    return f.filter_features(exclude=[0])


run("9 filter_features", filter_after)


# 10. to_narrative without PyYAML
def narrative():
    import importlib.util

    print("  pyyaml installed:", importlib.util.find_spec("yaml") is not None)
    w = calibrated_rf()
    f = w.explain_factual(X_te[:1])
    return f.to_narrative()


run("10 to_narrative", narrative)


# 11. threshold given for classification
def threshold_on_classifier():
    w = calibrated_rf()
    return w.predict_proba(X_te[:1], threshold=0.5)


run("11 predict_proba(threshold=) on a classifier", threshold_on_classifier)


# 12. low_high_percentiles on classifier
def percentiles_on_classifier():
    w = calibrated_rf()
    return w.explain_factual(X_te[:1], low_high_percentiles=(5, 95))


run("12 low_high_percentiles on a classifier", percentiles_on_classifier)
