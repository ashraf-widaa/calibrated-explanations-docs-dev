# Use CE: CE in Practice

<span id="ce-in-practice-explore-apply"></span>

*Where can I follow an example, try CE in my browser, or use it in Python?*

This section helps you complete a task with CE. Work through it in order:
learn the workflow, practise in the browser, then run CE in Python. Demos and
games illustrate how CE works; they do not validate CE for your data.
Mode-specific guarantees and their assumptions are stated in
{doc}`Guarantees and limits by mode <../foundations/concepts/calibrated_interval_semantics>`.

<span id="expert-hub-inspect-ce-in-the-browser"></span><span id="decision-lab-decide-under-uncertainty"></span><span id="practitioner-hub-run-and-apply-ce"></span>

<span id="explore-in-the-browser"></span>

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} 1. Quick Start
:link: ../get-started/try-in-browser
:link-type: doc

Understand what CE adds, choose your task and create your first explanation:
in the browser with no installation, or in Python.
:::

:::{grid-item-card} 2. Decision Lab
:link: try-decision-lab
:link-type: ref

Follow a guided browser scenario (Mission Control, lesson 4; Precision Works
for regression) and use calibrated advice to decide. Teaching games from
Grejna, powered by CE Enterprise; their outputs are not real-world guarantees.
:::

:::{grid-item-card} 3. Expert Hub
:link: qs-expert-lab
:link-type: ref

Experiment in the browser with the built-in datasets (Diabetes, Iris,
California Housing) or your own: calibrate, explain and explore
alternatives in all three CE modes.
:::

:::{grid-item-card} 4. Practitioner Hub
:link: ../practitioner/index
:link-type: doc

Install CE, run {doc}`Your First CE Explanation in Python <../get-started/first-explanation-python>`
and the tutorials, and apply the workflow on your own machine.
:::
::::

<span id="run-ce-in-python"></span><span id="apply-and-evaluate"></span>

## Python tutorials and task pages

- {doc}`Python tutorials <../tutorials/index>`: executable tutorials for
  classification, regression (interval and thresholded) and guarded
  explanations, every output checked by the documentation tests.
- {doc}`Tasks and capabilities <../tasks/index>`: one page per task, with
  the API calls and a capability map.
- [Example notebooks](https://github.com/Moffran/calibrated_explanations/tree/main/notebooks)
  on GitHub: binary and multiclass classification, regression, probabilistic
  regression and advanced topics.

## How-to guides by goal

{doc}`How-to guides <../foundations/how-to/index>` give prerequisites, steps
and expected output for one task each, grouped by what you want to achieve:

| Goal | Guides |
|---|---|
| **Explain and visualize** | interpretation, plots, narratives, export |
| **Calibrate and evaluate** | Mondrian (conditional) calibration, normalization, evaluation on held-out data |
| **Make decisions** | reject policies, ensured explanations, decision policies |
| **Deploy and operate** | pipelines, safe defaults, runtime configuration, performance, parallel execution, telemetry, plugins |
| **Consult compliance playbooks** | EU AI Act, EU data and liability regulation |

Choosing between CE and other explanation methods is covered in
{doc}`Comparison with other methods <../compare>`. What an output means for
your task is covered in {doc}`Understand CE <understand-ce>`.

**Next section:** {doc}`Software Architecture & Integration <software-integration>`.

```{toctree}
:hidden:
:maxdepth: 2

Decision Lab (browser) <https://games.grejna.ai/>
Expert Hub (browser) <https://calibrated-explanations-demo.ju.se/expert>
Practitioner Hub <../practitioner/index>
Python Tutorials <../tutorials/index>
Tasks and Capabilities <../tasks/index>
How-to Guides <../foundations/how-to/index>
```
