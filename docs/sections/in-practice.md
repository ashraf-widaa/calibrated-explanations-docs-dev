# CE in Practice: Explore & Apply

Try CE interactively, follow task guides and playbooks, and apply CE to your
own models.

A practical route runs from the executable Python tutorials, through applying
and evaluating CE on your own data, to the task guides and playbooks for
specific decisions. The browser demos offer a hands-on view without
installation. Demos and games illustrate how CE works; they do not validate CE
for your data. Mode-specific guarantees and their assumptions are stated in
{doc}`../foundations/concepts/calibrated_interval_semantics`.

## Run CE in Python

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Python Tutorials
:link: ../tutorials/index
:link-type: doc

Executable step-by-step tutorials with real output: the Python walkthrough, classification, regression, guarded explanations and applying CE to your own data.
:::

:::{grid-item-card} Example Notebooks
:link: https://github.com/Moffran/calibrated_explanations/tree/main/notebooks
:link-type: url

Executable demos on GitHub: binary and multiclass classification, regression, probabilistic regression and advanced topics.
:::
::::

## Apply and evaluate

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Use CE on Your Own Data
:link: ../get-started/apply-to-your-data
:link-type: doc

Follow the complete fit, calibrate, predict, explain and evaluate workflow.
For preprocessing details, continue to the pipeline integration guide.
:::

:::{grid-item-card} Evaluate CE on Your Data
:link: ../practitioner/evaluate_ce
:link-type: doc

Reproducible set-up, checks of calibrated outputs on held-out data, common mistakes and when not to trust the outputs.
:::

:::{grid-item-card} Tasks and Capabilities
:link: ../tasks/index
:link-type: doc

Classification, regression and probabilistic regression, with a capability map.
:::

:::{grid-item-card} Practitioner Hub
:link: ../practitioner/index
:link-type: doc

Interpretation, API choice, evaluation and playbooks for decision policies, ensured explanations, Mondrian calibration and regulatory context.
:::

:::{grid-item-card} Comparison with Other Methods
:link: ../compare
:link-type: doc

A short comparison of CE with SHAP, LIME and conformal prediction packages.
:::
::::

## Explore in the browser

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Interactive CE App
:link: https://calibrated-explanations-demo.ju.se/
:link-type: url

A browser companion to the Python package, with a guided workflow and an expert interface. Under active development.
:::

:::{grid-item-card} Expert Hub
:link: https://calibrated-explanations-demo.ju.se/expert
:link-type: url

Step through project setup, calibration, explanation and prediction in the browser, with built-in or your own data.
:::

:::{grid-item-card} Decision Lab Games
:link: https://games.grejna.ai/
:link-type: url

Teaching games from Grejna about decisions under uncertainty. Educational; their outputs are not real-world guarantees.
:::
::::
