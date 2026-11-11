# CE tasks and outputs

Read this page before running CE code. It answers four questions:

1. Which prediction tasks does CE support?
2. What does each kind of output mean?
3. Which workflow should you follow?
4. Which capabilities work for which task? (a reference table at the end)

If terms such as *classification* or *calibration set* are new, start with
{doc}`ml-foundations`.

## Supported tasks

CE explains **supervised** models that predict for one case at a time. It
supports two task families, and regression can be queried in two ways.

### Classification

The model predicts a **class label**, such as *malignant* or *benign*, and a
**probability** for each class.

- **Binary classification** has two classes. CE reports the calibrated
  probability of the positive class, which is class `1` in the label encoding.
- **Multiclass classification** has three or more classes. CE explains the
  predicted class by default. Explaining all classes at once
  (`multi_labels_enabled=True`) is an explicitly **experimental** option.

### Regression

The model predicts a **number**, such as a disease-progression score. CE can
answer two different questions about that number:

- **Interval regression:** *what range is the outcome likely to fall in?* CE
  returns the point prediction with a calibrated prediction interval.
- **Probabilistic (thresholded) regression:** *how likely is the outcome to be
  at or below a threshold?* CE returns a calibrated probability for that
  event, `P(y ≤ t)`.

Probabilistic regression is not a separate learning paradigm. The model is the
same regression model; only the question asked of its predictions changes.
You select it by passing a `threshold`.

## Semantic modes: what the outputs mean

CE's documentation distinguishes three **semantic modes**. A semantic mode is
a documentation term for *how to interpret an output*. It is not an API
argument: you select the mode through the model type and whether you pass a
`threshold`.

| Semantic mode | Underlying task | You call | Output | Read it as |
|---|---|---|---|---|
| Classification | Classification | `predict_proba(x, uq_interval=True)` | Calibrated class probability with lower and upper probability | "Of the cases that get a model score like this one, about this share belong to the class" |
| Interval regression | Regression | `predict(x, uq_interval=True)` | Point prediction with a prediction interval (default 5th–95th percentile) | "The outcome is likely to fall in this range" |
| Probabilistic regression | Regression | `predict_proba(x, threshold=t, uq_interval=True)` | Calibrated probability of `y ≤ t` with lower and upper probability | "The chance the outcome is at or below `t`" |

### How the uncertainty differs between modes

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
  individual case.
- **Probabilistic regression** combines both: a conformal predictive
  distribution gives the event probability, and Venn–Abers calibrates it.

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

## Choosing your workflow

```{mermaid}
flowchart TD
    Q{"What does your model predict?"} -->|"A category"| C["Classification mode<br/>predict_proba(x, uq_interval=True)"]
    Q -->|"A number"| R{"What do you want to know?"}
    R -->|"A likely range"| IR["Interval regression<br/>predict(x, uq_interval=True)"]
    R -->|"The chance of crossing a threshold"| PR["Probabilistic regression<br/>predict_proba(x, threshold=t, uq_interval=True)"]
    C --> E["Then explain:<br/>explain_factual, explore_alternatives"]
    IR --> E
    PR --> E
```

Every workflow follows the same steps:

1. **Choose the task** that matches your target.
2. **Pick the output interpretation**, the semantic mode.
3. **Check the capabilities** you need in the reference table below.
4. **Prepare data and model**: split into proper training, calibration and
   test sets, then fit the model.
5. **Calibrate** CE on the calibration set.
6. **Explain** the cases you care about.
7. **Interpret** the outputs with their uncertainty.
8. **Judge** whether exchangeability is plausible for how your data were
   collected and how the model will be used. It cannot be proved from the
   data alone.

**Next:** the {doc}`practical walkthrough <quickstart_walkthrough>` runs
this workflow step by step for **binary classification**. It starts there
because a single probability for one of two classes is the easiest output to
read and check, and every later mode reuses the same steps.

## Capability reference

This table is for looking things up, not for reading straight through. Each
row is something CE can do; each column is a task or mode; each cell records
what was checked for CE 1.1.0-dev by running the call on a fresh explainer
with public datasets. "Runs" means the call completes and returns the
documented object type; it is not a statistical validation.

| Capability | Binary classification | Multiclass classification | Interval regression | Probabilistic regression |
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
