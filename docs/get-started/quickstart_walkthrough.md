# Practical walkthrough: from a trained model to calibrated explanations

This page works like a notebook. Each step has a short explanation, the code,
the output that code produced when this page was built, and what the output
means. You can run the same cells yourself: [download this walkthrough as a Jupyter notebook](path:../_static/notebooks/quickstart_walkthrough.ipynb), or copy the cells
into a Python session.

**Before you start.** This walkthrough assumes you know what a feature, a
label and a train/test split are. If not, read
[Step 1: Machine learning basics](ml-foundations.md) first. It also
assumes you know which CE mode you are using; the
[Step 2: CE tasks and outputs](ce-tasks-and-modes.md) page
explains that choice. Here we use **binary classification**.

**What you will do**

1. Choose the task and model (B1).
2. Split the data into training, calibration and test sets (B2).
3. Train and evaluate an ordinary classifier (B3).
4. Calibrate CE on held-out data (B4).
5. Generate and read a factual explanation (B5).
6. Explore alternative explanations (B6).
7. Work with feature conditions (B7).
8. Interpret everything together, including a plot (B8).
9. Check assumptions and limitations (B9).
10. See how regression and guarded explanations differ (B10).

Install the packages once:

```bash
pip install calibrated-explanations scikit-learn matplotlib
```

## B1. Select the task and model

**What.** We will predict whether a breast tumour sample is *malignant* or
*benign* from 30 numeric measurements of cell nuclei. The target is one of two
labels, so this is **binary classification**.

**Why this example.** The dataset ships with scikit-learn, needs no
downloads, has only numeric features and trains in seconds. Classification is
also the easiest place to see what calibration adds: a probability you can
read as "out of comparable cases, about this share were benign".

**Model.** We use a random forest. CE works with scikit-learn style models
that provide `fit` and `predict` (and `predict_proba` for classification), so
the model family is your choice. The random forest here is an example, not a
recommendation.

**How regression differs.** If the target were a number (for example a
disease-progression score), the task would be regression. CE then reports
prediction intervals or threshold probabilities instead of class
probabilities. Section B10 shows both.

```python
import numpy as np
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X, y = data.data, data.target
feature_names = list(data.feature_names)

print("Samples, features:", X.shape)
for label, name in enumerate(data.target_names):
    print(f"Class {label} = {name}: {int((y == label).sum())} samples")
```

```{code-block} text
:caption: Output

Samples, features: (569, 30)
Class 0 = malignant: 212 samples
Class 1 = benign: 357 samples
```

**Interpretation.** There are 569 samples and 30 features. Label `0` means
*malignant* and label `1` means *benign*. Remember this mapping: for binary
classification, CE reports the calibrated probability of class `1`, which
here is *benign*.

## B2. Prepare the data: three separate sets

**What.** We split the data into three parts, each with one job:

| Set | Used for | Seen by the model during training? |
|---|---|---|
| Proper training set | Fitting the model | Yes |
| Calibration set | Calibrating CE's probabilities and explanations | No |
| Test set | Checking performance and explaining new cases | No |

**Why.** Calibration measures how the trained model behaves on data it has
not seen. If calibration used training data, the model would look more
reliable than it is. Keeping the test set separate gives an honest final check.
Reusing any of these rows in a different role is a form of **data leakage**.

**How.** Two calls to `train_test_split`: first hold out a test set, then split
the remainder into proper training and calibration sets. `stratify` keeps the
class balance similar in each part, and `random_state` makes the split
reproducible.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
X_proper, X_cal, y_proper, y_cal = train_test_split(
    X_train, y_train, test_size=0.25, stratify=y_train, random_state=42
)

print(f"Proper training: {len(X_proper)} samples")
print(f"Calibration:     {len(X_cal)} samples")
print(f"Test:            {len(X_test)} samples")
```

```{code-block} text
:caption: Output

