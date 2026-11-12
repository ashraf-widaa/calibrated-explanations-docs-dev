# Stage 01 — Quick Start redesign

**Started:** 2026-11-12 18:00 · **Completed:** 18:40
**Starting branch / commit:** `docs-dev/autonomous-20261112` / `22629495`

## Inspected

- All Quick Start pages:
  - `get-started/index.md`, `ml-foundations.md`, `ce-tasks-and-modes.md`;
  - generated `quickstart_walkthrough.md` and its generator;
  - `quickstart_classification`, `quickstart_regression`, `quickstart_guarded`;
  - `quick_api`, `getting_started_60s`.
- Teaching-first specification documents `01`–`06` (`learning-reports/quickstart-walkthrough-audit/`).
- Source code for the explanation mechanism.

## Problems (verified)

| ID | Problem | Evidence |
|---|---|---|
| QS-A | The walkthrough is organised by API step (B1–B10), not by the reader's questions; calibration is introduced without motivation | Old generator cells B1–B10 |
| QS-B | Accuracy shown only after calibration; no raw vs calibrated comparison | Old B4 |
| QS-C | Intuitions stated as facts: "A larger calibration set gives tighter, more stable uncertainty estimates"; "[width] is wide when few calibration cases received a model score similar…" | Old B2, B4; spec `05` §2, §5 mark these as [I] |
| QS-D | Conjunction text uses wording the specification forbids pending authors: "the weight is their joint estimated effect", "two conditions together matter more than either one alone" | Old B7; spec Q1 |
| QS-E | No explanation of how a weight is computed; readers meet weights without a mechanism | Spec `05` §6; `04` §2–3 |
| QS-F | Venn–Abers guarantee not separated from the merged estimate's lack of one | Spec `05` §5 requirement B |
| QS-G | No page teaches what a model explanation is (local/global, attribution vs rules) | `ml-foundations` A1–A6 |
| QS-H | The index's learning path does not show where each core idea is taught | `get-started/index.md` |
| QS-I | Task quickstarts were not executed by any test | `tests/docs/get_started` |

## Decisions and changes

| Page | Nature | Change |
|---|---|---|
| `scripts/docs/build_quickstart_walkthrough.py` → `quickstart_walkthrough.md` + notebook | **Substantial rewrite** | Ten core sections from spec `05` rev. 2: (1) problem and case; (2) data and three roles; (3) train and evaluate (raw accuracy before calibration); (4) why calibration matters (raw extremes framed as a reason to check, not evidence); (5) Venn–Abers step list, Mermaid diagram, raw vs calibrated table, the pair's guarantee with three limits, the merged estimate without one, "not a confidence interval", Brier comparison (calibrated *worse* here, explained without causal claims); (6) how CE builds an explanation (scope sentence, five-step table with the default each step depends on); (7) factual explanation and plot (red/blue, grey band geometric only, weights do not sum: −0.069 vs 0.286); (8) alternatives linked to the weight (0.286 − 0.476 = −0.190); (9) can/cannot conclude; (10) recap. Optional A–C: regression, guarded, shaping (feature exclusion of the strongest feature; conjunctions with neutral wording). The generator now **stops if a number quoted in prose is missing from the executed outputs** |
| `docs/get-started/ml-foundations.md` | **New section A7** "What a model explanation is" | Local vs global; feature attribution (LIME, SHAP) vs rules; CE combines rules, weights and uncertainty; explanations describe the model, not causes. References: Ribeiro et al. (2016), Lundberg and Lee (2017), Löfström et al. (2024) |
| `docs/get-started/index.md` | Moderate | Learning-path descriptions updated (times 15/10/30 min); new "Where each idea is taught" table mapping the ten core ideas to sections |
| `tests/docs/get_started/test_walkthrough_content.py` | New | 5 tests: core section order; must-not-say list (spec Q1, Q2, Q4, Q7 and overclaims); qualified guarantee statements and review markers; calibration not presented as improving scores; generator prose guard present |
| `tests/docs/get_started/test_quickstart_examples_execute.py` | New | Executes every python block of the classification, regression and guarded quickstarts in page order |

## Scientific sources

- Vovk, Petej and Fedorova (2015), Proposition 1 (pair validity; merged estimate without exact guarantee), as cited in spec `05` and ADD-1;
- Brier (1950);
- scikit-learn `RandomForestClassifier.predict_proba` documentation (leaf proportions);
- CE source for mechanism defaults (verified today):
  - `sample_percentiles=[25, 50, 75]` (`calibrated_explainer.py:368`);
  - `condition_source` default `"prediction"`;
  - `binaryEntropy` for factual classification (`discretizer_config.py:53`).

## Validation

| Check | Result |
|---|---|
| Generator reproducibility | Before editing, a re-run produced byte-identical page and notebook |
| Regeneration | All values equal the specification's independently re-executed values: accuracy 0.947; extremes 41/114, all correct; Brier 0.0366 / 0.0445; case 2: 0.286 [0.167, 0.333]; top weight −0.190 [−0.314, −0.048]; sum −0.069 over 17 weights; alternative 0.476 [0.333, 0.600]; figure byte-identical |
| Strict Beta build | 0 warnings |
| Docs tests | 262 → 270 passed (8 new Stage 01 tests) |
| Links and anchors | 150 pages, 0 broken |
| Executed quickstarts | classification 5/5, regression 4/4, guarded 4/4 blocks run |

## Remaining

- `quick_api.md` and `getting_started_60s.md` are fragment-style method maps (not runnable by design); unchanged.
- Explanation construction beyond this configuration and conjunction reading wait on the authors (SR-14).

## Commit, push, publication

- **Commit:** see `RUN-STATUS.md`.
- **Pushed:** no (B-01).
