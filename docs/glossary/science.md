# Scientific & Theoretical Glossary

Short definitions of the machine-learning, explainability, probability,
calibration and uncertainty terms behind CE. Each entry links to the page under
*How CE Works* that teaches the idea. For library objects and parameters, see
the {doc}`software`. For all terms in one list, see the {doc}`Glossary <index>`.

Each entry gives a short definition, other names for the same idea, and one
page to read next. Entries marked *wording under review* or *name under review*
are not yet confirmed by the CE authors.

## Machine learning and data

```{glossary}
:sorted:

Calibration set
Calibration data
Calibration split
  Labelled data held out from training and used only to calibrate CE. Because
  the model has not seen these cases, CE can measure how the model's outputs
  relate to real outcomes. Keep it separate from the
  {term}`proper training set <Proper training set>` and from the test data.

  **Learn more:** {doc}`../get-started/ml-foundations` (section A5)

Proper training set
Proper training split
  The part of the labelled data used to fit the underlying model. CE requires
  it to be separate from the {term}`calibration set <Calibration set>`: fit the
  model on the proper training set, then calibrate on the held-out data.

  **Learn more:** {doc}`../get-started/ml-foundations` (section A5)
```

## Explainability

```{glossary}
:sorted:

Feature attribution
Feature importance
  A number per feature that describes how much that feature moved a
  prediction. LIME and SHAP are widely used attribution methods. CE reports
  rules with weights, and an uncertainty range for each weight.

  **Learn more:** {doc}`../get-started/ml-foundations` (section A7)

Local explanation
Global explanation
  A local explanation describes one prediction; a global explanation
  describes the model as a whole. CE's factual and alternative explanations
  are local.

  **Learn more:** {doc}`../get-started/ml-foundations` (section A7)

Alternative explanation
  An explanation that proposes changes to feature values that would give a
  different calibrated outcome. Each rule pairs the changed condition with the
  calibrated prediction and uncertainty interval for that scenario.
  Alternatives describe how the model responds to changed inputs; they are not
  causal claims about the real world.

  **Learn more:** {doc}`../foundations/concepts/alternatives`

Conjunctive rule
Conjunction
  A {term}`rule <Rule>` whose condition combines more than one feature. CE adds
  conjunctive rules to existing explanations on request.

  **Learn more:** {doc}`../foundations/concepts/alternatives`

Ensured explanation
  An {term}`alternative explanation <Alternative explanation>` kept by the
  ensured filter because its uncertainty interval is not wider than the
  interval of the original prediction, so the calibration data gives the
  proposed change stronger support. *Wording under review.*

  **Learn more:** {doc}`../practitioner/playbooks/ensured-explanations`

Explanation envelope
  The uncertainty interval attached to a rule or feature weight inside an
  explanation. It summarises how the model's calibrated output responds when
  that feature is perturbed. It is not a causal guarantee and should not be
  read as a formal per-feature coverage guarantee.

  **Learn more:** {doc}`../foundations/concepts/calibrated_interval_semantics`

Factual explanation
  An explanation of one prediction as it is. It pairs the calibrated prediction
  and its uncertainty interval with factual rules: each rule binds the observed
  feature value to a condition and gives a calibrated
  {term}`feature weight <Feature weight>` with its own uncertainty interval.

  **Learn more:** {doc}`../foundations/how-to/interpret_explanations`

Feature weight
  The calibrated contribution of one feature rule to the prediction, reported
  with its own uncertainty interval. A positive weight pushes the calibrated
  prediction towards the positive outcome, a negative weight pulls it away, and
  a larger magnitude means more influence.

  **Learn more:** {doc}`../foundations/how-to/interpret_explanations`

Guarded explanation
  An experimental kind of CE explanation that removes candidate rule intervals
  rejected by an in-distribution guard. The guard checks whether the perturbed
  value behind each interval is plausible; it does not certify every point in
  an interval and does not test whether the explained instance itself is out
  of distribution.

  **Learn more:** {doc}`../foundations/concepts/guarded_explanations`

Rule
  The building block of a CE explanation. In a factual explanation, a rule is
  a feature condition with a calibrated weight; in an alternative explanation,
  it is a changed condition with the calibrated prediction for that scenario.
  Rules are listed by absolute weight, largest first.

  **Learn more:** {doc}`../foundations/how-to/interpret_explanations`
```

## Probability and calibration

