# L05 Stage 2A - Link and Evidence Map

Date: 2026-11-08  
Status: Final design mapping; no links changed

## Scope

This map covers all 27 sub-door destinations and the five main door links.
Evidence is repository evidence unless marked external. “Verified” means the
path or URL and its documented purpose were found; it does not mean a Sphinx
build, external runtime, installation or user test was performed.

## Main door destinations

| Door | Homepage title/link | Intended reader goal | Destination | Evidence | Status | Recommended action | Priority |
|---|---|---|---|---|---|---|---|
| 1 | CE: What & Why | Understand motivation and contribution | Homepage Door 1 card; README evidence | `README.md:28-84`; `docs/index.md:1-3` | Existing but needs improvement | Keep card linked to homepage Door 1 anchor until a canonical page is approved | High |
| 2 | How CE Works: The Theory Behind It | Learn concepts and assumptions | `docs/foundations/concepts/index.md` | `docs/foundations/concepts/index.md:1-32` | Existing and suitable | Link title to concepts index | High |
| 3 | CE in Practice: Explore & Apply | Try and apply CE | `docs/get-started/index.md` | `docs/get-started/index.md:1-30` | Existing and suitable | Link title to get-started; include task links in grid | High |
| 4 | CE Software & Integration | Install, integrate and extend CE | `docs/api/index.md` plus installation | `docs/api/index.md:1-10`; installation `:1-53` | Existing but needs improvement | Choose one title target and expose installation/API as links | High |
| 5 | CE Project, Vision & Evolution | Understand project and ecosystem | No single suitable landing page | `docs/researcher/index.md:1-20`; contributor and roadmap pages | New navigation landing page required | Approve a small landing page or use a qualified multi-link card | Medium |

## Door 1 sub-door mapping

| # | Exact label | Goal | Destination | Evidence | Status | Action | Priority |
|---|---|---|---|---|---|---|---|
| 1.1 | Understanding AI Models | Learn AI types, learning approaches, model families and predictions | Future educational content; supporting task pages | `docs/tasks/index.md:1-14`; quickstart pages | Future educational content | Do not create or imply during Stage 2B | Low |
| 1.2 | Can We Trust AI Outputs? | Understand reliability, calibration and uncertainty | Semantics and calibration material | `docs/foundations/concepts/calibrated_interval_semantics.md:5-60` | Existing but needs improvement | Add qualified route to canonical semantics | High |
| 1.3 | Trustworthy AI | Understand responsibility and European context | EU AI Act contextual page and decision policies | `docs/practitioner/playbooks/eu-ai-act-compliance.md:1-20` | Existing but needs improvement | Add “context, not compliance” qualifier | Medium |
| 1.4 | The Explainability Gap | Understand conventional XAI limitations | README and comparison | `README.md:28-32`; `docs/compare.md:1-20` | Existing but needs improvement | Link both and avoid universal criticism | Medium |
| 1.5 | What Is CE & What Does It Add? | Understand capabilities and limits | README, capabilities, semantics | `README.md:28-84`; `docs/tasks/capabilities.md:1-25` | Existing but needs improvement | Use concise router text, not duplicated content | High |

## Door 2 sub-door mapping

| # | Exact label | Goal | Destination | Evidence | Status | Action | Priority |
|---|---|---|---|---|---|---|---|
| 2.1 | Essential Foundations | Learn prerequisites | Foundations index and quickstarts | `docs/foundations/index.md:1-40` | Existing but needs improvement | Add a prerequisite label/sequence | High |
| 2.2 | Calibration & Uncertainty | Interpret reliability and uncertainty | Semantics and classification quickstart | Semantics `:5-60`; quickstart `:1-52` | Existing but needs improvement | Connect intuition to formal semantics | High |
| 2.3 | Statistical Methods Behind CE | Learn Venn-Abers, isotonic and conformal methods | Venn-Abers source and regression/concept pages | `src/calibrated_explanations/calibration/venn_abers.py:205-225`; `docs/foundations/concepts/probabilistic_regression.md` | Existing but needs improvement | Do not claim dedicated isotonic coverage | Medium |
| 2.4 | How CE Explanations Work | Understand factual and alternative explanations | Interpretation and alternatives | `docs/foundations/how-to/interpret_explanations.md:1-16`; `docs/foundations/concepts/alternatives.md` | Existing and suitable | Link directly | High |
| 2.5 | Assumptions & Guarantees | Find semantics and non-guarantees | Calibrated interval semantics | `docs/foundations/concepts/calibrated_interval_semantics.md:5-60` | Existing and suitable | Make canonical status explicit | High |

## Door 3 sub-door mapping

