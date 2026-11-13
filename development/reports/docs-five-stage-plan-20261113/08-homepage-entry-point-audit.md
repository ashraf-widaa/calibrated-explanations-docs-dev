# 08 — Homepage entry-point audit (Deliverable A)

Planning document. Baseline `8fedaf4d` (docs identical to Beta `main`
`a55c7e9d`). Navigation trees were extracted from the toctree directives of the
source (script output, 2026-11-13), not from memory.

Status tags: **[V]** existing and verified · **[P!]** existing but incomplete or
problematic · **[N]** proposed · **[S]** requires scientific or technical
verification (author review).

Reading levels: **L1** conceptual · **L2** practical · **L3** mathematical,
technical, research.

---

## 1. Quick Start

**Reader goal (current).** Newcomers and practitioners: understand CE, see it
run, apply it. **Landing:** `docs/get-started/index.md` (Tier 1). **Homepage
link:** hero button "Quick Start".

### A. Current navigation tree [V]

```text
Homepage hero button "Quick Start"
└── get-started/index.md  "Quick Start — Understand, Explore and Apply CE"
    │   sections: Where CE fits (conventional-vs-CE workflow figure) · Choose your path (cards A, B, C) · Before you start
    ├── A1 · Machine learning essentials ............ get-started/ml-foundations.md      (L1; A1–A7)
    ├── A2 · Why CE: from a conventional to a CE workflow  get-started/why-ce.md       (L1; two figures)
    ├── B  · Guided Python walkthrough .............. get-started/quickstart_walkthrough.md (L1→L2; generated, verified)
    ├── C1 · Tasks, modes and capabilities ........... get-started/ce-tasks-and-modes.md  (L1–L2; mode cards, semantics summary)
    ├── C2 · Classification quickstart ............... get-started/quickstart_classification.md (L2; executed + plot)
    ├── C3 · Regression quickstart ................... get-started/quickstart_regression.md    (L2; executed)
    ├── C4 · Guarded explanations .................... get-started/quickstart_guarded.md       (L2; executed + plot)
    ├── C5 · Apply CE to your own data ............... get-started/apply-to-your-data.md      (L2; executed + plot, AI-assistant prompt)
    └── Quick API .................................... get-started/quick_api.md               (L2; fragments, not executed)
    Cross-links from the landing: installation, quick_api, glossary, api/index, ce_workflow,
    calibrated_interval_semantics, external demo app.
    Not in this toctree but in get-started/: installation, troubleshooting (Software section),
    ce_first_agent_guide, copilot-setup (Project section).
```

### B. Reader-journey assessment

| Question | Finding |
|---|---|
| Purpose clear? | Yes [V] |
| Starting point clear? | Yes: recommended order A → B → C [V] |
| Logical sequence? | Mostly [V]; A1 A6 ends with a stale "next page" sentence [P!] |
| Prerequisites stated? | On A2, B, C1 [V]; not as a stage model [P!] |
| L1/L2/L3 access? | L1, L2 strong; L3 only via two landing links [P!] |
| Examples? | Executed and output-checked [V] |
| Deeper material? | No stage-level route to Venn–Abers, CPS, semantics, research [P!] |
| Other sections? | No route to Stage 5 (contributing) [P!] |
| Return path? | Sidebar and prev/next work [V] |

**Gaps (rev. 3).** No "Where should I go next?" route to the other six entry
points; six of nine pages have no deeper link to the methods page; no route
to contributing; the comparison figure is large on the landing (D-16); the
walkthrough's "Optional A/B/C" collides with Paths A/B/C; black boxes/XAI
and a calibration-intuition page do not exist (owned by other sections).
Paths are goal-based, not level-based (`13` §2).

### C. Proposed target tree — see `13` §5 and `02` rev. 3 §2.1. Change classes: **Keep** (A/B/C structure, order, labels), **Revise** (landing: "Where should I go next?"; figure per D-16), **Add cross-link** (Next / Go deeper / See also / Before this on every page), **Revise** (walkthrough optional-section names via generator), **Create missing content** (XAI and calibration-intuition pages, owned by other sections).

