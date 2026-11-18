# Quick API: cheat sheet of the main calls

<span id="quick-api-main-components-and-calls"></span>

This page is a compact map of the calls you use with `WrapCalibratedExplainer`,
part of {doc}`CE Software & Integration <../sections/software-integration>`.
For what each output means, start with {doc}`ce-tasks-and-modes` (How CE Works);
for longer worked examples, see the {doc}`Python tutorials <../tutorials/index>`.
Full signatures are in the {doc}`API reference <../api/index>`.

## What you need

:::{div} ce-table-compact
| Question | Answer |
|---|---|
| How do I install it? | `pip install calibrated-explanations` (Python 3.10 or later). Plotting needs the `viz` extra: `pip install "calibrated-explanations[viz]"`. Details and other extras: {doc}`installation`. |
| What do I import? | `from calibrated_explanations import WrapCalibratedExplainer` |
| Which model? | A scikit-learn-style model with `fit` and `predict`; a classifier also needs `predict_proba`. CE wraps it and does not change it. |
| Which data? | Three parts with known labels: a **proper training set** for `fit`, a **calibration set** the model never saw for `calibrate`, and the cases you want to predict or explain. |
| What are the minimum steps? | `fit` → `calibrate` → `predict_proba` or `predict` → `explain_factual` or `explore_alternatives`. |
| Which call for my task? | Classification: `predict_proba`. Interval regression: `predict(..., uq_interval=True)`. Probabilistic regression: `predict_proba(..., threshold=...)`. See {doc}`ce-tasks-and-modes`. |
| What comes back? | Calibrated predictions; with `uq_interval=True`, also a lower and an upper value. Explanation calls return collections you can print, plot or export, with a range for each feature weight. The prediction bounds and the weight ranges mean different things, and the bounds differ per task: see {doc}`../foundations/concepts/calibrated_interval_semantics`. |
| Something fails? | See {doc}`troubleshooting`. |
:::

## The components

| Component | Role | You create it? |
|---|---|---|
| Your model | Any scikit-learn-style classifier or regressor | Yes |
| `WrapCalibratedExplainer` | Wraps the model; holds the calibration; answers every call on this page | Yes |
| Calibrated predictions | NumPy arrays: a prediction, and with `uq_interval=True` a `(low, high)` pair | Returned |
| `CalibratedExplanations` | Collection returned by `explain_factual`; one explanation per case | Returned |
| `AlternativeExplanations` | Collection returned by `explore_alternatives`; one explanation per case | Returned |

## A complete minimal example

The example below runs as written. It uses the same data, split and model as
the {doc}`Python walkthrough <quickstart_walkthrough>`, and the case it prints
is the walkthrough's **case 2**.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from calibrated_explanations import WrapCalibratedExplainer

# Data: three parts. The model never sees the calibration or test parts.
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
X_proper, X_cal, y_proper, y_cal = train_test_split(
    X_train, y_train, test_size=0.25, stratify=y_train, random_state=42
)

# 1. Wrap and train your model.
explainer = WrapCalibratedExplainer(
    RandomForestClassifier(n_estimators=100, random_state=42)
)
explainer.fit(X_proper, y_proper)

# 2. Calibrate on the held-out calibration set.
explainer.calibrate(
    X_cal,
    y_cal,
    feature_names=list(data.feature_names),
    class_labels={0: "malignant", 1: "benign"},
)

# 3. Calibrated prediction with a range, for one test case.
case = X_test[2:3]
proba, (low, high) = explainer.predict_proba(case, uq_interval=True)
print(f"P(benign) = {proba[0, 1]:.3f}  range [{low[0]:.3f}, {high[0]:.3f}]")

