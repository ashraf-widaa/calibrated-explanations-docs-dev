# L05 Stage 2D - Phase B: Proposed Unified Navigation

Date: 2026-11-09  
Status: **Proposal only, awaiting Product Owner approval.** Nothing here has been
implemented.

## Recommendation

Replace the four homepage toctrees with five hidden, captioned toctrees that
match the homepage sections, and give every page exactly one parent. No pages
move, no pages are created and no URLs should change.

Before implementation, decide how to handle the STD-004 conflict (D1).

## Proposed sidebar

Key:

- **[L]** approved label shown for an existing page
- **[P]** existing page or hub under its own title
- `(+)` keeps children

```text
Home (site title; optional "Home" entry, see limits below)

CE: What & Why
  [L] Trustworthy AI                    practitioner/playbooks/eu-ai-act-compliance
  [L] The Explainability Gap            compare
  [L] What Is CE & What Does It Add?    tasks/capabilities

How CE Works: The Theory Behind It
  [L] Essential Foundations (+)         foundations/index -> Concepts & architecture
  [L] Calibration & Uncertainty         foundations/concepts/calibrated_interval_semantics
  [L] Statistical Methods Behind CE     foundations/concepts/probabilistic_regression
  [L] How CE Explanations Work          foundations/how-to/interpret_explanations

CE in Practice: Explore & Apply
  [L] Practical Workflows (+)           get-started/index
  [P] Tasks and capabilities (+)        tasks/index
  [P] Practitioner hub (+)              practitioner/index
  [P] How-to guides (+)                 foundations/how-to/index

CE Software & Integration
  [L] Installation & Configuration      get-started/installation
  [L] Internal Software Architecture    foundations/concepts/architecture
  [L] API & Technical Reference (+)     api/index
  [P] Reference (+)                     foundations/reference/index
  [L] Model & Pipeline Integration      foundations/how-to/integrate_with_pipelines
  [L] Extensions & Customization (+)    plugins
  [L] Troubleshooting & Upgrades        get-started/troubleshooting
  [P] Migration guides (+)              migration/index
  [P] Upgrade guides (+)                upgrade/index
  [P] Legacy Plotting Reference         maintenance/legacy-plotting-reference

CE Project, Vision & Evolution
  [L] Research & Publications (+)       researcher/index
  [P] Citing calibrated-explanations    citing
  [L] Development & Roadmap             ROADMAP
  [P] Changelog and release references  appendices/changelog_links
  [L] Community & Contributions (+)     contributor/index
  [P] Governance & support (+)          foundations/governance/index
  [P] RTD tier map                      appendices/rtd_tier_map
```

Not in the sidebar:

| Type | Items | Reason |
|---|---|---|
| Planned or missing content | Understanding AI Models; Vision, Origins & History | No page exists; no destination is invented |
| External resources | CE Examples for New Users; Explore Use-Case Examples | Homepage cards carry caveats a sidebar link would lose (D2) |
| Conceptual labels sharing a page | Can We Trust AI Outputs?; Assumptions & Guarantees; Test CE with Your Own Data; Evaluate & Compare; Software Overview & Versions; CE Ecosystem | Their page is listed once, under another label |

The homepage still shows all 27 cards with their existing destinations.

## Design rules

1. **One page, one parent.** Multiple cards can link to a page, but it appears
   once in the sidebar.
2. **Approved labels where a page is the primary home of a subtopic.** Toctree
   entries can display a label different from the page title. The page's own
   title does not change.
3. **Existing hubs keep their titles.** They are specialist routes rather than
   approved subtopics.
4. **Native Sphinx only.** No new extensions, CSS, JavaScript, theme settings or
   dependencies.

## Planned Phase C changes (after approval)

