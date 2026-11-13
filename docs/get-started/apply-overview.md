# Apply CE: the practical workflow

**Path C, step 2.** This page shows, without code, what applying CE to your
own problem involves: the steps, what each step produces, how to check it, and
which tutorial to run next. It assumes you have chosen a task and mode in
{doc}`ce-tasks-and-modes` (step 1).

## The seven steps at a glance

1. **Check that CE fits.** Confirm a supervised task (a class or a number per
   case), a compatible model and labelled data you can hold back.
   *You get:* a go or no-go. *Check:* the three checks in
   {doc}`ce-tasks-and-modes` ("Choosing your workflow").
2. **Split the data.** Divide labelled data into a training set, a calibration
   set and a test set, **before** any preprocessing.
   *You get:* three sets with separate jobs. *Check:* no case appears in two
   sets; preprocessing is fitted on training data only.
3. **Wrap and calibrate.** Wrap your model with `WrapCalibratedExplainer`;
   train it (`fit`) or use a model you have already trained; then `calibrate`
   on the calibration set.
   *You get:* a calibrated explainer; the model itself is unchanged.
   *Check:* the model was never trained on the calibration set.
4. **Predict with ranges.** Ask for calibrated predictions with their lower
   and upper values (`predict` or `predict_proba` with `uq_interval`).
   *You get:* for classification, a calibrated probability with lower and upper
   probability; for interval regression, a prediction with an interval; for
   probabilistic regression, the probability that the outcome is at or below a
   threshold, with lower and upper probability. *Check:* read the output for
   your mode in {doc}`ce-tasks-and-modes` ("What the outputs mean").
5. **Explain.** Ask for factual explanations (`explain_factual`) and, if
   useful, alternatives (`explore_alternatives`).
   *You get:* rules that hold for the case, each with a weight and a weight
   range, and what-if scenarios with their own ranges. *Check:* ranges that
   include 0 do not settle the direction of an effect; explanations describe
   the model, not causes.
6. **Evaluate.** Check the calibrated outputs on the test set.
   *You get:* scores such as the Brier score, reliability checks and interval
   coverage on held-out cases. *Check:* one small test set proves no
   improvement; repeat across splits ({doc}`../practitioner/evaluate_ce`).
7. **Integrate and maintain.** Put preprocessing and the model in one
   pipeline, save the calibrated state (`save_state`, `load_state`) and monitor
   the data.
   *You get:* a reusable calibrated explainer. *Check:* recalibrate when the
   model is retrained or the population changes.

## Things that matter in practice

- **The model may already be trained.** CE detects a fitted model; you then
  calibrate it directly. Without `predict_proba`, a classifier cannot be
  calibrated.
- **Keep preprocessing inside the model.** A scikit-learn pipeline fitted on
  the training set is applied in the same way to every case CE passes to the
  model. CE passes NumPy arrays to the model, so fit the pipeline on arrays.
- **The calibration set is evidence.** Its size limits how firm the ranges
  can be: with few calibration cases, ranges become wide. There is no fixed
  minimum; a few hundred cases is a common starting point.
- **Ranges describe many cases, not one.** What a range means, and what it
  does not guarantee, differs between modes; the canonical statement is
  {doc}`../foundations/concepts/calibrated_interval_semantics`.
- **Same process, or recalibrate.** CE's guarantees assume that calibration
  data and future cases come from the same stable process.

## Common mistakes

| Mistake | Why it matters |
|---|---|
| Calibrating on the training data | The model looks more reliable than it is |
| Fitting preprocessing (for example scaling) on all the data | Information from the calibration and test sets leaks into training |
| Reading a range as a guarantee for one case | Ranges are statements over many cases, under assumptions |
| Reading a weight as a cause, or an alternative as a recommendation | Explanations describe how the model responds |
| Concluding that calibration improved the model from one test set | One split can go either way; evaluate across splits |

## Which tutorial to run

| Your situation | Tutorial (executable, with real output) |
|---|---|
| You want to see the whole workflow on one case first | {doc}`Python walkthrough <quickstart_walkthrough>` (binary classification) |
| Your model predicts a class | {doc}`Classification tutorial <quickstart_classification>` |
| Your model predicts a number | {doc}`Regression tutorial <quickstart_regression>` (interval and probabilistic regression) |
| Explanations should only use typical feature values | {doc}`Guarded explanations tutorial <quickstart_guarded>` |
| You are ready to use your own data and model | {doc}`Apply CE to your own data <apply-to-your-data>` |

All tutorials are listed in the {doc}`Python tutorials <../tutorials/index>`;
the main calls are summarised in the {doc}`Quick API <quick_api>`.

## Continue

- **Next:** choose a tutorial from the table above.
- **Go deeper:** {doc}`../foundations/concepts/calibrated_interval_semantics`
  (what the ranges of each mode guarantee, and what they do not).
- **See also:** {doc}`../practitioner/evaluate_ce` and
  {doc}`../foundations/how-to/integrate_with_pipelines`.
- **Before this:** {doc}`ce-tasks-and-modes` (Path C, step 1).
- **Elsewhere in the documentation:** see
  {ref}`Where should I go next? <quick-start-next>` on the Quick Start page.

Entry-point tier: Tier 1.
