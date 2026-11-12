# Quick Start — Understand, Explore and Apply CE

**Calibrated Explanations (CE)** is a Python library that works with your
classification or regression model. It calibrates the model's predictions on
data the model has not seen, gives each prediction a range (a lower and an
upper value), and explains each prediction with a range for every feature's
contribution.

## Where CE fits

```{raw} html
<figure class="ce-figure">
  <a href="../_static/figures/ce-in-ml-workflow.svg" title="Open the figure at full size">
    <picture>
      <source media="(max-width: 600px)" srcset="../_static/figures/ce-in-ml-workflow-narrow.svg">
      <img src="../_static/figures/ce-in-ml-workflow.svg" width="1000" height="540" alt="In blue, a conventional workflow: labelled data is split into training and test sets, a model is trained (or an existing one is used), it predicts a label or a raw score, and it is evaluated on the test set. In orange, what CE adds: a calibration set held out from training, a Calibrate step (Venn-Abers predictors or conformal predictive systems) and an Explain step (factual and alternative explanations). CE returns a calibrated prediction with a lower and upper value and an explanation whose rules and weights each have a range; both are evaluated and interpreted on the test set.">
    </picture>
  </a>
  <figcaption>Blue: a conventional supervised ML workflow. Orange: what CE adds. Select the figure to enlarge it.</figcaption>
</figure>
```

You keep your model and your training. CE adds three things: a **calibration
set** held out from training, a **Calibrate** step and an **Explain** step.
In return, every prediction and every explanation comes with a range. (This
is a simplified teaching picture: a conventional workflow can also add a
calibration or an explanation tool; CE combines both around one calibrated
model.)

## Choose your path

::::{grid} 1 1 3 3
:gutter: 3

:::{grid-item-card} A · Understand CE
:link: why-ce
:link-type: doc

**Why is CE needed, and what changes in the workflow?** For newcomers,
students and decision-makers. No code.
:::

:::{grid-item-card} B · Learn CE by example
:link: quickstart_walkthrough
:link-type: doc

**How does CE work in practice?** Follow one case from code to real output to
interpretation, with Python you can run.
:::

:::{grid-item-card} C · Apply CE to your data
:link: ce-tasks-and-modes
:link-type: doc

**Does CE fit my problem, and how do I use it?** Tasks, modes, quickstarts
and an integration guide. For practitioners with a model.
:::
::::

**Recommended order:** A → B → C. Each path also stands on its own: if you
already know machine learning and CE's ideas, go straight to B; if you only
need to know whether CE fits your problem, start with C.

## Before you start

- **Install:** `pip install calibrated-explanations` (Python 3.10 or later);
  see {doc}`installation`.
- **Look things up:** the {doc}`Quick API <quick_api>` lists the main calls,
  the {doc}`Glossary <../glossary/index>` defines the terms, and the
  {doc}`API reference <../api/index>` gives full signatures.
- **Go deeper:** {doc}`../foundations/concepts/ce_workflow` gives a learning
  path from intuition to the mathematics. Guarantees are mode-specific; the
  canonical statement is {doc}`../foundations/concepts/calibrated_interval_semantics`.
- **Try it in the browser:** the
  [interactive web demo](https://calibrated-explanations-demo.ju.se/) shows CE
  without installing anything.

```{toctree}
:hidden:
:maxdepth: 1

A1 · Machine learning essentials <ml-foundations>
A2 · Why CE: from a conventional to a CE workflow <why-ce>
B · Guided Python walkthrough <quickstart_walkthrough>
C1 · Tasks, modes and capabilities <ce-tasks-and-modes>
C2 · Classification quickstart <quickstart_classification>
C3 · Regression quickstart <quickstart_regression>
C4 · Guarded explanations <quickstart_guarded>
C5 · Apply CE to your own data <apply-to-your-data>
Quick API <quick_api>
```

Entry-point tier: Tier 1.
