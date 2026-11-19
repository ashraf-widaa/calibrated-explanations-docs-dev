---
sidebarclass: how-to
---

# Interpret calibrated explanations

Use this guide after generating explanations: identify the quantity being
explained, read the conditions and weights, then inspect the public rule
payloads and plots. For how the substituted predictions are constructed,
read {doc}`../concepts/ce_workflow`; the mode-specific range meanings are in
{doc}`../concepts/calibrated_interval_semantics`.

```{raw} html
<nav class="ce-journey" aria-label="Get started, step 4 of 5"><ol><li><a href="../../what-is-ce.html"><span class="ce-journey-n">1</span>What CE is</a></li><li><a href="../../get-started/try-in-browser.html"><span class="ce-journey-n">2</span>Quick Start</a></li><li><a href="../../get-started/installation.html"><span class="ce-journey-n">3</span>Install</a></li><li aria-current="step"><a href="interpret_explanations.html"><span class="ce-journey-n">4</span>Read it</a></li><li><a href="../../get-started/apply-to-your-data.html"><span class="ce-journey-n">5</span>Your data</a></li></ol></nav>
```

**Get started, step 4 of 5 · about 15 minutes.** Coming from the
{doc}`Quick Start <../../get-started/try-in-browser>`,
{doc}`Your First CE Explanation in Python <../../get-started/first-explanation-python>`, the
{doc}`Python quickstart <../../get-started/quickstart>` or the in-depth
{doc}`Python walkthrough <../../get-started/quickstart_walkthrough>`, use this
page to read the records and plots you produced there. The examples are
classification; regression outputs are covered in
{ref}`a section of their own <interpret-regression-outputs>`. The next step is
{doc}`../../get-started/apply-to-your-data`.

```{admonition} Terminology
:class: tip

- **Factual explanation** – per the original CE classification and regression
  papers, this pairs the calibrated prediction and its uncertainty interval with
  factual feature rules. Every rule binds the observed feature value to a
  condition and surfaces the calibrated feature weight plus its uncertainty
  interval.
- **Alternative explanation** – proposes changes to feature values that would
  produce a different calibrated outcome. Each rule couples the alternative
  condition with the calibrated prediction estimate and uncertainty interval for
  that scenario.
- **Rule** – a feature-level contribution (weight + condition) inside each
  factual explanation and a prediction + condition pair inside each alternative
  explanation. Metadata retains the complementary quantities for ranking and
  provenance.
- More terms: {doc}`Glossary <../../glossary/index>`.
```

## Factual and alternative explanations at a glance

Factual and alternative explanations are two **explanation types**, not
calibration modes: both can be produced in every mode (classification,
interval regression, probabilistic regression). A factual explanation describes
the case as it is; an alternative explanation describes how the calibrated
prediction would respond if one feature had a value in another range. The
figure shows both for one case.

```{raw} html
<figure class="ce-figure ce-figure--compact">
  <a href="../../_static/figures/ce-reading-an-output.svg" title="Open the figure at full size">
    <img src="../../_static/figures/ce-reading-an-output.svg" width="480" height="572" alt="Three panels. 1, calibrated prediction: the calibrated probability of benign is 0.29, with a range from 0.17 to 0.33, all below 0.5, so the label is malignant. 2, factual rule worst concave points greater than 0.14: weight minus 0.19, with a range from minus 0.31 to minus 0.05, all below 0, so this condition lowers the probability of benign. 3, alternative worst concave points below 0.14: the calibrated probability of benign would be 0.48, with a range from 0.33 to 0.60, instead of 0.29 now; this describes how the model would respond, not a recommended action.">
  </a>
  <figcaption>CE output for case 2 of the Python walkthrough: the calibrated prediction (1), one factual rule with its weight and range (2), and one alternative with the calibrated prediction it would give (3). Panel 3 describes the model's response, not a recommended action.</figcaption>
</figure>
```

Read the panels from top to bottom. Panel 1 places the probability of
*benign* on a 0-to-1 scale; its estimate and range are below the 0.5 label
boundary. Panel 2 switches to a weight scale centered on zero: the negative
weight and range describe a condition associated with a lower model
probability of *benign*. Panel 3 returns to the probability scale for the
opposite feature condition. Its range crosses 0.5 even though its estimate
does not. This compares model responses, without establishing a causal
effect or recommending an intervention.

The collections below make these prediction, rule and alternative values
available for inspection in Python.

## 1. Start with the explanation collections

