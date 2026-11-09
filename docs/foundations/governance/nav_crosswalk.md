# Navigation crosswalk

Track where legacy documentation pages now live in the **Standard-004** five-section
navigation, which keeps direct audience routes. Update this checklist whenever a page moves or is retired.

> **Status note:** Last updated 2026-11-09 · Per Standard-004 (Documentation Audience Standard; five-section amendment pending formal standard-owner approval) · Supersedes ADR-022.

## Legacy → New location mapping

| Legacy page | New location | Notes |
| ----------- | ------------ | ----- |
| `calibrated_explanations.rst` (legacy landing page) | :doc:`../../index` | Landing narrative split into role-based overview and section toctrees with audience-first callouts. |
| `getting_started.md` | :doc:`../../get-started/index` with :doc:`../../get-started/installation`, :doc:`../../get-started/quickstart_classification`, :doc:`../../get-started/quickstart_regression`, :doc:`../../get-started/troubleshooting` | Content decomposed into dedicated installation, runnable quickstarts, and troubleshooting checklists. |
| `practitioner_guide.md` (legacy) | :doc:`../../practitioner/index` with :doc:`../../practitioner/playbooks/index` and :doc:`../../practitioner/advanced/index` | Practitioner core and advanced workflows split: core focuses on factual/alternative explanations; advanced collects optional telemetry and performance tooling. |
| `researcher_guide.md` (legacy) | :doc:`../../researcher/index` with :doc:`../../researcher/replication/index` and :doc:`../../researcher/advanced/index` | Research content consolidated: replication workflows, benchmark manifests, and literature map in one hub with advanced observability extras. |
| `contributor_guide.md` (legacy) | :doc:`../../contributor/index` with :doc:`../../contributor/plugin-contract` and :doc:`../../contributor/extending/guides/index` | Contributor paths split: plugin contract first (core requirement), then extending guides for CLI and configuration surfaces. |
| `viz_plotspec.md` | :doc:`../how-to/plot_with_plotspec` | PlotSpec guidance converted to a how-to focused on configuration plus telemetry links. Practitioner playbooks reference this for advanced visualization. |
| `architecture.md` | :doc:`../concepts/index`, :doc:`../concepts/alternatives`, :doc:`../concepts/probabilistic_regression` | Architecture material split into focused concept pages; optional telemetry moved under :doc:`../governance/optional_telemetry` so provenance scaffolding is clearly opt-in. |
| *(new)* interpretation guide | :doc:`../how-to/interpret_explanations` | Primary resource for reading factual and alternative explanations, PlotSpec visuals, and telemetry provenance. Linked from all quickstarts. |
| `plugin_guide.md` (legacy) | :doc:`../../contributor/plugin-contract` with :doc:`../../contributor/extending/guides/index` and :doc:`../../appendices/external_plugins` | Plugin contract elevated in contributor hub; extending guides cover wiring; the plugin catalog distinguishes official companion, core-provided optional, and community components. |
| `pr_guide.md` | :doc:`../governance/pr_guide` and :doc:`../governance/section_owners` | Governance actions captured under maintainership docs with owners and release narrative under shared foundations. |
| *(new)* migration guides | :doc:`../../migration/index` | Terminology changes, breaking changes, and upgrade guidance captured in a dedicated section linked from all audience hubs. |

## Five-section structure verification

Per Standard-004 (amendment pending formal standard-owner approval), the sidebar uses
the five approved sections and keeps direct audience routes:

- [x] **CE: What & Why** holds orientation pages
- [x] **How CE Works: The Theory Behind It** holds shared foundations and core theory pages
- [x] **CE in Practice: Explore & Apply** holds Get started, Tasks and capabilities, the Practitioner hub, and How-to guides
- [x] **CE Software & Integration** groups setup and upgrades, architecture and integration, and API and technical reference
- [x] **CE Project, Vision & Evolution** holds the Researcher hub, Contributor hub, roadmap, citation, changelog, and governance pages
- [x] Each page has one sidebar parent, and page paths are unchanged
- [ ] Re-run the gating commands in :doc:`release_checklist` after updating cross-references

## Verification checklist

- [ ] Confirm all pages in the mapping table are added to their respective section toctrees
- [ ] Ensure deprecated filenames or redirects point readers to the new audience-first paths
- [ ] Validate that classification and regression parity is maintained across quickstarts and advanced guides
- [ ] Confirm interpretation guides are linked from every quickstart (classification and regression)

## Navigation patterns to maintain

When editing audience landing hubs, playbooks, or quickstarts, follow these patterns:

1. **Interpretation-first callouts:** All quickstarts (classification and regression) link to :doc:`../how-to/interpret_explanations` immediately after the runnable code block.
2. **Parity enforcement:** Practitioner and researcher pages must provide equivalent coverage for binary/multiclass classification and probabilistic/interval regression.
3. **Research hub references:** Audience hubs can point readers to :doc:`../../researcher/index` in a Resources or Further Reading section to avoid navigation clutter.
4. **Plugin boundaries:** Contributor and practitioner docs route stable
   discovery through :doc:`../../appendices/external_plugins`, while the
   official plugin repository owns the changing package inventory and
   compatibility details.
5. **Cross-link validation:** After structural changes, run `sphinx-build -b html -W` and check for broken cross-references in the build log.
