# Your First CE Explanation in Python

This is **Path B** of the {doc}`Quick Start <try-in-browser>`: install the open-source
CE library and run a complete example on your own computer. You follow one patient
(classification) and one housing district (regression) from raw data to a calibrated
prediction, a factual explanation and alternative explanations, and then ask a
threshold question about the same district. Every code block runs as written, in
order, in one Python session, and every printed output below is checked by the
documentation tests. It takes about 30 minutes.

Prefer not to install anything yet? Use **Path A** of the Quick Start: the
{ref}`Expert Hub <qs-expert-lab>` or the {ref}`Decision Lab <try-decision-lab>`.

<span id="qs-worked-cases"></span>

## Step 1. Prerequisites

| You need | Details |
|---|---|
| Python | 3.10 or later (`requires-python = ">=3.10"`). The outputs on this page were produced with Python 3.13 |
| Internet access | The example data are read from the CE repository on GitHub |
| About 200 MB of disk space | For the virtual environment with scikit-learn, pandas and matplotlib |

**Tested versions.** Every output on this page was produced, identically, with the
released CE 1.0.2 (installed from PyPI with scikit-learn 1.9.1 on Python 3.13.7) and
with the 1.1.0 development version these pages are built from. Other versions of
scikit-learn can change the numbers slightly.

## Step 2. Install CE

Create a virtual environment so that CE and its dependencies stay separate from other
projects, then install CE with the `viz` extra, which adds the plots.

**macOS and Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install "calibrated-explanations[viz]"
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install "calibrated-explanations[viz]"
```

Check that the installation works:

```bash
python -c "import calibrated_explanations as ce; print(ce.__version__)"
```

Other options, such as conda, are in {doc}`Installation <installation>`. If something
fails, see {doc}`Troubleshooting <troubleshooting>`.

## Step 3. Import the libraries

Start Python (or a Jupyter notebook) in the activated environment and run:

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from calibrated_explanations import WrapCalibratedExplainer
```

`WrapCalibratedExplainer` wraps any scikit-learn-style model. It adds calibration,
predictions with uncertainty and explanations; the model itself is trained as usual.

(try-step-1)=
## Step 4. Load a dataset

The first case is **classification**: the target is a category. The data are the Pima
Indians Diabetes data: each row is a patient (an *observation*), described by eight
*features*, and the *target* `Y` is 1 for diabetes and 0 for no diabetes.

```python
DATA = ("https://raw.githubusercontent.com/Moffran/"
        "calibrated_explanations/main/tests/data/")
diab = pd.read_csv(DATA + "diabetes_full.csv")
Xc, yc = diab.drop(columns="Y"), diab["Y"]
print(list(Xc.columns))
print(yc.value_counts().to_dict())
```

```text
['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
{0: 500, 1: 268}
```

There are 500 patients without and 268 with diabetes. In this dataset a value of 0 for,
say, blood pressure means *not measured*.

## Step 5. Split the data into training, calibration and test sets

CE needs **three** separate parts of the labelled data, each with one job:

| Part | Job |
|---|---|
| **Training set** | Teaches the model how to make predictions |
| **Calibration set** | Labelled cases the model never sees during training. CE compares the model's outputs on them with the known outcomes to calibrate the predictions |
| **Test set** | Plays the role of new cases, which we predict and explain |

```python
Xc_rest, Xc_test, yc_rest, yc_test = train_test_split(
    Xc, yc, test_size=0.20, stratify=yc, random_state=42)
Xc_train, Xc_cal, yc_train, yc_cal = train_test_split(
    Xc_rest, yc_rest, test_size=0.33 / 0.80,
    stratify=yc_rest, random_state=42)
print("train", len(Xc_train), "cal", len(Xc_cal),
      "test", len(Xc_test))
```

```text
train 360 cal 254 test 154
```

The proportions (47 % training, 33 % calibration, 20 % test) match the Expert Hub's
defaults. **Avoid data leakage:** never use the calibration or test rows to train the
model, and do not reuse the calibration set to evaluate it.

