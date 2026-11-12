# Software & Technical Glossary

Short definitions of the CE library's objects, methods, parameters and
configuration. Each entry links to a guide or to the API reference, where the
full signature lives. For the theory behind these terms, see the
{doc}`science`. For all terms in one list, see the {doc}`Glossary <index>`.

## Core objects

```{glossary}
:sorted:

WrapCalibratedExplainer
  The recommended entry point to CE. It wraps a scikit-learn-style model and
  adds calibrated predictions, uncertainty intervals and explanations.

  **API:** {doc}`../api/calibrated_explainer` (section WrapCalibratedExplainer)
```

## Workflow methods

```{glossary}
:sorted:

calibrate
  The `WrapCalibratedExplainer` method that calibrates CE on held-out
  calibration data. Call it after `fit` and before any prediction or
  explanation. See {term}`Calibration set`.

  **Learn more:** {doc}`../foundations/how-to/integrate_with_pipelines`
```

## Parameters and configuration

```{glossary}
:sorted:

threshold
  Regression parameter that selects probabilistic regression.

  **Defined in:** {doc}`../foundations/concepts/parameter-reference` (section `threshold`)
```

## Explanation outputs and post-processing

Entries for this group are being added.

## Plotting, export and schema

Entries for this group are being added.

## Extensibility: plugins and CLI

Entries for this group are being added.

## Operations: logging, telemetry, caching and errors

Entries for this group are being added.

Entry-point tier: Tier 3.
