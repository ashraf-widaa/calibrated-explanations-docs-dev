# Why CE: from a conventional to a CE workflow

**Path A, step 2.** This page answers one question: *why is CE needed, and
how does a CE-enabled workflow differ from a conventional one?* It needs no
code. If terms such as *feature*, *label* or *test set* are new, read
{doc}`ml-foundations` first.

## A running example

A model flags breast-tumour samples as *malignant* or *benign* from 30
measurements of cell nuclei. (This is an educational example on a public
dataset, not clinical decision support.) For one sample, here is what the
model alone gives, and what CE adds; you will produce these numbers yourself
in the {doc}`guided walkthrough <quickstart_walkthrough>`.

| Question | The model alone | With CE |
|---|---|---|
| What is predicted? | *malignant* | *malignant*, with a calibrated probability of *benign* of 0.29, between 0.17 and 0.33 |
| Why? | — | The strongest reason is `worst concave points > 0.14`: with typical values below 0.14 instead, the calibrated probability of *benign* would be about 0.19 higher |
| What would change it? | — | If `worst concave points` were below 0.14, the calibrated probability of *benign* would be about 0.48 |

## The conventional workflow

```{mermaid}
flowchart TD
    D["Labelled data"] --> S["Split: training and test"]
    S --> T["Train a model"]
    T --> P["Predict: a label or a score"]
    P --> E["Evaluate on the test set"]
```

This gives you a model and a measure of how often it is right. Three things
are missing when someone has to act on **one** prediction:

- **Is the score a real probability?** Many models produce scores that look
  like probabilities but are not calibrated: among cases scored 0.9, far
  more or far fewer than 90% may turn out positive.
- **How certain is it?** A single number hides how well the data support it.
- **Why this prediction, and how firm is that reason?** Explanation tools
  usually explain the model's raw output, and report one number per feature
  without saying how certain it is.

## The CE workflow

```{figure} ../_static/figures/ce-in-ml-workflow.svg
:alt: Labelled data is split into training, calibration and test sets. The model is trained (or an existing one is used). CE takes the trained model and the calibration set, calibrates with Venn-Abers (classification) or conformal predictive systems (regression), explains with factual and alternative explanations, and produces calibrated predictions with a lower and upper value and explanations with ranges, which are interpreted and evaluated on the test set.
:width: 560px
:align: center
:target: ../_static/figures/ce-in-ml-workflow.svg

The CE workflow: grey steps are the conventional workflow; purple parts are added by CE.
```

What changes:

1. **A third data set.** Part of the labelled data becomes a *calibration
   set*. The model never trains on it, so CE can see how the model behaves
   on cases it has not seen.
2. **CE wraps the trained model.** CE does not replace model training. You
   can train the model through CE (`fit`) or wrap a model you have already
   trained; CE leaves the model itself unchanged.
3. **Calibrated outputs with ranges.** Every prediction comes back calibrated
   and with a lower and an upper value.
4. **Explanations from the calibrated output.** CE explains each prediction by
   asking the calibrated model again with one feature changed at a time, so
   every explanation inherits the calibration and has its own range.

## What CE needs from you

| Requirement | Details |
|---|---|
| A supervised task | Classification (a class) or regression (a number), one prediction per case |
| A compatible model | A scikit-learn-style model with `predict`; classifiers must also provide `predict_proba` (without it, calibration fails) |
| Labelled calibration data | Cases with known outcomes that the model was **not** trained on, with the same features |
| The same features for new cases | New cases must be described exactly like the training and calibration data |
| Some extra computation | An explanation asks the calibrated model for many extra predictions per explained case |

## Three data sets, three jobs

| Set | Job | Risk if misused |
|---|---|---|
| Training set | Fit the model | — |
| Calibration set | Let CE measure how the model's outputs relate to real outcomes | Using training data here makes the model look more reliable than it is |
| Test set | Check the model and CE's outputs on untouched cases | Using it for training or calibration gives over-optimistic results |

Any information from the calibration or test data that reaches training, for
example scaling statistics computed on all the data, is **data leakage**.
Split first; fit every preprocessing step on the training data only.
Details: {doc}`ml-foundations` (section A5).

## Four ideas you will meet

- **Calibration.** A probability is calibrated if, among cases given about
  70%, about 70% turn out positive. CE calibrates with Venn-Abers predictors
  for classification and conformal predictive systems for regression.
- **Uncertainty range.** The lower and upper value around a prediction. It
  shows how firmly the calibration data support that prediction. It is a
  statistical statement about many cases, not a promise about one case, and
  its exact meaning depends on the task.
- **Factual explanation.** For each feature, a rule that holds for the case
  (such as `worst concave points > 0.14`) and a weight: how much the
  calibrated prediction would differ with typical values from the other side
  of that condition, with a range.
- **Alternative explanation.** What the calibrated prediction would be if one
  feature had a value in a different range.

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

## Next

- **See it run:** Path B, the {doc}`guided walkthrough <quickstart_walkthrough>`.
- **Apply it:** Path C, {doc}`ce-tasks-and-modes`.
- **Read more:** {doc}`../what-is-ce` (what CE adds and how it compares) and
  {doc}`../foundations/concepts/ce_workflow` (how CE works, with a learning
  path).

Entry-point tier: Tier 3.
