# How CE Works: The Theory Behind It

Explore the scientific foundations, statistical mechanisms and assumptions
behind calibrated explanations. The pages follow one chain, from the
workflow through calibration by task, then factual and alternative
explanations, and finally the assumptions and guarantees behind their
outputs. Readers new to the vocabulary can start
with the {doc}`Essential Foundations <../foundations/index>` or the
{doc}`Scientific & Theoretical Glossary <../glossary/science>`.

## The chain to follow

Every CE output can be traced along one chain:

**task → CE mode → statistical method → output and what its range means →
assumptions and guarantees**.

{ref}`Which method CE uses for each task <ce-workflow-methods>` shows the chain
for the three modes in one table, and
{ref}`What the guarantees rest on <ce-workflow-guarantees>` separates the
assumptions from what they do and do not give you.

<span id="pages-in-this-section"></span>
<span id="read-in-this-order"></span>

## Calibration methods and their limits

Venn–Abers predictors supply classification probability information, while
conformal predictive systems supply regression prediction information. The
{doc}`methods explanation <../foundations/concepts/calibration_methods>`
develops these constructions and their assumptions. The
{ref}`workflow's task-to-method comparison <ce-workflow-methods>` identifies
which output is being explained in each mode.

## From calibrated prediction to explanation

The {doc}`CE workflow <../foundations/concepts/ce_workflow>` traces how
calibrated outputs become the inputs to an explanation. In its binary
example, the original probability of benign is 0.286 and a substituted
scenario gives 0.476. The factual weight is the difference, −0.190. The
{ref}`worked construction <ce-workflow-explanations>` connects the rule,
substitutions, weight and alternative prediction.

When {doc}`reading explanation records and plots <../foundations/how-to/interpret_explanations>`,
read the prediction and the feature weight as separate quantities, each with
its own range.

## Assumptions and guarantees

A range must be interpreted with its construction and assumptions. Prediction
bounds, target prediction intervals and explanation-weight ranges do not
share one guarantee. The
{ref}`calibration prerequisites <ce-workflow-guarantees>` and
{ref}`cross-mode non-guarantees <cross-mode-non-guarantees>` describe these
limits.

## Pages in this section

Read them in this order:

1. {doc}`The CE workflow <../foundations/concepts/ce_workflow>`: train,
   calibrate, explain; how a calibrated prediction becomes the input of an
   explanation, with one worked construction.
2. {doc}`Calibration by task <../foundations/concepts/calibration_methods>`:
   Venn–Abers predictors for classification and conformal predictive
   systems for regression, with the formal statements.
3. Factual and alternative explanations: the
   {ref}`worked construction in the workflow <ce-workflow-explanations>`
   builds a factual weight step by step, and
   {doc}`Alternative explanations <../foundations/concepts/alternatives>`
   covers the "what if" rules and ensured filters.
4. {doc}`Guarantees by mode <../foundations/concepts/calibrated_interval_semantics>`:
   interval semantics, assumptions, guarantees and non-guarantees, including
   the {ref}`open questions for the CE authors <open-author-questions>`.
5. {doc}`Essential foundations <../foundations/index>`: further concept
   pages on guarded explanations, probabilistic regression and explanation
   structures.

Related pages in other sections: the task each mode serves is chosen in
{doc}`Tasks, modes and capabilities <../get-started/ce-tasks-and-modes>`
(*CE: What & Why*); reading records and plots is taught in
{doc}`How to read CE explanations <../foundations/how-to/interpret_explanations>`
(step 3 of the learning journey in {doc}`Get started <../get-started/index>`).

**Next section:** {doc}`CE in Practice <in-practice>`.

```{toctree}
:hidden:
:maxdepth: 2

The CE Workflow <../foundations/concepts/ce_workflow>
Calibration by Task <../foundations/concepts/calibration_methods>
Alternative Explanations <../foundations/concepts/alternatives>
Guarantees by Mode <../foundations/concepts/calibrated_interval_semantics>
Essential Foundations <../foundations/index>
```