```{glossary}
:sorted:

Brier score
  The mean squared difference between predicted probabilities and observed
  outcomes (1 or 0). Lower is better and 0 is perfect. It scores the
  probabilities themselves, not only the predicted labels.

  **Learn more:** {doc}`../practitioner/evaluate_ce` (section 2)

Reliability diagram
Reliability table
  A bin-by-bin comparison of the average predicted probability with the
  observed share of positive outcomes on held-out data. For calibrated
  probabilities the two are close; with few cases per bin they vary by
  chance.

  **Learn more:** {doc}`../foundations/concepts/calibration_methods` (section 1)

Calibration
  In CE, the step that adjusts a trained model's outputs on held-out
  {term}`calibration data <Calibration set>` before anything is explained:
  Venn-Abers predictors for classification and conformal predictive systems
  for regression. Explanations are then computed from the calibrated outputs,
  not from raw model scores.

  **Learn more:** {doc}`../foundations/concepts/calibration_methods`

Venn-Abers predictor
Venn–Abers predictor
  The calibration method CE uses for classification. It turns the model's
  scores into calibrated probabilities with an interval, a lower and an upper
  bound. In probabilistic regression it calibrates the event probabilities
  derived from the {term}`conformal predictive system <Conformal predictive system>`.

  **Learn more:** {doc}`../foundations/concepts/calibration_methods` (section 2)
```

## Uncertainty

```{glossary}
:sorted:

Uncertainty interval
  The low and high bounds CE reports with a calibrated prediction. In
  classification and probabilistic regression it bounds the calibrated
  probability; in interval regression it is a CPS percentile interval for the
  predicted value. What it guarantees depends on the mode and its assumptions.

  **Learn more:** {doc}`../foundations/concepts/calibrated_interval_semantics`
```

## Conformal and Venn–Abers methods

```{glossary}
:sorted:

Conformal predictive system
CPS
  The conformal method CE uses for regression. Calibrated on held-out data, it
  gives predictive intervals for requested percentiles in interval regression
  and, combined with Venn-Abers, calibrated event probabilities in
  probabilistic regression.

  **Learn more:** {doc}`../foundations/concepts/calibration_methods` (section 3)

Difficulty estimation
  For regression: scaling the conformal intervals by how hard each instance is
  to predict, as estimated by a separate difficulty estimator from the `crepes`
  library. Harder instances get wider intervals and easier ones narrower
  intervals, instead of one width for all.

  **Learn more:** {doc}`../practitioner/advanced/normalization-guide`

Interval regression
Percentile regression
  A regression query that returns a numeric prediction with a CPS percentile
  interval, whose width is set by {term}`low_high_percentiles`. It answers
  "where will y fall?", while {term}`probabilistic regression <Probabilistic regression>`
  answers "how likely is an event on y?". *Name under review.*

  **Learn more:** {doc}`../foundations/concepts/probabilistic_regression`

Mondrian calibration
Conditional calibration
  Calibration that partitions the calibration data by a category label and fits
  a separate calibrator per category, so uncertainty can be reported by
  subgroup or segment. Categories are passed with {term}`bins` or derived by a
  stored categorizer ({term}`mc`).

  **Learn more:** {doc}`../foundations/how-to/conditional_calibration`

Probabilistic regression
Thresholded regression
  A regression query that returns the calibrated probability of a threshold
  event, such as P(y ≤ t), with an interval for that probability. It is
  selected by passing a {term}`threshold`; CPS outputs are calibrated with
  Venn-Abers. "Thresholded regression" names the same mode in implementation
  documents.

  **Learn more:** {doc}`../foundations/concepts/calibrated_interval_semantics`

Reject option
  In CE classification, withholding a prediction based on the instance's
  conformal prediction set: a single class is accepted, an empty set is a
  novelty reject, and a set of two or more classes is an ambiguity reject. How
  rejected instances are handled is set by a {term}`reject policy <Reject policy>`.

  **Learn more:** {doc}`../practitioner/advanced/reject-policy`
```

## Assumptions, guarantees and limits

```{glossary}
:sorted:

Distribution shift
Drift
  A change between the data CE was calibrated on and the data it is applied
  to, for example over time or between populations. CE gives no calibration
  guarantee under distribution drift, regime shift or adversarial change.

  **Learn more:** {doc}`../foundations/concepts/calibrated_interval_semantics`

Exchangeability
  The assumption, stated for every CE mode, that the calibration data and the
  cases CE is applied to are exchangeable or distribution-matched: their joint
  distribution does not change when the cases are reordered. CE's calibration
  guarantees depend on it. *Wording under review.*

  **Learn more:** {doc}`../foundations/concepts/calibrated_interval_semantics`
```

Entry-point tier: Tier 3.
