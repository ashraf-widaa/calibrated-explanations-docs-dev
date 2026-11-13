# 01 — Current-state audit

Planning document (Phase 0). No published page was changed.

## 0. Baseline

| Item | Value |
|---|---|
| Date | 2026-11-13 10:23 (+01:00) |
| Branch / HEAD | `docs-dev/autonomous-20261112` / `a55c7e9d` |
| Beta `main` (remote `docs-dev`) | `a55c7e9d` — the Quick Start v3 visuals pass is pushed |
| Unrelated working-tree items | 113 (modified `LEARNING_JOURNAL.md`, `learning-reports/L05-…`; untracked learning reports, `HANDOVER_REPORT.md`, `session-checkpoint-batch-5-prep.md`) — untouched |
| Strict Beta build | exit 0, **0 warnings** (`_build/plan-baseline`) |
| Docs tests | **300 passed** (`tests/docs` + parameter-naming test) |
| Internal links | 155 pages, **0 broken** |
| Pages | 129 source pages (`.md`/`.rst`, excluding generated autosummary); 2 intentional orphans (`getting_started_60s` redirect stub, `multiclass_all_classes_gap_analysis`) |
| Toolchain | Sphinx 7.4.7, MyST, Furo, sphinx-design, sphinxcontrib-mermaid, numpydoc, nbsphinx (not executed on RTD), autosummary |
| Tests for docs | 16 files under `tests/docs/` (navigation, homepage, landing pages, reader journeys, glossary, walkthrough, quickstart execution/output match, concept examples, plot colours, what-is-ce wording, upgrade checklist, notebook driver) |

