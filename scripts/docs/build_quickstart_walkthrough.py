"""Generate the Python walkthrough and its code-free companion from executed cells.

Every output shown on ``docs/get-started/quickstart_walkthrough.md`` (the
Python walkthrough, a CE in Practice tutorial) and every number on
``docs/get-started/ce-by-example.md`` (Quick Start Path B, no code) comes from
executing the cells defined below, so text, code and output cannot drift apart.

Writes:
- ``docs/get-started/quickstart_walkthrough.md``: the published page (MyST),
  with code, real outputs and figures.
- ``docs/get-started/ce-by-example.md``: the same example without code; tables
  are built from the executed outputs, and generation stops if they cannot be
  parsed or if a generated statement does not hold for the numbers.
- ``docs/get-started/walkthrough_assets/*.png``: figures produced by the cells.
- ``docs/_static/notebooks/quickstart_walkthrough.ipynb``: the executed
  notebook offered as a download (``_static`` is not parsed by Sphinx).

Requires calibrated-explanations, scikit-learn, matplotlib, nbformat, nbclient
and ipykernel. Usage::

    python scripts/docs/build_quickstart_walkthrough.py [repo_root]

Edit the cells here, never the generated page. Note that ``*.png`` is listed
in ``.gitignore``; add regenerated figures with ``git add -f``.
"""

import sys
from pathlib import Path

import nbformat as nbf
from nbclient import NotebookClient

repo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
page_dir = repo / "docs" / "get-started"
out = repo / "docs" / "_static" / "notebooks" / "quickstart_walkthrough.ipynb"
md_out = page_dir / "quickstart_walkthrough.md"
asset_dir = page_dir / "walkthrough_assets"
BETA = "https://calibrated-explanations-beta.readthedocs.io/en/latest/"

cells = []


def md(text):
    """Append a Markdown cell."""
    cells.append(nbf.v4.new_markdown_cell(text.strip("\n")))


def code(text):
    """Append a code cell."""
    cells.append(nbf.v4.new_code_cell(text.strip("\n")))


md(r"""
# Python walkthrough: from a trained model to calibrated explanations

This page works like a notebook. Each section has a short explanation, the
code, the output that code produced when this page was built, and what the
output means. You can run the same cells yourself: DOWNLOAD_LINK, or copy the
cells into a Python session.

**One of the [Python tutorials](../tutorials/index.md).** Each section follows
the same pattern: a **question**, the code that answers it, the real output,
the concept behind it, and what you can conclude. The same example without
code is [CE by example](ce-by-example.md) in the Quick Start.

**Before you start.** You should know what a feature, a label and a
train/test split are, and why CE adds a calibration step; if not, read
[Why CE](why-ce.md) first. We use **binary classification**; other tasks are
introduced in [Tasks, modes and capabilities](ce-tasks-and-modes.md). No
statistics beyond "probability" and "average" is needed.

**What you will learn**

1. The questions CE answers about one prediction (section 1).
2. Why a model needs three separate data sets (section 2).
3. Why accuracy alone says nothing about probabilities (section 3).
4. Why probabilities need a calibration check (section 4).
5. What CE's calibrated probability and its range are, and what they
   guarantee (section 5).
6. How CE builds an explanation (section 6), and how to read one (section 7).
7. How alternative scenarios relate to the explanation (section 8).
8. What you can and cannot conclude (section 9).

Sections 1–10 form the core path. Regression, guarded explanations and
options for shaping explanations follow as extra sections.

Install the packages once:

```bash
pip install calibrated-explanations scikit-learn matplotlib
```
""")

md(r"""
## 1. The prediction problem and the case we follow

A clinic uses a model to flag tumour samples as *malignant* or *benign*. For
one sample the model says *malignant*. Before anyone acts on that, three
questions matter:

1. **How sure is the model?** Not just which label, but how probable it is,
   and how certain that probability is.
2. **Which measurements drive the prediction?**
3. **What would change it?**

This is an educational example on a public dataset, not clinical decision
support.

CE answers these questions about the **model's behaviour**: calibrated
probabilities with uncertainty, explanations with uncertainty, and
alternative scenarios. It does not diagnose, and it does not tell you what
causes a tumour to be malignant.

We follow one test sample, **case 2**, from raw model output to a calibrated
explanation. First, the data.
""")

md(r"""
## 2. Data and the three data roles

**Question.** What data do we have, and which part may each step use?

We predict whether a breast tumour sample is *malignant* or *benign* from 30
numeric measurements of cell nuclei. The target is one of two labels, so this
is **binary classification**. The dataset ships with scikit-learn and needs no
download.
""")

code(r"""
import numpy as np
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X, y = data.data, data.target
feature_names = list(data.feature_names)

print("Samples, features:", X.shape)
for label, name in enumerate(data.target_names):
    print(f"Class {label} = {name}: {int((y == label).sum())} samples")
""")

md(r"""
**Interpretation.** There are 569 samples and 30 features. Label `0` means
*malignant* and label `1` means *benign*. Remember this mapping: for binary
classification, CE reports the probability of class `1`, which here is
*benign*.

Now we split the data into three parts, each with one job:

| Set | Used for | Seen by the model during training? |
|---|---|---|
| Proper training set | Fitting the model | Yes |
| Calibration set | Calibrating CE's probabilities and explanations | No |
| Test set | Checking performance and explaining new cases | No |

Calibration measures how the trained model behaves on data it has **not**
seen. If calibration used training data, the model would look more reliable
than it is. Using any of these rows in two roles is a form of **data
leakage**.
""")

