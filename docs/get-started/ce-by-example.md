# CE by example: one prediction, explained

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
30 measurements of cell nuclei. For one test sample, **case 2**, the
model says *malignant*. Before anyone acts on it, three questions matter:

1. **How sure is the model**, and how certain is that probability?
2. **Which measurements drive the prediction?**
3. **What would change it?**

## 2. The data and its three roles

The dataset has 569 samples (212 *malignant*, 357 *benign*). CE
reports the probability of class 1, which here is *benign*.

| Set | Cases | Job | Used to train the model? |
|---|---|---|---|
| Proper training | 341 | Fit the model | Yes |
| Calibration | 114 | Let CE measure how the model's outputs relate to real outcomes | No |
| Test | 114 | Check the results on cases nobody has used | No |

## 3. The model alone

A random forest predicts the correct label for about 95% of
the test cases (accuracy 0.947). Accuracy counts correct labels; it does not say
whether the model's probabilities can be taken at face value. On the test set,
41 of the 114 raw probabilities are exactly 0 or 1, a claim of
certainty that is a common reason to check calibration. (41 of
those 41 were correct, so this is not evidence that they are wrong.)

## 4. Calibrated probabilities, each with a range

CE calibrates the model on the calibration set; for classification it uses
**Venn–Abers predictors**. The model itself is not changed. For the first five
test cases, the probability of *benign* from the model alone and from CE:

| Case | Model alone | CE | CE range | Predicted (true) |
|---|---|---|---|---|
| 0 | 0.00 | 0.029 | [0.000, 0.029] | *malignant* (malignant) |
| 1 | 1.00 | 0.973 | [0.972, 1.000] | *benign* (benign) |
| 2 | 0.16 | 0.286 | [0.167, 0.333] | *malignant* (malignant) |
| 3 | 0.21 | 0.324 | [0.167, 0.400] | *malignant* (benign) |
| 4 | 0.00 | 0.029 | [0.000, 0.029] | *malignant* (malignant) |

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
- **One observation.** Case 3 has the widest range of the five and is
  the one the model gets wrong. That is a useful observation, but one case
  supports no general claim.
- **Not a guaranteed score improvement.** On this test set the Brier score
  (the mean squared difference between probability and outcome; lower is
  better) is 0.0366 for the model alone and 0.0445 with CE, so CE's
  probabilities scored worse (higher) here. One small test set settles nothing either
  way.

## 5. Why case 2 is predicted *malignant*

For case 2, CE's calibrated probability of *benign* is **0.286**, with range
**[0.167, 0.333]**. The probability is below 0.5, so the predicted label is
*malignant*; the whole range also lies below 0.5, so the calibration data
support that label throughout the range.

CE's **factual explanation** lists conditions that hold for this case. Each
condition has a **weight**: how much the calibrated probability of *benign*
would differ if that feature took typical values from the other side of the
condition, with all other features unchanged. Each weight has its own range.
The six strongest:

| Condition (holds for case 2) | Weight | Weight range |
|---|---|---|
| `worst concave points > 0.14` | −0.190 | [−0.314, −0.048] |
| `worst area <= 853.50` | +0.143 | [+0.119, +0.286] |
| `worst concavity <= 0.35` | +0.135 | [+0.108, +0.286] |
| `mean concavity > 0.07` | −0.048 | [−0.114, +0.086] |
| `mean concave points > 0.04` | −0.048 | [−0.114, +0.086] |
| `worst texture > 23.91` | −0.042 | [−0.114, +0.108] |

- **Sign.** A negative weight means the condition lowers the probability of
  *benign* (towards *malignant*); a positive weight raises it.
- **The strongest reason** is `worst concave points > 0.14`: with typical values from the other
  side instead, the calibrated probability of *benign* would be about
  0.19 higher. Its whole weight range lies below 0: the
  averaged lower and upper bounds agree on the direction. (No formal guarantee
  is claimed for weight ranges.)
- **Uncertain direction.** For `mean concavity > 0.07` the weight range includes 0: the
  averaged bounds do not settle whether it raises or lowers the probability.
- **Not a sum.** Each weight is computed one feature at a time; the weights do
  not add up to the prediction (their sum is −0.069).
- **Not a cause.** A weight compares the model's responses; it says nothing
  about what causes a tumour to be malignant.

```{figure} walkthrough_assets/walkthrough-figure-1.png
:alt: Factual explanation plot for case 2. Top: calibrated probability of benign 0.286 with its range from 0.167 to 0.333. Below: one bar per condition showing its weight range; worst concave points above 0.14 has the largest range entirely below zero.

CE output for case 2, drawn by CE's own plot function in the Python
walkthrough. Each bar covers a weight's range; red bars raise the probability
of *benign*, blue bars lower it.
```

The [guide to reading CE explanations](../foundations/how-to/interpret_explanations.md)
explains every element of this plot.

## 6. What would change it: alternative explanations

An **alternative explanation** asks: *if one feature had a value in a
different range, what would the calibrated probability be?*

| If, instead, … | Calibrated P(benign) | Range |
|---|---|---|
| `worst concave points < 0.14` | 0.476 | [0.333, 0.600] |
| `worst area > 853.50` | 0.143 | [0.000, 0.167] |
| `worst concavity > 0.35` | 0.151 | [0.000, 0.178] |
| `mean concavity < 0.13` | 0.333 | [0.200, 0.400] |
| `worst area < 745.15` | 0.333 | [0.200, 0.400] |
| `mean concave points < 0.06` | 0.333 | [0.200, 0.400] |

- If `worst concave points < 0.14` held, the calibrated
  probability of *benign* would be **0.476**, with range [0.333, 0.600]. The
  estimate stays below 0.5, but the range reaches above it: in that scenario CE
  would no longer clearly favour either class.
- Alternatives describe how the **model** would respond. They are not
  recommendations, and they do not say that changing a measurement would
  change the real outcome.

## 7. What we can and cannot conclude

**We can say.** The model predicts *malignant*. CE's calibrated probability of
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
