# 05 — Scientific review and author-review register

**Status:** COMPLETED as a review. The register items are PENDING AUTHOR REVIEW.

**Scope:** the pages changed in this cycle and the material needed to verify
them.

**Evidence order (`07` S12):** CE papers > code/tests > official docs > Beta
pages > literature > editorial.

**Release-blocking columns:**
- **Beta** = promotion of a candidate to Beta `latest`.
- **Official** = any publication on the official CE site.

## 1. Mandatory topics (master prompt §8)

| # | Topic | Result on changed pages | Evidence |
|---|---|---|---|
| 1–2 | Venn–Abers; classification bounds | Described as bounds of a probability, "not a confidence interval" (Quick API, `ce_workflow`) | `calibration_methods` §2 (Vovk & Petej 2014); code `calibration/venn_abers.py` |
| 3 | Conformal prediction / regression intervals | "Interval for the value; coverage on average over many cases" | `calibration_methods` §3 (Vovk et al. 2019/2022; Lei et al. 2018) |
| 4 | Probabilistic regression / threshold events | "Bounds of the probability of an event, not an interval for the value"; SR-15 marker | ADR-021 §3; `interval_regressor.py` |
| 5 | Exchangeability, shift | Exchangeability stated; shift ends the guarantee | ADR-021; SR-01 marker kept |
| 6 | Marginal vs conditional coverage | "Not for each case, nor each subgroup unless calibrated per group" | `calibration_methods` §5 limitations table |
| 7 | Calibration vs accuracy | New section on `what-is-ce` | Guo et al. 2017; definition |
| 8 | Aleatoric vs epistemic | Not asserted; SR-07 marker | SR-07 |
| 9–10 | Factual vs alternative; attribution vs causal | Explanation types, not modes; alternatives are "model response, not a recommended action" | C1 capability table; `ce-reading-an-output.svg` |
| 11 | Prediction vs explanation guarantees | "No formal guarantee is claimed" for explanation ranges | Semantics page |
| 12 | Released vs development behaviour | See §2 | Executed on three code bases |
| 13 | API / example compatibility | All new examples and troubleshooting entries executed on 1.0.2 and 1.1.0.dev0 | `02` |
| 14 | Trustworthy AI / regulation / compliance | Card relabelled; overclaim removed from `interpret_explanations`; playbook claims routed (N-01, N-07, N-08) | — |

## 2. Version-sensitive issue: one-sided regression intervals

The same call, `predict(x, uq_interval=True, low_high_percentiles=(-inf, 90))`
and `(10, inf)`, diabetes data, random forest, `random_state=42`:

