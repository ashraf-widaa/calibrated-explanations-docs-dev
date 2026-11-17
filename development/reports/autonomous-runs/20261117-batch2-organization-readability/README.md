# Batch 2 — Documentation organization and readability

## Authorization and baseline

- Approved scope: Batch 2 only (Product Owner approval, 2026-11-17), following
  Preserve → Reorganize → Clarify → Extend.
- Baseline: Batch 1 commit `77026e80d082ca7954d1d1d6158af588077c4e30` on
  `beta/enhancement-20261117-b1`.
- Implementation branch: `beta/enhancement-20261117-b2`, created at that commit in
  the existing isolated worktree `D:/Jönkoping/CE-Documentation-Redesign/ce-enhancement-20261117`.
- Official comparison remains pinned to `371bd8060bd279fbfd41f7509097617561ac1ae4`.
- Not authorized and not done: commits, merges, pushes, publication, Batches 3–5.

The four main sections, Project & Resources, the sidebar order and all page URLs
are unchanged. No page was created or deleted. No CE source, equation,
derivation, example code, numeric output, figure, CSS, template, notebook or
generated walkthrough file was modified.

## File-by-file change summary

All paths are relative to `docs/` unless stated.

| File | Change | Reason |
|---|---|---|
| `index.md` | Added a definition and purpose paragraph inside the existing hero copy; sidebar label `The Explainability Gap` → `Comparison with Other Methods`. | The homepage named CE but did not define it; the label did not describe a comparison page. |
| `get-started/index.md` | Opening definition aligned with the shared definition; a visible "To run CE now" route (installation → Python walkthrough or tutorials, Quick API) placed directly after the qualifications; `Before you start` renamed `Reference and further reading`, with its install/run items moved up and its old anchor kept as `(before-you-start)=`. | The opening said CE "gives each prediction a range", inconsistent with Batch 1 (bounds on request); the executable route was below the figure and path cards. |
| `what-is-ce.md` | First paragraph: "calibrated predictions, with lower and upper bounds available on request"; "feature's effect" → "feature's weight". | Aligns the authoritative definition with Batch 1 and with the homepage and Quick Start wording. |
| `sections/what-and-why.md` | One sentence states the section's progression (What CE Is → comparison → regulatory context). | Conceptual progression without a navigation inventory (guarded by an existing test). |
| `sections/how-ce-works.md` | Merged the two standalone pointer lines into an introduction that states the page chain, links the semantics reference and points newcomers to Essential Foundations and the glossary; removed the duplicate foundations mention at the end. | Repeated orientation; prerequisites were only mentioned last. |
| `sections/in-practice.md` | New two-sentence route; the same ten cards grouped under *Run CE in Python*, *Apply and evaluate*, *Explore in the browser*; card `Compare with Other Methods` → `Comparison with Other Methods`; the generic pointer folded into the demo caveat. | Ten ungrouped cards mixed executable documentation with external demos. |
| `sections/software-integration.md` | Removed generic guarantees pointer; `Troubleshooting & Upgrades` → `Troubleshooting`; `Upgrades & Migration` → `Upgrade Guides`; added `Migration Guides` card (existing `migration/index`, already in the Maintenance & Support sidebar group). | The two cards overlapped and migration was reachable only from the sidebar. |
| `sections/software-foundations.md`, `development-integration.md`, `maintenance-support.md`, `project-evolution.md` | Removed the identical "For guarantees, assumptions and non-guarantees" line. | Repeated on pages about installation, APIs, troubleshooting and the project, where it does not apply. |
| `sections/software-overview-versions.md` | Removed the same line; added *Stability statement of the 1.0.0 release*, restoring the official homepage statement as a historical, version-specific statement with links to the v1.0.0 upgrade checklist, Schema v1 freeze and release notes. | Official content from `index.md@371bd806` was not present in the Beta. |
| `tests/docs/test_section_landing_pages.py` (repo root) | In Practice link-order guard updated to the grouped order (same ten destinations) plus group headings; new guards for the version-scoped 1.0.0 statement and the single `compare` label. | Keep the new organization and restored content protected. |

## Official-content preservation assessment

- **Restored:** the 1.0.0 stable-API statement, scoped to the 1.0.x release line, and
  its upgrade-checklist, Schema v1 and release-notes links (official `index.md`).
