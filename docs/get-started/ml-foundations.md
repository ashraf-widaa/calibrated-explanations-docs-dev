# Machine learning basics

This page gives you just enough machine learning to follow the rest of the
Quick Start. If you already train and evaluate scikit-learn models, skip to
{doc}`ce-tasks-and-modes`.

Each section answers what a concept is, why it matters for calibrated
explanations, and how it shows up in practice. The running example is the
one used later in the {doc}`walkthrough <quickstart_walkthrough>`: deciding
whether a breast-tumour sample is malignant or benign from measurements of its
cells.

## A1. What is an AI/ML model?

**Artificial intelligence (AI)** is the broad goal of building systems that
perform tasks we associate with intelligence. **Machine learning (ML)** is one
way to get there: instead of writing rules by hand, we let a program learn
patterns from examples. **Deep learning** is a part of machine learning that
uses large neural networks.

```{mermaid}
flowchart LR
    AI["Artificial intelligence<br/>(the broad goal)"] --> ML["Machine learning<br/>(learn patterns from data)"]
    ML --> DL["Deep learning<br/>(large neural networks)"]
```

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

Machine learning methods differ in what kind of feedback they learn from.

| Learning approach | Learns from | Typical example |
|---|---|---|
| Supervised learning | Examples with known targets | Predicting a diagnosis from labelled patient records |
| Unsupervised learning | Examples without targets | Grouping customers with similar behaviour |
| Self-supervised learning | Targets created from the data itself | Predicting a hidden word in a sentence |
| Reinforcement learning | Rewards from acting in an environment | Learning to play a game by trial and error |

Calibrated Explanations works with **supervised** predictive models: models
trained on labelled examples that predict a class or a number for a new case.
It does not explain clustering, reinforcement-learning policies or generated
text.

## A3. From a problem to a prediction task

A real problem has to be turned into a precise **prediction task** before any
model is trained. The task depends on the output you want, not on the kind of
input data.

| If you want to predict… | The task is | Example output |
|---|---|---|
| One of two categories | Binary classification | *malignant* or *benign*, plus a probability such as 0.29 for *benign* |
| One of several categories | Multiclass classification | *setosa*, *versicolor* or *virginica*, plus a probability for each |
| A number | Regression | a disease-progression score of 172 |
| New content | Generation | a paragraph of text |

A probability is not a separate task: classification models usually output a
probability for each class alongside the predicted label, and a regression
model can be asked how likely an outcome above or below some value is. Those
probabilities are what calibration, later on this path, makes reliable.

Data comes in many forms: **tabular** data (rows and columns, like a
spreadsheet), **images**, **text** and **time series**. The same data can
support different tasks. Patient records can feed a classifier (*will this
patient be readmitted?*) or a regression model (*how many days until
readmission?*). The form of the data does not decide the task for you.

CE's core workflows are classification and regression on tabular features.
Generation is listed here only for contrast.

## A4. Model families, architectures and algorithms

Four words are often mixed up. They answer different questions:

```{mermaid}
flowchart LR
    P["Problem<br/>Is this tumour benign?"] --> T["Task<br/>Binary classification"]
    T --> F["Model family<br/>Tree ensemble"]
    F --> A["Architecture<br/>Random forest, 100 trees"]
    A --> O["Training algorithm<br/>Bootstrap sampling + greedy splits"]
```

- The **learning approach** is how the model gets feedback (A2).
- The **task** is what it predicts (A3).
- The **model family** and **architecture** describe the form of the model.
- The **training algorithm** is the procedure that sets its parameters.

You do not need to remember the families below to use CE; skim the table and
move on. Common model families for tabular data:

| Model family | How it works, in one line | Strengths | Watch out for |
|---|---|---|---|
| Linear models | Weighted sum of features | Fast, transparent | Miss non-linear patterns |
| Decision trees | A sequence of yes/no questions | Easy to read | Unstable, overfit easily |
| Random forests and other ensembles | Many trees vote or average | Strong default for tables | Less transparent |
| Neural networks | Layers of learned transformations | Very flexible | Need more data and tuning |
| Transformers | Neural networks built around attention | State of the art for text and sequences | Large and data-hungry |

Choose a model by the size and type of your data, the accuracy you need, how
fast it must run, and how much transparency the setting requires. CE adds
calibrated uncertainty and explanations on top of whichever model you choose;
it does not require a particular family.

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

A model with high accuracy can still mislead you about individual cases.

- **Probabilities may be miscalibrated.** Many models output scores that look
  like probabilities but are not: of the cases a model scores at 0.9, far
  fewer or far more than 90% may actually be positive. A **calibrated**
  probability matches the observed frequency of outcomes.
- **Uncertainty is usually hidden.** A single number such as 0.29 says nothing
  about how well the data support it. Reporting a range shows whether the
  estimate rests on many comparable cases or very few.
- **Predictions need reasons.** People who act on a prediction often need to
  know which features it depends on, so they can check it against their own
  knowledge.
- **Ordinary explanations have limits.** Many explanation methods report a
  feature's importance without saying how certain that importance is, and
  without connecting it to a calibrated prediction.

Calibrated Explanations addresses these points for supported supervised
models. It calibrates the model's outputs on held-out data, reports
uncertainty for predictions and for each feature's effect, and offers
alternative explanations that show how the prediction would change. These
guarantees hold under {doc}`stated assumptions <../foundations/concepts/calibrated_interval_semantics>`, and an explanation never proves
cause and effect. The next page shows which tasks and outputs CE supports.

Go deeper: {doc}`../foundations/concepts/calibration_methods` explains what
calibration means and how CE calibrates.

## A7. What a model explanation is

An **explanation** of a prediction tells you which inputs the prediction
depends on, so a person can check it against what they know.

- **Local or global.** A *local* explanation describes one prediction ("for
  this tumour sample, the measurement `worst concave points` mattered most").
  A *global* explanation describes the model as a whole ("across all samples,
  these features matter most"). CE explains individual predictions: its
  explanations are local.
- **Two common forms.** Some methods give each feature a number, a
  *feature attribution*, that shows how much it pushed the prediction up or
  down; LIME (Ribeiro, Singh and Guestrin, 2016) and SHAP (Lundberg and Lee,
  2017) are widely used examples. Other methods give *rules*: conditions
  such as `worst concave points > 0.14` that hold for the case. CE combines
  the two: each rule comes with a weight, and each weight comes with an
  uncertainty range.
- **What an explanation shows.** It describes how the **model** responds to
  its inputs. It does not show that a feature causes the outcome in the
  real world, and it can only be as reliable as the model and the data
  behind it.

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

**Next:** {doc}`ce-tasks-and-modes`

Entry-point tier: Tier 1.
