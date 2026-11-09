# L05 Stage 2D - Phase C Implementation Report

Date: 2026-11-09  
Status: **Conditionally accepted by the Product Owner for local implementation.
Publication not approved.** STD-004 amendment **pending formal standard-owner
approval**. Local closeout results are in the "Closeout" section below.

The homepage and sidebar now share the five approved sections, and every page
has one sidebar parent. The pinned strict build finished with zero warnings and
the navigation tests pass. Read the Docs has not been tested.

## Files changed

| File(s) | Change |
|---|---|
| `docs/index.md` | Removed "Door" from five headings; added Home plus five hidden captioned toctrees; added one sentence linking upgrade and migration guides |
| `docs/sections/getting-started-configuration.md`, `architecture-integration.md`, `api-technical-reference.md` | **New.** Minimal grouping pages: title, one sentence, semantics pointer, toctree, Tier 3 label |
| `docs/foundations/index.md`, `foundations/how-to/index.md`, `foundations/reference/index.md`, `get-started/index.md` | Moved pages out of toctrees and added `{doc}` links so the hub bodies still list them |
| `docs/foundations/concepts/index.md`, `tasks/index.md`, `migration/index.md` | Removed relocated or duplicate toctree lines; bodies already link to them |
| `docs/contributor/index.md` | Removed duplicate Migration entry; added the two AI agent guides |
| `docs/practitioner/playbooks/index.md`, `practitioner/advanced/index.md`, `researcher/advanced/index.md` | Removed duplicate or relocated entries from hidden toctrees |
| `docs/contributor/extending/guides/index.md`, `contributor/extending/advanced.md` | Removed hidden toctrees; all their pages remain linked in the body |
| `docs/ROADMAP.md` | Removed the wrapper H1 |
| `docs/citing.md` | Changed the second H1 to H2 and moved its child headings down one level |
| `docs/appendices/rtd_tier_map.md` | Added three grouping pages as Tier 3 |
| `development/standards/STD-004-documentation-audience-standard.md` | Revised sections 4.1 and 7.6; added amendment note |
| `docs/foundations/governance/nav_crosswalk.md` | Updated structure verification and status note |

No CE source code, dependency, theme, or existing document path changed. Nothing
was staged, committed, pushed or published.

## Validation results

Built with the pinned documentation environment (Sphinx 7.4.7, MyST 3.0.1, Furo
2025.12.19), Python 3.10, using `-E -W --keep-going` with `READTHEDOCS=True`.
Output is in `_build/html`.

| Check | Result | Evidence |
|---|---|---|
| Strict Sphinx build | **Pass** | Exit 0, 0 warnings or errors |
| Broken internal references | **Pass** | None reported by the strict build |
| `tests/docs/test_navigation.py` | **Pass** | 6 passed |
| Duplicate toctree parents | **Pass** | 0 (was 16) |
| Duplicate sidebar links | **Pass** | 122 links, 122 unique (was 158 links, 120 unique) |
| Roadmap and BibTeX sidebar duplicates | **Pass** | One Roadmap entry; no BibTeX sidebar entry |
| New orphans | **Pass** | None; only the existing intentional orphan `multiclass_all_classes_gap_analysis` |
| 27 homepage cards | **Pass** | 27 cards, titles and destinations identical to the previous build |
| Existing page paths | **Pass** | All 134 previous HTML pages still exist; only the 3 grouping pages were added |
| Five sidebar sections, no "Door" | **Pass** | Five captions match the homepage headings |
| External demos homepage-only | **Pass** | No demo links in the sidebar |
| "On this page" headings | **Pass** | Five section names listed; the subtitle is also listed, as before |
| Sidebar rendering | **Pass** | Headless Edge, 1200px: groups expand, current page highlighted |
| Narrow rendering | **Partial** | Headless Edge, 500px homepage only; mobile sidebar drawer not opened |

## Governance status

STD-004 now requires the five approved sections while keeping getting-started
and the practitioner, researcher and contributor hubs directly reachable from
the sidebar and landing page. The Product Owner approved this direction, but
approval by the standard's owner is not established, so both STD-004 and
`nav_crosswalk.md` record it as pending.

## Deviations from the approved proposal

1. **CE Software & Integration uses grouping pages.** As directed by the Product
   Owner, this replaces the proposal's flat list. Three pages in `docs/sections/`
   hold the groups. The positions for this section in
   `L05-stage2D-mapping-table.md` are therefore superseded.
2. **Software Overview & Versions has no sidebar entry.** A toctree can list only
   a page or URL. Showing it would require inventing a page or duplicating the
   capabilities page. Its homepage card still links to `tasks/capabilities`, and
   a dedicated destination remains planned for L06.
3. **`api/index` shows "API Reference" in the sidebar.** The approved label
   "API & Technical Reference" is now the group title. Card 4.4 is unchanged.
4. **The homepage gained one sentence** linking the upgrade and migration guides.
   `test_upgrade_index_in_toctree` requires `upgrade/index` in `docs/index.md`,
   and the toctree entry moved to a grouping page.

