# 03 — WP-13: CE: What & Why

**Status:** COMPLETED, except V-2, which is BLOCKED because its planned home is
the unapproved new page `explainable-ai` (D-25).

## 1. Changes

| File | Change |
|---|---|
| `docs/sections/what-and-why.md` | Two-paragraph intro ("The problem", "CE's answer"); **"Read in this order"** table answering the seven questions of the master prompt in sequence, each with a plain-words target and a "go deeper" link; Quick Start pointers for newcomers; cards reordered as a progression; card "Trustworthy AI" → **"Regulation Context (EU AI Act)"**, described as a practitioner guide that is not evidence of compliance and whose compliance wording is under review |
| `docs/index.md` (What & Why group) | Sidebar order What CE Is → The Explainability Gap → Regulation Context (EU AI Act); relabelled; URLs unchanged |
| `docs/what-is-ce.md` | Labels for each step (`wic-problem`, `wic-calibration`, `wic-adds`, `wic-guarantees`, `wic-fit`, `wic-compare`). New section **"Calibration is not accuracy"**. Nuance on attribution methods (they answer a different question; not "wrong"). **Small example** with walkthrough case 2 (raw 0.16 → calibrated 0.286 [0.167, 0.333]). "A range is not a statement that a prediction is correct". The fit list labelled as "not a list of demonstrated benefits", with links to the evaluations and to `evaluate_ce`. Both wide tables in the phone layout. Reference Guo et al. (2017) added |
| `docs/get-started/ml-foundations.md` | Label `ml-a1` only (no text change) |
| `tests/docs/test_what_and_why_progression.py` (new, 8 tests) | Order of the seven steps and their targets; card order; relabel and no compliance claim; calibration-vs-accuracy wording and citation; example numbers traced to the walkthrough output; fit list not presented as benefits; phone tables |

## 2. Conceptual progression (master prompt §6)

| # | Question | Where it is answered | L-level |
|---|---|---|---|
| 1 | What does a model produce? | `ml-foundations` A1 (existing) | L1 |
| 2 | Why is an explanation not enough by itself? | `what-is-ce` § The problem (+ nuance) | L1 |
| 3 | What is calibration; how does it differ from accuracy? | `what-is-ce` § Calibration is not accuracy (**new**) | L1 → `calibration_methods` L3 |
| 4–5 | What problem does CE address; what does it produce? | `what-is-ce` § What CE adds (+ **example**) → `ce-by-example` | L1 → L2 |
| 6 | When might CE be useful? | `what-is-ce` § When CE is a good fit (+ potential vs demonstrated) | L1 → `evaluate_ce` L2 |
| 7 | What does CE not guarantee? | `what-is-ce` § What CE guarantees… (+ range ≠ correctness) | L1 → semantics L3 |

## 3. Scientific review notes

- **Calibration vs accuracy.** These are standard definitions. "Accurate but miscalibrated" cites Guo et al. (2017, PMLR 70). "Calibrated but of little use" (the base-rate predictor) is an elementary consequence of the definition. Wording is "not designed to make a model more accurate", because Venn–Abers can change a predicted class near 0.5. Confidence: high. No author approval needed.
- **Example numbers.** These come from the walkthrough's executed output (`Raw P(benign), cases 0-4: [0. 1. 0.16 0.21 0.]`; 0.286 [0.167, 0.333]), and a test ties them together.
- **Range wording.** One draft sentence interpreted narrow ranges as stronger data support. It was removed before commit because it belongs to SR-07, and only the non-guarantee was kept.
- **Unchanged.** The SR-01 *under review* marker on the assumption wording is unchanged.

## 4. Cross-links added

- The landing links to A1, `compare`, `calibration_methods`, `ce-by-example`, `evaluate_ce`, the semantics page, the regulation playbook and the Quick Start.
- `what-is-ce` now links `evaluate_ce` and `calibration_methods` from the body.
