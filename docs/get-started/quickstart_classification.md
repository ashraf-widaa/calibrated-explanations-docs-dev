# Classification tutorial

**One of the {doc}`Python tutorials <../tutorials/index>`.** Calibrate a classifier, read its calibrated probabilities
with their ranges, and explain a prediction. The example is multiclass (three
iris species); the same code works for binary classification. If you have not
yet chosen a mode, start with {doc}`ce-tasks-and-modes`.

## Prerequisites

```bash
pip install "calibrated-explanations[viz]" scikit-learn
```

The `viz` extra installs Matplotlib, which the plotting step below needs. You
need a classifier with `predict` and `predict_proba`, and labelled data you
can split into training, calibration and test sets.

## Classification semantics note

- **Calibration prerequisites**: fit on `x_proper, y_proper` and calibrate on held-out `x_cal, y_cal`.
- **Mode-specific guarantees**: CE returns a Venn-Abers pair and a merged class probability; the exact pair/merged-probability validity wording remains under author review (SR-03).
- **Assumptions**: exchangeability under the method-specific calibration protocol; the alternative distribution-match wording remains under author review (SR-01).
- **Explicit non-guarantees**: no guarantee under drift or regime shift.
- **Explanation-envelope limits**: feature-level intervals are model-behavior summaries, not causal guarantees.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics`.

## 1. Load data and split sets

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

dataset = load_iris()
x = dataset.data
y = dataset.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=0
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, stratify=y_train, random_state=0
)
print(len(x_proper), len(x_cal), len(x_test))
```

```text
90 30 30
```

The model trains on 90 cases, CE calibrates on 30 others, and 30 are kept for
testing. Thirty calibration cases is very few; it keeps the example fast, and
step 3 shows its cost.

## 2. Fit and calibrate the explainer

```python
from sklearn.ensemble import RandomForestClassifier
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(RandomForestClassifier(random_state=0))
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal, feature_names=dataset.feature_names)
```

If your model is already trained, wrap it and skip `fit`; see
{doc}`apply-to-your-data`.

## 3. Calibrated probabilities with ranges

```python
proba, (low, high) = explainer.predict_proba(
    x_test[:3], uq_interval=True, normalization="simplex"
)
for i, label in enumerate(proba.argmax(axis=1)):
    print(f"case {i}: {dataset.target_names[label]:<10} "
          f"p = {proba[i, label]:.2f}  [{low[i, label]:.2f}, {high[i, label]:.2f}]")
```

```text
case 0: setosa     p = 0.73  [0.00, 1.00]
case 1: versicolor p = 0.91  [0.91, 1.00]
case 2: setosa     p = 0.91  [0.91, 1.00]
```

Each line shows the predicted class, its calibrated probability and the lower
and upper value of that probability. Cases 1 and 2 are predicted firmly. For
case 0 the probability of *setosa* is 0.73, but the range runs from 0.00 to
1.00: with only 30 calibration cases, the calibration data hardly constrain it.
More representative calibration data can help, but narrowing the range for
every individual case is not guaranteed.

`normalization="simplex"` preserves each class's raw Venn–Abers pair while
normalizing the point estimates; this does not establish joint multiclass
validity. With the default multiclass `scale` normalization, CE rescales the bounds together with the
probabilities, and an upper bound can then exceed 1; see limitation 1 in
{doc}`ce-tasks-and-modes`. For binary classification the option makes no
difference to how you read the output.

## 4. Generate calibrated factual explanations

The `simplex` setting above applies only to that prediction call. The
explanation calls below use the default multiclass `scale` normalization,
which rescales the bounds as well as the estimates. The explanation plot
therefore does not show the raw bounds from step 3. The interpretation of
these rescaled ranges remains under author review (SR-13).

```python
factual = explainer.explain_factual(x_test[:5])
rules = factual[1].get_rules()
for rule, w, lo, hi in zip(rules["rule"], rules["weight"],
                           rules["weight_low"], rules["weight_high"]):
    print(f"{rule:<28} weight {w:+.2f} [{lo:+.2f}, {hi:+.2f}]")
```

```text
sepal length (cm) > 5.55     weight +0.39 [+0.24, +0.43]
sepal width (cm) <= 2.95     weight +0.20 [+0.10, +0.22]
petal length (cm) > 2.55     weight +0.43 [-0.05, +0.91]
petal width (cm) > 0.65      weight +0.43 [-0.05, +0.91]
```

