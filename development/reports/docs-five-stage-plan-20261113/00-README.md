# CE documentation: five-stage learning journey — plan (Phase 0)

Planning deliverables, 2026-11-13, baseline `a55c7e9d` (= Beta `main`). No
published page was changed.

| File | Content |
|---|---|
| `01-current-state-audit.md` | Baseline gates, structure, strengths, weaknesses per stage, code-execution audit, risks |
| `02-target-information-architecture.md` | Five stages over the existing sections, Quick Start hierarchy, homepage mapping, topic owners, cross-reference strategy |
| `03-content-migration-matrix.md` | Page-by-page action, reason, priority, dependencies, validation |
| `04-interactive-learning-plan.md` | Existing interactive resources and what to reuse, verify or not build |
| `05-phased-implementation-roadmap.md` | Phases 1–6 split into work packages |
| `06-implementation-prompts.md` | One copy-ready Claude Code prompt per work package |
| `07-quality-and-acceptance-criteria.md` | Gates, scientific and editorial rules, layout checks |

Phase reports go to `phase-reports/` (created by the first implementation
prompt).

## Decisions requested from the PO

| ID | Decision | Recommendation |
|---|---|---|
| D-1 | Adopt the journey model: five stages as a reading order over the existing sections (no new top-level sections) | Approve |
| D-2 | Where the journey page is linked: sidebar entry under Quick Start + homepage hero hint line + section landings | Approve all three; minimum = section landings + Quick Start |
| D-3 | New Stage 1 page `explainable-ai.md` in "CE: What & Why", taking over ml-foundations A6–A7 | Approve |
| D-4 | New `calibration_intuition` page under "How CE Works"; relabel the sidebar entry of `calibrated_interval_semantics` from "Calibration & Uncertainty" to "Guarantees by mode" (URL unchanged); retarget the "Can We Trust AI Outputs?" card to the new page | Approve |
| D-5 | Notebooks: link only those that pass the notebook driver; do not edit notebooks (mirrored from the official project) | Approve |
| D-6 | Rewrite `compare.md` as a design comparison with no performance claims | Approve |
| D-7 | Development setup page: include `CONTRIBUTING.md` via MyST `{include}` (one source) or summarise and link | Include, if both builds pass |
| D-8 | Terminology: apply "probabilistic regression" for user-facing text now, or wait for the author answer (Q-5) | Wait if the author round is within weeks; otherwise apply |
| D-9 | Branching: one branch per work package from the latest approved branch; the PO pushes after each approved phase | Approve |
| D-10 | Fix outdated code examples on contributor/agent pages that mirror the official docs (Beta diverges until upstreamed) | Approve, with a divergence list for upstream |
