# L05 Stage 2D - Navigation Mapping Table

Date: 2026-11-09  
Status: **Proposal only, awaiting Product Owner approval.** No navigation has
changed.

Content status for existing pages uses the Stage 2B assessment: "Existing" means
existing and suitable, and "Partial" means existing but needing improvement.

"Reference" means the subtopic has no sidebar entry of its own; its homepage card
links to a page listed elsewhere in the sidebar. URL impact is based on source
files staying in place and is to be confirmed by the Phase C build.

## 27 approved subtopics

| Section | Subtopic | Existing destination | Proposed sidebar placement | Content status | Navigation action | URL impact |
|---|---|---|---|---|---|---|
| CE: What & Why | Understanding AI Models | None | Not listed until a page exists | Missing | Defer | No URL exists |
| CE: What & Why | Can We Trust AI Outputs? | `foundations/concepts/calibrated_interval_semantics` | Shared page: How CE Works, position 2 | Partial | Reference | Preserved |
| CE: What & Why | Trustworthy AI | `practitioner/playbooks/eu-ai-act-compliance` | CE: What & Why, position 1 | Partial | Relocate | Preserved |
| CE: What & Why | The Explainability Gap | `compare` | CE: What & Why, position 2 | Partial | Relocate | Preserved |
| CE: What & Why | What Is CE & What Does It Add? | `tasks/capabilities` | CE: What & Why, position 3 | Partial | Relocate | Preserved |
| How CE Works | Essential Foundations | `foundations/index` | How CE Works, position 1 | Partial | Relocate | Preserved |
| How CE Works | Calibration & Uncertainty | `foundations/concepts/calibrated_interval_semantics` | How CE Works, position 2 | Partial | Relocate | Preserved |
| How CE Works | Statistical Methods Behind CE | `foundations/concepts/probabilistic_regression` | How CE Works, position 3 | Partial | Relocate | Preserved |
| How CE Works | How CE Explanations Work | `foundations/how-to/interpret_explanations` | How CE Works, position 4 | Existing | Relocate | Preserved |
| How CE Works | Assumptions & Guarantees | `foundations/concepts/calibrated_interval_semantics` | Shared page: How CE Works, position 2 | Existing | Reference | Preserved |
| CE in Practice | CE Examples for New Users | External: `https://calibrated-explanations-demo.ju.se/` | Homepage card only (decision D2) | External | Defer | External URL unchanged |
| CE in Practice | Explore Use-Case Examples | External: `https://games.grejna.ai/` | Homepage card only (decision D2) | External | Defer | External URL unchanged |
| CE in Practice | Test CE with Your Own Data | `foundations/how-to/integrate_with_pipelines` (interim) | Shared page: Software & Integration, position 5 | Partial | Reference | Preserved |
| CE in Practice | Practical Workflows | `get-started/index` | CE in Practice, position 1 | Existing | Relocate | Preserved |
| CE in Practice | Evaluate & Compare | `compare` | Shared page: CE: What & Why, position 2 | Partial | Reference | Preserved |
| Software & Integration | Software Overview & Versions | `tasks/capabilities` | Shared page: CE: What & Why, position 3 | Partial | Reference | Preserved |
| Software & Integration | Installation & Configuration | `get-started/installation` | Software & Integration, position 1 | Existing | Relocate | Preserved |
| Software & Integration | Internal Software Architecture | `foundations/concepts/architecture` | Software & Integration, position 2 | Existing | Relocate | Preserved |
| Software & Integration | API & Technical Reference | `api/index` | Software & Integration, position 3 | Existing | Relocate | Preserved |
| Software & Integration | Model & Pipeline Integration | `foundations/how-to/integrate_with_pipelines` | Software & Integration, position 5 | Existing | Relocate | Preserved |
| Software & Integration | Extensions & Customization | `plugins` | Software & Integration, position 6 | Existing | Relocate | Preserved |
| Software & Integration | Troubleshooting & Upgrades | `get-started/troubleshooting` | Software & Integration, position 7 | Existing | Relocate | Preserved |
| Project & Evolution | Vision, Origins & History | None (homepage card has an interim README link) | Not listed until a page exists | Missing | Defer | No URL exists |
| Project & Evolution | Research & Publications | `researcher/index` | Project & Evolution, position 1 | Existing | Relocate | Preserved |
| Project & Evolution | Development & Roadmap | `ROADMAP` | Project & Evolution, position 3 | Partial | Relocate | Preserved |
| Project & Evolution | Community & Contributions | `contributor/index` | Project & Evolution, position 5 | Existing | Relocate | Preserved |
| Project & Evolution | CE Ecosystem | `plugins` | Shared page: Software & Integration, position 6 | Partial | Reference | Preserved |

