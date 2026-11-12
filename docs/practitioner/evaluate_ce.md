# Evaluate CE on your own data

This guide takes you from a working example to a checked, reproducible
application: how to set CE up on your own data, how to check its calibrated
outputs on held-out data, the most common mistakes, and the situations where
CE's outputs should not be trusted. It assumes you have completed the
{doc}`Quick Start <../get-started/index>`.

The checks below are **empirical**: they tell you how CE behaved on your test
data. They do not prove a guarantee, and they do not replace the conditions in
the {doc}`semantics reference <../foundations/concepts/calibrated_interval_semantics>`.

## 1. Set up reproducibly

Use three separate data sets, fix every random seed, and keep the test set out
of both training and calibration.

```python
import warnings

import numpy as np
from sklearn.calibration import calibration_curve
from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, brier_score_loss, log_loss
from sklearn.model_selection import train_test_split

from calibrated_explanations import WrapCalibratedExplainer

warnings.simplefilter("ignore")
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, stratify=data.target, random_state=42
)
X_proper, X_cal, y_proper, y_cal = train_test_split(
    X_train, y_train, test_size=0.25, stratify=y_train, random_state=42
)
clf = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=100, random_state=42))
clf.fit(X_proper, y_proper)
clf.calibrate(X_cal, y_cal)
```

**Record what you used:** the CE version (`calibrated_explanations.__version__`),
the scikit-learn version, the seeds and the split sizes. To reuse a calibrated
explainer later, `clf.save_state(path)` writes a JSON-safe artifact and
`WrapCalibratedExplainer.load_state(path, learner=model)` restores it; the
trained model itself is not stored and must be passed back.

## 2. Check calibrated probabilities (classification)

Three questions: are the labels accurate enough for your task, are the
probabilities sensible, and how wide are the ranges?

```python
proba, (low, high) = clf.predict_proba(X_test, uq_interval=True)
p = proba[:, 1]
print(f"Accuracy:    {accuracy_score(y_test, clf.predict(X_test)):.3f}")
print(f"Brier score: {brier_score_loss(y_test, p):.4f}")
print(f"Log loss:    {log_loss(y_test, p):.4f}")
print(f"Mean width of [low, high]: {np.mean(high - low):.3f}")
frac_pos, mean_pred = calibration_curve(y_test, p, n_bins=5, strategy="quantile")
print("Reliability (quantile bins): mean predicted -> observed share of benign")
for mp, fp in zip(mean_pred, frac_pos):
    print(f"  {mp:.2f} -> {fp:.2f}")
```

```text
Accuracy:    0.947
Brier score: 0.0445
Log loss:    0.1676
Mean width of [low, high]: 0.118
Reliability (quantile bins): mean predicted -> observed share of benign
  0.03 -> 0.00
  0.34 -> 0.37
  0.80 -> 1.00
  0.94 -> 1.00
  0.97 -> 1.00
```

**Reading it.**

- **Brier score and log loss** measure the probabilities themselves (lower is
  better). Compare them with the same scores for the uncalibrated model
  (`clf.predict_proba(X_test, calibrated=False)`); calibration does not
  necessarily improve them on every dataset, as the
  {doc}`walkthrough <../get-started/quickstart_walkthrough>` shows for this one.
- **The reliability table** groups test cases by predicted probability and
  compares the average prediction with the observed share. For calibrated
  probabilities the two columns should be close. Here each bin holds only
  about 23 test cases, so differences of this size are expected from chance
  alone; use a larger test set before drawing conclusions.
- **The mean width** summarises how uncertain the calibrated probabilities
  are. Track it over time: a change can signal that new data differ from the
  calibration data.

## 3. Check intervals (regression)

For interval regression, count how often the true value falls inside the
interval on the test set, and how wide the intervals are.

```python
reg_data = load_diabetes()
Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    reg_data.data, reg_data.target, test_size=0.2, random_state=0
)
Xr_proper, Xr_cal, yr_proper, yr_cal = train_test_split(
    Xr_train, yr_train, test_size=0.25, random_state=0
)
reg = WrapCalibratedExplainer(RandomForestRegressor(random_state=0))
reg.fit(Xr_proper, yr_proper)
reg.calibrate(Xr_cal, yr_cal)
point, (lo, hi) = reg.predict(Xr_test, uq_interval=True)
inside = (yr_test >= lo) & (yr_test <= hi)
print(f"Test cases: {len(yr_test)}")
print(f"Share of test values inside the 90% interval: {inside.mean():.3f}")
print(f"Mean interval width: {np.mean(hi - lo):.1f}")
```

```text
Test cases: 89
Share of test values inside the 90% interval: 0.955
Mean interval width: 222.8
```

**Reading it.** On these 89 test cases, 95.5% of the true values fall inside
the requested 90% intervals. A share near or above the requested level is
what you hope to see; with few test cases, the share varies from one split to
the next, so repeat the check with other seeds before reading much into it. A
share clearly **below** the requested level, repeated across splits, is a
reason to investigate: the calibration data may not represent the new data.
Narrower intervals are more useful, but only if the share stays acceptable.
*What coverage CE guarantees, and under which assumption, is stated on the
semantics page; that wording is under review by the CE authors.*

## 4. Common mistakes

| Mistake | Consequence | Do instead |
|---|---|---|
| Calibrating on the training data | The model looks more reliable than it is | Use a separate calibration set the model never saw |
| Evaluating on the calibration set | Optimistic results | Keep a third, untouched test set |
| Preprocessing (for example scaling) fitted on all data before splitting | Information leaks from test and calibration data into training | Split first; fit preprocessing on the training data only, or use a pipeline ({doc}`../foundations/how-to/integrate_with_pipelines`) |
| Predicting before `calibrate` | Uncalibrated outputs (CE warns) | Always `fit`, then `calibrate`, then predict or explain |
| Reading the first column of `predict_proba` with a threshold | You read 1 − P(event) | Use `proba[:, 1]`; see {doc}`../foundations/concepts/probabilistic_regression` |
| Reading explanation weights as causes | Wrong decisions | Weights describe the model's response; see {doc}`../foundations/how-to/interpret_explanations` |
| Judging calibration from one small test set | Conclusions driven by chance | Repeat with several seeds or a larger test set |

## 5. When not to trust the outputs

- **The data have changed.** If the population, measurement process or time
  period differs from the calibration data, the calibration may not apply.
  Recalibrate on recent, representative data.
- **Subgroups matter.** The calibration is for the data as a whole, not for
  each subgroup. If you need calibration per group, use
  {doc}`Mondrian (conditional) calibration <../foundations/how-to/conditional_calibration>`.
- **The case is unusual.** For cases far from the calibration data,
  explanations may rely on substituted values that rarely occur together;
  {doc}`guarded explanations <../foundations/concepts/guarded_explanations>`
  filter such values out (experimental).
- **The model is not good enough.** CE calibrates and explains a model; it does
  not make a weak model accurate. Evaluate accuracy for your task separately.

## Related pages

- {doc}`index` (practitioner hub)
- {doc}`../foundations/concepts/ce_workflow` (how CE works, with a learning path)
- {doc}`../get-started/troubleshooting`

Entry-point tier: Tier 3.
