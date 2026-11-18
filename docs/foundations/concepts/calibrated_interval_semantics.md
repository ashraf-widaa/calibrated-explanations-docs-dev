# Calibrated interval semantics

This page is the semantics source for user-facing documentation.

Read an output description separately from a statistical guarantee. The
exact guarantee wording for the Venn–Abers pair and its merged probability
(SR-03), CPS coverage (SR-02), and threshold-event probabilities (SR-15)
remains under review by the CE authors. The
{doc}`methods page <calibration_methods>` distinguishes the cited results
from CE's implementation and from illustrative examples.

New to these ideas? The Quick Start introduces each mode in plain language in
{doc}`../../get-started/ce-tasks-and-modes` and shows them in use in the
{doc}`../../get-started/quickstart_walkthrough`.

## Scope

Calibrated Explanations has three distinct semantics modes:

1. Classification with Venn-Abers probability intervals.
2. Percentile/interval regression without thresholds using CPS percentile intervals.
3. Probabilistic or thresholded regression using CPS with Venn-Abers event probabilities.

Do not merge these into one guarantee statement.

(ce-output-types)=

### The three output types at a glance

Each mode answers a different question, so its output has a different shape and
a different meaning. The figure shows one real CE output of each type.

```{raw} html
<figure class="ce-figure ce-figure--compact">
  <a href="../../_static/figures/ce-output-types.svg" title="Open the figure at full size">
    <img src="../../_static/figures/ce-output-types.svg" width="400" height="714" alt="Three panels. A, classification: walkthrough case 2 has a calibrated probability of benign of 0.286 with lower and upper probability 0.167 and 0.333, so the predicted class is malignant; these are bounds of a probability, not a confidence interval. B, interval regression: regression tutorial case 0 has a prediction of 273.4 with a 5th to 95th percentile prediction interval from 186.5 to 409.2, and the actual value 321 lies inside; about 90 percent of such intervals contain the true value on average over cases, not for every case. C, probabilistic regression: for the same case, the calibrated probability that the outcome is at most 150 is 0.077 with bounds 0.000 and 0.083; this is a probability for an event, not an interval for the value.">
  </a>
  <figcaption>CE outputs from the Python walkthrough (A) and the regression tutorial (B, C). The bounds in A and C bound a probability; the interval in B bounds the value itself. Each mode's guarantee is stated below.</figcaption>
</figure>
```

Compare the horizontal scales before comparing the bars. Panel A shows a
probability of *benign*, with the estimate marked between two Venn–Abers
values. Panel B uses target units: the estimate 273.4 and observed value 321
are separate markers, and the 5th–95th percentile interval extends from
186.5 to 409.2. That observation lies inside this particular interval; one
case cannot establish coverage. Panel C returns to a probability scale for
the event `y <= 150`, rather than locating the target value itself. Its
estimate 0.077 and bounds are therefore not directly comparable with the
values in B. The method-specific qualifications below govern these outputs;
the diagram does not add a guarantee for an individual case.

- **A, classification:** see the {doc}`Python walkthrough <../../get-started/quickstart_walkthrough>`
  (section 5) and, for the method, {doc}`calibration_methods` (section 2).
- **B and C, regression:** see the {doc}`regression tutorial <../../get-started/quickstart_regression>`
  and {doc}`calibration_methods` (sections 3–4).

## Mode 1: Classification (Venn-Abers)

### Calibration prerequisites
- Fit on a proper training split.
- Calibrate on a held-out calibration split.

### Mode-specific guarantees
- CE returns a merged class probability and the two Venn–Abers values.
  The exact calibration property of the pair must not be transferred to the
  merged probability. These bounds are not a conventional confidence interval
  for an individual case's unknown probability. *Wording under author review
  (SR-03); see {doc}`calibration_methods`, section 2.*
- In multiclass classification, the default normalization also rescales the
  bounds; an upper bound can exceed 1. These rescaled values must not be read
  as unchanged binary Venn–Abers bounds. See
  {doc}`../../get-started/ce-tasks-and-modes` for the normalization choices.

