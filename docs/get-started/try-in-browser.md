# Quick Start: learn the CE workflow and read your first explanation

<span id="quick-start-try-ce-in-your-browser"></span>

<span id="try-ce-in-your-browser"></span>

```{raw} html
<nav class="ce-journey" aria-label="Get started, step 2 of 5"><ol><li><a href="../what-is-ce.html"><span class="ce-journey-n">1</span>What CE is</a></li><li aria-current="step"><a href="try-in-browser.html"><span class="ce-journey-n">2</span>Quick Start</a></li><li><a href="installation.html"><span class="ce-journey-n">3</span>Install</a></li><li><a href="../foundations/how-to/interpret_explanations.html"><span class="ce-journey-n">4</span>Read it</a></li><li><a href="apply-to-your-data.html"><span class="ce-journey-n">5</span>Your data</a></li></ol></nav>
```

**Get started, step 2 of 5 · about 30 minutes · no installation.** This
tutorial takes you from a general prediction problem to your first
calibrated explanation. The core path needs **no installation**: you read two
worked cases on this page and can open the same examples in the browser.
Each section ends with links for more depth; you can skip them on a first
reading.

By the end you will be able to:

- say what a model predicts in a classification task and in a regression task;
- name the CE mode that answers your question;
- read a calibrated prediction and its uncertainty;
- read one factual explanation and one alternative explanation, and say what
  they do and do not tell you.

:::{admonition} Three ways to continue after this page
:class: tip

**{ref}`Follow a guided scenario <try-decision-lab>`** in the Decision Lab ·
**{ref}`Experiment with CE outputs <qs-expert-lab>`** in the Expert Lab ·
**{ref}`Run the examples in Python <qs-python>`** with the Practitioner Hub.
:::

(qs-predictive-task)=
## 1. Define a predictive task

A **dataset** is a table of **observations** (rows), such as patients or
housing districts. Each observation is described by **input features**
(columns), such as a patient's glucose level or a district's median income.
The quantity we want to predict is the **target**.

In **supervised learning** a model is *fitted* (trained) on observations
whose target is known, so that it learns how the features relate to the
target. The fitted model then makes a **prediction** for a new observation
whose target is not yet known.

The form of the target decides the task:

| Task | The target is… | Example on this page |
|---|---|---|
| **Classification** | a **category** (a class label) | Does a patient have diabetes? *yes* or *no* |
| **Regression** | a **numerical quantity** | What is a district's median house value, in US dollars? |

This page follows **one observation of each kind** from start to finish:

- **The diabetes case** is one patient from the Pima Indians Diabetes data
  (8 features, such as `Glucose`, `BMI` and `Age`; the target `Y` is 1 for
  diabetes and 0 for no diabetes).
