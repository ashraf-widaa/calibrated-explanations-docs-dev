# Stage 04 — Shared scientific foundations

**Started:** 2026-11-12 10:31 · **Completed:** 2026-11-12 10:45
**Starting branch / commit:** `docs-dev/autonomous-20261112` / `d418d106`

## Objective

Make canonical ownership explicit, collect every open scientific question in one register, and connect the glossary to the pages where readers need it, without resolving disputed claims.

## Inspected

- Glossary (G-P1/G-P2) and its tests.
- G-P3 cross-link proposal (`learning-reports/2026-11-12_0853_…`).
- B1 decision register and author questions (Step 8).
- ADD-1 author package (R1–R11).
- Glossary author note (Q-1–Q-7).
- `api/calibrated_explainer.md` rendering (no autodoc output; the defect is fixed in Stage 09).

## Decisions

1. **One scientific claims register.** `SCIENTIFIC-CLAIMS-REGISTER.md` merges S1–S8, Q-B1-1–4, R1–R11 and Q-1–Q-7 into 16 rows (SR-01–SR-16), each with merged IDs, the best evidence and its level (A–E), the docs status and what it blocks. S8 (plot colours) is reclassified as an implementation fact (IF-01), handled in Stage 07.
2. **Canonical ownership unchanged and confirmed:**
   - semantics: `calibrated_interval_semantics`;
   - methods: ADD-1 `calibration_methods`;
   - reading explanations: `interpret_explanations`;
   - parameters: `parameter-reference`;
   - short definitions: the glossary;
   - signatures: the `_autosummary` pages.
3. **R2: retarget weak glossary links.** 12 software entries now point to the API pages that render signatures: `WrapCalibratedExplainer` (8), `CalibratedExplainer` (3), `FactualExplanation` (1), plus `AlternativeExplanations`, 12 in total.
4. **G-P3: one glossary link on each of 11 landing points** (X1–X11, as proposed in `…_0853_…`). None in body text; none on the semantics page. The loop guard is enforced by a test.

## Files changed

| File | Change |
|---|---|
| `docs/glossary/software.md` | 12 retargeted API links |
| `docs/foundations/concepts/index.md` | X1: Scientific glossary sentence after the intro |
| `docs/sections/how-ce-works.md` | X2 |
| `docs/api/index.md` | X3: Software glossary sentence |
| `docs/sections/software-integration.md`, `docs/sections/development-integration.md` | X4, X5 |
| `docs/foundations/concepts/parameter-reference.md` | X6: Glossary first in "Cross-references" |
| `docs/foundations/how-to/interpret_explanations.md` | X7: "More terms" item inside the Terminology box |
| `docs/get-started/index.md` | X8: Glossary in "Setup and help" |
| `docs/foundations/concepts/terminology.md` | X9: Further Reading |
| `docs/foundations/concepts/terminology_thresholded_vs_probabilistic_regression.md` | X10: `{term}` link to *Probabilistic regression* |
| `docs/get-started/ce_first_agent_guide.md` | X11: the recommendation now points to the software glossary |
| `tests/docs/glossary/test_glossary.py` | Allows `_autosummary/` targets (`.rst`); 13 new tests: one link per landing page, none on the semantics page, no self-loop for any `{term}` link |
| `SCIENTIFIC-CLAIMS-REGISTER.md` | New |

No scientific claim was changed. Every disputed glossary entry keeps its marker or stays deferred.

## Validation

| Gate | Result |
|---|---|
| Strict Beta build | exit 0, 0 warnings |
| `pytest tests/docs …` | 237 passed (224 + 13 new) |
| Links and anchors | 150 pages, 0 broken; page set unchanged |
| Rendered checks | X7 link renders inside the admonition; software glossary has 25 `_autosummary` links |

## Remaining issues

- The five class entries still point to `api/calibrated_explainer`, whose prose is accurate; that page's signatures are repaired in Stage 09.
- SR-01 to SR-16 await the CE authors.

## Commit, push, publication

- **Commit:** see `RUN-STATUS.md`.
- **Pushed:** no (B-01).
- **Published:** no.
