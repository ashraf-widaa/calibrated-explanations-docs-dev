# ML and statistical foundations

<span id="essential-foundations"></span>

This page collects the concepts, guides and references you need to
understand and use calibrated explanations, ordered from first steps to
advanced material.

## Orientation and beginner foundations

CE uses features to describe a case and a trained model to produce its
prediction. Training, calibration and evaluation data have different roles;
{doc}`machine-learning essentials <../get-started/ml-foundations>` introduces
them. The {doc}`glossary <../glossary/index>` supplies short definitions.

## Practical understanding and interpretation

A factual explanation compares model responses associated with a condition
that holds for the case. An alternative reports a prediction under a
different condition. The {doc}`interpretation guide <how-to/interpret_explanations>`
connects these quantities to returned records and plots. Guarded explanations
add filtering of candidate feature intervals; they do not turn model-response
comparisons into causal evidence.

## Scientific and statistical foundations

The statistical meaning of an output depends on its calibration construction.
{doc}`concepts/calibration_methods` develops Venn–Abers predictors and
conformal predictive systems. Prediction bounds, target intervals and
explanation-weight ranges must be distinguished; their assumptions and open
qualifications are collected in {doc}`concepts/calibrated_interval_semantics`.

## Software architecture and reference

The calibrated runtime coordinates prediction and explanation operations.
The {doc}`architecture <concepts/architecture>` describes those
responsibilities and their extension points. The sidebar provides the
parameter, data-structure and API references for inspecting a specific
operation.

## Project governance (for maintainers)

Release, testing and documentation policies are kept separate from the
scientific explanations: see {doc}`governance/index`, also listed under
*Project* in the sidebar.

```{toctree}
:hidden:
:maxdepth: 1

Machine-Learning Essentials <../get-started/ml-foundations>
More Concepts <concepts/index>
```
