# 05 — Phased implementation roadmap

> **Revision 2 (2026-11-13).** The authoritative work-package list is now
> `12-prioritised-improvement-plan.md` (WP-1…WP-12). Phase 1 below is
> replaced by WP-1 (Quick Start as the five-stage roadmap, Option B; no
> `learning-journey.md`). Phases 2–6 keep their framing; their work packages
> map to WP-2…WP-12 as listed in `06` (prompt index).

Each phase is split into **work packages** (WP), one reviewable change and one
copy-ready prompt each (06). Work packages within a phase run in the listed
order; a phase starts only after the PO approves the previous one. Complexity:
S (≤ 2 pages, ≤ half a day), M (3–5 pages or a new figure), L (new page with
executed content, or a cluster).

Gates and rules referenced as §n are in `07-quality-and-acceptance-criteria.md`.

---

## Phase 0 — Baseline and audit (this delivery)

| Field | Content |
|---|---|
| Objective | Inventory the docs, verify the build, identify risks; produce documents 01–07 |
| Files affected | New: `development/reports/docs-five-stage-plan-20261113/01…07` only |
| Deliverables | Audit, architecture, migration matrix, interactive plan, roadmap, prompts, criteria |
| Acceptance | PO approves architecture (02) and roadmap (05), and answers the decisions in 01 §6 / the summary |
| Tests | None changed; baseline gates recorded in 01 |
| Risks | Audit coverage is static plus one execution pass; notebooks not run |
| Complexity | — |
| Approvals | D-1…D-8 (see the decision list) |

---

## Phase 1 — Quick Start as the five-stage roadmap (= WP-1)

**Objective.** Make the Quick Start landing the concise five-stage roadmap
(Stages 1–3 core, 4–5 optional) with direct routes; relabel Quick Start-owned
pages by stage; move the conventional-vs-CE figure to `why-ce` only; fix the
stale pointer in ml-foundations A6. No `learning-journey.md`.

Details, acceptance, risks: `12-prioritised-improvement-plan.md` WP-1.
Prompt: `06` Prompt 1.

---

## Phase 2 — Foundations and CE concepts

**Objective.** Fill the Stage 1–2 gaps with accessible, correct pages and
remove the conceptual duplication between A1, A2 and *What CE Is*.

| WP | Change | Files | Complexity |
|---|---|---|---|
| 2a | Stage 1 completion: AI systems vs models; rule-based AI vs ML; black boxes and transparency; what XAI is and its limits | `get-started/ml-foundations.md` (add A0 "AI systems and AI models", rule-based vs ML in A1; remove A6–A7 after moving); **new** `docs/explainable-ai.md` (absorbs A6–A7, adds black-box/transparency and XAI limits); `docs/index.md` toctree (What & Why group); `sections/what-and-why.md` card targets; `why-predictions-are-not-enough` label preserved by moving the anchor to the new page | L |
| 2b | Calibration and uncertainty intuition with real figures | **new** `docs/foundations/concepts/calibration_intuition.md`; **new** generator `scripts/docs/build_concept_figures.py` (reliability diagram raw vs calibrated and one interval figure, from the walkthrough data); `docs/index.md` (How CE Works group, label decision D-4); `sections/how-ce-works.md`; `get-started/why-ce.md` (one link) | L |
| 2c | Ownership clean-up between why-ce and what-is-ce | `docs/what-is-ce.md` ("The problem" shortened to a pointer to why-ce/explainable-ai); `docs/get-started/why-ce.md` ("What CE needs" stays; guarantees → one-line link to what-is-ce) | S |

- **Dependencies:** Phase 1; D-3 (new What & Why page), D-4 (sidebar label).
- **Acceptance:** S1–S8 (07 §2) hold; the anchor `why-predictions-are-not-enough`
  still resolves (the What & Why card uses it); the glossary single-link tests
  still pass; figures pass §4.
