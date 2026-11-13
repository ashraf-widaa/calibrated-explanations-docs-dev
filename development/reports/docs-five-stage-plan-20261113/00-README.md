# CE documentation: integrated learning and reference architecture — plan (Phase 0)

Planning deliverables, 2026-11-13, baseline `a55c7e9d` (= Beta `main`). No
published page was changed.

**Revision 4 (2026-11-13) — binding.** Quick Start (landing and learning pages) contains **no code blocks or mathematical derivations**; executable pages move by toctree (URLs unchanged) to CE in Practice and Software & Integration (`14`). All seven entry points get improvement plans (`15`). WP-1 remains first; nothing else is implemented before separate approval.

**Revision 3 (2026-11-13).** Quick Start **keeps Paths A/B/C**; the five stages are a planning aid only, never a navigation structure. The integrated architecture (three reading levels, prerequisite progression, forward/deeper/across/backward navigation, tutorial + compendium + manual, canonical ownership, audience flexibility) is preserved. Conflicts and their resolution: `13-architecture-reconciliation.md`, which wins over every older statement.

**Revision 2 (2026-11-13, entry-point audit, partly withdrawn).** The PO agreed on an Integrated
Learning and Reference Architecture with **Quick Start as the five-stage
roadmap (Option B)** and **no separate `learning-journey.md`**. Documents
08–12 were added; 02 was rewritten (revision 2); 03, 05 and 06 were updated to
match. Where an older statement conflicts, 02 rev. 2 and 12 win.

| File | Content |
|---|---|
| `01-current-state-audit.md` | Baseline gates, structure, strengths, weaknesses per stage, code-execution audit, risks |
| `02-target-information-architecture.md` | **Rev. 3 — Deliverable E.** Three functions (tutorial, compendium, manual); seven target entry-point trees; Quick Start Paths A/B/C kept; navigation directions; canonical owners |
| `03-content-migration-matrix.md` | Page-by-page action, reason, priority, dependencies, validation |
| `04-interactive-learning-plan.md` | Existing interactive resources and what to reuse, verify or not build |
| `05-phased-implementation-roadmap.md` | Phase framing (work packages superseded by 12) |
| `06-implementation-prompts.md` | Copy-ready Claude Code prompts (mapped to the WPs in 12) |
| `07-quality-and-acceptance-criteria.md` | Gates, scientific and editorial rules, layout checks |
| `08-homepage-entry-point-audit.md` | **Deliverable A.** Seven entry points: verified navigation trees, reader-journey assessment, gaps |
| `09-entry-point-navigation-matrix.md` | **Deliverable B.** Reader goal, current vs proposed path, function, levels, gaps, change classes |
| `10-concept-curriculum-matrix.md` | **Deliverable C.** 46 concepts in prerequisite order with owner, stage, L1/L2/L3 coverage, gaps |
| `11-cross-entry-navigation-matrix.md` | **Deliverable D.** Canonical pages linked from several entry points, with direction and placement |
| `14-quickstart-no-code-migration.md` | **Rev. 4.** Inventory of the 66 code blocks on six Quick Start pages; relocation by toctree (URLs unchanged); code-free Paths B and C; affected files; tests; migration risks; D-18…D-21 |
| `15-entry-point-improvement-plan.md` | **Rev. 4.** Phone-width evidence; shared standards; visualisation programme V-1…V-11; recommendations for all seven entry points; WP-13…WP-18 |
| `13-architecture-reconciliation.md` | **Rev. 3 decision record.** Binding architecture; verified purposes of Paths A/B/C; conflicts R-1…R-12 and resolutions; Quick Start target |
| `12-prioritised-improvement-plan.md` | **Deliverable F.** WP-1…WP-12 with objectives, pages, dependencies, verification, acceptance, risks, effort; sequence; decisions D-11…D-15 |

Phase reports go to `phase-reports/` (created by the first implementation
prompt).

## Decisions requested from the PO

| ID | Decision | Recommendation |
|---|---|---|
| D-1 | ~~Journey page~~ ~~Option B five-stage Quick Start~~ **Withdrawn (rev. 3, R-1):** Quick Start keeps Paths A/B/C; the five stages are a planning aid for concept order only | — |
| D-2 | ~~Journey page links / "Stage n" landing lines~~ **Withdrawn (rev. 3, R-5, R-6)** | — |
| D-3 | New page `explainable-ai.md` in "CE: What & Why" owning black boxes, transparency and XAI limits; ml-foundations keeps A7 (short, L1) and a shortened A6 bridge (rev. 3, R-8) | Approve |
| D-4 | New `calibration_intuition` page under "How CE Works"; relabel the sidebar entry of `calibrated_interval_semantics` from "Calibration & Uncertainty" to "Guarantees by mode" (URL unchanged); retarget the "Can We Trust AI Outputs?" card to the new page | Approve |
| D-5 | Notebooks: link only those that pass the notebook driver; do not edit notebooks (mirrored from the official project) | Approve |
| D-6 | Rewrite `compare.md` as a design comparison with no performance claims | Approve |
| D-7 | Development setup page: include `CONTRIBUTING.md` via MyST `{include}` (one source) or summarise and link | Include, if both builds pass |
| D-8 | Terminology: apply "probabilistic regression" for user-facing text now, or wait for the author answer (Q-5) | Wait if the author round is within weeks; otherwise apply |
| D-9 | Branching: one branch per work package from the latest approved branch; the PO pushes after each approved phase | Approve |
| D-10 | Fix outdated code examples on contributor/agent pages that mirror the official docs (Beta diverges until upstreamed) | Approve, with a divergence list for upstream |
| D-11 | Quick Start toctree keeps only Quick Start-owned pages, in the current A1, A2, B, C1–C5, Quick API order and labels | Approve |
| D-12 | ~~Stage labels~~ **Withdrawn (rev. 3, R-2)** | — |
| D-13 … D-15 | See `12` (fragment policy; author sheet first; internal workflow figure) | See 12 |
| D-16 | Workflow figure on the Quick Start landing: keep a smaller version (≤ ~560 px) as orientation with a link to `why-ce`, or remove it from the landing | Keep smaller (13 R-7) |
| D-17 | Rename the walkthrough's "Optional A/B/C" sections (collide with Paths A/B/C) to "Extra 1/2/3" | Approve |
| D-18 | Path C after the no-code migration: C1 + C2 overview, or C1 + four short code-free pages | C1 + C2 overview |
| D-19 | Quick Start inline code: single identifiers allowed; call expressions and snippets not | Approve |
| D-20 | Moved executable pages keep their `get-started/…` URLs (recommended) or move with redirect stubs | Keep URLs |
| D-21 | Path B = generated, code-free *CE by example*; the executable walkthrough becomes *Python walkthrough* under CE in Practice | Approve |
| D-22 | Approve WP-13…WP-18 for later scheduling (no implementation before separate approval) | Approve for planning |
