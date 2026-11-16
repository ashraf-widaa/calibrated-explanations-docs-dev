# How CE Works: The Theory Behind It

Explore the scientific foundations, statistical mechanisms and assumptions
behind calibrated explanations.

For guarantees, assumptions and non-guarantees, see
{doc}`../foundations/concepts/calibrated_interval_semantics`.

For short definitions of terms, see the {doc}`Scientific & Theoretical Glossary <../glossary/science>`.

## The chain to follow

Every CE output can be traced along one chain:

**task → CE mode → statistical method → output and what its range means →
assumptions and guarantees**.

{ref}`Which method CE uses for each task <ce-workflow-methods>` shows the chain
for the three modes in one table, and
{ref}`What the guarantees rest on <ce-workflow-guarantees>` separates the
assumptions from what they do and do not give you.

## Read in this order

Levels: **L1** understand (plain words), **L2** apply and interpret (real
output, how to read it), **L3** investigate (definitions, derivations,
assumptions and references).

1. {doc}`The CE workflow <../foundations/concepts/ce_workflow>` (L1): the
   whole picture, the chain above, and a learning path.
2. {ref}`How an explanation is built <ce-workflow-explanations>` (L1–L2): rules,
   substituted values, factual weights and alternative predictions.
3. {doc}`How to read CE explanations <../foundations/how-to/interpret_explanations>`
   (L2): factual and alternative explanations, rule tables and plots.
4. {doc}`Statistical methods behind CE <../foundations/concepts/calibration_methods>`
   (L2–L3): Venn–Abers predictors and conformal predictive systems, with
   worked examples and derivations.
5. {doc}`Guarantees by mode <../foundations/concepts/calibrated_interval_semantics>`
   (L3): the canonical statement of what holds in each mode, under which
   assumptions, and what does not.

Missing a prerequisite? The {doc}`Essential Foundations <../foundations/index>`
hub collects them; the {doc}`Quick Start <../get-started/index>` gives the
big picture without mathematics.

## Pages in this section

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} The CE Workflow
:link: ../foundations/concepts/ce_workflow
:link-type: doc

L1 · The whole picture in plain words, and a learning path from intuition to mathematics and code.
:::

:::{grid-item-card} Statistical Methods Behind CE
:link: ../foundations/concepts/calibration_methods
:link-type: doc

L2–L3 · How CE calibrates: Venn–Abers predictors and conformal predictive systems.
:::

:::{grid-item-card} Guarantees by Mode
:link: ../foundations/concepts/calibrated_interval_semantics
:link-type: doc

L3 · Canonical semantics of calibrated uncertainty, mode by mode.
:::

:::{grid-item-card} How to Read CE Explanations
:link: ../foundations/how-to/interpret_explanations
:link-type: doc

L2 · Read factual and alternative explanations: rule tables, uncertainty intervals and plots.
:::

:::{grid-item-card} Assumptions & Guarantees
:link: cross-mode-non-guarantees
:link-type: ref

L3 · What holds in every mode, and what CE does not guarantee.
:::

:::{grid-item-card} Essential Foundations
:link: ../foundations/index
:link-type: doc

Prerequisites; general statistics are not fully covered.
:::
::::
