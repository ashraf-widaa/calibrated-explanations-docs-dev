# Software & Technical Glossary

Short definitions of the CE library's objects, methods, parameters and
configuration. Each entry links to a guide or to the API reference, where the
full signature lives. For the theory behind these terms, see the
{doc}`science`. For all terms in one list, see the {doc}`Glossary <index>`.

## Core objects

```{glossary}
:sorted:

AlternativeExplanation
  The class of a single alternative explanation. It provides the ensured
  filters, such as `ensured_explanations()`, and plotting. For the concept, see
  {term}`Alternative explanation`.

  **API:** {doc}`../api/calibrated_explainer` (section AlternativeExplanation)

AlternativeExplanations
  The collection returned by {term}`explore_alternatives`, holding one
  {term}`AlternativeExplanation` per explained instance.

  **API:** {doc}`AlternativeExplanations <../_autosummary/calibrated_explanations.explanations.AlternativeExplanations>`

CalibratedExplainer
  The core CE class. It takes an already fitted model and calibration data,
  fits Venn-Abers calibrators for classification or conformal predictive
  systems for regression, and produces calibrated predictions and
  explanations. Most code should use {term}`WrapCalibratedExplainer`.

  **API:** {doc}`../api/calibrated_explainer` (section CalibratedExplainer)

CalibratedExplanations
  The collection returned by {term}`explain_factual`, with one explanation per
  explained instance. It can be iterated, indexed, plotted and exported.

  **API:** {doc}`../api/calibrated_explainer` (section CalibratedExplanations)

ExplainerConfig
  Typed configuration for building a configured {term}`WrapCalibratedExplainer`
  with `WrapCalibratedExplainer.from_config(config)`. It is usually built with
  `ExplainerBuilder`, and it switches on opt-in features such as the
  {term}`calibrator cache <Calibrator cache>`.

  **Learn more:** {doc}`../foundations/how-to/tune_runtime_performance`

FactualExplanation
  The class of a single factual explanation: the calibrated prediction, its
  rules and feature weights, and their uncertainty intervals. For the concept,
  see {term}`Factual explanation`.

  **API:** {doc}`../api/calibrated_explainer` (section FactualExplanation)

GuardedOptions
  Options that switch on guarded explanations and tune the guard: `confidence`
  (default 0.9), `n_neighbors`, `normalize`, `merge_adjacent` and `verbose`.
  Pass them as `guarded_options=` to `explain_factual` or
  `explore_alternatives`. Experimental; see
  {term}`Guarded explanation`.

  **Learn more:** {doc}`../foundations/concepts/guarded_explanations`

RejectResult
  The result object returned by {term}`predict` or {term}`predict_proba` when
  a {term}`reject policy <Reject policy>` other than `NONE` is set. It holds the
  prediction together with reject metadata, such as which instances matched
  the policy.

  **Learn more:** {doc}`../practitioner/advanced/reject-policy`

WrapCalibratedExplainer
  The recommended entry point to CE. It wraps a model with a scikit-learn
  interface: call {term}`fit` on the proper training set, then
  {term}`calibrate`, before requesting calibrated predictions or explanations.

  **API:** {doc}`../api/calibrated_explainer` (section WrapCalibratedExplainer)
```

## Workflow methods

