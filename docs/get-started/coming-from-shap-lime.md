# Coming from SHAP or LIME

If you already explain models with SHAP or LIME, this page maps what you do
today to the CE calls. CE answers a different question: SHAP and LIME explain
the model's own output, while CE first calibrates that output on labelled
held-out data and then explains the calibrated output, with a range for every
weight. This is a difference in purpose, not a performance ranking; see the
{doc}`comparison of methods <../compare>`.

## The same steps, in CE

| What you do with SHAP or LIME | In CE | What is different |
|---|---|---|
| Create an explainer from the model and background data, for example `shap.Explainer(model, background)` | `WrapCalibratedExplainer(model)`, then `fit` and `calibrate(X_cal, y_cal, feature_names=...)` | The calibration set is **labelled held-out data** the model has not seen. It is not a background or reference distribution. |
| Compute attributions for some rows (`shap_values`, LIME's `explain_instance`) | `factual = explainer.explain_factual(X)` | Returns a `CalibratedExplanations` collection; `factual[0].get_rules()` gives each condition with `weight`, `weight_low` and `weight_high`. |
| A waterfall or bar plot | `factual.plot()` | Bars show weight **ranges**. Weights are not additive: they do not sum to the prediction. |
| A text summary of what pushes the output up or down | `factual.to_narrative(output_format="text")` | Conditions whose weight range crosses 0 are marked as direction uncertain. |
| `model.predict_proba(X)` | `explainer.predict_proba(X, uq_interval=True)` | Returns `(proba, (low, high))`: a calibrated probability and its lower and upper values. |
| No direct equivalent | `explainer.explore_alternatives(X)` | For each condition, the calibrated prediction if the feature had a value in another range. |

## Three things to unlearn

1. **Explanations do not add up.** A SHAP explanation decomposes the model
   output into additive contributions. A CE weight compares the calibrated
   prediction with predictions under other values of one feature, so the
   weights need not sum to anything. In the {doc}`CE by example <ce-by-example>`
   case the weights sum to −0.069, while the calibrated probability is
   0.286.
2. **You need labels for the calibration data.** SHAP's background data can
   be unlabelled. CE's calibration set must be labelled and kept away from
   training.
3. **A range is part of the answer.** If a weight range crosses 0, the
   direction of that condition is not settled; report it that way.

## Try it

The {doc}`Quickstart <quickstart>` runs the full CE workflow on one dataset
in about 10 minutes, and {doc}`../foundations/how-to/interpret_explanations`
explains every field and plot. What each range guarantees depends on the
task: see {doc}`Guarantees by mode <../foundations/concepts/calibrated_interval_semantics>`.
