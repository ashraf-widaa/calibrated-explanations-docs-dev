# Apply CE to your own data

**Path C, step 5.** This page takes you from your own data and model to
calibrated predictions and explanations you can check. It assumes you have
chosen a mode in {doc}`ce-tasks-and-modes` and run the quickstart for it. The
example uses binary classification on a public dataset, standing in for your
data; each step says what to change for your problem.

## Before you start: four checks

| Check | What to look for | If it fails |
|---|---|---|
| Supported task | One class or one number predicted per case, from a fixed set of features | CE is not designed for generative, unsupervised or reinforcement-learning models |
| Compatible model | A scikit-learn-style model with `predict`; classifiers also need `predict_proba` | Without `predict_proba`, calibrating a classifier raises a `ConfigurationError` |
| Labelled calibration data | Cases with known outcomes the model was **not** trained on | Hold some labelled data back, or retrain on less data; do not reuse training data |
| Same population | Calibration cases and the cases you will explain come from the same, stable process | Recalibrate on recent data when the population or process changes |

## 1. Split your data into three sets

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()          # replace with your own features and labels
x, y = data.data, data.target
feature_names = list(data.feature_names)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=42
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, stratify=y_train, random_state=42
)
print(len(x_proper), len(x_cal), len(x_test))
```

```text
341 114 114
```

Split **before** any preprocessing, so that no information from the
calibration or test set reaches training. `stratify` keeps the class balance
equal across sets (classification only). There is no fixed rule for the size
of the calibration set; a few hundred cases is a common starting point, and
with very few cases the ranges become wide.

## 2. Train your model, or use one you already have

```python
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(x_proper, y_proper)
```

Put preprocessing inside the model (a scikit-learn `Pipeline`), so that it is
fitted on the training set only and applied the same way to every case CE
passes to the model. CE passes NumPy arrays to the model; a pipeline fitted on
a pandas DataFrame still works but warns about missing feature names, so fit it
on arrays (`df.to_numpy()`) as here.

## 3. Wrap and calibrate

```python
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(model)
print("fitted:", explainer.fitted)
explainer.calibrate(x_cal, y_cal, feature_names=feature_names)
print("calibrated:", explainer.calibrated)
```

```text
fitted: True
calibrated: True
```

CE detects that the model is already trained, so you calibrate it directly;
the model itself is not changed. To let CE train it, wrap an untrained model
and call `explainer.fit(x_proper, y_proper)` first.

## 4. Get calibrated predictions with ranges

```python
proba, (low, high) = explainer.predict_proba(x_test[:4], uq_interval=True)
for p, lo, hi in zip(proba[:, 1], low, high):
    print(f"P(benign) = {p:.2f}  [{lo:.2f}, {hi:.2f}]")
```

```text
P(benign) = 0.03  [0.00, 0.03]
P(benign) = 0.98  [0.98, 1.00]
P(benign) = 0.08  [0.00, 0.08]
P(benign) = 0.72  [0.67, 0.88]
```

Each line is the calibrated probability of the positive class (here *benign*,
label 1) with its lower and upper value. The first three cases are clear-cut,
with narrow ranges. The fourth, 0.72 [0.67, 0.88], is less certain: the
calibration data support a probability of *benign* anywhere from about 0.67 to
0.88. The range need not be centred on the probability. For regression, use
`explainer.predict(x, uq_interval=True)` instead.

## 5. Explain a prediction

```python
factual = explainer.explain_factual(x_test[3:4])
rules = factual[0].get_rules()
top = sorted(range(len(rules["weight"])), key=lambda i: -abs(rules["weight"][i]))[:3]
for i in top:
    print(f"{rules['rule'][i]:<30} weight {rules['weight'][i]:+.2f} "
          f"[{rules['weight_low'][i]:+.2f}, {rules['weight_high'][i]:+.2f}]")
```

```text
worst concave points <= 0.14   weight +0.49 [+0.42, +0.72]
worst symmetry <= 0.32         weight +0.47 [+0.39, +0.72]
radius error <= 0.38           weight +0.37 [+0.15, +0.72]
```

These are the three strongest rules for the fourth case (index 3). Each rule
holds for this case. A positive weight means the condition pushes the
calibrated probability of *benign* up: with typical values from the other side
of the condition instead, the probability would be about that much lower. The
bracket is the weight's range; a range that includes 0 would mean the direction
of the effect is not firmly supported. Here all three ranges are above 0.

The same explanation as a chart, with the six strongest rules:

```python
factual.plot(0, uncertainty=True, filter_top=6)
```

```{figure} quickstart_assets/apply-factual-case3.png
:alt: Factual explanation plot for test case 3: calibrated probability of benign 0.72 with a range from 0.67 to 0.88; worst concave points at most 0.14, worst symmetry at most 0.32, radius error at most 0.38 and worst concavity at most 0.20 raise it; two rules have ranges that cross 0.