Calibrated explanations return collections (`CalibratedExplanations`, `AlternativeExplanations`) that behave like sequences. The first step is to look at the summary for each item:

The code fragments below assume an `explainer` that is already fitted and
calibrated, and a query matrix `x_test`. For a complete setup, run the
{doc}`Quick API example <../../get-started/quick_api>` and use its `X_test`
as `x_test` here.

```python
factual_batch = explainer.explain_factual(x_test[:1])
factual = factual_batch[0]
alternative_batch = explainer.explore_alternatives(x_test[:1])
alternative = alternative_batch[0]

print(f"Mode: {factual.get_mode()}  Calibrated prediction: {factual.predict:.3f}")
print(f"Mode: {alternative.get_mode()}  Calibrated prediction: {alternative.predict:.3f}")
```

Key attributes shared by both explanation types:

| Attribute | Description |
| --------- | ----------- |
| `predict` | Calibrated probability (classification) or numeric estimate (regression). |
| `prediction_interval` | Tuple of `(low, high)` from the explanation's prediction record; its meaning depends on the mode. |
| `get_rules()` | Rule dictionary with aligned lists such as `rule`, `weight` and `predict`; not a list of rule objects. |


## 2. Examine the rule tables in detail

Rules describe the calibrated model's response in terms of feature conditions.
Use the helper payloads to inspect them in a structured way; a rule is not an
instruction to change a real-world feature.

### 2.1 Factual explanations

```python
factual_payload = factual.build_rules_payload()
factual_core = factual_payload["core"]
for rule in factual_core["feature_rules"]:
    interval = rule["weight"]["uncertainty_interval"]
    print(
        f"{rule['condition']['feature']:>20} "
        f"| condition={rule['condition']['operator']} {rule['condition']['value']} "
        f"| weight={rule['weight']['value']:+.3f} "
        f"| weight interval=({interval['lower']:.3f}, {interval['upper']:.3f})"
    )

# the metadata block preserves the detailed calibration artefacts
factual_metadata = factual_payload["metadata"]["feature_rules"]
for extra in factual_metadata:
    print(f"  repr={extra['weight_uncertainty']['representation']}")
```

The `build_rules_payload` result is a dictionary with two top-level keys:

- `core` contains the calibrated prediction (`core["prediction"]`) and the factual feature rules (`core["feature_rules"]`).
- `metadata` exposes the full uncertainty records and any derived artefacts (such as the baseline prediction) so downstream consumers can distinguish provenance data from the explanation itself.

Use the factual core for weight intervals and the alternative core for scenario
prediction intervals. In the worked case, factual metadata's
`prediction_uncertainty` records the original prediction's range, not the
substituted scenario's range. Do not use it to reconstruct a weight interval.

Read the factual core from top to bottom:

1. **Weight sign and units** – first identify the output being explained. For the binary example it is `P(benign)`; a positive factual weight means the current condition raises that output relative to the substituted values, and a negative weight means it lowers it. For interval regression, weights are in target units; for probabilistic regression, they are in event-probability units. In multiclass explanations, identify the class being explained before interpreting a sign.
2. **Condition** – confirms the feature value observed in the instance (for example, `glucose >= 140`). Use this to cross-check domain constraints.
3. **Prediction** – available through the metadata, showing the calibrated contribution when the feature is perturbed; compare it to `predict` to understand marginal impact.
4. **Weight interval** – the core payload keeps only the numeric bounds; consult the metadata if you need the representation (percentile vs. probabilistic) or raw percentiles used to derive them.

### 2.2 Alternative explanations

Alternative explanations add scenario guidance on top of feature contributions. The payload uses the same helper:

```python
alternative_payload = alternative.build_rules_payload()
alternative_core = alternative_payload["core"]
for rule in alternative_core["feature_rules"]:
    interval = rule["prediction"]["uncertainty_interval"]
    print(
        f"{rule['condition']['feature']:>20} "
        f"| new condition={rule['condition']['operator']} {rule['condition']['value']} "
        f"| predicted value={rule['prediction']['value']:+.3f} "
        f"| interval=({interval['lower']:.3f}, {interval['upper']:.3f})"
    )

alternative_metadata = alternative_payload["metadata"]["feature_rules"]
for extra in alternative_metadata:
    print(
        f"  Δ prediction={extra['weight_value']:+.3f} "
        f"(repr={extra['weight_uncertainty']['representation']})"
    )
```

