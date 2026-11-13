# 02 — Target information architecture

Planning document. Nothing here is implemented. Baseline: `a55c7e9d`
(= Beta `main`, live). Every path below exists at that commit unless marked
**(new)**.

## 1. Principle: a journey over the existing sections, not a new site

The homepage keeps its seven parts (Quick Start; CE: What & Why; How CE Works;
CE in Practice; CE Software & Integration; Project & Resources; Commercial
Services). The five stages are a **reading order across those sections**.
They are not five new top-level sections. Each stage:

- has **one landing anchor** on a single new journey page;
- lists the existing pages that own its topics, in reading order;
- names its audience, prerequisites and exit point.

Each section landing page states, in one line, which stage(s) it serves. This
keeps every section independently usable while giving beginners an ordered
path.

## 2. The five-stage journey

| Stage | Reader question | Audience | Owning section(s) | Pages, in reading order |
|---|---|---|---|---|
| **1 · Foundations** | What are AI, models and predictions, and why are they hard to trust? | Beginners, students | Quick Start (A1) + CE: What & Why | `get-started/ml-foundations` (revised: AI systems vs models, rule-based AI vs ML, training vs inference, learning approaches, tasks, families, data roles) → **(new)** `explainable-ai.md` (black boxes and transparency, what XAI is, its limits; absorbs ml-foundations A6–A7) |
| **2 · CE concepts** | What does CE add, and how should I read it? | Beginners, decision-makers | Quick Start (A2) + What & Why + How CE Works | `get-started/why-ce` → **(new)** `foundations/concepts/calibration_intuition.md` (scores vs probabilities, reliability, calibration, uncertainty, with real figures) → `what-is-ce` (what CE adds, guarantees and non-guarantees, fit) → `foundations/concepts/ce_workflow` → `foundations/how-to/interpret_explanations` |
| **3 · Using CE** | How do I install, run, read and integrate CE? | Practitioners, developers | Quick Start (B, C) + CE in Practice + Software & Integration | demo app / walkthrough (B) → `get-started/installation` → `get-started/ce-tasks-and-modes` → quickstarts C2–C4 → `get-started/apply-to-your-data` → `get-started/quick_api` (revised: main components) → `foundations/how-to/integrate_with_pipelines` → `practitioner/evaluate_ce` → `get-started/troubleshooting` (revised) → task guides and playbooks as needed |
| **4 · Going deeper** | Why does it work, what exactly is guaranteed, and how is it evaluated? | Advanced users, researchers | How CE Works + Research & Publications | `foundations/concepts/calibration_methods` → `foundations/concepts/calibrated_interval_semantics` → explanation construction (`ce_workflow` §, `explanation_structures`, `alternatives`, `probabilistic_regression`) → `compare` (rewritten: design comparison, no unsupported claims) → `researcher/advanced/theory_and_literature` → `researcher/replication/index` → `researcher/future_work` |
| **5 · Contributing** | How is CE built, tested and extended, and where can I contribute? | Contributors, researchers | Project & Resources + Software & Integration | `sections/project-evolution` → **(new)** `contributor/development_setup.md` (includes `CONTRIBUTING.md`) → `foundations/concepts/architecture` → `contributor/plugin-contract` and `contributor/extending/guides/index` → `foundations/governance/test_policy` and `pr_guide` → `researcher/future_work` (verified limitations vs proposed research) |

## 3. Quick Start child-page hierarchy (keep v3, small changes)

The v3 Quick Start already implements A/B/C and is live. It stays the
**condensed** entry; the journey page is the **full** route.

```text
Quick Start — Understand, Explore and Apply CE          get-started/index
├── A1 · Machine learning essentials                       get-started/ml-foundations   (trimmed to ML essentials; A6–A7 move to Stage 1 XAI page)
├── A2 · Why CE: from a conventional to a CE workflow      get-started/why-ce           (unchanged role; links calibration_intuition)
├── B  · Guided Python walkthrough                         get-started/quickstart_walkthrough  (generated; unchanged role)
├── C1 · Tasks, modes and capabilities                     get-started/ce-tasks-and-modes
├── C2 · Classification quickstart                         get-started/quickstart_classification
├── C3 · Regression quickstart                             get-started/quickstart_regression
├── C4 · Guarded explanations                              get-started/quickstart_guarded
├── C5 · Apply CE to your own data                         get-started/apply-to-your-data
└── Quick API → "Main components and calls"                get-started/quick_api       (revised, same URL)
```