| File(s) | Change |
|---|---|
| `docs/index.md` | Remove "Door" from five headings; replace four toctrees with five hidden captioned toctrees |
| `foundations/index`, `foundations/how-to/index`, `foundations/reference/index`, `get-started/index` | Move relocated pages out of the toctree and add plain `{doc}` links so each hub's page body still lists them |
| `foundations/concepts/index`, `tasks/index`, `migration/index` | Remove relocated or duplicate toctree lines; the pages already link to them in the body |
| `contributor/index` | Remove duplicate Migration entry; add the two AI agent guides |
| `practitioner/playbooks/index`, `practitioner/advanced/index`, `researcher/advanced/index` | Remove duplicate or relocated entries from hidden toctrees |
| `contributor/extending/guides/index`, `contributor/extending/advanced` | Remove hidden toctrees; all their pages are duplicates and remain linked in the body |
| `docs/ROADMAP.md` | Remove the wrapper H1 |
| `docs/citing.md` | Change the second H1 to H2 and move its children down one level |

This touches 16 files, nearly all in toctree blocks. It requires no content
migration.

## Section landing pages

**Recommendation: do not create them now.**

| | Captions only (recommended) | Five landing pages |
|---|---|---|
| New files | None | Five, each needing a tier label and tier-map row |
| Sidebar section titles | Not clickable, always visible | Clickable and collapsible |
| Duplication | None | Repeats homepage cards |
| Scope fit | Stays within toctree changes | Adds new pages |

If you later want clickable section titles, the intended files would be
`docs/sections/what-and-why.md`, `how-ce-works.md`, `in-practice.md`,
`software-and-integration.md` and `project-and-evolution.md`. Each would hold a
title, one-sentence description, tier label and toctree. They could be added
later without changing any URL.

## Decisions needed

**D1. How should the STD-004 conflict be handled? (Required before Phase C)**

- **Option A (recommended): amend STD-004** sections 4.1 and 7.6 to recognise the
  five-section structure while keeping audience routes prominent, then update
  `nav_crosswalk.md`. It keeps the approved architecture and fixes the conflict
  at its source, but needs agreement from whoever owns the standard.
- **Option B:** add a short "Start here" group above the five sections. This
  satisfies the standard without amending it, but gives six groups and departs
  from "exactly five".
- **Option C:** proceed with a recorded exception. This is quickest, but leaves
  the PR check failing for upstream contribution.

**D2. Should the two external demos appear in the sidebar?** Recommendation: no,
until their behaviour is verified, because the sidebar cannot carry their
caveats.

**D3. Do you accept the primary homepages for shared pages?** Proposed: semantics
in How CE Works, `compare` and capabilities in What & Why, pipeline integration
and plugins in Software & Integration. Trade-off: a reader arriving from a
different card will see the page highlighted in its primary section.

**D4. Should Trustworthy AI use the EU AI Act page in the first section?** It
fills the approved subtopic but separates that page from its sibling EU data and
liability playbook. The sidebar label also omits the homepage's "not evidence of
compliance" caveat, although the page itself is unchanged.

**D5. Do you approve the small non-toctree edits?** These are the `{doc}` links
in four hubs and the heading fixes in `ROADMAP.md` and `citing.md`, which are
needed to preserve hub listings and remove duplicates.

## Evidence and limits

An in-memory simulation applied this design to the toctree graph from the last
pinned build:

| Measure | Current | Proposed (simulated) |
|---|---|---|
| Pages reachable from the homepage | 119 of 120 | 119 of 120 |
| Pages with multiple parents | 16 | 0 |
| Newly unreachable pages | n/a | 0 |
| Unknown toctree targets | n/a | 0 |
| Top-level entries by section | n/a | 3, 4, 4, 10, 7 |

**A trial build was not run.** Copying the docs to a temporary folder for one was
denied, so these points must be confirmed in Phase C:

- Sphinx accepts captions containing colons and labels containing `&`.
- Furo renders a `Home <self>` entry correctly.
- Current-page highlighting works with custom labels.
- The two heading fixes behave as expected.
- The strict build and all documentation URLs are unchanged.
- Previous/next page links will follow the new order. This is expected.

If any of the Phase C checks reveals wider restructuring, I will stop and report
it rather than expand the scope.

## Deferred to L06

- Dedicated pages for the two missing subtopics and Software Overview & Versions.
- The educational content of any page.
- Cleanup of the stale tier-map rows and the "Telemetry (relocated)" stub.
