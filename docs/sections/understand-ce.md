# Understand CE

This section explains the methods, assumptions and guarantees behind
Calibrated Explanations: what problem CE addresses and when it is useful,
then how its workflow produces calibrated outputs and explanations and which
assumptions those outputs rest on. New to the vocabulary? Take the
{doc}`Quick Start <../get-started/try-in-browser>` first; it introduces every
term used here with two worked cases.

Each concept has one main page in this section. Other pages summarize it and
link here.

(ce-what-why)=
## CE: What & Why

*What problem does CE address, and when is it useful?*

A model's output often looks like a probability, but it may not behave like
one, and it does not say how much evidence lies behind it. Explanation
methods that describe that output inherit both limits: they show which
features drive the output, not how far the output or the explanation can be
relied on.

CE first calibrates the model's outputs on held-out labelled data, then
explains the calibrated output. Prediction calls can return uncertainty
information, and explanations report ranges for their feature weights. These
ranges describe different quantities; they do not establish cause and
effect, and their statistical meaning requires stated assumptions.

CE outputs can also support a discussion of transparency and oversight. The
{doc}`EU AI Act context <../practitioner/playbooks/eu-ai-act-compliance>`
playbook (in *CE in Practice*) examines that relationship; it is not evidence
of compliance, and its compliance wording remains under review.

1. {doc}`Why CE <../get-started/why-ce>`: why uncertainty matters, and how a
   machine-learning workflow changes when CE is added.
2. {doc}`Predictive tasks, CE modes and capabilities <../get-started/ce-tasks-and-modes>`:
   classification, interval regression and probabilistic (thresholded)
   regression, and the question each answers.

(how-ce-works)=
## How CE Works

*How does the workflow produce calibrated outputs and explanations, and what
assumptions matter?*

Every CE output can be traced along one chain:
**task → CE mode → statistical method → output and what its range means →
assumptions and guarantees**. Venn–Abers predictors supply classification
probability information; conformal predictive systems (CPS) supply
regression prediction information. Prediction bounds, prediction intervals
and explanation-weight ranges do not share one guarantee.

{ref}`Which method CE uses for each task <ce-workflow-methods>` shows the
chain for the three modes in one table; the
{ref}`worked construction <ce-workflow-explanations>` builds a factual weight
step by step; and {ref}`What the guarantees rest on <ce-workflow-guarantees>`
separates the assumptions from what they do and do not give you.

3. {doc}`The CE workflow <../foundations/concepts/ce_workflow>`: fit,
   calibrate, predict, explain; how a calibrated prediction becomes the input
   of an explanation, with one worked construction.
4. {doc}`Calibration by task <../foundations/concepts/calibration_methods>`:
   Venn–Abers predictors for classification and conformal predictive systems
   for regression, with the formal statements.
5. {doc}`Guarantees and limits by mode <../foundations/concepts/calibrated_interval_semantics>`:
   interval semantics, assumptions, guarantees and non-guarantees.
6. {doc}`Factual and alternative explanations <../foundations/concepts/alternatives>`:
   the "why" and "what if" explanations, and ensured filters.

## Context and foundations

7. {doc}`Comparison with other methods <../compare>`: what CE answers that
   attribution methods, counterfactual methods and conformal prediction
   alone do not.
8. {doc}`ML and statistical foundations <../foundations/index>`: features,
   targets, training, calibration and evaluation data, starting from the
   {doc}`machine-learning essentials <../get-started/ml-foundations>` for
   readers new to machine learning.

Further concept pages, on explanation structures, guarded explanations and
probabilistic regression, are collected in
{doc}`More concepts <../foundations/concepts/index>`. Short definitions are in
the {doc}`Scientific & Theoretical Glossary <../glossary/science>`.

Software components and execution flow are described separately, under
{doc}`Software Architecture & Integration <software-integration>`.

**Next section:** {doc}`Use CE: CE in Practice <in-practice>`.

```{toctree}
:hidden:
:maxdepth: 2

Why CE <../get-started/why-ce>
Tasks, Modes and Capabilities <../get-started/ce-tasks-and-modes>
The CE Workflow <../foundations/concepts/ce_workflow>
Calibration by Task <../foundations/concepts/calibration_methods>
Guarantees and Limits by Mode <../foundations/concepts/calibrated_interval_semantics>
Factual and Alternative Explanations <../foundations/concepts/alternatives>
Comparison with Other Methods <../compare>
ML and Statistical Foundations <../foundations/index>
```
