# L04 - Five-Door Content Mapping

Date: 2026-11-08  
Status: Read-only mapping completed; no structural changes implemented

## Objective and method

The current documentation was compared with every topic in the proposed five
doors. A topic is marked **Explained**, **Partially explained**, **Mentioned or
linked only**, **Not found**, or **Not yet verified**. Coverage and
discoverability are assessed separately.

The mapping treats `development/` as maintainer/project material, not as public
user documentation. The superseded ADR-022 is historical evidence only:
`development/adrs/superseded ADR-022-documentation-information-architecture.md:5`
explicitly says not to use it for new documentation.

## Door 1 - CE: What & Why

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| CE overview and motivation | `README.md:28-32` explains the miscalibrated-XAI problem and CE's calibration-first approach | Explained | Low from `docs/index.md`; README is external to docs navigation | Add a short homepage overview reusing README concepts |
| AI/ML in decision-making | No focused public CE page found in inspected inventory | Not found | None | Potential new contextual content only after audience need is confirmed |
| Trustworthy/responsible AI | `docs/index.md:28-31` establishes open-source context; practical limitations appear in `docs/foundations/concepts/calibrated_interval_semantics.md:51-60` | Partially explained | Medium | Link the limitations as responsible-use guidance; do not broaden into unsupported claims |
| European trustworthy AI/EU AI Act | `docs/practitioner/playbooks/eu-ai-act-compliance.md:1` exists | Mentioned or linked only | Medium for practitioners, low for beginners | Keep contextual and clearly distinguish documentation support from regulatory compliance |
| Limits of conventional explainability | README contrasts LIME/SHAP with miscalibrated outputs (`README.md:28-32`); `docs/compare.md` exists | Partially explained | Low in docs homepage | Link comparison/README-derived context from Door 1 |
| CE contribution | `README.md:30-32`; capability and semantics pages | Explained | Medium | Reuse concise wording in homepage and capabilities |
| Benefits, boundaries, non-guarantees | `docs/foundations/concepts/calibrated_interval_semantics.md:5-60` | Explained | Medium | Retitle/link as “guarantees, assumptions and limits” where appropriate |

## Door 2 - How CE Works

### A. Prerequisite foundations

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| AI/ML fundamentals | No dedicated prerequisite page found | Not found | None | Potential new content; do not assume CE docs must teach general ML |
| Supervised learning | No dedicated page found | Not found | None | Potential new content if student manual scope is approved |
| Classification and regression | `docs/tasks/classification.md:1-99`; `docs/tasks/regression.md`; `docs/tasks/probabilistic_regression.md` | Explained | High from task hub, medium from homepage | Preserve task hub and cross-link from theory |
| Data splitting/model evaluation | Quickstarts show proper/calibration/test splits (`docs/get-started/quickstart_classification.md:20-35`) | Partially explained | High after quickstart, low as prerequisite | Add a conceptual pointer rather than duplicate tutorial text |
| Predictions, probabilities, uncertainty | Quick API and interpretation guide (`docs/get-started/quick_api.md:1-70`; `docs/foundations/how-to/interpret_explanations.md:1-16`) | Explained | Medium | Create guided links from Door 2 and Door 3 |
| Explainable AI concepts | Interpretation, alternatives and explanation structures pages | Partially explained | Medium | Use existing interpretation page as conceptual entry |
| Basic probability/statistics | Statistical assumptions are described, but no general primer found | Partially explained | Low | Potential new content, subject to scope |

### B. CE-specific foundations

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| Calibration and calibrated explanations | Quickstarts, semantics and README | Explained | Medium | Add a direct “how calibration works” label/link |
| Factual and alternative explanations | `docs/foundations/how-to/interpret_explanations.md:8-16`; `docs/foundations/concepts/alternatives.md` | Explained | High after quickstart, medium from concepts | Preserve and cross-link |
| Venn-Abers predictors | Quickstart semantics and README method summary; API/source references | Partially explained | Medium | Add a concise theory pointer if mathematical depth is needed |
| Isotonic regression | No dedicated page found in inspected docs | Not found | None | Potential new content; verify desired depth before adding |
| Conformal prediction/CPS | Regression quickstart and semantics (`quickstart_regression.md:1-18`; semantics page) | Explained | Medium | Use regression as the practical entry and add theory cross-link |
| Classification, interval and probabilistic regression | Semantics page explicitly separates all three modes (`calibrated_interval_semantics.md:5-18`) | Explained | High | Preserve mode-specific structure |
| Aleatoric and epistemic uncertainty | No dedicated CE page found | Not found | None | Potential new content; avoid implying unsupported decomposition |
| Exchangeability and assumptions | Semantics page states exchangeability/distribution-match assumptions | Explained | Medium | Label as assumptions/limits in navigation |
| Interval interpretation/guarantees/non-guarantees | Semantics page | Explained | Medium | Promote as a named limits page/link |
| Conceptual CE workflow | Architecture page public lifecycle and practitioner core path | Explained | Medium | Cross-link architecture lifecycle from Door 2 and Door 3 |