(try-step-2)=
## Step 6. Train a predictive model

Wrap a random forest and train it on the training set only.

```python
clf = WrapCalibratedExplainer(
    RandomForestClassifier(n_estimators=100, random_state=42))
clf.fit(Xc_train.to_numpy(), yc_train.to_numpy())
print("fitted:", clf.fitted)
```

```text
fitted: True
```

## Step 7. Calibrate with the held-out calibration set

```python
clf.calibrate(
    Xc_cal.to_numpy(), yc_cal.to_numpy(),
    feature_names=list(Xc.columns),
    class_labels={0: "no diabetes", 1: "diabetes"})
print("calibrated:", clf.calibrated)
```

```text
calibrated: True
```

**Why a separate set?** A model is usually more confident on the data it was trained on
than on new data. To learn how reliable its outputs are, CE needs labelled cases the
model has never seen. For classification, CE calibrates with a
{term}`Venn–Abers predictor`; the method is explained in
{doc}`Calibration by task <../foundations/concepts/calibration_methods>`.

(try-step-3)=
## Step 8. Generate a prediction with its uncertainty

Predict one test patient and ask for the range.

```python
c_case = Xc_test.to_numpy()[112:113]
proba, (low, high) = clf.predict_proba(c_case, uq_interval=True)
print(f"P(diabetes) = {proba[0, 1]:.3f}  "
      f"range [{low[0]:.3f}, {high[0]:.3f}]")
print("true label:", yc_test.iloc[112])
```

```text
P(diabetes) = 0.510  range [0.467, 0.556]
true label: 1
```

**Reading it.** A decision rule at 0.5 would label the point prediction *diabetes*. The
lower and upper values [0.467, 0.556] straddle that threshold, which shows why the
point prediction alone gives an incomplete picture. For this binary case all three
numbers are probabilities between 0 and 1 (multiclass bounds are normalised
differently; see {doc}`ce-tasks-and-modes`).

(try-step-4)=
## Step 9. Generate a factual explanation

Ask *why* CE predicts what it does for this patient.

```python
c_factual = clf.explain_factual(c_case)
rules = c_factual[0].get_rules()
order = sorted(range(len(rules["weight"])),
               key=lambda i: -abs(rules["weight"][i]))
for i in order[:4]:
    print(f"{rules['rule'][i]:22s} {rules['weight'][i]:+.3f} "
          f"[{rules['weight_low'][i]:+.3f}, "
          f"{rules['weight_high'][i]:+.3f}]")
c_factual.plot(uncertainty=True)
```

```text
Age > 28.50            +0.290 [+0.286, +0.303]
Insulin > 113.00       +0.290 [+0.286, +0.303]
Glucose <= 132.50      -0.146 [-0.162, -0.139]
DiabetesPedigreeFunction > 0.50 +0.085 [+0.049, +0.130]
```

Each line is a **condition that is true for this patient**, its *weight* and the range
of that weight. A weight is how much the condition moves the prediction, in probability
points. Weights are not causal and do not add up to the prediction.

```{figure} try_assets/try-cls-factual.png
:alt: CE factual plot for the diabetes case with six numbered callouts. Top panel, probability bars for diabetes, about 0.51 with a light range from 0.47 to 0.56, and for not diabetes. Lower panel, feature weights from about minus 0.16 to plus 0.3; Age greater than 28.5 and Insulin greater than 113 push towards diabetes, Glucose at most 132.5 pushes away; a grey band surrounds zero.
:name: try-cls-factual-figure

Diabetes case, factual plot. Inspect whether the probability range crosses 0.5, then
which weight ranges stay on one side of zero.
{download}`Full-size diabetes factual plot <try_assets/try-cls-factual.png>`.
```

1. **Prediction.** The red bar is P(diabetes); the vertical marker is the calibrated
   probability (0.510) and the light part is its range (0.467 to 0.556). The blue bar
   below is P(not diabetes).
