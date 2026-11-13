# CE documentation: five-stage learning journey — plan (Phase 0)

Planning deliverables, 2026-11-13, baseline `a55c7e9d` (= Beta `main`). No
published page was changed.

**Revision 2 (2026-11-13, entry-point audit).** The PO agreed on an Integrated
Learning and Reference Architecture with **Quick Start as the five-stage
roadmap (Option B)** and **no separate `learning-journey.md`**. Documents
08–12 were added; 02 was rewritten (revision 2); 03, 05 and 06 were updated to
match. Where an older statement conflicts, 02 rev. 2 and 12 win.

| File | Content |
|---|---|
| `01-current-state-audit.md` | Baseline gates, structure, strengths, weaknesses per stage, code-execution audit, risks |
| `02-target-information-architecture.md` | **Rev. 2 — Deliverable E.** Three functions (tutorial, compendium, manual); seven target entry-point trees; Quick Start Option B; navigation directions; canonical owners |
| `03-content-migration-matrix.md` | Page-by-page action, reason, priority, dependencies, validation |
| `04-interactive-learning-plan.md` | Existing interactive resources and what to reuse, verify or not build |
| `05-phased-implementation-roadmap.md` | Phase framing (work packages superseded by 12) |
| `06-implementation-prompts.md` | Copy-ready Claude Code prompts (mapped to the WPs in 12) |
| `07-quality-and-acceptance-criteria.md` | Gates, scientific and editorial rules, layout checks |
| `08-homepage-entry-point-audit.md` | **Deliverable A.** Seven entry points: verified navigation trees, reader-journey assessment, gaps |
| `09-entry-point-navigation-matrix.md` | **Deliverable B.** Reader goal, current vs proposed path, function, levels, gaps, change classes |
| `10-concept-curriculum-matrix.md` | **Deliverable C.** 46 concepts in prerequisite order with owner, stage, L1/L2/L3 coverage, gaps |
| `11-cross-entry-navigation-matrix.md` | **Deliverable D.** Canonical pages linked from several entry points, with direction and placement |
| `12-prioritised-improvement-plan.md` | **Deliverable F.** WP-1…WP-12 with objectives, pages, dependencies, verification, acceptance, risks, effort; sequence; decisions D-11…D-15 |

Phase reports go to `phase-reports/` (created by the first implementation
prompt).

## Decisions requested from the PO

| ID | Decision | Recommendation |
|---|---|---|
| D-1 | ~~Journey page~~ **Superseded:** five stages as a reading order over the existing sections, presented by the Quick Start landing (Option B) | Approved in principle by the PO brief — confirm |
| D-2 | ~~Where the journey page is linked~~ **Superseded:** no `learning-journey.md`; section landings may carry one "Stage n" line linking back to the Quick Start roadmap | Approve the optional landing lines |
| D-3 | New Stage 1 page `explainable-ai.md` in "CE: What & Why", taking over ml-foundations A6–A7 | Approve |
| D-4 | New `calibration_intuition` page under "How CE Works"; relabel the sidebar entry of `calibrated_interval_semantics` from "Calibration & Uncertainty" to "Guarantees by mode" (URL unchanged); retarget the "Can We Trust AI Outputs?" card to the new page | Approve |
| D-5 | Notebooks: link only those that pass the notebook driver; do not edit notebooks (mirrored from the official project) | Approve |
| D-6 | Rewrite `compare.md` as a design comparison with no performance claims | Approve |
| D-7 | Development setup page: include `CONTRIBUTING.md` via MyST `{include}` (one source) or summarise and link | Include, if both builds pass |
| D-8 | Terminology: apply "probabilistic regression" for user-facing text now, or wait for the author answer (Q-5) | Wait if the author round is within weeks; otherwise apply |
| D-9 | Branching: one branch per work package from the latest approved branch; the PO pushes after each approved phase | Approve |
| D-10 | Fix outdated code examples on contributor/agent pages that mirror the official docs (Beta diverges until upstreamed) | Approve, with a divergence list for upstream |
| D-11 … D-15 | See `12-prioritised-improvement-plan.md` (Quick Start toctree scope; Stage labels; fragment policy; author sheet first; internal workflow figure) | See 12 |
