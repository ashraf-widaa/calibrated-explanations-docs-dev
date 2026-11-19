# What CE is and what it adds

```{raw} html
<nav class="ce-journey" aria-label="Get started, step 1 of 5"><ol><li aria-current="step"><a href="what-is-ce.html"><span class="ce-journey-n">1</span>What CE is</a></li><li><a href="get-started/try-in-browser.html"><span class="ce-journey-n">2</span>Quick Start</a></li><li><a href="get-started/installation.html"><span class="ce-journey-n">3</span>Install</a></li><li><a href="foundations/how-to/interpret_explanations.html"><span class="ce-journey-n">4</span>Read it</a></li><li><a href="get-started/apply-to-your-data.html"><span class="ce-journey-n">5</span>Your data</a></li></ol></nav>
```

**Calibrated Explanations (CE)** is an open-source Python library that adds two
things to a trained prediction model: **calibrated predictions, with lower and
upper bounds available on request**, and **explanations of each prediction with
an uncertainty range for every feature's weight**. It works with models that have a
scikit-learn-style classification or regression interface.

**Get started, step 1 of 5 · about 5 minutes.** Use this overview to
understand CE's purpose, outputs and fit for your task. To see these
outputs on two worked cases, continue with the
{doc}`Quick Start <get-started/try-in-browser>` (step 2, no installation).
For the steps CE adds to a model workflow, read {doc}`get-started/why-ce`;
for a concrete output, read {doc}`get-started/ce-by-example`. No mathematics
is needed here; the links below lead to mechanisms and formal qualifications.

(wic-problem)=

## The problem: a prediction and an explanation are not enough

A model's output often looks like a probability: "0.9 that this sample is
benign". Two things can go wrong with taking it at face value.

1. **The number may not mean what it says.** Many models produce scores that
   look like probabilities but are not *calibrated*: among all the cases a
   model scores at 0.9, far more or far fewer than 90% may turn out positive.
   Tree-based models trained without a calibration step are a common example.
2. **The number hides its own uncertainty.** A single 0.9 says nothing about
   how well the data support it. Two cases with the same score can rest on
   very different amounts of evidence.

An explanation of a raw model output does not itself calibrate that output.
Feature-attribution methods such as LIME and SHAP answer a useful question:
which features contribute to the model response? CE addresses the related
question of explaining calibrated outputs with reported ranges. The
{doc}`comparison <compare>` distinguishes these outputs without ranking
the methods generally.

(wic-calibration)=

## Calibration is not accuracy

**Accuracy** asks how often the predicted class is right. **Calibration** asks
whether the probabilities mean what they say: among the cases given about 0.7,
about 70% should turn out positive. The two are different properties.

- A model can be **accurate but miscalibrated**: it picks the right class most
  of the time, while its probabilities are too extreme or too cautious. Modern
  neural networks are a well-documented example (Guo et al., 2017).
- A model can be **calibrated but of little use**: a model that gives every
  case the overall share of positives as its probability is calibrated, yet it
  cannot tell one case from another.

Calibration concerns probability forecasts over many cases and says nothing
about whether one individual prediction is correct. It does not guarantee
improved accuracy.
In CE, the Venn–Abers pair and its merged estimate have different validity
qualifications. {doc}`How CE calibrates
<foundations/concepts/calibration_methods>` explains the methods.

(wic-adds)=

## What CE adds

CE changes the order of the work: it **calibrates first, then explains the
calibrated output**.

- **Calibration on held-out data.** CE uses data the model never saw (a
  *calibration set*) to learn how the model's outputs relate to real outcomes.
  For classification it uses Venn-Abers predictors; for regression it uses
  conformal predictive systems.
- **Prediction bounds and explanation ranges.** Request prediction bounds
  with `uq_interval=True`; explanation outputs also include ranges for
  feature weights or alternative scenarios. These derived ranges do not
  inherit a formal per-feature guarantee from prediction calibration.
- **Two kinds of explanation.** A *factual explanation* shows which of the
  case's own feature values move the calibrated prediction, and by how much.
  An *alternative explanation* shows what the model would predict if a feature
  had a value in a different range.
