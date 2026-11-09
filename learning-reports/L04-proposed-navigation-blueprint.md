# L04 - Proposed Five-Door Navigation Blueprint

Date: 2026-11-08  
Status: Conceptual blueprint only; no navigation implemented

## Objective and method

This blueprint expresses the proposed five-door architecture as a logical
navigation model while preserving all current physical paths. Each item is
labelled **Existing**, **Existing but needs improvement**, or **Proposed new
content**. “Proposed” describes a future decision, not a file created in this
task.

## Top-level entry points

```text
CE documentation homepage
├── Door 1: CE - What & Why
├── Door 2: How CE Works - Theory and foundations
├── Door 3: CE in Practice - Explore and apply
├── Door 4: CE Software & Integration
└── Door 5: CE Project, Vision & Evolution
```

The existing audience routes remain a parallel navigation layer:

```text
New users -> docs/get-started/index.md
Practitioners -> docs/practitioner/index.md
Researchers -> docs/researcher/index.md
Contributors -> docs/contributor/index.md
```

The existing task route also remains:

```text
Task type -> docs/tasks/index.md -> classification/regression/probabilistic regression
```

## Door 1 - CE: What & Why

| Logical item | Status | Existing support | Gap/cross-link |
|---|---|---|---|
| CE overview and motivation | Existing but needs improvement | `README.md:28-32`; homepage identity/open-source text in `docs/index.md:1-31` | Add a short canonical homepage summary or future overview page |
| Why calibration matters | Existing but needs improvement | README calibration-first explanation; quickstart semantics notes | Link directly from homepage before policy/release details |
| What CE contributes | Existing | `docs/tasks/capabilities.md:9-19`; interpretation guide | Add a capability-oriented label |
| Benefits and boundaries | Existing | `docs/foundations/concepts/calibrated_interval_semantics.md:51-60` | Label as assumptions, guarantees and limits |
| Responsible/trustworthy AI context | Existing but needs improvement | Practitioner decision-policy and EU AI Act contextual pages | Add context without claiming regulatory compliance |
| General AI/ML decision-making background | Proposed new content | No dedicated page found | Defer pending scope decision |

Suggested links: Door 1 -> recommended classification quickstart; Door 1 ->
capabilities; Door 1 -> semantics/limits; Door 1 -> practitioner and
researcher routes.

## Door 2 - How CE Works

### Prerequisite layer

| Logical item | Status | Existing support | Gap/cross-link |
|---|---|---|---|
| Classification/regression concepts | Existing | `docs/tasks/` pages | Link task pages from theory |
| Data splitting and evaluation | Existing but needs improvement | Quickstarts explain proper/calibration/test splits | Add a conceptual explanation link |
| Predictions, probabilities and uncertainty | Existing | Quick API and interpretation guide | Group under a beginner theory bridge |
| Explainable AI concepts | Existing but needs improvement | Interpretation, alternatives, explanation structures | Add a labelled conceptual entry |
| Basic probability/statistics | Proposed new content | No dedicated CE page found | Decide whether to link outward or write a primer |
| General supervised learning | Proposed new content | No dedicated CE page found | Scope decision required |

### CE-specific layer

| Logical item | Status | Existing support | Gap/cross-link |
|---|---|---|---|
| Calibration and calibrated explanations | Existing | README, quickstarts, semantics | Add direct homepage/theory link |
| Factual and alternative explanations | Existing | `docs/foundations/how-to/interpret_explanations.md`; `concepts/alternatives.md` | Preserve canonical interpretation page |
| Venn-Abers and CPS | Existing but needs improvement | Quickstarts, semantics, README and researcher theory | Add an intuitive-to-formal bridge |
| Classification, interval and probabilistic regression | Existing | `calibrated_interval_semantics.md:5-18` | Preserve mode-specific separation |
| Exchangeability and non-guarantees | Existing | Semantics page | Link with explicit “limits” label |
| Conceptual CE workflow | Existing | `docs/foundations/concepts/architecture.md` public lifecycle | Cross-link from quickstarts and API |
| Isotonic regression and uncertainty decomposition | Proposed new content | No dedicated pages found | Do not imply support or theory commitment before verification |

