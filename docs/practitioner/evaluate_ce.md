# Evaluate CE on your own data

Use this guide once your CE workflow runs. It checks the outputs on held-out
data: label accuracy, probability scores and reliability for classification,
and observed target coverage and width for interval regression. For the
integration steps, start with {doc}`../get-started/apply-to-your-data`.

The checks below are **empirical**: they tell you how CE behaved on your test
data. They do not prove a guarantee, and they do not replace the conditions in
the {doc}`semantics reference <../foundations/concepts/calibrated_interval_semantics>`.


**How-to guide · about 30 minutes.** Check CE's outputs on your own
held-out data after you
{doc}`apply CE to your own data <../get-started/apply-to-your-data>`.

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

### Threshold events (probabilistic regression)

With a `threshold`, CE returns the calibrated probability of an event such as
*y ≤ 150* instead of an interval. Check it like a classification probability:
compare it with how often the event actually happened on the test set.

```python
threshold = 150
p_event, (p_lo, p_hi) = reg.predict_proba(Xr_test, threshold=threshold, uq_interval=True)
p = p_event[:, 1]
observed = (yr_test <= threshold).astype(int)
print(f"Observed share with y <= {threshold}: {observed.mean():.3f}")
print(f"Mean predicted P(y <= {threshold}):  {p.mean():.3f}")
print(f"Brier score: {brier_score_loss(observed, p):.4f}")
print(f"Mean width of [low, high]: {np.mean(p_hi - p_lo):.3f}")
frac_pos, mean_pred = calibration_curve(observed, p, n_bins=4, strategy="quantile")
print("Reliability (quantile bins): mean predicted -> observed share")
for mp, fp in zip(mean_pred, frac_pos):
    print(f"  {mp:.2f} -> {fp:.2f}")
```

```text
Observed share with y <= 150: 0.528
Mean predicted P(y <= 150):  0.444
Brier score: 0.1965
Mean width of [low, high]: 0.123
Reliability (quantile bins): mean predicted -> observed share
  0.19 -> 0.21
  0.42 -> 0.47
  0.60 -> 0.74
  0.76 -> 0.86
```

**Reading it.** The event probability is in column 1, `p_event[:, 1]`. On
these 89 test cases the predicted probabilities are on average lower than the
observed shares (0.444 against 0.528), most visibly in the upper bins. With
about 22 cases per bin and one split, a difference of this size can arise by
chance; repeat the check with other seeds or more data before concluding that
the event probabilities are systematically too low. The event construction
uses half of the calibration set for the conformal scores and half for
Venn–Abers calibration (see
{doc}`../foundations/concepts/probabilistic_regression`), so its estimates
rest on fewer calibration cases than the intervals above. *The exact validity
statement for these event probabilities is under review by the CE authors.*

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

### Checking a subgroup

To see whether a subgroup behaves differently, repeat the coverage check of
section 3 within each group. Here the groups are the two values of the
diabetes dataset's `sex` column, which it stores as two scaled numbers.

```python
sex = Xr_test[:, 1]  # the 'sex' column; the dataset stores it as two scaled values
for value in np.unique(sex):
    group = sex == value
    inside_g = (yr_test[group] >= lo[group]) & (yr_test[group] <= hi[group])
    print(f"group sex={value:+.3f}: {group.sum()} cases, inside {inside_g.mean():.3f}, "
          f"mean width {np.mean(hi[group] - lo[group]):.1f}")
```

```text
group sex=-0.045: 54 cases, inside 0.963, mean width 222.8
group sex=+0.051: 35 cases, inside 0.943, mean width 222.8
```

**Reading it.** Both groups show a share near the requested 90% here, but
with 54 and 35 cases this says little: a few cases more or less inside would
change the shares noticeably. The mean width is the same in both groups
because standard conformal intervals have the same width for every case.
If groups differ systematically in how hard they are to predict, consider
{doc}`difficulty-adapted intervals <advanced/normalization-guide>` or
{doc}`Mondrian (conditional) calibration <../foundations/how-to/conditional_calibration>`.
*What Mondrian calibration guarantees within each group, and under which
conditions, is under review by the CE authors.*

(after-the-learning-journey)=
## Where next

You have now run, read, applied and checked CE. To go deeper, study
{doc}`Understand CE <../sections/understand-ce>` (workflow, calibration methods
and the guarantees by mode), or browse the task guides and playbooks in
{doc}`CE in Practice <../sections/in-practice>`.

## Related pages

- {doc}`index` (practitioner hub)
- {doc}`../foundations/concepts/ce_workflow` (how CE works)
- {doc}`../get-started/troubleshooting`
