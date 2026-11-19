# Practitioner hub

Runnable task examples and recipes for using CE on real tasks. New to CE?
Try it first in the browser with the
{doc}`browser Quick Start <../get-started/try-in-browser>` (Expert Hub and
Decision Lab), then come back here.

## Recipes

| I want to… | Recipe |
|---|---|
| Generate a factual explanation for a classifier | {doc}`../get-started/quickstart_classification` |
| Generate an explanation with a prediction interval for a regressor | {doc}`../get-started/quickstart_regression` |
| Generate "what if" alternatives | {doc}`../foundations/concepts/alternatives` |
| Plot an explanation and read the plot | {doc}`../foundations/how-to/plot_with_plotspec`, {doc}`../foundations/how-to/interpret_explanations` |
| Turn an explanation into text | {doc}`../foundations/how-to/to_narrative` |
| Export explanations to JSON or a table | {doc}`../foundations/how-to/export_explanations` |
| Check CE on my own held-out data | {doc}`evaluate_ce` |

## Core path

1. Run {doc}`../get-started/quickstart_classification` or
   {doc}`../get-started/quickstart_regression`.
2. Read {doc}`../foundations/how-to/interpret_explanations`.
3. Check CE on your own held-out data with {doc}`evaluate_ce`.
4. Choose API style in {doc}`task_api_comparison`.
5. Apply production workflows in {doc}`playbooks/index`.

Semantics and non-guarantees are documented in
{doc}`../foundations/concepts/calibrated_interval_semantics`.

## Optional tools

Use {doc}`advanced/index` only when you need performance, telemetry, or plugin
extensions.

```{toctree}
:maxdepth: 1
:hidden:

task_api_comparison
playbooks/index
advanced/index
narrative_templates
```