The Quick Start landing gets one added line: "For the full five-stage route,
see the learning journey." No other structural change.

## 4. Mapping to the homepage cards

| Homepage part | Stage(s) | Change |
|---|---|---|
| Quick Start | 1 (A1), 2 (A2), 3 (B, C) | One link to the journey page |
| CE: What & Why | 1, 2 | Add `explainable-ai` to the sidebar group; landing card "Understanding AI Models" keeps → ml-foundations; card "Can We Trust AI Outputs?" → `calibration_intuition` |
| How CE Works | 2, 4 | Add `calibration_intuition` before the semantics page; relabel the semantics entry "Guarantees by mode" (URL unchanged) — **PO decision** |
| CE in Practice | 3 | Unchanged structure; cards already list demos, notebooks, evaluation |
| CE Software & Integration | 3, 5 | `quick_api` revision and troubleshooting are linked from the landing; no moves |
| Project & Resources | 4, 5 | `contributor/development_setup` (new) in the Community group; research hub gains a "Research history" list (existing citations) |
| Commercial Services | — | Unchanged |

**Journey page placement — PO decision.** Recommended: `docs/learning-journey.md`
**(new)**, linked from (1) the homepage hero hint line, (2) the Quick Start
landing, (3) each section landing ("This section is Stage N of the learning
journey"). It sits in the sidebar directly under Quick Start. Alternative: only
section-landing links, no sidebar entry.

## 5. Primary content ownership (one owner per topic)

| Topic | Canonical owner | Others must link, not restate |
|---|---|---|
| AI, ML, learning approaches, tasks, model families, data roles | `get-started/ml-foundations` | why-ce, what-is-ce, glossary |
| Black boxes, transparency, what XAI is and its limits | `explainable-ai` **(new)** | ml-foundations, what-is-ce, compare |
| Conventional vs CE workflow; reading one CE output | `get-started/why-ce` | ce_workflow, landing |
| Scores vs probabilities; calibration; uncertainty (intuition) | `foundations/concepts/calibration_intuition` **(new)** | ml-foundations A6 (removed), why-ce, ce-tasks-and-modes |
| What CE adds, guarantees vs non-guarantees, when it fits | `what-is-ce` | why-ce (one-line pointers) |
| Mode semantics (formal) | `foundations/concepts/calibrated_interval_semantics` | all quickstarts (semantics notes point here, per STD-004) |
| How CE calibrates (methods, maths) | `foundations/concepts/calibration_methods` | ce_workflow, tasks pages |
| How explanations are built | `foundations/concepts/ce_workflow` §"How an explanation is built" (overview) and walkthrough §6 (worked) | interpret_explanations |
| Reading explanations and plots | `foundations/how-to/interpret_explanations` | quickstarts ("Reading the plot" stays short and links here) |
| Task/mode choice | `get-started/ce-tasks-and-modes` | tasks/index (reference), quick_api, task_api_comparison |
| Evaluating CE on your data | `practitioner/evaluate_ce` | C5, walkthrough |
| Errors and fixes | `get-started/troubleshooting` | C5 "Common problems" (keeps a short table + link) |
| Development setup and tests | `contributor/development_setup` **(new)**, including `CONTRIBUTING.md` | contributor hub |
| Performance, reject, plugins, Mondrian, telemetry clusters | as in Report C (C-23…C-28) of `learning-reports/2026-11-12_0910_L06-FULL-DOCS-REVIEW-A-E.md` | — (Phase 6 housekeeping) |

## 6. Cross-reference strategy

- **Forward and back at page edges.** Each journey page ends with "Next" (the
  next stage page) and starts with "You are in Stage N" plus its prerequisite.
- **Concept on first use.** First use of a defined term links once to its owner
  page or the glossary (`{term}` roles exist, per G-P3).
- **Depth links, not depth text.** Beginner pages end sections with "Go deeper:"
  to the Stage 4 owner; Stage 4 pages start with "Intuition first:" back to the
  Stage 2 owner.
- **No restated guarantees.** Any page that mentions a guarantee links the
  semantics page instead of paraphrasing it (existing STD-004 rule).

## 7. Research and contributor pathway

Researchers: Stage 2 (intuition) → Stage 4 (methods → semantics → explanation
construction → evaluation/comparison → literature → replication → open
questions). Contributors: Stage 3 (use the API) → Stage 5 (setup → architecture
→ extension contracts → tests and PR guide). The two meet at
`researcher/future_work`, which must label each item **verified limitation**,
**open question to authors** or **proposed extension**.