---

## 2. CE: What & Why

**Reader goal.** Decision-makers, students: why trust is hard, what CE adds.
**Landing:** `docs/sections/what-and-why.md` (Tier 3).

### A. Current navigation tree [V]

```text
Homepage card "CE: What & Why"
└── sections/what-and-why.md  (5 cards)
    ├── card "Understanding AI Models" ........ → get-started/ml-foundations.md (Quick Start page)
    ├── card "Can We Trust AI Outputs?" ........ → ref why-predictions-are-not-enough (ml-foundations A6)
    ├── card "Trustworthy AI" .................. → practitioner/playbooks/eu-ai-act-compliance.md
    ├── card "The Explainability Gap" .......... → compare.md (20 lines)
    └── card "What Is CE & What Does It Add?" .. → what-is-ce.md
Sidebar group "CE: What & Why": Overview · What CE Is · Trustworthy AI (= EU AI Act playbook) · The Explainability Gap (= compare)
```

### B. Assessment

- Purpose and start: clear [V]. Sequence: cards are not ordered as a progression [P!].
- Two cards leave the section for Quick Start pages; fine as cross-entry links, but the section has **no own L1 page on black boxes, transparency or XAI** [P!] — the concept locator finds "black box" only on a compliance playbook and "XAI" only on `citing`.
- "Trustworthy AI" opens a long regulatory playbook (`eu-ai-act-compliance.md`) whose line 478 states "Empirical coverage vs. nominal confidence (Venn-Abers guarantee) — **Covered**" [S]: conflates coverage, confidence and Venn–Abers, and asserts compliance coverage.
- `compare.md` is thin with an unsupported "more stable rules" [P!][S].
- `what-is-ce` "The problem" overlaps `why-ce` and A6 [P!].

### C. Target — 12 §2.2: **Create missing content** (`explainable-ai.md`), **Reorder** cards as a progression (AI models → XAI and its limits → trust and calibration → what CE adds → comparison → regulation context), **Revise** compare, **Requires author review** (regulatory claims).

---

## 3. How CE Works: The Theory Behind It

**Reader goal.** Learners and researchers: mechanisms, methods, guarantees.
**Landing:** `docs/sections/how-ce-works.md` (Tier 3).

### A. Current navigation tree [V]

```text
Homepage card "How CE Works"
└── sections/how-ce-works.md (6 cards: workflow, foundations, calibration & uncertainty, methods, reading explanations, assumptions & guarantees → anchor)
Sidebar group:
    ├── Overview ............................... sections/how-ce-works.md
    ├── The CE Workflow ........................ foundations/concepts/ce_workflow.md (L1–L3 learning path; uses the conventional-vs-CE figure)
    ├── Essential Foundations .................. foundations/index.md (hub of links: beginner, practical, scientific, architecture, governance)
    │   └── Concepts & architecture ............ foundations/concepts/index.md
    │       ├── alternatives.md · error_handling.md · explanation_structures.md · guarded_explanations.md
    │       └── probabilistic_regression.md · terminology_thresholded_vs_probabilistic_regression.md
    ├── Calibration & Uncertainty .............. foundations/concepts/calibrated_interval_semantics.md (L3 canonical semantics)
    ├── Statistical Methods Behind CE .......... foundations/concepts/calibration_methods.md (L2–L3, 683 lines, executed examples, exercises)
    └── How to Read CE Explanations ............ foundations/how-to/interpret_explanations.md (L2)
```

### B. Assessment

