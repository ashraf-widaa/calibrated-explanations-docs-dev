# L05 Stage 2D - Phase A: Navigation Audit

Date: 2026-11-09  
Status: **Findings only.** No documentation, navigation or configuration file
was changed.

Evidence comes from the Sphinx environment and rendered sidebar of the last
pinned build (Sphinx 7.4.7, Furo 2025.12.19, 120 source documents), plus the
repository files cited below.

## Summary

The sidebar has four captions that do not match the five homepage sections. It
renders 158 links for 120 distinct targets because 16 pages have more than one
toctree parent. The duplicate Roadmap entry is a heading problem, not a toctree
problem.

Page URLs depend on source file paths, so changing navigation need not change
them. The main obstacle is governance: an active project standard requires
audience-first navigation, which the approved section order cannot fully
satisfy.

## Findings by severity

### Blocker for Phase C

**F1. The approved section order conflicts with active standard STD-004.**

- Evidence: `development/standards/STD-004-documentation-audience-standard.md:34-35`
  says navigation "MUST start with getting-started and audience hubs
  (practitioner, researcher, contributor/maintainer) before deep architecture".
  Line 129 makes this a PR pass/fail check.
- Impact: in the five-section order, theory comes before getting-started, and
  Internal Software Architecture comes before the researcher and contributor
  hubs. A PR implementing this fails the check as written.
- Recommended fix: a Product Owner decision (D1 in the proposal) before Phase C.
- Related: `docs/foundations/governance/nav_crosswalk.md:24-34` records the
  audience-first structure as verified and would become out of date.

### High

**F2. The sidebar does not express the five-section architecture.**

- Evidence: `docs/index.md:288-323` defines four captions: Start here, Core
  references, Companion projects, and Migration and project docs. The homepage
  has five sections (`docs/index.md:34,76,120,164,224`).
- Impact: readers see two different structures.
- Recommended fix: five captioned toctrees (see proposal).

**F3. Sixteen pages have multiple toctree parents.**

- Evidence: section 3 below. Thirty-two link targets appear more than once in
  the rendered sidebar.
- Impact: repeated entries crowd the sidebar, and a page's position depends on
  which parent Sphinx selects.
- Recommended fix: give each page one parent. Most redundant entries are in
  `:hidden:` toctrees, so removing them leaves those page bodies unchanged.

**F4. The duplicate Roadmap comes from a nested H1.**

- Evidence: `docs/ROADMAP.md:1` has `# Roadmap`, then line 3 includes
  `../ROADMAP.md`, whose line 1 is also `# Roadmap`. The sidebar shows
  `ROADMAP.html` and `ROADMAP.html#id1`. Furo's sidebar uses `titles_only=True`,
  so a second H1 becomes an extra entry.
- Impact: changing toctrees alone will not remove this duplicate.
- Recommended fix: remove the wrapper heading at `docs/ROADMAP.md:1`. No inbound
  links to `ROADMAP` anchors were found.

**F5. "BibTeX entries" appears as a page-level sidebar entry for the same reason.**

- Evidence: `docs/citing.md:190` is a second H1.
- Impact: extra entry each time `citing` is listed.
- Recommended fix: make it H2 and move its child headings down one level.

### Medium

**F6. Governance pages sit under practitioner playbooks.**
`docs/practitioner/playbooks/index.md:49-50` lists the release checklist and
section owners, which are maintainer content. Fix: keep them only under
Governance & support.

**F7. Homepage toctrees render as a long link list at the bottom of the page.**
`docs/index.md:288-323` does not use `:hidden:`. Fix: mark them `:hidden:`; Furo
still builds the sidebar from hidden toctrees.

**F8. A test depends on homepage text.**
`tests/docs/test_navigation.py:12-22` requires five hub paths in `docs/index.md`,
and its comment at lines 45-47 says it must not be modified. Those paths also
appear in homepage cards and guided learning paths, and all five stay in the
proposed navigation. Fix: leave the test alone and run it in Phase C.

**F9. The subtitle appears in "On this page".**
`docs/index.md:3` is an H2, so the tagline is listed before the five sections.
It is outside the stated scope; noted for review.

### Low

**F10. Stale tier-map rows.** `docs/appendices/rtd_tier_map.md:97-102` lists six
`standards/` pages that are not part of the build.

**F11. Relocation stub in navigation.** "Telemetry (relocated)"
(`foundations/concepts/telemetry`) is listed under practitioner advanced topics.
It is kept as is; candidate for L06.

## 1. Current top-level sidebar

Furo uses every toctree reachable from the homepage, including hidden ones, and
displays the full depth.

