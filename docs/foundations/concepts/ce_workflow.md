# The CE workflow and how to study it

This page gives the whole picture of how Calibrated Explanations works, in
plain words, and then a learning path from intuition to mathematics and
source code. Start here if you want to understand CE rather than just use it.

## The workflow in one picture

```{mermaid}
flowchart LR
    D["Labelled data"] --> T["Proper training set"]
    D --> C["Calibration set"]
    T --> F["fit: train the model"]
    F --> K["calibrate: learn how the model's<br/>outputs relate to real outcomes"]
    C --> K
    K --> P["predict: calibrated prediction<br/>with a range"]
    K --> E["explain: factual and alternative<br/>explanations with ranges"]
```

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

## Which method CE uses for each task

| Task | Question | Calibration method | Output |
|---|---|---|---|
| Classification | Which class, and how probable? | Venn-Abers predictors | Calibrated class probability with lower and upper bounds |
| Interval regression | Where will the value fall? | Conformal predictive system (CPS) | Prediction with an interval for requested percentiles |
| Probabilistic regression | How likely is an event on the value? | CPS scores calibrated with Venn-Abers | Calibrated event probability with lower and upper bounds |

**Venn-Abers**, in one sentence: CE fits the relation between model score and
outcome twice, once pretending the new case is positive and once negative;
the two fits give the lower and upper probability. **A conformal predictive
system**, in one sentence: CE uses the model's errors on the calibration set
to say how far the true value is likely to be from the prediction.

## How an explanation is built

For each feature, CE splits the feature's values into ranges using the
calibration data, notes which range the case falls in (the *rule*, such as
`worst concave points > 0.14`), and substitutes typical values from the other
range(s). The difference between the case's calibrated prediction and the
calibrated predictions with substituted values is the feature's **weight**,
and the differences between the corresponding bounds give the weight's
range. *Alternative explanations* report the calibrated predictions for
other ranges directly. The
{doc}`walkthrough, section 6 <../../get-started/quickstart_walkthrough>`
shows each step with real numbers.

## What the guarantees rest on

The calibration guarantees hold under one assumption: the calibration data
and the new cases are **exchangeable**, roughly, drawn from the same stable
process. They are statistical statements about many cases, not about one
case, and they apply to the calibrated predictions. Explanation ranges are
computed from calibrated outputs, but no formal per-feature guarantee is
claimed for them. Explanations describe the model; they are not causal. See
{doc}`calibrated_interval_semantics` for the exact statements per task.

## Learning path

Each row is one concept, from Level 1 (understand) to Level 3 (study in
depth). You can enter at any level.

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

Open scientific questions that the CE authors are reviewing are marked
*under review* on the pages above.

Entry-point tier: Tier 3.
