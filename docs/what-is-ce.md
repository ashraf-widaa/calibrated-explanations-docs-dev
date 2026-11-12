# What CE is and what it adds

**Calibrated Explanations (CE)** is an open-source Python library that adds two
things to a trained prediction model: **calibrated predictions with an
uncertainty range**, and **explanations of each prediction with an uncertainty
range for every feature's effect**. It works with models that have a
scikit-learn-style classification or regression interface.

This page explains the problem CE addresses, what it contributes, what it does
and does not guarantee, and when it is a good fit. No mathematics is needed;
links at the end lead to the full treatment.

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

Explanation methods inherit both problems. Most explanation tools, such as
LIME and SHAP, explain whatever the model outputs. If those outputs are
miscalibrated, the explanation describes a miscalibrated model; and a
feature's importance is usually reported as one number, without saying how
certain it is.

## What CE adds

CE changes the order of the work: it **calibrates first, then explains the
calibrated output**.

- **Calibration on held-out data.** CE uses data the model never saw (a
  *calibration set*) to learn how the model's outputs relate to real outcomes.
  For classification it uses Venn-Abers predictors; for regression it uses
  conformal predictive systems.
- **Uncertainty on every output.** Each calibrated prediction comes with a
  lower and an upper value. Each feature's effect in an explanation also comes
  with a range.
- **Two kinds of explanation.** A *factual explanation* shows which of the
  case's own feature values move the calibrated prediction, and by how much.
  An *alternative explanation* shows what the model would predict if a feature
  had a value in a different range.
- **Three tasks.** Classification (binary and multiclass), interval regression
  ("where will the value fall?") and probabilistic regression ("how likely is
  the value to be below a threshold?").

The methods are published in peer-reviewed work, starting with Löfström et
al. (2024) for classification and Löfström et al. (2025) for regression; the
[citation page](citing.md) lists all papers, including multiclass, conditional
(Mondrian), fast and guarded explanations.

## What CE guarantees, and what it does not

CE's guarantees are **statistical and conditional**. They hold for the
calibrated predictions, under an assumption about the data, and they differ by
task.

| CE does provide | CE does not provide |
|---|---|
| Classification: calibrated class probabilities with interval bounds from Venn-Abers | A guarantee for any single individual case |
| Interval regression: intervals for requested percentiles from a conformal predictive system | Guarantees after the data change (drift, a new population, a new period) |
| Probabilistic regression: calibrated probabilities for threshold events | Causal statements: explanations describe the **model**, not what would happen if the world changed |
| Explanations computed from calibrated outputs, with ranges | Formal per-feature guarantees for explanation ranges |

**The assumption.** The calibration data and the new cases must be
*exchangeable*: roughly, drawn from the same stable process, so that their
order does not matter. You cannot prove this from the data; it is a judgement
about how the data were collected and how the model is used. The current
documentation also speaks of "distribution-matched" data; *that wording is
under review by the CE authors*.

The [semantics reference](foundations/concepts/calibrated_interval_semantics.md)
is the canonical statement of all guarantees and non-guarantees.

## When CE is a good fit

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

## How CE relates to other methods

The differences below are about **what each kind of method is designed to
produce**, not about which performs better. Published comparisons are listed
on the [citation page](citing.md).

| Method family | Designed to produce | Calibration of the model's output | Uncertainty for each explanation |
|---|---|---|---|
| Feature-attribution methods such as LIME and SHAP | A number per feature explaining the model's own output | Not part of the method | Not part of the standard methods |
| Conformal prediction packages | Prediction sets or intervals with coverage guarantees | Yes, for predictions | No feature-level explanations |
| Calibrated Explanations | Calibrated predictions with ranges, and rule-based explanations with ranges | Yes (Venn-Abers, conformal predictive systems) | Yes, as ranges derived from calibrated outputs |

A {doc}`short comparison page <compare>` gives more detail.

## Where to go next

| You want to | Go to |
|---|---|
| Try CE on a real example | {doc}`Quick Start <get-started/index>` |
| See which tasks and outputs CE supports | {doc}`get-started/ce-tasks-and-modes` |
| Understand how CE calibrates | {doc}`foundations/concepts/calibration_methods` |
| Learn to read explanations | {doc}`foundations/how-to/interpret_explanations` |
| Look up a term | {doc}`Glossary <glossary/index>` |
| Read the regulatory context | {doc}`practitioner/playbooks/eu-ai-act-compliance` |

## References

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

Entry-point tier: Tier 3.