Suggested links: Door 2 -> interpretation; Door 2 -> task capabilities; Door 2
-> researcher theory; Door 2 -> API architecture.

## Door 3 - CE in Practice

| Logical item | Status | Existing support | Gap/cross-link |
|---|---|---|---|
| Start/install | Existing | `docs/get-started/` | Add recommended first example label |
| Browser demo | Existing | `docs/index.md:36-45`; README | Preserve illustrative/versioned distinction |
| Task quickstarts | Existing | Classification, regression, guarded quickstarts | Preserve task-specific alternatives |
| Capabilities map | Existing | `docs/tasks/capabilities.md` | Promote from task hub |
| Interpretation and alternatives | Existing | Interpretation guide and alternatives concept | Add one onward sequence |
| Pipeline integration | Existing | `docs/foundations/how-to/integrate_with_pipelines.md` | Promote from foundations to practitioner route |
| Troubleshooting | Existing | `docs/get-started/troubleshooting.md` | Link after installation/quickstart |
| Practical comparisons/evaluation | Existing but needs improvement | `docs/compare.md`, researcher theory and playbooks | Create a clearer evaluation label, not a duplicate page |

Suggested user journey:

```text
Door 1 overview -> Door 3 classification quickstart ->
Door 2 interpretation and limits -> Door 4 API/integration ->
Door 5 research/contribution routes
```

## Door 4 - CE Software & Integration

| Logical item | Status | Existing support | Gap/cross-link |
|---|---|---|---|
| Public API | Existing | `docs/api/`, Quick API, lazy exports | Add API choice link from practitioner path |
| Runtime architecture | Existing | `docs/foundations/concepts/architecture.md` | Link from API landing page |
| Model/pipeline integration | Existing | Pipeline how-to and README compatibility | Promote to practitioner and task pages |
| Plugins and extension contracts | Existing | `docs/plugins.md`, plugin API, contributor contract | Preserve separate practitioner/contributor depth |
| Serialization/schema | Existing | API serialization, `docs/schema_v1.md`, migration | Add a technical reference cross-link |
| Compatibility and release constraints | Existing | upgrade/migration, changelog, homepage release notice | Link to Door 5 for history |
| Internal implementation details | Existing but needs improvement | `src/calibrated_explanations/` and architecture docs | Keep stable public contract distinct from internals |

## Door 5 - CE Project, Vision & Evolution

| Logical item | Status | Existing support | Gap/cross-link |
|---|---|---|---|
| Vision/origins/publications | Existing but needs improvement | README, citing, researcher theory | Add one project-history link |
| Research directions | Existing | `docs/researcher/future_work.md` | Preserve researcher route |
| Releases/migration/changelog | Existing | `CHANGELOG.md`, migration and upgrade pages | Add a single evolution landing link |
| Contribution and governance | Existing | Contributor hub, governance docs, CONTRIBUTING.md | Preserve contributor route |
| ADRs and standards | Existing, maintainer-only | `development/adrs/`, `development/standards/` | Link selectively; do not mirror catalogs |
| Official plans and future work | Existing | Active plan, `ROADMAP.md`, researcher future work | Distinguish committed release scope from research ideas |

## Cross-links and labels

Recommended labels for future navigation:

- “What CE solves” -> Door 1
- “Supported tasks and examples” -> Door 3
- “How calibration and uncertainty work” -> Door 2
- “API and pipeline integration” -> Door 4
- “Research, releases and contributing” -> Door 5

These are logical labels only. They should point to existing pages before any
folder or filename changes are considered.

## Gaps requiring decisions

1. Whether to create a canonical Door 1 overview page or improve the homepage.
2. Whether prerequisite ML/statistics material belongs in CE documentation.
3. Whether a CE-specific theory bridge is needed after a navigation pilot.
4. Which maintainer-only records should be linked from contributor pages.
5. Whether the five doors should be visible top-level navigation or remain a
   planning model.

## Recommended next step

Approve a small navigation pilot using existing pages only: add Door 1
orientation, capability/integration links, and one guided journey. Re-evaluate
content gaps after reader feedback rather than creating all proposed pages at
once.