### Assumptions
- Calibration and new cases must satisfy the method's exchangeability
  assumption, with the predictive model fixed before calibration. Older CE
  wording also says "distribution-matched"; whether that wording is sufficient
  is under author review (SR-01).

### Explicit non-guarantees
- No guarantee under distribution drift or regime shift.
- No guarantee that class probability intervals transfer unchanged across domains.

### Explanation-envelope and feature-level limits
- Rule-level and feature-level intervals are explanation artifacts tied to calibrated
  perturbation behavior.
- They are not causal guarantees.

## Mode 2: Percentile or interval regression (CPS)

### Calibration prerequisites
- Fit on a proper training split.
- Calibrate with CPS on a held-out calibration split.

### Mode-specific guarantees
- CE returns a CPS median and prediction interval for the requested percentiles.
  Coverage concerns the target value over calibration/test draws, not the
  correctness of each point prediction. The precise finite-sample statement,
  endpoint conventions, ties, and subgroup conditions are under author review
  (SR-02); see {doc}`calibration_methods`, section 3.

### Assumptions
- Exchangeability of calibration and new cases, with the model and any fitted
  difficulty estimator fixed before calibration. The alternative
  "distribution-matched" wording remains under review (SR-01).

### Explicit non-guarantees
- No guarantee that requested percentiles remain calibrated after drift.
- No guarantee of fixed interval width across subpopulations.

### Explanation-envelope and feature-level limits
- Feature-level interval effects describe model behavior under perturbation.
- They do not guarantee intervention outcomes in the real world.

## Mode 3: Probabilistic or thresholded regression (CPS + Venn-Abers)

### Calibration prerequisites
- Fit regression model on a proper training split.
- Build threshold event probabilities through CPS outputs calibrated with Venn-Abers.

### Mode-specific guarantees
- Returns event probabilities and lower/upper values from CPS scores followed
  by Venn–Abers calibration, for queries such as `P(y <= t)` or interval events.
  This is a range for an event probability, not a prediction interval for
  the numeric target. The exact validity statement is under author review
  (SR-15); the pair/merged-probability distinction also applies.

### Assumptions
- Exchangeability and the calibration/scoring construction described in
  {doc}`calibration_methods`, section 4. The alternative
  "distribution-matched" wording remains under review (SR-01).

### Explicit non-guarantees
- No guarantee for threshold probability calibration under drift.
- No guarantee that threshold semantics imply causal actionability.

### Explanation-envelope and feature-level limits
- Feature-level probability shifts and envelopes describe model response patterns.
- They are not guarantees of controlled intervention effects.

(cross-mode-non-guarantees)=

## Cross-mode non-guarantees

- Calibration guarantees are conditional on calibration assumptions.
- No unconditional guarantee under dataset shift, temporal drift, or adversarial change.
- Explanation-level intervals should not be promoted as formal per-feature coverage
  guarantees unless explicitly proven for that claim.

(open-author-questions)=

## Open questions for the CE authors

The statements on this page are deliberately limited where the exact
scientific wording has not yet been confirmed by the CE authors. The open
items are collected here so that they stay visible; none of them is resolved
by this documentation. Pages that touch an item carry an inline *under review*
note.

