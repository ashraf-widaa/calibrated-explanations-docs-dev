# Scientific verification — Quick Start v3

Evidence levels: **A** CE papers or official CE pages · **B** source code,
tests or executed output · **C** official docs · **D** Beta pages · **E**
external literature · **F** editorial. Open author questions SR-01 to SR-16
(see `../20261112T175441+0100/SCIENTIFIC-CLAIMS-REGISTER.md`) are **not
resolved** here.

| ID | Page | Statement | Evidence | Status |
|---|---|---|---|---|
| Q3-01 | `why-ce`, landing | A pre-trained model can be wrapped and calibrated directly; same output 0.286 [0.167, 0.333] as training through CE | Executed (B) | Verified |
| Q3-02 | `why-ce`, C1, C5 | Classifiers need `predict_proba`; without it calibration raises `ConfigurationError` (LinearSVC) | Executed (B) | Verified |
| Q3-03 | `why-ce` | Running-example numbers 0.29 [0.17, 0.33], rule `worst concave points > 0.14`, weight ≈ −0.19, alternative ≈ 0.48 | Walkthrough output (B), C2-05 | Verified |
| Q3-04 | `why-ce` | Exchangeability assumption; statements over many cases; mode-specific guarantees | `calibrated_interval_semantics` (A/C) | Verified; assumption wording is SR-01 |
| Q3-05 | C1 | Coverage "on average over cases (marginal coverage)" | PO-reviewed X2 wording | **Under review (SR-02); marked on the page** |
| Q3-06 | C1 | Mode → calibration method: Venn-Abers; CPS; CPS then Venn-Abers | Source (B); CE papers (A) | Verified; validity of the two-half construction is SR-15 (not claimed) |
| Q3-07 | C2 | Default multiclass bounds are rescaled and can exceed 1; `normalization="simplex"` keeps calibrated bounds | C1 limitation 1 (D), executed (B: 1.45 default, 1.00 simplex; alternative bound 1.10) | Verified as behaviour; interpretation is SR-13 |
| Q3-08 | C2, C3, C5 | Weight sign: positive weight = condition raises the calibrated prediction; other side ≈ that much lower | C2-05 (B) | Verified |
| Q3-09 | C3 | Default interval = 5th–95th percentile | `api/config.py:44` (B) | Verified |
| Q3-10 | C3 | Threshold event is column 1, P(y ≤ t) | C2-11 (B) | Verified |
| Q3-11 | C4 | Guarded audit numbers (945 / 743 / 202 / 101; one case with all candidates removed and a `UserWarning`) | Executed (B) | Verified |
| Q3-12 | C4 | Guard checks representative values, not whole intervals; does not detect an out-of-distribution case itself | `guarded_explanations` limitations (C), ADR-032 | Verified |
| Q3-13 | C5 | A factual explanation can contain no rules when no single-feature change moves the calibrated probability (15 of 114 test cases) | `explanation.py:2011–2045` (B); executed (B) | Verified |
| Q3-14 | C5 | Indexing explanations with a NumPy integer raises `ValidationError` | Executed (B) | Verified |
| Q3-15 | C5 | Pipeline fitted on a DataFrame warns about feature names because CE passes arrays | Executed (B) | Verified |
| Q3-16 | C5 | Brier score 0.024 (model) vs 0.023 (CE) on one split; no improvement claimed | Executed (B) | Verified as an observation only |
| Q3-17 | C5 | `save_state` / `load_state(..., learner=model)` restore the same prediction | Executed (B) | Verified |
| Q3-18 | Figure | Workflow structure (three sets; CE wraps the trained model; calibrate → explain → outputs) | CE papers (A), source (B) | Verified; caption calls it a simplified teaching picture |

No performance comparison, no new guarantee and no causal claim was added.
