# The CE workflow and how to study it

This page gives the whole picture of how Calibrated Explanations works, in
plain words, and then a learning path from intuition to mathematics and
source code. Start here if you want to understand CE rather than just use it.

## The workflow in one picture

```{raw} html
<figure class="ce-figure">
  <a href="../../_static/figures/ce-in-ml-workflow.svg" title="Open the figure at full size">
    <picture>
      <source media="(max-width: 600px)" srcset="../../_static/figures/ce-in-ml-workflow-narrow.svg">
      <img src="../../_static/figures/ce-in-ml-workflow.svg" width="1000" height="540" alt="In blue, a conventional workflow: labelled data is split into training and test sets, a model is trained (or an existing one is used), it predicts a label or a raw score, and it is evaluated on the test set. In orange, what CE adds: a calibration set held out from training, a Calibrate step (Venn-Abers predictors or conformal predictive systems) and an Explain step (factual and alternative explanations). CE returns a calibrated prediction with a lower and upper value and an explanation whose rules and weights each have a range; both are evaluated and interpreted on the test set.">
    </picture>
  </a>
  <figcaption>Where CE fits in a machine-learning workflow: conventional steps in blue, CE's additions in orange.</figcaption>
</figure>
```

The arrows show where each data split is used. Training data fit the model;
calibration data enter **Calibrate**; test data reach **Evaluate and
interpret** alongside the outputs. The two CE output boxes separate a
calibrated prediction from the rules and weights that explain model
responses. A range in one box does not automatically carry the statistical
interpretation of a range in the other. The numbered steps below follow
these labelled roles.

1. **Split the data.** The model trains on one part (the *proper training
   set*). A second part, the *calibration set*, is never used for training.
2. **Fit.** An ordinary model is trained, exactly as without CE.
3. **Calibrate.** CE looks at how the trained model's outputs relate to the
   real outcomes on the calibration set. The model itself is not changed.
4. **Predict.** Every prediction comes back calibrated and with a range: a
   lower and an upper value.
5. **Explain.** CE explains a prediction by asking the calibrated model again
   with one feature changed at a time, and reports how much each feature's
   value moves the calibrated prediction, again with a range.

These five steps are a teaching view of CE. They follow the calls you make
(`fit`, `calibrate`, `predict` or `predict_proba`, `explain_factual` or
`explore_alternatives`), not every internal step of the implementation.

(ce-workflow-methods)=

## Which method CE uses for each task

Read each row from left to right: the task and question decide the CE mode,
the mode decides the calibration method, and the method decides what the
range in the output means.

:::{div} ce-table-compact
| Task | Question | Calibration method | Output | Read the range as |
|---|---|---|---|---|
| Classification | Which class, and how probable? | Venn-Abers predictors | Calibrated class probability with lower and upper bounds | Bounds of a probability, not a confidence interval |
| Interval regression | Where will the value fall? | Conformal predictive system (CPS) | Prediction with an interval for requested percentiles | An interval for the value; the requested coverage holds on average over many cases, not for each case |
| Probabilistic regression | How likely is an event on the value? | CPS scores calibrated with Venn-Abers | Calibrated event probability with lower and upper bounds | Bounds of the probability of an event, not an interval for the value |
:::

The exact statements, with their conditions, are in
{doc}`calibrated_interval_semantics`; the methods are derived in
{doc}`calibration_methods` (section 4). *The validity statement for
threshold events in probabilistic regression is under review by the CE
authors.*

Factual and alternative explanations are **explanation types**, not modes:
both are available in every mode above.

**Venn-Abers**, in one sentence: CE fits the relation between model score and
outcome twice, once pretending the new case is positive and once negative;
the two fits give the lower and upper probability. **A conformal predictive
system**, in one sentence: CE uses the model's errors on the calibration set
to say how far the true value is likely to be from the prediction.

(ce-workflow-explanations)=

## How an explanation is built

Start with the quantity CE is explaining. In the running binary example it is
the probability of *benign*, not the probability of the predicted class
*malignant*. CE reports 0.286, with a prediction range of [0.167, 0.333].

1. **Find a factual rule.** CE groups a numerical feature's values into ranges
   using calibration data. The case satisfies
   `worst concave points > 0.14`; this observed condition is its factual rule.
2. **Substitute feature values.** Keep the case's other features fixed and ask
   the calibrated model again with representative values from another range.
   CE summarizes those substituted outputs. This asks about the model's
   response, not about changing the real-world patient.
3. **Compare the predictions.** For the other side of this split,
   `worst concave points < 0.14`, the summarized probability is 0.476.
   The factual weight compares the original with the substituted output:
   0.286 − 0.476 = −0.190. Relative to those substituted values, the observed
   condition lowers the modeled probability of *benign*.
