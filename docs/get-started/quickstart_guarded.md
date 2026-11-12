# Guarded explanations quickstart

**Path C, step 4.** Guarded explanations are an **explanation
configuration**, not a separate prediction task: you add
`guarded_options=GuardedOptions()` to an explanation call in any mode
(classification, interval or probabilistic regression). CE then drops
candidate rules whose substituted feature values look unusual compared with
the calibration data, so explanations stay closer to the data the model was
calibrated on. Predictions and their ranges are unchanged. The example below
uses binary classification.

## Prerequisites

```bash
pip install calibrated-explanations scikit-learn
```

You need a calibrated explainer, as in {doc}`quickstart_classification` or
{doc}`quickstart_regression`.

## Classification guarded semantics note

- **Calibration prerequisites**: fit on proper split and calibrate on held-out calibration split.
- **Mode-specific guarantees**: guarded outputs are schema-compatible with CE helpers while filtering interval candidates through the shipped mixed guard rule.
- **Assumptions**: exchangeability or calibration-deployment distribution match.
- **Explicit non-guarantees**: no whole-interval guard certification, no metric identity with standard CE, no guarantee under drift, and no causal guarantee for suggested changes.
- **Explanation-envelope limits**: rule intervals remain model-response summaries.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics` and
  {doc}`../foundations/concepts/guarded_explanations`.

```{admonition} Fast explainers are not supported in guarded mode
:class: warning

Guarded mode requires a standard (non-fast) `CalibratedExplainer`.
Passing a fast explainer — one initialised with `CalibratedExplainer(..., fast=True)` or
retrieved via `WrapCalibratedExplainer` with fast mode enabled — raises a
`ConfigurationError` at the `explain_factual(guarded_options=GuardedOptions())` /
`explore_alternatives(guarded_options=GuardedOptions())` call site.  See ADR-032, decision 7 for the rationale.
```

For guarded regression workflows, start from {doc}`quickstart_regression`.
The only workflow difference is passing `guarded_options=GuardedOptions()` to the explanation call:

- Use `explain_factual(..., guarded_options=GuardedOptions())` instead of `explain_factual(...)`.
- Use `explore_alternatives(..., guarded_options=GuardedOptions())` instead of `explore_alternatives(...)`.

> **Migration**: `guarded=True` was removed in v0.11.5. Use `guarded_options=GuardedOptions()` everywhere.

## 1. Load data and split sets

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

dataset = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(
    dataset.data, dataset.target, test_size=0.2,
    stratify=dataset.target, random_state=0,
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25,
    stratify=y_train, random_state=0,
)
```

## 2. Fit and calibrate

```python
from sklearn.ensemble import RandomForestClassifier
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(RandomForestClassifier(random_state=0))
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal, feature_names=dataset.feature_names)
```

## 3. Guarded factual and alternatives

```python
from calibrated_explanations.explanations.guarded_options import GuardedOptions
guarded_factual = explainer.explain_factual(x_test[:5], guarded_options=GuardedOptions(confidence=0.9))
guarded_alts = explainer.explore_alternatives(x_test[:2], guarded_options=GuardedOptions(confidence=0.9))
for i in range(5):
    print(f"case {i}: {len(guarded_factual[i].get_rules()['rule'])} guarded rules")
```

```text
case 0: 25 guarded rules
case 1: 0 guarded rules
case 2: 28 guarded rules
case 3: 24 guarded rules
case 4: 24 guarded rules
```

`confidence=0.9` is the default; higher values are more inclusive and remove
fewer candidates. Case 1 has no rules: the guard removed every candidate
interval, and CE says so in a `UserWarning` ("All interval candidates were
removed by the guard ..."). That is a signal to look at the case, not an
error. Guarded and standard explanations are not computed identically, so
do not compare their rule counts or weights one to one.

The guarded explanation of case 0 as a chart, with its six strongest rules:

```python
guarded_factual.plot(0, uncertainty=True, filter_top=6)
```

```{figure} quickstart_assets/guarded-factual-case0.png
:alt: Guarded factual explanation plot for case 0: calibrated probability of benign about 0.08; six rules, each a range of feature values such as 0.06233 < mean concave points <= 0.08508, all with weights below 0 and most with ranges that cross 0.

Guarded explanation of case 0, as drawn by `guarded_factual.plot(0, uncertainty=True, filter_top=6)`.
```

The plot reads like a standard factual plot (see the
{doc}`walkthrough, section 7 <quickstart_walkthrough>`). Guarded rules are often
bounded on both sides, such as `0.06233 < mean concave points <= 0.08508`,
because the guard works on ranges of feature values that it has checked
against the calibration data.

## 4. Audit guarded filtering

```python
audit = guarded_factual.get_guarded_audit()
for key, value in audit["summary"].items():
    print(f"{key}: {value}")
```

```text
n_instances: 5
intervals_tested: 945
intervals_conforming: 743
intervals_removed_guard: 202
intervals_emitted: 101
instances_with_any_removed_guard: 5
instances_all_intervals_removed_guard: 1
instances_with_zero_emitted: 1
```

Across the five cases, the guard tested 945 candidate intervals, accepted
743 and removed 202; 101 rules were emitted in the explanations. Every case
lost at least one candidate, and for one case (case 1) all were removed.
`audit["instances"]` gives the same figures per case, down to each tested
interval.

Key audit fields:
- `intervals_conforming`: candidate intervals accepted by the shipped guard rule.
- `intervals_removed_guard`: candidate intervals rejected by the shipped guard rule.

## Common mistakes

- Treating guarded explanations as a different task or a different model:
  only the explanation call changes.
- Reading a guarded explanation as a certificate that every value in a rule's
  interval is typical; the guard checks representative values, not the whole
  interval.
- Expecting the guard to detect that the case itself is unusual; it checks
  the substituted values (see the limitations in
  {doc}`../foundations/concepts/guarded_explanations`).
- Using a fast explainer, which guarded mode does not support.

Next steps:
- {doc}`apply-to-your-data`, to use your own data and model.
- {doc}`../foundations/concepts/guarded_explanations`
- {doc}`../foundations/concepts/alternatives`
- {doc}`../foundations/how-to/interpret_explanations`

Entry-point tier: Tier 2.