| Code base | `__version__` | Open side |
|---|---|---|
| Released v1.0.2 (`609d7b72`) | 1.0.2 | calibration min/max placeholder (39.0 / 317.0) |
| Beta `src/` (`f908527f` state) | 1.1.0.dev0 | the same placeholder |
| Official `main` (`371bd806`, #237) | **1.1.0.dev0** | `-inf` / `inf` |

**Findings.**
1. The documentation wording, "a placeholder in v1.0.2; `-inf`/`inf` from v1.1.0", is correct for released versions.
2. Beta's own build reports 1.1.0.dev0 but still behaves like v1.0.2. A reader on a development install cannot tell the two behaviours apart from the version string (N-09).
3. Tests cover only the wording (`tests/docs/test_beta_v2_corrections.py`); no test checks the behaviour in either version.
4. An isolated code-sync proposal is still needed. That is D-23: sync Beta `src/` to `371bd806` on its own branch and rerun the docs tests. Not done: merging upstream implementation needs PO approval.

## 3. Register

Confidence = how sure the documentation team is about the *concern*.

| ID | Location | Concern | Evidence | Proposed correction | Conf. | Author? | Beta | Official |
|---|---|---|---|---|---|---|---|---|
| SR-01 | 9 pages ("exchangeable or distribution-matched") | Assumption should be exchangeability only? | ADR-021 (B) | Use "exchangeable" only | High | Yes | No (marked) | **Yes** |
| SR-02 | `calibration_methods`, X2 | Exact coverage statement, ties, Mondrian | Vovk 2019/2022, Lei 2018 (D) | Authors confirm X2 text | Med | Yes | No (marked) | **Yes** |
| SR-03 | `calibration_methods`, `ce-by-example` | Validity is for the Venn–Abers pair; CE reports merged *p* | Vovk & Petej 2014 (D); code (B) | Keep merged *p* without exact guarantee | High | Yes | No (marked) | **Yes** |
| SR-04 | Glossary, task pages | Probability interval vs prediction interval vocabulary | Standard (D) | Adopt both terms per mode | High | Yes | No | No |
| SR-05 | `compare.md` | May Venn–Abers be called conformal? | Literature (D) | "Venn predictor" | High | Yes | No | No |
| SR-06 | `compare.md` | "More stable rules than LIME" unsupported | CE-REG §5.2 (A) | Remove or cite | High | Yes | No | **Yes** |
| SR-07 | Task pages, `ce_workflow` (new marker) | Are ranges aleatoric/epistemic? | No decomposition in `src/` (B) | Neutral wording (done) until answered | High | Yes | No (marked) | No |
| SR-08 | Alternatives pages | "Counterfactual", "flip" | Semantics page (A/C) | Neutral wording (done on task pages) | Med | Yes | No | No |
| SR-09 | Glossary | Ensured: "no wider" vs "narrower" | Docstrings disagree (B) | Authors pick one | High | Yes | No | No |
| SR-10 | Glossary | Super/semi/counter/Pareto definitions | Three competing definitions (B/C) | Authors define | Med | Yes | No | No |
| SR-11 | Task page titles | Name of the second regression mode | Inconsistent (C) | Authors pick | High | Yes | No | No |
| SR-12 | Global | Venn-Abers vs Venn–Abers | Both present | House style | High | Yes | No | No |
| SR-13 | Troubleshooting (new entry), C1 | Multiclass upper bounds > 1 by default | Reproduced 1.18 (B) | Confirm intended default | High | Yes | No | No |
| SR-14 | — | Explanation construction (baseline, weight ranges) | Paper §3.4 (A); code (B) | Write ADD-2 after answer | Med | Yes | No | No |
| SR-15 | `ce_workflow` (new marker), V-6 panel C | Validity of threshold-event probabilities | ADR-021 §3 (B) | Authors confirm | Med | Yes | No (marked) | **Yes** |
| SR-16 | Reject pages | Which reject validity statements are canonical | Four pages (C) | Authors classify | Med | Yes | No | No |
| N-01 | `eu-ai-act-compliance.md:472–479` | "Covered" legal verdicts; coverage/confidence/Venn–Abers mixed | Page (C) | "Supports", exact output, no verdicts | High | Yes + PO | No (inherited, live) | **Yes** |
| N-02 | `tasks/regression.md` | "Confidence levels" for percentiles | ADR-021 | Done on V2 | High | Confirm | No | No |
| N-03 | Library plot label "…with 90.0% confidence" | Same confusion, in a rendered plot | `viz/` (B) | "90% prediction interval" (library change) | High | Yes | No | No |
| N-04 | `guarded_explanations.md:81` | `confidence` read as a prediction confidence | Docstring (B) | Done on V2 | High | Confirm | No | No |
| N-05 | One-sided endpoints | Official #237 | §2 | Version-aware wording (done) | High | Confirm | No | No |
| **N-06** | `troubleshooting.md` (Beta-written) | Known issue misdescribed (blamed `add_conjunctions`) | Reproduced on 1.0.2 and 1.1.0.dev0 (B) | **Fixed** | High | No (implementation fact) | — | — |
| **N-07** | `eu-ai-act-compliance.md:392–396` | "Empirical coverage **on the calibration set**", "**certifiable bound**", "90 % confidence". Coverage is a property over new exchangeable cases (marginal), not of the calibration set; "certifiable" overstates it | `calibration_methods` §3 (B/D) | Rephrase as marginal coverage on new cases, no "certifiable" | High | Yes + PO | No (inherited, live) | **Yes** |
| **N-08** | `eu-ai-act-compliance.md:479` | Art. 50 labelled "Right to explanation". In Regulation (EU) 2024/1689, Art. 50 sets transparency obligations for certain AI systems; the right to explanation of individual decision-making is Art. 86 | Regulation text (to be checked against the Official Journal by the PO) | Relabel the row or cite Art. 86 | High | PO (legal) | No (inherited, live) | **Yes** |
| **N-09** | Version statements | `1.1.0.dev0` names two different behaviours (Beta `src/` vs official `main`) | §2 (B) | D-23 sync, or state the source commit on the version page | High | No | No | No |
| **N-10** | `reject-policy.md:728–741` | "Confidence level" table and reject rates, without evidence in the repository | Page (C), external study link | Authors confirm or soften | Med | Yes | No (inherited) | No |
| **N-11** | `apply-to-your-data.md:200` | "An explanation has no rules" for saturated cases: not reproduced (a saturated case still had rules) | Reproduction (B) | Find a reproducing case or remove the row | Med | No | No | No |

## 4. Corrections made in this cycle

| Item | Status |
|---|---|
| N-06 | Fixed |
| NaN, telemetry and `filter_features` version notes on the troubleshooting page | Fixed (implementation facts) |
| `interpret_explanations` overclaim ("ensures … safe decisions") | Removed (editorial) |
| Unverified telemetry snippet | Removed (editorial) |
| "Trustworthy AI" card | Relabelled (editorial) |

Nothing on the register was resolved by the documentation team.
