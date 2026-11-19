# Python quickstart: a ten-minute classification example

<span id="python-quickstart-your-first-calibrated-explanation"></span>

*The main first example is {doc}`Your First CE Explanation in Python <first-explanation-python>`
(classification and regression, 13 steps). This page is a shorter, single
classification example on scikit-learn's breast-cancer data; the
{doc}`Python walkthrough <quickstart_walkthrough>` and {doc}`CE by example <ce-by-example>`
explain the same case in depth.*

<span id="quickstart-your-first-calibrated-explanation"></span>

**Practitioner Hub · about 10 minutes · You need: Python 3.10 or later
and CE {doc}`installed <installation>`.** You will train a model, calibrate it and explain one prediction,
and see what CE returns at each step. The example predicts whether a breast
tumour sample is *benign* or *malignant*, using scikit-learn's built-in
dataset. Prefer to see the result first, without code? Read
{doc}`CE by example <ce-by-example>`.

## 1. Install

```bash
pip install "calibrated-explanations[viz,narrative]"
```

The `viz` extra adds plotting; the `narrative` extra (PyYAML) is needed for the
text narrative in step 6. Other extras and conda: {doc}`installation`.

## 2. Split the data three ways

CE needs a **calibration set**: labelled cases that the model never trains on.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
X_proper, X_cal, y_proper, y_cal = train_test_split(
    X_train, y_train, test_size=0.25, stratify=y_train, random_state=42
)
print(len(X_proper), len(X_cal), len(X_test))
```

```text
341 114 114
```

```{raw} html
<div class="ce-roles" role="img" aria-label="The 569 cases are split three ways: 341 proper training cases used by fit, 114 calibration cases used by calibrate and never seen by the model, and 114 test cases that are predicted and explained.">
  <span class="ce-role ce-role-train" style="flex-grow:341"><strong>341 training</strong><code>fit</code></span>
  <span class="ce-role ce-role-cal" style="flex-grow:114"><strong>114 calibration</strong><code>calibrate</code></span>
  <span class="ce-role ce-role-test" style="flex-grow:114"><strong>114 test</strong><code>predict</code> · <code>explain</code></span>
</div>
```

| Set | Used for | Never used for |
|---|---|---|
| `X_proper`, `y_proper` | Training the model (`fit`) | Calibration |
| `X_cal`, `y_cal` | Calibrating (`calibrate`) | Training |
| `X_test` | The cases you predict and explain | Training or calibration |

Do not calibrate on the training data: the model has already seen it.

## 3. Wrap your model, train it, calibrate it

```python
from sklearn.ensemble import RandomForestClassifier

from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(
    RandomForestClassifier(n_estimators=100, random_state=42)
)
explainer.fit(X_proper, y_proper)
explainer.calibrate(
    X_cal,
    y_cal,
    feature_names=list(data.feature_names),
    class_labels={0: "malignant", 1: "benign"},
)
```

`class_labels` makes printed explanations use class names instead of 0 and 1.
Already have a trained model? Wrap it and skip `fit`.

## 4. Predict with a range

```python
case = X_test[2:3]
proba, (low, high) = explainer.predict_proba(case, uq_interval=True)
print(f"P(benign) = {proba[0, 1]:.3f}  range [{low[0]:.3f}, {high[0]:.3f}]")
```

```text
P(benign) = 0.286  range [0.167, 0.333]
```

The calibrated probability of *benign* is 0.286, so CE predicts *malignant*;
the whole range lies below 0.5. The range gives the lower and upper
calibrated probability. It is **not** a confidence interval for this one
patient.

## 5. Explain the prediction

```python
factual = explainer.explain_factual(case)
rules = factual[0].get_rules()

top = sorted(range(len(rules["weight"])), key=lambda i: -abs(rules["weight"][i]))[:3]
for i in top:
    print(
        f"{rules['rule'][i]:32s} weight {rules['weight'][i]:+.3f}  "
        f"range [{rules['weight_low'][i]:+.3f}, {rules['weight_high'][i]:+.3f}]"
    )
```

```text
worst concave points > 0.14      weight -0.190  range [-0.314, -0.048]
worst area <= 853.50             weight +0.143  range [+0.119, +0.286]
worst concavity <= 0.35          weight +0.135  range [+0.108, +0.286]
```

Each line is a **condition that is true for this case**.

- **Weight:** how much the condition moves the calibrated probability of
  *benign*. A negative weight moves it towards *malignant*.
- **Range:** the uncertainty of that weight. All three ranges stay on one side
  of 0, so their direction is clear.
- **Not additive, not causal:** the weights do not add up to the prediction,
  and they describe the model, not the disease.

## 6. Read it as text or as a plot

```python
narrative = factual.to_narrative(output_format="text", expertise_level="beginner")
# Print the first lines of the beginner narrative.
print("\n".join(narrative.strip().splitlines()[4:12]))
```

```text
Factual Explanation (Beginner):
--------------------------------------------------------------------------------
Prediction: malignant
Calibrated Probability: 0.286

Factors impacting the probability for class benign positively:
* worst area (788.0) <= 853.50
* worst concavity (0.34) <= 0.35
```

The full text continues with every condition; those whose weight range
crosses 0 are marked `[!] direction uncertain`. To draw the same ranges as
bars, call `factual.plot()`; the
{doc}`reading guide <../foundations/how-to/interpret_explanations>` explains
every element of the plot.

## 7. Ask "what if?"

```python
alternatives = explainer.explore_alternatives(case)
r = alternatives[0].get_rules()
for i, rule in enumerate(r["rule"]):
    if "worst concave points" in rule:
        print(
            f"{rule:32s} P(benign) {r['predict'][i]:.3f}  "
            f"range [{r['predict_low'][i]:.3f}, {r['predict_high'][i]:.3f}]"
        )
```

```text
worst concave points < 0.14      P(benign) 0.476  range [0.333, 0.600]
```

If this feature were in the other range, the calibrated probability of
*benign* would be 0.476: still below 0.5, but its range now crosses 0.5. This
describes how the model responds; it is not a recommended action.

## What you did

1. Split the data into training, calibration and test sets.
2. Wrapped, trained and calibrated a model with `WrapCalibratedExplainer`.
3. Got a calibrated probability with a range (`predict_proba`).
4. Explained it with weighted conditions and their ranges (`explain_factual`).
5. Asked a "what if" question (`explore_alternatives`).

:::{note}
What each range guarantees depends on the task and on the calibration data
coming from the same process as new cases. Read
{doc}`Guarantees by mode <../foundations/concepts/calibrated_interval_semantics>`
before reporting a range as a guarantee.
:::

## Next

- **Next:**
  {doc}`How to read CE explanations <../foundations/how-to/interpret_explanations>`
  (step 4 of {doc}`Get started <index>`).
- **Go deeper on this example:** the
  {doc}`Python walkthrough <quickstart_walkthrough>` explains every step,
  including how the calibration works.
- **Regression instead?** The {doc}`regression tutorial <quickstart_regression>`.
- **Something failed?** {doc}`troubleshooting`.

Every output on this page is checked by the documentation tests.