Proper training: 341 samples
Calibration:     114 samples
Test:            114 samples
```

**Interpretation.** About 60% of the data trains the model, 20% calibrates it
and 20% is kept for testing. A larger calibration set gives tighter, more
stable uncertainty estimates; very small calibration sets give wide intervals.

## B3. Train and evaluate the model

**What.** `WrapCalibratedExplainer` wraps an ordinary model. Training happens
with `fit`, exactly as in scikit-learn; nothing CE-specific has happened yet.

**Why wrap the model now?** The wrapper keeps the model, the calibration and
the explanation methods together, so later steps cannot accidentally mix up
models or data sets.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(
    RandomForestClassifier(n_estimators=100, random_state=42)
)
explainer.fit(X_proper, y_proper)

print("Fitted:", explainer.fitted, "| Calibrated:", explainer.calibrated)
```

```{code-block} text
:caption: Output

Fitted: True | Calibrated: False
```

**Interpretation.** The model is trained but not yet calibrated. Before
calibration, predictions come straight from the random forest. Its
`predict_proba` values average the class proportions in the trees' leaves.
They are often over- or under-confident: treat them as **scores**, not yet as
reliable probabilities.

## B4. Calibrate CE

**What.** `calibrate` shows CE the held-out calibration set. CE records how
the trained model's outputs relate to the true labels on data the model has
not seen.

**Why.** Training teaches the model to separate classes. Calibration answers a
different question: *when the model says 70%, how often is it right?* For
classification, CE uses **Venn–Abers** calibration, which turns the model's
score into a calibrated probability together with a lower and an upper bound.

**Training versus calibration**

| | Training (`fit`) | Calibration (`calibrate`) |
|---|---|---|
| Data | Proper training set | Calibration set |
| Changes the model? | Yes, learns its parameters | No, the model is fixed |
| Result | A predictive model | Calibrated probabilities, intervals and explanations |

```python
explainer.calibrate(X_cal, y_cal, feature_names=feature_names)

y_pred = explainer.predict(X_test)
print("Calibrated:", explainer.calibrated)
print(f"Test accuracy: {accuracy_score(y_test, y_pred):.3f}")
```

```{code-block} text
:caption: Output

Calibrated: True
Test accuracy: 0.947
```

**Interpretation.** Accuracy measures how often the predicted label is
correct. It says nothing about whether the probabilities are trustworthy or
why a particular prediction was made. The next cells look at both.

Now look at the probabilities for a few test cases, with their uncertainty:

```python
proba, (low, high) = explainer.predict_proba(X_test[:5], uq_interval=True)

print("case  predicted   P(benign)  interval        true label")
for i in range(5):
    print(
        f"{i:>4}  {data.target_names[y_pred[i]]:<10}  {proba[i, 1]:.3f}      "
        f"[{low[i]:.3f}, {high[i]:.3f}]  {data.target_names[y_test[i]]}"
    )
```

```{code-block} text
:caption: Output

case  predicted   P(benign)  interval        true label
   0  malignant   0.029      [0.000, 0.029]  malignant
   1  benign      0.973      [0.972, 1.000]  benign
   2  malignant   0.286      [0.167, 0.333]  malignant
   3  malignant   0.324      [0.167, 0.400]  benign
   4  malignant   0.029      [0.000, 0.029]  malignant
```

**Interpretation.**

- `low` and `high` are the Venn–Abers lower and upper probabilities of
  *benign*. Venn–Abers calibrates the model's score twice, once assuming the
  new case is benign and once assuming it is malignant; the two results are
  `low` and `high`.
- `proba[:, 1]` is CE's single best estimate of the probability of *benign*,
  a combination of `low` and `high`. It always lies between them.
- The **width** of the interval shows how much the calibration depends on
  this one case. It is wide when few calibration cases received a model score
  similar to this case's score, and narrow when many did.
- These bounds are *not* conventional confidence intervals around an unknown
  "true" probability. The
  [semantics reference](../foundations/concepts/calibrated_interval_semantics.md)
  states exactly what is and is not guaranteed.

Case `2` is the most interesting: the model predicts *malignant*, but less
confidently than for cases `0` and `4`. We explain that case next.

## B5. Generate a factual explanation

**What.** A **factual explanation** answers: *which of this case's actual
feature values pushed the prediction up or down, and how certain is each
effect?* Each line is a **rule**: a feature condition that is true for this
case (for example `worst concave points > 0.14`) together with a **weight**.

