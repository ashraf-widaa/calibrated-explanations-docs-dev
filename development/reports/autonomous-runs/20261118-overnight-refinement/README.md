# Overnight refinement — 2026-11-18

## Scope and baseline

- Branch `docs/overnight-refinement-20261118`, created from `beta/integration`
  at `7394c330` (validated in Step 6, published as RTD `beta-integration`).
- `beta/integration` itself is unchanged. Official CE resources were not touched.
- No CE source code, scientific equations, figures, generated walkthrough or
  notebook files changed. The four main documentation sections, the sidebar
  hierarchy, page URLs and existing anchors are unchanged.

## Changes

| Commit | Page or file | Original issue | Improvement |
|---|---|---|---|
| `008a3653` | `get-started/quick_api.md` | No install step on the copy-and-run page; "What comes back?" said predictions come with lower and upper values, although bounds are returned only with `uq_interval=True` (Batch 1 semantics). | Install row (base package, Python 3.10+, `viz` extra for plots); return row separates requested prediction bounds from explanation weight ranges. |
| `008a3653` | `get-started/index.md` (Quick Start) | The executable route listed the walkthrough first; the copy-and-run minimal example was only "lists the main calls". | Points beginners to the Quick API minimal example first, then the walkthrough and task tutorials; mentions the `viz` extra. The hub stays code-free (existing decision and test). |
| `eac672ea` | `quickstart_classification.md`, `quickstart_guarded.md`, `apply-to-your-data.md`, `installation.md` | Pages that call `.plot()` installed only the base package; without Matplotlib, plotting raises a `ConfigurationError` naming the `viz` extra (verified in `plotting.py`). | Install lines use `"calibrated-explanations[viz]"`; Installation explains why. |
| `eac672ea` | `why-ce.md`, `quickstart_classification.md`, `tasks/classification.md` | Ranges described as showing "how firmly the calibration data support" a value, which implies a sample-size reading Batch 1 removed elsewhere. | Prediction bounds: calibrated behaviour over many cases. Weight ranges: derived from substituted predictions, no formal guarantee. A range crossing 0 does not establish a direction. |
| `eac672ea` | `apply-to-your-data.md` | "With very few cases the ranges become wide" and "Use more calibration data" implied that more data narrows every range. | More data tends to help on average but does not narrow every case. |
| `eac672ea` | `quickstart_classification.md` | The plot reading did not state that two kinds of range appear. | One paragraph distinguishes prediction bounds from derived weight ranges. |
| `88b62bc5` | `practitioner/evaluate_ce.md` | No threshold-event check and no subgroup check (Batch 3 audit, items C and D). | Executed threshold-event check (observed share, mean prediction, Brier score, range width, reliability table) and executed per-group coverage check, both read as empirical, with SR-15 and SR-02 kept open. Added as subsections, so existing anchors are unchanged. |
| `43a9b75f` | `tutorials/index.md` | No reading order between tutorials. | Suggested order and a `viz` reminder; more specific pointer to the evaluation checks. |
| `43a9b75f` | `tests/docs/test_overnight_refinement_20261118.py` | — | Guards for the above (7 tests). |

Correction to the Batch 3 audit: `evaluate_ce.md` was already executed and
output-checked by `tests/docs/foundations/concepts/test_concept_examples.py`;
the new examples are therefore verified by that existing test.

## Validation (local, before publication)

| Check | Result |
|---|---|
| `tests/docs` | 374 passed (367 existing + 7 new), 0 failed, 0 skipped; one known `CE_DOCS_BETA` configuration warning |
| `tests/scripts/test_check_parameter_naming.py` | 5 passed |
| `tests/integration/test_doc_examples_smoke.py` | 16 passed, 1 failed: the official wheel-packaging test needs the `build` package, which is not installed (pre-existing, unchanged since Step 6) |
| Strict Sphinx, Beta and standard (`-W --keep-going -E`, `nbsphinx_execute=never`) | Both exit 0, 0 warnings, 158 pages each |
| Internal links | 158 pages, 0 broken, both variants |
| Assets and alt text | 2,510 / 2,352 local references resolve; 0 images without alt text |
| Anchors versus the `beta/integration` build | 0 pages or ids lost |

Environment: Python 3.13.7 with the pinned documentation versions (Sphinx
7.4.7, MyST 3.0.1, nbsphinx 0.9.8, numpydoc 1.10.0); CE imported from this
worktree (`1.1.0.dev0`). Not run: RTD's Python 3.11 locally, `make
local-checks-pr` (mypy and ruff unavailable), the wheel-packaging test.

## Scientific review

No open scientific item was settled. New wording reuses Batch 1 semantics.
Items still requiring CE author decisions: SR-01, SR-02 (including what
Mondrian calibration guarantees per group), SR-03/13, SR-15 (including the
validity of threshold-event probabilities checked empirically above),
SR-07/09 (including the official "Reduce epistemic uncertainty" line in
`practitioner/playbooks/index.md`), SR-08/10/14, SR-16, legal pages, and the
official wordings `Confidence:` (`tasks/probabilistic_regression.md`),
"reduce confidence in the prediction" and "change the prediction to a
different class" (`tasks/classification.md`).
