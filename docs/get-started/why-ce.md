# Why CE: from a conventional to a CE workflow

**Path A, step 2.** This page answers one question: *why is CE needed, and
how does a CE workflow differ from a conventional one?* It needs no code. If
terms such as *feature*, *label* or *test set* are new, read
{doc}`ml-foundations` first.

## What a conventional workflow leaves open

In a conventional supervised workflow you split labelled data into a
training set and a test set, train a model, let it predict, and measure on the
test set how often it is right. That tells you how good the model is **on
average**. When someone has to act on **one** prediction, three questions
remain open:

- **Is the score a real probability?** Many models produce scores that look
  like probabilities but are not calibrated: among cases scored 0.9, far
  more or far fewer than 90% may turn out positive.
- **How certain is this prediction?** A single number hides how well the data
  support it.
- **Why this prediction, and how firm is that reason?** Explanation tools
  usually explain the model's raw output and give one number per feature,
  without saying how certain that number is.

## The CE workflow

```{raw} html
<figure class="ce-figure">
  <a href="../_static/figures/ce-in-ml-workflow.svg" title="Open the figure at full size">
    <picture>
      <source media="(max-width: 600px)" srcset="../_static/figures/ce-in-ml-workflow-narrow.svg">
      <img src="../_static/figures/ce-in-ml-workflow.svg" width="1000" height="540" alt="In blue, a conventional workflow: labelled data is split into training and test sets, a model is trained (or an existing one is used), it predicts a label or a raw score, and it is evaluated on the test set. In orange, what CE adds: a calibration set held out from training, a Calibrate step (Venn-Abers predictors or conformal predictive systems) and an Explain step (factual and alternative explanations). CE returns a calibrated prediction with a lower and upper value and an explanation whose rules and weights each have a range; both are evaluated and interpreted on the test set.">
    </picture>
  </a>
  <figcaption>The conventional workflow (blue) and what CE adds (orange).</figcaption>
</figure>
```

What changes:

1. **A third data set.** Part of the labelled data becomes a *calibration
   set*. The model never trains on it, so CE can see how the model behaves
   on cases it has not seen.
2. **CE wraps the trained model.** CE does not replace training. You can train
   the model through CE or wrap a model you have already trained; the model
   itself is not changed.
3. **Calibrated outputs with ranges.** Every prediction comes back calibrated,
   with a lower and an upper value.
4. **Explanations from the calibrated output.** CE explains a prediction by
   asking the calibrated model again with one feature changed at a time, so
   every explanation inherits the calibration and has its own range.

## What CE gives you: one example

A model flags breast-tumour samples as *malignant* or *benign* from 30
measurements of cell nuclei. (This is an educational example on a public
dataset, not clinical decision support.) For one sample, here is what the
model alone gives, and what CE adds. Path B, {doc}`CE by example <ce-by-example>`,
follows this case step by step without code; the
{doc}`Python walkthrough <quickstart_walkthrough>` produces the same numbers with code.

| Question | The model alone | With CE |
|---|---|---|
| What is predicted? | *malignant* | *malignant*, with a calibrated probability of *benign* of 0.29, between 0.17 and 0.33 |
| Why? | — | The strongest reason is `worst concave points > 0.14`: with typical values below 0.14 instead, the calibrated probability of *benign* would be about 0.19 higher |
| What would change it? | — | If `worst concave points` were below 0.14, the calibrated probability of *benign* would be about 0.48 |

The figure shows how to read the three parts:

```{raw} html
<figure class="ce-figure ce-figure--compact">
  <a href="../_static/figures/ce-reading-an-output.svg" title="Open the figure at full size">
    <img src="../_static/figures/ce-reading-an-output.svg" width="480" height="572" alt="Three panels. 1, calibrated prediction: the calibrated probability of benign is 0.29, with a range from 0.17 to 0.33, all below 0.5, so the label is malignant. 2, factual rule worst concave points greater than 0.14: weight minus 0.19, with a range from minus 0.31 to minus 0.05, all below 0, so this condition lowers the probability of benign. 3, alternative worst concave points below 0.14: the calibrated probability of benign would be 0.48, with a range from 0.33 to 0.60, instead of 0.29 now; this describes how the model would respond, not a recommended action.">
  </a>
  <figcaption>Reading a CE output for the example case: the prediction, one factual rule and one alternative, each with its range.</figcaption>
</figure>
```

## The four ideas behind it

- **Calibration.** A probability is calibrated if, among cases given about
  70%, about 70% turn out positive. CE calibrates with Venn-Abers predictors
  for classification and conformal predictive systems for regression.
- **Range (uncertainty).** The lower and upper value around a prediction
  (panel 1). It shows how firmly the calibration data support that
  prediction. It is a statement about many cases, not a promise about one
  case, and its exact meaning depends on the task.
- **Factual explanation.** For each feature, a rule that holds for the case and
  a weight: how much the calibrated prediction would differ with typical
  values from the other side of the condition, with a range (panel 2). A
  range that includes 0 means the direction is not firmly supported.
- **Alternative explanation.** What the calibrated prediction would be if one
  feature had a value in a different range (panel 3).

## What CE needs from you

| Requirement | Details |
|---|---|
| A supervised task | Classification (a class) or regression (a number), one prediction per case |
| A compatible model | A scikit-learn-style model with `predict`; classifiers must also provide `predict_proba` (without it, calibration fails) |
| Labelled calibration data | Cases with known outcomes that the model was **not** trained on, with the same features |
| The same features for new cases | New cases must be described exactly like the training and calibration data |
| Some extra computation | An explanation asks the calibrated model for many extra predictions per explained case |

Each data set has one job. The **training set** fits the model. The
**calibration set** lets CE measure how the model's outputs relate to real
outcomes; calibrating on training data makes the model look more reliable
than it is. The **test set** checks the model and CE's outputs on untouched
cases; using it for training or calibration gives over-optimistic results.
Any information from the calibration or test data that reaches training, for
example scaling statistics computed on all the data, is **data leakage**:
split first, and fit every preprocessing step on the training data only
(details in {doc}`ml-foundations`, section A5).

## Assumptions and limitations

- **Same process.** The guarantees assume the calibration data and new cases
  are *exchangeable*: drawn from the same stable process. You cannot prove
  this from the data; if the population or process changes, recalibrate.
- **Many cases, not one.** Calibration statements describe behaviour over many
  cases. They do not guarantee anything about one individual prediction.
- **Mode-specific guarantees.** What the range guarantees differs between
  classification, interval regression and probabilistic regression; see
  {doc}`../foundations/concepts/calibrated_interval_semantics`.
- **The model, not the world.** Explanations describe how the **model**
  responds. They are not causal evidence, and an alternative may describe a
  change that is impossible or undesirable in practice.
- **Not a model fix.** CE calibrates and explains a model; it does not make a
  weak model accurate.

## Continue

- **Next:** {doc}`CE by example <ce-by-example>` (Path B): one prediction,
  explained step by step without code.
- **Go deeper:** {doc}`../foundations/concepts/ce_workflow` (how CE works,
  with a learning path), {doc}`How CE calibrates <../foundations/concepts/calibration_methods>`
  (the methods and their mathematics).
- **See also:** {doc}`../what-is-ce` (what CE adds and how it compares) and,
  if you want to apply CE now, Path C: {doc}`ce-tasks-and-modes`.
- **Before this:** {doc}`ml-foundations` (Path A, step 1).

Entry-point tier: Tier 3.
