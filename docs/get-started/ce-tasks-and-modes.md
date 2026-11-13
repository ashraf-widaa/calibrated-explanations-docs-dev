# Tasks, modes and capabilities

**Path C, step 1.** Start here if you have a model or a prediction problem
and want to know whether and how CE applies. In three steps: check that CE
fits, pick the mode, and learn what its outputs mean. A reference of
capabilities and limitations follows at the end.

If terms such as *classification* or *calibration set* are new, start with
Path A: {doc}`ml-foundations` and {doc}`why-ce`.

## Choosing your workflow

### Step 1: check that CE fits

1. **Is it a supported task?** CE explains **supervised** models that predict
   a class or a number for one case at a time, from a fixed set of features.
   It is not designed for generative models, unsupervised learning or
   reinforcement learning.
2. **Is the model compatible?** A scikit-learn-style model with `predict`;
   classifiers must also provide `predict_proba` (without it, calibration
   fails with a `ConfigurationError`). The model may already be trained: CE
   detects a fitted model, and you can calibrate it directly.
3. **Do you have calibration data?** Labelled cases with the same features,
   held out from training.

### Step 2: pick the mode

The **mode** follows from what your model predicts and what you want to know
about it.

::::{grid} 1 1 3 3
:gutter: 3

:::{grid-item-card} Your model predicts a **class**
:link: quickstart_classification
:link-type: doc

**Classification** (binary or multiclass)

*How probable is each class?*

Call: `predict_proba` with `uq_interval`.

Calibrated with **Venn-Abers** predictors.
+++
Classification tutorial →
:::

:::{grid-item-card} Your model predicts a **number**, and you want a range
:link: quickstart_regression
:link-type: doc

**Interval regression**

*Where is the value likely to fall?*

Call: `predict` with `uq_interval`.

Calibrated with a **conformal predictive system** (CPS).
+++
Regression tutorial →
:::

:::{grid-item-card} Your model predicts a **number**, and you ask about a threshold
:link: quickstart_regression
:link-type: doc

**Probabilistic regression**

*How likely is the value to be at or below `t`?*

Call: `predict_proba` with `threshold` and `uq_interval`.

**CPS**, then **Venn-Abers**.
+++
Regression tutorial →
:::
::::

In every mode you then explain predictions with `explain_factual` and
`explore_alternatives`; adding `guarded_options` (see
{doc}`quickstart_guarded`) restricts explanations to typical feature values.
Probabilistic regression is not a separate kind of model: the model is the
same regression model, and only the question asked of its predictions changes
when you pass a `threshold`.

## What the outputs mean

:::{div} ce-table-compact
| Mode | Output | Read it as |
|---|---|---|
| Classification | Calibrated class probability with lower and upper probability | "Of the cases that get a model score like this one, about this share belong to the class" |
| Interval regression | Point prediction with a prediction interval (default 5th–95th percentile) | "The outcome is likely to fall in this range" |
| Probabilistic regression | Calibrated probability of `y ≤ t` with lower and upper probability | "The chance the outcome is at or below `t`" |
:::

- **Binary classification** has two classes. CE reports the calibrated
  probability of the positive class, which is class `1` in the label encoding.
- **Multiclass classification** has three or more classes. CE explains the
  predicted class by default; its bounds need care (limitation 1 below).

These three are the **semantic modes** of CE's documentation: a semantic mode
is *how to interpret an output*. It is not an API argument; you select it
through the model type and whether you pass a `threshold`.

### How the uncertainty differs between modes

The {ref}`three output types, side by side <ce-output-types>`, on the guarantees page show
one real example of each.

All three modes rely on one assumption, **exchangeability**: the calibration
data and the new cases come from the same process, and their order does not
matter. Independent samples from one stable population satisfy it; data from
before and after a change in practice may not.

- **Classification** uses Venn–Abers calibration. It calibrates the model's
  score twice, once assuming the new case belongs to the class and once
  assuming it does not. The two results are the lower and upper probability.
  Under exchangeability, the value that matches the case's true outcome is
  calibrated in the long run; because that outcome is unknown when you
  predict, CE reports both. The single probability CE reports merges the pair
  into one number between them; it is designed to stay close to calibrated
  but does not keep the exact guarantee. The bounds are **not** a
  conventional confidence interval for an unknown true probability.
- **Interval regression** uses conformal prediction, which turns the model's
  errors on the calibration set into intervals (CE uses conformal predictive
  systems). Under exchangeability, intervals contain the true value at the
  requested rate *on average over cases* (marginal coverage), not for every
  individual case. *Wording under review by the CE authors.*
- **Probabilistic regression** combines both: a conformal predictive
  distribution gives the event probability, and Venn–Abers calibrates it.

Go deeper: {doc}`../foundations/concepts/calibration_methods` shows how
Venn–Abers and conformal predictive systems work, with worked examples.