```{glossary}
:sorted:

add_conjunctions
  Adds {term}`conjunctive rules <Conjunctive rule>` to existing explanations.
  Arguments such as `n_top_features` and `max_rule_size` limit which features
  are combined and how many.

  **API:** {doc}`FactualExplanation <../_autosummary/calibrated_explanations.explanations.FactualExplanation>`

calibrate
  The `WrapCalibratedExplainer` method that calibrates CE on held-out
  calibration data. Call it after `fit` and before any prediction or
  explanation. See {term}`Calibration set`.

  **API:** {doc}`WrapCalibratedExplainer <../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer>`

explain_factual
  Returns {term}`factual explanations <Factual explanation>` for the given
  instances as a {term}`CalibratedExplanations` collection.

  **API:** {doc}`WrapCalibratedExplainer <../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer>`

explore_alternatives
  Returns {term}`alternative explanations <Alternative explanation>` for the
  given instances as an {term}`AlternativeExplanations` collection.

  **API:** {doc}`WrapCalibratedExplainer <../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer>`

fit
  The `WrapCalibratedExplainer` method that trains the wrapped model on the
  {term}`proper training set <Proper training set>`. Call it before
  {term}`calibrate`.

  **API:** {doc}`WrapCalibratedExplainer <../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer>`

plot
  The `.plot()` method of an explanation or collection. It draws the rules,
  their weights and their uncertainty intervals; the `style` argument selects
  the plot type, for example `"triangular"` for alternatives.

  **Learn more:** {doc}`../foundations/how-to/interpret_explanations` (section 3)

predict
  Returns calibrated predictions: class labels for classification, numeric
  values for regression. With {term}`uq_interval` set to `True` it also returns
  the {term}`uncertainty interval <Uncertainty interval>`.

  **API:** {doc}`WrapCalibratedExplainer <../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer>`

predict_proba
  Returns calibrated probabilities: class probabilities for classification,
  or event probabilities for regression when a {term}`threshold` is passed.
  With {term}`uq_interval` set to `True` it also returns their intervals.

  **API:** {doc}`WrapCalibratedExplainer <../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer>`

to_json
  Exports an explanation collection as a payload aligned with
  {term}`Explanation schema v1`, including calibration metadata.
  `CalibratedExplanations.from_json()` reads such a payload back.

  **Learn more:** {doc}`../foundations/how-to/export_explanations`

to_narrative
  Turns explanations into narrative text, HTML or a table, using a template
  and one or more expertise levels.

  **Learn more:** {doc}`../foundations/how-to/to_narrative`
```

## Parameters and configuration

```{glossary}
:sorted:

bins
  Mondrian category labels for {term}`Mondrian calibration`. Pass them to
  `calibrate` and again when predicting or explaining.

  **Learn more:** {doc}`../foundations/how-to/conditional_calibration`

categorical_features
  The indices of the features CE should treat as categorical.

  **API:** {doc}`CalibratedExplainer <../_autosummary/calibrated_explanations.core.CalibratedExplainer>`

confidence
  Removed reject parameter; use `reject_confidence`.

  **Defined in:** {doc}`../foundations/concepts/parameter-reference` (section `confidence`)

confidence_level
  Regression interval level; alternative input to `low_high_percentiles`.

  **Defined in:** {doc}`../foundations/concepts/parameter-reference` (section `confidence_level`)

difficulty_estimator
  A `crepes` `DifficultyEstimator` for regression that switches on
  {term}`difficulty estimation <Difficulty estimation>`.

  **Learn more:** {doc}`../practitioner/advanced/normalization-guide`

feature_names
  Human-readable feature names used in rules and plots. They can be passed to
  `calibrate`.

  **API:** {doc}`CalibratedExplainer <../_autosummary/calibrated_explanations.core.CalibratedExplainer>`

low_high_percentiles
  Regression parameter that sets the percentile interval width.

  **Defined in:** {doc}`../foundations/concepts/parameter-reference` (section `low_high_percentiles`)

mc
  A stored categorizer, such as `crepes` `MondrianCategorizer`, passed to
  `calibrate` so that CE derives Mondrian categories from the inputs itself.
  Do not pass {term}`bins` at inference as well.

  **Learn more:** {doc}`../foundations/how-to/conditional_calibration`

mode
  The `CalibratedExplainer` setting, `"classification"` or `"regression"`,
  that selects which calibrators and plugins are used.

  **API:** {doc}`CalibratedExplainer <../_autosummary/calibrated_explanations.core.CalibratedExplainer>`

reject_confidence
  Reject-policy coverage target for accepting a prediction.

  **Defined in:** {doc}`../foundations/concepts/parameter-reference` (disambiguation table)

significance
  Removed guarded parameter; use `GuardedOptions.confidence`.

  **Defined in:** {doc}`../foundations/concepts/parameter-reference` (section `significance`)

threshold
  Regression parameter that selects probabilistic regression.

  **Defined in:** {doc}`../foundations/concepts/parameter-reference` (section `threshold`)

uq_interval
  Flag that makes {term}`predict` and {term}`predict_proba` also return the
  uncertainty interval.

  **API:** {doc}`WrapCalibratedExplainer <../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer>`
```