The explanation of case 1 (predicted *versicolor*) lists one rule per feature
that holds for the case. A positive weight means the condition raises the
calibrated probability of the predicted class: with typical values from the
other side of the condition, the probability would be about that much lower.
The bracket is the weight's range. The two petal rules have the largest
weights, but their ranges reach below 0, so the calibration data support their
direction less firmly than that of the two sepal rules.

The same explanation as a chart:

```python
factual.plot(1, uncertainty=True)
```

```{figure} quickstart_assets/classification-factual-case1.png
:alt: Factual explanation plot for case 1: calibrated probability of versicolor 0.91 with a range from about 0.90 to 0.99 (default multiclass bounds); sepal length above 5.55 and sepal width at most 2.95 raise it with ranges above 0; the two petal rules have ranges from below 0 to about 0.91.

Factual explanation of case 1, as drawn by `factual.plot(1, uncertainty=True)`.
```

**Reading the plot.** The top panel shows the calibrated probability (vertical
line) with its range (dark bar up to the lower value, light bar up to the upper
value). Below it, each rule has one bar covering its weight's range: red for
rules that raise the probability, blue for rules that lower it. A rule whose
range crosses 0 has no dark part. The walkthrough explains the plot
{doc}`in detail <quickstart_walkthrough>` (section 7).
In this plot, class `y=1` is *versicolor*; `y!=1` groups the other
classes. The sepal rules have ranges entirely to the right of zero, while
the petal-rule ranges cross zero despite extending far to the right. Thus
bar length alone does not establish a direction. The right-hand numbers are
the case's feature values in centimeters. The grey band shows the
prediction bounds shifted around zero, not another feature's contribution.
These are the default multiclass bounds described above; the weight ranges
do not establish individual coverage or causal effects.

The plot therefore shows two different kinds of range. The **prediction
bounds** in the top panel come from the calibration itself. Each **weight
range** below is derived by comparing calibrated predictions after
substituting feature values; it is not a calibrated statement about the
feature, and no formal guarantee is claimed for it.

For more, see {doc}`../foundations/how-to/interpret_explanations`.

For multiclass all-class explanations:

```python
multi_factual = explainer.explain_factual(x_test[:5], multi_labels_enabled=True)
```

`multi_labels_enabled` remains an explicitly experimental call-time option; its
spelling is canonical, but its contract is not part of the frozen stable surface.

## 5. Explore calibrated alternatives

```python
alternatives = explainer.explore_alternatives(x_test[:2])
alt = alternatives[0].get_rules()
for rule, p, lo, hi in zip(alt["rule"], alt["predict"],
                           alt["predict_low"], alt["predict_high"]):
    print(f"if {rule:<28} p = {p:.2f} [{lo:.2f}, {hi:.2f}]")
```

```text
if sepal length (cm) < 5.35     p = 0.91 [0.90, 0.99]
if sepal length (cm) > 5.55     p = 0.55 [0.00, 1.10]
if petal length (cm) > 2.55     p = 0.41 [0.00, 0.82]
if petal width (cm) > 0.65      p = 0.43 [0.00, 0.85]
```

Each line is a what-if for case 0: the calibrated probability of the predicted
class (*setosa*) if that one feature had a value in the stated range instead.
The wide ranges again reflect the small calibration set; an upper value above 1
(here 1.10) comes from the default multiclass rescaling described in limitation 1.
Alternatives describe
how the model responds; they do not say that such a change is possible or
would change the real outcome.

## Common mistakes

- Calibrating on the training data: the model then looks more reliable than it
  is. Always calibrate on held-out cases.
- Reading `[low, high]` as a guarantee for one case: the bounds describe
  calibrated behaviour over many cases, not the correctness of one prediction.
- Reading the default multiclass bounds as probabilities (limitation 1).
- Treating a weight as a cause, or an alternative as a recommended action.

## Continue

- **Next:** {doc}`quickstart_regression`, the next Python tutorial.
- **Go deeper:** {doc}`How CE calibrates <../foundations/concepts/calibration_methods>`
  (section 2, Venn–Abers predictors) and the classification guarantees in
  {doc}`../foundations/concepts/calibrated_interval_semantics`.
- **See also:** {doc}`quickstart_guarded` (filter explanations to typical
  feature values), {doc}`apply-to-your-data` (your own data and model),
  {doc}`../foundations/how-to/interpret_explanations`,
  {doc}`../foundations/concepts/alternatives` and {doc}`../citing`.
- **Before this:** {doc}`ce-tasks-and-modes` (choosing the mode) and
  {doc}`apply-overview` (the practical workflow without code).
