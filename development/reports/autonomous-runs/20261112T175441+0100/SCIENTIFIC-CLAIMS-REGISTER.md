# Scientific claims register — run 2

**Carried over unchanged:** SR-01 to SR-16 and IF-01 from
`../20261112T100852+0100/SCIENTIFIC-CLAIMS-REGISTER.md`. **None was resolved in
run 2.** Pages that touch them keep "under review" wording.

## New statements introduced in run 2 and their support

Evidence levels:
- **A**: original CE publication or page;
- **B**: source code or executed output;
- **D**: external literature;
- **E**: editorial.

| ID | Page | Statement | Evidence | Status |
|---|---|---|---|---|
| C2-01 | walkthrough §5 | The member of the Venn-Abers pair selected by the true label is calibrated; this assumes exchangeability, is a property over many cases, and cannot pick the member at prediction time | Vovk, Petej & Fedorova 2015, Prop. 1 (D); spec `05` §5 | **Under review** (SR-03); marked on the page |
| C2-02 | walkthrough §5 | The merged estimate has no exact calibration guarantee | Vovk, Petej & Fedorova 2015 (D) | Under review (SR-03); marked |
| C2-03 | walkthrough §5 | Calibration does not necessarily improve the Brier score; here calibrated 0.0445 vs raw 0.0366 | Executed (B); Brier 1950 (D) | Verified for this dataset; general statement is the absence of a guarantee |
| C2-04 | walkthrough §6 | Factual weight construction in this configuration (binary split; predicted labels; 25/50/75 percentiles; averaged bounds) | `calibrated_explainer.py:368`, `discretizer_config.py:53`, mechanisms `04` (B) | Verified; scoped to the configuration on the page |
| C2-05 | walkthrough §7, alternatives page | Weight = case probability − alternative probability (0.286 − 0.476 = −0.190) | Executed (B) | Verified |
| C2-06 | walkthrough §7 | The 17 weights sum to −0.069, not to the prediction | Executed (B) | Verified |
| C2-07 | ML basics A7 | Local vs global; attributions (LIME, SHAP) vs rules; explanations describe the model | Ribeiro et al. 2016; Lundberg & Lee 2017 (D); CE 2024 paper (A) | Verified (standard definitions) |
| C2-08 | `what-is-ce` | Problem statement: XAI tools explain whatever the model outputs; tree models without calibration often miscalibrated | README (A) | Verified source; "often" is the README's own wording |
| C2-09 | `what-is-ce` | Guarantees vs non-guarantees table | `calibrated_interval_semantics` (A) | Verified; the assumption wording (SR-01) is marked |
| C2-10 | `what-is-ce` | Design-level comparison with attribution methods and conformal packages | `compare.md` (A); method papers (D) | Verified as design statements; **no performance claims** (SR-05, SR-06 open) |
| C2-11 | `probabilistic_regression` | `threshold=(low, high)` gives P(low < y ≤ high); column 1 = event; column 0 = 1 − p | `interval_regressor.py:328`, `:472–482` (B); executed | Verified |
| C2-12 | `probabilistic_regression` | Validity of the two-half CPS + Venn-Abers construction | ADD-1 §4 | **Under review** (SR-15); marked |
| C2-13 | `alternatives` | Classification alternatives use at most 8 ranges per feature | `discretizers.py:229–231` (B) | Verified |
| C2-14 | `alternatives` | Scenario ranges are averages of Venn-Abers bounds and do not carry the case's guarantee | Mechanisms `04` §4.2 (B) | Verified mechanism; "no guarantee" stated as not claimed |
| C2-15 | `evaluate_ce` | Empirical checks (Brier, log loss, reliability bins, coverage share 0.955 on 89 cases) | Executed (B); scikit-learn | Verified as observations; the coverage guarantee itself is under review (SR-02), marked |
| C2-16 | glossary | Brier score, reliability diagram, local explanation, feature attribution definitions | Brier 1950; Guo et al. 2017 (as in ADD-1 §1); A7 sources | Verified (standard definitions) |

## Questions for the CE authors (unchanged list, for the next author round)

SR-01 assumption wording · SR-02 coverage statement · SR-03 Venn-Abers
guarantee object · SR-04 vocabulary · SR-05 "conformal" umbrella · SR-06
comparison claims · SR-07 epistemic/aleatoric · SR-08 counterfactual · SR-09
ensured rule · SR-10 filter definitions · SR-11 Mode 2 name · SR-12 spelling ·
SR-13 multiclass bounds · SR-14 explanation construction · SR-15 thresholded
validity · SR-16 reject-option statements.