**Why.** Knowing the probability is not enough to trust or challenge it.
The factual explanation shows what the prediction depends on, with calibrated
uncertainty for each feature's effect.

**How.** Call `explain_factual` on the cases to explain. It returns a
collection; index it to get one explanation.

```python
case = 2
factual = explainer.explain_factual(X_test[case:case + 1])
explanation = factual[0]

pred = explanation.prediction
print(f"Calibrated P(benign) = {pred['predict']:.3f}  "
      f"interval [{pred['low']:.3f}, {pred['high']:.3f}]")
```

```{code-block} text
:caption: Output

Calibrated P(benign) = 0.286  interval [0.167, 0.333]
```

```python
def rule_table(expl, top=6):
    rules = expl.get_rules()
    order = np.argsort(-np.abs(np.asarray(rules["weight"], dtype=float)))[:top]
    print(f"{'feature condition':<34} {'weight':>8}   weight interval")
    for i in order:
        print(f"{rules['rule'][i]:<34} {rules['weight'][i]:+8.3f}   "
              f"[{rules['weight_low'][i]:+.3f}, {rules['weight_high'][i]:+.3f}]")

rule_table(explanation)
```

```{code-block} text
:caption: Output

feature condition                    weight   weight interval
worst concave points > 0.14          -0.190   [-0.314, -0.048]
worst area <= 853.50                 +0.143   [+0.119, +0.286]
worst concavity <= 0.35              +0.135   [+0.108, +0.286]
mean concavity > 0.07                -0.048   [-0.114, +0.086]
mean concave points > 0.04           -0.048   [-0.114, +0.086]
worst texture > 23.91                -0.042   [-0.114, +0.108]
```

**Interpretation.** Read each line as: *"For this case, `<condition>` holds.
Compared with what the model predicts when this feature takes values outside
that range, the calibrated probability of benign is higher (positive weight)
or lower (negative weight) by about `<weight>`."* CE computes each weight one
feature at a time, so the weights are not designed to add up to the
prediction.

- **Sign.** A negative weight pulls the probability of *benign* down (towards
  *malignant*); a positive weight pushes it up.
- **Size.** Larger absolute weights matter more for this prediction.
- **Weight interval.** The uncertainty of the effect, derived from the
  calibrated lower and upper predictions. If the interval includes zero, even
  the direction of the effect is uncertain for this prediction. These intervals
  describe the model's response; they are not formal coverage guarantees for
  individual features.

A weight is an *estimated contribution to this model's prediction*. It is not
a causal effect of the feature in the real world.

## B6. Explore alternative explanations

**What.** An **alternative explanation** asks: *if this feature had a value in
a different range, what would the calibrated prediction be?* Each rule shows a
different condition for one feature and the calibrated probability, with its
interval, that the model would give under that condition.

**Why.** Alternatives show how sensitive the prediction is and which features
could change it. That is useful for checking a decision, spotting fragile
predictions or exploring "what if" questions.

**Important.** Alternatives describe the *model's* behaviour, not the world.
"If `worst area` were lower, the model would predict benign" does **not** mean
that changing the tumour would change the diagnosis. They are not causal
counterfactuals.

```python
alternatives = explainer.explore_alternatives(X_test[case:case + 1])
alt = alternatives[0]
rules = alt.get_rules()

base = explanation.prediction["predict"]
print(f"Current calibrated P(benign): {base:.3f}\n")
print(f"{'alternative condition':<34} {'P(benign)':>9}   interval")
order = np.argsort(-np.abs(np.asarray(rules["predict"], dtype=float) - base))[:6]
for i in order:
    print(f"{rules['rule'][i]:<34} {rules['predict'][i]:9.3f}   "
          f"[{rules['predict_low'][i]:.3f}, {rules['predict_high'][i]:.3f}]")
```

