# Stage 11 — Whole-site integration

**Started:** 2026-11-12 12:31 · **Completed:** 2026-11-12 12:45
**Starting branch / commit:** `docs-dev/autonomous-20261112` / `34ebe0ed`

## Objective

Make the entry points independently usable and connected; resolve the main structural gap left after Stages 02–10.

## Problem

**IN-1:** the five section landing pages behind the homepage cards were `orphan: true` and absent from the sidebar. A reader who left a landing page lost the section's map, and the sidebar groups showed different pages from the landing cards (Step 9 E-03, full review C-07).

## Change

| File | Change |
|---|---|
| `docs/index.md` | First entry "Overview <sections/…>" added to the five sidebar groups (What & Why, How CE Works, CE in Practice, Software & Integration, Project). Captions and every other entry unchanged |
| `docs/sections/{what-and-why,how-ce-works,in-practice,software-integration,project-evolution}.md` | `orphan: true` front matter removed |
| `tests/docs/test_section_landing_pages.py` | 5 tests: each landing page is the "Overview" entry of its group and not an orphan |

## Integration review (whole site, after Stages 02–11)

| Check | Result |
|---|---|
| Sidebar (navigation diff against the Stage 10 build) | 129 → 134 links: +5 "Overview" entries, 0 removed |
| Previous/next | Follows the sidebar order (for example Overview of In Practice → Tasks; Overview of Software → Software Foundations) |
| Strict builds | Beta: 0 warnings; standard (non-Beta): 0 warnings; "CE Beta Documentation" marker present only in the Beta build |
| Docs tests | 262 passed |
| Links and anchors | 150 pages, 0 broken; page set unchanged since Stage 02 |
| Visual | Sidebar renders the five Overview entries; In Practice landing has no horizontal scroll at 1440 or 390 px |

**Cross-area transitions now present** (✗ → ✓ compared with full review Report D.1):

| From → To | Before | After |
|---|---|---|
| Quick Start → Software | partial | ✓ ("After the Quick Start", walkthrough table) |
| Quick Start → How CE Works (methods) | partial | ✓ (index + walkthrough) |
| How CE Works (semantics, tasks) → methods | ✗ | ✓ |
| Practice → notebooks, Expert Hub | ✗ | ✓ |
| Software → configuration and operations | ✗ | ✓ |
| Project → support and feedback | ✗ | ✓ |
| Research hub → methods, citing | ✗ | ✓ |
| Any section → its own map | homepage only | ✓ (sidebar "Overview") |
| Glossary ↔ landing pages | 2 links | 13 contextual entry points |

## Remaining (recorded for the final report)

- What & Why still has no inbound links from Practice or Software (only the homepage and sidebar).
- Duplicate operational clusters (performance ×3, reject ×3, plugins ×5, telemetry ×3) were not consolidated; this needs a content-diff audit before anything is merged.

## Commit, push, publication

- **Commit:** see `RUN-STATUS.md`.
- **Pushed:** no (B-01).