| # | Exact label | Goal | Destination | Evidence | Status | Action | Priority |
|---|---|---|---|---|---|---|---|
| 3.1 | CE Examples for New Users | Explore a browser example | `https://calibrated-explanations-demo.ju.se/` | `docs/index.md:36-45` | External resource requiring verification | Say “illustrative browser demo”; verify before stronger claims | High |
| 3.2 | Explore Use-Case Examples | Explore simulated decision scenarios | `https://games.grejna.ai/` | `docs/index.md:25-34` | External resource requiring verification | Say “external Decision Labs”; do not claim CE integration | Medium |
| 3.3 | Test CE with Your Own Data | Use local predictive data | Pipeline guide and notebooks | `docs/foundations/how-to/integrate_with_pipelines.md:1-67`; `notebooks/README.md:1-80` | Existing but needs improvement | Explicitly label local Python workflow | High |
| 3.4 | Practical Workflows | Follow task guides | Get-started, tasks and practitioner hubs | `docs/get-started/index.md:1-30`; `docs/tasks/index.md:1-14` | Existing and suitable | Link existing hubs | High |
| 3.5 | Evaluate & Compare | Assess suitability and limits | Compare and semantics | `docs/compare.md:1-20`; semantics page | Existing but needs improvement | Distinguish comparisons from benchmarks | Medium |

## Door 4 sub-door mapping

| # | Exact label | Goal | Destination | Evidence | Status | Action | Priority |
|---|---|---|---|---|---|---|---|
| 4.1 | Software Overview & Versions | Understand capabilities and release status | Capabilities, metadata, changelog | `docs/tasks/capabilities.md:1-25`; `pyproject.toml:10-13`; `CITATION.cff:68` | Existing but needs improvement | Reconcile version references | High |
| 4.2 | Installation & Configuration | Install and configure | `docs/get-started/installation.md` | `docs/get-started/installation.md:1-53` | Existing and suitable | Use as canonical | High |
| 4.3 | Internal Software Architecture | Understand internals and data flow | Architecture page and source modules | `docs/foundations/concepts/architecture.md:1-120`; wrapper `:147-821`; plugin manager `:145-554` | Existing and suitable | Keep distinct from public API | High |
| 4.4 | API & Technical Reference | Use public interfaces | `docs/api/index.md` and API pages | `docs/api/index.md:1-10`; wrapper public methods `:380-821` | Existing and suitable | Link API reference | High |
| 4.5 | Model & Pipeline Integration | Integrate a model/pipeline | Pipeline guide | `docs/foundations/how-to/integrate_with_pipelines.md:1-67` | Existing and suitable | Link directly | High |
| 4.6 | Extensions & Customization | Extend through plugins | Plugins and contributor contracts | `docs/plugins.md:1-80`; `docs/api/plugins.md:1-40` | Existing and suitable | Separate user and contributor routes | Medium |
| 4.7 | Troubleshooting & Upgrades | Resolve issues and compatibility | Troubleshooting, migration and upgrade | `docs/get-started/troubleshooting.md`; migration/upgrade hubs | Existing and suitable | Link version-specific guidance | Medium |

## Door 5 sub-door mapping

| # | Exact label | Goal | Destination | Evidence | Status | Action | Priority |
|---|---|---|---|---|---|---|---|
| 5.1 | Vision, Origins & History | Understand project evolution | README; no single history page | `README.md:28-32` | New navigation landing page required | Decide whether to create a future landing page | Medium |
| 5.2 | Research & Publications | Find papers and replication | Researcher hub, citing and replication | `docs/researcher/index.md:1-20`; `docs/citing.md` | Existing and suitable | Link researcher hub | High |
| 5.3 | Development & Roadmap | Track releases and future work | Roadmap, changelog, current-work plan | `docs/ROADMAP.md:1-20`; `CHANGELOG.md:1-25` | Existing but needs improvement | Separate public and maintainer planning | Medium |
| 5.4 | Community & Contributions | Contribute safely | Contributor hub and guide | `docs/contributor/index.md:1-35`; `CONTRIBUTING.md` | Existing and suitable | Link contributor hub | High |
| 5.5 | CE Ecosystem | Understand companions and related organizations | Homepage, plugins, external plugins, Grejna link | `docs/index.md:25-34`; `docs/appendices/external_plugins.md:1-43` | Existing but needs improvement | Explicitly distinguish library, companions, external tools and commercial services | Medium |

## Verification summary

Of the 27 sub-doors:

- 11 have suitable existing destinations.
- 12 have existing evidence but need clearer labels, sequencing or caveats.
- 1 needs a new navigation landing-page decision.
- 1 is future educational content, not a current destination.
- 2 are documented external resources requiring verification.