2. **Axis.** Probability, from 0 to 1. The weights below use their own axis, *Feature
   weights*, in probability points.
3. **Weight bar.** One condition that holds for this patient. Red, to the right, raises
   P(diabetes); blue, to the left, lowers it.
4. **Weight range.** The dark part runs from 0 to the end of the range nearest 0; the
   light part is the rest of the range. A range that crosses 0 has no dark part: its
   direction is uncertain.
5. **Instance values.** The patient's own value for each feature.
6. **Grey band.** The prediction's own range, redrawn on the weight scale. It is not a
   confidence region for the weights.

Every element of these plots is explained in
{doc}`How to read CE explanations <../foundations/how-to/interpret_explanations>`.

(try-step-5)=
## Step 10. Explore alternative explanations

Ask what CE would predict if one feature were in another range.

```python
c_alts = clf.explore_alternatives(c_case)
alt = c_alts[0].get_rules()
for i, rule in enumerate(alt["rule"]):
    if rule.startswith("BMI"):
        print(f"{rule:14s} P(diabetes) {alt['predict'][i]:.3f} "
              f"[{alt['predict_low'][i]:.3f}, "
              f"{alt['predict_high'][i]:.3f}]")
c_alts.plot(filter_top=None)
```

```text
BMI < 24.90    P(diabetes) 0.220 [0.207, 0.224]
BMI > 29.80    P(diabetes) 0.577 [0.569, 0.588]
```

**Reading it.** This patient's BMI is 28.7. If it were below 24.9, CE would predict
0.220, and the whole range [0.207, 0.224] is below 0.5: the prediction would change to
*no diabetes*. Above 29.8 it would rise to 0.577.

```{figure} try_assets/try-cls-alternatives.png
:alt: CE alternative plot for the diabetes case with four numbered callouts. Fourteen alternative conditions on a probability axis from 0 to 1. A shaded band from 0.47 to 0.56 marks the current prediction. Seven alternatives, including BMI below 24.9 at about 0.21 to 0.22, lie below 0.5; the others lie above.
:name: try-cls-alternatives-figure

Diabetes case, alternative plot. Inspect which alternatives lie wholly below 0.5, where
the predicted class would change.
{download}`Full-size diabetes alternative plot <try_assets/try-cls-alternatives.png>`.
```

1. **Current prediction.** The shaded band is the range of the current prediction (0.467
   to 0.556), split at 0.5: the blue part is below 0.5, the red part above.
2. **Axis.** Probability of the class *diabetes*, from 0 to 1.
3. **One alternative.** *BMI < 24.90*: the bar is the range CE predicts if that condition
   held instead. Blue bars lie below 0.5 (the prediction would become *no diabetes*), red
   bars above.
4. **Instance values.** The patient's actual value for each feature.

An alternative describes how **the model** responds, not what would happen if you
changed the world: a lower BMI in the data is not a treatment plan. See
{doc}`Factual and alternative explanations <../foundations/concepts/alternatives>`.

## Step 11. Explore regression: a value with a prediction interval

The second case is **regression**: the target is a number, the median house value of a
California district, in **US dollars**. The steps are the same: load, split, train,
calibrate, predict, explain.

```python
house = pd.read_csv(DATA + "reg/housing.csv", sep=";").dropna()
Xr = house.drop(columns="median_house_value")
yr = house["median_house_value"]

Xr_rest, Xr_test, yr_rest, yr_test = train_test_split(
    Xr, yr, test_size=0.20, random_state=42)
Xr_train, Xr_cal, yr_train, yr_cal = train_test_split(
    Xr_rest, yr_rest, test_size=0.33 / 0.80,
    random_state=42)
print(list(Xr.columns))
print("train", len(Xr_train), "cal", len(Xr_cal),
      "test", len(Xr_test))
```

```text
['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'ocean_proximity']
train 9603 cal 6743 test 4087
```

`ocean_proximity` is a code: 0 means inland; 1–4 mean near the bay, within an hour of
the ocean, near the ocean, or on an island. `median_income` is in tens of thousands of
dollars.

