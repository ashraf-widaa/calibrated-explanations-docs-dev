# L05 Stage 2A - Five-Door Navigation Design

Date: 2026-11-08  
Status: Final mapping design; no navigation implemented

## Objective and invariants

This design maps the approved five-door structure to evidence-backed
destinations. It preserves current audience and task navigation and treats
folders as physical storage rather than the logical information architecture.

Destination statuses used below:

- **Existing and suitable**
- **Existing but needs improvement**
- **New navigation landing page required**
- **Future educational content**
- **External resource requiring verification**

## Door 1 - CE: What & Why

| # | Exact homepage label | Reader goal | Destination/evidence | Status | Recommended action | Priority |
|---|---|---|---|---|---|---|
| 1.1 | Understanding AI Models | Build the basic AI/ML-to-prediction mental model | `docs/tasks/index.md:1-14`; quickstarts explain predictive workflows, but no general AI primer | Future educational content | Do not imply CE supports all listed AI families; decide whether to add bounded educational content later | Low |
| 1.2 | Can We Trust AI Outputs? | Understand accuracy, confidence, reliability, calibration and uncertainty | `docs/foundations/concepts/calibrated_interval_semantics.md:5-60`; README motivation | Existing but needs improvement | Add a beginner-oriented route to canonical semantics without universal guarantees | High |
| 1.3 | Trustworthy AI | Understand responsible AI, transparency, explainability and European context | `docs/practitioner/playbooks/eu-ai-act-compliance.md:1-20`; decision-policy pages | Existing but needs improvement | Label EU AI Act material as context; state it is not CE compliance evidence | Medium |
| 1.4 | The Explainability Gap | Understand conventional XAI limits and why calibration matters | `README.md:28-32`; `docs/compare.md:1-20` | Existing but needs improvement | Link comparison and motivation with careful non-universal wording | Medium |
| 1.5 | What Is CE & What Does It Add? | Understand CE motivation, contribution, capabilities and limits | `README.md:28-84`; `docs/tasks/capabilities.md:1-25`; semantics | Existing but needs improvement | Provide one homepage route to these existing sources; do not duplicate full content | High |

## Door 2 - How CE Works: The Theory Behind It

| # | Exact homepage label | Reader goal | Destination/evidence | Status | Recommended action | Priority |
|---|---|---|---|---|---|---|
| 2.1 | Essential Foundations | Learn supervised ML, probability, statistics and data splitting | `docs/foundations/index.md:1-40`; quickstarts show data splits | Existing but needs improvement | Label prerequisite material and identify missing general statistics coverage | High |
| 2.2 | Calibration & Uncertainty | Understand predictive reliability and uncertainty interpretation | `docs/foundations/concepts/calibrated_interval_semantics.md:5-60`; `docs/get-started/quickstart_classification.md:1-52` | Existing but needs improvement | Add a progressive link sequence from intuition to semantics | High |
| 2.3 | Statistical Methods Behind CE | Learn Venn-Abers, isotonic regression and conformal methods | `src/calibrated_explanations/calibration/venn_abers.py:205-225`; regression concepts and semantics | Existing but needs improvement | Link verified methods; do not imply a dedicated isotonic tutorial exists | Medium |
| 2.4 | How CE Explanations Work | Understand factual, alternative and task-specific explanations | `docs/foundations/how-to/interpret_explanations.md:1-16`; alternatives concept page | Existing and suitable | Link directly and preserve the distinction between factual and alternatives | High |
| 2.5 | Assumptions & Guarantees | Understand exchangeability, interval semantics, guarantees and limits | `docs/foundations/concepts/calibrated_interval_semantics.md:5-60` | Existing and suitable | Use this as the canonical semantics destination | High |

## Door 3 - CE in Practice: Explore & Apply

| # | Exact homepage label | Reader goal | Destination/evidence | Status | Recommended action | Priority |
|---|---|---|---|---|---|---|
| 3.1 | CE Examples for New Users | Try an interactive beginner experience | `https://calibrated-explanations-demo.ju.se/`; `docs/index.md:36-45` | External resource requiring verification | Link with “illustrative browser demo”; do not claim runtime or upload behavior | High |
| 3.2 | Explore Use-Case Examples | Explore decision-oriented simulated scenarios | `https://games.grejna.ai/`; `docs/index.md:25-34` | External resource requiring verification | Label as external Decision Labs; verify functionality before stronger wording | Medium |
| 3.3 | Test CE with Your Own Data | Apply CE locally to a predictive model/data | `docs/foundations/how-to/integrate_with_pipelines.md:1-67`; `notebooks/README.md:1-80` | Existing but needs improvement | Label explicitly as a local Python workflow; link installation and API prerequisites | High |
| 3.4 | Practical Workflows | Run classification, regression, factual and alternative workflows | `docs/get-started/index.md:1-30`; `docs/tasks/index.md:1-14`; practitioner hub | Existing and suitable | Link existing hubs and keep installation under Door 4 | High |
| 3.5 | Evaluate & Compare | Assess reliability, limitations and practical suitability | `docs/compare.md:1-20`; semantics page | Existing but needs improvement | Distinguish documented comparison from executed benchmark evidence | Medium |