- **Tests:** execution test for any code; wording tests (no "all models are
  black boxes", no "calibration guarantees correct predictions");
  generator re-run test for concept figures (numbers in prose present in the
  generated data, like `PROSE_NUMBERS`).
- **Risks:** moving A6–A7 breaks inbound links (`{ref}` labels, glossary
  "Taught in" links) — search and update in the same commit; the walkthrough
  generator links `ml-foundations.md` — check.

---

## Phase 3 — Using CE

**Objective.** Make Stage 3 complete and verifiably correct: components,
troubleshooting, notebooks, and the code-example defects from the audit.

| WP | Change | Files | Complexity |
|---|---|---|---|
| 3a | "Main components and calls" | `get-started/quick_api.md` (same URL; add a component figure: model → `WrapCalibratedExplainer` → calibrated predictions / explanation collections → plots/export; executed examples with output) | M |
| 3b | Troubleshooting as the single owner of errors | `get-started/troubleshooting.md` (absorb verified errors: missing `predict_proba`, NumPy-integer indexing, empty explanations, DataFrame feature-name warning, guarded fast-explainer error); `apply-to-your-data.md` keeps a short table + link | S |
| 3c | Notebook verification and links | `sections/in-practice.md`, `tasks/*.md` (links only after the driver passes); report of notebook results | M |
| 3d | Correct code examples flagged by the execution audit | pages listed in 01 §4 with class API/OTHER | M |
| 3e | Task-page wording (C-17) | `tasks/classification.md`, `tasks/probabilistic_regression.md` ("counterfactuals", "epistemic and aleatoric", "necessary to flip") — **neutral wording only for items not blocked by author questions** | S |

- **Dependencies:** Phase 2 (owners exist); D-5 (notebook linking policy).
- **Acceptance:** every code block on touched pages runs (execution test);
  troubleshooting entries each reproduced by a script in the phase report.
- **Risks:** notebooks may fail against the current API; they live in the
  repository mirror of the official project — report, do not rewrite them
  without approval (D-5).

---

## Phase 4 — Scientific foundations

**Objective.** Align Stage 4 with the Stage 2 intuitions and the evidence
hierarchy, without resolving author questions.

| WP | Change | Files | Complexity |
|---|---|---|---|
| 4a | "Intuition first" and "Go deeper" links both ways | `foundations/concepts/{calibration_methods,calibrated_interval_semantics,ce_workflow,explanation_structures,alternatives,probabilistic_regression}.md` (headers/footers only) | S |
| 4b | Comparison page as a design comparison | `docs/compare.md` (remove the unsupported "more stable rules"; table of what each method outputs and assumes; cite method papers; no performance claims) | M |
| 4c | Research hub: history and labelled open questions | `researcher/index.md` (research history list from `citing.md` and `theory_and_literature.md`); `researcher/future_work.md` (label each item: verified limitation / open author question / proposed extension) | M |
| 4d | Assumption wording alignment (C-18) | 9 pages with "exchangeable or distribution-matched" — **blocked** until the authors answer Q-6/SR-01 | — |

- **Dependencies:** Phase 2b; D-6 (compare rewrite scope); author answers for 4d.
- **Acceptance:** S10–S12; no new guarantee wording; markers on SR items kept.

---

## Phase 5 — Software architecture and contributing

| WP | Change | Files | Complexity |
|---|---|---|---|
| 5a | Development setup page | **new** `docs/contributor/development_setup.md` (MyST `{include}` of `../../CONTRIBUTING.md` sections, or a summary + link — D-7); `contributor/index.md` toctree | S |
| 5b | Contributor hub path | `contributor/index.md` (path: setup → architecture → contracts → tests/PR → open questions; replace references to maintainer-only files with GitHub links) | S |
| 5c | Architecture entry for contributors | `foundations/concepts/architecture.md` (top "How to read this page" + link to source tree and tests; no restructuring) | S |

- **Dependencies:** D-7. **Risk:** `{include}` of a root file with relative
  links breaks link checks — test both builds.

---

## Phase 6 — Integration and quality assurance

| WP | Change | Files | Complexity |
|---|---|---|---|
| 6a | Cluster housekeeping (Report C: C-23…C-28) | performance, reject, plugin, Mondrian, telemetry pages: one-line role statements and owner links; no deletions | M |
| 6b | Terminology (C-31) and release notes (C-03) | 16 pages with "thresholded regression" (user-facing → "probabilistic regression", mechanism contexts unchanged); `foundations/governance/release_notes.md` → pointer to CHANGELOG | M |
| 6c | Final QA and reports | whole site: §1 gates, §4 layout pass on all journey pages, journey test, page inventory, final report | M |

- **Dependencies:** Phases 1–5; Q-5 answered for 6b terminology (or PO decision).
