# 06 — Educational and architecture review

**Status:** COMPLETED (review). Gaps that need new pages are PENDING PRODUCT OWNER APPROVAL (D-25).

## 1. Seven-entry navigation

| Entry | Purpose / audience | First action now | L1 → L2 → L3 links | Back to Quick Start | Change this cycle |
|---|---|---|---|---|---|
| Quick Start | Newcomers; code-free | Choose path A/B/C | A1/A2 → B → C1/C2 → tutorials | — | None |
| CE: What & Why | Newcomers, decision-makers | "Read in this order", step 1 | A1 → `what-is-ce` → semantics | Yes (Path A, CE by example) | **WP-13** |
| How CE Works | Learners, researchers | "Read in this order", step 1 (L1) | `ce_workflow` → `calibration_methods` → semantics | Yes | **WP-14** |
| CE in Practice | Practitioners | Python tutorials | Tutorials → task pages → evaluate | Yes (hub) | Notebook notes |
| Software & Integration | Developers | Install / Quick API | Quick API → API reference → troubleshooting | Yes (Quick API "Before this") | **WP-6** |
| Project & Resources | Researchers, contributors | Research & publications | Citing, glossary | — | None |
| Commercial Services | External link | — | — | — | None |

No new navigation level was added. All URLs are unchanged. Two sidebar labels
changed, both as specified in the plan:
- "Trustworthy AI" → "Regulation Context (EU AI Act)";
- "Calibration & Uncertainty" → "Guarantees by Mode".

## 2. Three readers

| Reader | Can they now… | Before → after | Remaining gap |
|---|---|---|---|
| A — Beginner | say what CE is, why it exists, how to start, what outputs mean, where next | Already good via Path A/B; What & Why now gives an ordered route and separates calibration from accuracy | No L1 calibration-intuition page with a reliability diagram (WP-3, new page) |
| B — Practitioner | pick task and mode, prepare data, run an example, read output, troubleshoot, find the API | The Quick API now answers the entry questions with one runnable example and linked calls; troubleshooting is a reproduced, version-labelled list | 2 quickstart notebooks not verifiable in this environment (D-29) |
| C — Researcher | find methods, assumptions, guarantees vs limits, references, reproduce examples, open questions | How CE Works now names the chain and the levels; `ce_workflow` lists six distinctions; open questions carry markers | Open questions are scattered as markers; a single public "open questions" page is WP-9 (needs approval) |

## 3. Duplication and consistency

- The **task → method → output** table exists once (`ce_workflow`). The landing
  links it instead of copying it.
- `calibration_methods` §4 keeps the formal L3 version. The L1 table points to
  it, and the two do not repeat each other's reasoning.
- Explanation types are now defined the same way in two places:
  `ce_workflow` and `interpret_explanations`. Each has one sentence, and both
  link the same figure.
- **Still duplicated (WP-4, not in scope):** the motivation in `why-ce` and
  `what-is-ce`. The new "Read in this order" table makes `what-is-ce` the What
  & Why owner, while `why-ce` remains the Quick Start (Path A) owner.

## 4. Accessibility and usability

- **Figures.**
  - V-8 reuses an accessible SVG, with full alt text and a provenance caption.
  - No new figure was drawn.
- **Phone layout.**
  - 8 tables gained the compact layout (`what-is-ce` 2, `ce_workflow` 2,
    `calibration_methods` 4); the two new Quick API tables also use it.
  - Tables that still scroll inside their own wrapper at 390 px on the checked
    pages fell from 11 to 8, with 0 page-level overflow.
  - The residual 8 are dense reference tables (the 11-column worked example,
    long code identifiers). Further work belongs to WP-18.
- **Theming.** The Beta banner and light/dark rendering were checked on all
  36 views (`07`).

## 5. Gaps that need PO decisions

| Gap | Package | Needs |
|---|---|---|
| L1 calibration intuition with a reliability diagram (V-7) | WP-3 | New page (D-25) |
| Black boxes and explainable AI, with the attribution vs CE schematic (V-2) | WP-2 | New page (D-25) |
| Internal-mechanism figure (V-4) | WP-4 | Figure work; no page needed |
| Research pathway and labelled open questions | WP-9 | Author answers for SR-02 |