code(r"""
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
""")

md(r"""
**Interpretation.** About 60% of the data trains the model, 20% calibrates it
and 20% is kept for testing. `stratify` keeps the class balance similar in
each part, and `random_state` makes the split reproducible. One way to
picture the calibration set: it is the evidence CE uses to judge the model,
so the uncertainty ranges later on reflect how much evidence there is; 114
cases is a small evidence base.
""")

md(r"""
## 3. Train the model and evaluate it

**Question.** How good is an ordinary model, before CE is involved?

`WrapCalibratedExplainer` wraps an ordinary scikit-learn model. Training
happens with `fit`, exactly as in scikit-learn; nothing CE-specific has
happened yet. We use a random forest as an example, not a recommendation: CE
works with models that provide `fit` and `predict` (and `predict_proba` for
classification).
""")

code(r"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(
    RandomForestClassifier(n_estimators=100, random_state=42)
)
explainer.fit(X_proper, y_proper)

y_pred_raw = explainer.predict(X_test, calibrated=False)
print(f"Test accuracy: {accuracy_score(y_test, y_pred_raw):.3f}")
""")

md(r"""
**Interpretation.** About 95% of the predicted labels are correct. Accuracy
counts correct labels; it cannot tell us whether a score of 0.16 means a 16%
chance, or how sure the model is about one particular case. For that we look
at the probabilities themselves.
""")

md(r"""
## 4. Why calibration matters

**Question.** Can we take the model's probabilities at face value?

First we **calibrate**: `calibrate` shows CE the held-out calibration set.
The model itself is not changed. Section 5 explains what calibration does;
here we only use it to keep the model's raw scores and CE's calibrated
probabilities side by side.
""")

code(r"""
explainer.calibrate(X_cal, y_cal, feature_names=feature_names)

raw = explainer.predict_proba(X_test, calibrated=False)[:, 1]
print("Raw P(benign), cases 0-4:", raw[:5].round(2))
extreme = (raw == 0) | (raw == 1)
print("Cases with raw probability exactly 0 or 1:", int(extreme.sum()), "of", len(raw))
print("Of those, correctly labelled:", int(((raw[extreme] > 0.5) == y_test[extreme]).sum()))
""")

md(r"""
**Interpretation.**

- A random forest's `predict_proba` averages the class proportions in the
  leaves its trees reach. When every tree agrees, the output is exactly 0
  or 1.
- A probability of exactly 0 or 1 claims certainty. A model trained on 341
  cases rarely has grounds for certainty, so outputs like these are a common
  **reason to check** calibration.
- They are **not evidence** that the scores are wrong: on this test set, every
  extreme prediction was correct. Whether probabilities are calibrated can
  only be judged against observed outcomes on held-out data.

A probability is **calibrated** if, among all cases given about 70%, about
70% turn out positive. Calibration does not judge or retrain the model. It
learns, from cases the model never saw, how the model's scores relate to
observed outcomes, and it attaches an uncertainty range.
""")

md(r"""
## 5. How Venn–Abers calibration works, and what its output means

**Question.** What does CE's calibrated probability mean, and what is guaranteed?

For classification, CE calibrates with **Venn–Abers** predictors. For each
new case:

1. Sort the calibration cases by the model's score.
2. Fit the best *increasing* curve from score to observed outcome (isotonic
   regression).
3. Do this twice: once adding the new case as *benign*, once as *malignant*.
4. Read both curves at the new case's score. This gives a lower and an upper
   probability, `low` and `high`.
5. Merge the two into one estimate, `high / (1 − low + high)`, which always
   lies between them.

```{mermaid}
flowchart LR
    S["model score of the new case"] --> A["fit with the case labelled benign"]
    S --> B["fit with the case labelled malignant"]
    A --> H["upper probability (high)"]
    B --> L["lower probability (low)"]
    H --> M["merged estimate, between low and high"]
    L --> M
```
""")

code(r"""
proba, (low, high) = explainer.predict_proba(X_test[:5], uq_interval=True)
y_pred = explainer.predict(X_test)

print("case  raw    calibrated  range           predicted   true")
for i in range(5):
    print(
        f"{i:>4}  {raw[i]:.2f}   {proba[i, 1]:.3f}       [{low[i]:.3f}, {high[i]:.3f}]  "
        f"{data.target_names[y_pred[i]]:<10}  {data.target_names[y_test[i]]}"
    )
print(f"\nTest accuracy after calibration: {accuracy_score(y_test, y_pred):.3f}")
""")

md(r"""
**Interpretation: what the numbers are.**

- **A pair, not one number.** Venn–Abers produces two probabilities for each
  case, `low` and `high`, from the two fits in step 3.