### What explanations mean in every mode

Explanations sit on top of the calibrated output:

- A **factual explanation** lists conditions that hold for the case and the
  estimated contribution of each to the calibrated output, with an interval.
- An **alternative explanation** shows what the calibrated output would be if
  one feature were in a different range.
- A **guarded explanation** applies the same ideas but removes candidate
  feature values that look out of distribution relative to the calibration
  data.

Explanations describe the model's behaviour. They are not causal claims about
the world, and acting on an alternative does not guarantee a different real
outcome. The canonical statement of guarantees and non-guarantees for each
mode is {doc}`../foundations/concepts/calibrated_interval_semantics`.

## Four terms that are easy to mix up

:::{div} ce-table-compact
| Term | Means | Examples | How you choose it |
|---|---|---|---|
| **Prediction task** | What the model predicts | Classification (a class), regression (a number) | Your problem and your model |
| **CE mode** | Which question CE answers about the prediction, and so how to read the output | Classification; interval regression; probabilistic regression | The model type, and whether you pass a `threshold` |
| **Calibration method** | The statistical procedure CE uses to calibrate the output | Venn-Abers predictors; conformal predictive systems (CPS); CPS followed by Venn-Abers | Set by the mode, not chosen separately |
| **Explanation configuration** | How explanations are produced or constrained | Factual or alternative explanations; guarded explanations; conjunctions; excluded features | Arguments to the explanation calls |
:::

Guarded explanations, for example, are an explanation configuration available
in every mode; they are not a third kind of prediction task.

**Continue**

- **Next:** {doc}`apply-overview` (Path C, step 2): the practical workflow,
  step by step, without code.
- **Go deeper:** {doc}`How CE calibrates <../foundations/concepts/calibration_methods>`
  (section 4, the three modes) and the guarantees by mode in
  {doc}`../foundations/concepts/calibrated_interval_semantics`.
- **See also:** the executable {doc}`Python tutorials <../tutorials/index>`
  for each mode, and the {doc}`Quick API <quick_api>` for the calls named on
  this page.
- **Before this:** {doc}`CE by example <ce-by-example>` (Path B) and
  {doc}`why-ce` (Path A).

## Capability reference

This table is for looking things up, not for reading straight through. Each
row is something CE can do; each column is a task or mode; each cell records
what was checked for CE 1.1.0-dev by running the call on a fresh explainer
with public datasets. "Runs" means the call completes and returns the
documented object type; it is not a statistical validation.

Columns: binary and multiclass classification; interval and probabilistic
regression.

:::{div} ce-table-compact
| Capability | Binary | Multi­class | Interval | Proba­bilistic |
|---|---|---|---|---|
| Calibrated prediction with interval | Runs | Runs, see limitation 1 | Runs | Runs |
| Factual explanations | Runs | Runs (predicted class) | Runs | Runs |
| Alternative explanations | Runs | Runs | Runs | Runs |
| Conjunctive rules (`add_conjunctions`) | Runs | Runs | Runs | Runs |
| Excluding features (`features_to_ignore`) | Runs | Runs | Runs | Runs |
| Plots (`plot`) | Runs | Runs | Runs | Runs |
| Guarded explanations (`guarded_options`) | Runs | Runs | Runs | Runs |
| All-class explanations (`multi_labels_enabled`) | n/a | Experimental | n/a | n/a |
| JSON export (`to_json`) | Runs | Runs | Runs | Runs |
:::

Go deeper: {doc}`../foundations/how-to/interpret_explanations`,
{doc}`../foundations/concepts/alternatives` and
{doc}`../foundations/concepts/guarded_explanations`.

### Limitations that affect how you read outputs

1. **Multiclass bounds are rescaled by default and are then not
   probabilities.** For a multiclass model, CE calibrates each class against
   all the others, which gives each class its own Venn–Abers pair with the
   same meaning as in binary classification. By default CE then divides every
   class's probability *and* its bounds by the sum of the class probabilities,
   so that the probabilities add up to 1. The rescaled bounds no longer carry
   the Venn–Abers meaning, and an upper bound can exceed 1. Use them only to
   compare uncertainty between classes. If you need per-class bounds that keep
   their Venn–Abers meaning, pass `normalization="simplex"` to `predict_proba`:
   the bounds stay as calibrated, and only the class probabilities are scaled
   to add up to 1, so a probability may then fall slightly outside its own
   bounds.
2. **All-class explanations are experimental.** By default a multiclass
   explanation explains the predicted class only; `multi_labels_enabled=True`
   is not part of the stable interface.
3. **Probabilistic regression splits the calibration set.** CE uses part of
   the calibration data to compute threshold probabilities and the rest to
   calibrate them, so each part is smaller and the bounds can be wider than
   with the same data in classification.

Operational issues, such as errors from specific call orders, are listed in
{doc}`troubleshooting`.

Entry-point tier: Tier 1.
