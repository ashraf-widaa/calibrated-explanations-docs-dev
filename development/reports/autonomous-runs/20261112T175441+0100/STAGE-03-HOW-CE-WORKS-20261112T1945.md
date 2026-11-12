# Stage 03 — How CE Works

**Started:** 19:06 · **Completed:** 19:45
**Starting commit:** `29df0d5c`

## Audit

| ID | Problem | Evidence |
|---|---|---|
| HW-A | No Level 1 overview of the whole workflow; no learning path from intuition to mathematics and code | Section pages: landing, `foundations/index` (link list), semantics (terse Level 3 checklist), ADD-1 (683 lines, Level 2–3), `interpret_explanations` |
| HW-B | `probabilistic_regression.md` (46 lines): routing table and two code lines; no event forms, no reading guidance, no mistakes | Page |
| HW-C | `alternatives.md` (44 lines): lists filter names; does not teach what an alternative is or how to read it | Page |
| HW-D | Ensured, semi and related filter definitions conflict between sources | SR-09, SR-10 |

## Verified facts used (source, today)

| Fact | Source |
|---|---|
| `threshold` gives P(y ≤ t); a `(low, high)` pair gives P(low < y ≤ high); column 1 is the event, column 0 is 1 − p | `calibrated_explainer.py:1728–1731`; `interval_regressor.py:328`, `:472–482`; executed |
| `threshold` and `confidence_level` are mutually exclusive | docstring (`EXCLUSIVE_PARAM_GROUPS`) |
| Alternatives for classification: entropy tree depth 3, so at most 8 ranges | `utils/discretizers.py:229–231` |
| Factual weight = case probability − alternative probability for the other side | Executed: 0.286 − 0.476 = −0.190 |

## Changes

| File | Nature | Change |
|---|---|---|
| `docs/foundations/concepts/ce_workflow.md` | **New page** | Level 1 workflow (Mermaid: split → fit → calibrate → predict/explain); method per task (Venn-Abers, CPS, CPS + Venn-Abers) with one-sentence intuitions; how an explanation is built; what the guarantees rest on; **learning-path table**: 10 concepts × Level 1/2/3, Level 3 linking ADD-1 sections, papers, and source files and tests on the official repository (paths verified on `upstream/main`) |
| `docs/foundations/concepts/probabilistic_regression.md` | **Substantial rewrite** | Two questions about a numeric target; routing table kept; self-contained executed example (interval, P(y ≤ 150), interval event (100, 200), threshold explanation); reading notes; how CE computes it (two-half calibration, kept from the original, validity marked under review, SR-15); common-mistakes table |
| `docs/foundations/concepts/alternatives.md` | **Substantial rewrite** | What an alternative is and how CE builds it; executed example (case 2) with reading notes; link to the factual weight; scenario ranges do not carry the case's guarantee; filters listed with neutral wording (definitions under review); conjunction wording neutral; what alternatives do not tell you; CE paper reference |
| `docs/sections/how-ce-works.md`, `docs/index.md`, `docs/foundations/concepts/index.md`, `docs/appendices/rtd_tier_map.md` | Minor | Workflow card first; sidebar entry "The CE Workflow"; concept table row; tier map |
| `tests/docs/foundations/concepts/test_concept_examples.py` | New | Runs the python blocks of both concept pages; printed output must equal the page's text blocks |

## Validation

| Check | Result |
|---|---|
| Strict Beta build | 0 warnings |
| Docs tests | 276 passed |
| Links and anchors | 152 pages, 0 broken |
| Executed examples | Both pages' outputs match the page exactly |

## Remaining (author-dependent)

- Explanation construction beyond the default configuration (SR-14).
- Filter definitions (SR-09, SR-10).
- Validity of the two-step probabilistic regression construction (SR-15).
- Coverage wording for intervals (SR-02).

## Commit, push, publication

- **Commit:** see `RUN-STATUS.md`.
- **Pushed:** no (B-01).
