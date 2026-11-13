# Author-review sheet (WP-8)

**Date:** 2026-11-13. **For:** the CE authors, via the PO. **Status:** open; no
item is resolved by the documentation team. The established register SR-01…SR-16
lives in `development/reports/autonomous-runs/20261112T100852+0100/SCIENTIFIC-CLAIMS-REGISTER.md`
(carried over unchanged by run 2); this sheet adds new items **N-01…N-05** found
in the 2026-11-13 audit and records the interim wording used on Beta V2.

## New items

| ID | Page:line (Beta V2) | Current text (quoted) | Issue | Evidence | Options for the authors | Interim on Beta V2 |
|---|---|---|---|---|---|---|
| N-01 | `practitioner/playbooks/eu-ai-act-compliance.md:478` | "Art. 15 \| Declared, verifiable accuracy; robustness documentation \| Empirical coverage vs. nominal confidence (Venn-Abers guarantee) \| **Covered**" | Mixes coverage (a CPS/interval notion), "confidence" and Venn–Abers (a probability-calibration method); marks a legal requirement as "Covered". Lines 475–479 mark three more articles "Covered" (Art. 13, 14, 50; Art. 50 calls alternatives "actionable counterfactual rules") | page; SR-03, SR-04, SR-08 | (a) Rephrase as "supports" with the exact CE output; (b) separate classification calibration from interval coverage; (c) remove compliance verdicts | Unchanged (legal reading; route to authors and PO) |
| N-02 | `tasks/regression.md` (former line 58) | "You can request explanations with arbitrary confidence levels by strictly passing the percentiles" | Percentiles set the target coverage of a prediction interval, not a confidence level | ADR-021; `calibration_methods` §3 | Confirm "coverage level" | **Changed** to coverage wording ("holds on average over many cases, not for each case") |
| N-03 | CE library: regression plot label "Prediction interval with 90.0% confidence" (`src/calibrated_explanations/viz/…`) | (library string) | Same confusion as N-02, in the rendered plot; also the label is overlapped by the lower panel at default size | rendered plot (WP-1 session) | Rename to "90% prediction interval" | Report only (library code is out of scope) |
| N-04 | `foundations/concepts/guarded_explanations.md:81` | "`confidence` … Coverage-style conformity threshold" | Readers may read `confidence` as a confidence level for predictions | `GuardedOptions` docstring | Confirm wording | **Added**: "it is not a confidence level for a prediction or its interval" |
| N-05 | `tasks/regression.md`, `foundations/concepts/calibration_methods.md` (one-sided intervals) — **also the official docs** | "the open side is reported as the smallest … or largest … target value in the calibration set" | Official `main` (`371bd806`, #237) now reports `-inf`/`inf`; v1.0.2 keeps the placeholder | official CHANGELOG, ADR-021 §2/§4 | Update official docs for v1.1.0 | **Changed** to version-aware wording on Beta V2 |

## Interim wording applied for existing SR items (Beta V2)

| SR | Page | Interim change | Marker |
|---|---|---|---|
| SR-07 | `tasks/classification.md` (factual), `tasks/probabilistic_regression.md` (`uq_interval`) | "epistemic and aleatoric" removed from the description of ranges | "*Whether these ranges should be described as epistemic or aleatoric uncertainty is under review by the CE authors.*" |
| SR-08 | `tasks/classification.md` (table row, alternatives section) | "counterfactuals", "necessary to flip" replaced by a neutral description; "not recommendations and make no causal claim" | — (neutral wording makes no claim either way) |
| SR-03 | `get-started/ce-by-example.md` (WP-1, generated) | merged estimate "does not carry that exact property" | "*Wording under review by the CE authors.*" |

## Still open, unchanged on Beta V2

SR-01 (assumption wording, 9 pages), SR-02 (coverage statement), SR-04
(vocabulary), SR-05/SR-06 (comparison page), SR-09/SR-10 (ensured and filter
definitions; the ensured playbook's epistemic/aleatoric table and "more reliable
intervention recommendations" also fall under SR-07/SR-08), SR-11 (mode name),
SR-12 (spelling), SR-13 (multiclass bounds above 1), SR-14 (explanation
construction), SR-15 (thresholded regression validity), SR-16 (reject option).
