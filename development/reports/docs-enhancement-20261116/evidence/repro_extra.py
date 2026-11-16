"""Follow-up reproductions: NaN handling, filter_features, CLI."""
import subprocess
import sys
import warnings

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from calibrated_explanations import WrapCalibratedExplainer

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
X_pr, X_cal, y_pr, y_cal = train_test_split(X_tr, y_tr, test_size=0.33, random_state=42, stratify=y_tr)
warnings.simplefilter("ignore")


def run(label, fn):
    print(f"\n=== {label}")
    try:
        print("OK ->", repr(fn())[:200])
    except Exception as exc:  # noqa: BLE001
        print("RAISED", type(exc).__name__, "|", str(exc)[:300])
        if exc.__cause__ is not None:
            print("  cause:", type(exc.__cause__).__name__, str(exc.__cause__)[:200])


def with_nan(a):
    a = a.copy()
    a[0, 0] = np.nan
    return a


def nan_fit_rf():
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=20, random_state=0))
    w.fit(with_nan(X_pr), y_pr)
    return "fit ok"


def nan_cal_rf():
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=20, random_state=0))
    w.fit(X_pr, y_pr)
    w.calibrate(with_nan(X_cal), y_cal)
    return "calibrate ok"


def nan_fit_lr():
    w = WrapCalibratedExplainer(LogisticRegression(max_iter=5000))
    w.fit(with_nan(X_pr), y_pr)
    return "fit ok"


def nan_explain_lr():
    w = WrapCalibratedExplainer(LogisticRegression(max_iter=5000))
    w.fit(X_pr, y_pr)
    w.calibrate(X_cal, y_cal)
    return w.explain_factual(with_nan(X_te[:1]))


def inf_cal_rf():
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=20, random_state=0))
    w.fit(X_pr, y_pr)
    bad = X_cal.copy()
    bad[0, 0] = np.inf
    w.calibrate(bad, y_cal)
    return "calibrate ok"


def filter_features_known_issue():
    w = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=20, random_state=0))
    w.fit(X_pr, y_pr)
    w.calibrate(X_cal, y_cal)
    f = w.explain_factual(X_te[:2])
    return f.filter_features(exclude_features=[0])


run("NaN in fit data, RandomForest", nan_fit_rf)
run("NaN in calibration data, RandomForest", nan_cal_rf)
run("NaN in fit data, LogisticRegression", nan_fit_lr)
run("NaN in explained case, LogisticRegression", nan_explain_lr)
run("inf in calibration data, RandomForest", inf_cal_rf)
run("filter_features(exclude_features=[0])", filter_features_known_issue)

print("\n=== CLI list all")
r = subprocess.run([sys.executable, "-m", "calibrated_explanations.plugins.cli", "list", "all"], capture_output=True, text=True)
print("exit", r.returncode, "|", (r.stdout or r.stderr)[:300])
r = subprocess.run([sys.executable, "-m", "calibrated_explanations.plugins.cli", "list", "explanations", "--trusted-only"], capture_output=True, text=True)
print("exit", r.returncode, "|", (r.stdout or r.stderr)[:300])