## Door 4 - CE Software & Integration

| # | Exact homepage label | Reader goal | Destination/evidence | Status | Recommended action | Priority |
|---|---|---|---|---|---|---|
| 4.1 | Software Overview & Versions | Identify capabilities, compatibility and release context | `docs/tasks/capabilities.md:1-25`; `pyproject.toml:10-13`; `CITATION.cff:68` | Existing but needs improvement | Reconcile `1.0.0`, `v1.0.2` and `1.1.0-dev` before current-version wording | High |
| 4.2 | Installation & Configuration | Set up package, extras and environment | `docs/get-started/installation.md:1-53`; runtime configuration guide | Existing and suitable | Link canonical installation page; do not duplicate instructions | High |
| 4.3 | Internal Software Architecture | Understand components, data flow, boundaries and extension points | `docs/foundations/concepts/architecture.md:1-120`; `src/calibrated_explanations/core/wrap_explainer.py:147-821`; `src/calibrated_explanations/plugins/manager.py:145-554` | Existing and suitable | Keep architecture separate from API; identify internal details as implementation context | High |
| 4.4 | API & Technical Reference | Find public classes, methods and specifications | `docs/api/index.md:1-10`; public wrapper methods at `src/calibrated_explanations/core/wrap_explainer.py:380-821` | Existing and suitable | Link API landing page and quick API; preserve public/private distinction | High |
| 4.5 | Model & Pipeline Integration | Use CE with an existing model or pipeline | `docs/foundations/how-to/integrate_with_pipelines.md:1-67` | Existing and suitable | Link directly and require the documented fit/calibrate lifecycle | High |
| 4.6 | Extensions & Customization | Use plugins, extension contracts and configuration | `docs/plugins.md:1-80`; `docs/contributor/plugin-contract.md:1-35`; `docs/api/plugins.md:1-40` | Existing and suitable | Link user plugin overview separately from contributor contract | Medium |
| 4.7 | Troubleshooting & Upgrades | Resolve setup issues and manage compatibility | `docs/get-started/troubleshooting.md`; `docs/migration/index.md:1-20`; `docs/upgrade/index.md:1-20` | Existing and suitable | Link troubleshooting first, then migration/upgrade by version | Medium |

## Door 5 - CE Project, Vision & Evolution

| # | Exact homepage label | Reader goal | Destination/evidence | Status | Recommended action | Priority |
|---|---|---|---|---|---|---|
| 5.1 | Vision, Origins & History | Understand project motivation, milestones and evolution | `README.md:28-32`; no single project-history landing page verified | New navigation landing page required | Decide whether a small navigation-only landing page is permitted; otherwise link README with qualified label | Medium |
| 5.2 | Research & Publications | Find scientific contributions, citations and replication | `docs/researcher/index.md:1-20`; `docs/citing.md`; replication hub | Existing and suitable | Link researcher hub and preserve version-specific study caveats | High |
| 5.3 | Development & Roadmap | Understand releases, current work and future direction | `docs/ROADMAP.md:1-20`; `CHANGELOG.md:1-25`; `development/current-work/v1.1.0_plan.md` | Existing but needs improvement | Separate public roadmap/changelog from maintainer current-work plans | Medium |
| 5.4 | Community & Contributions | Learn contribution pathways and governance | `docs/contributor/index.md:1-35`; `CONTRIBUTING.md` | Existing and suitable | Preserve contributor hub as the canonical route | High |
| 5.5 | CE Ecosystem | Distinguish library, companions, external tools and Grejna AB | `docs/index.md:25-34`; `docs/plugins.md`; external plugins appendix | Existing but needs improvement | Use explicit ecosystem labels and separate optional commercial services | Medium |

## Mapping totals

| Status | Count |
|---|---:|
| Existing and suitable | 11 |
| Existing but needs improvement | 12 |
| New navigation landing page required | 1 |
| Future educational content | 1 |
| External resource requiring verification | 2 |
| **Total sub-doors** | **27** |

## Architectural decisions

- Five doors are logical homepage navigation, not a request to reorganize
  physical folders.
- Door 4.3 and 4.4 must remain separate: internal architecture is not API
  reference.
- Door 3.3 is local Python/API use, not browser upload.
- Door 5.3 distinguishes public project records from maintainer-only plans.
- Existing audience hubs and task pages remain parallel navigation routes.