Abbreviated section names in this table refer to the full approved names:

- How CE Works: The Theory Behind It
- CE in Practice: Explore & Apply
- CE Software & Integration
- CE Project, Vision & Evolution

## Legacy and specialist documentation

Generated from the last pinned build's toctree data and the simulated proposal.
Every page below keeps its source path.

| Page | Title | Current toctree parent(s) | Proposed parent | Proposed section | Navigation action | URL impact |
|---|---|---|---|---|---|---|
| `api/calibrated_explainer` | Calibrated Explainer API | `api/index` | `api/index` | CE Software & Integration | Keep | Preserved |
| `api/cli` | CLI reference | `api/index` | `api/index` | CE Software & Integration | Keep | Preserved |
| `api/plugins` | Plugin registry reference | `api/index` | `api/index` | CE Software & Integration | Keep | Preserved |
| `api/serialization` | Serialization & schema reference | `api/index` | `api/index` | CE Software & Integration | Keep | Preserved |
| `api/visualization` | Visualization & PlotSpec reference | `api/index` | `api/index` | CE Software & Integration | Keep | Preserved |
| `appendices/changelog_links` | Changelog and release references | `index` | `index` | CE Project, Vision & Evolution | Keep | Preserved |
| `appendices/external_plugins` | Plugin catalog | `plugins` | `plugins` | CE Software & Integration | Keep | Preserved |
| `appendices/rtd_tier_map` | RTD tier map | `index` | `index` | CE Project, Vision & Evolution | Keep | Preserved |
| `citing` | Citing calibrated-explanations | `foundations/reference/index`, `index` | `index` | CE Project, Vision & Evolution | Keep; remove duplicate parent | Preserved |
| `contributor/agent_skills` | Agent skill catalogue | `contributor/index` | `contributor/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `contributor/extending/advanced` | Advanced contributor tooling | `contributor/index` | `contributor/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `contributor/extending/guides/index` | Extending guides | `contributor/index` | `contributor/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `contributor/extending/plugin-advanced-contract` | Advanced plugin wiring and configuration | `contributor/index` | `contributor/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `contributor/notebook_policy` | Notebook Policy for calibrated_explanations | `contributor/index` | `contributor/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `contributor/performance_harness` | Performance Harness | `contributor/index` | `contributor/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `contributor/plugin-contract` | Plugin contract | `contributor/index` | `contributor/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `contributor/reject_policy_usage` | Reject Policy Usage | `contributor/index` | `contributor/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `foundations/concepts/alternatives` | Alternative explanations and ensured filters | `foundations/concepts/index`, `researcher/advanced/index` | `foundations/concepts/index` | How CE Works: The Theory Behind It | Keep; remove duplicate parent | Preserved |
| `foundations/concepts/error_handling` | Error handling and validation | `foundations/concepts/index` | `foundations/concepts/index` | How CE Works: The Theory Behind It | Keep | Preserved |
| `foundations/concepts/explanation_structures` | Explanation Structures | `foundations/concepts/index` | `foundations/concepts/index` | How CE Works: The Theory Behind It | Keep | Preserved |
| `foundations/concepts/guarded_explanations` | Guarded explanations | `foundations/concepts/index` | `foundations/concepts/index` | How CE Works: The Theory Behind It | Keep | Preserved |
| `foundations/concepts/index` | Concepts & architecture | `foundations/index` | `foundations/index` | How CE Works: The Theory Behind It | Keep | Preserved |
| `foundations/concepts/parameter-reference` | CE Parameter Reference | `foundations/concepts/index` | `foundations/concepts/index` | How CE Works: The Theory Behind It | Keep | Preserved |
| `foundations/concepts/telemetry` | Telemetry (relocated) | `practitioner/advanced/index` | `practitioner/advanced/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `foundations/concepts/terminology` | Terminology Standardization | `foundations/concepts/index`, `migration/index` | `foundations/concepts/index` | How CE Works: The Theory Behind It | Keep; remove duplicate parent | Preserved |
| `foundations/concepts/terminology_thresholded_vs_probabilistic_regression` | Terminology: thresholded vs probabilistic regression | `foundations/concepts/index` | `foundations/concepts/index` | How CE Works: The Theory Behind It | Keep | Preserved |
| `foundations/governance/governance_events` | Governance Events (Plugin + Config Lifecycle) | `foundations/governance/index` | `foundations/governance/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `foundations/governance/index` | Governance & support | `foundations/index` | `index` | CE Project, Vision & Evolution | Relocate | Preserved |
| `foundations/governance/nav_crosswalk` | Navigation crosswalk | `contributor/extending/guides/index`, `foundations/governance/index` | `foundations/governance/index` | CE Project, Vision & Evolution | Keep; remove duplicate parent | Preserved |
| `foundations/governance/optional_telemetry` | Optional telemetry scaffolding | `contributor/extending/advanced`, `foundations/governance/index` | `foundations/governance/index` | CE Project, Vision & Evolution | Keep; remove duplicate parent | Preserved |
| `foundations/governance/pr_guide` | Pull Request Guide | `foundations/governance/index` | `foundations/governance/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `foundations/governance/release_checklist` | Release checklist | `foundations/governance/index`, `practitioner/playbooks/index` | `foundations/governance/index` | CE Project, Vision & Evolution | Keep; remove duplicate parent | Preserved |
| `foundations/governance/release_notes` | Release notes | `foundations/governance/index` | `foundations/governance/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `foundations/governance/section_owners` | Documentation section owners | `foundations/governance/index`, `practitioner/playbooks/index` | `foundations/governance/index` | CE Project, Vision & Evolution | Keep; remove duplicate parent | Preserved |
| `foundations/governance/test_policy` | Documentation test policy | `foundations/governance/index` | `foundations/governance/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `foundations/governance/waivers_inventory` | Coverage waiver inventory | `foundations/governance/index` | `foundations/governance/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `foundations/how-to/conditional_calibration` | Configure Conditional Calibration | `foundations/how-to/index` | `foundations/how-to/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `foundations/how-to/configure_runtime` | Configure runtime behaviour (ConfigManager) | `foundations/how-to/index` | `foundations/how-to/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `foundations/how-to/configure_telemetry` | Configure telemetry | `contributor/extending/guides/index`, `foundations/how-to/index`, `practitioner/advanced/index`, `researcher/advanced/index` | `foundations/how-to/index` | CE in Practice: Explore & Apply | Keep; remove duplicate parent | Preserved |
| `foundations/how-to/export_explanations` | Export explanations | `foundations/how-to/index`, `practitioner/playbooks/index` | `foundations/how-to/index` | CE in Practice: Explore & Apply | Keep; remove duplicate parent | Preserved |
| `foundations/how-to/index` | How-to guides | `foundations/index` | `index` | CE in Practice: Explore & Apply | Relocate | Preserved |
| `foundations/how-to/plot_with_plotspec` | Plot explanations with PlotSpec | `contributor/extending/advanced`, `foundations/how-to/index`, `practitioner/advanced/index` | `foundations/how-to/index` | CE in Practice: Explore & Apply | Keep; remove duplicate parent | Preserved |
| `foundations/how-to/safe-defaults` | Safe defaults for production deployments | `foundations/how-to/index` | `foundations/how-to/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `foundations/how-to/to_narrative` | Generate narratives with to_narrative | `foundations/how-to/index` | `foundations/how-to/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `foundations/how-to/tune_runtime_performance` | Tune runtime performance (opt-in) | `contributor/extending/advanced`, `foundations/how-to/index`, `practitioner/advanced/index` | `foundations/how-to/index` | CE in Practice: Explore & Apply | Keep; remove duplicate parent | Preserved |
| `foundations/reference/api` | API reference | `contributor/extending/guides/index`, `foundations/reference/index` | `foundations/reference/index` | CE Software & Integration | Keep; remove duplicate parent | Preserved |
| `foundations/reference/index` | Reference | `foundations/index` | `index` | CE Software & Integration | Relocate | Preserved |
| `get-started/ce_first_agent_guide` | CE-First Calibrated Explanations Guide (OSS) | `index` | `contributor/index` | CE Project, Vision & Evolution | Relocate | Preserved |
| `get-started/copilot-setup` | AI Agent Setup Guide for calibrated_explanations | `index` | `contributor/index` | CE Project, Vision & Evolution | Relocate | Preserved |
| `get-started/quick_api` | Quick API | `get-started/index` | `get-started/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `get-started/quickstart_classification` | Classification quickstart | `get-started/index` | `get-started/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `get-started/quickstart_guarded` | Guarded explanations quickstart | `get-started/index` | `get-started/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `get-started/quickstart_regression` | Regression quickstart | `get-started/index` | `get-started/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `getting_started_60s` | 60-second decision tree | `get-started/index` | `get-started/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `maintenance/legacy-plotting-reference` | Legacy Plotting Reference (Maintenance Only) | `index` | `index` | CE Software & Integration | Keep | Preserved |
| `migration/adr033_v0_11_0` | ADR-033 Migration Notes (v0.11.0) | `migration/index` | `migration/index` | CE Software & Integration | Keep | Preserved |
| `migration/deprecations` | Deprecation & Migration Guide | `migration/index` | `migration/index` | CE Software & Integration | Keep | Preserved |
| `migration/index` | Migration guides | `contributor/index`, `index` | `index` | CE Software & Integration | Keep; remove duplicate parent | Preserved |
| `multiclass_all_classes_gap_analysis` | Multiclass all-classes plotting quality + gap analysis | none | none | None (orphan page) | Keep orphan status | Preserved |
| `practitioner/advanced/explanation_retrieval` | Explanation retrieval | `practitioner/advanced/index` | `practitioner/advanced/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/advanced/index` | Practitioner advanced topics | `practitioner/index` | `practitioner/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/advanced/modality-plugins` | Modality plugin selection | `practitioner/advanced/index` | `practitioner/advanced/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/advanced/normalization-guide` | Normalization and Difficulty Estimation | `practitioner/advanced/index` | `practitioner/advanced/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/advanced/parallel_execution_playbook` | Parallel execution playbook (opt-in) | `practitioner/advanced/index` | `practitioner/advanced/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/advanced/reject-policy` | Reject Policy Guide | `practitioner/advanced/index` | `practitioner/advanced/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/advanced/use_plugins` | Use external plugins | `practitioner/advanced/index` | `practitioner/advanced/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/index` | Practitioner hub | `index` | `index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/narrative_templates` | Narrative Template Customization | `practitioner/index` | `practitioner/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/performance-tuning` | Performance Tuning Guide | `practitioner/advanced/index` | `practitioner/advanced/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/playbooks/decision-policies` | Decision Policies Guide | `practitioner/playbooks/index` | `practitioner/playbooks/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/playbooks/ensured-explanations` | Ensured Explanations Playbook | `practitioner/playbooks/index` | `practitioner/playbooks/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/playbooks/eu-data-liability-compliance` | Satisfying EU Data, Liability, and Algorithmic Regulations with calibrated_explanations | `practitioner/playbooks/index` | `practitioner/playbooks/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/playbooks/index` | Practitioner playbooks | `practitioner/index` | `practitioner/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/playbooks/mondrian-calibration` | Mondrian (Conditional) Calibration Playbook | `practitioner/playbooks/index` | `practitioner/playbooks/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `practitioner/task_api_comparison` | Task API Comparison | `practitioner/index` | `practitioner/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `researcher/advanced/difficulty_normalized_reject` | Difficulty-Normalized Reject for Conformal Classification | `researcher/advanced/index` | `researcher/advanced/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `researcher/advanced/index` | Researcher advanced topics | `researcher/index` | `researcher/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `researcher/advanced/theory_and_literature` | Theory & literature | `researcher/advanced/index` | `researcher/advanced/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `researcher/future_work` | Research Directions | `researcher/index` | `researcher/index` | CE Project, Vision & Evolution | Keep | Preserved |
| `researcher/replication/index` | Replication workflow | `index`, `researcher/index` | `researcher/index` | CE Project, Vision & Evolution | Keep; remove duplicate parent | Preserved |
| `schema_v1` | Explanation Schema v1 | `foundations/reference/index` | `foundations/reference/index` | CE Software & Integration | Keep | Preserved |
| `tasks/classification` | Classification (Binary & Multiclass) | `tasks/index` | `tasks/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `tasks/index` | Tasks and capabilities | `index` | `index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `tasks/probabilistic_regression` | Probabilistic (Thresholded) Regression | `tasks/index` | `tasks/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `tasks/regression` | Conformal Interval Regression (CPS) | `tasks/index` | `tasks/index` | CE in Practice: Explore & Apply | Keep | Preserved |
| `upgrade/index` | Upgrade guides | `index` | `index` | CE Software & Integration | Keep | Preserved |
| `upgrade/v0.11.4-upgrade-checklist` | v0.11.4 Upgrade Checklist | `upgrade/index` | `upgrade/index` | CE Software & Integration | Keep | Preserved |
| `upgrade/v0.11.6-upgrade-checklist` | v0.11.6 Upgrade Checklist | `upgrade/index` | `upgrade/index` | CE Software & Integration | Keep | Preserved |
| `upgrade/v1.0.0-upgrade-checklist` | v1.0.0 upgrade checklist | `upgrade/index` | `upgrade/index` | CE Software & Integration | Keep | Preserved |
| `_autosummary/*` (13 generated API pages) | Generated API reference | `foundations/reference/api` | `foundations/reference/api` | CE Software & Integration | Keep | Preserved |