Factual explanation of test case 3, as drawn by `factual.plot(0, uncertainty=True, filter_top=6)`.
```

**Reading the plot.** The top panel shows the calibrated probability (vertical
line) with its range (dark bar up to the lower value, light bar up to the upper
value). Below it, each rule has one bar covering its weight's range: red for
rules that raise the probability, blue for rules that lower it. A rule whose
range crosses 0 has no dark part. The walkthrough explains the plot
{doc}`in detail <quickstart_walkthrough>` (section 7).
Use `explainer.explore_alternatives(...)` for what-if alternatives;
{doc}`../foundations/how-to/interpret_explanations` explains how to read both.

## 6. Check the results on your test set

```python
from sklearn.metrics import brier_score_loss

raw = model.predict_proba(x_test)[:, 1]
calibrated = explainer.predict_proba(x_test)[:, 1]
print(f"Brier score, model alone: {brier_score_loss(y_test, raw):.3f}")
print(f"Brier score, with CE:     {brier_score_loss(y_test, calibrated):.3f}")
```

```text
Brier score, model alone: 0.024
Brier score, with CE:     0.023
```

The Brier score is the mean squared difference between probability and
outcome; lower is better. One test set of this size cannot show that one
version is reliably better than the other: the difference may come from which
cases happened to fall in the test set. {doc}`../practitioner/evaluate_ce`
shows the checks to run before you rely on CE for your problem: a reliability
table, the mean width of the ranges, and repeating the check across splits.

## 7. Save the calibrated explainer

```python
import tempfile
from pathlib import Path

state_dir = Path(tempfile.mkdtemp()) / "ce_state"
explainer.save_state(state_dir)
restored = WrapCalibratedExplainer.load_state(state_dir, learner=model)
print(restored.predict_proba(x_test[3:4])[:, 1].round(2))
```

```text
[0.72]
```

`save_state` stores the calibration state; you supply the trained model again
when loading it. Recalibrate, rather than reload, after retraining the model or
when the population changes.

## Common problems

| Symptom | Likely cause | What to do |
|---|---|---|
| `ConfigurationError` mentioning `predict_proba` | The classifier has no `predict_proba` (for example `LinearSVC`) | Use a classifier with `predict_proba`, or wrap it in `CalibratedClassifierCV` first |
| An explanation has no rules | The calibrated probability does not change when any single feature changes, typically for cases at the edge of the range (such as 0.03 [0.00, 0.03]) | Nothing is wrong; read the prediction and its range. Alternative explanations may still be informative |
| Very wide ranges | Small calibration set, or few calibration cases like this one | Use more calibration data; check the range widths on the test set |
| `UserWarning` about feature names | The model was fitted on a pandas DataFrame | Fit the model on NumPy arrays |
| `ValidationError: Invalid argument type` when indexing explanations | Indexing with a NumPy integer | Use a plain `int`, for example `factual[int(i)]` |
| Explanations are slow | Many features or many cases explained at once | Explain fewer cases, use `features_to_ignore`, see {doc}`../practitioner/performance-tuning` |

## Use an AI coding assistant to integrate CE (optional)

An AI coding assistant can adapt the steps above to your code base. It can also
invent functions or claims that CE does not have, so treat its output as a
draft: read it, run it and compare it with this page and the
{doc}`API reference <../api/index>`. Do not paste confidential data or code
into a tool you are not allowed to share it with.

A reusable prompt; replace the parts in angle brackets:

```text
I want to add Calibrated Explanations (the Python package
calibrated-explanations) to my project. Context:
- Task: <binary classification | multiclass classification | regression>
- Model: <model class and library>; it <is | is not> already trained.
- Data: <format, number of rows and features, categorical features>.
- Preprocessing: <steps>.

Please:
1. Use only the public API: WrapCalibratedExplainer with fit (if needed),
   calibrate, predict / predict_proba with uq_interval=True,
   explain_factual and explore_alternatives.
2. Split the data into training, calibration and test sets before any
   preprocessing; never calibrate on training data.
3. Keep preprocessing inside a scikit-learn Pipeline fitted on the training set.
4. Pass feature_names to calibrate.
5. Show how to read the calibrated prediction, its lower and upper value,
   and the rules and weights of one explanation.
6. Add a test-set check (for example the Brier score or a reliability
   diagram) without claiming that one test set proves an improvement.
7. Do not invent functions, arguments or guarantees. If you are unsure that
   something exists in calibrated-explanations, say so instead of guessing.
8. State the assumptions: calibration data and future cases come from the
   same, stable process; ranges describe behaviour over many cases, not a
   guarantee for one case; explanations describe the model, not causes.
9. List what I should check by hand before using the result.
10. Keep the code minimal and runnable, with comments.
```

## Next

- Evaluate before you rely on it: {doc}`../practitioner/evaluate_ce`.
- Understand the guarantees for your mode:
  {doc}`../foundations/concepts/calibrated_interval_semantics`.
- Configure explanations (guarded explanations, conjunctions, ignored
  features): {doc}`quickstart_guarded` and
  {doc}`../foundations/how-to/interpret_explanations`.
- Look up a call: {doc}`quick_api`.

Entry-point tier: Tier 3.
