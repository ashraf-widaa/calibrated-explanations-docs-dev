# L04 - Current Documentation Inventory

Date: 2026-11-08  
Status: Read-only inventory completed; no documentation changes implemented

## Objective and inspection method

This inventory maps the current CE documentation and the repository material
that supports it against the proposed five-door architecture. Inspection was
limited to repository source files. No Sphinx, Read the Docs, package install,
or linkcheck was run.

The checked-out release context is verifiable as development version
`1.1.0-dev` in `pyproject.toml:10`, with the fallback package version
`1.1.0.dev0` in `src/calibrated_explanations/__init__.py:16-28`. The active
release plan is `development/current-work/v1.1.0_plan.md:1-20`.

## Documentation surface

`docs/` contains 107 Markdown pages grouped into the following physical areas.
The physical folders are not themselves the proposed five doors.

| Existing parent section | Page inventory and purpose | Typical audience/type | Likely door |
|---|---|---|---|
| `docs/index.md` | Homepage, release notice, demo, audience routing, and toctrees (`docs/index.md:1-106`) | All audiences / orientation | Doors 1 and 3 |
| `docs/get-started/` | Installation, three quickstarts, Quick API, troubleshooting, agent setup (`docs/get-started/index.md:1-30`) | New users / tutorial and how-to | Door 3 |
| `docs/foundations/concepts/` | Semantics, architecture, alternatives, uncertainty-related terminology, error handling, telemetry, parameters (`docs/foundations/concepts/index.md:1-32`) | Users, practitioners, contributors / explanation | Doors 1, 2 and 4 |
| `docs/foundations/how-to/` | Pipeline integration, interpretation, runtime/telemetry, exports, plots, narratives, performance (`docs/foundations/how-to/index.md:1-18`) | Practitioners / how-to | Doors 3 and 4 |
| `docs/foundations/reference/` | API and schema/citation links (`docs/foundations/reference/index.md:1-11`) | Technical users / reference | Door 4 |
| `docs/foundations/governance/` | PR, testing, release, section ownership, telemetry and governance events (`docs/foundations/governance/index.md:1-20`) | Contributors and maintainers / project guidance | Door 5 |
| `docs/tasks/` | Capability map plus classification, CPS interval regression, and probabilistic regression pages (`docs/tasks/index.md:1-14`) | Practitioners / task how-to and reference | Door 3 |
| `docs/practitioner/` | Practitioner core path, playbooks, advanced topics, plugins, reject policies and task API comparison (`docs/practitioner/index.md:1-22`) | Practitioners / how-to and applied explanation | Doors 3 and 4 |
| `docs/researcher/` | Replication, theory/literature, research directions and advanced research topics (`docs/researcher/index.md:1-20`) | Researchers / explanation and project information | Door 5, with Door 2 links |
| `docs/contributor/` | Plugin contract, extension guides, contributor policies, performance and agent skills (`docs/contributor/index.md:1-35`) | Contributors / how-to and governance | Doors 4 and 5 |
| `docs/api/` | Public explainer, CLI, plugin, serialization and visualization references (`docs/api/index.md:1-10`) | Technical users / reference | Door 4 |
| `docs/appendices/` | Changelog links, external plugin catalog and RTD tier map (`docs/appendices/changelog_links.md:1-10`) | All/maintainers / project reference | Doors 4 and 5 |
| `docs/migration/` and `docs/upgrade/` | Deprecations, ADR-033 notes and version checklists (`docs/migration/index.md:1-20`; `docs/upgrade/index.md:1-12`) | Existing users and maintainers / migration | Door 5 |
| Root-level `docs/` pages | 60-second decision tree, comparison, plugins, citing, schema, roadmap and gap analysis (`docs/getting_started_60s.md:1-20`; `docs/ROADMAP.md:1-5`) | Mixed / orientation and project information | Doors 1, 3, 4 and 5 |

## Traceable page inventory by section

### Entry and practical pages