# 4. Explanations of the same case.
factual = explainer.explain_factual(case)
alternatives = explainer.explore_alternatives(case)
print(type(factual).__name__, "with", len(factual), "explanation")
print(type(alternatives).__name__, "with", len(alternatives), "explanation")
```

```text
P(benign) = 0.286  range [0.167, 0.333]
CalibratedExplanations with 1 explanation
AlternativeExplanations with 1 explanation
```

How to read it: the calibrated probability that this case is benign is 0.286,
so the predicted class is malignant. For binary classification, `low` and
`high` are the lower and upper calibrated probability for the positive class
(here *benign*); they are bounds of a probability, not a confidence interval.
`factual.plot()` and `alternatives.plot()` draw the explanations; the
walkthrough shows and explains both plots.
What each range guarantees differs by mode: see the
{ref}`mode-specific semantics notes <quick-api-semantics-notes>` at the end of
this page. The {doc}`Quickstart <quickstart>` runs the same example step by
step, with the output of every step.

## Core calls by step

Each name links to its entry in the API reference.

:::{div} ce-table-compact
| Step | Call | Purpose |
|---|---|---|
| Train | {py:meth}`fit <calibrated_explanations.core.WrapCalibratedExplainer.fit>` | Fit the wrapped model on the proper training set (skip if the model is already fitted) |
| Calibrate | {py:meth}`calibrate <calibrated_explanations.core.WrapCalibratedExplainer.calibrate>` | Learn the calibration from held-out labelled data |
| Predict | {py:meth}`predict <calibrated_explanations.core.WrapCalibratedExplainer.predict>` | Calibrated prediction; interval with `uq_interval=True` |
| Predict | {py:meth}`predict_proba <calibrated_explanations.core.WrapCalibratedExplainer.predict_proba>` | Calibrated probabilities; with `threshold=` for probabilistic regression |
| Explain | {py:meth}`explain_factual <calibrated_explanations.core.WrapCalibratedExplainer.explain_factual>` | Factual explanations: which of the case's feature values move the calibrated prediction |
| Explain | {py:meth}`explore_alternatives <calibrated_explanations.core.WrapCalibratedExplainer.explore_alternatives>` | Alternative explanations: the calibrated prediction if a feature had a value in another range |
| Inspect | {py:meth}`plot <calibrated_explanations.explanations.CalibratedExplanations.plot>` | Plot the explanations in a collection |
| Inspect | {py:meth}`to_narrative <calibrated_explanations.explanations.CalibratedExplanations.to_narrative>` | Plain-text narrative of the explanations |
| Save | {py:meth}`save_state <calibrated_explanations.core.WrapCalibratedExplainer.save_state>`, {py:meth}`load_state <calibrated_explanations.core.WrapCalibratedExplainer.load_state>` | Store a fitted and calibrated explainer and load it again |
:::

## Core methods

The snippets in this and the following sections are a reference, not a
program: they assume an `explainer` that is already fitted and calibrated, as
in the example above, and data named `X_query` or `X_sample`.

```python
pred = explainer.predict(X_query)
pred, (low, high) = explainer.predict(X_query, uq_interval=True)
probs = explainer.predict_proba(X_query)
probs, (low, high) = explainer.predict_proba(X_query, uq_interval=True)
factual = explainer.explain_factual(X_query)
alternatives = explainer.explore_alternatives(X_query)
```

## Reject-aware prediction note

When `predict(...)` or `predict_proba(...)` is called with a non-`NONE`
`reject_policy`, the return value is a `RejectResult` envelope. For
`ONLY_ACCEPTED` and `ONLY_REJECTED`, `result.prediction` remains full-batch;
use `result.metadata["source_indices"]` and `result.metadata["matched_count"]`
to identify the matched subset. Reject-enabled `explain_factual(...)` and
`explore_alternatives(...)` return reject-aware collections
(`RejectCalibratedExplanations` / `RejectAlternativeExplanations`), not a
`RejectResult` envelope.

## Classification

```python
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal, feature_names=feature_names)
probs, (low, high) = explainer.predict_proba(X_sample, uq_interval=True)
```

## Percentile or interval regression

```python
pred, (low, high) = explainer.predict(
    X_sample,
    uq_interval=True,
    low_high_percentiles=(5, 95),
)
```

## Probabilistic or thresholded regression

```python
p = explainer.predict_proba(X_sample, threshold=120.0)
p, (plo, phi) = explainer.predict_proba(X_sample, uq_interval=True, threshold=120.0)
```

(quick-api-semantics-notes)=

## Mode-specific semantics notes

### Classification

- **Calibration prerequisites**: fit on proper split and calibrate on held-out calibration split.
- **Mode-specific guarantees**: CE returns a Venn-Abers pair and a merged class probability; the exact pair/merged-probability validity wording remains under author review (SR-03).
- **Assumptions**: exchangeability under the method-specific calibration protocol; the alternative distribution-match wording remains under author review (SR-01).
- **Explicit non-guarantees**: no guarantee under drift or regime shift.
- **Explanation-envelope limits**: feature-level intervals are model-response summaries, not causal claims.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics`.

### Percentile or interval regression

- **Calibration prerequisites**: fit regression model and calibrate CPS on held-out calibration split.
- **Mode-specific guarantees**: CPS percentile intervals for requested `low_high_percentiles`.
- **Assumptions**: exchangeability under the method-specific calibration protocol; the alternative distribution-match wording remains under author review (SR-01).
- **Explicit non-guarantees**: no guarantee under drift or fixed interval width across subpopulations.
- **Explanation-envelope limits**: interval effects on explanations summarize model behavior under perturbation.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics`.

### Probabilistic or thresholded regression

- **Calibration prerequisites**: fit regression model and calibrate before threshold queries.
- **Mode-specific guarantees**: threshold queries return event probabilities and ranges from CPS scores followed by Venn-Abers; the exact validity statement remains under author review (SR-15).
- **Assumptions**: exchangeability under the method-specific calibration protocol; the alternative distribution-match wording remains under author review (SR-01).
- **Explicit non-guarantees**: no guarantee under drift and no causal guarantee from threshold probabilities.
- **Explanation-envelope limits**: feature-level probability shifts are model-response summaries.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics`.

## Continue

- **Go deeper:** full signatures in the {doc}`API reference <../api/index>`.
- **See also:** the {doc}`Python tutorials <../tutorials/index>`; when a call
  fails, {doc}`troubleshooting`.
- **Before this:** {doc}`ce-tasks-and-modes` and {doc}`apply-overview`.

Verified with CE 1.0.2 (released) and 1.1.0.dev0 (this Beta's source) on
2026-11-16; the example's printed output is checked by the documentation tests.