## Explanation outputs and post-processing

```{glossary}
:sorted:

Discretization
  How CE bins feature values before it generates rules. Rule conditions refer
  to these bins, and alternatives for a continuous feature use values outside
  the instance's current bin.

  **Learn more:** {doc}`../foundations/concepts/explanation_structures`

Rules payload
  A structured view of an explanation's rules from `build_rules_payload()`.
  Its `core` part holds the calibrated prediction and the feature rules; its
  `metadata` part holds the full uncertainty records and provenance.

  **Learn more:** {doc}`../foundations/how-to/interpret_explanations` (section 2)
```

## Plotting, export and schema

```{glossary}
:sorted:

Explanation schema v1
Schema v1
  The stable JSON contract for serialized explanations, frozen for v1. It fixes
  top-level fields such as `task`, `explanation_type`, `prediction` and
  `rules`; `metadata` and `provenance` may only gain new fields.

  **Learn more:** {doc}`../schema_v1`

PlotSpec
  CE's default plotting path. Explanation plots are first described as
  PlotSpec objects and then rendered by an adapter such as matplotlib. If
  PlotSpec rendering fails, CE falls back to legacy plotting with a visible
  warning.

  **API:** {doc}`../api/visualization`
```

## Extensibility: plugins and CLI

```{glossary}
:sorted:

ce plugins
  The command-line tool for listing, validating and configuring registered
  plugins, for example `ce plugins list all`.

  **API:** {doc}`../api/cli`

Plugin
  An optional, independently versioned package that adds explanation,
  interval or plot capabilities without changing the core CE installation.
  Plugins run in the host Python process and must be registered explicitly.

  **Learn more:** {doc}`../plugins`

Plugin registry
  The central registry through which CE finds explanation, interval and plot
  plugins. Plugins have dot-delimited IDs, such as `core.explanation.factual`,
  and trust settings decide which plugins may load by default.

  **API:** {doc}`../api/plugins`
```

## Operations: logging, telemetry, caching and errors

```{glossary}
:sorted:

Calibrator cache
  An opt-in cache that stores intermediate calibration artefacts, so that
  repeated explanation runs do not recompute identical results. It is off by
  default and switched on through {term}`ExplainerConfig`.

  **Learn more:** {doc}`../foundations/how-to/tune_runtime_performance`

ConfigurationError
  The CE exception for conflicting or invalid parameter combinations, including
  removed parameter names.

  **Learn more:** {doc}`../foundations/concepts/error_handling`

Parallel backend
  An opt-in backend that runs explanation work in parallel. It is off by
  default and switched on through {term}`ExplainerConfig`.

  **Learn more:** {doc}`../foundations/how-to/tune_runtime_performance`

Reject policy
RejectPolicy
  The setting that decides how CE handles rejected instances: `NONE` (the
  default), `FLAG`, `ONLY_REJECTED` or `ONLY_ACCEPTED`. Any value other than
  `NONE` switches on reject handling for that call. See
  {term}`Reject option`.

  **Learn more:** {doc}`../practitioner/advanced/reject-policy`

Telemetry
  Metadata attached to explanations that records which components produced
  them, such as `interval_source` and `plot_source`. A `legacy:` prefix shows
  that a fallback was used.

  **Learn more:** {doc}`../foundations/how-to/interpret_explanations` (section 4)

ValidationError
  The CE exception raised when inputs or configuration fail validation.

  **Learn more:** {doc}`../foundations/concepts/error_handling`
```

Entry-point tier: Tier 3.