- **Three output modes for two prediction tasks.** Classification (binary and
  multiclass), interval regression
  ("where will the value fall?") and probabilistic regression ("how likely is
  the value to be below a threshold?").

**A small example.** In the breast-cancer example used throughout these
pages, the random forest's raw score that test case 2 is benign is 0.16. After
calibration, CE reports a probability of 0.286 with the range [0.167, 0.333],
so the predicted class is malignant. A factual explanation then lists the
feature conditions of that case with a weight, and a range for each weight.
{doc}`CE by example <get-started/ce-by-example>` walks through this case and
its explanations step by step.

The methods are published in peer-reviewed work, starting with Löfström et
al. (2024) for classification and Löfström et al. (2025) for regression; the
[citation page](citing.md) lists all papers, including multiclass, conditional
(Mondrian), fast and guarded explanations.

(wic-guarantees)=

## What CE guarantees, and what it does not

CE's guarantees are **statistical and depend on stated assumptions** and the
method-specific calibration protocol. They differ by task and returned
quantity; the pair's validity must not be transferred to its merged estimate
or to explanation-weight ranges.

:::{div} ce-table-compact
| CE does provide | CE does not provide |
|---|---|
| Classification: a Venn-Abers pair and a merged probability, with their distinct qualifications in the semantics reference | A guarantee for any single individual case |
| Interval regression: intervals for requested percentiles from a conformal predictive system | Guarantees after the data change (drift, a new population, a new period) |
| Probabilistic regression: event probabilities and ranges; exact validity wording remains under author review | Causal statements: explanations describe the **model**, not what would happen if the world changed |
| Explanations computed from calibrated outputs, with ranges | Formal per-feature guarantees for explanation ranges |
:::

A range is not a statement that a prediction is correct: a case with a narrow
range can still turn out differently from the prediction.

**Data and protocol assumptions.** The calibration data and the new cases must be
*exchangeable*: reordering them leaves their joint distribution unchanged.
Independent draws from one stable population are an example. The predictive
model and any fitted preprocessing or difficulty estimator must be fixed
before the calibration cases are used. Exchangeability cannot be established
by an empirical calibration check alone. The current
documentation also speaks of "distribution-matched" data; *that wording is
under review by the CE authors*.

The [semantics reference](foundations/concepts/calibrated_interval_semantics.md)
is the canonical statement of all guarantees and non-guarantees.

(wic-fit)=

## When CE is a good fit

The list below describes situations where CE's outputs can be used. It is not
a list of demonstrated benefits: the published evaluations are on the
{doc}`citation page <citing>`, and whether CE helps in your own setting is
something to measure ({doc}`practitioner/evaluate_ce`).

CE fits when:

- decisions are made about **individual cases** and someone needs to judge how
  far to trust each prediction;
- you can set aside **labelled data the model was not trained on** for
  calibration;
- the model has a scikit-learn-style interface (`fit`, `predict`, and
  `predict_proba` for classification);
- the people using the predictions need **reasons** they can check against
  their own knowledge, with an indication of how firm those reasons are.

Points to plan for:

- **Calibration data.** Labelled data must be held out from training, so less
  data is left for training the model itself.
- **Computation.** An explanation asks the calibrated model for many extra
  predictions per explained case (one set per feature), so explaining many
  cases takes longer than predicting them; see
  [performance tuning](foundations/how-to/tune_runtime_performance.md).
- **Data that change over time.** If the population or process changes, the
  calibration may no longer apply; recalibrate on recent data.
- **Not a replacement for evaluation.** CE does not tell you whether the model
  is accurate enough for the task; evaluate that separately.

(wic-compare)=

## How CE relates to other methods

The differences below are about **what each kind of method is designed to
produce**, not about which performs better. Published comparisons are listed
on the [citation page](citing.md).

:::{div} ce-table-compact
| Method family | Designed to produce | Calibration of the model's output | Uncertainty for each explanation |
|---|---|---|---|
| Feature-attribution methods such as LIME and SHAP | A number per feature explaining the model's own output | Not part of the method | Not part of the standard methods |
| Conformal prediction packages | Prediction sets or intervals with coverage guarantees | Coverage calibration; not necessarily probability calibration | No feature-level explanations |
| Calibrated Explanations | Calibrated predictions with ranges, and rule-based explanations with ranges | Yes (Venn-Abers, conformal predictive systems) | Yes, as ranges derived from calibrated outputs |
:::

A {doc}`short comparison page <compare>` gives more detail.

<span id="where-to-go-next"></span>

## Interpreting a concrete CE output

{doc}`get-started/ce-by-example` follows one prediction through calibration,
factual rules and alternatives. The
{doc}`interpretation guide <foundations/how-to/interpret_explanations>`
explains the returned quantities, while
{doc}`foundations/concepts/calibration_methods` develops the statistical
construction behind them.

**Next in Get started (step 2 of 5):** the
{doc}`Quick Start <get-started/try-in-browser>`: learn the CE workflow and
read your first explanation.

## References

- Guo, C., Pleiss, G., Sun, Y., and Weinberger, K. Q. (2017).
  [On calibration of modern neural networks](https://proceedings.mlr.press/v70/guo17a.html).
  *Proceedings of the 34th International Conference on Machine Learning*,
  PMLR 70, 1321–1330.
- Löfström, H., Löfström, T., Johansson, U., and Sönströd, C. (2024).
  [Calibrated explanations: with uncertainty information and counterfactuals](https://doi.org/10.1016/j.eswa.2024.123154).
  *Expert Systems with Applications*, 246, 123154.
- Löfström, T., Löfström, H., Johansson, U., Sönströd, C., and Matela, R.
  (2025). [Calibrated explanations for regression](https://doi.org/10.1007/s10994-024-06642-8).
  *Machine Learning*, 114, 100.
- Vovk, V., and Petej, I. (2014). Venn-Abers predictors. *Proceedings of the
  30th Conference on Uncertainty in Artificial Intelligence*.
  [arXiv:1211.0025](https://arxiv.org/abs/1211.0025).
- Vovk, V., Shen, J., Manokhin, V., and Xie, M. (2019). Nonparametric
  predictive distributions based on conformal prediction. *Machine Learning*,
  108, 445–474. [doi:10.1007/s10994-018-5755-8](https://doi.org/10.1007/s10994-018-5755-8).
