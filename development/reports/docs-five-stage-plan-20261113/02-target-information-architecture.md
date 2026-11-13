# 02 — Target information architecture (Deliverable E, revision 2)

**Revision 2 (2026-11-13).** Replaces revision 1. Changes, as agreed by the PO:
Quick Start is the **five-stage roadmap (Option B)**; **no separate
`learning-journey.md`**; the conventional-vs-CE comparison lives on its
canonical conceptual page, distinct from an internal CE workflow diagram; three
reading levels (L1/L2/L3) and four navigation directions (forward, deeper,
across, backward). Evidence: `08-homepage-entry-point-audit.md`.

Tags: **[V]** exists and verified · **[N]** proposed · **[S]** needs author
review. URLs of existing pages are unchanged throughout.

## 1. Three functions, one set of canonical pages

| Function | Purpose | Where it lives | Rule |
|---|---|---|---|
| **Tutorial** | Prerequisite-aware learning sequence | Quick Start (navigator) + Quick Start-owned tutorial pages (ML essentials, Why CE, walkthrough, quickstarts, C5) | Teaches by linking canonical pages in order; owns only tutorial pages |
| **Academic compendium** | Concepts, mathematics, statistics, science | How CE Works, CE: What & Why, Research & Publications | Owns definitions, mechanisms, guarantees, references |
| **Technical reference manual** | Accurate task-oriented use, integration, extension, evaluation | CE in Practice, CE Software & Integration, Project (contributing) | Owns APIs, procedures, configuration, troubleshooting |

A concept is **defined once** (compendium owner), **practised once** (tutorial
or manual owner) and **referenced** everywhere else with a forward, deeper,
across or backward link (`11-cross-entry-navigation-matrix.md`).

## 2. Seven entry-point trees (target)

### 2.1 Quick Start — five-stage roadmap (Option B)

Landing `get-started/index.md` [V → revised]: short definition of CE; **five
stage cards**; "direct routes" for experienced readers; install/API/glossary
line. **No workflow figure on the landing** (it moves to `why-ce` only).

```text
Quick Start  get-started/index.md
├── Stage 1 · Foundations  (core)
│     get-started/ml-foundations ............ [V, revised: AI systems vs models, rule-based vs ML]
│     explainable-ai ........................ [N] (CE: What & Why) black boxes, transparency, XAI and limits
├── Stage 2 · CE concepts  (core)
│     get-started/why-ce .................... [V] conventional vs CE workflow (canonical comparison figure)
│     foundations/concepts/calibration_intuition [N] scores vs probabilities, calibration, uncertainty, interval meaning (L1)
│     get-started/ce-tasks-and-modes ........ [V] task → mode → method → output
│     foundations/concepts/ce_workflow ...... [V, revised: internal CE workflow diagram]
│     foundations/how-to/interpret_explanations [V] factual and alternative explanations
│     what-is-ce ............................ [V] guarantees vs non-guarantees, fit (summary; links semantics)
├── Stage 3 · Using CE  (core)
│     external demo app (no install) → get-started/quickstart_walkthrough [V] → get-started/installation [V]
│     → quickstart_classification / quickstart_regression / quickstart_guarded [V] → apply-to-your-data [V]
│     → practitioner/evaluate_ce [V] → get-started/troubleshooting [V, revised] → get-started/quick_api [V, revised]
├── Stage 4 · Going deeper  (optional)
│     foundations/concepts/calibration_methods [V] → calibrated_interval_semantics [V] → explanation construction
│     (ce_workflow §, explanation_structures [S], alternatives, probabilistic_regression) → foundations/how-to/conditional_calibration
│     → compare [V, rewrite] → researcher/index [V, revised] → researcher/future_work [V, revised]
└── Stage 5 · Contributing  (optional)
      sections/project-evolution → contributor/development_setup [N] → foundations/concepts/architecture
      → contributor/plugin-contract → contributor/extending/guides/index → foundations/governance/test_policy, pr_guide
```

**Sidebar (toctree) of Quick Start.** Only Quick Start-owned pages, relabelled
by stage; pages owned by other sections are linked from the stage cards but
not duplicated in this toctree (avoids two sidebar homes and conflicting
prev/next):

```text
1 · Machine learning essentials       get-started/ml-foundations
2 · Why CE                            get-started/why-ce
2 · Tasks, modes and capabilities     get-started/ce-tasks-and-modes
3 · Guided Python walkthrough         get-started/quickstart_walkthrough
3 · Classification quickstart         get-started/quickstart_classification
3 · Regression quickstart             get-started/quickstart_regression
3 · Guarded explanations              get-started/quickstart_guarded
3 · Apply CE to your own data         get-started/apply-to-your-data
3 · Quick API                         get-started/quick_api
```

Direct routes on the landing: "I know ML → Stage 2"; "I want code now →
walkthrough or C2/C3"; "I have a model → C1 then C5"; "I need the maths →
Stage 4"; "I want to contribute → Stage 5".

Page path labels change from "Path A/B/C, step n" to "Stage n" (in-page labels
and the walkthrough generator).

### 2.2 CE: What & Why (compendium, L1)

```text
sections/what-and-why.md — cards reordered as a progression
├── Understanding AI models ......... → get-started/ml-foundations (across; Quick Start owns it)
├── Black boxes and explainable AI .. explainable-ai.md [N] (owner; absorbs ml-foundations A6–A7, keeps anchor why-predictions-are-not-enough)
├── Can we trust AI outputs? ........ → foundations/concepts/calibration_intuition [N] (across)
├── What CE is and adds ............. what-is-ce.md [V] (owner: contribution, fit, guarantee summary)
├── The explainability gap .......... compare.md [V → rewrite as design comparison]
└── Trustworthy AI (regulation) ..... practitioner/playbooks/eu-ai-act-compliance [V, S: line 478 claim]
Sidebar: Overview · Black boxes and XAI [N] · What CE Is · The Explainability Gap · Trustworthy AI
```

