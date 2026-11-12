# Probabilistic and interval regression

When the target is a number, such as a disease-progression score or a price,
you can ask CE two different questions about it:

- **Where will the value fall?** This is *interval regression*: a prediction
  with a calibrated interval, for example "about 172, between 85 and 308".
- **How likely is an event on the value?** This is *probabilistic
  regression*: a calibrated probability, for example "a 42% chance that the
  value is at most 150".

The model and the calibration are the same; only the question changes. This
page explains both, shows real outputs, and lists common mistakes. For the
guarantees, assumptions and non-guarantees of each mode, use
{doc}`calibrated_interval_semantics`.

## Mode routing

| Mode | API signal | Output | Primary question |
| --- | --- | --- | --- |
| Percentile or interval regression | `predict(..., uq_interval=True, low_high_percentiles=...)` | Numeric prediction with CPS percentile interval | Where will `y` fall? |
| Probabilistic or thresholded regression | `predict_proba(..., threshold=...)` | Calibrated event probability with interval | How likely is an event on `y`? |

"Thresholded regression" is another name for probabilistic regression, used
in implementation documents ({doc}`terminology_thresholded_vs_probabilistic_regression`).

## A worked example

The example uses scikit-learn's diabetes data: the target is a measure of
disease progression one year after baseline.

```python
import warnings

from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from calibrated_explanations import WrapCalibratedExplainer

warnings.simplefilter("ignore")
data = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=0
)
X_proper, X_cal, y_proper, y_cal = train_test_split(
    X_train, y_train, test_size=0.25, random_state=0
)

explainer = WrapCalibratedExplainer(RandomForestRegressor(random_state=0))
explainer.fit(X_proper, y_proper)
explainer.calibrate(X_cal, y_cal, feature_names=data.feature_names)
```

### Interval regression: where will the value fall?

```python
point, (low, high) = explainer.predict(X_test[:3], uq_interval=True)
for p, lo, hi in zip(point, low, high):
    print(f"prediction {p:6.1f}   90% interval [{lo:6.1f}, {hi:6.1f}]")
```

```text
prediction  273.4   90% interval [ 186.5,  409.2]
prediction  248.2   90% interval [ 161.2,  384.0]
prediction  172.1   90% interval [  85.2,  308.0]
```

By default CE asks for the 5th and 95th percentiles, a 90% interval; change
them with `low_high_percentiles`. The interval comes from a **conformal
predictive system** fitted on the calibration set.

### Probabilistic regression: how likely is an event?

Pass a `threshold` to `predict_proba`. CE returns two columns: the
probability that the event does **not** happen, and the probability that it
does. With a single number `t`, the event is **y ≤ t**.

```python
proba, (p_low, p_high) = explainer.predict_proba(X_test[:3], threshold=150, uq_interval=True)
for row, lo, hi in zip(proba, p_low, p_high):
    print(f"P(y <= 150) = {row[1]:.3f}   range [{lo:.3f}, {hi:.3f}]")
```

```text
P(y <= 150) = 0.077   range [0.000, 0.083]
P(y <= 150) = 0.083   range [0.000, 0.091]
P(y <= 150) = 0.417   range [0.364, 0.455]
```

**Reading it.** The first two cases are predicted far above 150 (273 and 248),
so the calibrated probability of a value at or below 150 is low. The third,
predicted at 172, is closer to the threshold, and its probability is about
0.42. The range is the uncertainty of that probability, as for classification.

**Other events.** A pair `(low, high)` asks for the event **low < y ≤ high**,
and an array gives one threshold per case:

```python
proba_int, (i_low, i_high) = explainer.predict_proba(
    X_test[:3], threshold=(100, 200), uq_interval=True
)
for row, lo, hi in zip(proba_int, i_low, i_high):
    print(f"P(100 < y <= 200) = {row[1]:.3f}   range [{lo:.3f}, {hi:.3f}]")
```

```text
P(100 < y <= 200) = 0.200   range [0.000, 0.250]
P(100 < y <= 200) = 0.200   range [0.000, 0.250]
P(100 < y <= 200) = 0.503   range [0.476, 0.529]
```

### Explaining a threshold prediction

The same `threshold` turns an explanation into an explanation of the
**event probability**. Weights are then in probability units.

```python
factual = explainer.explain_factual(X_test[2:3], threshold=150)
pred = factual[0].prediction
print(f"P(y <= 150) = {pred['predict']:.3f}  range [{pred['low']:.3f}, {pred['high']:.3f}]")
```

```text
P(y <= 150) = 0.417  range [0.364, 0.455]
```

For this case the strongest rule is `s5 <= 0.02` with a weight of about
+0.29: with typical values from the other side of that split, the calibrated
probability of a value at or below 150 would be about 0.29 lower. As always,
this describes the model's response, not a cause.

## How CE computes the probability

The two modes use the calibration set differently. Interval mode fits the CPS
on the full calibration set. Probabilistic mode randomly splits it into two
halves: one half fits a CPS that scores the threshold event, and the other
half calibrates those scores with Venn-Abers, so each step uses about half of
the calibration cases. See {doc}`../../tasks/probabilistic_regression` and,
for the mathematics, {doc}`calibration_methods` (section 4). *The exact
validity statement for this two-step construction is under review by the CE
authors.*

## Common mistakes

| Mistake | What to do instead |
|---|---|
| Reading the first column as the event probability | The event probability is the **second** column, `proba[:, 1]`; the first is 1 minus it |
| Reading P(y ≤ t) as P(y > t) | P(y > t) = 1 − P(y ≤ t) |
| Passing both `threshold` and `confidence_level` | They are mutually exclusive and raise `ConfigurationError`; see the {doc}`parameter reference <parameter-reference>` |
| A threshold in different units from the target | The threshold is compared with `y` directly; use the target's own scale |
| Treating the probability as a statement about one individual case | Like all CE guarantees, it is a calibration property over many cases, under exchangeability |

## Related pages

- {doc}`../../get-started/quickstart_regression`
- {doc}`../how-to/interpret_explanations`
- {doc}`../../tasks/probabilistic_regression`
- {doc}`calibrated_interval_semantics`

Entry-point tier: Tier 3.
