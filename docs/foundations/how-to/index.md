# How-to guides

Practical recipes for integrating calibrated explanations into production.
Each guide answers one task; the concepts behind them are in
{doc}`How CE Works <../../sections/how-ce-works>`.

## Explaining and presenting results

- {doc}`interpret_explanations`: read rule tables, payloads and plots.
- {doc}`conditional_calibration`: calibrate separately per group (Mondrian
  `bins` or a categorizer).
- {doc}`to_narrative`: turn explanations into plain-text narratives.
- {doc}`export_explanations`: export explanations for storage or other tools.
- {doc}`plot_with_plotspec`: build and customise plots through PlotSpec.

## Running CE in production

- {doc}`integrate_with_pipelines`: use CE with scikit-learn pipelines and
  fitted preprocessing.
- {doc}`configure_runtime`: configure runtime behaviour through the
  configuration manager.
- {doc}`safe-defaults`: recommended settings for production deployments.
- {doc}`configure_telemetry`: optional telemetry and provenance records.
- {doc}`tune_runtime_performance`: opt-in caching and parallel execution.

```{toctree}
:hidden:
:maxdepth: 1

configure_telemetry
configure_runtime
conditional_calibration
safe-defaults
export_explanations
to_narrative
plot_with_plotspec
tune_runtime_performance
```
