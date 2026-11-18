# Quick Start — Understand, Explore and Apply CE

**Calibrated Explanations (CE)** is an open-source Python library for
scikit-learn-style classification and regression models. It calibrates a
model's outputs on held-out data, can report lower and upper bounds for each
prediction, and explains each prediction with a range for every feature's
weight.

**What CE gives you**

- **Predictions from calibrated outputs.** For classification, a merged
  probability estimate and two Venn–Abers values. For interval regression,
  a numeric prediction with a target-value interval; for probabilistic
  regression, an event-probability estimate with reported bounds.
- **Factual explanations.** The feature conditions behind one prediction,
  each with a weight and a range for that weight.
- **Alternative explanations.** What the calibrated prediction would be if
  one feature had a different value.
- **Your own model.** CE wraps scikit-learn-style classifiers and regressors,
  trained or not, and leaves the model itself unchanged.

The pair, merged estimate and explanation ranges have different statistical
qualifications. These depend on the task and calibration protocol, including
held-out calibration data and exchangeability. See the
{doc}`semantics reference <../foundations/concepts/calibrated_interval_semantics>`;
exact validity wording remains under CE author review.

This Quick Start gives the big picture and one learning journey through the
documentation; its first step needs no code.


## Where CE fits

```{raw} html
<figure class="ce-figure">
  <a href="why-ce.html" title="Why CE: the full workflow, explained">
    <picture>
      <source media="(max-width: 600px)" srcset="../_static/figures/ce-at-a-glance-narrow.svg">
      <img src="../_static/figures/ce-at-a-glance.svg" width="760" height="276" alt="In blue, a conventional workflow: labelled data, train a model, predict a label or a score. In orange, what CE adds: part of the labelled data is held out as a calibration set; CE uses it to calibrate the trained model's outputs (the model itself is unchanged), explains each prediction, and returns a calibrated prediction and an explanation, each with a range.">
    </picture>
  </a>
  <figcaption>Blue: a conventional ML workflow. Orange: what CE adds. Schematic; the full workflow is explained in <a href="why-ce.html">Why CE</a>.</figcaption>
</figure>
```

Follow the arrows from labelled data through training to prediction: these
are the conventional steps. The branch labelled **Calibration set** supplies
held-out examples to **Calibrate**, and **Explain** uses the calibrated
outputs to construct explanations. The final box groups the prediction and
explanation, each with a reported range. These ranges describe different
quantities; their meaning depends on the task and output, as the paths below
explain. CE adds these steps without retraining your model.

(choose-your-path)=

## Your learning journey

Follow these five steps in order. Each page ends with a link to the next one.

1. **{doc}`CE by example <ce-by-example>`: start here (no code, about 15
   minutes).** One real prediction, from the model's raw score to a
   calibrated probability, a factual explanation and alternatives, with every
   number taken from an executed CE run.
2. **{doc}`Python walkthrough <quickstart_walkthrough>` (about 45 minutes).**
   Run the same example yourself, step by step, with the code and real output.
   Install the package first: {doc}`installation` (Python 3.10 or later, with
   the `viz` extra for plots).
3. **{doc}`How to read CE explanations <../foundations/how-to/interpret_explanations>`.**
   What each field of the returned records and plots means, and which range
   belongs to which quantity.
4. **{doc}`Apply CE to your own data <apply-to-your-data>`.** Wrap your own
   model, calibrate, explain, check and save.
5. **{doc}`Evaluate CE on your own data <../practitioner/evaluate_ce>`.**
   Empirical checks of probabilities, intervals, threshold events and
   subgroups on held-out data.

**Prefer to start with code?** The {doc}`Quick API <quick_api>` page has a
complete minimal example you can copy and run in one go; it uses the same
case as steps 1 and 2.

**Want the reasons first?** {doc}`Why CE <why-ce>` explains what changes in a
machine-learning workflow when CE is added, and
{doc}`Tasks, modes and capabilities <ce-tasks-and-modes>` helps you decide
whether CE fits your problem.

(before-you-start)=

## Reference and further reading

- **Look things up:** the {doc}`Glossary <../glossary/index>` defines the terms,
  and the {doc}`API reference <../api/index>` gives full signatures.
- **Go deeper:** {doc}`../foundations/concepts/ce_workflow` gives a learning
  path from intuition to the mathematics. Guarantees are mode-specific; the
  canonical statement is {doc}`../foundations/concepts/calibrated_interval_semantics`.
- **Try it in the browser:** the
  [interactive web demo](https://calibrated-explanations-demo.ju.se/) shows CE
  without installing anything.

(quick-start-next)=

## Where should I go next?

| Section | Go there to |
|---|---|
| {doc}`CE: What & Why <../sections/what-and-why>` | Understand why trusting AI outputs is hard, what CE adds and how it compares with other methods |
| {doc}`How CE Works <../sections/how-ce-works>` | Study the theory: calibration methods, guarantees by mode and how explanations are built |
| {doc}`CE in Practice <../sections/in-practice>` | Run the Python tutorials, try the demos, follow task guides and evaluate CE on your data |
| {doc}`CE Software & Integration <../sections/software-integration>` | Install, look up the API, integrate CE into pipelines and fix problems |
| {doc}`Project & Resources <../sections/project-evolution>` | Find the research and publications, how to cite CE, the roadmap and how to contribute |
| [Commercial Services](https://grejna.ai/#kontakt) | Contact Grejna AB for customized CE solutions and commercial support, separate from the open-source library and its license |

```{toctree}
:hidden:
:maxdepth: 1

CE by Example <ce-by-example>
```