4. **Read the alternative directly.** The alternative reports 0.476 with
   range [0.333, 0.600]. The same substituted scenario supports the factual
   comparison and the alternative row, but they report different quantities:
   a contribution versus a scenario prediction.

The factual weight also has a derived range, approximately [−0.31, −0.05]
here. In this single-feature comparison, CE subtracts the substituted-output
bounds from the original point prediction and orders the resulting values.
It does not subtract the original lower bound from another lower bound.
These derived ranges describe the computation; they are not formal
per-feature coverage guarantees.

This is one numerical feature and one split. Other features can have more
candidate ranges; conjunctions combine conditions. The
{doc}`walkthrough, section 6 <../../get-started/quickstart_walkthrough>`
shows the calculation and its output, while
{doc}`../how-to/interpret_explanations` explains how to read the rule payloads.
The general scientific interpretation of explanation ranges remains under
author review (SR-14).

(ce-workflow-guarantees)=

## What the guarantees rest on

The calibration data and new cases must be **exchangeable**, roughly, drawn
from the same stable process, and the method's calibration protocol must be
respected. For example, the predictive model is fixed before calibration;
{doc}`calibration_methods` states the detailed prerequisites. The exact
validity wording remains under author review. The statements concern
calibrated predictions over calibration/test draws, not guaranteed correctness
for one case. Explanation ranges are
computed from calibrated outputs, but no formal per-feature guarantee is
claimed for them. Explanations describe the model; they are not causal. See
{doc}`calibrated_interval_semantics` for the exact statements per task.

When reading a range, first ask what it refers to: a class or event
probability, a numeric target, or an explanation weight. These quantities have
different interpretations. The {doc}`semantics reference <calibrated_interval_semantics>`
keeps the formal qualifications together; {doc}`../how-to/interpret_explanations`
connects them to returned records.

Whether CE's ranges should be described as aleatoric or epistemic uncertainty
remains under author review. Do not infer either interpretation from width
alone.

## Learning path

Each row is one concept, from Level 1 (understand) to Level 3 (study in
depth). You can enter at any level.

:::{div} ce-table-compact
| Concept | Level 1: understand | Level 2: apply and interpret | Level 3: study in depth |
|---|---|---|---|
| Why CE | {doc}`../../what-is-ce` | {doc}`../../get-started/ce-tasks-and-modes` | Löfström et al. (2024), see {doc}`../../citing` |
| Data roles and calibration | {doc}`../../get-started/ml-foundations` (A5, A6) | {doc}`Walkthrough <../../get-started/quickstart_walkthrough>` (sections 2–5) | {doc}`calibration_methods` (section 1) |
| Venn-Abers | This page | {doc}`Walkthrough <../../get-started/quickstart_walkthrough>` (section 5) | {doc}`calibration_methods` (section 2); Vovk and Petej (2014); [`calibration/venn_abers.py`](https://github.com/Moffran/calibrated_explanations/blob/main/src/calibrated_explanations/calibration/venn_abers.py) |
| Conformal prediction and CPS | This page; {doc}`Glossary <../../glossary/science>` | {doc}`probabilistic_regression` | {doc}`calibration_methods` (section 3); Vovk et al. (2019); [`calibration/interval_regressor.py`](https://github.com/Moffran/calibrated_explanations/blob/main/src/calibrated_explanations/calibration/interval_regressor.py) |
| Probabilistic regression | This page | {doc}`probabilistic_regression` | {doc}`calibration_methods` (section 4); Löfström et al. (2025) |
| Factual explanations | {doc}`../../get-started/ml-foundations` (A7) | {doc}`../how-to/interpret_explanations`; walkthrough sections 6–7 | Löfström et al. (2024); [`explanations/explanation.py`](https://github.com/Moffran/calibrated_explanations/blob/main/src/calibrated_explanations/explanations/explanation.py); [`utils/discretizers.py`](https://github.com/Moffran/calibrated_explanations/blob/main/src/calibrated_explanations/utils/discretizers.py) |
| Alternative explanations | Walkthrough section 8 | {doc}`alternatives` | Löfström et al. (2024) |
| Subgroup (Mondrian) calibration | {doc}`Glossary <../../glossary/science>` | {doc}`../how-to/conditional_calibration` | Löfström and Löfström (2024), see {doc}`../../citing` |
| Guarantees and limits | {doc}`../../what-is-ce` | This page | {doc}`calibrated_interval_semantics`; {doc}`calibration_methods` (section 5) |
| Implementation and tests | — | {doc}`architecture` | [Source code](https://github.com/Moffran/calibrated_explanations/tree/main/src/calibrated_explanations); [calibration tests](https://github.com/Moffran/calibrated_explanations/tree/main/tests/unit/calibration) |
:::

Open scientific questions that the CE authors are reviewing are marked
*under review* on the pages above.

Entry-point tier: Tier 3.