| Caption | Top-level entries (children) |
|---|---|
| Start here | Get started (7), Practitioner hub (4, two with nested lists), Researcher hub (3), Contributor hub (9) |
| Core references | Shared foundations (4 sub-hubs), Tasks and capabilities (4), API Reference (5) |
| Companion projects | Plugins (1), Replication workflow |
| Migration and project docs | Migration guides (3), Upgrade guides (3), Changelog and release references, RTD tier map, CE-First Guide, AI Agent Setup Guide, Legacy Plotting Reference, Comparisons, Roadmap, Roadmap (duplicate), Citing, BibTeX entries |

No `html_sidebars` or Furo navigation options are set in `docs/conf.py`.

## 2. Duplicate entries

| Rendered duplicate | Cause |
|---|---|
| Roadmap / Roadmap | Two H1 headings (F4) |
| Citing + BibTeX entries, shown twice | Two H1 headings (F5) and two parents |
| Migration guides and its 3 children | Listed under Contributor hub and at top level |
| Replication workflow | Listed under Researcher hub and at top level |
| API reference and 13 generated pages | Listed under Reference and Extending guides |

## 3. Pages under multiple branches

| Page | Parents |
|---|---|
| `citing` | `index`, `foundations/reference/index` |
| `migration/index` | `index`, `contributor/index` |
| `researcher/replication/index` | `index`, `researcher/index` |
| `foundations/concepts/alternatives` | `foundations/concepts/index`, `researcher/advanced/index` |
| `foundations/concepts/probabilistic_regression` | `foundations/concepts/index`, `researcher/advanced/index` |
| `foundations/concepts/terminology` | `foundations/concepts/index`, `migration/index` |
| `foundations/governance/nav_crosswalk` | `foundations/governance/index`, `contributor/extending/guides/index` |
| `foundations/governance/optional_telemetry` | `foundations/governance/index`, `contributor/extending/advanced` |
| `foundations/governance/release_checklist` | `foundations/governance/index`, `practitioner/playbooks/index` |
| `foundations/governance/section_owners` | `foundations/governance/index`, `practitioner/playbooks/index` |
| `foundations/how-to/configure_telemetry` | `foundations/how-to/index`, `contributor/extending/guides/index`, `practitioner/advanced/index`, `researcher/advanced/index` |
| `foundations/how-to/export_explanations` | `foundations/how-to/index`, `practitioner/playbooks/index` |
| `foundations/how-to/integrate_with_pipelines` | `foundations/how-to/index`, `contributor/extending/guides/index`, `practitioner/playbooks/index` |
| `foundations/how-to/plot_with_plotspec` | `foundations/how-to/index`, `contributor/extending/advanced`, `practitioner/advanced/index` |
| `foundations/how-to/tune_runtime_performance` | `foundations/how-to/index`, `contributor/extending/advanced`, `practitioner/advanced/index` |
| `foundations/reference/api` | `foundations/reference/index`, `contributor/extending/guides/index` |

## 4. Pages that do not fit the five sections directly

These have no approved subtopic, so each needs a suitable parent:

- Migration guides, upgrade guides and the legacy plotting reference.
- Foundations how-to, reference and governance sub-hubs.
- Changelog links, citation page and RTD tier map.
- AI agent guides: `get-started/ce_first_agent_guide`, `get-started/copilot-setup`.

## 5. Orphan risk

- Currently unreachable by design: `multiclass_all_classes_gap_analysis`, which
  has `orphan` metadata.
- Removing a page's only toctree would create a new orphan, and strict builds
  fail on orphaned pages. Pages with a single parent therefore have to be moved,
  not removed.
- An in-memory simulation of the proposed hierarchy found no newly unreachable
  pages. See the proposal for its limits.

## 6. Canonical destinations for the 27 subtopics

See `L05-stage2D-mapping-table.md`. Of the 27:

- 23 have internal destinations, using 17 distinct pages.
- 2 are external.
- 2 have no page (Understanding AI Models; Vision, Origins & History).

Five pages serve more than one subtopic:

| Page | Subtopics |
|---|---|
| `foundations/concepts/calibrated_interval_semantics` | Can We Trust AI Outputs?; Calibration & Uncertainty; Assumptions & Guarantees |
| `compare` | The Explainability Gap; Evaluate & Compare |
| `tasks/capabilities` | What Is CE & What Does It Add?; Software Overview & Versions |
| `foundations/how-to/integrate_with_pipelines` | Test CE with Your Own Data; Model & Pipeline Integration |
| `plugins` | Extensions & Customization; CE Ecosystem |

## 7. Missing landing pages and gaps

- No page exists for Understanding AI Models or Vision, Origins & History.
- No dedicated page exists for Software Overview & Versions; it borrows the
  capabilities page.
- The five sections have no landing pages. The proposal evaluates whether they
  are needed.

## 8. URLs that must remain stable

Sphinx derives each page URL from its source path. No redirects are configured,
so moving or renaming a source file would break its URL. All 120 current
documents must stay at their existing paths, including the 17 card destinations
and 13 generated API pages. Homepage anchors will change when "Door" is removed;
no inbound links to `door-` anchors were found in `docs/`.