- **The guarantee belongs to the pair.** Vovk, Petej and Fedorova (2015)
  show that the member of the pair selected by the *true* label (`high` if the
  case is truly benign, `low` if it is truly malignant) is perfectly
  calibrated. Three limits apply: the result assumes the calibration and test
  cases are exchangeable (roughly: drawn from the same stable process); it is
  a property of the predictor over many cases, not a statement about one case;
  and it cannot be used to pick the calibrated member, because the true label
  is unknown when we predict. *Wording under review by the CE authors.*
- **The merged estimate has no exact guarantee.** CE's single number is a
  practical summary between `low` and `high`; merging gives up the exact
  calibration property.
- **What the range is not.** `[low, high]` is not a confidence interval for an
  unknown "true probability" of the case, and it guarantees nothing about one
  individual case.
- **Width.** The width shows how much the calibration curve depends on the
  unknown label of the new case. One way to picture it: it tends to be wider
  where few calibration cases had similar scores.

Case `3` is misclassified (truly benign) and has the widest range of the
five. That is a useful observation, but one case supports no general claim.

Does calibration make the probabilities score better? We can check one common
score on the test set:
""")

code(r"""
from sklearn.metrics import brier_score_loss

cal = explainer.predict_proba(X_test)[:, 1]
print(f"Brier score, raw:        {brier_score_loss(y_test, raw):.4f}")
print(f"Brier score, calibrated: {brier_score_loss(y_test, cal):.4f}")
""")

md(r"""
**Interpretation.** The **Brier score** is the mean squared difference between
the predicted probability of *benign* and the outcome (1 if benign, 0 if
not); **lower is better** and 0 is perfect (Brier, 1950). On these 114 test
cases the calibrated probabilities scored *worse* than the raw ones.

- Calibration does not necessarily improve scores such as the Brier score on
  every dataset or test set.
- This comparison does not test the guarantee above: the Brier score is
  computed on CE's merged estimate, which does not carry the exact guarantee,
  and on one small test set.
