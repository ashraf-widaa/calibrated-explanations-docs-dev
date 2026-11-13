# 03 — Content migration matrix

Scope: every page the plan touches, plus each page group's status. Pages not
listed keep their place and content (action **Keep**). No URL changes are
proposed; new pages get new URLs; no page is deleted.

Priority: **P1** blocks a stage's learning goal; **P2** quality or friction;
**P3** housekeeping. "Val." = validation (gate numbers in 07 §1; S-rules in 07 §2).

## Stage 1 — Foundations

| Existing path | Current purpose | Audience | Destination | Action | Reason | Pri | Depends on | Val. |
|---|---|---|---|---|---|---|---|---|
| `get-started/ml-foundations.md` | ML essentials A1–A7 (Quick Start A1) | Beginners | same | **Revise / Split** | Add AI systems vs models and rule-based vs ML (missing); move A6–A7 to the XAI page (A6 duplicates why-ce §1; A6 ends with a stale "next page" pointer) | P1 | 1b, D-3 | builds, links, S1–S3 |
| — | — | Beginners | `explainable-ai.md` **(new)** | **New (Merge from A6–A7)** | Black boxes, transparency, XAI and its limits have no owner | P1 | 2a | S3, S4, S8, wording test |
| `sections/what-and-why.md` | Section landing | All | same | **Revise** | Add card for the XAI page; stage line | P2 | 1a, 2a | landing tests |
| `glossary/science.md` | Definitions with "Taught in" links | All | same | **Cross-reference** | Retarget links that point at A6/A7 | P2 | 2a | glossary tests |

## Stage 2 — CE concepts

| Existing path | Current purpose | Audience | Destination | Action | Reason | Pri | Depends on | Val. |
|---|---|---|---|---|---|---|---|---|
| `get-started/why-ce.md` | Conventional vs CE workflow, reading an output (Quick Start A2) | Beginners | same | **Keep / Cross-reference** | Owner of workflow difference; add one link to calibration intuition; guarantees → pointer | P2 | 2b, 2c | builds |
| — | — | Beginners, decision-makers | `foundations/concepts/calibration_intuition.md` **(new)** | **New** | No L1 page explains scores vs probabilities, reliability and uncertainty; the sidebar "Calibration & Uncertainty" opens the formal semantics page | P1 | 2b, D-4 | S5–S7, generator test, 07 §4 |
| `what-is-ce.md` | Problem, what CE adds, guarantees, fit, comparison | Decision-makers | same | **Revise (dedupe)** | "The problem" restates why-ce/A6 | P2 | 2c | `test_what_is_ce.py` |
| `foundations/concepts/ce_workflow.md` | Whole picture + learning path | Learners | same | **Keep** | Already owner of the overview and levels | — | 4a (links) | journeys test |
| `foundations/how-to/interpret_explanations.md` | Reading explanations and plots | Users | same | **Keep / Cross-reference** | Owner of plot reading; quickstarts link it | P3 | 4a | plot-colour test |
| `sections/how-ce-works.md` | Section landing | All | same | **Revise** | Card for calibration intuition; stage line | P2 | 1a, 2b | landing tests |

## Stage 3 — Using CE

| Existing path | Current purpose | Audience | Destination | Action | Reason | Pri | Depends on | Val. |
|---|---|---|---|---|---|---|---|---|
| `get-started/index.md` | Quick Start landing (v3) | All | same | **Revise (one line)** | Link the journey page | P2 | 1a | continuity tests |
| `get-started/quickstart_walkthrough.md` | Generated walkthrough (Path B) | Learners | same | **Keep** | Verified; edit only via generator | — | — | generator, PROSE guard |
| `get-started/ce-tasks-and-modes.md` | Mode choice, outputs, capabilities (C1) | Practitioners | same | **Keep** | Owner of mode choice | — | — | continuity tests |
| `get-started/quickstart_{classification,regression,guarded}.md`, `apply-to-your-data.md` | Executed quickstarts (C2–C5) | Practitioners | same | **Keep** | Verified outputs and plots | — | — | execution tests |
| `get-started/quick_api.md` | Call list with semantics notes | Practitioners | same (retitled) | **Revise** | No component overview; Stage 3 "main components" missing | P1 | 3a | S9, execution test |
| `get-started/troubleshooting.md` (25 lines) | Environment troubleshooting | Practitioners | same | **Revise (Merge)** | Verified user-facing errors are scattered (C5, guarded quickstart) | P1 | 3b | reproduction tests |
| `get-started/installation.md` | Install (states Python ≥ 3.10) | Practitioners | same | **Keep** | Correct | — | — | — |
| `sections/in-practice.md` | Demos, notebooks, evaluation | Practitioners | same | **Revise** | Link only verified notebooks; stage line | P2 | 1a, 3c | link check |
| `tasks/classification.md`, `tasks/probabilistic_regression.md` | Task guides | Practitioners | same | **Revise (wording)** | Causal/undefined terms (C-17) | P2 | 3e, SR-07/SR-08 | wording test |
| `tasks/regression.md`, `tasks/index.md`, `tasks/capabilities.md` | Task guides, capability manifest | Practitioners | same | **Keep / Cross-reference** | Mode routing owner is C1 | P3 | 3c | — |
| Pages flagged by the execution audit (01 §4) | various | Users | same | **Revise (code)** | Examples fail against current API or are unrunnable fragments | P1–P2 | 3d | execution tests |
| `foundations/how-to/integrate_with_pipelines.md` | Pipeline integration | Developers | same | **Keep / Cross-reference** | Linked from C5 and Software | — | — | — |
| `practitioner/evaluate_ce.md` | Evaluation guide | Practitioners | same | **Keep** | Owner of evaluation | — | — | — |

