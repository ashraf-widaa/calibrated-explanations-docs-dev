# Scientific & Theoretical Glossary

Short definitions of the machine-learning, explainability, probability,
calibration and uncertainty terms behind CE. Each entry links to the page under
*How CE Works* that teaches the idea. For library objects and parameters, see
the {doc}`software`. For all terms in one list, see the {doc}`Glossary <index>`.

Each entry gives a short definition, other names for the same idea, and one
page to read next. Entries marked *wording under review* are not yet confirmed
by the CE authors.

## Machine learning and data

```{glossary}
:sorted:

Calibration set
Calibration data
Calibration split
  Labelled data held out from training and used only to calibrate CE. The model
  never sees it during training, so CE can measure how the model's outputs
  relate to real outcomes on unseen cases.

  **Learn more:** {doc}`../get-started/ml-foundations` (section A5)
```

## Explainability

Entries for this group are being added.

## Probability and calibration

Entries for this group are being added.

## Uncertainty

Entries for this group are being added.

## Conformal and Venn–Abers methods

```{glossary}
:sorted:

Conformal predictive system
CPS
  A conformal method for regression that outputs a whole predictive
  distribution for a new case instead of a single interval. CE uses the split
  version and reads interval regression bounds from its percentiles.

  **Learn more:** {doc}`../foundations/concepts/calibration_methods` (section 3)
```

## Assumptions, guarantees and limits

```{glossary}
:sorted:

Exchangeability
  Cases are exchangeable if their joint distribution does not change when they
  are reordered. Independent draws from one distribution are exchangeable; data
  with a time trend, or from a population that changed after calibration, are
  not. CE's calibration guarantees depend on this assumption. *Wording under
  review.*

  **Learn more:** {doc}`../foundations/concepts/calibrated_interval_semantics`
```

Entry-point tier: Tier 3.
