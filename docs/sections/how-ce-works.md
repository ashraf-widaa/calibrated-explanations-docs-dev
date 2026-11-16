# How CE Works: The Theory Behind It

Explore the scientific foundations, statistical mechanisms and assumptions
behind calibrated explanations.

For guarantees, assumptions and non-guarantees, see
{doc}`../foundations/concepts/calibrated_interval_semantics`.

For short definitions of terms, see the {doc}`Scientific & Theoretical Glossary <../glossary/science>`.

## The chain to follow

Every CE output can be traced along one chain:

**task → CE mode → statistical method → output and what its range means →
assumptions and guarantees**.

{ref}`Which method CE uses for each task <ce-workflow-methods>` shows the chain
for the three modes in one table, and
{ref}`What the guarantees rest on <ce-workflow-guarantees>` separates the
assumptions from what they do and do not give you.

<span id="read-in-this-order"></span>

## From calibrated prediction to explanation

The {doc}`CE workflow <../foundations/concepts/ce_workflow>` traces how
calibrated outputs become the inputs to an explanation.

A factual explanation starts with the quantity being predicted, then compares
it with outputs obtained after substituting feature values. In the existing
binary example, the probability of benign is 0.286; a substituted scenario
gives 0.476, so the factual weight is 0.286 − 0.476 = −0.190. The
{ref}`worked construction <ce-workflow-explanations>` connects the rule,
substitutions, weight and alternative prediction. These comparisons describe
the model's responses, not causal effects.

The same distinction helps when
{doc}`reading explanation records and plots <../foundations/how-to/interpret_explanations>`:
a prediction and a feature weight are different quantities, even when both
are accompanied by a range.

<span id="pages-in-this-section"></span>

## Calibration methods and their limits

Venn–Abers predictors supply classification probability information, while
conformal predictive systems supply regression prediction information. The
{doc}`methods explanation <../foundations/concepts/calibration_methods>`
develops these constructions and their assumptions. The
{ref}`workflow's task-to-method comparison <ce-workflow-methods>` identifies
which output is being explained in each mode.

A range must be interpreted with its construction and assumptions. Prediction
bounds, target prediction intervals and explanation-weight ranges do not
share one guarantee. The
{ref}`calibration prerequisites <ce-workflow-guarantees>` and
{ref}`cross-mode non-guarantees <cross-mode-non-guarantees>` describe these
limits. The {doc}`foundations <../foundations/index>` supply prerequisite
concepts where needed.
