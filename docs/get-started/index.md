# Quick Start — Understand, Explore and Apply CE

**Calibrated Explanations (CE)** is a Python library that works with an
already-trained classification or regression model. It calibrates the model's
predictions on data the model has not seen, attaches an uncertainty range to
each prediction, and explains each prediction with an uncertainty range for
every feature's contribution. This Quick Start helps you understand where CE
fits into an ML workflow, explore a working example, and apply CE to your own
data.

## Where CE fits

```{figure} ../_static/figures/ce-in-ml-workflow.svg
:alt: Labelled data is split into training, calibration and test sets. The model is trained (or an existing one is used). CE takes the trained model and the calibration set, calibrates with Venn-Abers (classification) or conformal predictive systems (regression), explains with factual and alternative explanations, and produces calibrated predictions with a lower and upper value and explanations with ranges, which are interpreted and evaluated on the test set.
:width: 560px
:align: center
:target: ../_static/figures/ce-in-ml-workflow.svg

Where CE fits: grey steps are part of a conventional supervised ML workflow; purple parts are added by CE.
```

CE adds a calibration set, wraps the model you train (or already have), and
returns calibrated predictions and explanations with uncertainty. This is a
simplified teaching picture: conventional workflows can also add calibration
or explanation tools; CE combines both around one calibrated model.

## Choose your path

::::{grid} 1 1 3 3
:gutter: 3

:::{grid-item-card} A · Understand CE
:link: why-ce
:link-type: doc

**Why is CE needed, and how does a CE workflow differ from a conventional
one?** For newcomers to CE, students and decision-makers. No code.
:::

:::{grid-item-card} B · Learn CE by example
:link: quickstart_walkthrough
:link-type: doc

**How does CE work in practice?** Follow one case from code to real output to
interpretation. For anyone who wants to see CE run.
:::

:::{grid-item-card} C · Apply CE to your data
:link: ce-tasks-and-modes
:link-type: doc

**What does CE support, and how do I use it on my problem?** Tasks, modes,
limitations and task quickstarts. For practitioners with a model or a
prediction problem.
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