- **The housing case** is one district from the California Housing data
  (9 features, such as `median_income` and `ocean_proximity`; the target is the
  district's median house value in US dollars).

:::{admonition} Optional background
:class: note

- [Supervised learning, Google for Developers](https://developers.google.com/machine-learning/intro-to-ml/supervised):
  a short introduction to features, labels (targets), training a model and
  using it to predict.
- {doc}`Machine-learning essentials <ml-foundations>`: the same ideas in the
  vocabulary of these pages, with a CE example.
:::

(qs-task-mode-capability)=
## 2. Task, mode and capability

Three words recur throughout the CE documentation. They answer different
questions:

- The **task** says *what the model predicts*: a class or a number.
- The **CE mode** says *which question you ask about that prediction* and
  therefore the form of the calibrated output CE returns.
- A **capability** is *what you can do with CE* in that mode, such as
  predicting with uncertainty or explaining a prediction.

A regression model supports two modes, because you can ask two different
questions about the same number:

| CE mode | Task | Question it answers | Calibrated output |
|---|---|---|---|
| **Classification** | Classification | How probable is each class? | A probability with lower and upper bounds |
| **Interval regression** | Regression | Which value, and within what range? | A prediction with a prediction interval, in the target's units |
| **Probabilistic (thresholded) regression** | Regression | How probable is it that the value is at most a threshold *t*? | A probability for that event, with lower and upper bounds |

In every mode CE offers two kinds of explanation for one prediction. They are
introduced by the questions they answer:

- A **factual explanation** answers *"Why this prediction?"* It lists
  conditions that are true for the observation, such as *Glucose ≤ 132.5*,
  each with a {term}`feature weight <Feature weight>` and a range for that
  weight. See {term}`Factual explanation`.
- An **alternative explanation** answers *"What would the model predict if
  one condition were different?"* For example: if BMI were below 24.9, what
  would CE predict, and with what range? See {term}`Alternative explanation`.

More detail: {doc}`Tasks, modes and capabilities <ce-tasks-and-modes>` and
the {doc}`capabilities manifest <../tasks/capabilities>`.

<span id="ce-in-four-steps-train-calibrate-explain-interpret"></span>

(qs-workflow)=
## 3. The CE workflow: fit → calibrate → predict → explain → interpret

```{raw} html
<figure class="ce-figure" id="qs-workflow-figure">
  <a href="../_static/figures/ce-adds-to-workflow.svg" title="Open the figure at full size">
    <picture>
      <source media="(max-width: 600px)" srcset="../_static/figures/ce-adds-to-workflow-narrow.svg">
      <img src="../_static/figures/ce-adds-to-workflow.svg" width="900" height="450" alt="Two aligned lanes share one fitted model. Lane 1, supervised prediction, in blue: the training set is used to fit a model, and the model predicts for a new case; this example baseline returns one value without uncertainty. Lane 2, workflow with CE, in orange: CE takes the same fitted model and a separate labelled calibration set, held out from training, calibrates, and predicts the same new case. It returns a calibrated prediction with its uncertainty, shown as probability bounds on a 0 to 1 scale for classification or as a prediction interval in the target's units for regression, and then factual and alternative explanations.">
    </picture>
  </a>
  <figcaption><strong>What CE adds to a supervised prediction workflow.</strong> Lane 1 (blue) is a supervised prediction workflow; its single-value output is an example baseline. Lane 2 (orange) adds CE. Inspect three things: the calibration set is labelled data that is never used to fit the model; CE uses the <em>same</em> fitted model; and the uncertainty takes two different forms, bounds on a probability (0 to 1) or an interval in the target's units.</figcaption>
</figure>
```

**Reading the figure.** Lane 1 is what most machine-learning workflows do:
fit a model on the training set, then predict a new case. Lane 2 keeps that
model as it is. CE adds a second, separate set of labelled data, the
calibration set, and uses it to calibrate the model's outputs. It then
predicts the same new case with its uncertainty and explains that
prediction.

```{raw} html
<ol class="ce-flow" aria-label="The CE workflow in five steps">
<li><strong>Fit</strong><span>Train a model on the training data.</span></li>
<li><strong>Calibrate</strong><span>Show CE labelled cases the model has never seen.</span></li>
<li><strong>Predict</strong><span>Predict a new case, with its uncertainty.</span></li>
<li><strong>Explain</strong><span>Ask why, and what if, for that case.</span></li>
<li><strong>Interpret</strong><span>Read each number with the range and assumptions that belong to it.</span></li>
</ol>
```

CE uses three kinds of data, and each has one job:

| Data | Job | Glossary |
|---|---|---|
| **Training data** | Teaches the model how to make predictions. | {term}`Proper training set` |
| **Calibration data** | Separate labelled cases. CE compares the model's outputs with the observed outcomes to calibrate class probabilities or estimate prediction intervals, depending on the task. | {term}`Calibration set` |
| **The new case** | One observation to predict and explain, for example a patient or a district. | {term}`Local explanation` |

At each step:

| Step | What to do | Why it matters | What to inspect |
|---|---|---|---|
| **Fit** | Train any scikit-learn-style model on the training data. | CE does not change how the model learns. | The model is fitted. |
| **Calibrate** | Pass the held-out, labelled calibration data to CE. | Calibration is what turns raw model outputs into calibrated probabilities or intervals. | The explainer reports that it is calibrated. |
| **Predict** | Ask for a prediction with its uncertainty. | A point prediction alone hides how far it can be trusted. | The prediction and its lower and upper values. |
| **Explain** | Ask for a factual explanation, then alternatives. | Shows which conditions the prediction rests on and how it would respond to other conditions. | The weight of each condition and its range; the prediction under each alternative. |
| **Interpret** | Read every number with its units, range and mode. | Different ranges describe different quantities and rest on stated assumptions. | Whether a range crosses a decision point, such as 0.5 or a price. |

**Why CE reserves labelled data for calibration.** A model is usually more
confident on the data it was fitted on than on new data. To learn how
reliable the model's outputs are, CE needs labelled cases the model has never
seen: it compares the model's outputs on those cases with their known
outcomes. That is the calibration set's only job. It is not used to fit the
model, and because CE uses it, it cannot double as a test set; keep a
separate test set if you also want to evaluate.

:::{admonition} Optional background
:class: note

- [Dividing a dataset, Google for Developers](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets):
  why training and evaluation use separate data. CE's calibration set is a
  further, separate split with the role described above.
- [Probability calibration, scikit-learn](https://scikit-learn.org/stable/modules/calibration.html):
  what it means in general for a classifier's probabilities to be calibrated.
  CE's own methods are explained in
  {doc}`Calibration by task <../foundations/concepts/calibration_methods>`.
:::

<span id="expert-hub-one-classification-and-one-regression-example-side-by-side"></span>

(qs-worked-cases)=
## 4. Two worked cases, step by step

You can read both cases on this page. To see them run live, open the same
built-in examples in the **Expert Lab**, the
[online CE demo](https://calibrated-explanations-demo.ju.se/expert); its menu
calls it *Expert Hub*.

```{admonition} Optional: open both cases in the Expert Lab
:class: tip

The Expert Lab opens one project at a time. Follow these steps for Diabetes,
then go back to **Project** and repeat them for California Housing. Compare
the outputs step by step using the walkthrough on this page.

1. Open the [Expert Lab](https://calibrated-explanations-demo.ju.se/expert).
   The left menu shows **Project**, **Prepare & Calibrate**, **Explain** and
   **Predict**.
2. On **Project**, under **Quick Start — Demo Datasets**, choose
   **Diabetes (Binary Classification)** or **California Housing (Regression)**.
   Keep the default split (20% test, 33% calibration and 47% training), then
   select **Next: Prepare & Calibrate**.
3. Select **Prepare Random Forest + Calibrate**. When the project says
   **Calibrated**, select **Next: Explain**.
4. On **Explain**, select a row under **Test Set Instances**. For housing,
   leave **Use Threshold (probabilistic regression)** off to see a prediction
   interval for house value. Use **Factual** for the original prediction and
   feature weights, then **Alternatives** to compare conditions for that same row.
5. On **Predict**, select **Run Predictions**. Compare **P(positive)** and
   **Probability Interval** for Diabetes with **Prediction** and
   **Conformal Interval** for Housing.
```

The code and annotated plots below come from a reproducible run of the CE
Python library. The live lab selects its own test cases. It also uses
scikit-learn's California Housing features (such as `MedInc` and `AveRooms`)
and reports its target in units of $100,000. The Python example uses the CE
repository's Housing CSV and reports predictions in US dollars. Compare how
each output is read across the two tasks. Values depend on the dataset, split
and selected case.

Each step puts classification on the left and regression on the right. On
a narrow screen, the two examples stack within each step.

(try-step-1)=
### Step 1. Task and data

Load the data and split it three ways, with the lab's default proportions.

::::{grid} 1 1 2 2
:gutter: 3
:class-container: ce-parallel

:::{grid-item}
:class: ce-par ce-par-cls

**Classification · Diabetes**

```python
import pandas as pd
from sklearn.model_selection import train_test_split

DATA = ("https://raw.githubusercontent.com/Moffran/"
        "calibrated_explanations/main/tests/data/")
diab = pd.read_csv(DATA + "diabetes_full.csv")
Xc, yc = diab.drop(columns="Y"), diab["Y"]

Xc_rest, Xc_test, yc_rest, yc_test = train_test_split(
    Xc, yc, test_size=0.20, stratify=yc, random_state=42)
Xc_train, Xc_cal, yc_train, yc_cal = train_test_split(
    Xc_rest, yc_rest, test_size=0.33 / 0.80,
    stratify=yc_rest, random_state=42)
print(list(Xc.columns))
print("train", len(Xc_train), "cal", len(Xc_cal),
      "test", len(Xc_test))
```

```text
['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
train 360 cal 254 test 154
```

`Y` is 1 for diabetes and 0 for no diabetes. In this dataset a value of 0
for, say, blood pressure means *not measured*.
:::

:::{grid-item}
:class: ce-par ce-par-reg

**Regression · California Housing**

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

The target is the median house value in US dollars. `ocean_proximity` is a
code: 0 means inland; 1–4 mean near the bay, within an hour of the ocean,
near the ocean, or on an island.
:::
::::

**Reading it.** The model learns only from the training rows. The calibration
rows are labelled but unseen by the model; CE uses them in the next step.
The test rows play the role of new cases.

(try-step-2)=
### Step 2. Model and calibration

Wrap a random forest (the lab's default model), train it, then calibrate.

::::{grid} 1 1 2 2
:gutter: 3
:class-container: ce-parallel

:::{grid-item}
:class: ce-par ce-par-cls

**Classification · Diabetes**

```python
from sklearn.ensemble import RandomForestClassifier
from calibrated_explanations import WrapCalibratedExplainer

clf = WrapCalibratedExplainer(
    RandomForestClassifier(n_estimators=100, random_state=42))
clf.fit(Xc_train.to_numpy(), yc_train.to_numpy())
clf.calibrate(
    Xc_cal.to_numpy(), yc_cal.to_numpy(),
    feature_names=list(Xc.columns),
    class_labels={0: "no diabetes", 1: "diabetes"})
print("fitted:", clf.fitted, " calibrated:", clf.calibrated)
```

```text
fitted: True  calibrated: True
```

For classification, CE calibrates with a {term}`Venn–Abers predictor`.
:::

:::{grid-item}
:class: ce-par ce-par-reg

**Regression · California Housing**

```python
from sklearn.ensemble import RandomForestRegressor

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

For regression, CE calibrates with a {term}`conformal predictive system <Conformal predictive system>`.
:::
::::

**Reading it.** The status confirms both steps ran. Calibration uses the
held-out rows to compute the task-specific prediction information. How each method
works is explained in
{doc}`Statistical methods behind CE <../foundations/concepts/calibration_methods>`.

(try-step-3)=
### Step 3. Prediction and uncertainty

Predict one test case and ask for its range.

::::{grid} 1 1 2 2
:gutter: 3
:class-container: ce-parallel

:::{grid-item}
:class: ce-par ce-par-cls

**Classification · Diabetes**

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

**Reading it.** A decision rule using 0.5 would label the point prediction
*diabetes*. The probability bounds [0.467, 0.556] straddle that threshold,
which shows why the point prediction alone gives an incomplete picture.
:::

:::{grid-item}
:class: ce-par ce-par-reg

**Regression · California Housing**

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

**Reading it.** The 90% prediction interval uses the default 5th and 95th
percentiles. It spans about $155,000. That width matters if a decision
depends on whether the district's median house value exceeds a given price.
:::
::::

:::{admonition} What you are looking at
:class: note

These are the first uncertainty outputs on this page. For the patient, CE
returns a **calibrated probability** of diabetes with **lower and upper
bounds**: all three are probabilities between 0 and 1. For the district, CE
returns a **predicted value** with a **prediction interval** in US dollars.
Both come from the calibration set, so they carry their documented meaning
only when the patient or district resembles the calibration cases in the
sense of *exchangeability*, explained in
{ref}`Read the uncertainty beside each output <qs-uncertainty>`.
:::

What each range guarantees, and under which assumptions, is stated once in
{doc}`Guarantees by mode <../foundations/concepts/calibrated_interval_semantics>`.
Classification gives bounds for a class probability. Interval regression
gives a range in the target's units. Interpret both under the assumptions for
their mode, including how closely the new cases match the calibration data.

(try-step-4)=
### Step 4. Factual explanation

Ask why CE predicts what it does for this case.

::::{grid} 1 1 2 2
:gutter: 3
:class-container: ce-parallel

:::{grid-item}
:class: ce-par ce-par-cls

**Classification · Diabetes**

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
:::

:::{grid-item}
:class: ce-par ce-par-reg

**Regression · California Housing**

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
:::
::::

Each line is a **condition that is true for this case**, its weight, and the
range of that weight. A weight is how much the condition moves the
prediction: in probability points for classification, in dollars for
regression. Weights are not causal and do not add up to the prediction.

::::{grid} 1 1 2 2
:gutter: 3
:class-container: ce-parallel

:::{grid-item}
:class: ce-par ce-par-cls

```{figure} try_assets/try-cls-factual.png
:alt: CE factual plot for the diabetes case with six numbered callouts. Top panel, probability bars for diabetes, about 0.51 with a light range from 0.47 to 0.56, and for not diabetes. Lower panel, feature weights from about minus 0.16 to plus 0.3; Age greater than 28.5 and Insulin greater than 113 push towards diabetes, Glucose at most 132.5 pushes away; a grey band surrounds zero.
:name: try-cls-factual-figure

Diabetes case, factual plot. Inspect whether the probability range crosses
0.5, then which weight ranges stay on one side of zero.
{download}`Full-size diabetes factual plot <try_assets/try-cls-factual.png>`.
```

1. **Prediction.** The red bar is P(diabetes); the vertical marker is the
   calibrated probability (0.510) and the light part is its range
   (0.467 to 0.556). The blue bar below is P(not diabetes).
2. **Axis.** Probability, from 0 to 1. The weights below use their own
   axis, *Feature weights*, in probability points.
3. **Weight bar.** One condition that holds for this patient. Red, to the
   right, raises P(diabetes); blue, to the left, lowers it.
4. **Weight range.** The dark part runs from 0 to the end of the range
   nearest 0; the light part is the rest of the range. A range that crosses
   0 has no dark part: its direction is uncertain.
5. **Instance values.** The patient's own value for each feature.
6. **Grey band.** The prediction's own range, redrawn on the weight scale.
   It is not a confidence region for the weights.
:::

:::{grid-item}
:class: ce-par ce-par-reg

```{figure} try_assets/try-reg-factual.png
:alt: CE factual plot for the housing case with five numbered callouts. Top panel, the median prediction about 238,000 dollars with a 90 percent interval from about 173,000 to 327,000 dollars. Lower panel, feature weights in dollars; only median income and longitude have ranges entirely below zero, the other ranges cross zero.
:name: try-reg-factual-figure

Housing case, factual plot. Inspect the width of the interval, then which
weight ranges stay on one side of zero.
{download}`Full-size housing factual plot <try_assets/try-reg-factual.png>`.
```

1. **Prediction.** The marker is the median prediction ($237,814); the band
   is the 90 % interval ($172,503 to $327,324).
2. **Axis.** The top axis is the house value in US dollars. The weights
   below use their own axis, *Feature weights*, also in dollars.
3. **Weight bar.** One condition that holds for this district. In
   regression plots, blue to the right raises the prediction and red to the
   left lowers it (the opposite colours to classification).
4. **Weight range.** As in classification, only a range that stays on one
   side of 0 has a dark part. Here only `median_income ≤ 5.00` and
   `longitude > -121.78` do; for every other condition, even the direction
   is uncertain.
5. **Instance values.** The district's own value for each feature.
:::
::::

Every element of these plots is explained in
{doc}`How to read CE explanations <../foundations/how-to/interpret_explanations>`.

(try-step-5)=
### Step 5. One alternative

Ask what CE would predict if one feature were in another range.

::::{grid} 1 1 2 2
:gutter: 3
:class-container: ce-parallel

:::{grid-item}
:class: ce-par ce-par-cls

**Classification · Diabetes**

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

**Reading it.** This patient's BMI is 28.7. If it were below 24.9, CE would
predict 0.220, and the whole range [0.207, 0.224] is below 0.5: the
prediction would change to *no diabetes*. Above 29.8 it would rise to 0.577.
:::

:::{grid-item}
:class: ce-par ce-par-reg

**Regression · California Housing**

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

**Reading it.** `median_income` is in tens of thousands of dollars; this
district's value is 3.18. Above 3.93, the median prediction would rise to
about $282,000. Its interval [$216,863, $371,683] overlaps the current one
([$172,503, $327,324]), so the two point predictions hide substantial overlap
in the reported ranges.
:::
::::

::::{grid} 1 1 2 2
:gutter: 3
:class-container: ce-parallel

:::{grid-item}
:class: ce-par ce-par-cls

```{figure} try_assets/try-cls-alternatives.png
:alt: CE alternative plot for the diabetes case with four numbered callouts. Fourteen alternative conditions on a probability axis from 0 to 1. A shaded band from 0.47 to 0.56 marks the current prediction. Seven alternatives, including BMI below 24.9 at about 0.21 to 0.22, lie below 0.5; the others lie above.
:name: try-cls-alternatives-figure

Diabetes case, alternative plot. Inspect which alternatives lie wholly
below 0.5, where the predicted class would change.
{download}`Full-size diabetes alternative plot <try_assets/try-cls-alternatives.png>`.
```

1. **Current prediction.** The shaded band is the range of the current
   prediction (0.467 to 0.556), split at 0.5: the blue part is below 0.5,
   the red part above.
2. **Axis.** Probability of the class *diabetes*, from 0 to 1.
3. **One alternative.** *BMI < 24.90*: the bar is the range CE predicts if
   that condition held instead. Blue bars lie below 0.5 (the prediction
   would become *no diabetes*), red bars above.
4. **Instance values.** The patient's actual value for each feature.
:::

:::{grid-item}
:class: ce-par ce-par-reg

```{figure} try_assets/try-reg-alternatives.png
:alt: CE alternative plot for the housing case with four numbered callouts. Fifteen alternative conditions on a dollar axis from about 0 to 500,000. A shaded band from about 173,000 to 327,000 dollars with a line at about 238,000 marks the current prediction. Each alternative has a median marker and a 90 percent interval; all intervals overlap the shaded band.
:name: try-reg-alternatives-figure

Housing case, alternative plot. Inspect how far each alternative's
interval overlaps the current one.
{download}`Full-size housing alternative plot <try_assets/try-reg-alternatives.png>`.
```

1. **Current prediction.** The shaded band is the current 90 % interval;
   the vertical line inside it is the current median prediction.
2. **Axis.** House value in US dollars; the axis title names the interval
   level (90 %).
3. **One alternative.** *median_income > 3.93*: the marker is the median
   prediction under that condition and the bar is its 90 % interval.
4. **Instance values.** The district's actual value for each feature.
:::
::::

**Reading it.** An alternative describes how the model responds, not what
would happen if you changed the world: a lower BMI in the data is not a
treatment plan. Alternatives are explained in
{doc}`../foundations/concepts/alternatives`.

(try-step-6)=
### Step 6. The same district, a threshold question

The interval in Step 3 says *where* the house value is likely to lie. A buyer
with a budget asks a different question. A **threshold** is a cutoff value
on the target, here $300,000; the **event** is "the value is at most the
threshold". The question becomes: **how likely is the district's median house
value to be at most $300,000?** That is the probabilistic (thresholded)
regression mode, asked of the same model and the same district.

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

**Reading it.** The 90 % interval from Step 3 ($172,503 to $327,324)
contains $300,000, so on its own it cannot say on which side of the budget
the value falls. The threshold question answers that directly: CE estimates
a probability of 0.905 that the value is at most $300,000, with bounds
[0.904, 0.917]. This is a range for the *probability of an event*, not a range for
the house value.

The factual explanation now uses probability points towards the event
*value ≤ $300,000*. The conditions are the same ones that **lowered** the
predicted value in Step 4 (`longitude > -121.78`, `median_income <= 5.00`);
here they **raise** the probability of staying under the budget. Both
readings describe the same model. The alternative shows that if
`median_income` were above 3.93, the probability would drop to 0.654 (range [0.644, 0.678]).

```{figure} try_assets/try-thr-factual.png
:alt: CE factual plot for the housing case with the threshold 300,000 dollars, with five numbered callouts. Top panel, probability bars: P of value at most 300,000 is about 0.905, P of value above 300,000 about 0.095. Lower panel, feature weights in probability points; longitude greater than minus 121.78 and median income at most 5.00 raise the probability by about 0.54 and 0.47; ocean proximity greater than 0.5 and latitude at most 37.92 lower it.
:name: try-thr-factual-figure

Housing case, threshold question *value ≤ $300,000*, factual plot. Inspect
the top bar first (the event probability and its range), then which weight
bars point towards the event.
{download}`Full-size threshold factual plot <try_assets/try-thr-factual.png>`.
```

1. **Prediction.** The red bar is P(value ≤ $300,000) with its range; the
   blue bar below is P(value > $300,000).
2. **Axis.** Probability, from 0 to 1. The weights below use their own
   axis, in probability points.
3. **Weight raising the probability.** `longitude > -121.78`: red, to the
   right.
4. **Weight lowering the probability.** `ocean_proximity > 0.50`: blue, to
   the left.
5. **Instance values.** The district's own value for each feature, the same
   as in Step 4.

How the threshold mode is calibrated, and why its bounds are reported
separately from the interval in Step 3, is explained in
{doc}`Probabilistic and interval regression <../foundations/concepts/probabilistic_regression>`.

(qs-uncertainty)=
## 5. Read the uncertainty beside each output

This page has shown four different ranges. They look alike in a plot, but
they describe different quantities and must be read separately:

| Range | Describes | Units | In this tutorial |
|---|---|---|---|
| **Class-probability bounds** | The calibrated probability of a class | Probability, 0 to 1 | P(diabetes) 0.510, bounds [0.467, 0.556] (Step 3) |
| **Prediction interval** | Where the target value is likely to lie | The target's units | $237,814, interval [$172,503, $327,324] (Step 3) |
| **Bounds on a threshold-event probability** | The probability that the target is at most *t* | Probability, 0 to 1 | P(value ≤ $300,000) 0.905, bounds [0.904, 0.917] (Step 6) |
| **Feature-weight range** | How much one condition moves the prediction, and how sure CE is of that | Probability points or target units | `median_income <= 5.00`: −$86,776, range [−$176,285, −$21,465] (Step 4) |

**Where the ranges come from.** For classification, CE calibrates with a
{term}`Venn–Abers predictor`, which returns two calibrated probabilities; CE
reports a merged probability between them as the prediction. For regression,
CE uses a {term}`conformal predictive system <Conformal predictive system>`
(CPS), which turns the calibration errors into a distribution for the new
case's value; the interval is read from its percentiles (by default the 5th
and 95th, a 90 % interval). The threshold question combines the two: CPS
scores followed by Venn–Abers calibration of the event.

**What the ranges rest on.** The statistical meaning of these ranges assumes
**exchangeability**: in plain language, the calibration cases and the new
case behave like draws from the same process, so that no case is special and
their order does not matter. The model must also be fixed before calibration.
When the new case comes from a different population, for example another
region or a later year (*distribution shift*), the ranges may no longer mean
what they say, and CE gives no guarantee under such drift.

**What each mode guarantees.** The guarantees differ by mode and are stated
once, with their assumptions and non-guarantees, in
{doc}`Guarantees and limits by mode <../foundations/concepts/calibrated_interval_semantics>`.
Two points matter for reading this page:

- The class-probability bounds and threshold-event bounds bound a
  *probability*; they are not a confidence interval for one case. The
  prediction interval concerns the *target value* and holds on average over
  cases, not for every case. The exact guarantee wording for each mode is
  still under review by the CE authors.
- Feature-weight ranges describe how the model responds to conditions; they
  are explanation quantities, not causal effects.

**When groups differ.** If you expect the ranges to behave differently for
defined groups, such as regions or product lines, CE can calibrate each group
separately. See {doc}`Mondrian (conditional) calibration <../foundations/how-to/conditional_calibration>`;
this is optional and not needed for this tutorial.

**Alternatives are not interventions.** An alternative explanation reports
what *the model* would predict under a different feature condition. It does
not say what would happen if you changed the patient or the district: a lower
BMI in the data is not a treatment plan. See
{doc}`Factual and alternative explanations <../foundations/concepts/alternatives>`.

(qs-checkpoint)=
## 6. Checkpoint and next action

Answer these three questions for the diabetes case before moving on.

:::{dropdown} 1. What does CE predict for the patient?
The calibrated probability of diabetes is 0.510. A decision rule at 0.5
would label the patient *diabetes*.
:::

:::{dropdown} 2. What does the uncertainty of that prediction mean?
The bounds [0.467, 0.556] straddle 0.5, so the calibrated evidence does not
clearly favour either class. The bounds are calibrated values of a
probability, valid under exchangeability with the calibration data; they are
not a confidence interval for this one patient.
:::

:::{dropdown} 3. How does the prediction change under one alternative condition?
If BMI were below 24.9 (the patient's BMI is 28.7), CE would predict 0.220
with range [0.207, 0.224], wholly below 0.5: the model would predict *no
diabetes*. This describes the model's response, not the effect of changing the
patient's BMI.
:::

Then choose how to continue.

<span id="decision-lab-decide-then-reconsider"></span>

(try-decision-lab)=
### Follow a guided scenario: Decision Lab

The [Decision Lab](https://games.grejna.ai/) is a set of teaching games from
Grejna in which you make the decisions and a CE-based assistant advises you.
They are teaching games: their predictions and explanations are not
real-world guarantees.

The labels below are those of the games' public versions on 18 November
2026 (Port Authority 1.2.0, Mission Control 2.1.2). Games change; if a label
differs, look for the same idea.

#### Scenario: Port Authority

Open [Port Authority](https://games.grejna.ai/games/port-authority) and select
**Open the harbour**. Select **Next harbour event** until a ship appears in
**Anchorage**, then select the ship on the map to open its decision panel.

| | In the game |
|---|---|
| **Who decides** | You, as the harbour master. Each ship waits at the anchorage, **Awaiting clearance**. |
| **What the model predicts** | The **Chance routine clearance is appropriate, with its calibrated range**, shown in the panel **AI support · routine clearance**. The model is a random forest with separate calibration. |
| **What it sees** | Engine condition, manifest quality, weather severity, vessel class and whether the cargo is high-value. |
| **Your actions** | **CLEAR** sends the ship to the berth queue now. **HOLD** keeps it at anchorage for about 35 minutes: safe, but waiting costs money. **INSPECT** sends it to an inspection team first. If you do not decide in time, the ship is held. |

Try it with one ship:

1. **Decide first.** Look only at the chance of routine clearance. Write down
   CLEAR, HOLD or INSPECT.
2. **Inspect the uncertainty.** Look at the calibrated range. Is its lower end
   still high enough that you would clear? Does it cross the point where you
   would change your mind?
3. **Inspect the explanation.** If the panel offers
   **Investigate WHY & alternatives · 80 cr**, open that report. **Why this
   probability?** lists each observation's contribution with its uncertainty
   range; **Alternative observations** shows what the model would say if an
   observation were different. The game reminds you that the report explains
   the model, and that a different reported observation does not change the
   ship.
4. **Reconsider.** Keep or change your choice. Then name what you still do not
   know: an inspection, for example, tells you about the ship itself, which
   no explanation of the model can.

#### Scenario: Mission Control

*On 19 November 2026 this game opened from its direct link but was not
listed on the Decision Lab home page, which listed Uncertain Acres, Port
Authority and Precision Works. If the link stops working, start with Port
Authority above.*

Open [Mission Control](https://games.grejna.ai/games/mission-control) and
select **Start** on **WHY? What is it resting on?** (level 4). Under
**Upgrades for this level**, buy **Calibrated probability**, **Uncertainty
intervals** and **WHY? factual explanations**, in that order. The first
mission appears once all three are installed.

| | In the game |
|---|---|
| **Who decides** | You, as the operator who sends autonomous rovers on missions. |
| **What the model predicts** | **Chance of success** for the mission. **Could be anywhere in** shows its uncertainty range under **Assistant assessment**. |
| **Your actions** | Under **Your call**, choose **GO** to launch the rover or **STOP** to hold it on the pad. |

1. **Decide first.** Read the mission file and the **Chance of success**.
   Write down **GO** or **STOP** before selecting an action.
2. **Inspect the uncertainty.** Ask whether you would make the same call at
   both ends of **Could be anywhere in**, given the launch reward and failure
   cost shown in the mission file.
3. **Inspect the explanation.** Select **WHY?** to see which observations
   push the probability up or down and which contributions the game marks
   **either way**. Compare a contribution's own range with the overall
   chance-of-success range.
4. **Reconsider.** Keep or change your choice. Name one new piece of evidence
   that would help, such as an updated communications or weather check,
   then select **GO** or **STOP**.

(qs-expert-lab)=
### Experiment with CE outputs: Expert Lab

The **Expert Lab** is the [online CE demo](https://calibrated-explanations-demo.ju.se/expert);
its menu calls it **Expert Hub**. It runs CE in the browser, with no
installation. Open the two built-in examples from Section 4 and change one
thing at a time:

- choose another row under **Test Set Instances** and compare its prediction
  range with the one on this page;
- for housing, switch on **Use Threshold (probabilistic regression)** and
  compare the result with Step 6;
- change the split proportions on **Project** and see how the ranges respond.

The Expert Lab also offers the Iris data and your own data; it is under
active development, so labels may change.

<span id="run-ce-locally"></span>

(qs-python)=
### Run the examples in Python: Practitioner Hub

You have now seen the whole workflow without installing anything. To run it
yourself:

1. **Prerequisites.** Python 3.10 or later and a scikit-learn-style model.
2. {doc}`Install CE <installation>`: `pip install "calibrated-explanations[viz]"`;
   the `viz` extra adds the plots.
3. Copy the code blocks of this page, in order, into one Python session: they
   run as written and print the outputs shown.
4. Go to the {doc}`Practitioner Hub <../practitioner/index>` for the
   {doc}`Python quickstart <quickstart>` and the complete
   {doc}`classification <quickstart_classification>` and
   {doc}`regression <quickstart_regression>` tutorials, then
   {doc}`apply CE to your own data <apply-to-your-data>`.

## Go deeper

Each topic has one main page. Use these when you want more than this page
gives:

| Question | Main page | Section |
|---|---|---|
| What is CE, and which mode am I using? | {doc}`../what-is-ce`, {doc}`ce-tasks-and-modes` | {doc}`Get started <index>`, {doc}`Understand CE <../sections/how-ce-works>` |
| How do I read every element of a plot? | {doc}`../foundations/how-to/interpret_explanations` | {doc}`Get started <index>` |
| What do the ranges guarantee? | {doc}`../foundations/concepts/ce_workflow`, {doc}`../foundations/concepts/calibrated_interval_semantics` | {doc}`Understand CE <../sections/how-ce-works>` |
| How do I plot, export or narrate explanations? | {doc}`../foundations/how-to/index` | {doc}`CE in Practice <../sections/in-practice>` |
| How do I integrate CE into my software? | {doc}`../get-started/quick_api`, {doc}`../api/index` | {doc}`Software Integration & Architecture <../sections/software-integration>` |

**Next:** {doc}`Install CE <installation>`, step 3 of
{doc}`Get started <index>`.
