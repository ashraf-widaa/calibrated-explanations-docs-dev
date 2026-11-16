# CE: What & Why

Understand what Calibrated Explanations adds to a predictive model, why
calibration matters, and how to interpret CE's outputs and limits.

**The problem.** A model's output often looks like a probability, but it may
not behave like one, and it does not say how much evidence lies behind it.
Explanation methods that describe that output inherit both limits: they show
which features drive the output, not how far the output or the explanation can
be relied on.

**CE's answer.** CE first calibrates the model's outputs on data the model
never saw, then explains the calibrated output, and gives every prediction and
every feature effect a range. It does not establish cause and effect, and its
guarantees hold only under stated assumptions. For guarantees, assumptions and
non-guarantees, see {doc}`../foundations/concepts/calibrated_interval_semantics`.

## Read in this order

Each step answers one question, in plain words; the last column leads to the
detail when you want it.

| # | Question | Read | Go deeper |
|---|---|---|---|
| 1 | What does a machine-learning model produce? | {ref}`Understanding AI models, A1 <ml-a1>` | {doc}`../get-started/ml-foundations` (A2–A5) |
| 2 | Why is an explanation of that output not enough on its own? | {ref}`The problem <wic-problem>` | {doc}`../compare` |
| 3 | What is calibration, and how is it different from accuracy? | {ref}`Calibration is not accuracy <wic-calibration>` | {doc}`../foundations/concepts/calibration_methods` |
| 4 | What problem does CE address, and what does it produce? | {ref}`What CE adds <wic-adds>` | {doc}`../get-started/ce-by-example` |
| 5 | When might CE be useful? | {ref}`When CE is a good fit <wic-fit>` | {doc}`../practitioner/evaluate_ce` |
| 6 | What does CE not guarantee? | {ref}`What CE guarantees, and what it does not <wic-guarantees>` | {doc}`../foundations/concepts/calibrated_interval_semantics` |
| 7 | Where does regulation come in? | {doc}`Regulation context (EU AI Act) <../practitioner/playbooks/eu-ai-act-compliance>` | — |

New to machine learning? Start with the {doc}`Quick Start, Path A <../get-started/index>`.
Ready to see real CE output? Go to {doc}`CE by example <../get-started/ce-by-example>`.

## Pages in this section

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Understanding AI Models
:link: ../get-started/ml-foundations
:link-type: doc

Machine-learning basics: models, learning, prediction tasks, data roles and why a prediction alone is not enough.
:::

:::{grid-item-card} Can We Trust AI Outputs?
:link: why-predictions-are-not-enough
:link-type: ref

Why accuracy is not enough: miscalibrated probabilities, hidden uncertainty and explanations without a measure of their reliability.
:::

:::{grid-item-card} What Is CE & What Does It Add?
:link: ../what-is-ce
:link-type: doc

The problem CE addresses, what it adds, what it guarantees and does not, and when it fits.
:::

:::{grid-item-card} The Explainability Gap
:link: ../compare
:link-type: doc

A short comparison of CE with SHAP, LIME and conformal prediction packages.
:::

:::{grid-item-card} Regulation Context (EU AI Act)
:link: ../practitioner/playbooks/eu-ai-act-compliance
:link-type: doc

A detailed practitioner guide to how CE's outputs relate to EU AI Act obligations. It is not evidence of compliance, and its compliance wording is under review.
:::
::::

Entry-point tier: Tier 3.
