# CE compared with SHAP, LIME, counterfactuals and conformal prediction

<span id="calibrated-explanations-comparisons-ce-first"></span>

## Which method answers your question?

:::{div} ce-table-compact
| If you need… | Use | Why |
|---|---|---|
| Which features drive the model's own output, as contributions that add up | SHAP | Attributions sum to the model output minus a baseline |
| A quick local approximation around one case | LIME | Fits a simple surrogate model to perturbed samples near the case |
| A calibrated probability or value with bounds, and the feature conditions behind it, each with a range | CE factual explanations | Calibrates on labelled held-out data first, then explains the calibrated output |
| What the calibrated prediction would be if a feature were in another range | CE alternative explanations | Rule-based alternatives, each with its calibrated prediction and range |
| The smallest concrete change that would flip a decision | Counterfactual methods | Search for a nearby case with a different outcome |
| A set or interval of plausible outcomes with a coverage statement, without an explanation | Conformal prediction | Prediction sets or intervals under exchangeability |
:::

## Side by side

:::{div} ce-table-compact
| | SHAP | LIME | Counterfactual methods | CE |
|---|---|---|---|---|
| Explains | The model's own output | The model's own output, through a local surrogate | The decision boundary | The **calibrated** output |
| Needs | Background or reference data | Perturbation settings | A search space and constraints | A **labelled** calibration set the model has not seen |
| Unit of explanation | Feature attribution | Surrogate coefficient | A changed case | A feature **condition** (rule) with a weight |
| Range per feature | Not in the standard method | Not in the standard method | Not in the standard method | A range for every weight |
| Adds up to the prediction | Yes | Approximately, within the surrogate | Not applicable | No |
| "What if" | No | No | Yes, optimised for a small change | Yes, rule-based; not optimised and not a recommended action |
| Causal | No | No | No | No |
:::

The SHAP, LIME and counterfactual columns describe the standard form of each
method; variants exist, and this wording is part of the comparison that
remains under CE author review (SR-06). The table describes purposes and
outputs, not a performance ranking. Coming from SHAP or LIME? See
{doc}`get-started/coming-from-shap-lime`.

## Summary of purposes

Choose an explanation method by the question you need it to answer.
CE explains a calibrated output and attaches ranges to its rules; this differs
from explaining the original model score or returning a prediction set alone.
The comparison below describes those purposes, not a performance ranking.

:::{div} ce-table-compact
| Approach | Main question | Output and calibration | What to check |
|---|---|---|---|
| SHAP or LIME | Which features contribute to the model output being explained? | Feature attributions; calibrating that model output is a separate step | Which output and reference/background the explanation uses |
| Conformal prediction methods | Which target values or labels form a prediction set? | Sets or intervals with method-specific coverage statements | Calibration protocol, exchangeability, and the scope of coverage |
| CE | What does the calibrated model predict, which feature conditions contribute, and how would other feature ranges change it? | A calibrated prediction, factual weights, and alternative predictions, with ranges | Held-out calibration data; mode-specific output meanings; explanation-range limitations |
:::

CE classification uses Venn–Abers predictors; numeric prediction intervals
use conformal predictive systems. Probabilistic regression combines CPS scores
with Venn–Abers. The {doc}`methods reference <foundations/concepts/calibration_methods>`
explains these constructions without treating their guarantees as interchangeable.

Ranges on CE feature weights do not establish causal effects or formal
per-feature coverage. The earlier comparative rule-stability claim remains an
author-review question (SR-06); no general stability advantage is asserted here.
For guarantees and open qualifications, see
{doc}`foundations/concepts/calibrated_interval_semantics`.

For an example, read {doc}`get-started/ce-by-example`. Method papers and CE
evaluations are listed in {doc}`citing`; assess performance on your own
held-out data using {doc}`practitioner/evaluate_ce`.
