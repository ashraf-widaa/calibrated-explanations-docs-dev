# How-to guides

Each guide answers one practical task: what you need, the steps, and the
output to expect. The guides are grouped by what you want to achieve. The
concepts behind them are in {doc}`Understand CE <../../sections/understand-ce>`,
and exact signatures in the {doc}`API reference <../../api/index>`.

<span id="explaining-and-presenting-results"></span>

## Explain and visualize

- {doc}`interpret_explanations`: read rule tables, payloads and plots
  (step 4 of *Get started*).
- {doc}`plot_with_plotspec`: build and customise plots through PlotSpec.
- {doc}`to_narrative`: turn explanations into plain-text narratives.
- {doc}`../../practitioner/narrative_templates`: customise narrative templates.
- {doc}`export_explanations`: export explanations for storage or other tools.
- {doc}`../../practitioner/advanced/explanation_retrieval`: retrieve
  explanations by rule pattern and metadata for audits.

## Calibrate and evaluate

- {doc}`../../practitioner/playbooks/mondrian-calibration`: why and when to
  calibrate per group.
- {doc}`conditional_calibration`: configure conditional calibration (Mondrian
  `bins` or a categorizer).
- {doc}`../../practitioner/advanced/normalization-guide`: difficulty
  estimation and normalized intervals for heteroscedastic regression.
- {doc}`../../practitioner/evaluate_ce`: check probabilities, intervals,
  threshold events and subgroups on your own held-out data.

## Make decisions

- {doc}`../../practitioner/advanced/reject-policy`: reject-aware predictions
  and explanations.
- {doc}`../../practitioner/playbooks/ensured-explanations`: reduce epistemic
  uncertainty in alternative explanations.
- {doc}`../../practitioner/playbooks/decision-policies`: turn uncertainty into
  accept, reject or defer policies.

<span id="running-ce-in-production"></span>

## Deploy and operate

- {doc}`integrate_with_pipelines`: scikit-learn pipelines and fitted
  preprocessing.
- {doc}`safe-defaults`: recommended settings for production deployments.
- {doc}`configure_runtime`: runtime behaviour through the configuration
  manager.
- {doc}`tune_runtime_performance`: opt-in caching and parallelism; the
  {doc}`performance tuning guide <../../practitioner/performance-tuning>`
  adds profiling.
- {doc}`../../practitioner/advanced/parallel_execution_playbook`: choose a
  parallel explain strategy.
- {doc}`configure_telemetry`: optional telemetry and provenance records.
- {doc}`../../practitioner/advanced/use_plugins` and
  {doc}`../../practitioner/advanced/modality-plugins`: opt in to plugins and
  select them by modality.

## Consult compliance playbooks

These playbooks discuss how CE outputs relate to regulation. They keep their
documented scope and qualifications: they are not evidence of compliance.

- {doc}`../../practitioner/playbooks/eu-ai-act-compliance`
- {doc}`../../practitioner/playbooks/eu-data-liability-compliance`

```{toctree}
:hidden:
:maxdepth: 1

plot_with_plotspec
to_narrative
../../practitioner/narrative_templates
export_explanations
../../practitioner/advanced/explanation_retrieval
../../practitioner/playbooks/mondrian-calibration
conditional_calibration
../../practitioner/advanced/normalization-guide
../../practitioner/evaluate_ce
../../practitioner/advanced/reject-policy
../../practitioner/playbooks/ensured-explanations
../../practitioner/playbooks/decision-policies
integrate_with_pipelines
safe-defaults
configure_runtime
tune_runtime_performance
../../practitioner/performance-tuning
../../practitioner/advanced/parallel_execution_playbook
configure_telemetry
../../practitioner/advanced/use_plugins
../../practitioner/advanced/modality-plugins
../../practitioner/playbooks/eu-ai-act-compliance
../../practitioner/playbooks/eu-data-liability-compliance
```
