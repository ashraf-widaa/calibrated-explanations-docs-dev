# CE in Practice: Explore & Apply

Try CE interactively, then generate, plot and export explanations for your
own task.

Read this section in order: explore CE in the **Expert Hub**, practise
decisions under uncertainty in the **Decision Lab**, then use the
**Practitioner Hub** for runnable task examples and recipes. Demos and games
illustrate how CE works; they do not validate CE for your data. Mode-specific
guarantees and their assumptions are stated in
{doc}`../foundations/concepts/calibrated_interval_semantics`.

The {doc}`browser Quick Start <../get-started/try-in-browser>` walks through
both labs with a classification and a regression example side by side.

<span id="explore-in-the-browser"></span>

## 1. Expert Hub: inspect CE in the browser

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Expert Hub
:link: https://calibrated-explanations-demo.ju.se/expert
:link-type: url

Load a built-in dataset (Diabetes, Iris or California Housing) or your own,
then step through **Project**, **Prepare & Calibrate**, **Explain** and
**Predict**. Under active development.
:::

:::{grid-item-card} Guided walkthrough of both examples
:link: ../get-started/try-in-browser
:link-type: doc

Classification and regression in parallel: data, calibration, prediction
with uncertainty, a factual explanation and one alternative, each with code,
output and how to read it.
:::
::::

## 2. Decision Lab: decide under uncertainty

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Decision Lab Games
:link: https://games.grejna.ai/
:link-type: url

Teaching games from Grejna. An assistant offers calibrated advice; you
decide. Educational; their outputs are not real-world guarantees.
:::

:::{grid-item-card} Two scenarios to start with
:link: try-decision-lab
:link-type: ref

Port Authority (CLEAR, HOLD or INSPECT a ship) and Mission Control (send a
rover or stop): decide, inspect the uncertainty and explanation, reconsider.
:::
::::

<span id="run-ce-in-python"></span><span id="apply-and-evaluate"></span>

## 3. Practitioner Hub: run and apply CE

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Practitioner Hub
:link: ../practitioner/index
:link-type: doc

Runnable task examples and recipes: generate, plot, narrate and export
explanations, choose an API style, and follow production playbooks.
:::

:::{grid-item-card} Python Tutorials
:link: ../tutorials/index
:link-type: doc

Executable step-by-step tutorials with real output for classification,
regression, guarded explanations and your own data.
:::

:::{grid-item-card} Tasks and Capabilities
:link: ../tasks/index
:link-type: doc

Classification, regression and probabilistic regression, with a capability map.
:::

:::{grid-item-card} How-to Guides
:link: ../foundations/how-to/index
:link-type: doc

Short recipes: plotting, exporting, narratives, conditional calibration and
runtime settings.
:::

:::{grid-item-card} Use CE on Your Own Data
:link: ../get-started/apply-to-your-data
:link-type: doc

The complete fit, calibrate, predict, explain and evaluate workflow.
:::

:::{grid-item-card} Evaluate CE on Your Data
:link: ../practitioner/evaluate_ce
:link-type: doc

Checks of calibrated outputs on held-out data, common mistakes and when not
to trust the outputs.
:::

:::{grid-item-card} Example Notebooks
:link: https://github.com/Moffran/calibrated_explanations/tree/main/notebooks
:link-type: url

Executable demos on GitHub: binary and multiclass classification, regression,
probabilistic regression and advanced topics.
:::
::::

Choosing between CE and other explanation methods is covered once, in
{doc}`Comparison with other methods <../compare>` (*CE: What & Why*). What
an output means for your task is covered in {doc}`How CE Works <how-ce-works>`.

**Next section:** {doc}`CE Software & Integration <software-integration>`.

```{toctree}
:hidden:
:maxdepth: 2

Expert Hub (browser) <https://calibrated-explanations-demo.ju.se/expert>
Decision Lab (browser) <https://games.grejna.ai/>
Practitioner Hub <../practitioner/index>
Python Tutorials <../tutorials/index>
Tasks and Capabilities <../tasks/index>
How-to Guides <../foundations/how-to/index>
Apply CE: The Practical Workflow <../get-started/apply-overview>
```