```python
reg = WrapCalibratedExplainer(
    RandomForestRegressor(n_estimators=100, random_state=42))
reg.fit(Xr_train.to_numpy(), yr_train.to_numpy())
reg.calibrate(
    Xr_cal.to_numpy(), yr_cal.to_numpy(),
    feature_names=list(Xr.columns))
print("fitted:", reg.fitted, " calibrated:", reg.calibrated)
```

```text
fitted: True  calibrated: True
```

For regression, CE calibrates with a
{term}`conformal predictive system <Conformal predictive system>` (CPS).

```python
r_case = Xr_test.to_numpy()[:1]
pred, (low, high) = reg.predict(r_case, uq_interval=True)
print(f"prediction = ${pred[0]:,.0f}  "
      f"range [${low[0]:,.0f}, ${high[0]:,.0f}]")
print(f"true value: ${yr_test.iloc[0]:,.0f}")
```

```text
prediction = $237,814  range [$172,503, $327,324]
true value: $245,800
```

**Reading it.** The range is a **prediction interval for the house value**, in dollars.
By default it runs from the 5th to the 95th percentile, a 90 % interval. It spans about
$155,000, which matters if a decision depends on whether the value exceeds a given
price.

```python
r_factual = reg.explain_factual(r_case)
rules = r_factual[0].get_rules()
order = sorted(range(len(rules["weight"])),
               key=lambda i: -abs(rules["weight"][i]))
for i in order[:4]:
    print(f"{rules['rule'][i]:24s} {rules['weight'][i]:+9,.0f} "
          f"[{rules['weight_low'][i]:+9,.0f}, "
          f"{rules['weight_high'][i]:+9,.0f}]")
r_factual.plot(uncertainty=True)
```

```text
ocean_proximity > 0.50     +87,147 [   -2,363,  +152,458]
median_income <= 5.00      -86,776 [ -176,285,   -21,465]
longitude > -121.78        -85,016 [ -174,525,   -19,704]
total_bedrooms <= 704.50   -37,395 [ -126,904,   +27,917]
```

Here the weights are in **dollars**.

```{figure} try_assets/try-reg-factual.png
:alt: CE factual plot for the housing case with five numbered callouts. Top panel, the median prediction about 238,000 dollars with a 90 percent interval from about 173,000 to 327,000 dollars. Lower panel, feature weights in dollars; only median income and longitude have ranges entirely below zero, the other ranges cross zero.
:name: try-reg-factual-figure

Housing case, factual plot. Inspect the width of the interval, then which weight ranges
stay on one side of zero.
{download}`Full-size housing factual plot <try_assets/try-reg-factual.png>`.
```

1. **Prediction.** The marker is the median prediction ($237,814); the band is the 90 %
   interval ($172,503 to $327,324).
2. **Axis.** The top axis is the house value in US dollars. The weights below use their
   own axis, *Feature weights*, also in dollars.
3. **Weight bar.** One condition that holds for this district. In regression plots, blue
   to the right raises the prediction and red to the left lowers it (the opposite
   colours to classification).
4. **Weight range.** Only a range that stays on one side of 0 has a dark part. Here only
   `median_income ≤ 5.00` and `longitude > -121.78` do; for every other condition, even
   the direction is uncertain.
5. **Instance values.** The district's own value for each feature.

```python
r_alts = reg.explore_alternatives(r_case)
alt = r_alts[0].get_rules()
for i, rule in enumerate(alt["rule"]):
    if rule.startswith("median_income"):
        print(f"{rule:22s} ${alt['predict'][i]:,.0f} "
              f"[${alt['predict_low'][i]:,.0f}, "
              f"${alt['predict_high'][i]:,.0f}]")
r_alts.plot(filter_top=None)
```

```text
median_income < 3.16   $213,767 [$148,455, $303,276]
median_income > 3.93   $282,174 [$216,863, $371,683]
```

