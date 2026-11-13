# Python tutorials

Executable, step-by-step tutorials for the CE Python library. Every code block
on these pages runs as shown, and every printed output is the real output,
checked by the documentation tests.

**Before these tutorials.** For the ideas without code, start with the
{doc}`Quick Start <../get-started/index>`: {doc}`../get-started/why-ce`,
{doc}`CE by example <../get-started/ce-by-example>`,
{doc}`../get-started/ce-tasks-and-modes` and
{doc}`../get-started/apply-overview`.

| Tutorial | Who it is for | You will be able to |
|---|---|---|
| {doc}`Python walkthrough <../get-started/quickstart_walkthrough>` | Anyone learning CE with code, step by step | Follow one binary-classification case from data to calibrated probabilities, explanations and alternatives, and know what you can and cannot conclude; a notebook is available |
| {doc}`Classification tutorial <../get-started/quickstart_classification>` | Practitioners with a classifier | Calibrate a classifier and read calibrated probabilities, their ranges, factual explanations and alternatives (multiclass example) |
| {doc}`Regression tutorial <../get-started/quickstart_regression>` | Practitioners with a regression model | Get prediction intervals (interval regression) and threshold probabilities (probabilistic regression) from one calibrated model |
| {doc}`Guarded explanations tutorial <../get-started/quickstart_guarded>` | Users who need explanations restricted to typical feature values | Add guarded options to an explanation call and read the guard's audit |
| {doc}`Apply CE to your own data <../get-started/apply-to-your-data>` | Practitioners integrating CE into their own work | Wrap an existing model, calibrate, explain, check on a test set, save and reload; includes a reviewable prompt for AI coding assistants |

Guarantees are mode-specific; the canonical statement is
{doc}`../foundations/concepts/calibrated_interval_semantics`.

**After the tutorials:** {doc}`../practitioner/evaluate_ce` (evaluate CE on your
own data), {doc}`../foundations/how-to/integrate_with_pipelines` and the
{doc}`Quick API <../get-started/quick_api>`.

```{toctree}
:hidden:
:maxdepth: 1

Python walkthrough <../get-started/quickstart_walkthrough>
Classification tutorial <../get-started/quickstart_classification>
Regression tutorial <../get-started/quickstart_regression>
Guarded explanations tutorial <../get-started/quickstart_guarded>
Apply CE to your own data <../get-started/apply-to-your-data>
```

Entry-point tier: Tier 1.