## Stage 4 — Going deeper

| Existing path | Current purpose | Audience | Destination | Action | Reason | Pri | Depends on | Val. |
|---|---|---|---|---|---|---|---|---|
| `foundations/concepts/calibration_methods.md` (683 l.) | Methods and derivations (ADD-1) | Advanced | same | **Cross-reference** | Add "Intuition first" link | P2 | 4a | builds |
| `foundations/concepts/calibrated_interval_semantics.md` | Canonical guarantees | Advanced | same (sidebar label per D-4) | **Cross-reference** | Beginners land on it from "Calibration & Uncertainty" | P1 | 2b, D-4 | STD-004 tests |
| `foundations/concepts/{explanation_structures,alternatives,probabilistic_regression}.md` | Explanation and regression detail | Advanced | same | **Cross-reference** | Two-way links; C-37 stays blocked | P2 | 4a | — |
| `compare.md` (20 l.) | Checklist vs SHAP/LIME/conformal | Decision-makers, researchers | same | **Revise (rewrite)** | Thin; unsupported "more stable rules" (C-19) | P2 | 4b, SR-05/06 | superiority-phrase test |
| `researcher/index.md` | Researcher hub | Researchers | same | **Revise** | No research history | P2 | 4c | — |
| `researcher/future_work.md` | Open directions | Researchers, contributors | same | **Revise** | Items not labelled verified/open/proposed | P2 | 4c | tag test |
| Nine pages with "exchangeable or distribution-matched" (01 §3) | Semantics notes etc. | All | same | **Revise — blocked** | C-18; needs author answer (SR-01/Q-6) | P1 (blocked) | authors | — |

## Stage 5 — Contributing

| Existing path | Current purpose | Audience | Destination | Action | Reason | Pri | Depends on | Val. |
|---|---|---|---|---|---|---|---|---|
| — (`CONTRIBUTING.md`, repo root, 187 l.) | Dev install, extras, tests | Contributors | `contributor/development_setup.md` **(new)** | **New (include or summarise)** | No setup page in the docs | P1 | 5, D-7 | both builds |
| `contributor/index.md` (40 l.) | Contributor hub | Contributors | same | **Revise** | No ordered path; references unreachable maintainer files | P1 | 5 | link check |
| `foundations/concepts/architecture.md` (429 l.) | Internal architecture | Contributors | same | **Revise (intro only)** | No reading guide | P3 | 5 | — |
| `sections/project-evolution.md` | Section landing | All | same | **Revise** | Stage line | P3 | 1a | landing tests |

## Housekeeping (Phase 6)

| Existing path(s) | Action | Reason | Pri | Depends on |
|---|---|---|---|---|
| Performance cluster (C-23), reject (C-24), plugins (C-25), Mondrian (C-27), telemetry (C-28) | **Cross-reference** (owner + role lines) | Overlap without owners | P3 | 6a |
| 16 pages with "thresholded regression" (C-31) | **Revise (wording)** | Terminology policy | P3 | 6b, D-8 |
| `foundations/governance/release_notes.md` (latest v0.10.2) (C-03) | **Revise → pointer** | Stale | P2 | 6b |
| `getting_started_60s.md`, `multiclass_all_classes_gap_analysis.md` | **Keep (orphans)** | Redirect stub; internal analysis | — | — |
| `learning-journey.md` **(new)** | **New** | Five-stage route | P1 | 1a, D-1, D-2 |
