# Machine learning essentials

Calibrated explanations build on the roles of predictive models, data and
evaluation. The running example is the
one used later in the {doc}`walkthrough <quickstart_walkthrough>`: deciding
whether a breast-tumour sample is malignant or benign from measurements of its
cells.

(ml-a1)=

## A1. What is an AI/ML model?

**Machine learning (ML)** learns patterns from examples instead of relying
entirely on rules written by hand. It is one approach to artificial intelligence
(AI). For CE, the relevant object is the trained predictive model: something
you can ask for a class or a numeric prediction.

A model learns a relationship between **inputs** and an **output**:

- The inputs are **features**, the measured properties of each example. In the
  running example these are 30 measurements such as cell radius and texture.
- The output is the **target** (also called the label), the thing we want to
  predict: *malignant* or *benign*.

Using a model has two phases. During **training**, the model sees examples
where the target is known and adjusts its internal parameters. During
**inference** (prediction), it receives new inputs and produces an output for
cases it has never seen.

## A2. How does machine learning learn?

CE works with **supervised** predictive models, trained on examples with known
targets. In the running example, the inputs are cell measurements and the known
target is malignant or benign. CE needs additional labelled cases for
calibration after the model has been trained.

These pages focus on supervised prediction: first learn from known outcomes,
then calibrate and explain predictions for new cases.

## A3. From a problem to a prediction task

A real problem has to be turned into a precise **prediction task** before any
model is trained. The task depends on the output you want, not on the kind of
input data.

| If you want to predict… | The task is | Example output |
|---|---|---|
| One of two categories | Binary classification | *malignant* or *benign*, plus a probability such as 0.29 for *benign* |
| One of several categories | Multiclass classification | *setosa*, *versicolor* or *virginica*, plus a probability for each |
| A number | Regression | a disease-progression score of 172 |

A probability is not a separate task: classification models usually output a
probability for each class alongside the predicted label, and a regression
model can be asked about an event on its numeric target. CE calibrates these
outputs in different ways; {doc}`ce-tasks-and-modes` introduces the choices.

These CE workflows use **tabular** features: rows describe cases and columns
describe measurements. The same patient records could support classification
(*will this patient be readmitted?*) or regression (*how many days until
readmission?*). Choose the question before choosing how to read CE's output.

## A4. Model families, architectures and algorithms

A model's family describes its form; its training algorithm describes how
it is fitted. The running example uses a random forest, an ensemble of
decision trees. CE does not require this particular family or algorithm.

For CE, the practical question is whether the fitted model supplies the
prediction methods the chosen workflow needs: `predict`, and for classifiers
`predict_proba`. The {doc}`tasks and modes guide <ce-tasks-and-modes>` explains
compatibility. Model selection is a separate task; use the
[scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)
for deeper background on families, algorithms and tuning.

## A5. Developing a model: the data sets and their roles

A model is only as trustworthy as the way it was developed and tested. The
data is split so that each step uses examples it has not seen before.

```{mermaid}
flowchart LR
    D["All labelled data"] --> TR["Proper training set<br/>fit the model"]
    D --> CA["Calibration set<br/>calibrate CE"]
    D --> TE["Test set<br/>evaluate and explain"]
    TR --> M["Trained model"]
    M --> C["Calibrated explainer"]
    CA --> C
    C --> R["Predictions with uncertainty<br/>and explanations"]
    TE --> R
```

Read the three branches from **All labelled data** as separate roles, not
three successive training stages. Only the proper training branch fits the
model. The trained model and calibration branch meet at the calibrated
explainer; the test branch supplies cases on which to evaluate its outputs.
This separation lets CE relate model outputs to held-out outcomes before
producing predictions and explanations for new cases.

| Step | Purpose |
|---|---|
| Data preparation | Clean the data and choose the features |
| Training | Fit the model's parameters on the proper training set |
| Validation | Choose settings, such as the number of trees, without touching the test set |
| Calibration | Measure how the trained model's outputs relate to real outcomes on unseen data |
| Testing | Estimate performance on data used for nothing else |
| Inference | Predict for new cases in use |

The walkthrough uses the model's default settings, so it needs no validation
set and splits the data into three parts only: proper training, calibration
and test. If you tune settings, take the validation data from the training
portion, never from the calibration or test sets.

**Data leakage** happens when information from the evaluation or calibration
data reaches the model during training, for example by scaling features with
statistics computed on all the data. Leakage makes a model look better and
more reliable than it is. The simplest protection is to split first and do
every fitting step on the training portion only.

**Evaluation** measures how well the model predicts. For classification,
accuracy is the share of correct labels; for regression, error measures such
as mean absolute error describe how far predictions are from the truth.

(why-predictions-are-not-enough)=

## A6. Why predictions are not enough

A model can predict the right class often while reporting misleading
probabilities. **Calibration** asks whether predicted probabilities agree with
outcome frequencies over cases; it is different from label accuracy.

CE calibrates first, then explains the calibrated output with feature rules
and ranges. The next page, {doc}`why-ce`, shows what changes in the workflow
and follows one output. Its ranges have
{doc}`mode-specific meanings and limits <../foundations/concepts/calibrated_interval_semantics>`;
they do not establish that an individual prediction is correct or that a
feature causes the outcome.

Go deeper: {doc}`../foundations/concepts/calibration_methods` explains what
calibration means and how CE calibrates.

## A7. What a model explanation is

An **explanation** of a prediction tells you which inputs the prediction
depends on, so a person can check it against what they know.

CE gives **local explanations**: explanations of individual predictions,
rather than a **global** description of the whole model. A factual explanation
pairs a feature condition, such as `worst concave points > 0.14`, with a weight
and a range. The weight describes the model's response to substituted feature
values; it does not show that the feature causes the outcome.

Other methods use feature attributions, numbers describing each feature's
contribution to an output. LIME (Ribeiro, Singh and Guestrin, 2016) and SHAP
(Lundberg and Lee, 2017) are examples. For how CE combines conditions and
weights, continue to the worked example rather than treating the methods as
interchangeable.

The {doc}`walkthrough <quickstart_walkthrough>` shows how CE builds and reads
one explanation step by step. CE's explanation method is described in
Löfström, Löfström, Johansson and Sönströd (2024),
[*Calibrated explanations: with uncertainty information and counterfactuals*](https://doi.org/10.1016/j.eswa.2024.123154),
*Expert Systems with Applications*, 246, 123154.

**References for this section**

- Ribeiro, M. T., Singh, S., and Guestrin, C. (2016). "Why should I trust
  you?" Explaining the predictions of any classifier. *Proceedings of the
  22nd ACM SIGKDD International Conference on Knowledge Discovery and Data
  Mining*, 1135–1144. [doi:10.1145/2939672.2939778](https://doi.org/10.1145/2939672.2939778).
- Lundberg, S. M., and Lee, S.-I. (2017). A unified approach to interpreting
  model predictions. *Advances in Neural Information Processing Systems 30*.
  [arXiv:1705.07874](https://arxiv.org/abs/1705.07874).

<span id="continue"></span>

## From predictive models to CE

The {doc}`CE workflow <why-ce>` adds calibration and explanation to these
data and model roles. The {doc}`Python walkthrough <quickstart_walkthrough>`
uses the same classification example to show the resulting predictions,
rules and alternatives.
