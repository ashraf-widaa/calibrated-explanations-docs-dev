# Consume CE output from an application

**Goal.** Pass CE's predictions and explanations from a Python service to
another application (a dashboard, an audit store or a decision service) as
JSON, then read the prediction, its uncertainty and the explanation rules on
the receiving side.

**You need.** CE installed ({doc}`../get-started/installation`) and a
calibrated `WrapCalibratedExplainer`. The meaning of every value read below is
introduced in the {doc}`Quick Start <../get-started/try-in-browser>`.

## 1. Produce: explain and serialize

This example reuses the diabetes case from the Quick Start.

```python
import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from calibrated_explanations import WrapCalibratedExplainer

DATA = ("https://raw.githubusercontent.com/Moffran/"
        "calibrated_explanations/main/tests/data/")
diab = pd.read_csv(DATA + "diabetes_full.csv")
X, y = diab.drop(columns="Y"), diab["Y"]
X_rest, X_test, y_rest, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42)
X_train, X_cal, y_train, y_cal = train_test_split(
    X_rest, y_rest, test_size=0.33 / 0.80, stratify=y_rest, random_state=42)

explainer = WrapCalibratedExplainer(
    RandomForestClassifier(n_estimators=100, random_state=42))
explainer.fit(X_train.to_numpy(), y_train.to_numpy())
explainer.calibrate(X_cal.to_numpy(), y_cal.to_numpy(),
                    feature_names=list(X.columns))

batch = explainer.explain_factual(X_test.to_numpy()[112:113])
message = json.dumps(batch.to_json(), default=str)
print(sorted(json.loads(message)))
```

```text
['collection', 'explanations', 'schema_version']
```

`to_json()` returns a dictionary that follows
{doc}`Explanation Schema v1 <../schema_v1>`: a `collection` block (mode,
feature names, class labels) and one entry per explained case under
`explanations`. Send `message` over any channel that carries text.

## 2. Consume: validate and read

The receiving application needs only the standard library and, for
validation, CE's schema validator.

```python
from calibrated_explanations.schema import validate_payload

payload = json.loads(message)
print("mode:", payload["collection"]["mode"])
for item in payload["explanations"]:
    validate_payload(item)            # raises if the entry breaks schema v1
    p = item["prediction"]
    print(f"{item['task']} {item['explanation_type']}: "
          f"{p['predict']:.3f} [{p['low']:.3f}, {p['high']:.3f}]")
    top = sorted(item["rules"],
                 key=lambda r: -abs(r["rule_weight"]["predict"]))[:3]
    for r in top:
        w = r["rule_weight"]
        print(f"  {r['rule']:22s} {w['predict']:+.3f} "
              f"[{w['low']:+.3f}, {w['high']:+.3f}]")
```

```text
mode: classification
classification factual: 0.510 [0.467, 0.556]
  Age > 28.50            +0.290 [+0.286, +0.303]
  Insulin > 113.00       +0.290 [+0.286, +0.303]
  Glucose <= 132.50      -0.146 [-0.162, -0.139]
```

**Expected result.** The same calibrated probability, bounds and rule weights
as in the Quick Start's diabetes case. Read them with the same care on the
receiving side: `low` and `high` bound a probability for classification and
for threshold questions, but are a prediction interval in the target's units
for interval regression, so carry `collection["mode"]` with every payload.

## 3. Checks before you deploy

- **Validate every payload** with `validate_payload` at the boundary between
  services; it raises an error when an entry does not follow schema v1.
- **Keep the mode and threshold with the numbers.** The collection block
  records them; a dashboard that drops them cannot be read correctly.
- **Rehydrate in Python** when you need the explanation objects again:
  {doc}`Export explanations <../foundations/how-to/export_explanations>`
  shows `CalibratedExplanations.from_json()` and table exports.
- **Recalibrate when the data changes.** The ranges assume the new cases
  resemble the calibration data; see
  {doc}`Guarantees and limits by mode <../foundations/concepts/calibrated_interval_semantics>`.

Related: {doc}`Explanation Schema v1 <../schema_v1>`,
{doc}`Serialization & schema reference <../api/serialization>`,
{doc}`Integrate with scikit-learn pipelines <../foundations/how-to/integrate_with_pipelines>`
and {doc}`Safe defaults for production <../foundations/how-to/safe-defaults>`.