Side effect of this audit: running every docs code block once from the
repository root wrote `plotspec_example.png` there (git-ignored, untracked;
deleting files is outside the agent's permissions — remove by hand). The rerun
used a scratch directory.

## 1. Structure as built

Homepage: Quick Start; four section cards (CE: What & Why; How CE Works; CE in
Practice; CE Software & Integration); Project & Resources (project, glossary,
GitHub, licence); Commercial Services. Sidebar groups mirror the cards, each
starting with an "Overview" landing page.

| Area | Pages in nav (approx.) | Notes |
|---|---|---|
| Quick Start | 10 | v3 three-path structure (A1, A2, B, C1–C5, Quick API) |
| CE: What & Why | 4 | overview, what-is-ce, EU AI Act playbook (as "Trustworthy AI"), compare |
| How CE Works | 12 | workflow, foundations hub (+6 concept pages), semantics, methods (ADD-1), interpret |
| CE in Practice | 33 | tasks (4), practitioner hub (playbooks 4, advanced 8, evaluation, API comparison, narratives), how-to (8) |
| Software & Integration | 24 | overview/versions, install, architecture, API (5 + autosummary), schema, pipelines, plugins, troubleshooting, upgrade (3), migration (3) |
| Resources | 4 | glossary (hub + 2), parameter reference |
| Project | 26 | overview, research (5), citing, roadmap, contributor (11), governance (9), tier map |

The official stable docs (read-only reference, v1.0.2 sidebar) are organised by
audience hubs (Get started / Practitioner / Researcher / Contributor / Core
references) and link no notebooks; the Beta reorganised the same pages into the
homepage sections and added the Quick Start paths, the methods page and the
glossary.

## 2. Strengths to preserve

1. **Verified examples.** Quick Start B, C2–C5, the evaluation guide and four
   concept pages execute in tests; quickstart outputs are compared with the
   page; the walkthrough is generated with a prose-number guard.
2. **Canonical semantics and evidence discipline.** One semantics page;
   STD-004 semantics notes; a claims register with SR-01…SR-16 open and
   "under review" markers.
3. **Clear Quick Start paths** (A understand / B example / C apply) with a
   validated, accessible workflow figure and real CE plots.
4. **Methods page (ADD-1)** with derivations, references and executed examples.
5. **Glossary** with science/software split and contextual links (G-P3).
6. **Section landings in the sidebar** (fixed in run 1), feedback route,
   honest demo/game labels.

## 3. Weaknesses by stage

> **Revision 3 note.** "Stage 1–5" in this document names **curriculum bands**, a planning aid for
> grouping concepts. They are not a navigation structure; Quick Start keeps Paths A/B/C
> (`13-architecture-reconciliation.md`).


### Stage 1 — Foundations

- **Missing:** AI systems vs AI models; rule-based AI vs machine learning (only
  implied in A1); black-box models and transparency; what XAI is as a field and
  its limits (A7 covers explanation forms; A6 mentions one limit).
- **Duplication:** ml-foundations A6 "Why predictions are not enough" restates
  why-ce "What a conventional workflow leaves open".
- **Broken transition:** A6 ends "The next page shows which tasks and outputs CE
  supports" — the next page is now why-ce (v3).
- Mermaid diagrams on A1/A4 are not in the figure style of the rest of Path A.

### Stage 2 — CE concepts

- **No intuition page for calibration and uncertainty.** The sidebar entry
  "Calibration & Uncertainty" opens the formal semantics page
  (`calibrated_interval_semantics`), which is a Tier 3 reference, not a first
  explanation. The L1/L2 material is spread over A6, why-ce, ADD-1 §1 and the
  walkthrough §4–5.
- **Overlap:** `what-is-ce` "The problem" and why-ce/A6 tell the same story.
- **Confusing terminology (open):** "exchangeable or distribution-matched" on 9
  pages (C-18, blocked on SR-01/Q-6); "thresholded regression" on 16 pages
  (C-31, policy says user-facing = probabilistic).

### Stage 3 — Using CE

- **No "main components" overview.** `quick_api` lists calls; `api/index` is a
  16-line link page. Readers do not see how wrapper, explanation collections,
  plots and export fit together.
- **Troubleshooting is thin** (25 lines, environment only) while verified
  user-facing errors are documented only in C5 and the guarded quickstart.
- **Notebooks:** 18 in `notebooks/`, linked only as a GitHub folder and four
  core demos from task pages; none was run in this audit; nbsphinx does not
  execute on RTD.
- **Unsupported wording on task pages (C-17):** "Alternative explanations
  (counterfactuals)", "epistemic and aleatoric explanation envelopes",
  "necessary to flip the prediction" (`tasks/classification.md:23,44,52`),
  "aleatoric + epistemic uncertainty on the score"
  (`tasks/probabilistic_regression.md:81`); linked to open SR-07/SR-08.

### Stage 4 — Going deeper

- `compare.md` is 20 lines with an unsupported "more stable rules" (C-19).
- Research history is not presented; `researcher/future_work` does not separate
  verified limitations, open author questions and proposed extensions.
- Explanation construction is described in three places at three depths
  (ce_workflow overview, walkthrough §6, `explanation_structures`, which has
  blocked items C-37).

### Stage 5 — Contributing

- **No development-setup page.** `CONTRIBUTING.md` (187 lines: dev install,
  extras, tests) is not rendered in the docs.
- The contributor hub (40 lines) points readers to
  `development/standards/…` and `development/adrs/…` files that are not
  reachable from the docs ("maintainer-only docs set").
- Architecture (429 lines) sits under Software & Integration with no reading
  guide for contributors.

### Housekeeping still open from the 2026-11-12 review (Report C)

C-03 release notes stop at v0.10.2; C-23…C-28 overlapping clusters
(performance, reject, plugins, Mondrian, telemetry) without owners; C-31
terminology; C-32/C-33 internal material in public navigation (needs a
visibility decision); C-37 blocked. Fixed since: C-01, C-02, C-04, C-05, C-06,
C-07, C-08, C-10, C-12, C-13, C-14 (partly), C-21.

## 4. Code-example execution audit

Every page with `python` blocks was executed in page order in one namespace
(scratch directory, current `src/`). 54 pages:

| Class | Pages | Meaning |
|---|---|---|
| OK | 14 | Runs as written (all Quick Start pages, evaluate_ce, integrate_with_pipelines, calibration_methods, alternatives, probabilistic_regression, plot_with_plotspec, safe-defaults, migration ADR-033, v0.11.4 checklist) |
| FRAGMENT | 32 | Uses variables defined elsewhere (`explainer`, `model`, …); readers cannot run it as shown, and no test covers it |
| **API (outdated)** | 3 | see below |
| IMPORT | 3 | `plugin-advanced-contract` (private `_EXPLANATION_PLUGINS` no longer exists — **outdated**); `notebook_policy` (imports the repo `scripts` package — contributor-only, expected); `plugins.md` (optional external plugin — expected) |
| OTHER | 2 | `explanation_structures.md` block 0 is a schema sketch in a `python` fence (use `text`); `explanation_retrieval.md` block 0 is indented and uses `expl.factual`, an attribute not found in `src/` (**likely outdated**) |

**Outdated API examples (confirmed against `src/`):**

| Page | Problem |
|---|---|
| `get-started/ce_first_agent_guide.md` block 6 | `explore_alternatives(..., ensure_coverage=True, ensure_order=True)` → `ConfigurationError: unknown keyword arguments`; neither name exists in `src/` |
| `contributor/plugin-contract.md` block 2 | `plugin_meta` lacks the required `data_modalities` (ADR-033) → `ValidationError` |
| `contributor/extending/plugin-advanced-contract.md` block 1 | imports `_EXPLANATION_PLUGINS`, which no longer exists |
| `practitioner/advanced/explanation_retrieval.md` | `expl.factual` not found in `src/` (needs confirmation in Phase 3d) |
| `foundations/how-to/configure_runtime.md` blocks 0→1 | running block 0 initialises the process config manager, so block 1's `init_process_config_manager` then raises "already been initialized" — a real ordering trap readers will hit; document it |

## 5. Interactive resources

See `04-interactive-learning-plan.md` §1: app + Expert Hub (external, live),
Decision Lab games (external, educational), walkthrough and quickstarts
(verified), 18 repository notebooks (unverified), studies repository
(replication authority).

## 6. Risks

| Risk | Mitigation |
|---|---|
| Moving A6/A7 breaks the `why-predictions-are-not-enough` anchor used by a What & Why card and glossary links | Move the label with the content; test that it resolves |
| New sidebar entries break navigation tests | Update tests in the same commit |
| Fixing examples on pages mirrored from the official project diverges Beta from upstream | Record each divergence in phase reports for upstream proposal |
| Author questions block terminology and assumption wording | Keep markers; do not resolve; schedule after answers |
| Notebook failures | Report, do not rewrite without approval (D-5) |
| Git Bash heredoc corruption; ignored figure files | Editor tools only; `git add -f` for figures (07 §1) |