```{code-block} text
:caption: Output

Current calibrated P(benign): 0.286

alternative condition              P(benign)   interval
worst concave points < 0.14            0.476   [0.333, 0.600]
worst area > 853.50                    0.143   [0.000, 0.167]
worst concavity > 0.35                 0.151   [0.000, 0.178]
mean concavity < 0.13                  0.333   [0.200, 0.400]
worst area < 745.15                    0.333   [0.200, 0.400]
mean concave points < 0.06             0.333   [0.200, 0.400]
```

**Interpretation.** The rows are sorted by how far the alternative moves the
probability away from the current value. Keep two things apart:

- **The current prediction.** For case 2, the calibrated probability of
  *benign* is 0.286, with a range of 0.167 to 0.333 (from B4). The whole range
  is below 0.5, the point where the predicted label changes, so the model
  predicts *malignant*.
- **Each alternative scenario.** In the first row, if `worst concave points`
  were below 0.14, the probability would be 0.476, with a range of 0.333 to
  0.600. The estimate is still below 0.5, so the predicted label would stay
  *malignant*; but the range now spans 0.5, so in that scenario the
  calibrated output would no longer clearly favour either class.

An alternative describes what the model would do in a different scenario. It
does not change how certain the current prediction is; that is still the
0.167 to 0.333 range above. Alternatives can also move the probability in
either direction: the second and third rows lower it.

## B7. Work with feature conditions

**What.** Every rule is built from a **feature condition**, such as
`worst concave points > 0.14`. CE derives the thresholds from the calibration data.
You can shape which conditions appear in two verified ways:

1. **Combine conditions** into conjunctions, such as two conditions joined
   with `&`, with `add_conjunctions`.
2. **Exclude features** you cannot or should not use as explanations, with
   `features_to_ignore` (feature indices).

**Why.** Some features are not meaningful to the person reading the
explanation, or are fixed by design. Conjunctions show when two conditions
together matter more than either one alone.

```python
conjunctive = explainer.explain_factual(X_test[case:case + 1])
conjunctive.add_conjunctions()  # defaults: top 5 features, pairs of conditions

rules = conjunctive[0].get_rules()
pairs = [i for i, joint in enumerate(rules["is_conjunctive"]) if joint]
pairs = sorted(pairs, key=lambda i: -abs(rules["weight"][i]))[:4]
print(f"{sum(rules['is_conjunctive'])} conjunctive rules added; strongest:")
for i in pairs:
    condition = " ".join(rules["rule"][i].split())
    print(f"  {condition:<52} weight {rules['weight'][i]:+.3f}")
```

```{code-block} text
:caption: Output

70 conjunctive rules added; strongest:
  worst radius <= 16.62 & worst area <= 853.50         weight +0.048
  worst perimeter <= 110.00 & worst area <= 853.50     weight +0.048
  worst area <= 853.50 & worst concavity <= 0.35       weight +0.048
  worst smoothness > 0.15 & worst area <= 853.50       weight +0.048
```

```python
ignore = [feature_names.index("mean radius"), feature_names.index("mean perimeter")]
constrained = explainer.explain_factual(X_test[case:case + 1], features_to_ignore=ignore)

shown = constrained[0].get_rules()["rule"]
print("Any rule on ignored features?",
      any(r.startswith(("mean radius ", "mean perimeter ")) for r in shown))
rule_table(constrained[0], top=4)
```

```{code-block} text
:caption: Output

Any rule on ignored features? False
feature condition                    weight   weight interval
worst concave points > 0.14          -0.190   [-0.314, -0.048]
worst area <= 853.50                 +0.143   [+0.119, +0.286]
worst concavity <= 0.35              +0.135   [+0.108, +0.286]
mean concavity > 0.07                -0.048   [-0.114, +0.086]
```

**Interpretation.** In the first output, rules joined with `&` are conjunctions: both conditions hold for
this case, and the weight is their joint estimated effect. By default CE
combines conditions among the five most important features, two at a time;
larger settings multiply the number of rules and the run time. The second
table contains no rules on the ignored features.

## B8. Interpret the outputs together

The plot shows the factual explanation from B5 for the eight strongest rules.

**Top panel: the prediction.** `P(y=1)` is the probability of class `1`
(*benign*). The vertical line marks CE's single estimate (0.286). The dark bar
runs from 0 to the lower probability (0.167) and the light bar from the lower
to the upper probability (0.333). `P(y!=1)` shows the same for *malignant*:
each value is 1 minus the corresponding *benign* value.

