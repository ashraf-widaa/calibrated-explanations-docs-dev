# Conformal Interval Regression (CPS)

Regression in Calibrated Explanations is **conformal interval regression** implemented via **Conformal Predictive Systems (CPS)**.

- **Canonical semantics:** Point regression + calibrated uncertainty intervals = conformal regression.
- **Interval control:** The specific interval width is controlled by `low_high_percentiles`.

## Percentile or interval regression semantics note

- **Calibration prerequisites**: fit on `x_proper, y_proper` and calibrate on held-out `x_cal, y_cal`.
- **Mode-specific guarantees**: CPS returns calibrated percentile intervals for requested `low_high_percentiles`.
- **Assumptions**: calibration and deployment data are exchangeable or distribution-matched.
- **Explicit non-guarantees**: no guarantee under drift or fixed interval width across subpopulations.
- **Explanation-envelope limits**: feature-level interval effects summarize model behavior under perturbation.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics`.
- **How CE computes these outputs**: {doc}`../foundations/concepts/calibration_methods`.

## Supported signatures

| Method | Description |
| :--- | :--- |
| `predict(x)` | Calibrated point estimate: the CPS median (50th percentile), which can differ from the model's own prediction |
| `predict(x, uq_interval=True, ...)` | Point estimate + CPS parameterised interval |
| `explain_factual(x, ...)` | Factual explanation with CPS intervals |
| `explore_alternatives(x, ...)` | Alternative explanations with CPS intervals |

`predict(x, calibrated=False)` returns the underlying model's prediction instead.

## Controlling the interval: `low_high_percentiles`

The `low_high_percentiles` parameter (tuple `(low, high)`) governs the CPS interval.

* Default: `(5, 95)` → 90% central interval.
* One-sided: `(-np.inf, 95)` or `(5, np.inf)`.

For a one-sided interval, the open side is reported as the smallest (`-np.inf`)
or largest (`np.inf`) target value in the calibration set. That value is a
placeholder, not a calibrated bound: treat that side of the interval as open.
Because the point prediction is the median, a one-sided interval whose finite
percentile is below 50, such as `(-np.inf, 40)`, does not contain it.

## Examples

### 1. Point prediction + 90% conformal interval

```python
# Returns median, low (5th percentile), and high (95th percentile)
prediction, (low, high) = explainer.predict(
    x_test,
    uq_interval=True,
    low_high_percentiles=(5, 95)
)
print(f"Prediction: {prediction[0]} Interval: {low[0]} – {high[0]}")
```

### 2. Explanation with specific interval settings

You can request explanations with arbitrary confidence levels by strictly passing the percentiles:

```python
# Explain with a 50% central interval (25th - 75th percentiles)
explanation = explainer.explain_factual(
    x_test,
    low_high_percentiles=(25, 75)
)
```

## Key semantics

* **Prediction Interval:** The interval returned by `predict(..., uq_interval=True)` is the conformal interval derived from the CPS.
* **Rule Intervals:** The explanation envelopes on feature weights in `explain_factual` rules are also derived from the underlying CPS calibration.

## Adaptive and per-group intervals

* Intervals whose width depends on how difficult each instance is to predict:
  {doc}`../practitioner/advanced/normalization-guide`.
* Separate calibration for each group (Mondrian `bins`):
  {doc}`../foundations/how-to/conditional_calibration`.

## Go further

- Executable demo: [demo_regression.ipynb](https://github.com/Moffran/calibrated_explanations/blob/main/notebooks/core_demos/demo_regression.ipynb)
- Full signatures: {doc}`WrapCalibratedExplainer API reference <../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer>`
- Check CE on your own data: {doc}`../practitioner/evaluate_ce`

Entry-point tier: Tier 2.