| Source path | Title | Main purpose | Incoming/outgoing navigation | Door |
|---|---|---|---|---|
| `docs/index.md` | Calibrated Explanations documentation | Site entry point and audience/task routing | Links to all four audience hubs, foundations semantics, plugins, replication and toctrees (`docs/index.md:47-104`) | 1/3 |
| `docs/get-started/index.md` | Get started | Chooses among quickstarts and interpretation/semantics links | Linked from homepage; links to quickstarts, Quick API, interpretation and semantics (`docs/get-started/index.md:1-30`) | 3 |
| `docs/get-started/quickstart_classification.md` | Classification quickstart | Complete binary/multiclass fit-calibrate-explain example | Linked from Get started, practitioner and capabilities; links to interpretation, alternatives and citing (`quickstart_classification.md:1-52`) | 3 |
| `docs/get-started/quickstart_regression.md` | Regression quickstart | Interval and thresholded regression example | Linked from Get started and practitioner; links to semantics, probabilistic regression and interpretation (`quickstart_regression.md:1-58`) | 3 |
| `docs/get-started/quickstart_guarded.md` | Guarded explanations quickstart | In-distribution guarded workflow and audit | Linked from Get started and capabilities; links to guarded/alternative concepts (`quickstart_guarded.md:1-75`) | 3/4 |
| `docs/get-started/installation.md` | Installation | Package installation instructions | In Get started toctree | 3 |
| `docs/getting_started_60s.md` | 60-second decision tree | Fast route selection | Linked from Get started | 3 |
| `docs/tasks/index.md` | Tasks and capabilities | Task-first navigation | Linked by homepage core references | 3 |
| `docs/tasks/capabilities.md` | Capabilities manifest | Maps capabilities to primary pages | Linked from task hub; links to task quickstarts and audience hubs (`capabilities.md:9-25`) | 3 |

### Concept, interpretation and integration pages

| Source path | Title | Main purpose | Incoming/outgoing navigation | Door |
|---|---|---|---|---|
| `docs/foundations/index.md` | Shared foundations | Groups concepts, how-to, references and governance | Homepage core references; links to four foundations groups (`foundations/index.md:1-12`) | 2/4 |
| `docs/foundations/concepts/index.md` | Concepts & architecture | Concept index and progressive pointers | Foundations toctree; links to interpretation, alternatives, regression and semantics (`concepts/index.md:1-32`) | 2 |
| `docs/foundations/concepts/calibrated_interval_semantics.md` | Calibrated interval semantics | Mode-specific guarantees, assumptions and non-guarantees | Linked from homepage, quickstarts, tasks, practitioner and contributor | 2 |
| `docs/foundations/concepts/architecture.md` | Architecture | Public lifecycle, component ownership, inference, reject and plugin views | Concepts index; links conceptually to API and plugin material | 4 |
| `docs/foundations/how-to/interpret_explanations.md` | Interpret calibrated explanations | Explains factual/alternative objects, intervals, rules, plots and telemetry | Linked from Get started, practitioner and quickstarts | 2/3 |
| `docs/foundations/how-to/integrate_with_pipelines.md` | Integrate with scikit-learn pipelines | Preprocessing, configured wrapper and telemetry | In how-to toctree; not prominent from homepage/practitioner core path | 3/4 |
| `docs/foundations/concepts/probabilistic_regression.md` | Probabilistic and interval regression | Regression terminology and modes | Concepts index and regression quickstart | 2 |
| `docs/foundations/concepts/alternatives.md` | Alternative explanations and ensured filters | Counterfactual/alternative semantics | Concepts index and classification quickstart | 2/3 |

### Technical and project pages

