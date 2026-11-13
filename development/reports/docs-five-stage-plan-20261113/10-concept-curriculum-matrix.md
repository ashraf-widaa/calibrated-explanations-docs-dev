# 10 — Concept dependency and learning-curriculum matrix (Deliverable C)

Concepts are listed in **prerequisite order**. Coverage cells name the page
(and section) that teaches the concept at that level today; **—** means
missing; **[N]** proposed owner; **[S]** needs author review. Evidence: concept
locator over `docs/**/*.md` (2026-11-13), execution audit (`01` §4), page
outlines.

Task/mode column: C = classification, IR = interval regression, PR =
probabilistic regression, all = every mode.

## Stage 1 — Foundations

| # | Concept | Prerequisites | Canonical owner | Stage | L1 | L2 | L3 | Task/mode | Next | Gaps |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AI system vs AI model | — | `get-started/ml-foundations` (new §A0) | 1 | — | — | — | — | 2 | **Missing.** "AI system" appears only in the two compliance playbooks |
| 2 | Rule-based AI vs machine learning | 1 | ml-foundations A1 | 1 | A1 (one clause: "instead of writing rules by hand") | — | — | — | 3 | Needs a short explicit contrast |
| 3 | Training vs inference | 2 | ml-foundations A1 | 1 | A1 [V] | walkthrough §3 | — | — | 4 | — |
| 4 | Learning approaches (supervised, unsupervised, self-supervised, RL) | 3 | ml-foundations A2 | 1 | A2 table [V] | — | — | CE: supervised only | 5 | — |
| 5 | Prediction task: classification vs regression | 4 | ml-foundations A3 | 1 | A3 [V] | C1 | — | C, IR, PR | 6 | — |
| 6 | Model families and architectures | 5 | ml-foundations A4 | 1 | A4 [V] | — | — | all | 7 | Mermaid style inconsistent with Path A figures (minor) |
| 7 | Data roles: training, calibration, test; leakage | 5 | ml-foundations A5 | 1 | A5 [V], why-ce | walkthrough §2, C5 step 1 | calibration_methods §1 (notation) | all | 8 | — |
| 8 | Black-box models and transparency | 6 | `explainable-ai` [N] | 1 | — | — | — | — | 9 | **Missing** (one mention, compliance playbook). Must not claim all models are black boxes |
| 9 | Explainable AI (local/global, attributions vs rules) and its limits | 8 | `explainable-ai` [N] (from A7) | 1 | A7 [V] (forms); limits partly A6 | — | theory_and_literature (papers) | all | 10 | Limits of XAI (disagreement, no reliability measure, not causal) scattered |

## Stage 2 — CE concepts

| # | Concept | Prerequisites | Canonical owner | Stage | L1 | L2 | L3 | Task/mode | Next | Gaps |
|---|---|---|---|---|---|---|---|---|---|---|
| 10 | Why CE: what a conventional workflow leaves open; conventional vs CE workflow | 7, 9 | `get-started/why-ce` | 2 | why-ce (figure) [V] | — | what-is-ce (references) | all | 11 | A6 and what-is-ce "The problem" restate it (dedupe) |
| 11 | Prediction score vs probability | 5 | `calibration_intuition` [N] | 2 | ml-foundations A6, why-ce (one sentence each) | walkthrough §4 | calibration_methods §1 | C, PR | 12 | No owner; 8 pages touch it in passing |
| 12 | Calibration (calibrated probability, reliability) | 11 | `calibration_intuition` [N] (L1); calibration_methods §1 (L3) | 2 | why-ce "Four ideas" | walkthrough §4, evaluate_ce §2 | calibration_methods §1 + reliability diagrams | C, PR | 13 | Sidebar "Calibration & Uncertainty" opens L3 semantics instead of an L1 page |
| 13 | Accuracy vs calibration vs confidence score vs uncertainty | 12 | `calibration_intuition` [N] | 2 | — | — | — | all | 14 | **Missing contrast table** (S5 rule in 07) |
| 14 | Uncertainty and the range (lower/upper value) | 12 | `calibration_intuition` [N] | 2 | why-ce, reading-an-output figure | walkthrough §5, quickstarts | semantics | all | 15 | — |
| 15 | Prediction task vs CE mode vs calibration method vs explanation configuration | 5, 14 | `get-started/ce-tasks-and-modes` | 2 | C1 "Four terms" [V] | C1 mode cards | calibration_methods §4 | all | 16 | "Semantic mode" defined only on C1 (fine); glossary entry should point there |
| 16 | Interval regression vs probabilistic regression | 15 | ce-tasks-and-modes; foundations/concepts/probabilistic_regression | 2 | C1 [V] | C3, tasks/regression, tasks/probabilistic_regression | calibration_methods §4, semantics modes 2–3 | IR, PR | 17 | "thresholded regression" on 16 pages incl. calibration_methods §4 heading (terminology C-31) |
| 17 | Probability bounds vs prediction intervals | 14, 16 | `calibration_intuition` [N] (L1); semantics (L3) | 2 | C1 output table (implicit) | C2, C3 | semantics modes 1–3 | C/PR vs IR | 18 | **No explicit L1 contrast**: bounds of a probability (C, PR) vs interval for a value (IR) |
| 18 | Interval semantics by mode (what the range does and does not mean) | 17 | `calibrated_interval_semantics` (L3); L1 summary in `calibration_intuition` [N] | 2→4 | C1 "How the uncertainty differs" [V; PO-reviewed] | — | semantics [V] | all | 19 | L1 summary should link, not paraphrase |
| 19 | Factual explanation (rule, weight, weight range) | 9, 14 | `foundations/how-to/interpret_explanations` (reading); `ce_workflow` § (construction overview) | 2 | why-ce panel 2 | walkthrough §6–7, quickstarts, interpret §2.1 | explanation_structures [S C-37]; CE 2024 paper | all | 20 | Weight sign convention stated in several places — keep one owner (interpret_explanations) |
| 20 | Alternative explanation | 19 | interpret_explanations §2.2; `foundations/concepts/alternatives` | 2 | why-ce panel 3 | walkthrough §8 | alternatives [V], explanation_structures | all | 21 | "counterfactual" wording on task pages and compliance playbooks [S SR-08] |
| 21 | Assumptions and limitations (exchangeability, many cases not one, model not world) | 14 | what-is-ce (summary); semantics (canonical) | 2 | why-ce, what-is-ce [V] | evaluate_ce §5 | calibration_methods §5, semantics | all | 22 | "exchangeable or distribution-matched" on 9 pages [S SR-01, C-18] |
| 22 | Internal CE workflow (calibrate → perturb → weights → ranges) | 12, 19 | `ce_workflow` | 2 | ce_workflow (text) | walkthrough §6 | explanation_structures | all | 23 | **No mechanism diagram**; ce_workflow reuses the comparison figure |