**Reading it.** This district's `median_income` is 3.18. Above 3.93, the median
prediction would rise to about $282,000. Its interval [$216,863, $371,683] overlaps the
current one ([$172,503, $327,324]), so the two point predictions hide substantial
overlap in the reported ranges.

```{figure} try_assets/try-reg-alternatives.png
:alt: CE alternative plot for the housing case with four numbered callouts. Fifteen alternative conditions on a dollar axis from about 0 to 500,000. A shaded band from about 173,000 to 327,000 dollars with a line at about 238,000 marks the current prediction. Each alternative has a median marker and a 90 percent interval; all intervals overlap the shaded band.
:name: try-reg-alternatives-figure

Housing case, alternative plot. Inspect how far each alternative's interval overlaps the
current one.
{download}`Full-size housing alternative plot <try_assets/try-reg-alternatives.png>`.
```

1. **Current prediction.** The shaded band is the current 90 % interval; the vertical
   line inside it is the current median prediction.
2. **Axis.** House value in US dollars; the axis title names the interval level (90 %).
3. **One alternative.** *median_income > 3.93*: the marker is the median prediction
   under that condition and the bar is its 90 % interval.
4. **Instance values.** The district's actual value for each feature.

(try-step-6)=
## Step 12. Explore probabilistic regression: a threshold question

A buyer with a budget asks a different question about the same district. A
**threshold** is a cutoff value on the target, here $300,000. The **event** is "the
value is at most the threshold", and the question is: *how probable is that event?*
This is the probabilistic (thresholded) regression mode, asked of the same model.

```python
t = 300_000
p, (low, high) = reg.predict_proba(r_case, uq_interval=True, threshold=t)
print(f"P(value <= ${t:,}) = {p[0, 1]:.3f}  "
      f"range [{low[0]:.3f}, {high[0]:.3f}]")

t_factual = reg.explain_factual(r_case, threshold=t)
rules = t_factual[0].get_rules()
order = sorted(range(len(rules["weight"])),
               key=lambda i: -abs(rules["weight"][i]))
for i in order[:4]:
    print(f"{rules['rule'][i]:28s} {rules['weight'][i]:+.3f} "
          f"[{rules['weight_low'][i]:+.3f}, "
          f"{rules['weight_high'][i]:+.3f}]")
t_factual.plot(uncertainty=True)

t_alts = reg.explore_alternatives(r_case, threshold=t)
alt = t_alts[0].get_rules()
for i, rule in enumerate(alt["rule"]):
    if rule.startswith("median_income"):
        print(f"{rule:22s} P(value <= ${t:,}) {alt['predict'][i]:.3f} "
              f"[{alt['predict_low'][i]:.3f}, "
              f"{alt['predict_high'][i]:.3f}]")
```

```text
P(value <= $300,000) = 0.905  range [0.904, 0.917]
longitude > -121.78          +0.544 [+0.529, +0.569]
median_income <= 5.00        +0.470 [+0.450, +0.480]
total_bedrooms <= 704.50     +0.179 [+0.119, +0.201]
housing_median_age <= 50.50  +0.121 [+0.114, +0.123]
median_income < 3.16   P(value <= $300,000) 0.945 [0.945, 0.948]
median_income > 3.93   P(value <= $300,000) 0.654 [0.644, 0.678]
```

**Reading it.**

- **Event direction.** CE reports the probability that the value is **at most** the
  threshold, P(value ≤ $300,000). The probability of exceeding it is one minus that.
- **Estimate and bounds.** The estimated probability is 0.905, with lower and upper
  values [0.904, 0.917]. This is a range for the *probability of an event*, not a range
  for the house value.
- **Why ask it.** The interval from Step 11 ($172,503 to $327,324) contains $300,000, so
  on its own it cannot say on which side of the budget the value falls; the threshold
  question answers that directly.
- **Weights.** They are now in probability points towards the event. The conditions that
  **lowered** the predicted value in Step 11 (`longitude > -121.78`,
  `median_income <= 5.00`) here **raise** the probability of staying under the budget.
  Both readings describe the same model.
