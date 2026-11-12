# Regression quickstart

**Path C, step 3.** Calibrate a regression model once, then use it in two
modes: **interval regression** (a predicted number with an interval) and
**probabilistic regression** (the calibrated probability that the target is at
or below a threshold you choose). The example predicts a disease-progression
score one year ahead. If you have not yet chosen a mode, start with
{doc}`ce-tasks-and-modes`.

## Prerequisites

```bash
pip install calibrated-explanations scikit-learn
```

You need a regression model with `predict`, and labelled data you can split
into training, calibration and test sets.

## Interval regression semantics note

- **Calibration prerequisites**: fit on `x_proper, y_proper` and calibrate on held-out `x_cal, y_cal`.
- **Mode-specific guarantees**: percentile intervals use CPS for requested percentile bounds.
- **Assumptions**: calibration and deployment data are exchangeable or distribution-matched.
- **Explicit non-guarantees**: no guarantee under drift or fixed interval width across subpopulations.
- **Explanation-envelope limits**: feature-level intervals summarize model behavior under perturbation.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics`.

## Probabilistic or thresholded regression semantics note

- **Calibration prerequisites**: fit on `x_proper, y_proper` and calibrate on held-out `x_cal, y_cal`.
- **Mode-specific guarantees**: threshold queries use CPS with Venn-Abers for calibrated event probabilities.
- **Assumptions**: calibration and deployment data are exchangeable or distribution-matched.
- **Explicit non-guarantees**: no guarantee under drift, and no causal guarantee from threshold probabilities.
- **Explanation-envelope limits**: feature-level intervals summarize model behavior under perturbation.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics`.

## 1. Prepare the dataset

```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

dataset = load_diabetes()
x = dataset.data
y = dataset.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, random_state=0
)
print(len(x_proper), len(x_cal), len(x_test))
```

```text
264 89 89
```

The features of this dataset are already centred and scaled, which is why the
rules below show small values such as `bmi > -0.00`.

## 2. Fit and calibrate the explainer

```python
from sklearn.ensemble import RandomForestRegressor
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(RandomForestRegressor(random_state=0))
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal, feature_names=dataset.feature_names)
```

## 3. Interval predictions

```python
pred, (low, high) = explainer.predict(x_test[:3], uq_interval=True)
for p, lo, hi, true in zip(pred, low, high, y_test[:3]):
    print(f"predicted {p:6.1f}  interval [{lo:6.1f}, {hi:6.1f}]  actual {true:.0f}")
```

```text
predicted  273.4  interval [ 186.5,  409.2]  actual 321
predicted  248.2  interval [ 161.2,  384.0]  actual 215
predicted  172.1  interval [  85.2,  308.0]  actual 127
```

By default the interval runs from the 5th to the 95th percentile, so it aims
to contain the true value for about 90% of cases, **on average over cases**
under exchangeability; it does not promise that for any one case. Set other
percentiles with `low_high_percentiles=(10, 90)`. The intervals are wide
because this small dataset is hard to predict; here all three actual values
fall inside.

## 4. Probabilistic regression: the probability of a threshold event

```python
probabilities, (p_low, p_high) = explainer.predict_proba(
    x_test[:3], threshold=150, uq_interval=True
)
for p, lo, hi in zip(probabilities[:, 1], p_low, p_high):
    print(f"P(y <= 150) = {p:.3f}  range [{lo:.3f}, {hi:.3f}]")
```

```text
P(y <= 150) = 0.077  range [0.000, 0.083]
P(y <= 150) = 0.083  range [0.000, 0.091]
P(y <= 150) = 0.417  range [0.364, 0.455]
```

With `threshold=150`, the event is *y ≤ 150*, and its calibrated probability
is the **second** column, `probabilities[:, 1]`. For the first case,
progression of 150 or less is unlikely (about 8%); for the third, which the
model predicts at about 172, it is about 42%. This mode splits the calibration
set in two, so its ranges can be wider than in classification (limitation 3 in
{doc}`ce-tasks-and-modes`).

## 5. Explain a prediction

```python
factual = explainer.explain_factual(x_test[:1])
rules = factual[0].get_rules()
top = sorted(range(len(rules["weight"])), key=lambda i: -abs(rules["weight"][i]))[:3]
for i in top:
    print(f"{rules['rule'][i]:<14} weight {rules['weight'][i]:+7.1f} "
          f"[{rules['weight_low'][i]:+7.1f}, {rules['weight_high'][i]:+7.1f}]")
```

```text
bmi > -0.00    weight  +128.2 [   -7.6,  +215.1]
bp > 0.03      weight   +98.3 [  -37.6,  +185.2]
s2 <= 0.02     weight   +16.0 [ -119.8,  +102.9]
```

In interval regression, a weight is in the units of the target. A positive
weight means the condition raises the calibrated prediction: with typical
values from the other side of the condition, the prediction would be about that
much lower. All three ranges here include 0, so even the strongest rules
are not firmly supported in direction. That is common with a small calibration
set, and it is exactly what the ranges are there to show.

## 6. Explore alternatives for a threshold

```python
alternatives = explainer.explore_alternatives(x_test[:2], threshold=150)
alt = alternatives[0].get_rules()
for rule, p, lo, hi in zip(alt["rule"], alt["predict"],
                           alt["predict_low"], alt["predict_high"]):
    print(f"if {rule:<12} P(y <= 150) = {p:.2f} [{lo:.2f}, {hi:.2f}]")
```

```text
if bmi < 0.09   P(y <= 150) = 0.33 [0.24, 0.38]
if bp < 0.07    P(y <= 150) = 0.31 [0.24, 0.33]
if s5 < -0.00   P(y <= 150) = 0.10 [0.00, 0.11]
```

Each line is a what-if for the first case: the calibrated probability of
*y ≤ 150* if one feature had a value in the stated range. Lower `bmi` or blood
pressure (`bp`) would raise it from about 0.08 to about 0.3. These describe the
model's behaviour, not the effect of changing a patient's measurements.

## Common mistakes

- Reading the first column of `predict_proba(..., threshold=...)` as the event
  probability; it is the second.
- Reading the interval as a guarantee for one case; coverage is on average
  over cases.
- Calibrating on training data, or on data from a different population.
- Treating a weight as a cause, or an alternative as a recommended action.

## Next

- {doc}`../foundations/concepts/probabilistic_regression`
- {doc}`quickstart_guarded`, to filter explanations to typical feature values.
- {doc}`apply-to-your-data`, to use your own data and model.
- {doc}`../foundations/how-to/interpret_explanations`
- {doc}`../citing`

Entry-point tier: Tier 2.
