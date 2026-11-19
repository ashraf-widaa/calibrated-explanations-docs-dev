# Practitioner Hub

Install CE, run worked Python examples and apply the CE workflow on your own
machine. New to CE? Read the {doc}`Quick Start <../get-started/try-in-browser>`
first; it needs no installation and explains every output used below.

## 1. Install

You need Python 3.10 or later and a scikit-learn-style model (`fit` and
`predict`; a classifier also needs `predict_proba`).

```bash
pip install "calibrated-explanations[viz]"
```

The `viz` extra adds the plots. Other options, conda and a check that the
installation works are in {doc}`Installation <../get-started/installation>`;
problems are covered in {doc}`Troubleshooting <../get-started/troubleshooting>`.

## 2. Run the worked examples

| Example | What you get |
|---|---|
| {doc}`Python quickstart <../get-started/quickstart>` | One classification example, step by step, in about 10 minutes |
| The {doc}`Quick Start <../get-started/try-in-browser>` code | Its code blocks run as written in one Python session: the diabetes and housing cases, including the threshold question |
| {doc}`Classification tutorial <../get-started/quickstart_classification>` | Binary and multiclass classification, probabilities and their ranges, factual and alternative explanations |
| {doc}`Regression tutorial <../get-started/quickstart_regression>` | Prediction intervals (interval regression) and threshold probabilities (thresholded regression) from one model |
| {doc}`Guarded explanations tutorial <../get-started/quickstart_guarded>` | Explanations restricted to typical feature values |

All tutorials are listed, with a suggested order, in
{doc}`Python tutorials <../tutorials/index>`.

<span id="core-path"></span><span id="optional-tools"></span>

## 3. Apply the workflow to your own data

1. {doc}`Apply CE: the practical workflow <../get-started/apply-overview>`:
   the decisions to make before you write code.
2. {doc}`Apply CE to your own data <../get-started/apply-to-your-data>`:
   split, wrap, calibrate, explain, check and save.
3. {doc}`Evaluate CE on your own data <evaluate_ce>`: are the probabilities
   calibrated and the intervals wide enough on *your* held-out data?
4. {doc}`Task API comparison <task_api_comparison>`: choose between the
   wrapper and lower-level calls.

## Recipes

| I want to… | Recipe |
|---|---|
| Generate "what if" alternatives | {doc}`../foundations/concepts/alternatives` |
| Plot an explanation and read the plot | {doc}`../foundations/how-to/plot_with_plotspec`, {doc}`../foundations/how-to/interpret_explanations` |
| Turn an explanation into text | {doc}`../foundations/how-to/to_narrative` |
| Export explanations to JSON or a table | {doc}`../foundations/how-to/export_explanations` |
| Calibrate per group | {doc}`../practitioner/playbooks/mondrian-calibration` |
| Deploy in a pipeline | {doc}`../foundations/how-to/integrate_with_pipelines` |

Every recipe is listed by goal in the {doc}`How-to guides <../foundations/how-to/index>`.
Semantics and non-guarantees are documented in
{doc}`Guarantees and limits by mode <../foundations/concepts/calibrated_interval_semantics>`.

```{toctree}
:maxdepth: 1
:hidden:

Python Quickstart <../get-started/quickstart>
Apply CE: The Practical Workflow <../get-started/apply-overview>
Task API Comparison <task_api_comparison>
```