### 2.3 How CE Works (compendium, L1→L3)

```text
sections/how-ce-works.md
Sidebar (reordered; URLs unchanged):
├── Overview
├── Calibration & Uncertainty (intuition) ... foundations/concepts/calibration_intuition [N] (L1)
├── The CE Workflow ......................... foundations/concepts/ce_workflow [V; new internal-mechanism figure] (L1–L2)
├── Statistical Methods Behind CE ........... foundations/concepts/calibration_methods [V] (L2–L3)
├── Guarantees by Mode ...................... foundations/concepts/calibrated_interval_semantics [V; label only] (L3)
├── How Explanations Are Built .............. foundations/concepts/explanation_structures [V, S] + alternatives, probabilistic_regression (L2–L3)
├── How to Read CE Explanations ............. foundations/how-to/interpret_explanations [V; telemetry section → link] (L2)
└── Essential Foundations (hub) ............. foundations/index [V; governance pointer moved to Project]
```

### 2.4 CE in Practice (manual, L2)

```text
sections/in-practice.md — cards: app, Expert Hub, Decision Lab (external, labelled);
  "Apply CE to your own data" → get-started/apply-to-your-data [V] (deeper: integrate_with_pipelines);
  "Example notebooks" → only notebooks verified by the driver [N]; evaluate_ce; tasks
Sidebar unchanged in shape; each cluster gets one owner page with role lines on the others:
  performance → foundations/how-to/tune_runtime_performance · reject → practitioner/advanced/reject-policy
  Mondrian → foundations/how-to/conditional_calibration · telemetry → foundations/how-to/configure_telemetry
Task guides: wording revised where no author question is pending; SR-tied terms marked [S]
```

### 2.5 CE Software & Integration (manual, L2–L3)

```text
sections/software-integration.md — add group "Configuration & operations" (links only:
  configure_runtime, safe-defaults, tune_runtime_performance, configure_telemetry)
├── Software Foundations ......... versions · installation · architecture
├── Development & Integration .... api/index [V; add "main components" overview linking quick_api and autosummary]
│                                  · integrate_with_pipelines · plugins
└── Maintenance & Support ........ troubleshooting [V → canonical error list] · upgrade · migration
Sub-hub pages (16–18 lines) stay as sidebar parents but carry no repeated prose.
```

### 2.6 Project & Resources (compendium + manual for contributors)

```text
Resources: Glossary [V] · Parameter Reference [V]
CE Project, Vision & Evolution:
├── Overview
├── Research & Publications ... researcher/index [V; + research history] → replication · advanced · future_work [V; items labelled]
├── citing · ROADMAP
├── Community & Contributions .. contributor/index [V; ordered path]
│     → contributor/development_setup [N] (includes or summarises CONTRIBUTING.md)
│     → architecture (across, Software) → plugin-contract [V; example fixed] → extending → test_policy, pr_guide
└── Governance & support [V; visibility decision C-33]
```

### 2.7 Commercial Services — keep unchanged

## 3. Navigation directions (applied on every stage and compendium page)

- **Forward:** "Next:" to the next concept in the stage (or next stage).
- **Deeper:** "Go deeper:" to the L3 owner.
- **Across:** "See it in practice:" to the example or reference.
- **Backward:** "Before this:" prerequisite or intuition owner.

Detailed edges: `11-cross-entry-navigation-matrix.md`. Concept order and
owners: `10-concept-curriculum-matrix.md`.

## 4. Canonical owners (summary)

| Topic | Owner | Function |
|---|---|---|
| AI, ML, learning approaches, tasks, model families, data roles | `get-started/ml-foundations` | Tutorial (L1) |
| Black boxes, transparency, XAI and its limits | `explainable-ai` [N] | Compendium (L1) |
| Conventional vs CE workflow (comparison figure) | `get-started/why-ce` | Tutorial (L1) |
| Internal CE workflow (mechanism figure), learning path | `foundations/concepts/ce_workflow` | Compendium (L1–L2) |
| Scores vs probabilities; calibration; uncertainty; interval meaning (intuitive) | `foundations/concepts/calibration_intuition` [N] | Compendium (L1) |
| Task → mode → method → output | `get-started/ce-tasks-and-modes` | Tutorial/manual (L1–L2) |
| Methods (Venn–Abers, conformal, CPS) | `foundations/concepts/calibration_methods` | Compendium (L2–L3) |
| Guarantees and non-guarantees by mode | `foundations/concepts/calibrated_interval_semantics` | Compendium (L3) |
| Explanation construction | `ce_workflow` §(overview) + `explanation_structures` (L3) [S] | Compendium |
| Reading explanations and plots | `foundations/how-to/interpret_explanations` | Manual (L2) |
| Applying to own data / integration | `get-started/apply-to-your-data` / `foundations/how-to/integrate_with_pipelines` | Manual (L2) |
| Evaluation | `practitioner/evaluate_ce` | Manual (L2) |
| Errors | `get-started/troubleshooting` | Manual (L2) |
| API components | `get-started/quick_api` (overview) + autosummary (signatures) | Manual (L2–L3) |
| Development setup and contribution | `contributor/development_setup` [N] + `contributor/index` | Manual (L2) |
| Open questions and limitations | `researcher/future_work` | Compendium (L3) |
