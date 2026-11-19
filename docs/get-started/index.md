# Get started

<span id="where-ce-fits"></span>

<span id="quick-start-understand-explore-and-apply-ce"></span>

**Calibrated Explanations (CE)** is an open-source Python library that
provides uncertainty-aware explanations of individual predictions from
supervised machine-learning models. It wraps a classification or regression
model you already have, calibrates the model's outputs on labelled data the
model has not seen, and then explains each calibrated prediction, with a
range for the prediction and for every feature's weight.

This section takes you from the definition to an explanation of your own
data. The first two steps need **no installation**.

```{raw} html
<figure class="ce-figure">
  <a href="try-in-browser.html#qs-workflow" title="The workflow, explained step by step in the Quick Start">
    <picture>
      <source media="(max-width: 600px)" srcset="../_static/figures/ce-adds-to-workflow-narrow.svg">
      <img src="../_static/figures/ce-adds-to-workflow.svg" width="900" height="450" alt="Two aligned lanes share one fitted model. Lane 1, supervised prediction, in blue: the training set is used to fit a model, and the model predicts for a new case; this example baseline returns one value without uncertainty. Lane 2, workflow with CE, in orange: CE takes the same fitted model and a separate labelled calibration set, held out from training, calibrates, and predicts the same new case. It returns a calibrated prediction with its uncertainty, shown as probability bounds on a 0 to 1 scale for classification or as a prediction interval in the target's units for regression, and then factual and alternative explanations.">
    </picture>
  </a>
  <figcaption><strong>What CE adds to a supervised prediction workflow.</strong> The Quick Start explains each part of this figure with two worked cases.</figcaption>
</figure>
```

<span id="your-learning-journey"></span>

(choose-your-path)=

## Your path through this section

Every page ends with a link to the next.

1. **{doc}`What CE is <../what-is-ce>` (5 minutes).** The definition, the
   problem CE addresses, what it provides and what it does not.
2. **{doc}`Quick Start <try-in-browser>` (30 minutes, no installation).**
   Learn the CE workflow and read your first explanations, with one
   classification and one regression case. Start here if you read only one
   page.
3. **{doc}`Installation <installation>` (2 minutes).**
   `pip install "calibrated-explanations[viz]"`; the `viz` extra adds plots.
4. **{doc}`Read your first explanation <../foundations/how-to/interpret_explanations>` (15 minutes).**
   Which number is the prediction, which is a weight, and what each range is.
5. **{doc}`Apply CE to your own data <apply-to-your-data>` (30 minutes).**
   Split, wrap, calibrate, explain, check and save.
6. **{ref}`Next steps <quick-start-next>`**, below.

**Coming from SHAP or LIME?** {doc}`Map your workflow to CE <coming-from-shap-lime>`,
then see the {doc}`comparison with other methods <../compare>`.

**Prefer one worked prediction without code?** {doc}`CE by example <ce-by-example>`
follows a single prediction from the Python quickstart, with every number
explained.

<span id="which-ce-task-am-i-doing"></span>

## Which CE mode am I using?

| Your question | CE mode | Prediction call |
|---|---|---|
| Which class, and how probable? | Classification | `predict_proba(X, uq_interval=True)` |
| Which value, and within what range? | Interval regression | `predict(X, uq_interval=True)` |
| How probable is it that the value is at most *t*? | Probabilistic (thresholded) regression | `predict_proba(X, uq_interval=True, threshold=t)` |

Every mode explains with `explain_factual(X)` and `explore_alternatives(X)`.
The Quick Start introduces the three modes in
{ref}`Task, mode and capability <qs-task-mode-capability>`; the full account
is {doc}`Tasks, modes and capabilities <ce-tasks-and-modes>`. What each range
guarantees differs by mode: see
{doc}`Guarantees and limits by mode <../foundations/concepts/calibrated_interval_semantics>`.

<span id="reference-and-further-reading"></span>

(before-you-start)=

## Look things up

- The {doc}`Glossary <../glossary/index>` defines the terms.
- The {doc}`API reference <../api/index>` gives full signatures, and the
  {doc}`Quick API <quick_api>` the main calls on one page.
- {doc}`Troubleshooting <troubleshooting>` covers installation and runtime
  problems.

<span id="where-should-i-go-next"></span>

(quick-start-next)=

## Next steps

| I want to… | Go to |
|---|---|
| Understand the theory: why CE, calibration by task, guarantees and limits | {doc}`Understand CE <../sections/understand-ce>` |
| Practise in the browser with a guided scenario | {ref}`Decision Lab <try-decision-lab>` |
| Experiment with CE outputs in the browser | {ref}`Expert Lab <qs-expert-lab>` |
| Run the Python tutorials and task recipes | {doc}`CE in Practice <../sections/in-practice>` and the {doc}`Practitioner Hub <../practitioner/index>` |
| Integrate CE into an application, or understand and extend its code | {doc}`Software Architecture & Integration <../sections/software-integration>` |
| Find the research, how to cite CE, governance and support | {doc}`Project <../sections/project-evolution>` |

```{toctree}
:hidden:
:maxdepth: 1

What CE Is <../what-is-ce>
Quick Start <try-in-browser>
Installation <installation>
Read Your First Explanation <../foundations/how-to/interpret_explanations>
Apply CE to Your Own Data <apply-to-your-data>
Coming from SHAP or LIME <coming-from-shap-lime>
CE by Example (No Code) <ce-by-example>
```