## Stage 3 — Using CE

| # | Concept | Prerequisites | Canonical owner | Stage | L1 | L2 | L3 | Task/mode | Next | Gaps |
|---|---|---|---|---|---|---|---|---|---|---|
| 23 | CE components (wrapper, explanation collections, plots, export, state) | 22 | `get-started/quick_api` (overview) + autosummary | 3 | — | quick_api (fragments) | autosummary [V], architecture | all | 24 | **No components overview**; quick_api blocks not executable |
| 24 | Fit/calibrate/predict workflow in code | 23 | walkthrough (Path B) | 3 | — | walkthrough, C2–C5 [V, executed] | API reference | all | 25 | — |
| 25 | Choosing the mode in code (`threshold`, `uq_interval`, `low_high_percentiles`, `normalization`) | 15, 24 | ce-tasks-and-modes; tasks/* | 3 | C1 cards | C2, C3, tasks pages | parameter-reference | all | 26 | `tasks/regression.md:58` calls percentiles "confidence levels" [S] (see 29) |
| 26 | Guarded explanations (explanation configuration) | 19 | `foundations/concepts/guarded_explanations` | 3 | C1 | C4 [V] | guarded_explanations limitations, ADR-032 | all | 27 | Parameter `confidence` (= 1 − significance) is a guard threshold, not a confidence level — say so explicitly |
| 27 | Applying CE to own data; integration | 24 | apply-to-your-data (C5); integrate_with_pipelines | 3 | — | C5 [V], integrate_with_pipelines [V] | — | all | 28 | Two owners for one card ("Use CE on your own data") |
| 28 | Evaluating CE (Brier, reliability, coverage on held-out data) | 12, 27 | `practitioner/evaluate_ce` | 3 | — | evaluate_ce [V] | calibration_methods §1, §3 | all | 29 | — |
| 29 | Confidence level vs coverage | 18 | `calibration_intuition` [N] (L1); calibration_methods §3 (L3) | 3→4 | — | — | calibration_methods §3 "Why the interval covers" | IR (and guarded/reject parameters) | 30 | **Missing L1**; "confidence" used for percentile choice (tasks/regression:58), for the guard and reject parameters, and in CE's own regression plot label "Prediction interval with 90.0% confidence" (library code, not docs) [S] |
| 30 | Troubleshooting (known errors and surprises) | 24 | `get-started/troubleshooting` | 3 | — | troubleshooting (environment only), C5 table | — | all | 31 | Verified errors not in the owner page |

## Stage 4 — Going deeper

| # | Concept | Prerequisites | Canonical owner | Stage | L1 | L2 | L3 | Task/mode | Next | Gaps |
|---|---|---|---|---|---|---|---|---|---|---|
| 31 | Exchangeability | 21 | calibration_methods §3 "Exchangeability" | 4 | C1 (one paragraph) | — | calibration_methods [V] | all | 32 | Wording conflict C-18 [S] |
| 32 | Venn–Abers predictors (pair, merged estimate) | 12, 31 | calibration_methods §2 | 4 | ce_workflow (one sentence) | walkthrough §5, calibration_methods "Example with CE" | calibration_methods §2 [V] | **C** (and the second stage of PR) | 33 | Merged-estimate guarantee wording [S SR-03]; must not be presented as the method for IR |
| 33 | Conformal prediction and conformal predictive systems | 31 | calibration_methods §3 | 4 | ce_workflow (one sentence) | C3, tasks/regression | calibration_methods §3 [V] | **IR**, first stage of PR | 34 | — |
| 34 | Marginal vs conditional coverage; Mondrian calibration | 33 | calibration_methods §3 (marginal); conditional_calibration (Mondrian) | 4 | — | conditional_calibration, mondrian playbook | calibration_methods | IR (C via Mondrian categories) | 35 | "Marginal coverage" taught on 2 pages only; marginal-coverage sentence on C1 under review [S SR-02] |
| 35 | Probabilistic regression construction (CPS then Venn–Abers, split calibration set) | 32, 33 | calibration_methods §4; probabilistic_regression | 4 | C1 limitation 3 | C3 | calibration_methods §4 | PR | 36 | Validity of the two-half construction [S SR-15] |
| 36 | Multiclass calibration and normalisation of bounds | 32 | ce-tasks-and-modes limitation 1 | 4 | C1 | C2 (shows >1 and simplex) | — (no L3 owner) | C (multiclass) | 37 | Interpretation [S SR-13]; no L3 derivation |
| 37 | Aleatoric vs epistemic uncertainty | 14, 32 | — (proposed: glossary entry + ensured-explanations playbook section, after author answer) | 4 | — | ensured playbook table | papers (ensured, `citing`) | C, PR | 38 | **No canonical definition**; used on task pages and the ensured playbook [S SR-07] |
| 38 | Explanation construction (perturbation, discretisation, weight ranges; no per-feature guarantee) | 22, 32, 33 | explanation_structures (L3); ce_workflow (overview) | 4 | ce_workflow | walkthrough §6 | explanation_structures [S C-37], CE 2024 paper | all | 39 | Filter semantics and value selection blocked [S]; "no formal per-feature guarantee" [S SR-14] |
| 39 | Ensured and guarded filters | 20, 38 | alternatives; ensured playbook; guarded_explanations | 4 | — | ensured playbook, C4 | alternatives, guarded_explanations | all | 40 | "more reliable intervention recommendations" (ensured playbook line 3) — causal-sounding [S SR-08] |
| 40 | Statistical guarantees vs empirical observations | 18, 28 | semantics (guarantees); evaluate_ce (observations) | 4 | what-is-ce table | evaluate_ce | semantics, calibration_methods §5 | all | 41 | Compliance playbook line 478 presents an empirical/coverage item as "Venn-Abers guarantee — Covered" [S] |
| 41 | Comparison with other XAI and conformal methods | 9, 40 | `compare` (rewrite) | 4 | — | — | compare (20 lines), what-is-ce §relations | all | 42 | Unsupported "more stable rules" [S SR-05/06] |
| 42 | Research history, replication, open questions | 41 | researcher/index; replication; future_work | 4 | — | replication [V] | theory_and_literature, future_work | all | 43 | No history list; future_work items unlabelled |

## Stage 5 — Contributing

| # | Concept | Prerequisites | Canonical owner | Stage | L1 | L2 | L3 | Task/mode | Next | Gaps |
|---|---|---|---|---|---|---|---|---|---|---|
| 43 | Development setup and tests | 24 | `contributor/development_setup` [N] (from CONTRIBUTING.md) | 5 | — | CONTRIBUTING.md (not rendered) | test_policy, pr_guide | — | 44 | **Missing page** |
| 44 | Software architecture | 23 | foundations/concepts/architecture | 5 | — | — | architecture [V] | — | 45 | No reading guide |
| 45 | Extension points (plugins, PlotSpec, modalities) | 44 | plugin-contract; extending guides | 5 | — | plugins, use_plugins | plugin-contract, api/plugins | — | 46 | Contract examples outdated (`data_modalities`, private import) |
| 46 | Contribution workflow and governance | 43 | pr_guide; contributor/index | 5 | — | contributor/index | governance pages | — | — | Hub cites unreachable maintainer files |

## Terminology order (introduce in this sequence; define once)

prediction task (5) → classification/regression (5) → score vs probability
(11) → calibration (12) → uncertainty/range (14) → CE mode (15) → interval vs
probabilistic regression (16) → probability bounds vs prediction intervals
(17) → interval semantics (18) → factual vs alternative (19–20) → confidence
level vs coverage (29) → Venn–Abers vs CPS (32–33) → marginal vs conditional
coverage (34) → aleatoric vs epistemic (37, after author answer) → statistical
guarantees vs empirical observations (40).
