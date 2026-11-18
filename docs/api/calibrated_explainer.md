# Calibrated Explainer API

This reference documents the public API for the `calibrated_explanations` package. It includes the main explainer classes, the explanation containers, and the specific explanation types.

## Core Explainers

Most code uses `WrapCalibratedExplainer`: it wraps your model with a scikit-learn-style interface (`fit`, `calibrate`, `predict`, `predict_proba`, `explain_factual`, `explore_alternatives`). It builds a `CalibratedExplainer`, which performs the calibration, when you call `calibrate`.

### WrapCalibratedExplainer (start here)

<span id="wrapcalibratedexplainer"></span>

The `WrapCalibratedExplainer` acts as a wrapper around `CalibratedExplainer` to provide a standard scikit-learn interface (`fit`, `predict`, `predict_proba`). Callers retain control of the proper-training and held-out calibration splits: call `fit(...)`, then `calibrate(...)`, before requesting predictions or explanations.

**Example Usage:**

```python
from calibrated_explanations import WrapCalibratedExplainer
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
X, y = load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, stratify=y_train, random_state=0
)

# Initialize wrapper with a base model
model = RandomForestClassifier(random_state=0)
wrapper = WrapCalibratedExplainer(model)

# Fit on the proper-training split and calibrate on held-out data
wrapper.fit(x_proper, y_proper)
wrapper.calibrate(x_cal, y_cal)

# Explain through the canonical public method
explanations = wrapper.explain_factual(x_test[:1])
```

Full signatures, methods and parameters: {doc}`WrapCalibratedExplainer API reference <../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer>`.

### CalibratedExplainer (advanced)

<span id="calibratedexplainer"></span>

Use `CalibratedExplainer` directly only when you already hold a fitted model
and calibration data and do not need the `fit`/`calibrate` lifecycle.

`CalibratedExplainer` takes a fitted classifier or regressor and held-out
calibration data. It uses Venn–Abers for classification and CPS for regression;
threshold-event queries also use Venn–Abers. Explanations are computed from
these calibrated outputs. Prediction guarantees do not transfer automatically
to explanation-weight ranges; see
{doc}`../foundations/concepts/calibrated_interval_semantics`.

For a task-oriented view of the same capabilities (classification, conformal interval regression via CPS, and probabilistic/thresholded regression), see {doc}`../tasks/index`.

**Example Usage:**

```python
from calibrated_explanations import CalibratedExplainer
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
X, y = load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, stratify=y_train, random_state=0
)

# Train model
model = RandomForestClassifier(random_state=0)
model.fit(x_proper, y_proper)

# Initialize explainer
explainer = CalibratedExplainer(model, x_cal, y_cal, mode='classification')

# Explain a test instance
explanations = explainer.explain_factual(x_test[:1])
```

Full signatures, methods and parameters: {doc}`CalibratedExplainer API reference <../_autosummary/calibrated_explanations.core.CalibratedExplainer>`.

## Explanation Containers

When you request explanations for a set of instances, the result is returned in a `CalibratedExplanations` object. This collection holds the individual explanations and provides methods for visualization and export.

### CalibratedExplanations

A `CalibratedExplanations` object is returned when you call `explain_factual()` on a `CalibratedExplainer` or `WrapCalibratedExplainer`. It is a collection of explanations for the provided test instances. It serves as a container that allows you to iterate over individual explanations, visualize them, or export them.

**Example Usage:**

```python
# Assuming 'explanations' is a CalibratedExplanations object
# Iterate over explanations
for explanation in explanations:
    print(explanation.prediction)

# Plot all explanations
explanations.plot()

# Get a specific explanation
first_explanation = explanations[0]
```

**Metadata Attributes:**

When FAST-based feature filtering is enabled (experimental), the `CalibratedExplanations` object may include additional metadata for transparency and debugging:

- `feature_filter_per_instance_ignore`: On the returned collection, a best-effort list of per-instance feature-index masks produced by filtering. The `CalibratedExplainer` also exposes the transient mask from the most recent filtered batch under the same attribute name. This diagnostic metadata is not part of the stable API.

Full signatures, methods and parameters: {doc}`CalibratedExplanations API reference <../_autosummary/calibrated_explanations.explanations.CalibratedExplanations>`.

## Explanation Types

Individual explanations are represented by specific classes depending on the type of explanation requested.

### CalibratedExplanation

This is the abstract base class for a single explanation. It contains the instance data, the prediction, and the feature weights (rules) that explain the prediction. It provides methods for plotting the explanation.

**What `get_rules()` returns.** A dictionary. Most keys hold aligned lists
with one entry per rule; a few describe the case as a whole. For a factual
explanation the main keys are:

| Key | Meaning |
|---|---|
| `rule` | The condition as text, for example `worst concave points > 0.14` |
| `feature`, `feature_value`, `value` | Per rule: the feature's column index, the case's value for it, and that value as text |
| `weight`, `weight_low`, `weight_high` | The rule's weight and its range |
| `predict`, `predict_low`, `predict_high` | The calibrated prediction for the rule's scenario and its range |
| `base_predict`, `base_predict_low`, `base_predict_high` | For the case as a whole: the calibrated prediction and its range |
| `is_conjunctive` | Whether the rule combines several conditions |
| `classes` | The explained class (a single value) |
| `sampled_values` | Per rule: the substituted values used to compute the weight |

For an alternative explanation, read `predict`, `predict_low` and
`predict_high` as the calibrated prediction under the alternative condition.
The {doc}`Quickstart <../get-started/quickstart>` prints both. How to
interpret the values: {doc}`../foundations/how-to/interpret_explanations`.

Full signatures, methods and parameters: {doc}`CalibratedExplanation API reference <../_autosummary/calibrated_explanations.explanations.CalibratedExplanation>`.

### FactualExplanation

A `FactualExplanation` explains the model's calibrated prediction for an instance through local feature rules, weights, and uncertainty intervals. It describes the observed instance; use `explore_alternatives(...)` when you need candidate changes.

**Example Usage:**

```python
# Plot a factual explanation
factual_explanation.plot()

# Add a conjunction to the explanation
factual_explanation.add_conjunctions()
```

Full signatures, methods and parameters: {doc}`FactualExplanation API reference <../_autosummary/calibrated_explanations.explanations.FactualExplanation>`.

### AlternativeExplanation

An `AlternativeExplanation` reports model predictions for substituted feature
values or ranges. An alternative may reinforce the current prediction, move
it towards a boundary, or change the predicted class. It need not flip a label,
be minimal, or describe a feasible real-world action. See
{doc}`../foundations/concepts/alternatives` for construction and interpretation.

**Example Usage:**

```python
# Plot an alternative explanation
alternative_explanation.plot()
```

Full signatures, methods and parameters: {doc}`AlternativeExplanation API reference <../_autosummary/calibrated_explanations.explanations.AlternativeExplanation>`.


## Narrative facts

`build_narrative_spec` turns one serialized explanation into an immutable
`NarrativeSpec` (ADR-041). See [Generate narratives](../foundations/how-to/to_narrative.md).

```{eval-rst}
.. automodule:: calibrated_explanations.explanations.narrative_spec
   :members: build_narrative_spec, NarrativeSpec, NarrativeRuleFact, NarrativeInterval
```
