# CE documentation — author and supervisor review

This is the experimental **Beta review environment**, not official CE
documentation or an official release.

**[Open the Beta preview](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/)**  
Branch: `beta/author-review-20261117`  
Verified deployed commit: `2bc637bc9b55febf77215783e2cbf3ab4288a520`  
[RTD build 35951339](https://app.readthedocs.org/projects/calibrated-explanations-beta/builds/35951339/):
successful, 79 seconds, zero Sphinx warnings or errors.

## Improvements in this candidate

- The regression tutorial explicitly distinguishes the threshold-event query
  from the following target-value explanation and its target-unit weights.
- What & Why qualifies requested prediction uncertainty and distinguishes it
  from explanation-weight ranges and their method-specific interpretation.
- CE by Example opens its factual plot at full size. On mobile, version
  selection is in the existing sidebar, so the floating version widget no
  longer obscures the tutorial once RTD version data is available.

The continuous tutorial style, sidebar hierarchy, scientific examples,
figures and immediate explanatory paragraphs are preserved.

## Recommended review pages

1. [CE: What & Why](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/sections/what-and-why.html):
   motivation, calibration and uncertainty wording.
2. [CE by Example](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/ce-by-example.html):
   the worked prediction, factual rule, alternative, plot explanation and
   full-size image access.
3. [Regression tutorial, section 5](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_regression.html#5-explain-a-prediction):
   the transition from event probabilities to target-value weights.
4. [The CE workflow](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/ce_workflow.html)
   and [calibration methods](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/calibration_methods.html):
   connections between the practical example and statistical construction.
5. [Canonical semantics](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/calibrated_interval_semantics.html):
   assumptions, limits and open author-review qualifications.

## Feedback requested

- Are Venn–Abers pair/merged outputs, CPS target intervals, threshold-event
  probabilities and explanation ranges distinguished scientifically correctly?
- Are the assumptions and exact guarantee qualifications adequate? In
  particular, please review multiclass bounds, the threshold-event construction
  and the meaning of derived feature-weight ranges.
- Can a newcomer connect prediction → substituted values → factual weight →
  alternative prediction without inferring causality?
- Does the prose read as a clear academic tutorial? Please identify any
  unexplained term, abrupt transition or unclear figure by page and section.

The [existing scientific-review register](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/development/reports/docs-focused-20261116/author-review.md)
remains open; successful publication is not scientific or legal acceptance.

## Evidence and known limitations

- All 158 published articles match the validated local candidate; 2,203
  internal page/anchor targets resolve. Scientific tables, examples,
  references and mathematical content remain intact.
- Live verification covered 100 desktop/mobile/theme cases and 10
  selector/image interactions. All 19 instructional figures retain their
  explanatory text. Prepublication evidence includes 381 passing tests and
  both strict Sphinx builds.
- Small plot labels still benefit from the full-size view.
- Version selection relies on RTD's live addon data. One automated 768px
  dark-mode load did not receive that event within 15 seconds; reloading
  resolved it. The standard RTD widget remains the fallback when data is
  unavailable. RTD hosting ads may also appear.
- The local quick profile remains incomplete because mypy is unavailable.

Official CE, previous Beta candidates and Beta latest are unchanged.
This handoff is hosted separately so the published candidate stays at its
authorized commit.