**Lower panel: the rules.** Each row is one rule; red rules raise the
probability of *benign* and blue rules lower it.

- The whole bar, light and dark together, is the rule's **weight interval**.
  For `worst concave points > 0.14` it runs from −0.314 to −0.048.
- The dark part runs from zero to the end of the interval nearest zero.
  Rules whose interval crosses zero have no dark part.
- The point weight itself (−0.190 for that rule) is **not drawn**; read it
  from the table in B5.
- The grey vertical band is this case's own probability range from the top
  panel, redrawn around zero on the weight scale: from 0.286 − 0.333 to
  0.286 − 0.167.
- The right-hand axis shows this case's actual feature values.

```python
factual.plot(0, uncertainty=True, filter_top=8)
```

```{figure} walkthrough_assets/walkthrough-figure-1.png
:alt: Factual explanation plot: calibrated probability with its interval, then one bar per feature condition with its weight and weight interval

Output: factual explanation plot for test case 2.
```

**How to read everything together**

| Output | What it means for this case |
|---|---|
| Predicted label | The class the model chooses. |
| Calibrated probability | CE's best single estimate of the probability of *benign*, combining the two Venn–Abers values. |
| Probability interval | The Venn–Abers lower and upper probability; wide when few calibration cases had similar model scores. |
| Rule weight | How much this condition moves the calibrated probability compared with other values of the same feature. |
| Weight interval | Uncertainty about that contribution; if it spans zero, even the direction of the effect is uncertain. |
| Alternative rule | What the model would predict if one feature were in a different range; not causal. |

A practical reading order: check the interval width first, then the
strongest rules, then whether their intervals exclude zero, and finally
which alternative scenarios move the probability towards or across 0.5.

## B9. Assumptions, guarantees and limitations

**What CE's calibration relies on.** The calibration set and the new cases
should be **exchangeable**: roughly, they come from the same process and their
order does not matter. Independent draws from one stable population satisfy
this; data collected before and after a change in practice may not.

You cannot prove exchangeability from the data alone; it is a judgement
about how the data were collected and how the model will be used.

**What you can rely on, under that assumption.**

- *Classification.* Venn–Abers theory guarantees that, of the two values,
  the one that matches the case's true outcome (`high` if the case is in fact
  benign, `low` if it is not) is calibrated in the long run. When you make a
  prediction the true outcome is unknown, so CE reports both values. The
  single probability CE reports merges the pair into one number that always
  lies between them. The merge is designed to stay close to calibrated, but
  it does not keep the exact guarantee.
- *Interval regression.* CE uses **conformal prediction**, which turns the
  model's errors on the calibration set into intervals. These intervals cover
  the true value at the requested rate *on average over cases* (marginal
  coverage).

**What is not guaranteed**

- Calibration under distribution shift, drift or a different population.
- Coverage for every individual case or subgroup (conditional coverage);
  [Mondrian (conditional) calibration](../foundations/how-to/conditional_calibration.md)
  is the tool for subgroup-aware calibration.
- That an explanation is the "true" reason for a prediction, or that a
  feature has a causal effect.
- That acting on an alternative explanation will change a real outcome.
- Treating Venn–Abers probability bounds as conventional confidence
  intervals.

The [semantics reference](../foundations/concepts/calibrated_interval_semantics.md)
is the canonical statement of these guarantees and non-guarantees.

## B10. Continue with other CE tasks and capabilities

The same three steps (`fit`, `calibrate`, `explain`) work for regression. Only
the meaning of the output changes.

### Interval regression

For a numeric target, `predict(..., uq_interval=True)` returns a point
prediction and a calibrated prediction interval. By default CE requests the
5th and 95th percentiles, a 90% interval.