| Source path | Title | Main purpose | Incoming/outgoing navigation | Door |
|---|---|---|---|---|
| `docs/api/index.md` | API Reference | Public API table of contents | Homepage core references; links to five API pages | 4 |
| `docs/api/calibrated_explainer.md` | Calibrated Explainer API | Public classes, lifecycle and containers | API index; links to task and narrative guides (`api/calibrated_explainer.md:1-189`) | 4 |
| `docs/api/plugins.md` | Plugin registry reference | Plugin scope, trust model and registration | API index; relates to contributor/plugin pages | 4 |
| `docs/api/serialization.md` | Serialization & schema reference | Explanation and PlotSpec payloads | API index; relates to schema and migration pages | 4 |
| `docs/api/visualization.md` | Visualization & PlotSpec reference | Plot contracts and current posture | API index; relates to PlotSpec how-to | 4 |
| `docs/contributor/index.md` | Contributor hub | Code/docs contribution path | Homepage and capabilities; links to plugin contract, guides, governance and migration (`contributor/index.md:9-35`) | 4/5 |
| `docs/researcher/index.md` | Researcher hub | Replication, semantics, theory and future work | Homepage; links to replication, semantics, theory and future work (`researcher/index.md:5-20`) | 5 |
| `docs/researcher/future_work.md` | Research Directions | Open research questions and discussion route | Researcher hub; links concepts and citing | 5 |
| `docs/ROADMAP.md` | Roadmap | Points to active plan, issues, milestones, ADRs and research directions | Homepage migration/project toctree | 5 |
| `docs/migration/index.md` | Migration guides | Version migration and terminology links | Homepage migration/project toctree | 5 |
| `docs/upgrade/index.md` | Upgrade guides | Version-specific checklists | Homepage migration/project toctree | 5 |

## Repository support outside `docs/`

| Repository location | Verified role | Door relevance |
|---|---|---|
| `README.md:28-32` | Plain-language problem statement: miscalibrated model outputs can produce overconfident explanations; CE calibrates before explaining | Door 1 |
| `README.md:34-84` | Illustrative factual/alternative outputs and quick start | Doors 1 and 3 |
| `src/calibrated_explanations/__init__.py:29-82` | Lazy public exports including `WrapCalibratedExplainer`, `CalibratedExplainer`, configuration and policy symbols | Door 4 |
| `src/calibrated_explanations/core/wrap_explainer.py:147-181` | High-level wrapper contract and lifecycle facade | Door 4 |
| `src/calibrated_explanations/core/wrap_explainer.py:380-419` | `fit` and `calibrate` entry points | Door 4 |
| `src/calibrated_explanations/core/wrap_explainer.py:643-699` | Factual and alternative explanation methods | Door 4 |
| `src/calibrated_explanations/core/wrap_explainer.py:768-821` | Prediction and probability methods | Door 4 |
| `development/README.md:1-58` | Canonical map separating user docs from ADRs, standards, claims and evidence | Door 5 |
| `development/adrs/` | 39 ADR records, including accepted current decisions and explicitly superseded historical records | Doors 4 and 5 |
| `development/current-work/v1.1.0_plan.md:1-117` | Active release scope, statuses, exclusions and release gates | Door 5 |
| `CHANGELOG.md:1-45` | Unreleased and v1.0.2 changes with migration-relevant detail | Door 5 |
| `CONTRIBUTING.md:1-150` | Repository authority, install/test workflow, governance and plugin intake | Doors 4 and 5 |
| `release.md:1-80` | Release preparation and publication runbook | Door 5 |

## Interpretation and open questions

The repository already contains material for all five logical doors, but the
material is organized primarily by audience, task, and technical document
type. Door 1 is the least explicit in `docs/`; its strongest existing
motivation text is in `README.md`. Door 2 is strong for CE-specific semantics
but does not present a complete prerequisite ML/statistics curriculum. Doors 4
and 5 are well supported, though much of their authoritative material lives in
`src/` and `development/` rather than the public docs.

Open questions:

- Should the README problem statement be reused or adapted into the public
  docs homepage?
- Which prerequisite topics are genuinely needed for the intended student
  audience, rather than merely desirable?
- Which maintainer-only `development/` topics should be linked from public
  contributor pages without exposing internal planning as user documentation?
- Can navigation labels distinguish “semantics and limits” from “theory” for
  readers who do not know the term semantics?

## Recommended next step

Use the content mapping and gap analysis reports to approve a navigation-first
pilot. Prefer adding cross-links and labels before moving or duplicating pages.

