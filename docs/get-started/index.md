# Quick Start

## CE in 60 seconds

**Calibrated Explanations (CE)** is a Python library that adds two things to
a trained prediction model: **probabilities you can rely on**, with an honest
range of uncertainty, and **explanations** of what each prediction depends on.

Here is what that looks like for one patient sample in the walkthrough, where
a model decides whether a breast tumour is *malignant* or *benign*:

| Question | What the model alone gives | What CE adds |
|---|---|---|
| What is predicted? | *malignant* | *malignant*, with a calibrated probability of *benign* of 0.29, between 0.17 and 0.33 |
| Why? | — | The strongest reason is `worst concave points > 0.14`: compared with other values of that feature, it lowers the probability of *benign* by about 0.19 |
| What would change it? | — | If `worst concave points` were below 0.14, the model's probability of *benign* would rise to about 0.48 |

The probability is **calibrated** on data the model never saw, and the range
around it shows how firmly that data supports it; step 2 explains exactly
what is guaranteed and under which assumption. The explanations describe the
model's behaviour; they do not prove cause and effect. You will produce every
number above yourself in step 3.

## How this Quick Start works

It takes you from the basic ideas of machine learning to running and
interpreting calibrated explanations on a real model. Follow the three steps
in order, or skip ahead if you already know the material.

```{mermaid}
flowchart LR
    A["1. Machine learning basics<br/>tasks, models, data splits"] --> B["2. CE tasks and outputs<br/>what CE supports and what outputs mean"]
    B --> C["3. Practical walkthrough<br/>train, calibrate, explain, interpret"]
    C --> D["Go deeper<br/>foundations and task guides"]
```

## Your learning path

| Step | Page | You will learn | Time |
|---|---|---|---|
| 1 | {doc}`ml-foundations` | Features and targets, prediction tasks, model families, training versus calibration, and why predictions alone are not enough | 10 min read |
| 2 | {doc}`ce-tasks-and-modes` | Which tasks CE supports, what it can do for each, and how to read its outputs | 10 min read |
| 3 | {doc}`quickstart_walkthrough` | A notebook-style, step-by-step classification example with real outputs and interpretation | 20 min hands-on |

Already know machine learning? Start at step 2. Already know CE's modes? Go
straight to the walkthrough, or use the {doc}`60-second decision tree
<../getting_started_60s>` to pick a task-specific quickstart.

Want to explore the concepts before installing the package?
[Open the interactive web demo](https://calibrated-explanations-demo.ju.se/),
then return here to run the walkthrough locally.

## Task-specific quickstarts

Short, code-first pages for when you know which mode you need:

- {doc}`quickstart_classification`: binary and multiclass classification.
- {doc}`quickstart_regression`: interval and probabilistic regression.
- {doc}`quickstart_guarded`: guarded (in-distribution) explanations.

For fast routing, use {doc}`../getting_started_60s`.
For method signatures, use {doc}`quick_api`.
For interpretation, use {doc}`../foundations/how-to/interpret_explanations`.

Semantics are mode-specific. The canonical reference is
{doc}`../foundations/concepts/calibrated_interval_semantics`.

## After the Quick Start

- {doc}`How CE calibrates <../foundations/concepts/calibration_methods>`: the methods behind the calibrated
  outputs you just produced.
- {doc}`CE Software & Integration <../sections/software-integration>`: installation, the Python API and
  integration with your own models and pipelines.
- {doc}`Practitioner hub <../practitioner/index>`: playbooks for applying CE to real tasks.

## Setup and help

- {doc}`installation`
- {doc}`troubleshooting`
- {doc}`Glossary <../glossary/index>`: short definitions of CE terms.

```{toctree}
:maxdepth: 1

Step 1: Machine learning basics <ml-foundations>
Step 2: CE tasks and outputs <ce-tasks-and-modes>
Step 3: Practical walkthrough <quickstart_walkthrough>
Shortcut: 60-second decision tree <../getting_started_60s>
quickstart_classification
quickstart_regression
quickstart_guarded
quick_api
```

Entry-point tier: Tier 1.
