# Normalization and Difficulty Estimation

Use difficulty estimation when regression errors vary across the input space.
CE can scale calibration residuals by a positive difficulty estimate, then use
the same estimator when predicting. This changes how interval widths adapt to
the input; it does not establish a new coverage guarantee.

## What is Difficulty Estimation?

An estimator assigns a difficulty value to each input. In normalized CPS,
residuals are divided by this value during calibration and prediction ranges
are scaled back at inference. The value depends on the estimator you choose;
it is not a direct observation of the case's true uncertainty.

**Without difficulty estimation**: A global CPS uses common residual quantiles.
Conditioning and endpoint clipping can still affect reported widths.

**With difficulty estimation**: Interval width scales with estimated prediction difficulty

## When to Use

Consider difficulty estimation when:

* **Heteroscedastic data**: Prediction errors vary systematically across the feature space
* **Mixed complexity**: Some regions of input space are inherently harder to predict
* **Instance-specific intervals**: You need intervals that reflect per-instance uncertainty
* **Residual patterns**: You observe that residuals have non-constant variance

```{admonition} Signs You Need Difficulty Estimation
:class: tip

* Residual plots show "fan" or "funnel" shapes
* Some subgroups have much larger prediction errors
* Interval coverage varies significantly across the feature space
* Simple conformal intervals are too wide for easy cases or too narrow for hard cases
```

## How It Works

CE's interval-regression implementation uses `crepes` CPS. The relevant choices are:

1. **Standard (no normalization)**: Residuals are used directly
2. **Normalized residuals**: Residuals are divided by positive difficulty estimates
3. **Choice of estimator**: For example, ensemble variation or a neighbourhood-based estimate

Fit the estimator using proper-training data and keep it fixed for calibration
and inference. See the [crepes documentation](https://crepes.readthedocs.io/)
for estimator choices and their prerequisites.

## Configuration

Use the public wrapper's `set_difficulty_estimator` method after calibration.
It reinitializes the calibration internals with the supplied estimator.
The fragments below assume a regression `model`, proper-training and
calibration splits, and a query matrix `x_test`; see the
{doc}`regression tutorial <../../get-started/quickstart_regression>` for setup.

### Basic Usage

By default, no difficulty estimator is configured. This example uses
unnormalized residuals:

```python
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(model)
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal)

# Intervals are already calibrated with CPS
prediction, (low, high) = explainer.predict(
    x_test,
    uq_interval=True,
    low_high_percentiles=(5, 95)
)
```

### Advanced Configuration

For an ensemble regressor such as the tutorial's random forest, fit an
estimator of ensemble variation on the proper-training inputs. Then attach
it through the wrapper:

```python
from crepes.extras import DifficultyEstimator

difficulty = DifficultyEstimator().fit(X=x_proper, learner=model)
explainer.set_difficulty_estimator(difficulty)
prediction, (low, high) = explainer.predict(x_test, uq_interval=True)
```

## Trade-offs

| Aspect | Without Normalization | With Normalization |
| :--- | :--- | :--- |
| Interval width | Common residual quantiles in a global CPS | Scaled by the estimated difficulty |
| Complexity | Simpler | Requires difficulty model |
| Coverage | Subject to the CPS assumptions | Subject to the normalization protocol and CPS assumptions; evaluate by region |
| Computation | Faster | Slightly slower |

## Interpreting Normalized Intervals

When difficulty estimation is active:

* **Narrow or wide intervals**: Read in target units, at the requested percentiles.
* **Varying widths**: Can reflect the estimator's input-dependent scaling.
* **Coverage by region**: Check on held-out outcomes; width alone does not establish it.

The exact validity wording for normalized and group-conditioned intervals
remains under author review (SR-02). See
{doc}`../../foundations/concepts/calibrated_interval_semantics`.

```python
import numpy as np

prediction, (low, high) = explainer.predict(x_test, uq_interval=True)

# Examine interval widths
widths = high - low

# Compare relatively narrow and wide intervals in this query batch
easy_instances = widths < np.percentile(widths, 25)
hard_instances = widths > np.percentile(widths, 75)

print(f"Relatively narrow intervals: {easy_instances.sum()}")
print(f"Relatively wide intervals: {hard_instances.sum()}")
```

## Research Background

Difficulty estimation and normalized conformal prediction are documented in:

> Löfström, T., et al. (2025). Calibrated Explanations for Regression.
> Machine Learning 114, 100.
> [DOI: 10.1007/s10994-024-06642-8](https://link.springer.com/article/10.1007/s10994-024-06642-8)

The underlying conformal prediction methodology:

> Boström, H., et al. (2021). crepes: Conformal Regressors and Predictive Systems.
> [crepes documentation](https://crepes.readthedocs.io/)

## Cross-References

* {doc}`../../tasks/regression` - Regression task documentation
* {doc}`../../foundations/concepts/probabilistic_regression` - Probabilistic regression concepts
* {doc}`../../tasks/capabilities` - Full capability manifest
* {doc}`../../citing` - Citation information
