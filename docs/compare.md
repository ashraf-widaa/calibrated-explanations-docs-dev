# Calibrated Explanations comparisons (CE-first)

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

Entry-point tier: Tier 3.
