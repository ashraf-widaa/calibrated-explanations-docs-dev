# How CE Calibrates: Venn–Abers and Conformal Predictive Systems

:::{admonition} About this page
:class: note

This page is new and is being reviewed by the Calibrated Explanations authors. Statements
marked *wording under review* follow the cited sources, but their final wording has not
yet been confirmed and may change.
:::

Calibrated Explanations (CE) turns a model's raw outputs into calibrated probabilities
and prediction intervals. It does this with two methods from the conformal prediction
framework: **Venn–Abers predictors** for probabilities and **conformal predictive
systems (CPS)** for numeric targets. This page explains what the two methods compute,
what they guarantee, and where the guarantees stop.

**What you will learn**

- What it means for a probability to be calibrated, and why calibration is not accuracy.
- How Venn–Abers produces two probabilities, p0 and p1, and what CE reports.
- How a conformal predictive system turns calibration errors into prediction intervals,
  and why they cover the truth at the requested rate on average.

**Prerequisites:** {doc}`../../get-started/ml-foundations` (data roles) and
{doc}`../../get-started/ce-tasks-and-modes` (CE's three modes). The mathematical parts assume
conditional expectation and order statistics.

**How to read this page.** Each section starts with a plain-language summary, then
explains the mechanism and CE's output, then gives the construction and the formal
statement. You can stop after the first two parts. Four kinds of boxes separate the
statements:

| Box | Meaning |
|---|---|
| **Theoretical guarantee** | A result from the cited literature, with its assumption |
| **How CE does it** | What the implementation computes |
| **Illustrative example** | Numbers from one dataset or simulation; illustrates, proves nothing |
| **Under review** | Not yet confirmed by the CE authors; may change |

## Notation

| Symbol | Meaning |
|---|---|
| {math}`x`, {math}`y` | Features and true label (or target) of one case |
| {math}`X`, {math}`Y` | The same, as random variables |
| {math}`s(x)` | The model's raw score for class 1 |
| {math}`\hat y(x)` | The model's raw regression prediction |
| {math}`(x_i, y_i),\ i = 1,\dots,n` | Calibration cases, never used for training |
| {math}`p_0, p_1` | The two Venn–Abers probabilities for a test case |
| {math}`p` | CE's single (merged) probability |
| {math}`\alpha_i = y_i - \hat y(x_i)` | Calibration residuals; {math}`\alpha_{(k)}` is the {math}`k`-th smallest |
| {math}`l, h` | Requested lower and upper percentiles as fractions (5 % is 0.05) |

## 1. Calibration

**In one minute.** A forecaster is calibrated if, on the days they say "70 % chance of
rain", it rains about 70 % of the time. A calibrated classifier does the same with its
predicted probabilities. Many models produce scores that look like probabilities but are
over- or under-confident.

**How it works.** Calibration is checked, and corrected, on data the model has not seen:
the *calibration set*. Calibration changes what a probability means; it does not
necessarily make the model more accurate.

:::{admonition} Illustrative example
:class: note

In the {doc}`practical walkthrough <../../get-started/quickstart_walkthrough>`, calibration
changes test case 2 from a raw random-forest probability of 0.160 to a calibrated 0.286.
Over the whole test set, the Brier score is 0.0366 before calibration and 0.0445 after.
Calibration is about the meaning of the number, not about a better score.
:::

**Definition.** A predictor {math}`\hat p` is *perfectly calibrated* if

```{math}
P\big(Y = 1 \mid \hat p(X) = q\big) = q \quad \text{for every value } q \text{ that } \hat p \text{ outputs,}
```

equivalently {math}`E[Y \mid \hat p(X)] = \hat p(X)` (Dawid, 1982). Calibration alone is
weak: the constant prediction {math}`\hat p(x) = P(Y = 1)` is perfectly calibrated and
useless, because it does not distinguish cases. Useful predictions need calibration and
discrimination.

### Checking calibration: reliability diagrams

A *reliability diagram* checks calibration on held-out data (Guo et al., 2017, §2).

1. Sort the test cases into bins by their predicted probability, for example
   0–0.2, 0.2–0.4, …, 0.8–1.0.
2. For each bin, compute the **mean predicted probability** and the **observed share** of
   positive cases.
3. Plot observed share against mean prediction. A perfectly calibrated model lies on the
   diagonal.

**Reading it.**

- **Below the diagonal:** the model predicts higher probabilities than it achieves.
- **Above the diagonal:** it predicts lower ones.
- **Over-confidence:** a model that is too extreme sits above the diagonal at low
  probabilities and below it at high ones.

The weighted average distance from the diagonal is the *expected calibration error*:

```{math}
\mathrm{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{n}\,\big|\,\bar o(B_m) - \bar p(B_m)\,\big| ,
```

where {math}`B_m` is the set of cases in bin {math}`m`, {math}`\bar p(B_m)` their mean
prediction and {math}`\bar o(B_m)` their observed share of positives (Guo et al., 2017,
Eq. 3, which uses top-label accuracy and confidence; this is the binary form).

**Limits.**

- A bin with few cases gives a noisy point, so always report the bin counts. The diagram
  itself does not show them (Guo et al., 2017, §2).
- Different bin choices can give different pictures.
- A reliability diagram measures calibration only. It says nothing about how well the
  model separates the classes: the base-rate predictor above is a single point on the
  diagonal. Accuracy and discrimination need separate measures, such as accuracy, ROC AUC
  or the Brier score.

Section 2 shows a reliability table for the walkthrough data.

**Isotonic regression.** A standard way to calibrate scores is to fit a non-decreasing
function {math}`f` that minimises {math}`\sum_i \big(y_i - f(s_i)\big)^2` on the calibration
set. The *pool-adjacent-violators* algorithm computes it: scan the cases in score order;
whenever a fitted value is larger than the next one, merge them into one block whose value
is their mean; repeat until the values never decrease.

## 2. Venn–Abers predictors

**In one minute.** For each new case, CE asks the calibration data two "what if"
questions: what calibrated probability would this case get if it turned out negative
(p0), and if it turned out positive (p1)? CE reports both as the interval
`[low, high]`, together with one combined probability. The interval is narrow when many
calibration cases have similar scores, and wide when few do.

**How it works.**

1. The model gives the new case a score {math}`s`.
2. CE adds the case to the calibration scores twice: once labelled 0, once labelled 1.
3. Each time it fits isotonic regression and reads the fitted value at {math}`s`. This
   gives {math}`p_0` and {math}`p_1`, with {math}`p_0 \le p_1`.
4. CE reports {math}`[p_0, p_1]` and the merged probability
   {math}`p = p_1 / (1 - p_0 + p_1)`.

:::{admonition} How CE does it
:class: tip

`predict_proba(x, uq_interval=True)` returns `probs` and `(low, high)`. For binary
classification, `low` and `high` are {math}`p_0` and {math}`p_1` for the positive class,
with shape `(n_samples,)`, and `probs[:, 1]` is the merged {math}`p`. CE uses an inductive
Venn–Abers predictor from the `venn_abers` package (`calibration/venn_abers.py`).
:::

### Worked example

Ten calibration cases and a test score {math}`s = 0.50`:

| Score {math}`s_i` | 0.05 | 0.15 | 0.25 | 0.35 | 0.45 | 0.55 | 0.65 | 0.75 | 0.85 | 0.95 |
|---|---|---|---|---|---|---|---|---|---|---|
| Label {math}`y_i` | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 1 |

*Test case labelled 0.* In score order the labels are 0, 0, 1, 0, 0, **0**, 1, 1, 0, 1, 1.
Pool-adjacent-violators merges the 1 at 0.25 with the three 0s that follow (mean
{math}`1/4`), and the 1, 1, 0 at scores 0.55–0.75 (mean {math}`2/3`). The test score falls
in the first block, so {math}`p_0 = 0.25`.

*Test case labelled 1.* The labels are 0, 0, 1, 0, 0, **1**, 1, 1, 0, 1, 1. The 1, 0, 0 at
scores 0.25–0.45 merge to {math}`1/3`. The 0 at 0.75 then forces the 1, 1, 1 before it into
one block **1**, 1, 1, 0 with mean {math}`3/4`, so {math}`p_1 = 0.75`.

Merged: {math}`p = 0.75 / (1 - 0.25 + 0.75) = 0.50`. The merge is not the midpoint in
general: for a test score of 0.30, {math}`[p_0, p_1] = [0.25, 0.50]` and {math}`p = 0.40`,
not 0.375.

:::{admonition} Theoretical guarantee
:class: important

**Validity of Venn–Abers predictors** (Vovk and Petej, 2014; Vovk, Petej and Fedorova,
2015). If the calibration cases and the test case are exchangeable (for example,
independent draws from one distribution), the probability selected by the *true* label,
{math}`p_Y`, is perfectly calibrated:

```{math}
E\left[\,Y \mid p_Y\,\right] = p_Y .
```

*Wording under review.*
:::

What the guarantee does not say:

- It is a property of the **pair** over many cases. At prediction time {math}`Y` is
  unknown, so we do not know which of {math}`p_0` and {math}`p_1` is the calibrated one.
  {math}`[p_0, p_1]` is therefore not a confidence interval for "the true probability of
  this case". *Wording under review.*
- The merged {math}`p = p_1/(1 - p_0 + p_1)` minimises the worst-case log-loss regret
  (Vovk, Petej and Fedorova, 2015, §4). The same paper notes that merged probabilities
  lose the exact calibration guarantee. *Wording under review.*

**Why the interval is wide or narrow (interpretation).** {math}`p_0` and {math}`p_1` differ
only because the one added case pulls the isotonic fit. Where many calibration scores lie
near {math}`s`, one extra case changes the block mean little; where few do, it changes it a
lot. This is an intuition, not a theorem.

:::{admonition} How CE does it: multiclass
:class: tip

CE fits one Venn–Abers predictor per class (class against the rest). With the default
normalisation it divides every class's probability **and** its bounds by the sum of the
class probabilities, so the probabilities add up to 1 but an upper bound can exceed 1.
`normalization="simplex"` keeps the raw Venn–Abers bounds. See
{doc}`../../get-started/ce-tasks-and-modes`.
:::

:::{admonition} Under review
:class: warning

Whether the default multiclass normalisation is intended, and how its rescaled bounds
should be read, is being confirmed by the CE authors.
:::

### Example with CE

```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from calibrated_explanations import WrapCalibratedExplainer

data = load_breast_cancer()
x, y = data.data, data.target
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=42
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, stratify=y_train, random_state=42
)

classifier = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=100, random_state=42))
classifier.fit(x_proper, y_proper)
classifier.calibrate(x_cal, y_cal)

probs, (low, high) = classifier.predict_proba(x_test[2:3], uq_interval=True)
p0, p1 = low[0], high[0]
print(f"p0 = {p0:.4f}, p1 = {p1:.4f}, merged p = {probs[0, 1]:.4f}")
print(f"p1 / (1 - p0 + p1) = {p1 / (1 - p0 + p1):.4f}")
```

```text
p0 = 0.1667, p1 = 0.3333, merged p = 0.2857
p1 / (1 - p0 + p1) = 0.2857
```

**Reliability table.** The same classifier, before and after calibration, on all 114 test
cases (the reliability diagram of section 1, as a table):

```python
import numpy as np


def reliability_table(p, y_true, edges=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0)):
    bins = np.digitize(p, edges[1:-1])  # bin 0 is [0, 0.2), ..., the last bin includes 1.0
    for b in range(len(edges) - 1):
        in_bin = bins == b
        if in_bin.any():
            print(
                f"{edges[b]:.1f}-{edges[b + 1]:.1f}  n={in_bin.sum():3d}  "
                f"mean predicted {p[in_bin].mean():.3f}  observed {y_true[in_bin].mean():.3f}"
            )


print("raw forest")
reliability_table(classifier.predict_proba(x_test, calibrated=False)[:, 1], y_test)
print("calibrated")
reliability_table(classifier.predict_proba(x_test)[:, 1], y_test)
```

```text
raw forest
0.0-0.2  n= 38  mean predicted 0.028  observed 0.000
0.2-0.4  n=  3  mean predicted 0.320  observed 0.667
0.4-0.6  n=  2  mean predicted 0.480  observed 1.000
0.6-0.8  n= 11  mean predicted 0.712  observed 0.727
0.8-1.0  n= 60  mean predicted 0.970  observed 1.000
calibrated
0.0-0.2  n= 35  mean predicted 0.057  observed 0.000
0.2-0.4  n=  7  mean predicted 0.311  observed 0.429
0.4-0.6  n=  3  mean predicted 0.500  observed 1.000
0.6-0.8  n= 17  mean predicted 0.682  observed 0.824
0.8-1.0  n= 52  mean predicted 0.951  observed 1.000
```

:::{admonition} Illustrative example
:class: note

The middle bins hold only 2 to 7 cases, so their observed shares are too noisy to judge
calibration. With 114 test cases, this table cannot show whether calibration helped, and
on this data it does not visibly improve the picture (consistent with the Brier scores in
section 1). Checking calibration reliably needs a larger test set. The Venn–Abers
guarantee concerns the pair {math}`(p_0, p_1)` over many cases, not a reliability table
on one small test set.
:::

## 3. Conformal prediction and conformal predictive systems

**In one minute.** For a numeric target, CE gives a range that contains the true value in
about 90 % of cases, provided that future cases resemble the calibration cases. It builds
the range from how wrong the model was on the calibration cases.

**How it works.**

1. On the calibration set, CE records the model's errors (residuals)
   {math}`\alpha_i = y_i - \hat y(x_i)`.
2. For a new case it shifts the sorted residuals by the new prediction:
   {math}`\hat y(x) + \alpha_{(1)} \le \dots \le \hat y(x) + \alpha_{(n)}`. This sorted list
   is a *predictive distribution* for {math}`y`.
3. The requested percentiles of that list form the prediction interval, and its median is
   CE's point prediction.

:::{admonition} How CE does it
:class: tip

`predict(x, uq_interval=True, low_high_percentiles=(5, 95))` returns the median and
`(low, high)`. CE uses a split conformal predictive system from the `crepes` package
(`calibration/interval_regressor.py`). `predict(x)` returns the CPS median, which can
differ from the model's own prediction. A one-sided request (`-np.inf` or `np.inf`)
leaves one side open: v1.0.2 reports it as the smallest or largest calibration target
(a placeholder), and from v1.1.0 it is reported as `-inf` or `inf`; in neither case is
it a bound (see {doc}`../../tasks/regression`).
:::

### Exchangeability

Cases {math}`Z_1, \dots, Z_{n+1}` (here {math}`Z_i = (X_i, Y_i)`) are *exchangeable* if
their joint distribution does not change when they are reordered. Independent draws from
one distribution are exchangeable; data with a time trend, or from a population that
changed after calibration, are not. *Wording under review: some CE pages also say
"exchangeable or distribution-matched".*

### Conformal predictive systems

A *conformal predictive system* (Vovk et al., 2019) outputs a whole predictive
distribution {math}`Q(y)` instead of a single interval. The *split* version used by CE
has guaranteed validity and is computationally efficient (Vovk et al., 2020). The
unsmoothed value that `crepes` computes is

```{math}
Q(y) = \frac{\#\{\, i : \hat y(x) + \alpha_i \le y \,\} + 1}{n + 1},
```

and the interval endpoints are order statistics of the residuals:

```{math}
\text{low} = \hat y(x) + \alpha_{(a)},\quad a = \lfloor l\,(n+1) \rfloor;
\qquad
\text{high} = \hat y(x) + \alpha_{(b)},\quad b = \lceil h\,(n+1) \rceil .
```

### Worked example

Nineteen calibration residuals, sorted: −3.1, −2.4, −1.9, −1.5, −1.2, −0.9, −0.6, −0.4,
−0.2, 0.0, 0.1, 0.3, 0.5, 0.8, 1.0, 1.4, 1.7, 2.2, 3.0. A new case has
{math}`\hat y(x) = 10` and the request is (5, 95), so {math}`n + 1 = 20`.

| Step | Calculation | Result |
|---|---|---|
| Lower endpoint | {math}`a = \lfloor 0.05 \cdot 20 \rfloor = 1`, {math}`\alpha_{(1)} = -3.1` | 6.9 |
| Upper endpoint | {math}`b = \lceil 0.95 \cdot 20 \rceil = 19`, {math}`\alpha_{(19)} = 3.0` | 13.0 |
| Median | {math}`\lfloor 0.5 \cdot 20 \rfloor = \lceil 0.5 \cdot 20 \rceil = 10`, {math}`\alpha_{(10)} = 0.0` | 10.0 |
| {math}`Q(11)` | 15 residuals satisfy {math}`10 + \alpha_i \le 11` | {math}`(15 + 1)/20 = 0.80` |

### Why the interval covers

**Assumptions.**

1. The calibration cases and the new case are exchangeable.
2. The model {math}`\hat y` (and the difficulty estimate, if one is used) was fixed before
   the calibration cases were seen, for example trained only on the proper training set.
3. The endpoint indices satisfy {math}`1 \le a < b \le n`.

Let {math}`\alpha_{n+1} = Y - \hat y(X)` be the test residual. Under assumptions 1 and 2,
{math}`\alpha_1, \dots, \alpha_{n+1}` are exchangeable.

**Without ties** (for example a continuous target), the rank {math}`R` of
{math}`\alpha_{n+1}` among all {math}`n + 1` residuals is uniform on
{math}`\{1, \dots, n+1\}`. The test residual lies in {math}`[\alpha_{(a)}, \alpha_{(b)}]`
exactly when at least {math}`a` and at most {math}`b - 1` calibration residuals are below
it, that is when {math}`R \in \{a + 1, \dots, b\}`. Hence

```{math}
P\big(Y \in [\text{low}, \text{high}]\big) = \frac{b - a}{n + 1}
= \frac{\lceil h(n+1) \rceil - \lfloor l(n+1) \rfloor}{n + 1}
\;\ge\; h - l ,
```

and, because {math}`\lceil u \rceil < u + 1` and {math}`\lfloor u \rfloor > u - 1`, it is
less than {math}`h - l + 2/(n+1)`. In the worked example the value is
{math}`(19 - 1)/20 = 0.90`.

**With ties** (for example an integer target), break ties at random. The event above
still implies that the test residual lies in the closed interval, so the lower bound
{math}`(b - a)/(n + 1) \ge h - l` still holds. The equality and the upper bound need not.

**Endpoint conventions.** If {math}`\lfloor l(n+1) \rfloor < 1`, there are too few
calibration cases for the requested lower percentile. `crepes` then warns and reports the
endpoint as {math}`-\infty`, so that side is unbounded; the same applies to the upper
percentile if {math}`\lceil h(n+1) \rceil > n`. A finite 5 % endpoint therefore needs
{math}`\lfloor 0.05\,(n+1) \rfloor \ge 1`, that is {math}`n \ge 19`. With Mondrian
calibration this applies to the number of calibration cases in each category.

**Finite samples.** The probability above is taken over the random calibration set *and*
the new case. For one fixed calibration set, the share of future cases covered is itself
random. For conformal predictors, Vovk (2012, Propositions 2a and 2b) shows that it is
close to the nominal level with high probability, with deviations that shrink as
{math}`n` grows ("training-conditional validity"). The simulation below shows one such
calibration set.

:::{admonition} Theoretical guarantee
:class: important

If calibration and future cases are exchangeable, CE's {math}`(l, h)` prediction interval
contains the true value with probability at least {math}`h - l`, **on average over cases**
(marginal coverage; Vovk, Gammerman and Shafer, 2022; Lei et al., 2018). It is not a
statement about each individual case, or about each subgroup.

*Wording under review: the derivation above follows the `crepes` endpoint rule; whether
the documentation should say "at least" or "about" the requested rate is being confirmed.*
:::

**Subgroups and difficulty.**

- *Mondrian* calibration repeats the construction separately within each category
  (`bins=`), which gives the coverage statement within each category (Boström, Johansson
  and Löfström, 2021). See {doc}`../how-to/conditional_calibration`.
  *Wording under review.*
- *Normalised* CPS divide residuals by a difficulty estimate so that intervals widen where
  the model is less accurate. See {doc}`../../practitioner/advanced/normalization-guide`.

:::{admonition} Illustrative example
:class: note

A simulation with two equally large groups, one three times noisier than the other. The
90 % intervals cover close to 90 % of all cases, but far more in the quiet group and far
fewer in the noisy one. Mondrian calibration by group brings both close to 90 %. Shifting
the targets after calibration breaks exchangeability, and coverage drops. One run on
synthetic data; it illustrates the definitions and proves nothing.

```python
import numpy as np
from sklearn.ensemble import RandomForestRegressor


def make_data(n, rng, shift=0.0):
    x = rng.uniform(0, 1, size=(n, 3))
    group = (x[:, 0] > 0.5).astype(int)  # group 1 is three times noisier
    noise = rng.normal(0, np.where(group == 1, 3.0, 1.0))
    return x, 5 * x[:, 0] + 2 * x[:, 1] + noise + shift, group


def coverage(low, high, y):
    return np.mean((y >= low) & (y <= high))


rng = np.random.default_rng(0)
x_proper, y_proper, _ = make_data(500, rng)
x_cal, y_cal, group_cal = make_data(400, rng)
x_new, y_new, group_new = make_data(4000, rng)
x_shifted, y_shifted, _ = make_data(4000, rng, shift=2.0)

standard = WrapCalibratedExplainer(RandomForestRegressor(n_estimators=50, random_state=0))
standard.fit(x_proper, y_proper)
standard.calibrate(x_cal, y_cal)
_, (low, high) = standard.predict(x_new, uq_interval=True, low_high_percentiles=(5, 95))
print(f"standard, all cases:  {coverage(low, high, y_new):.3f}")
for g in (0, 1):
    in_g = group_new == g
    print(f"standard, group {g}:    {coverage(low[in_g], high[in_g], y_new[in_g]):.3f}")

mondrian = WrapCalibratedExplainer(RandomForestRegressor(n_estimators=50, random_state=0))
mondrian.fit(x_proper, y_proper)
mondrian.calibrate(x_cal, y_cal, bins=group_cal)
_, (low, high) = mondrian.predict(
    x_new, uq_interval=True, low_high_percentiles=(5, 95), bins=group_new
)
for g in (0, 1):
    in_g = group_new == g
    print(f"mondrian, group {g}:    {coverage(low[in_g], high[in_g], y_new[in_g]):.3f}")

_, (low, high) = standard.predict(x_shifted, uq_interval=True, low_high_percentiles=(5, 95))
print(f"standard, shifted:    {coverage(low, high, y_shifted):.3f}")
```

```text
standard, all cases:  0.879
standard, group 0:    0.999
standard, group 1:    0.768
mondrian, group 0:    0.910
mondrian, group 1:    0.909
standard, shifted:    0.820
```

The overall value 0.879 is below 0.90 for this one calibration set. That is consistent
with the guarantee, which averages over calibration sets as well as over new cases; a
single calibration set can land somewhat above or below the requested rate.
:::

## 4. Classification, interval regression and thresholded regression

| Mode | Call | Method | Output |
|---|---|---|---|
| Classification | `predict_proba(x, uq_interval=True)` | Venn–Abers on model scores | {math}`p` and {math}`[p_0, p_1]` |
| Interval regression | `predict(x, uq_interval=True, low_high_percentiles=(l, h))` | Split CPS on residuals, full calibration set | Median and prediction interval |
| Thresholded (probabilistic) regression | `predict_proba(x, threshold=t, uq_interval=True)` | CPS score, then Venn–Abers on the event {math}`y \le t`, on two halves of the calibration set | {math}`P(y \le t)` and {math}`[p_0, p_1]` |

The two kinds of interval answer different questions. *Terms under review.*

| | Classification and thresholded regression | Interval regression |
|---|---|---|
| What is uncertain | A probability | The value of {math}`y` |
| Interval | Venn–Abers pair {math}`[p_0, p_1]` (*probability interval*) | CPS percentiles in units of {math}`y` (*prediction interval*) |
| Formal statement | Calibration of {math}`p_Y`, selected by the unknown true label | Marginal coverage of {math}`y` |

:::{admonition} How CE does it: thresholded regression
:class: tip

CE splits the calibration set at random (seeded) into two halves. A CPS fitted on the
first half turns each case into a score, the CPS value {math}`Q(t)` for the event
{math}`y \le t`. A Venn–Abers predictor is fitted on the second half with labels
{math}`\mathbb{1}\{y_i \le t\}` and refitted for every new threshold. A tuple threshold
{math}`(t_0, t_1)` uses the event {math}`t_0 < y \le t_1`. Each step therefore uses about
half of the calibration cases. See {doc}`../../tasks/probabilistic_regression`.
:::

:::{admonition} Theoretical guarantee
:class: important

Because the score function is fixed by the first half before the second half and the test
case are used, the Venn–Abers validity of section 2 applies to the event
{math}`\{Y \le t\}`, under exchangeability of the second half and the test case.

*Wording under review: this follows from the Venn–Abers result and the calibration split
described above; the formulation has not yet been confirmed by the CE authors.*
:::

### Example with CE

```python
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

x, y = load_diabetes(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.33, random_state=0
)

regressor = WrapCalibratedExplainer(RandomForestRegressor(n_estimators=100, random_state=0))
regressor.fit(x_proper, y_proper)
regressor.calibrate(x_cal, y_cal)

median, (low, high) = regressor.predict(
    x_test[:1], uq_interval=True, low_high_percentiles=(5, 95)
)
print(f"median {median[0]:.1f}, 90% interval [{low[0]:.1f}, {high[0]:.1f}]")
print(f"model alone {regressor.predict(x_test[:1], calibrated=False)[0]:.1f}")

prob, (p_low, p_high) = regressor.predict_proba(x_test[:1], threshold=150, uq_interval=True)
print(f"P(y <= 150) = {prob[0, 1]:.3f}, probability interval [{p_low[0]:.3f}, {p_high[0]:.3f}]")
```

```text
median 246.4, 90% interval [165.7, 373.8]
model alone 250.6
P(y <= 150) = 0.056, probability interval [0.000, 0.059]
```

## 5. Assumptions and limitations

| Situation | What happens | What to do |
|---|---|---|
| Future data differ from the calibration data (drift, new population) | The guarantees no longer apply | Monitor; recalibrate on recent data |
| Subgroups with different noise | Coverage holds on average, not per group | Mondrian `bins`; check coverage per group |
| Calibration data also used for training | Errors look too small; intervals too narrow | Keep training, calibration and test data separate |
| Small calibration set | Wide Venn–Abers intervals; extreme percentiles may be undefined; thresholded queries use half the set | Use a larger calibration set |
| One-sided intervals | The open side is not a calibrated bound (a placeholder in v1.0.2; `-inf`/`inf` from v1.1.0) | Treat that side as open |
| Merged probability | No exact calibration guarantee | Use {math}`[p_0, p_1]` when validity matters |
| Multiclass default normalisation | Bounds rescaled; an upper bound can exceed 1 | `normalization="simplex"` |

Explanations are built on these calibrated outputs, but the guarantees above are stated
for predictions, not for feature weights and their intervals. The CE regression paper
notes that explanation intervals may not carry the same guarantees (Löfström et al., 2025,
§3.4). *Wording under review.* See
{doc}`../how-to/interpret_explanations` and {doc}`alternatives`.

:::{admonition} Under review
:class: warning

The CE authors are reviewing the following points, and this page will be updated with
their decisions:

- the wording of the Venn–Abers guarantee, including for thresholded regression;
- whether coverage is stated as "at least" or "about" the requested rate, and the
  Mondrian statement;
- the terms *probability interval* and *prediction interval*;
- exchangeability as the single stated assumption;
- the default multiclass normalisation;
- how the uncertainty intervals of feature weights should be described.
:::

## 6. Exercises

1. Is a model that always predicts the base rate calibrated? Is it useful?
2. In the Venn–Abers example, compute {math}`p_0` and {math}`p_1` for a test score of 0.30,
   and the merged probability.
3. Same data, test score 0.90.
4. In the CPS example, give the 80 % interval, percentiles (10, 90).
5. In the CPS example, compute {math}`Q(9)`.
6. Overall coverage is 0.90, but 0.80 in one group. Is the guarantee broken? What helps?
7. Why do threshold questions need more calibration data than interval questions?

:::{dropdown} Answers
1. Calibrated, by the definition in section 1; not useful, because it does not
   distinguish cases.
2. {math}`p_0 = 0.25`, {math}`p_1 = 0.50`, merged {math}`0.50 / 1.25 = 0.40`.
3. {math}`p_0 = 0.60`, {math}`p_1 = 1.00`, merged {math}`1.00 / 1.40 = 0.7143`.
4. {math}`a = \lfloor 0.1 \cdot 20 \rfloor = 2` gives {math}`10 - 2.4 = 7.6`;
   {math}`b = \lceil 0.9 \cdot 20 \rceil = 18` gives {math}`10 + 2.2 = 12.2`;
   coverage {math}`(18 - 2)/20 = 0.80`.
5. Five residuals satisfy {math}`10 + \alpha_i \le 9`, so {math}`Q(9) = 6/20 = 0.30`.
6. No: the guarantee is marginal. Mondrian calibration by group gives coverage within each
   group.
7. The calibration set is split in half between the CPS and Venn–Abers.
:::

## References

**Calibrated Explanations** (full list: {doc}`../../citing`)

- Löfström, H., Löfström, T., Johansson, U., and Sönströd, C. (2024). Calibrated
  explanations: With uncertainty information and counterfactuals. *Expert Systems with
  Applications*, 123154. [doi:10.1016/j.eswa.2024.123154](https://doi.org/10.1016/j.eswa.2024.123154).
- Löfström, T., Löfström, H., Johansson, U., Sönströd, C., and Matela, R. (2025).
  Calibrated explanations for regression. *Machine Learning*, 114, 100.
  [doi:10.1007/s10994-024-06642-8](https://doi.org/10.1007/s10994-024-06642-8).

**Venn–Abers and conformal prediction**

- Vovk, V., and Petej, I. (2014). Venn-Abers predictors. *Proceedings of UAI 2014*.
  [arXiv:1211.0025](https://arxiv.org/abs/1211.0025).
- Vovk, V., Petej, I., and Fedorova, V. (2015). Large-scale probabilistic predictors with
  and without guarantees of validity. *Advances in Neural Information Processing Systems
  28*. [arXiv:1511.00213](https://arxiv.org/abs/1511.00213).
- Vovk, V., Gammerman, A., and Shafer, G. (2022). *Algorithmic Learning in a Random World*
  (2nd ed.). Springer. [doi:10.1007/978-3-031-06649-8](https://doi.org/10.1007/978-3-031-06649-8).
- Vovk, V., Shen, J., Manokhin, V., and Xie, M. (2019). Nonparametric predictive
  distributions based on conformal prediction. *Machine Learning*, 108, 445–474.
  [doi:10.1007/s10994-018-5755-8](https://doi.org/10.1007/s10994-018-5755-8).
- Vovk, V., Petej, I., Nouretdinov, I., Manokhin, V., and Gammerman, A. (2020).
  Computationally efficient versions of conformal predictive distributions.
  *Neurocomputing*, 397, 292–308.
  [doi:10.1016/j.neucom.2019.10.110](https://doi.org/10.1016/j.neucom.2019.10.110).
- Boström, H. (2022). crepes: a Python package for generating conformal regressors and
  predictive systems. *Proceedings of COPA 2022*, PMLR 179, 24–41.
- Boström, H., Johansson, U., and Löfström, T. (2021). Mondrian conformal predictive
  distributions. *Proceedings of COPA 2021*, PMLR 152, 24–38.
- Vovk, V. (2012). Conditional validity of inductive conformal predictors. *Proceedings
  of the Asian Conference on Machine Learning*, PMLR 25, 475–490.
  [arXiv:1209.2673](https://arxiv.org/abs/1209.2673).
- Lei, J., G'Sell, M., Rinaldo, A., Tibshirani, R. J., and Wasserman, L. (2018).
  Distribution-free predictive inference for regression. *Journal of the American
  Statistical Association*, 113(523), 1094–1111.
  [doi:10.1080/01621459.2017.1307116](https://doi.org/10.1080/01621459.2017.1307116).

**Calibration**

- Guo, C., Pleiss, G., Sun, Y., and Weinberger, K. Q. (2017). On calibration of modern
  neural networks. *Proceedings of the 34th International Conference on Machine
  Learning*, PMLR 70, 1321–1330. [arXiv:1706.04599](https://arxiv.org/abs/1706.04599).
- Dawid, A. P. (1982). The well-calibrated Bayesian. *Journal of the American Statistical
  Association*, 77(379), 605–610.
  [doi:10.1080/01621459.1982.10477856](https://doi.org/10.1080/01621459.1982.10477856).
