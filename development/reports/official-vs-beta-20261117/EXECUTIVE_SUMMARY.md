# Executive summary: CE official versus Beta documentation

**Recommendation:** use the current Beta candidate for CE-author and internship-supervisor review. It is an experimental feedback environment, not an official release recommendation. No documentation was edited or newly published for this comparison.

Official stable is a compact audience/task-oriented collection with shared technical foundations, API references and specialist guides. Beta reorganizes access around CE subjects and adds the explanations needed to connect those resources into a tutorial: what is predicted, what calibration changes, how factual rules compare substituted values, how weights relate to alternatives, and what their ranges do and do not establish.

The comparison uses verified deployed commits: official **`609d7b72`** (stable v1.0.2, [build 35281189](https://app.readthedocs.org/projects/calibrated-explanations/builds/35281189/)) and Beta **`2bc637bc`** ([build 35951339](https://app.readthedocs.org/projects/calibrated-explanations-beta/builds/35951339/)). [Open the Beta review](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/).

The direct Git comparison contains **24 added, 80 modified and no removed tracked page sources**: 120 → 144 pages, with 40 byte-identical. The additions span earlier enhancement stages, not only the final three corrections. Documentation source adds 6,702 lines and removes 1,144; growth is evidence of extent rather than a learning-outcome score. Separate inherited narrative API/code and development-version changes are disclosed in the full report.

Demonstrated improvements include complete same-case walkthroughs and interpreted outputs; corrected binary-bound indexing, estimator defaults, reject aliases and public API examples; clearer probability/target/weight distinctions; meaningful prose after all 19 instructional visual placements; and sidebar-led navigation without reader-facing tier matrices. All original page URLs remain. A/B/C orientation remains on the Quick Start hub, while conceptual pages present subject explanations. Original scientific comparison tables, examples, references and mathematical material remain available.

Fresh comparison validation passed **381 tests** (one wheel-install test excluded), a strict Sphinx build and 48 live desktop/mobile light/dark layout cases. All 278 requested official/Beta HTML URLs returned 200; no current Beta internal HTML targets were broken. These checks support technical reviewability, not statistical or legal approval or measured learner benefit. Mypy is unavailable; external links and layouts were sampled, not exhaustively certified.

Four targeted issues should guide feedback:

1. **Scientific validity language:** approve exact VA pair/merged/multiclass, CPS/Mondrian, event-probability, explanation-range, ensured-filter and reject-policy statements. Legal mappings require qualified review.
2. **Version wording:** one-sided v1.1 infinity behavior is described, but this development candidate still returns finite calibration extrema for open sides. Supply an implementing commit or qualify the future-version note.
3. **Incoming-link compatibility:** 24 official section IDs across 15 preserved pages are absent in Beta. Invisible aliases can preserve bookmarks without restoring old navigation tables.
4. **Two summary inconsistencies:** qualify Quick Start's universal prediction-range wording and distinguish shared input data from the different interval/event calibration constructions.

Expected benefits are reduced prerequisite guessing and a clearer connection between theory, calls, returned values and interpretation. These are editorial assessments; no user study or comprehension test was conducted.

For educational review, read [Why CE](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/why-ce.html), [CE by example](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/ce-by-example.html), [the workflow](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/ce_workflow.html), then [regression](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_regression.html) or [classification](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_classification.html). Authors should also examine [calibration methods](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/calibration_methods.html) and [interval semantics](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/calibrated_interval_semantics.html).

Feedback questions: Are the model-response and guarantee distinctions scientifically faithful? Can a new reader explain the connection between a factual weight and an alternative? Which statistical passages need a specific clarification? Do figures and following text make their quantities clear? Record exact passages and proposed corrections rather than request another broad redesign.

Full package: [Detailed report](OFFICIAL_VS_BETA_REPORT.md), [104-page change inventory and unchanged pages](PAGE_CHANGE_INVENTORY.md), [prioritized author questions](SCIENTIFIC_REVIEW_REGISTER.md), [source comparisons, metrics and validation evidence](CHANGE_EVIDENCE.md).