- `core["feature_rules"]` lists the alternative feature conditions alongside the calibrated prediction estimate and uncertainty interval for each alternative scenario.
- `metadata["feature_rules"]` retains the richer calibration context: the difference from the factual baseline (`weight_value`), the detailed uncertainty metadata, and the alternative value used to create the scenario.

Compare the alternative prediction with the current one, and inspect its range.
A large change in model output is not evidence that a real-world action is
feasible, beneficial or causal. Alternatives describe how the model's calibrated
output responds to a different feature range; changing a feature in the real
world need not change the outcome.
## 3. Connect explanations to plots

PlotSpec plots visualise the same rule rankings and uncertainty intervals:

```python
fig = factual.plot(uncertainty=True, filter_top=6)
try:
    from matplotlib import pyplot as plt

    plt.close(fig)
except Exception:
    pass
```

Interpret the chart as follows:

1. **Weight range.** With `uncertainty=True`, each bar spans the rule's
   lower and upper weight values. Its length is not the absolute point weight;
   read that estimate from the rule table. A range crossing zero does not
   establish a direction, and excluding zero is not a statistical significance test.
2. **Colour** indicates direction. With the default plot style, classification and
   probabilistic-regression plots draw contributions that raise the prediction in red
   and those that lower it in blue; plain regression plots swap the two (raise in blue,
   lower in red). The colours come from the plot style configuration and can be changed.
3. **Dark and light portions.** In the default factual uncertainty plot,
   the dark portion runs from zero to the range endpoint nearest zero. The
   remaining range is light; a range crossing zero has no dark portion.
   The grey band behind the rules redraws the original prediction range on
   the weight scale; it is not a confidence region for the feature weights.
4. **Prediction panel.** The vertical marker is the point estimate; the
   reported lower and upper values determine the dark/light probability bar.
   Interval-regression headers instead show the numeric estimate and target
   interval. These prediction quantities have different qualifications from
   the derived weight ranges; see {doc}`../concepts/calibrated_interval_semantics`.

When reviewing alternative explanations, use `plot(style="alternative")` (or open the alternative tab in interactive renderers) to see how the suggested feature changes alter the bars and the calibrated outcome.

If the plot does not match the table, check the selected instance, output class,
ranking and plotting options. Record the CE version and a reproducing example
before reporting a mismatch.

(interpret-regression-outputs)=

## 4. Regression outputs

For **interval regression without a threshold**, `prediction_interval` is a
target prediction interval produced by a **conformal predictive system (CPS)**;
`low_high_percentiles` selects its percentiles. With a threshold, the explained
quantity is an event probability and its bounds, as described below.

For regression with a scalar `threshold` `t`, the `predict` value is the calibrated event probability `P(y <= t)`; with a `(low, high)` threshold it is the probability that the outcome lies within those bounds. The interval gives the lower and upper calibrated probability for that event. See {doc}`../concepts/calibrated_interval_semantics` (Mode 3).

<span id="provenance-and-telemetry"></span>

## 5. Structured payloads, provenance and telemetry

For pipelines and audits, two more methods return the same explanation as
data:

| Method | Returns |
|---|---|
| `build_rules_payload()` | Structured `core` and `metadata` dictionaries; `core["feature_rules"]` is a list of rule records. |
| `to_telemetry()` | Explanation uncertainty and rule metadata; runtime provenance is documented separately in {doc}`configure_telemetry`. |

Reading an explanation does not require telemetry. When you need to record
which calibration and plotting components produced an explanation (for audits
or for comparing environments), see {doc}`configure_telemetry`.

## 6. Validate in notebooks and downstream systems

After you absorb the tables and plots:

1. Run the [demo notebooks](https://github.com/Moffran/calibrated_explanations/tree/main/notebooks) (`advanced/demo_under_the_hood.ipynb` and the classification and regression demos in `core_demos/`) and compare their outputs with your own environment.
2. Embed the interpretation checks into dashboards—surface calibrated prediction vs. interval charts and highlight scenarios with wide rule uncertainty.
3. Share this guide with auditors and stakeholders so everyone relies on the same vocabulary when discussing factual or alternative explanations.

Keeping the interpretation workflow front and centre helps people read calibrated explanations consistently. It does not by itself make a decision safe: the guarantees and their limits are in {doc}`../concepts/calibrated_interval_semantics`.

(next-in-the-learning-journey)=
## Next in Get started

**Step 5 of 5:** {doc}`../../get-started/apply-to-your-data` applies the same
calls to your own model and data.