- **Preserved and more visible:** the official Quick Start purpose ("pick one quickstart
  and run it end to end") as the *To run CE now* route; installation and Quick API links.
- **Still reachable, unchanged:** web demo, PyPI (Installation), issue tracker
  (Project & Resources), replication and plugins pages, migration and upgrade guides.
- **Official headings unchanged:** `compare.md`, `calibrated_interval_semantics.md`,
  `interpret_explanations.md` and all other official H1s. Only sidebar labels and card
  titles were adjusted.
- **Official pointers kept:** semantics pointers on official pages (`tasks/index.md`,
  `practitioner/index.md`, tutorials and quickstarts) and the homepage pointer guarded
  by `test_homepage.py` were not removed. Only Beta-added duplicates on section pages were.
- **Batch 1 preserved:** the Quick Start "What CE gives you" list and its qualification
  paragraph are untouched; the new definitions use Batch 1's request-dependent bounds.

## Navigation and naming consistency

| Page | Sidebar | Card / link text | H1 (unchanged) |
|---|---|---|---|
| `compare.md` | Comparison with Other Methods | Comparison with Other Methods | Calibrated Explanations comparisons (CE-first) |
| `migration/index.md` | Migration guides (subpage) | Migration Guides (new card) | Migration guides |
| `upgrade/index.md` | Upgrade guides (subpage) | Upgrade Guides | — |
| `get-started/troubleshooting.md` | Troubleshooting (subpage) | Troubleshooting | — |

Sidebar order, toctree membership and every URL are unchanged.

## Anchors

Every HTML `id` present in the Batch 1 build of the 12 changed pages is still present.
Retained deliberately: `read-in-this-order` and `pages-in-this-section` spans
(external-link compatibility) and `before-you-start` (explicit label on the renamed
section). Added ids: `reference-and-further-reading`, `run-ce-in-python`,
`apply-and-evaluate`, `explore-in-the-browser`, `stability-statement-of-the-1-0-0-release`.

## Validation

| Check | Result |
|---|---|
| Documentation test suite (`tests/docs`) | **367 passed**, 0 failed (365 from Batch 1 + 2 new guards). One existing `CE_DOCS_BETA` `UserWarning`, not suppressed. |
| Strict Sphinx build (`-W --keep-going -E`, `nbsphinx_execute=never`) | **Succeeded, 0 warnings**. |
| Internal links | **158 pages, 0 broken links**. |
| Anchor comparison against the Batch 1 build | **0 ids lost** on all changed pages. |
| Protected content vs `77026e80` | Fenced code, `{raw}` figure HTML, `{math}` and display math in every changed file: **byte-for-byte equal**. |
| Validation integrity | SHA-256 of all 1,817 tracked files before and after validation: **0 changes**. |
| Rendering | Homepage at 1366 px and 390 px (no horizontal scroll; definition above the decorative wave); Quick Start (run route above the fold); In Practice (three groups, ten cards). |
| `git diff --check` | Clean. |

A first strict build reported a `ROADMAP.md` heading warning. This was caused by
the temporary source copy omitting the repository-root `ROADMAP.md` that
`docs/ROADMAP.md` includes; after copying it, the build passed with 0 warnings.
No documentation change was involved.

Not executed: RTD's Python 3.11 environment, a clean installation test, fresh
notebook execution, and `make local-checks-pr` (mypy and ruff are unavailable in
the existing environment; nothing was installed). Mobile rendering of the Quick
Start and section pages was not separately captured.

Environment: Python 3.13.7 (`C:/Python313`), pytest 9.0.3, Sphinx 7.4.7; CE imported
from this worktree (`1.1.0.dev0`). Raw evidence is outside the repository in
`C:/Users/ashra/AppData/Local/Temp/ce-batch2-OM82495W/` (`pytest.log`, `pytest.xml`,
`sphinx.log`, `internal-links.log`, `tracked-before.sha`, `tracked-after.sha`) and
screenshots in `D:/Jönkoping/CE-Documentation-Redesign/.playwright-mcp/b2-*.png`.

## Remaining issues and recommendations

1. `compare.md` keeps the official H1 *Calibrated Explanations comparisons (CE-first)*;
   a heading change to match the label would need author approval.
2. The Quick Start still links the semantics page twice (qualification paragraph and
   *Go deeper*); the second form is pinned by `test_quickstart_continuity.py`.
3. `foundations/how-to/index.md` (official) introduces itself as production recipes but
   also contains interpretation; runtime and telemetry guides appear under both
   In Practice and Software. Left unchanged as official content; candidate for author review.
4. The Batch 1 report's statement that Batch 1 "remains uncommitted" is historical.
5. Open scientific items SR-01, SR-02, SR-03/13, SR-07/09/14, SR-15 and endpoint
   compatibility remain open; this batch closes none.

Batch 2 is uncommitted and awaits Product Owner review.
