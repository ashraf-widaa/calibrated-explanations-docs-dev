# Alternative explanations and ensured filters

Alternative explanations show how feature changes may change predictions.
A factual explanation says *which of this case's values drive the prediction*;
an alternative explanation asks *what would the calibrated prediction be if
one feature had a value in a different range?*

Semantics and non-guarantees are defined in
{doc}`calibrated_interval_semantics`.

## What an alternative is

For each feature, CE splits the feature's values into ranges using the
calibration data. For classification, alternatives use finer ranges than
factual rules: a small entropy-based decision tree gives up to eight ranges
per feature. For every range the case is **not** in, CE substitutes typical
calibration values from that range into the case, asks the calibrated model
again, and reports the resulting calibrated prediction with its lower and
upper value. Each such row is one alternative: a condition, such as
`worst concave points < 0.14`, and the prediction the model would give under
it.

Alternatives can move the prediction in either direction. They describe the
**model's** behaviour in a different scenario; they do not say that changing
the real-world quantity would change the outcome.

## Generate and read alternatives

The example is the case followed in the
{doc}`Quick Start walkthrough <../../get-started/quickstart_walkthrough>`:
a random forest classifying breast-tumour samples, with the probability of
*benign* as the calibrated output.

```python
import warnings

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from calibrated_explanations import WrapCalibratedExplainer

warnings.simplefilter("ignore")
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, stratify=data.target, random_state=42
)
X_proper, X_cal, y_proper, y_cal = train_test_split(
    X_train, y_train, test_size=0.25, stratify=y_train, random_state=42
)
explainer = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=100, random_state=42))
explainer.fit(X_proper, y_proper)
explainer.calibrate(X_cal, y_cal, feature_names=list(data.feature_names))

alternatives = explainer.explore_alternatives(X_test[2:3])
alt0 = alternatives[0]
rules = alt0.get_rules()
base = alt0.prediction["predict"]
order = np.argsort(-np.abs(np.asarray(rules["predict"], dtype=float) - base))[:3]
print(f"Current calibrated P(benign): {base:.3f}")
for i in order:
    print(f"{rules['rule'][i]:<30} {rules['predict'][i]:.3f}  "
          f"[{rules['predict_low'][i]:.3f}, {rules['predict_high'][i]:.3f}]")
```

```text
Current calibrated P(benign): 0.286
worst concave points < 0.14    0.476  [0.333, 0.600]
worst area > 853.50            0.143  [0.000, 0.167]
worst concavity > 0.35         0.151  [0.000, 0.178]
```

**Reading it.**

- The case's calibrated probability of *benign* is 0.286, so the model
  predicts *malignant*.
- If `worst concave points` were below 0.14, the calibrated probability would
  be 0.476, with a range of 0.333 to 0.600. The estimate stays below 0.5, but
  the range spans 0.5: in that scenario the output would no longer clearly
  favour either class.
- The next two alternatives **lower** the probability: they show conditions
  under which the model would be even more inclined towards *malignant*.

**The link to the factual explanation.** The factual weight of
`worst concave points > 0.14` for this case is −0.190, which is
0.286 − 0.476: the factual weight compares the case with typical values from
the other side of the split, which is exactly the first alternative here.

**The ranges shown for scenarios** are averages of Venn-Abers bounds over the
substituted values. They are not the calibrated range of the case itself and
do not carry its guarantee.

For probabilistic regression, pass the same `threshold` as for prediction:

```{code-block} python
alternatives = explainer.explore_alternatives(X_query, threshold=150.0)
```

## Ensured filters

The alternative object provides filters that select subsets of its
alternatives:

- `super_explanations()`
- `semi_explanations()`
- `counter_explanations()`
- `ensured_explanations()`
- `pareto_explanations()`

The ensured filter compares each alternative's uncertainty range with the
original prediction's range; the
{doc}`ensured explanations playbook <../../practitioner/playbooks/ensured-explanations>`
shows how to use the filters together. *The exact definitions of these
filters are under review by the CE authors*, so this page does not define
them further.

## Plotting and conjunctions

```python
alt0.add_conjunctions(n_top_features=5, max_rule_size=2)
alt0.plot(style="triangular", show=False)
```

`add_conjunctions` adds rules that combine conditions on more than one
feature. Their values are computed differently from single-feature rules:
compare conjunctions with each other, not with single rules. *How to read
them is under review by the CE authors.*

## What alternatives do not tell you

- They are not causal: they describe how the model responds to a changed
  input, not what would happen if the case changed in reality.
- They are not recommendations: a scenario may be impossible or undesirable
  in practice.
- They say nothing about other cases; each set of alternatives belongs to one
  case.

## Related pages

- {doc}`../../practitioner/playbooks/ensured-explanations`
- {doc}`../how-to/interpret_explanations`
- {doc}`guarded_explanations`
- Löfström, H., Löfström, T., Johansson, U., and Sönströd, C. (2024).
  [Calibrated explanations: with uncertainty information and counterfactuals](https://doi.org/10.1016/j.eswa.2024.123154).
  *Expert Systems with Applications*, 246, 123154.

Entry-point tier: Tier 3.
