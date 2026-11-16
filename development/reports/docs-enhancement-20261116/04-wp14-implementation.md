# 04 — WP-14: How CE Works

**Status:** COMPLETED for the WP-14 scope. V-4 (internal-mechanism figure,
WP-4) and V-7 (reliability-diagram intuition page, WP-3) are NOT STARTED: they
were not in scope and the WP-3 page needs approval.

## 1. Changes

| File | Change |
|---|---|
| `docs/sections/how-ce-works.md` | New "The chain to follow" (**task → CE mode → statistical method → output and what its range means → assumptions and guarantees**) linking the two `ce_workflow` sections that hold it; **"Read in this order"** with five steps, each tagged L1/L2/L3, and a definition of the levels; prerequisite pointer; cards in reading order with level tags; card "Calibration & Uncertainty" → "Guarantees by Mode" |
| `docs/index.md` (How CE Works group) | Sidebar: Overview → The CE Workflow → Statistical Methods → **Guarantees by Mode** → How to Read CE Explanations → Essential Foundations (plan `02` §2.3 order; URLs unchanged) |
| `docs/foundations/concepts/ce_workflow.md` | Note that the five steps are a teaching view, not every internal call. The method table gains a **"Read the range as"** column: probability bounds / interval with marginal coverage / event-probability bounds. Explanation types are not modes. SR-15 marker. New list **"Six things are easy to mix up"**: probability calibration, coverage (marginal vs per-group → `conditional_calibration`), explanation ranges, model correctness, distribution shift, aleatoric/epistemic (SR-07 marker). Labels `ce-workflow-methods`, `-explanations`, `-guarantees`. Both tables in the phone layout |
| `docs/foundations/concepts/calibration_methods.md` | Four wide tables (worked example, modes, interval kinds, limitations) wrapped in the phone layout; no text change |
| `docs/foundations/how-to/interpret_explanations.md` | New "Factual and alternative explanations at a glance" with **V-8**: reuse of `ce-reading-an-output.svg` (real CE output, case 2) and a caption saying panel 3 is a model response, not a recommendation. §4 telemetry walkthrough → one paragraph linking `configure_telemetry`; the removed snippet used an unverified `telemetry["plot_source"]` key on a collection attribute. Intro links the semantics page. Notebook path fixed (`advanced/demo_under_the_hood.ipynb`). Closing overclaim ("ensures … safe … decisions") replaced |
| `tests/docs/test_how_ce_works_progression.py` (new, 6 tests) | Chain sentence and levels; sidebar order and label; three output meanings; the six distinctions and both markers; telemetry removed and figure present; phone tables |

## 2. Coverage of master prompt §7

| Topic | Where | Notes |
|---|---|---|
| A. Unified workflow, teaching view | `ce_workflow` § workflow + new note | Steps unchanged (previously reviewed) |
| B. Classification / Venn–Abers / bounds | `calibration_methods` §2 (existing L3); `ce_workflow` table L1 | No new derivation; existing worked example kept |
| C. Interval regression / CPS / coverage, marginal vs conditional | `calibration_methods` §3; `ce_workflow` table and distinctions | "Not for each case", "not per subgroup unless calibrated per group" |
| D. Probabilistic regression / threshold events | `ce_workflow` table "not an interval for the value"; `calibration_methods` §4 | SR-15 marker added on `ce_workflow` |
| E. Factual vs alternative are types, not modes | `ce_workflow`, `interpret_explanations` | Verified against the C1 capability table: both run in all four task columns |
| F. Assumptions vs guarantees | `ce_workflow` § What the guarantees rest on | Explanation ranges are given no guarantee (as before) |
| G. V-6 figure | Checked on the guarantees page | Three panels, alt text and caption agree (verified live on 2026-11-13; unchanged in this cycle) |

## 3. Author-review dependencies

The changes depend on these open items. None is presented as resolved; each is
either marked or linked:
- SR-01: assumption wording;
- SR-02: coverage wording, reused from the reviewed X2 text;
- SR-07: aleatoric/epistemic;
- SR-15: threshold-event validity.
