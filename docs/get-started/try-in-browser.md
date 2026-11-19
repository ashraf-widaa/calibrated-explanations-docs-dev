# Quick Start: try CE in your browser

<span id="try-ce-in-your-browser"></span>

No installation needed. This page shows what CE does with two small examples
you can open in the browser, then hands you over to Python when you want to
run CE yourself. It takes about 20 minutes.

## CE in four steps: train → calibrate → explain → interpret

```{raw} html
<ol class="ce-flow" aria-label="The CE workflow in four steps">
<li><strong>Train</strong><span>Fit a model on the training data.</span></li>
<li><strong>Calibrate</strong><span>Show CE labelled cases the model has never seen.</span></li>
<li><strong>Explain</strong><span>Ask why the model predicts what it does for one case.</span></li>
<li><strong>Interpret</strong><span>Read the prediction, its range and the conditions behind it.</span></li>
</ol>
```

CE uses three kinds of data, and each has one job:

| Data | Job | Glossary |
|---|---|---|
| **Training data** | Teaches the model how to make predictions. | {term}`Proper training set` |
| **Calibration data** | Separate labelled cases. CE compares the model's outputs with the observed outcomes to calibrate class probabilities or estimate prediction intervals, depending on the task. | {term}`Calibration set` |
| **The case being explained** | One new case, for example a patient or a district. CE predicts it and explains that prediction. | {term}`Local explanation` |

CE gives two kinds of explanation for one case:

- A **factual explanation** lists the conditions that are true for the case,
  such as *Glucose ≤ 132.5*, each with a {term}`feature weight <Feature weight>`
  and a range for that weight. See {term}`Factual explanation`.
- An **alternative explanation** asks *what if*: if one feature were in
  another range, what would CE predict, and with what range? See
  {term}`Alternative explanation`.

Each topic has one main page in the documentation. Use these when you want
more than this page gives:

| Question | Main page | Section |
|---|---|---|
| What is CE, and which task am I doing? | {doc}`../what-is-ce`, {doc}`ce-tasks-and-modes` | {doc}`CE: What & Why <../sections/what-and-why>` |
| What does the output mean for my task? | {doc}`../foundations/concepts/ce_workflow`, {doc}`../foundations/concepts/calibrated_interval_semantics` | {doc}`How CE Works <../sections/how-ce-works>` |
| How do I generate, plot and export explanations? | {doc}`../practitioner/index` | {doc}`CE in Practice <../sections/in-practice>` |
| How do I install CE and use it with my model? | {doc}`installation` | {doc}`CE Software & Integration <../sections/software-integration>` |

## Expert Hub: one classification and one regression example, side by side

The Expert Lab is called **Expert Hub** in the
[online CE demo](https://calibrated-explanations-demo.ju.se/expert). Use these
two built-in examples to compare the tasks:

- **Classification:** *Diabetes (Binary Classification)*, the Pima Indians
  Diabetes data. Does a patient have diabetes?
- **Regression:** *California Housing (Regression)*. What is the median house
  value in a district, in US dollars?

```{admonition} How to open both examples in the Expert Hub
:class: tip

The Expert Hub opens one project at a time. Follow these steps for Diabetes,
then go back to **Project** and repeat them for California Housing. Compare
the outputs step by step using the walkthrough on this page.

1. Open the [Expert Hub](https://calibrated-explanations-demo.ju.se/expert).
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

The factual plot for the diabetes case, annotated.
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

The factual plot for the housing case, annotated.
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

The alternative plot for the diabetes case, annotated.
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

The alternative plot for the housing case, annotated.
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

(try-decision-lab)=
## Decision Lab: decide, then reconsider

The [Decision Lab](https://games.grejna.ai/) is a set of teaching games from
Grejna in which you make the decisions and a CE-based assistant advises you.
They are teaching games: their predictions and explanations are not
real-world guarantees.

The labels below are those of the games' public versions on 18 November
2026 (Port Authority 1.2.0, Mission Control 2.1.2). Games change; if a label
differs, look for the same idea.

### Scenario: Port Authority

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

### Scenario: Mission Control

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

## Run CE locally

You have now seen the whole workflow without installing anything. To run it
yourself:

1. {doc}`Install CE <installation>`: `pip install "calibrated-explanations[viz]"`.
2. Run the {doc}`Quickstart <quickstart>`: one classification example,
   step by step, in about 10 minutes.
3. Continue with {doc}`how to read CE explanations <../foundations/how-to/interpret_explanations>`
   and {doc}`apply CE to your own data <apply-to-your-data>`.

The code on this page also runs as it is: copy the blocks in order into one
Python session.
