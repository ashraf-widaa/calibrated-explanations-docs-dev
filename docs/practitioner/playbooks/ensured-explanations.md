# Ensured Explanations Playbook

Ensured explanations filter existing alternatives by comparing their reported
interval widths with the original prediction's width. This is a way to inspect
model-response scenarios, not a guarantee about an intervention.

> **Audience:** Practitioner

```{admonition} Guarantees & Assumptions
:class: important

- Ensured explanations are a *filtering and ranking framework* over existing
    alternative rules.
- The implementation retains alternatives whose reported uncertainty interval
    is **no wider** than the base prediction interval.
- The calibration guarantees behind uncertainty intervals require that the
    calibration set and your deployment queries are exchangeable / distribution
    matched. The alternative distribution-match wording and exact validity
    statements remain under author review; see
    {doc}`../../foundations/concepts/calibrated_interval_semantics`.
```

## What are Ensured Explanations?

An alternative reports the calibrated model's prediction for another feature
range. Its interval can be wider or narrower than the current prediction's
interval. The ensured filter compares these widths; ranking controls can then
order the retained scenarios. Neither step establishes a better real-world
decision.

## When to Use

Use the filter when you want to compare alternative model outputs while
excluding scenarios with wider reported intervals. Record the task, explained
class or threshold, and filtering options so that the comparison is meaningful.

## Understanding Epistemic vs Aleatoric Uncertainty

Whether CE's reported ranges should be interpreted as epistemic or aleatoric
uncertainty remains under review by the CE authors (SR-07). This guide describes
the observable width comparison and does not claim that the filter measures or
reduces a separately identified uncertainty component.

## Usage Pattern

### Core filtering API

The ensured framework is exposed directly on the alternative explanation objects.

```python
alternatives = explainer.explore_alternatives(x_test)
alt0 = alternatives[0]

# Ensured: alternatives with intervals no wider than the base prediction's
ensured = alt0.ensured_explanations()

# Super: alternatives reinforcing the base prediction
super_alts = alt0.super_explanations()

# Semi/Counter: alternatives opposing the prediction
semi_alts = alt0.semi_explanations()
counter_alts = alt0.counter_explanations()

# Pareto: output-envelope frontier over (output, uncertainty width)
pareto_alts = alt0.pareto_explanations()

# Pareto: prefer fewer changed features (effective with conjunctions)
pareto_simple = alt0.pareto_explanations(pareto_cost="rule_size")

# Combine: ensured super-explanations
ensured_super = alt0.super_explanations(only_ensured=True)
```

### Ranking controls (rnk_metric / rnk_weight / filter_top)

Triangular plots are commonly used together with ensured ranking:

```python
# Use ensured-style triangular view (alias for style="triangular")
alt0.plot(
    style="ensured",
    rnk_metric="ensured",
    rnk_weight=0.7,
    filter_top=10,
    show=False,
)
```

Notes:

- ``rnk_metric="ensured"`` combines output and uncertainty interval width.
- ``rnk_weight`` shifts the trade-off between output and uncertainty.
- Use ``show=False`` in headless environments.

## Setting Uncertainty Thresholds

The ensured filter uses a relative comparison with the base interval; it is
not an application-specific safety threshold. There is no validated universal
width cutoff for medical, financial or other decisions in this guide. Numeric
regression widths are in target units, while classification and threshold-event
widths are in probability units; do not compare them as if they shared a scale.

## Best Practices

### 1. Document Your Confidence Criteria

Record the base prediction, its interval, the query, the CE version and the
arguments passed to `ensured_explanations`. The core filtering examples above
assume an already fitted and calibrated `explainer`; use the
{doc}`Quick API <../../get-started/quick_api>` for a complete setup.

### 2. Report Both Ensured and All Alternatives

```python
all_alternatives = alternatives[0]
ensured_alternatives = all_alternatives.ensured_explanations()

print(f"Total alternatives: {len(all_alternatives)}")
print(f"Ensured alternatives: {len(ensured_alternatives)}")
if len(all_alternatives):
    print(f"Ensured ratio: {len(ensured_alternatives)/len(all_alternatives):.1%}")
```

### 3. Consider Augmenting Calibration Data

If scenarios of interest have wide intervals, investigate the data and
calibration protocol. More data or subgroup calibration may be relevant, but
neither is a guaranteed remedy. Evaluate any change on held-out data and record
the assumptions; see {doc}`../evaluate_ce`.

## Interpreting Ensured Results

| Outcome | What it establishes | What it does not establish |
| :--- | :--- | :--- |
| Many retained alternatives | Many scenarios passed the width comparison | Good coverage or permission to act |
| Few retained alternatives | Few scenarios passed the width comparison | A diagnosis of sparse data |
| No retained alternatives | No candidate passed with the chosen options | That the case is necessarily novel |

## Research Background

This capability is documented in:

> Löfström, H., Löfström, T., and Hallberg Szabadvary, J. (2024).
> [Ensured: Explanations for Decreasing the Epistemic Uncertainty in Predictions](https://arxiv.org/abs/2410.05479).
> arXiv preprint arXiv:2410.05479.

## Cross-References

* {doc}`../../tasks/capabilities` - Full capability manifest
* {doc}`../../foundations/concepts/alternatives` - Alternative explanations concept
* {doc}`decision-policies` - Decision policy patterns using uncertainty
* {doc}`../../citing` - Citation information

## Regression support notes

Ensured explanations support:

- **Classification** (binary/multiclass) via calibrated probabilities.
- **Probabilistic regression** via calibrated probabilities for events like
    $\Pr(y \le t)$ (pass ``threshold=...`` to ``explore_alternatives``).
- **Plain regression** (numeric outputs):

    - ``super_explanations`` keeps higher predicted outputs than the base.
    - ``semi_explanations`` and ``counter_explanations`` keep lower predicted
        outputs than the base.
    - ``ensured_explanations`` and ``pareto_explanations`` work the same way as
        in classification, filtering by uncertainty interval width and trade-offs.

Use the global plot to sanity-check calibration and uncertainty behaviour over
a dataset:

```python
explainer.plot(x_test, y_test, show=False)
explainer.plot(x_test, y_test, threshold=150.0, show=False)
```