- Strong L3 [V]: methods page with derivations, exercises, references; canonical semantics.
- **No L1 page for calibration and uncertainty** [P!]: the sidebar label "Calibration & Uncertainty" opens the formal semantics (Tier 3).
- `ce_workflow` uses the **same** figure as the Quick Start landing (conventional vs CE). The *internal* CE workflow (calibrate → perturb → weights → ranges) has no diagram [P!].
- "Essential Foundations" mixes audiences (beginner, practical, scientific, architecture, governance) [P!] (Report C-22).
- `interpret_explanations` §4 "Tie everything back to telemetry" is an operations topic inside a reading guide [P!].
- `explanation_structures` mixes L3 internals (rules payload) with filter semantics that are blocked on author questions (C-37) [S].
- `calibration_methods` §4 heading uses "thresholded regression" (terminology policy: user-facing = probabilistic) [P!].

### C. Target — 12 §2.3: **Create missing content** (`calibration_intuition.md`, internal-workflow figure), **Reorder** (intuition → workflow → methods → semantics → explanation construction → reading), **Revise** sidebar labels (URLs unchanged), **Relocate content** (telemetry section → link), **Requires author review** (C-37).

---

## 4. CE in Practice: Explore & Apply

**Reader goal.** Practitioners: try, apply, evaluate. **Landing:**
`docs/sections/in-practice.md`.

### A. Current navigation tree [V]

```text
Homepage card "CE in Practice"
└── sections/in-practice.md (7 cards: Interactive CE App [ext], Expert Hub [ext], Decision Lab Games [ext],
    Use CE on your own data → integrate_with_pipelines, Example notebooks [GitHub folder],
    Evaluate CE → practitioner/evaluate_ce, Tasks and capabilities → tasks/index)
Sidebar group:
    ├── Overview
    ├── Tasks and capabilities ......... tasks/index.md → classification · regression · probabilistic_regression · capabilities
    ├── Practitioner hub ............... practitioner/index.md
    │   ├── evaluate_ce · task_api_comparison
    │   ├── Practitioner playbooks ..... mondrian-calibration · ensured-explanations · decision-policies · eu-data-liability-compliance
    │   ├── Practitioner advanced ...... use_plugins · modality-plugins · normalization-guide · reject-policy · parallel_execution_playbook
    │   │                                · explanation_retrieval · telemetry (relocated stub) · performance-tuning
    │   └── narrative_templates
    └── How-to guides .................. foundations/how-to/index.md → configure_telemetry · configure_runtime · conditional_calibration
                                         · safe-defaults · export_explanations · to_narrative · plot_with_plotspec · tune_runtime_performance
```

### B. Assessment

- Clear card set, honest labels on external tools [V].
- "Use CE on your own data" card targets `integrate_with_pipelines`; the Quick Start now has `apply-to-your-data` (C5) — two owners for one task [P!].
- Task guides: wording issues — "counterfactuals", "epistemic and aleatoric envelopes", "necessary to flip" (`tasks/classification.md:23,44,52`), "arbitrary confidence levels" for percentiles (`tasks/regression.md:58`) [S].
- Ensured playbook: epistemic/aleatoric table and "more reliable intervention recommendations" [S] (SR-07/SR-08).
- Execution audit: 32 practice pages are non-runnable fragments; `explanation_retrieval` uses `expl.factual` (not in `src/`) and an indented block; `configure_runtime` blocks 0→1 fail in sequence [P!].
- Overlapping clusters without owners: performance (3 pages), reject (3), Mondrian (2), telemetry (3) [P!].
- 18 repository notebooks unverified [P!].

### C. Target — 12 §2.4: **Revise** "own data" card → C5 with integration as the deeper link; **Requires author review** (task-page and ensured wording); **Merge duplicate content** (cluster owners); **Revise** code (Phase 3d).

---

## 5. CE Software & Integration

**Reader goal.** Developers: install, call, integrate, extend, maintain.
**Landing:** `docs/sections/software-integration.md` (128 lines, grouped cards).

### A. Current navigation tree [V]