- **Alternative.** If `median_income` were above 3.93, the probability would drop to
  0.654 (range [0.644, 0.678]).

```{figure} try_assets/try-thr-factual.png
:alt: CE factual plot for the housing case with the threshold 300,000 dollars, with five numbered callouts. Top panel, probability bars: P of value at most 300,000 is about 0.905, P of value above 300,000 about 0.095. Lower panel, feature weights in probability points; longitude greater than minus 121.78 and median income at most 5.00 raise the probability by about 0.54 and 0.47; ocean proximity greater than 0.5 and latitude at most 37.92 lower it.
:name: try-thr-factual-figure

Housing case, threshold question *value ≤ $300,000*, factual plot. Inspect the top bar
first (the event probability and its range), then which weight bars point towards the
event.
{download}`Full-size threshold factual plot <try_assets/try-thr-factual.png>`.
```

1. **Prediction.** The red bar is P(value ≤ $300,000) with its range; the blue bar below
   is P(value > $300,000).
2. **Axis.** Probability, from 0 to 1. The weights below use their own axis, in
   probability points.
3. **Weight raising the probability.** `longitude > -121.78`: red, to the right.
4. **Weight lowering the probability.** `ocean_proximity > 0.50`: blue, to the left.
5. **Instance values.** The district's own value for each feature, the same as in
   Step 11.

Unlike the regression plots in Step 11, this plot uses the probability colours of the
classification plots. How the threshold mode is calibrated is explained in
{doc}`Probabilistic and interval regression <../foundations/concepts/probabilistic_regression>`.

## Step 13. Interpret the results and continue

You have now seen four different ranges. They describe different quantities and must be
read separately:

| Range | Describes | Units | In this tutorial |
|---|---|---|---|
| **Class-probability bounds** | The calibrated probability of a class | Probability, 0 to 1 | P(diabetes) 0.510, [0.467, 0.556] (Step 8) |
| **Prediction interval** | Where the target value is likely to lie | The target's units | $237,814, [$172,503, $327,324] (Step 11) |
| **Bounds on a threshold-event probability** | The probability that the target is at most *t* | Probability, 0 to 1 | P(value ≤ $300,000) 0.905, [0.904, 0.917] (Step 12) |
| **Feature-weight range** | How much one condition moves the prediction, and the range CE reports for that weight | Probability points or the target's units | `median_income <= 5.00`: −$86,776, [−$176,285, −$21,465] (Step 11) |

**What the ranges rest on.** Their statistical meaning assumes **exchangeability**: in
plain language, the calibration cases and the new case behave like draws from the same
process, and the model is fixed before calibration. When new cases come from a different
population (for example another region or a later year), the ranges may no longer mean
what they say, and CE gives no guarantee under such drift.

**What each mode guarantees** differs and is stated once, with its assumptions and
non-guarantees, in
{doc}`Guarantees and limits by mode <../foundations/concepts/calibrated_interval_semantics>`.
The probability bounds and event bounds describe a *probability*, not the target value;
they are not a confidence interval for one case. The prediction interval concerns the
target value and is read over many cases, not as a promise for one. Feature-weight ranges
describe how the model responds to conditions; they are not causal effects. If you expect
the ranges to behave differently for defined groups, see
{doc}`Mondrian (conditional) calibration <../foundations/how-to/conditional_calibration>`.

**Continue:**

- {doc}`Read your first explanation <../foundations/how-to/interpret_explanations>`:
  every field of the records and plots.
- {doc}`Apply CE to your own data <apply-to-your-data>`, then
  {doc}`evaluate it on held-out data <../practitioner/evaluate_ce>`.
- The {doc}`classification <quickstart_classification>` and
  {doc}`regression <quickstart_regression>` tutorials, and the
  {doc}`Practitioner Hub <../practitioner/index>`.
- {doc}`Tasks, modes and capabilities <ce-tasks-and-modes>` and
  {doc}`Understand CE <../sections/understand-ce>`.

Back to the {doc}`Quick Start <try-in-browser>`.
