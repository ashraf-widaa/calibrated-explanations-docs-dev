# Final report — autonomous run 2 (20261112T175441+0100)

**Window:** 2026-11-12 17:54 → 18:47 (clock-read)
**Branch:** `docs-dev/autonomous-20261112`, 8 commits on top of `22629495`; linear, so publishing is a fast-forward
**Publication:** run 1 is live (verified). Run 2 is **not published**, because `git push` is denied to the agent (B-01). The PO publishes with `git push docs-dev docs-dev/autonomous-20261112:main`.

## 1. Stages

| Stage | Status | Commit |
|---|---|---|
| 00 Deployment verification | complete: run 1 live at `22629495` (build #35841238) | — |
| 01 Quick Start | complete | `66174c30` |
| 02 What & Why | complete | `29df0d5c` |
| 03 How CE Works | complete | `1372eb64` |
| 04 CE in Practice | complete | `34d61ebd` |
| 05 Foundations and references | complete | `5a48de93` |
| 06 Repository and research assets | complete | `2058fec1` |
| 07 Integration and reader journeys | complete | `3bb13216` |
| 08 Final validation | complete | final records commit |

## 2. Pages (details in `PAGE-INVENTORY.md`, `CONTENT-CHANGE-REGISTER.md`)

**Substantially rewritten (3):**
- **Quick Start walkthrough:** ten teaching sections that follow one case; the Venn-Abers pair and its limits; how CE builds a weight; Brier comparison; can/cannot conclude; generated, with a prose-number guard.
- **`probabilistic_regression`:** both regression questions, three threshold forms, executed examples, common mistakes.
- **`alternatives`:** what an alternative is, how it is built, reading it, its link to the weight, neutral filter wording.

**New (3 pages, 1 section):**
- **`what-is-ce`:** the problem, contribution, guarantees vs non-guarantees, fit, and a design-level comparison.
- **`ce_workflow`:** the whole workflow, plus a Level 1/2/3 learning path linking papers, ADD-1 and source files and tests.
- **`practitioner/evaluate_ce`:** reproducible set-up, empirical checks, common mistakes, failure cases.
- **ML basics §A7:** what a model explanation is.

**Reorganised:**
- section landing cards and the sidebar;
- the Quick Start idea-to-section map;
- the practitioner core path.

**Minor:**
- task-guide "Go further" sections;
- 4 glossary entries;
- the tier map.

**Deferred for authors:** `compare.md`; task-page epistemic and counterfactual wording; filter semantics; assumption wording; ADD-1 R1–R11; explanation construction (ADD-2).

**Unchanged:** 105 of 126 tracked pages.

## 3. Scientific improvements

- **Guarantees stated precisely and qualified:**
  - the validity of the Venn-Abers *pair* versus the merged estimate;
  - "not a confidence interval";
  - no individual-case guarantee;
  - calibration not presented as improving scores (a counter-example is shown).
- **Mechanism stated with its scope:** how a factual weight is computed in the default configuration, verified in source and by execution (0.286 − 0.476 = −0.190; weights sum to −0.069, not to the prediction).
- **Verified API semantics documented:** interval events `threshold=(low, high)`, column meaning, mutually exclusive parameters.
- **Evaluation methodology:** worded as empirical checks, not guarantees.
- **Claims register:** every new statement (C2-01 to C2-16) has a source and an evidence level.
- **Open author items:** SR-01 to SR-16 remain open and are marked on the pages.

## 4. Repository

- `scripts/docs/README.md`: regeneration procedure and validation sequence.
- `scripts/docs/check_internal_links.py`, with tests.
- No library code changed; the layout is unchanged (run 1 AD-01).

## 5. Validation (see `VALIDATION-SUMMARY.md`)

- Strict Beta and standard builds: 0 warnings.
- Docs tests: 262 → **289**.
- 0 broken links on 153 pages.
- Full suite: **5338 passed**, with the same 4 pre-existing environmental failures as in run 1.
- Executed-example checks on 7 pages.
- Responsive checks in light and dark.

## 6. Questions for the CE authors

Unchanged from run 1 (SR-01 to SR-16). Most important for the content written in this run:
- **SR-03:** the Venn-Abers guarantee object;
- **SR-02:** coverage wording;
- **SR-14:** explanation construction and the reading of conjunctions;
- **SR-09 and SR-10:** filter definitions;
- **SR-15:** the validity of probabilistic regression.

## 7. Record correction

The first three stage reports were initially future-dated. They were renamed to their actual commit times; see Stage 04.

## 8. Report locations

`development/reports/autonomous-runs/20261112T175441+0100/`:
- `RUN-PLAN`, `RUN-STATUS`;
- `STAGE-00` … `STAGE-08`;
- `PAGE-INVENTORY`, `CONTENT-CHANGE-REGISTER`, `SCIENTIFIC-CLAIMS-REGISTER`;
- `ENTRY-POINT-QUALITY-MATRIX`, `VALIDATION-SUMMARY`, `PUBLICATION-HISTORY`;
- this report.