```text
Homepage card "CE Software & Integration"
└── sections/software-integration.md (groups: Software Foundations · Development & Integration · Maintenance & Support)
Sidebar group:
    ├── Overview
    ├── Software Foundations (16-line sub-hub) → software-overview-versions (→ appendices/changelog_links) · get-started/installation · foundations/concepts/architecture
    ├── Development & Integration (18-line sub-hub) → api/index (→ calibrated_explainer · cli · plugins · serialization · visualization · foundations/reference/index → api (autosummary) · schema_v1)
    │                                                · foundations/how-to/integrate_with_pipelines · plugins (→ appendices/external_plugins)
    └── Maintenance & Support (16-line sub-hub) → get-started/troubleshooting · upgrade/index (3 checklists) · migration/index (deprecations · adr033 · terminology)
```

### B. Assessment

- Complete reference set [V]; autosummary pages render signatures [V].
- **No "main components" overview**: `api/index` is 16 lines of links; `quick_api` (Quick Start) lists calls as fragments [P!].
- Troubleshooting is 25 lines (environment only) [P!].
- Two hub layers (landing + 16-line sub-hubs) repeat each other (C-30) [P!].
- Configuration pages (configure_runtime, safe-defaults, tune_runtime_performance, configure_telemetry) live under CE in Practice → How-to; developers look here (C-29) [P!].
- `api/index.md` nests a second hub, `foundations/reference/index.md` (→ `api.md` autosummary, `schema_v1`): two reference layers under one card [P!].

### C. Target — 12 §2.5: **Create missing content** (components overview in `quick_api`/`api/index`), **Revise** troubleshooting, **Add cross-link** group "Configuration & operations", **Merge duplicate content** (sub-hubs become link lists only).

---

## 6. Project & Resources

**Reader goal.** Researchers, contributors, everyone: project, research,
terms, licence. **Homepage:** a row of four items (Project, Glossary, GitHub,
Licence); the sidebar has two groups ("Resources", "CE Project, Vision &
Evolution").

### A. Current navigation tree [V]

```text
Homepage "Project & Resources"
├── CE Project, Vision & Evolution → sections/project-evolution.md (6 cards: README [ext], research, roadmap, community, ecosystem → plugins, support & feedback [ext])
├── Glossary → glossary/index.md → science.md · software.md
├── GitHub Repository [ext, official]
└── BSD-3-Clause License [ext, official]
Sidebar "Resources": Glossary · Parameter Reference (foundations/concepts/parameter-reference)
Sidebar "CE Project, Vision & Evolution":
    ├── Overview · Research & Publications (researcher/index → replication/index · advanced/index (theory_and_literature, difficulty_normalized_reject) · future_work)
    ├── citing · Development & Roadmap (ROADMAP) · Community & Contributions (contributor/index → 11 pages incl. agent guides, legacy plotting)
    └── Governance & support (foundations/governance/index → 9 pages) · RTD tier map
```

### B. Assessment

- Glossary strong [V]. Research hub is short; no research history; future_work items unlabelled [P!].
- **Contributor path missing**: no development-setup page (`CONTRIBUTING.md` not rendered), hub references maintainer-only files [P!].
- Execution audit: `plugin-contract` (missing `data_modalities`), `plugin-advanced-contract` (removed private import), `ce_first_agent_guide` (`ensure_coverage`/`ensure_order` do not exist) — outdated [P!].
- Internal governance pages and the tier map in public navigation (C-33) — needs a visibility decision [P!].

### C. Target — 12 §2.6: **Create missing content** (development setup; research history), **Revise** contributor path, **Requires author review** (future_work labels where SR items apply).

---

## 7. Commercial Services

**Reader goal.** Organisations seeking support. **Homepage:** one item "Contact
Grejna AB" → `https://grejna.ai/#kontakt` with the statement that it is separate
from the open-source library and licence [V]. No sidebar entry, no child pages.

**Assessment.** Fit for purpose; clearly separated [V]. No documentation
navigation is needed. **Target:** **Keep** unchanged.
