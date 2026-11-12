# Scientific claims register — CE author review

**Purpose:** one place for every open scientific question raised during the Beta redesign. Each row merges the overlapping items from earlier reports. **No row is resolved by the documentation team.** Where docs text depends on a row, it is either left unchanged, marked "under review" on the page, or deferred.

**Source reports** (in `learning-reports/`):
- B1 = `2026-11-11_2051_L06-STEP-8-B1-SCIENTIFIC-DECISION-REGISTER.md` and `…_2051_…-B1-CE-AUTHOR-QUESTIONS.md`;
- ADD1 = `2026-11-11_2146_L06-STEP-8-ADD1-AUTHOR-REVIEW-PACKAGE.md` (R1–R11);
- GLOSS = `2026-11-12_0853_L06-GLOSSARY-CE-AUTHOR-REVIEW-NOTE.md` (Q-1–Q-7).

Evidence levels follow the master instruction §4: A primary, B implementation, C Beta, D literature, E editorial.

| ID | Question (merged) | Merged items | Best current evidence | Docs status | Blocks |
|---|---|---|---|---|---|
| SR-01 | **Assumption wording:** is the assumption "exchangeability" only, or "exchangeable **or distribution-matched**"? What does "distribution-matched" mean? | S1, R5, Q-6 (part) | ADR-021 states exchangeability only (B); 13 lines on 9 pages say "or distribution-matched" (C) | Unchanged; glossary *Exchangeability* marked under review | Semantics wording; glossary |
| SR-02 | **Coverage statement for CPS intervals:** "at least *h − l* on average over cases" (marginal); exact or lower bound with ties; per-category statement under Mondrian | Q-B1-2, R6, R7, R8, Q-6 (part) | Vovk et al. 2019/2022, Lei et al. 2018 (D); `crepes` endpoints (B); ADD-1 marked under review | ADD-1 and X2 keep "under review" markers; glossary leaves "coverage" out | B1-PKG-3; glossary coverage entries |
| SR-03 | **Venn–Abers guarantee object:** validity holds for the pair (p0, p1) and the probability selected by the true label; CE reports a merged *p* | Q-B1-1, R1, R3 | Vovk & Petej 2014; Vovk, Petej & Fedorova 2015 (D); `calibration/venn_abers.py` 388–405 (B) | ADD-1 under review | B1-PKG-3 |
| SR-04 | **Vocabulary:** "probability interval" (Venn–Abers) vs "prediction interval" (CPS); no "confidence interval" | Q-B1-3, R2, R9 | Standard terminology (D) | Unchanged; the glossary uses "uncertainty interval" as the CE umbrella term | B1-PKG-3; glossary |
| SR-05 | **"Conformal" umbrella:** may Venn–Abers be called conformal? | S4 | Venn–Abers is a Venn predictor; CPS is conformal (D) | `compare.md` unchanged | B1-PKG-4 |
| SR-06 | **Comparison claims:** "more stable rules" than LIME | Q-B1-4 | No repository evidence; CE-REG §5.2 says more stable run-to-run but less robust (A) | `compare.md` unchanged | B1-PKG-4 |
| SR-07 | **Epistemic vs aleatoric:** what do CE intervals and envelopes represent? | S3, Q-1 | Task pages claim both (C); the ensured playbook ties ensured explanations to epistemic uncertainty (C, paper title A); no decomposition in `src/` (B) | Task-page wording unchanged; glossary entries deferred | WP-06g; glossary |
| SR-08 | **"Counterfactual" and "flip":** may alternatives be called counterfactuals? Is "necessary to flip the prediction" acceptable? | S2, Q-2 | Interval semantics: "not causal guarantees" (C/A); paper title uses "Counterfactuals" (A) | Unchanged; glossary alias deferred | WP-06g; glossary |
| SR-09 | **Ensured filter rule:** "not wider" or "narrower" than the base interval? | Q-3 | `explanation.py` docstrings "no wider" (B); `explanations.py:1995` and the playbook "narrower" (B/C) | Glossary *Ensured explanation* under review | Glossary; `explanation_structures` |
| SR-10 | **Super/semi/counter/Pareto definitions,** including plain-regression semi | Q-4 | Three competing semi definitions (B/C) | Glossary entries deferred | Glossary; `explanation_structures` |
| SR-11 | **Name of the second regression mode** | Q-5 | "percentile or interval" (semantics), "conformal interval" (tasks page title) (C) | Glossary *Interval regression* "name under review" | Glossary; task page title |
| SR-12 | **House spelling:** Venn-Abers or Venn–Abers | Q-7 | Hyphen in code and original pages (B/C); en dash in ADD-1 and X2 | Both spellings present; glossary alias | Global copy-edit |
| SR-13 | **Multiclass bounds above 1** under default normalisation: intended default? | S7, R4 | `venn_abers.py` 232–359; observed 1.36 (B) | X2 explains it | WP-06g |
| SR-14 | **Explanation construction:** conjunction baseline, grey band, weight-interval reading; guarantees apply to predictions, not weights | S5, R11 | Löfström et al. 2025 §3.4 (A); code verified (B) | No canonical page (ADD-2 not written) | ADD-2 |
| SR-15 | **Thresholded regression validity:** Venn–Abers validity for the event {Y ≤ t} given the split calibration | R10 | `interval_regressor.py` 379–445 (B); ADR-021 §3 | ADD-1 under review | B1-PKG-3 |
| SR-16 | **Reject option:** which validity statements are canonical, which are experimental | S6 | Four pages; experimental parts (C) | Unchanged | B2 |

## Decided during this run (implementation facts, not author questions)

| ID | Fact | Evidence | Action |
|---|---|---|---|
| IF-01 | Plot colours (former S8). This is a rendering fact, not a scientific claim: documentation must describe what the library draws. | Verified in Stage 07 against `viz/matplotlib_adapter.py` | Corrected in Stage 07; the authors may still change the palette in code |