## Door 3 - CE in Practice

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| Audiences/application areas | Homepage audience bullets and practitioner/researcher hubs | Explained | High | Preserve audience routing |
| Use cases/decision contexts | Practitioner decision policies and README illustrative examples | Partially explained | Medium | Link decision-policy playbook; avoid unsupported domain claims |
| Browser demo | Homepage and README demo admonitions | Explained | High | Preserve demo/docs distinction |
| Installation/quickstarts | Get started pages | Explained | High | Preserve and label a recommended first quickstart |
| Classification/regression examples | Three quickstarts and task pages | Explained | High | Preserve task-first navigation |
| Factual/alternative explanations in practice | Interpretation guide and quickstarts | Explained | High after quickstart | Add an explicit continuation route |
| Task-oriented how-to guides | `docs/tasks/` and foundations how-to | Explained | Medium | Cross-link task pages to integration and interpretation |
| Practical evaluation/comparisons | `docs/compare.md`, practitioner playbooks, researcher theory | Partially explained | Low-medium | Add a discoverable comparison/evaluation link |
| Troubleshooting/next steps | `docs/get-started/troubleshooting.md`, quickstart next links | Explained | Medium | Add to a practical journey rather than homepage clutter |

## Door 4 - CE Software & Integration

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| Stable release/capabilities | Homepage 1.0.0 notice (`docs/index.md:13-23`), changelog, active 1.1.0 plan | Explained | Medium; release context is split | Keep public release notice and link project release material |
| High-level architecture | `docs/foundations/concepts/architecture.md:1-80+` | Explained | Medium | Link architecture from API and practitioner routes |
| Internal modules/components/data flow | Architecture page plus `src/calibrated_explanations/core`, `plugins`, `calibration`, `explanations`, `viz` | Partially explained | Low for public users | Keep details in technical/contributor pages; avoid exposing unstable internals as API |
| Public API/technical reference | `docs/api/`, Quick API, public lazy exports | Explained | High from API and Get started, medium from homepage | Add one direct API choice link for practitioners |
| Model adapters/supported interfaces | README scikit-learn compatibility; pipeline integration page | Partially explained | Medium | Link pipeline guide from practitioner/task paths |
| External ML pipeline/application integration | `docs/foundations/how-to/integrate_with_pipelines.md:1-67` | Explained | Low-medium | Promote integration link |
| Extension/customization | Plugin docs, contributor contract, practitioner plugin guides | Explained | Medium | Preserve separate user/contributor plugin routes |
| Dependencies/compatibility/constraints | Installation, README, migration and upgrade pages | Explained | Medium | Cross-link from Door 4 entry point |

## Door 5 - CE Project, Vision & Evolution

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| Project vision/mission | README summary and project description | Partially explained | Medium in README, low in docs | Reuse only if a public overview is approved |
| Origins/research history | README publications/funding sections; researcher theory page | Partially explained | Medium | Link researcher hub and citing rather than duplicate history |
| Publications/milestones | `docs/citing.md`, `docs/researcher/advanced/theory_and_literature.md` | Explained | Medium | Preserve researcher route |
| Development journey | Changelog, migration, finished plans | Explained | Low for general users | Link release history from project door |
| ADRs | `development/adrs/` and contributor references | Explained for maintainers | Low and intentionally not user-facing | Keep ADRs maintainer-facing; link selected decisions only |
| Version control/development workflow | `CONTRIBUTING.md`, `development/README.md` | Explained | Medium for contributors | Preserve contributor path |
| Releases/changelog/migration | `CHANGELOG.md`, `docs/migration`, `docs/upgrade`, `release.md` | Explained | Medium | Add one project evolution landing link |
| Contribution/governance | Contributor hub and foundations governance | Explained | High for contributors | Preserve audience route |
| Research directions/open questions | `docs/researcher/future_work.md:1-68` | Explained | High within researcher hub | Preserve distinction from committed work |
| Development roadmap/future opportunities | `ROADMAP.md`, `docs/ROADMAP.md` | Explained | Medium | Label official plan versus exploratory research |

## Overall interpretation

Coverage is strongest for Doors 3 and 4, followed by the CE-specific portion
of Door 2 and the project/evolution portion of Door 5. Door 1 is represented
in README and limitations pages but is not a first-class public documentation
entry point. The prerequisite layer of Door 2 is the largest genuine content
gap, although it may be outside the library's appropriate scope.

## Open questions and recommended next step

Before creating new pages, decide whether the project wants to teach general
AI/ML foundations or only provide CE prerequisites. Then test a navigation-only
blueprint that exposes the existing motivation, capability, theory, API and
project-history pages without moving files.