## Remaining issues

- `test_upgrade_index_in_toctree` now passes through the homepage link, while the
  real toctree entry is on the grouping page. Its comment about the "THIRD
  toctree group" is out of date; the test was not changed.
- Pytest 9.2.0, which the unpinned requirement installs, crashed on this machine
  even with the project's conftest disabled. The test run used pytest 8.4.2 in
  the temporary environment only. `.venv` has no pytest.
- Not verified: an actual RTD build, Python 3.11, the full CI docs job (which
  executes notebooks), and `make local-checks-pr`.
- The "Trustworthy AI" sidebar label does not carry the homepage's "not evidence
  of compliance" caveat.
- Still open from earlier stages: conflicting version claims, six stale
  `standards/` tier-map rows, the "Telemetry (relocated)" stub, and the missing
  pages for Understanding AI Models and Vision, Origins & History.

## Closeout (local only)

### Product Owner decision

Decision: conditionally accepted for local implementation. Publication status:
not approved. The remaining verification items do not reopen the navigation
architecture. Next milestone: L06 - Documentation Content, Learning Paths &
Cross-Linking.

| Publication condition | Status after closeout |
|---|---|
| Formal approval of the STD-004 amendment | **Open**: pending the standard's owner |
| Verify the RTD build and mobile/dark-theme navigation | **Partly closed**: mobile and dark theme verified locally; RTD build not run |
| Resolve the malformed external link and check affected heading anchors | **Closed locally** |
| Confirm the applicable repository CI checks | **Open**: requires the changes to reach GitHub, which was out of scope |

### Changes made

Only `docs/index.md` changed in this closeout:

- **Grejna link.** Every Markdown link form tested (inline, reference and
  autolink, including a pre-escaped `&amp;` source) double-escaped `&` under the
  pinned MyST 3.0.1. The paragraph now uses MyST's `{eval-rst}` directive, with a
  longer outer fence on the notice. Tested under MyST 3.0.1 and 5.1; both produce
  a correctly escaped link. No other link in the built site is double-escaped.
- **Anchor.** Added a `(companion-projects)=` target so the published
  `index.html#companion-projects` link still resolves. It lands on CE Project,
  Vision & Evolution.

### Anchor check

Compared with the build before Phase C:

| Page | Result | Action |
|---|---|---|
| `citing.html` | 41 anchors before and after; none lost | None |
| `ROADMAP.html` | Only auto-generated `#id1` lost, which pointed to the duplicate top heading | None; a missing anchor also opens at the top of the page |
| `index.html` | Five `door-*` anchors replaced | None; "Door" headings were never committed, so these were not published |
| `index.html` | `#companion-projects` was the only committed section anchor at risk | Preserved with a target |

No inbound links to the changed anchors were found in `docs/`. External inbound
links cannot be checked locally.

### Validation results

Pinned environment (Sphinx 7.4.7, MyST 3.0.1, Furo 2025.12.19), Python 3.10,
`-E -W --keep-going`, `READTHEDOCS=True`. Output is in `_build/html`.

| Check | Result | Evidence |
|---|---|---|
| Strict Sphinx build | **Pass** | Exit 0, 0 warnings or errors |
| `tests/docs/test_navigation.py` | **Pass** | 6 passed (pytest 8.4.2, temporary environment) |
| Grejna link | **Pass** | `href` decodes to the exact URL; no `&amp;amp;` in built hrefs |
| Duplicate parents and sidebar links | **Pass** | 0 multi-parent pages; 122 links, 122 unique |
| New orphans | **Pass** | Only the existing intentional orphan |
| 27 cards and page paths | **Pass** | Cards identical; 134 previous pages kept, 3 grouping pages added |
| Mobile drawer | **Pass** | Real hamburger control opens it; overlay closes it; group expands to 4 visible children; 5 sections visible |
| Dark theme | **Pass** | Real theme toggle sets dark; sidebar and cards themed on desktop and in the drawer |
| Dark sidebar contrast | **Pass** | Links 5.6:1 and captions 4.66:1 against the sidebar background |

Browser checks used headless Edge against a scratch copy of the built site, with
a test script clicking Furo's own controls. The repository build was not altered.

Limits: Edge's layout width bottomed out at about 496px, so true phone widths
were not tested, and no physical device was used. Drawer opening was confirmed
by screenshot in dark mode, while the position reading did not update under
headless virtual time. Light-mode drawer state was confirmed from control state
only.

### Remaining publication blockers

1. Formal approval of the STD-004 amendment.
2. An actual Read the Docs build.
3. The applicable repository CI checks, including the docs job that executes
   notebooks, on Python 3.11.

The other outstanding items in "Remaining issues" do not block navigation but
should be reviewed. The Grejna paragraph can return to plain Markdown once the
pinned MyST version no longer double-escapes URLs.

## Review gate

Local closeout is complete. Do not publish to Read the Docs until the blockers
above are resolved.