- Do not read a cause into the difference (for example "the forest was
  already well calibrated"): this page does not test that.

What CE adds is the validity property of the probability pair and an
uncertainty range for every case. The
[semantics reference](../foundations/concepts/calibrated_interval_semantics.md)
and [How CE Calibrates](../foundations/concepts/calibration_methods.md) give
the full statements and the mathematics.
""")

md(r"""
## 6. How CE builds an explanation

**Question.** Where do the numbers in an explanation come from?

Case 2 is predicted *malignant*. Before reading its explanation, it helps to
know where the numbers come from.

**Scope.** The steps below describe how CE computes a factual explanation in
the version and settings used on this page (binary classification, default
explanation options). They are implementation details, not part of the
definition of a calibrated explanation; other settings or later versions can
differ.

| Step | What CE does here | Depends on (default here) |
|---|---|---|
| 1. Split each feature into two ranges | For each feature, CE finds one split point in the calibration data with a one-split decision tree, trained on the model's *predicted* labels for the calibration cases | discretizer `binaryEntropy`; `condition_source="prediction"` |
| 2. Read off the condition | The case falls on one side of the split, which gives the rule's condition, for example `worst concave points > 0.14` | — |
| 3. Try typical values from the other side | CE takes three typical calibration values from the *other* range (its 25th, 50th and 75th percentiles) and puts each into the case in place of its real value | `sample_percentiles=[25, 50, 75]` |
| 4. Ask the calibrated model again | For each modified case CE gets a calibrated probability, lower bound and upper bound, and averages the three probabilities, the three lower bounds and the three upper bounds separately | — |
| 5. Compute the weight | Weight = the case's calibrated probability − that average. The weight interval runs from the case's probability − the averaged upper bound to the case's probability − the averaged lower bound | — |

**In words:** a weight answers "how different would the calibrated probability
be if this feature took typical values from the other side of the split, with
all other features unchanged?" It compares the model's responses; it is not a
cause.
""")

md(r"""
## 7. The factual explanation of our case

**Question.** Which of case 2's values drive its prediction, and how firmly?

`explain_factual` returns a collection; index it to get one explanation.
""")

code(r"""
case = 2
factual = explainer.explain_factual(X_test[case:case + 1])
explanation = factual[0]

pred = explanation.prediction
print(f"Calibrated P(benign) = {pred['predict']:.3f}  "
      f"range [{pred['low']:.3f}, {pred['high']:.3f}]")
""")

code(r"""
def rule_table(expl, top=6):
    rules = expl.get_rules()
    order = np.argsort(-np.abs(np.asarray(rules["weight"], dtype=float)))[:top]
    print(f"{'feature condition':<34} {'weight':>8}   weight interval")
    for i in order:
        print(f"{rules['rule'][i]:<34} {rules['weight'][i]:+8.3f}   "
              f"[{rules['weight_low'][i]:+.3f}, {rules['weight_high'][i]:+.3f}]")

rule_table(explanation)
weights = np.asarray(explanation.get_rules()["weight"], dtype=float)
print(f"\nSum of all {len(weights)} weights: {weights.sum():+.3f}")
""")

md(r"""
**Interpretation.** Read each line as: *"For this case, `<condition>` holds.
With typical values from the other side of the split instead, the calibrated
probability of benign would be lower (positive weight) or higher (negative
weight) by about `<weight>`."*

- **Sign.** A negative weight means the case's condition pulls the probability
  of *benign* down (towards *malignant*); a positive weight pushes it up.
- **Size.** Larger absolute weights matter more for this prediction.
- **Weight interval.** It comes from the averaged lower and upper bounds in
  step 5. Where an interval spans zero, the averaged bounds do not settle the
  direction of the effect. These intervals are differences of averaged
  Venn–Abers bounds; no guarantee is claimed for them.
- **Weights do not add up to the prediction.** Each weight is computed one
  feature at a time; their sum (printed above) differs from the prediction of 0.286.

The plot shows the same explanation for the eight strongest rules:
""")

code(r"""
%matplotlib inline
factual.plot(0, uncertainty=True, filter_top=8)
""")

md(r"""
**Reading the plot.**

- **Top panel.** `P(y=1)` is the probability of *benign*. The vertical line
  marks CE's single estimate; the dark bar runs from 0 to the lower
  probability and the light bar from the lower to the upper probability.
  `P(y!=1)` shows the same for *malignant*.
- **Lower panel.** One row per rule. With the default plot style, rules that
  raise the probability of *benign* are drawn in red and rules that lower it
  in blue.
- The whole bar, light and dark together, is the rule's weight interval. The
  dark part runs from zero to the end of the interval nearest zero; rules
  whose interval crosses zero have no dark part. The point weight itself is
  not drawn: read it from the table above.
- The grey vertical band is this case's own probability range redrawn around
  zero on the weight scale (from 0.286 − 0.333 to 0.286 − 0.167).
- The right-hand axis shows the case's actual feature values.
""")

md(r"""
## 8. Alternative explanations of our case

**Question.** What would the model predict if one feature were different?

An **alternative explanation** asks: *if one feature had a value in a
different range, what would the calibrated prediction be?* Alternatives use
finer ranges than factual rules (up to eight per feature, in either direction).
""")

code(r"""
alternatives = explainer.explore_alternatives(X_test[case:case + 1])
alt_rules = alternatives[0].get_rules()

base = pred["predict"]
print(f"Current calibrated P(benign): {base:.3f}\n")
print(f"{'alternative condition':<34} {'P(benign)':>9}   range")
order = np.argsort(-np.abs(np.asarray(alt_rules["predict"], dtype=float) - base))[:6]
for i in order:
    print(f"{alt_rules['rule'][i]:<34} {alt_rules['predict'][i]:9.3f}   "
          f"[{alt_rules['predict_low'][i]:.3f}, {alt_rules['predict_high'][i]:.3f}]")
""")

md(r"""
**Interpretation.**

- **The link to the weights.** The first row's probability, 0.476, is the
  average from step 4 behind the strongest factual rule:
  0.286 − 0.476 = −0.190, the weight of `worst concave points > 0.14`.
- **The current prediction.** The calibrated probability of *benign* is 0.286
  with range 0.167 to 0.333. Above 0.5 the predicted label would be *benign*;
  the whole range lies below 0.5, so the model predicts *malignant*.
- **One scenario.** If `worst concave points` were below 0.14, the estimate
  would be 0.476 with range 0.333 to 0.600. The estimate stays below 0.5, but
  the range spans 0.5: in that scenario the calibrated output would no longer
  clearly favour either class. The ranges shown for scenarios are averages of
  Venn–Abers bounds; they do not carry the guarantee from section 5.
- **Direction.** Scenarios can move the probability either way: some rows
  lower it.

Alternatives describe what the **model** would do in a different scenario.
They do not say that changing the tumour would change the diagnosis, and they
do not change how certain the current prediction is.
""")

CONCLUDE = r"""**We can say.** The model predicts *malignant*. CE's calibrated probability of
*benign* is 0.29, with a range of 0.17 to 0.33. The prediction depends most
on `worst concave points` being above 0.14: with typical lower values, the
calibrated probability would be about 0.48, and that scenario's range reaches
above 0.5.

**We cannot say:**

- that 0.29 holds for this individual case, or that its "true" probability
  lies between 0.17 and 0.33;
- that the calibrated probabilities score better than the raw ones: on this
  test set they did not (see the Brier scores above);
- that the measurements cause the outcome;
- that the numbers hold for data from a different population, scanner or
  period: the guarantees assume exchangeability;
- that the weight intervals are formal guarantees;
- anything about other cases, from this one case.
"""

md("## 9. What we can and cannot conclude about case 2\n\n" + CONCLUDE)

md(r"""
## 10. Recap and next steps

- CE answers three questions about one prediction: how sure, which features,
  what would change it.
- Calibration needs its own held-out data; accuracy says nothing about
  probabilities.
- Venn–Abers gives a pair of probabilities whose guarantee holds for the
  pair, under exchangeability; the single number and the range summarise it.
- A factual weight compares the case's calibrated probability with typical
  values from the other side of a split; it is not a cause.
- Alternatives show model behaviour in other scenarios, with their own
  ranges.

**Common mistakes to avoid**

- Calibrating on the training data, or evaluating on the calibration data.
- Reading `[low, high]` as a confidence interval for one case.
- Reading a weight as a cause, or an alternative as a feasible intervention.
- Concluding that calibration improved the model from one small test set.

[Evaluate CE on your own data](../practitioner/evaluate_ce.md) covers these
in more depth. The extra sections below show regression, guarded
explanations and ways to shape explanations. The table at the end lists
where to go next.
""")

md(r"""
## Extra 1. The same workflow for regression

The same three steps (`fit`, `calibrate`, `explain`) work for regression; only
the meaning of the output changes.

### Interval regression

For a numeric target, `predict(..., uq_interval=True)` returns a point
prediction and a calibrated prediction interval. By default CE requests the
5th and 95th percentiles, a 90% interval.
""")

code(r"""
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
""")

md(r"""
**Interpretation.** CE builds these intervals with a conformal predictive
system. Under exchangeability, intervals built this way contain the true value
for about 90% of cases *on average*; they do not promise 90% for each
individual case. *Wording under review by the CE authors.*

### Probabilistic (thresholded) regression

Pass a `threshold` to ask for the calibrated probability of an event on the
numeric target. CE returns **P(y ≤ threshold)** in the second column.
""")

code(r"""
threshold = 150
p_event, (p_lo, p_hi) = regressor.predict_proba(Xr_test[:3], threshold=threshold, uq_interval=True)
for p, l, h in zip(p_event[:, 1], p_lo, p_hi):
    print(f"P(y <= {threshold}) = {p:.3f}   range [{l:.3f}, {h:.3f}]")
""")

md(r"""
**Interpretation.** The first two cases have point predictions far above 150,
so the calibrated probability of an outcome at or below 150 is low. The third
sits closer to the threshold, and its probability is correspondingly higher.
The task is still regression; only the question asked of it changes.
""")

md(r"""
## Extra 2. Guarded explanations

Guarded explanations filter candidate feature ranges through an
in-distribution check, so explanations avoid substituted values that are
unusual relative to the calibration data. They use the same calls with
`guarded_options` (experimental):
""")

code(r"""
from calibrated_explanations.explanations.guarded_options import GuardedOptions

guarded = explainer.explain_factual(
    X_test[case:case + 1], guarded_options=GuardedOptions(confidence=0.9)
)
summary = guarded.get_guarded_audit()["summary"]
print(f"Candidate intervals tested:   {summary['intervals_tested']}")
print(f"Passed the guard:             {summary['intervals_conforming']}")
print(f"Removed by the guard:         {summary['intervals_removed_guard']}")
""")

md(r"""
**Interpretation.** The audit shows how many candidate feature ranges the
guard tested and how many it removed. Removed candidates never appear in the
explanation. The guard is a filter, not a certificate: it checks whether each
substituted value is plausible, not whether the case itself is out of
distribution. See the [guarded explanations concept page](../foundations/concepts/guarded_explanations.md).
""")

md(r"""
## Extra 3. Shaping explanations

You can exclude features that are not meaningful to the reader, with
`features_to_ignore` (feature indices). Here we exclude the strongest
feature from section 7 and look at the re-ranked rules:
""")

code(r"""
ignore = [feature_names.index("worst concave points")]
constrained = explainer.explain_factual(X_test[case:case + 1], features_to_ignore=ignore)

shown = constrained[0].get_rules()["rule"]
print("Any rule on the ignored feature?",
      any(r.startswith("worst concave points ") for r in shown))
rule_table(constrained[0], top=4)
""")

md(r"""
**Interpretation.** The ignored feature no longer appears, and the remaining
rules keep their own weights. Excluding a feature changes what is shown, not
the model or its prediction.

You can also add **conjunctions** (rules that combine two conditions, joined
with `&`) with `add_conjunctions()`. Conjunctive weights are computed
differently from single-rule weights: compare conjunctions with each other,
not with single rules. *How to read them is under review by the CE authors.*
""")

md(r"""
### Where to go next

| You want to | Go to |
|---|---|
| Understand calibration and uncertainty properly | [Calibrated interval semantics](../foundations/concepts/calibrated_interval_semantics.md) |
| Read explanations in more depth | [Interpret calibrated explanations](../foundations/how-to/interpret_explanations.md) |
| Learn more about alternatives | [Alternative explanations](../foundations/concepts/alternatives.md) |
| Go deeper on threshold regression | [Probabilistic regression](../foundations/concepts/probabilistic_regression.md) |
| Use guarded explanations | [Guarded explanations tutorial](quickstart_guarded.md) |
| Look up method signatures | [Quick API](quick_api.md) |
| See how CE calibrates its outputs | [How CE Calibrates](../foundations/concepts/calibration_methods.md) |
| See the whole workflow and a learning path | [The CE workflow](../foundations/concepts/ce_workflow.md) |
| Use CE with your own models and pipelines | [Integrate with pipelines](../foundations/how-to/integrate_with_pipelines.md) |
| Read this example again without code | [CE by example](ce-by-example.md) |
| Find the other Python tutorials | [Python tutorials](../tutorials/index.md) |
| Choose a task and mode for your problem | [Tasks, modes and capabilities](ce-tasks-and-modes.md) |
| Apply CE to your own data | [Apply CE to your own data](apply-to-your-data.md) |
| Install, configure and integrate CE | [CE Software & Integration](../sections/software-integration.md) |
| Fix installation problems | [Troubleshooting](troubleshooting.md) |
""")


# Numbers quoted in the prose above must come from the executed outputs.
# If CE's behaviour changes, generation stops instead of publishing stale text.
PROSE_NUMBERS = [
    "0.286", "[0.167, 0.333]", "0.476", "[0.333, 0.600]", "-0.190",
    "worst concave points > 0.14", "worst concave points < 0.14",
]

import base64, re, tempfile

nb = nbf.v4.new_notebook()
nb.cells = cells
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nb.metadata["language_info"] = {"name": "python"}
with tempfile.TemporaryDirectory() as run_dir:
    NotebookClient(
        nb, timeout=120, kernel_name="python3", resources={"metadata": {"path": run_dir}}
    ).execute()
for index, c in enumerate(nb.cells):
    c.id = f"cell-{index:02d}"  # stable ids keep the downloadable notebook reproducible
    if c.cell_type == "code":
        merged = []
        for o in c.outputs:
            if o.get("output_type") == "stream" and o.get("name") == "stderr":
                continue  # drop warnings; keep stdout, results and figures
            if (
                o.get("output_type") == "stream"
                and merged
                and merged[-1].get("output_type") == "stream"
            ):
                # the kernel may split one print into several messages
                merged[-1]["text"] += o["text"]
                continue
            merged.append(o)
        c.outputs = merged
        c.metadata = {}
        c.execution_count = None

outputs_text = "\n".join(
    o.get("text", "") for c in nb.cells if c.cell_type == "code" for o in c.outputs
)
missing = [n for n in PROSE_NUMBERS if n not in outputs_text]
if missing:
    raise SystemExit(f"prose numbers not found in generated outputs: {missing}")

# --- 1. Published MyST page: text, code, real outputs, saved figures ---------
asset_dir.mkdir(exist_ok=True)
parts, fig_no = [], 0
for c in nb.cells:
    if c.cell_type == "markdown":
        parts.append(
            c.source.replace(
                "DOWNLOAD_LINK",
                "[download this walkthrough as a Jupyter notebook]"
                "(path:../_static/notebooks/quickstart_walkthrough.ipynb)",
            )
        )
        continue
    shown = "\n".join(line for line in c.source.splitlines() if not line.startswith("%"))
    parts.append("```python\n" + shown.strip("\n") + "\n```")
    for o in c.outputs:
        if o.output_type == "stream":
            parts.append("```{code-block} text\n:caption: Output\n\n" + o.text.rstrip() + "\n```")
        elif o.output_type in ("display_data", "execute_result") and "image/png" in o.data:
            fig_no += 1
            name = f"walkthrough-figure-{fig_no}.png"
            (asset_dir / name).write_bytes(base64.b64decode(o.data["image/png"]))
            parts.append(
                f"```{{figure}} walkthrough_assets/{name}\n"
                ":alt: Factual explanation plot: calibrated probability with its interval, "
                "then one bar per feature condition with its weight and weight interval\n\n"
                "Output: factual explanation plot for test case 2.\n```"
            )
        elif o.output_type == "execute_result" and "text/plain" in o.data:
            parts.append(
                "```{code-block} text\n:caption: Output\n\n" + o.data["text/plain"] + "\n```"
            )
        elif o.output_type == "error":
            raise SystemExit(f"cell failed: {o.ename}: {o.evalue}")
md_out.write_text("\n\n".join(parts) + "\n\nEntry-point tier: Tier 1.\n", encoding="utf-8")


# --- 2. Downloadable notebook: absolute links to the Beta site ---------------
def absolute(m):
    target = (Path("get-started") / m.group(1)).as_posix()
    parts_ = []
    for seg in target.split("/"):
        if seg == "..":
            parts_.pop()
        else:
            parts_.append(seg)
    return "](" + BETA + "/".join(parts_) + ".html)"


for c in nb.cells:
    if c.cell_type == "markdown":
        c.source = re.sub(r"\]\(([\w./-]+)\.md\)", absolute, c.source).replace(
            "DOWNLOAD_LINK", "run them in this notebook"
        )
out.parent.mkdir(parents=True, exist_ok=True)
nbf.write(nb, out)
print("wrote", md_out.name, out.name, fig_no, "figure(s)")


# --- 3. Code-free companion: Quick Start Path B --------------------------------
def output_of(marker):
    """Stdout text of the code cell whose source contains ``marker``."""
    for c in nb.cells:
        if c.cell_type == "code" and marker in c.source:
            return "".join(o.get("text", "") for o in c.outputs if o.get("output_type") == "stream")
    raise SystemExit(f"no code cell contains {marker!r}")


def grab(pattern, text, what):
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        raise SystemExit(f"ce-by-example: cannot parse {what}")
    return m.groups()


def check(condition, what):
    if not condition:
        raise SystemExit(f"ce-by-example: statement no longer holds: {what}")


t_data = output_of('print("Samples, features:"')
n_samples, n_features = grab(r"Samples, features: \((\d+), (\d+)\)", t_data, "data shape")
n_mal, = grab(r"Class 0 = malignant: (\d+) samples", t_data, "malignant count")
n_ben, = grab(r"Class 1 = benign: (\d+) samples", t_data, "benign count")

t_split = output_of('print(f"Proper training:')
n_proper, = grab(r"Proper training: (\d+) samples", t_split, "proper size")
n_cal, = grab(r"Calibration:\s+(\d+) samples", t_split, "calibration size")
n_test, = grab(r"Test:\s+(\d+) samples", t_split, "test size")

acc, = grab(r"Test accuracy: ([\d.]+)", output_of('print(f"Test accuracy: {accuracy_score(y_test, y_pred_raw)'), "accuracy")
t_raw = output_of('print("Cases with raw probability exactly 0 or 1:"')
n_extreme, n_test2 = grab(r"exactly 0 or 1: (\d+) of (\d+)", t_raw, "extreme count")
n_extreme_ok, = grab(r"correctly labelled: (\d+)", t_raw, "extreme correct")

t_cases = output_of('print("case  raw    calibrated  range')
rows5 = re.findall(r"^\s*(\d+)\s+([\d.]+)\s+([\d.]+)\s+\[([\d.]+), ([\d.]+)\]\s+(\w+)\s+(\w+)\s*$", t_cases, re.MULTILINE)
check(len(rows5) == 5, "five cases parsed")
widths = [float(r[4]) - float(r[3]) for r in rows5]
widest = max(range(5), key=lambda i: widths[i])
misclassified = [int(r[0]) for r in rows5 if r[5] != r[6]]

brier_raw, = grab(r"Brier score, raw:\s+([\d.]+)", output_of("brier_score_loss"), "raw Brier")
brier_cal, = grab(r"Brier score, calibrated:\s+([\d.]+)", output_of("brier_score_loss"), "calibrated Brier")

t_case = output_of('print(f"Calibrated P(benign) = ')
p2, lo2, hi2 = grab(r"Calibrated P\(benign\) = ([\d.]+)\s+range \[([\d.]+), ([\d.]+)\]", t_case, "case 2 prediction")
check(float(hi2) < 0.5, "the whole range of case 2 lies below 0.5")

t_rules = output_of("rule_table(explanation)")
rules = re.findall(r"^(.+?)\s+([+-]\d\.\d{3})\s+\[([+-]\d\.\d{3}), ([+-]\d\.\d{3})\]\s*$", t_rules, re.MULTILINE)
check(len(rules) >= 4, "factual rules parsed")
weight_sum, = grab(r"Sum of all \d+ weights: ([+-][\d.]+)", t_rules, "weight sum")
top_rule, top_w, top_lo, top_hi = rules[0]
check(float(top_w) < 0 and float(top_hi) < 0, "strongest rule has a negative weight with its whole range below 0")
crossing = next((r for r in rules if float(r[2]) < 0 < float(r[3])), None)
check(crossing is not None, "at least one shown rule has a range that includes 0")

t_alt = output_of("alt_rules = alternatives[0].get_rules()")
alts = re.findall(r"^(.+?)\s+(\d\.\d{3})\s+\[(\d\.\d{3}), (\d\.\d{3})\]\s*$", t_alt, re.MULTILINE)
alts = [a for a in alts if not a[0].startswith("Current")]
check(len(alts) >= 3, "alternatives parsed")
a_rule, a_p, a_lo, a_hi = alts[0]
check(float(a_p) < 0.5 < float(a_hi), "top alternative stays below 0.5 but its range spans 0.5")


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out)


def signed(x):
    return x.replace("-", "−")


better = "better (lower)" if float(brier_cal) < float(brier_raw) else "worse (higher)"
widest_note = (
    f"- **One observation.** Case {rows5[widest][0]} has the widest range of the five and is\n"
    "  the one the model gets wrong. That is a useful observation, but one case\n"
    "  supports no general claim.\n"
    if int(rows5[widest][0]) in misclassified else ""
)

page = f"""# CE by example: one prediction, explained

**Path B of the Quick Start.** This page follows one real prediction from a
model's raw output to a calibrated explanation, **without code**. Every number,
table and the plot below are CE outputs produced by the code of the
[Python walkthrough](quickstart_walkthrough.md), which runs the same example
step by step; this page is regenerated from that run. This is an educational
example on a public dataset, not clinical decision support.

**Before this:** [Why CE](why-ce.md) (Path A) explains why CE adds a calibration
step and how to read its outputs.

## 1. The question

A model flags breast-tumour samples as *malignant* or *benign* from
{n_features} measurements of cell nuclei. For one test sample, **case 2**, the
model says *malignant*. Before anyone acts on it, three questions matter:

1. **How sure is the model**, and how certain is that probability?
2. **Which measurements drive the prediction?**
3. **What would change it?**

## 2. The data and its three roles

The dataset has {n_samples} samples ({n_mal} *malignant*, {n_ben} *benign*). CE
reports the probability of class 1, which here is *benign*.

{table(["Set", "Cases", "Job", "Used to train the model?"], [
    ["Proper training", n_proper, "Fit the model", "Yes"],
    ["Calibration", n_cal, "Let CE measure how the model's outputs relate to real outcomes", "No"],
    ["Test", n_test, "Check the results on cases nobody has used", "No"],
])}

## 3. The model alone

A random forest predicts the correct label for about {float(acc) * 100:.0f}% of
the test cases (accuracy {acc}). Accuracy counts correct labels; it does not say
whether the model's probabilities can be taken at face value. On the test set,
{n_extreme} of the {n_test2} raw probabilities are exactly 0 or 1, a claim of
certainty that is a common reason to check calibration. ({n_extreme_ok} of
those {n_extreme} were correct, so this is not evidence that they are wrong.)

## 4. Calibrated probabilities, each with a range

CE calibrates the model on the calibration set; for classification it uses
**Venn–Abers predictors**. The model itself is not changed. For the first five
test cases, the probability of *benign* from the model alone and from CE:

{table(["Case", "Model alone", "CE", "CE range", "Predicted (true)"],
       [[r[0], r[1], r[2], f"[{r[3]}, {r[4]}]", f"*{r[5]}* ({r[6]})"] for r in rows5])}

How to read the CE columns:

- **Two values behind every range.** CE calibrates twice, once as if the case
  were *benign* and once as if it were *malignant*. In the long run, the value
  that matches the true outcome is calibrated; because that outcome is unknown
  when you predict, CE reports both as the lower and upper value. The single
  calibrated probability lies between them and does not carry that exact
  property. *Wording under review by the CE authors.*
- **What the range is not.** It is not a confidence interval for a "true
  probability" of the case, and it guarantees nothing about one individual
  case. These statements hold over many cases, assuming the calibration data
  and new cases come from the same stable process.
{widest_note}- **Not a guaranteed score improvement.** On this test set the Brier score
  (the mean squared difference between probability and outcome; lower is
  better) is {brier_raw} for the model alone and {brier_cal} with CE, so CE's
  probabilities scored {better} here. One small test set settles nothing either
  way.

## 5. Why case 2 is predicted *malignant*

For case 2, CE's calibrated probability of *benign* is **{p2}**, with range
**[{lo2}, {hi2}]**. The probability is below 0.5, so the predicted label is
*malignant*; the whole range also lies below 0.5, so the calibration data
support that label throughout the range.

CE's **factual explanation** lists conditions that hold for this case. Each
condition has a **weight**: how much the calibrated probability of *benign*
would differ if that feature took typical values from the other side of the
condition, with all other features unchanged. Each weight has its own range.
The six strongest:

{table(["Condition (holds for case 2)", "Weight", "Weight range"],
       [[f"`{r[0]}`", signed(r[1]), f"[{signed(r[2])}, {signed(r[3])}]"] for r in rules])}

- **Sign.** A negative weight means the condition lowers the probability of
  *benign* (towards *malignant*); a positive weight raises it.
- **The strongest reason** is `{top_rule}`: with typical values from the other
  side instead, the calibrated probability of *benign* would be about
  {abs(float(top_w)):.2f} higher. Its whole weight range lies below 0: the
  averaged lower and upper bounds agree on the direction. (No formal guarantee
  is claimed for weight ranges.)
- **Uncertain direction.** For `{crossing[0]}` the weight range includes 0: the
  averaged bounds do not settle whether it raises or lowers the probability.
- **Not a sum.** Each weight is computed one feature at a time; the weights do
  not add up to the prediction (their sum is {signed(weight_sum)}).
- **Not a cause.** A weight compares the model's responses; it says nothing
  about what causes a tumour to be malignant.

```{{figure}} walkthrough_assets/walkthrough-figure-1.png
:alt: Factual explanation plot for case 2. Top: calibrated probability of benign {p2} with its range from {lo2} to {hi2}. Below: one bar per condition showing its weight range; worst concave points above 0.14 has the largest range entirely below zero.

CE output for case 2, drawn by CE's own plot function in the Python
walkthrough. Each bar covers a weight's range; red bars raise the probability
of *benign*, blue bars lower it.
```

The [guide to reading CE explanations](../foundations/how-to/interpret_explanations.md)
explains every element of this plot.

## 6. What would change it: alternative explanations

An **alternative explanation** asks: *if one feature had a value in a
different range, what would the calibrated probability be?*

{table(["If, instead, …", "Calibrated P(benign)", "Range"],
       [[f"`{a[0]}`", a[1], f"[{a[2]}, {a[3]}]"] for a in alts])}

- If `{a_rule}` held, the calibrated
  probability of *benign* would be **{a_p}**, with range [{a_lo}, {a_hi}]. The
  estimate stays below 0.5, but the range reaches above it: in that scenario CE
  would no longer clearly favour either class.
- Alternatives describe how the **model** would respond. They are not
  recommendations, and they do not say that changing a measurement would
  change the real outcome.

## 7. What we can and cannot conclude

{CONCLUDE.strip()}

## Continue

- **Run it yourself:** the [Python walkthrough](quickstart_walkthrough.md)
  shows the code and outputs behind this page, with a downloadable notebook.
- **Next:** [Tasks, modes and capabilities](ce-tasks-and-modes.md) (Path C),
  for regression and the other CE modes.
- **Go deeper:** [How CE calibrates: Venn–Abers predictors](../foundations/concepts/calibration_methods.md)
  (section 2), [The CE workflow](../foundations/concepts/ce_workflow.md) (how an
  explanation is built) and the formal
  [guarantees by mode](../foundations/concepts/calibrated_interval_semantics.md).
- **See also:** [How to read CE explanations](../foundations/how-to/interpret_explanations.md).
- **Before this:** [Why CE](why-ce.md).

Entry-point tier: Tier 1.
"""
companion = page_dir / "ce-by-example.md"
companion.write_text(page, encoding="utf-8")
print("wrote", companion.name)
