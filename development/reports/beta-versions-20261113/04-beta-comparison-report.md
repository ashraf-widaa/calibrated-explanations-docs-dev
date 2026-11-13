# Beta V1 / V2 / V3 comparison

**Date:** 2026-11-13. **Previews:** none published yet (push blocked, see
`03-version-register.md`); local preview of the integrated candidate at
http://127.0.0.1:8002/. Screenshots of the WP-1 baseline:
`acceptance/` in the session scratchpad (landing, Path B, Path C, 390/1440 px);
V3 phone-table screenshot `acceptance/v3_c1_capability_390.png`.

Scale 1–5 (5 best), scored against the evidence listed; a rise is only given
where a change is verified.

| Criterion | V1 Reference (`917a04e2`) | V2 Correctness (`1e487429`) | V3 Visual (`f06061b9`) | Evidence |
|---|---|---|---|---|
| 1 Scientific accuracy | 3 | **5** | 3 | V2 fixes A-01 (one-sided endpoints vs official #237), A-05, A-07; marks SR-07/SR-08; V3 adds correct per-mode labels in V-6 |
| 2 CE content coverage | 4 | 4 | **5** | V3 adds the missing three-output-type explanation (A-17) on the canonical page |
| 3 Conceptual clarity | 4 | 4 | **5** | V-6 separates probability bounds from prediction intervals and threshold probabilities |
| 4 Learning progression | 4 | 4 | 4 | Unchanged structure; V3 adds a cross-link from C1 to V-6 |
| 5 Practical usefulness | 4 | **5** | 4 | V2: six code examples now run as written (agent guide, plugin contracts, retrieval, config order, schema fence); verified-version statement |
| 6 Navigation | 4 | 4 | 4 | No structural change in any candidate |
| 7 Visual quality | 4 | 4 | **5** | V-6 figure in the established palette, readable at 390 px |
| 8 Accessibility | 4 | 4 | **5** | V-6 `<title>`/`<desc>`/alt; tables no longer need horizontal scrolling |
| 9 Mobile readability | 3 | 3 | **5** | V1/V2: C1 tables +72/+244 px, A1 +67 px; V3: 0 at 390 px (Playwright) |
| 10 Maintainability | 4 | **5** | 4 | V2 adds 17 regression tests for the corrections; V3 adds 7 (figure numbers traced to outputs) |
| 11 Alignment with official CE behaviour | 3 | **5** | 3 | V2 matches official `main` (`371bd806`) and the v1.0.2 release |

## Trade-offs

- V2 and V3 change disjoint files (the merge was conflict-free), so they
  combine without compromise.
- V3's compact tables use smaller text (0.8 em) on phones only; desktop is
  unchanged. Capability headers are now short ("Binary", "Multiclass", …) with
  one explanatory line above the table on all screens.
- Neither candidate adds new pages; the larger planned additions (calibration
  intuition page, explainable-AI page, contributor setup page) still need PO
  approval for new pages.

## Recommendation

Adopt the **integrated candidate** (`944942cd` = V2 + V3) as the next Beta
baseline after review of its published preview. It keeps every V1 (WP-1)
improvement, adds all verified corrections, and fixes the deferred mobile
issues. Promotion to `main`/`latest` requires PO approval.