| Item | What is open | Where it appears |
|---|---|---|
| SR-01 | Which exchangeability, data-use and fitted-component conditions apply to each CE path, and whether any distribution-match alternative is justified | Assumptions on this page; {doc}`calibration_methods`; {doc}`../../what-is-ce` |
| SR-02 | The exact finite-sample statement for CPS intervals (ties, endpoints, one-sided requests, difficulty estimates) and the conditions for per-group (Mondrian) coverage | Mode 2; {doc}`calibration_methods`; {doc}`../../practitioner/evaluate_ce` |
| SR-03 / SR-13 | Validity wording for the Venn–Abers pair versus the merged probability, rescaled multiclass bounds (upper bounds above 1) and selection of the predicted class | Mode 1; {doc}`../../get-started/ce-tasks-and-modes`; {doc}`../../tasks/classification` |
| SR-15 | The validity statement for threshold-event probabilities built from CPS scores and Venn–Abers, including their merged output | Mode 3; {doc}`probabilistic_regression`; {doc}`../../practitioner/evaluate_ce` |
| SR-08 / SR-10 / SR-14 | What a feature-weight range should be called and which inferences it supports (including zero crossing and conjunctions) | Explanation-envelope limits; {doc}`../how-to/interpret_explanations`; {doc}`alternatives` |
| SR-07 / SR-09 | The interpretation of ensured filtering (no claim that it reduces an identified uncertainty component) | {doc}`../../practitioner/playbooks/ensured-explanations`; {doc}`../../practitioner/playbooks/index` |
| SR-16 | Which accepted-case error and reject-rate statements hold for reject policies | {doc}`../../practitioner/advanced/reject-policy` |
| SR-06 | Whether any evidence-backed stability comparison with other explainers can be stated | {doc}`../../compare` |
| Legal | The mapping of CE records to EU AI Act and data or liability obligations; these pages are not evidence of compliance | {doc}`../../practitioner/playbooks/eu-ai-act-compliance`; {doc}`../../practitioner/playbooks/eu-data-liability-compliance` |
| Versions | One-sided interval endpoints differ between the Beta source and the official source although both identify as `1.1.0-dev` | {doc}`../../tasks/regression` |

The maintained registers are
`development/reports/official-vs-beta-20261117/SCIENTIFIC_REVIEW_REGISTER.md`
and `development/reports/docs-focused-20261116/author-review.md` (maintainer
documents, not part of the published site).

## Further reading

- {doc}`How CE Calibrates <calibration_methods>`: how CE computes the probabilities and
  intervals described on this page (methods page; some wording is under author review).
- Venn–Abers predictors: Vovk, V., and Petej, I. (2014). Venn-Abers predictors.
  *Proceedings of the 30th Conference on Uncertainty in Artificial Intelligence (UAI 2014)*.
  [arXiv:1211.0025](https://arxiv.org/abs/1211.0025).
- Inductive Venn–Abers predictors: Vovk, V., Petej, I., and Fedorova, V. (2015).
  Large-scale probabilistic predictors with and without guarantees of validity.
  *Advances in Neural Information Processing Systems 28*.
  [arXiv:1511.00213](https://arxiv.org/abs/1511.00213).
- Conformal predictive systems: Vovk, V., Shen, J., Manokhin, V., and Xie, M. (2019).
  Nonparametric predictive distributions based on conformal prediction.
  *Machine Learning*, 108, 445–474.
  [doi:10.1007/s10994-018-5755-8](https://doi.org/10.1007/s10994-018-5755-8).
- Split conformal predictive systems: Vovk, V., Petej, I., Nouretdinov, I., Manokhin, V.,
  and Gammerman, A. (2020). Computationally efficient versions of conformal predictive
  distributions. *Neurocomputing*, 397, 292–308.
  [doi:10.1016/j.neucom.2019.10.110](https://doi.org/10.1016/j.neucom.2019.10.110).
- Conformal prediction framework: Vovk, V., Gammerman, A., and Shafer, G. (2022).
  *Algorithmic Learning in a Random World* (2nd ed.). Springer.
  [doi:10.1007/978-3-031-06649-8](https://doi.org/10.1007/978-3-031-06649-8).
- Calibrated Explanations publications: {doc}`../../citing`.

## Related standards and ADRs

- `development/standards/STD-004-documentation-audience-standard.md` (maintainer-only docs set)
- `development/standards/STD-002-code-documentation-standard.md` (maintainer-only docs set)
- `development/adrs/ADR-021-calibrated-interval-semantics.md` (maintainer-only docs set)
- `development/adrs/ADR-012-documentation-and-gallery-build-policy.md` (maintainer-only docs set)
- `development/adrs/ADR-026-explanation-plugin-semantics.md` (maintainer-only docs set)
