# Work-package reports (2026-11-13 run)

## WP-19 (new) + WP-7 + WP-8 (part) — Beta V2 corrections · `1e487429`

**Objective.** Correct verified scientific and technical errors found in the
official-vs-Beta audit; do not resolve open author questions.

| Item | Pages | Change | Source checked |
|---|---|---|---|
| A-01 one-sided intervals | `tasks/regression.md`, `foundations/concepts/calibration_methods.md` (2 places) | Version-aware: placeholder in v1.0.2, `-inf`/`inf` from v1.1.0 (#237); JSON strings; handle open side explicitly | official `371bd806` CHANGELOG + ADR-021 §2/§4; v1.0.2 tag |
| A-05 | `tasks/regression.md` | "confidence levels" → percentiles set target coverage, on average over cases | ADR-021; `calibration_methods` §3 |
| A-06/A-07 | `tasks/classification.md`, `tasks/probabilistic_regression.md` | No "counterfactuals", "necessary to flip", undefined epistemic/aleatoric claims; SR-07 marker; threshold = event y ≤ t, column 1 | claims register SR-07/SR-08; C2-11 |
| A-08 | `get-started/ce_first_agent_guide.md` | `ensure_coverage`/`ensure_order` (non-existent) → `explore_alternatives(...)` + `.ensured_explanations()`; lifecycle template names aligned; `X_query` defined; `DifficultyEstimator` fitted before use | `src/.../explanations/explanations.py:1989`; crepes `DifficultyEstimator.fit` signature; executed |
| A-09/A-10 | `contributor/plugin-contract.md`, `contributor/extending/plugin-advanced-contract.md` | `data_modalities` added to 8 `plugin_meta` examples; private `_EXPLANATION_PLUGINS` import and cleanup removed; package sketch labelled | `plugins/base.py:148–169` (ADR-033); executed |
| A-11 | `practitioner/advanced/explanation_retrieval.md` | Entry points `explain_factual(...)[0]` / `explore_alternatives(...)[0]`; schema keys verified | executed: keys `index, feature, condition, weight, uncertainty_interval, support` / `alternative_prediction` |
| A-12 | `foundations/how-to/configure_runtime.md` | States that `get_process_config_manager()` creates the singleton, so `init_process_config_manager()` must run first in a fresh process | executed (CalibratedError) |
| A-13 | `foundations/concepts/explanation_structures.md` | Schema sketch fenced as `text` | — |
| N-04 | `foundations/concepts/guarded_explanations.md` | `confidence` is not a confidence level for predictions | `GuardedOptions` |
| A-03 | `tutorials/index.md` | "outputs verified with CE 1.0.2 and 1.1.0-dev" | v1.0.2 worktree: 8/8 output-match tests, generator byte-identical |

**Reports.** Master audit (`01`), author-review sheet (`02`, N-01…N-05).
**Tests.** New `tests/docs/test_beta_v2_corrections.py` (17 tests). Both strict
builds 0 warnings; docs tests 333 passed; tutorials/guarded/Quick API 42
passed; 158 pages, 0 broken links. **Remaining.** Fragment pages (32) still
untested by design (D-13); N-01 compliance claims unchanged pending authors.

## WP-3 (V-6 only) + WP-18 (part) — Beta V3 visuals · `f06061b9`

**Objective.** Explain the three CE output types visually on the canonical page;
remove the deferred phone-table overflow.

| Item | Pages | Change | Evidence |
|---|---|---|---|
| V-6 | `foundations/concepts/calibrated_interval_semantics.md` (existing), new `docs/_static/figures/ce-output-types.svg` | Three panels (A classification bounds, B interval-regression interval with marginal-coverage wording, C P(y ≤ 150) with bounds + SR-15 marker); real outputs; links to walkthrough/tutorial (L2) and methods §2–§4 (L3); C1 links to it | Numbers asserted against published outputs (test) |
| WP-18 | `get-started/ce-tasks-and-modes.md` (3 tables), `get-started/ml-foundations.md` (1 table), `docs/_static/ce-docs.css` | `ce-table-compact` phone layout; short capability headers with soft hyphens and an explanatory line | Playwright 390 px: 0 scrolling tables on the three pages |

**Tests.** New `tests/docs/test_beta_v3_visual.py` (7). Both builds 0 warnings;
323 docs tests; 0 broken links. **Remaining.** 11 wide tables on non-Quick-Start
pages (calibration_methods 4, ce_workflow 2, others) for a later WP-18 pass.

## Integrated candidate · `944942cd`

Conflict-free merge of V3 into V2, built and tested in a separate worktree:
both builds 0 warnings; 369 tests; 158 pages, 0 broken links.
