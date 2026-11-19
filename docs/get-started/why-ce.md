# Why CE: from a conventional to a CE workflow

*The {doc}`Quick Start <try-in-browser>` introduces this workflow in one minute,
cases, starting from {ref}`one figure <qs-workflow>`.*

A conventional workflow trains and evaluates a predictive model. CE adds
calibration and explanations of model responses to that workflow. The
{doc}`project overview <../what-is-ce>` describes CE's scope and its
relationship to other methods. Terms such as *feature*, *label* and *test set*
are introduced in {doc}`ml-foundations`.

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

Follow the arrows from the data split to the trained model, then through
**Calibrate** and **Explain** to the two output boxes. The calibration set
feeds the added calibration step; the test set feeds the final evaluation
and interpretation step. Thus CE adds information about predictions and
model responses while keeping training and final evaluation separate.
The blue and orange groups distinguish existing steps from CE's additions;
the labels identify their roles without relying on color.

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
   explanations are computed from calibrated outputs and have their own ranges.
   This does not transfer a prediction guarantee to a feature weight.

## What CE gives you: one example

A model flags breast-tumour samples as *malignant* or *benign* from 30
measurements of cell nuclei. (This is an educational example on a public
dataset, not clinical decision support.) For one sample, here is what the
model alone gives, and what CE adds. {doc}`CE by example <ce-by-example>`,
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

Read the panels from top to bottom. Panel 1 places the probability of
*benign* on a 0-to-1 scale; its estimate and range are below the 0.5 label
boundary. Panel 2 switches to a weight scale centered on zero: the negative
weight and range describe a condition associated with a lower model
probability of *benign*. Panel 3 returns to the probability scale for the
opposite feature condition. Its range crosses 0.5 even though its estimate
does not. This compares model responses, without establishing a causal
effect or recommending an intervention.

## The four ideas behind it

- **Calibration.** CE relates model outputs to known outcomes on held-out
  data. See {ref}`Calibration is not accuracy <wic-calibration>` for the
  probability interpretation and {doc}`ce-tasks-and-modes` for CE's modes.
- **Range (uncertainty).** The lower and upper value around a prediction
  (panel 1), returned when requested. It is CE's calibrated uncertainty
  information for that prediction: a statement about many cases, not a
  promise about one case, and its exact meaning depends on the task.
- **Factual explanation.** For each feature, a rule that holds for the case and
  a weight: how much the calibrated prediction would differ with typical
  values from the other side of the condition, with a range (panel 2). A
  range that includes 0 does not establish a direction.
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

Keep these data roles separate: train the model, calibrate CE on held-out
cases, then evaluate on untouched test cases. Split before fitting
preprocessing as well. {doc}`ML essentials <ml-foundations>` (A5) explains
data leakage and how to avoid it.

## Assumptions and limitations

- **Data and protocol.** Calibration and new cases must be *exchangeable*:
  reordering them leaves their joint distribution unchanged. Independent
  samples from one stable population are an example. Keep the predictive
  model and fitted preprocessing fixed before calibration; the full
  method-specific prerequisites are in the semantics reference. An empirical
  calibration check alone cannot establish these conditions.
- **Many cases, not one.** Calibration statements describe behaviour over many
  cases. They do not guarantee correctness for an individual prediction or
  locate its unknown "true probability" inside the reported pair.
- **Mode-specific guarantees.** What the range guarantees differs between
  classification, interval regression and probabilistic regression; see
  {doc}`../foundations/concepts/calibrated_interval_semantics`.
- **The model, not the world.** Explanations describe how the **model**
  responds. They are not causal evidence, and an alternative may describe a
  change that is impossible or undesirable in practice.
- **Not a model fix.** CE calibrates and explains a model; it does not make a
  weak model accurate.

<span id="continue"></span>

## CE outputs in a concrete case

{doc}`CE by example <ce-by-example>` follows a prediction through calibration,
a factual rule and an alternative. The
{doc}`CE workflow <../foundations/concepts/ce_workflow>` connects those
comparisons to feature substitutions, while
{doc}`calibration_methods <../foundations/concepts/calibration_methods>`
develops the calibration construction behind the reported outputs.
