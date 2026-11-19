# CE: What & Why

Understand what Calibrated Explanations adds to a predictive model, why
calibration matters, and how to interpret CE's outputs and limits.
{doc}`What CE Is <../what-is-ce>` defines the method's scope and assumptions;
the section then shows what changes in a workflow when CE is added and
compares CE with other explanation methods.

A model's output often looks like a probability, but it may
not behave like one, and it does not say how much evidence lies behind it.
Explanation methods that describe that output inherit both limits: they show
which features drive the output, not how far the output or the explanation can
be relied on.

CE first calibrates the model's outputs on held-out data, then explains the
calibrated output. Prediction calls can return uncertainty information when
requested, and explanations report ranges for their feature weights. These
ranges describe different quantities; their interpretation depends on the
task and method. They do not establish cause and effect, and statistical
guarantees require the stated assumptions. For guarantees, assumptions and
non-guarantees, see {doc}`../foundations/concepts/calibrated_interval_semantics`.

<span id="read-in-this-order"></span>

## Predictions, calibration and explanations

A predictive model maps features to an output, such as a class score or a
numeric target prediction. If those terms are unfamiliar, the
{doc}`machine-learning essentials <../get-started/ml-foundations>` explain
them using the same example as the CE tutorials.

A score that resembles a probability need not be calibrated. Calibration
concerns how reported probabilities relate to observed outcomes; accuracy
concerns whether predicted labels are correct. The distinction is developed
in {ref}`Calibration is not accuracy <wic-calibration>`. Explaining a
model's score does not by itself supply that calibration information.

<span id="pages-in-this-section"></span>

## What CE adds to the model output

CE uses held-out calibration data to obtain task-appropriate prediction
information, then compares model responses to feature conditions or
substituted values. A factual explanation describes conditions that hold for
the case; an alternative reports a prediction under a different condition.
{doc}`CE by example <../get-started/ce-by-example>` follows these quantities
for one real prediction, including the ranges reported with them.

The ranges need interpretation alongside the methods and assumptions that
produced them. They do not make an explanation causal or establish that a
prediction is correct. The {doc}`comparison with other methods <../compare>`
helps distinguish CE's purpose from other explanation tools.

CE outputs can also support a discussion of transparency and oversight.
The {doc}`EU AI Act context <../practitioner/playbooks/eu-ai-act-compliance>`
playbook (in *CE in Practice*) examines that relationship; it is not evidence of compliance, and its
compliance wording remains under review.

## Pages in this section

Read them in this order:

1. {doc}`What CE Is <../what-is-ce>`: the canonical definition, the problem
   CE addresses, what it provides and what it does not.
2. {doc}`Why CE <../get-started/why-ce>`: why uncertainty matters, and how a
   machine-learning workflow changes when CE is added, shown in one figure.
3. {doc}`Tasks, modes and capabilities <../get-started/ce-tasks-and-modes>`:
   the tasks CE supports (classification, regression, probabilistic
   regression) and which question each answers. Use it to choose your task.
4. {doc}`Comparison with other methods <../compare>`: what CE answers that
   attribution methods, counterfactual methods and conformal prediction
   alone do not.

Once you know your task, {doc}`How CE Works <how-ce-works>` explains what
CE's output means for it, and {doc}`CE in Practice <in-practice>` shows how
to generate and read it. To see CE's outputs without installing anything,
take the {doc}`browser Quick Start <../get-started/try-in-browser>`.

**Next section:** {doc}`How CE Works <how-ce-works>`.

```{toctree}
:hidden:
:maxdepth: 2

What CE Is <../what-is-ce>
Why CE: From a Conventional to a CE Workflow <../get-started/why-ce>
Tasks, Modes and Capabilities <../get-started/ce-tasks-and-modes>
Comparison with Other Methods <../compare>
```