```python
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

reg_data = load_diabetes()
Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    reg_data.data, reg_data.target, test_size=0.2, random_state=0
)
Xr_proper, Xr_cal, yr_proper, yr_cal = train_test_split(
    Xr_train, yr_train, test_size=0.25, random_state=0
)

regressor = WrapCalibratedExplainer(RandomForestRegressor(random_state=0))
regressor.fit(Xr_proper, yr_proper)
regressor.calibrate(Xr_cal, yr_cal, feature_names=reg_data.feature_names)

point, (lo, hi) = regressor.predict(Xr_test[:3], uq_interval=True)
for p, l, h in zip(point, lo, hi):
    print(f"prediction {p:6.1f}   90% interval [{l:6.1f}, {h:6.1f}]")
```

```{code-block} text
:caption: Output

prediction  273.4   90% interval [ 186.5,  409.2]
prediction  248.2   90% interval [ 161.2,  384.0]
prediction  172.1   90% interval [  85.2,  308.0]
```

**Interpretation.** Under exchangeability, intervals built this way contain the
true value for about 90% of cases on average. They do not promise 90% for
each individual case.

### Probabilistic (thresholded) regression

Pass a `threshold` to ask for the calibrated probability of an event on the
numeric target. CE returns **P(y ≤ threshold)** in the second column.

```python
threshold = 150
p_event, (p_lo, p_hi) = regressor.predict_proba(Xr_test[:3], threshold=threshold, uq_interval=True)
for p, l, h in zip(p_event[:, 1], p_lo, p_hi):
    print(f"P(y <= {threshold}) = {p:.3f}   interval [{l:.3f}, {h:.3f}]")
```

```{code-block} text
:caption: Output

P(y <= 150) = 0.077   interval [0.000, 0.083]
P(y <= 150) = 0.083   interval [0.000, 0.091]
P(y <= 150) = 0.417   interval [0.364, 0.455]
```

**Interpretation.** The first two cases have point predictions far above
150 (273 and 248), so the calibrated probability of an outcome at or below 150
is low. The third, predicted at 172, sits much closer to the threshold, and its
probability is correspondingly higher. The task is still regression; only the
question asked of it changes.

### Guarded explanations

Guarded explanations filter rule candidates through an in-distribution check,
so explanations avoid feature values that are unusual relative to the
calibration data. They use the same calls with `guarded_options`:

```python
from calibrated_explanations.explanations.guarded_options import GuardedOptions

guarded = explainer.explain_factual(
    X_test[case:case + 1], guarded_options=GuardedOptions(confidence=0.9)
)
summary = guarded.get_guarded_audit()["summary"]
print(f"Candidate intervals tested:   {summary['intervals_tested']}")
print(f"Passed the guard:             {summary['intervals_conforming']}")
print(f"Removed by the guard:         {summary['intervals_removed_guard']}")
```

```{code-block} text
:caption: Output

Candidate intervals tested:   189
Passed the guard:             183
Removed by the guard:         6
```

**Interpretation.** The audit shows how many candidate feature intervals the
guard tested and how many it removed as out of distribution. Removed
candidates never appear in the explanation. The guard is a filter, not a
certificate: see the [guarded explanations concept page](../foundations/concepts/guarded_explanations.md)
for what it does and does not establish.

### Where to go next

| You want to | Go to |
|---|---|
| Understand calibration and uncertainty properly | [Calibrated interval semantics](../foundations/concepts/calibrated_interval_semantics.md) |
| Read explanations in more depth | [Interpret calibrated explanations](../foundations/how-to/interpret_explanations.md) |
| Learn more about alternatives | [Alternative explanations](../foundations/concepts/alternatives.md) |
| Go deeper on threshold regression | [Probabilistic regression](../foundations/concepts/probabilistic_regression.md) |
| Use guarded explanations | [Guarded explanations quickstart](quickstart_guarded.md) |
| Look up method signatures | [Quick API](quick_api.md) |
| See how CE calibrates its outputs | [How CE Calibrates](../foundations/concepts/calibration_methods.md) |
| Use CE with your own models and pipelines | [Integrate with pipelines](../foundations/how-to/integrate_with_pipelines.md) |
| Install, configure and integrate CE | [CE Software & Integration](../sections/software-integration.md) |
| Fix installation problems | [Troubleshooting](troubleshooting.md) |

Entry-point tier: Tier 1.
