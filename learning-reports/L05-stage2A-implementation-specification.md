# L05 Stage 2A - Homepage Implementation Specification

Date: 2026-11-08  
Status: Proposed; implementation requires explicit approval

## Scope

Implement only the approved homepage navigation design. Preserve existing
canonical pages, audience routes, task routes and physical folders. Do not
duplicate full conceptual or API content on the homepage.

## Proposed files

### Required modification

- `docs/index.md`: replace the current audience-first introduction with the
  approved header and five-door navigation, while retaining the existing
  release, ecosystem, demo, audience and toctree links where still accurate.

### Files not to modify in Stage 2B

- `README.md`
- `docs/conf.py`
- `.readthedocs.yaml`
- `src/`
- existing canonical concept, task, API, installation and project pages

### New pages

No new public page is required for the minimum navigation-first implementation.
Door 5.1 may require a future navigation landing page; that decision must be
approved separately. Door 1.1 is future educational content, not an
implementation target.

## Navigation and link targets

Use MyST relative links or `{doc}` roles consistent with current `docs/index.md`.
Recommended targets:

- Door 2: `foundations/concepts/index.md`
- Door 3: `get-started/index.md`
- Door 4: `api/index.md` with `get-started/installation.md`
- Door 5: use a qualified multi-link card to researcher, contributor and
  roadmap pages until a landing page is approved
- Door 3.1: `https://calibrated-explanations-demo.ju.se/`
- Door 3.2: `https://games.grejna.ai/`, explicitly external
- Door 3.3: `foundations/how-to/integrate_with_pipelines.md` and
  `../../notebooks/README.md` only if notebook source linking is confirmed by
  the documentation configuration

Do not use a misleading single destination when a label represents several
different existing pages.

## Sphinx/MyST considerations

- Preserve the existing `{toctree}` groups unless a small homepage-only
  reordering is approved.
- Use standard Markdown headings, tables or MyST grid/list constructs already
  supported by the repository; do not add extensions.
- Keep external URLs explicit and qualified.
- Do not add a page to a toctree merely to make a logical door appear if that
  page is not an approved canonical landing page.
- Check heading hierarchy, duplicate labels, unresolved `{doc}` targets and
  external-link rendering during validation.

## Responsive layout

- Prefer semantic headings and link lists over CSS-dependent fixed squares.
- If compact cards are used, allow labels to wrap and stack at narrow widths.
- Keep the five-door sequence readable in source order and screen readers.
- Avoid relying on color alone to distinguish external, future or qualified
  destinations.
- Preserve the Furo theme's existing admonition and toctree behavior.

## Content and wording safeguards

- Use the exact approved subtitle and introduction.
- Do not add separate Try CE, Get Started or Explore Theory buttons above the
  doors.
- Do not add a separate Why CE section.
- Call the browser demo illustrative.
- Call Decision Labs external and limit claims to repository evidence.
- Describe own-data use as local Python/API workflow.
- Do not call CE EU AI Act compliant.
- Do not infer Grejna AB ownership, endorsement or functionality.
- Do not present `1.1.0-dev`, `v1.0.2` or `1.0.0` as current stable until
  release evidence is reconciled.

## Preservation requirements

Retain discoverable links to:

- `get-started/index.md`
- `practitioner/index.md`
- `researcher/index.md`
- `contributor/index.md`
- `foundations/index.md`
- `tasks/index.md`
- `api/index.md`
- migration, upgrade, plugins, roadmap and citation material

The homepage redesign must not remove audience or task paths.

## Validation plan for Stage 2B

Do not run these commands during Stage 2A. If implementation is approved:

1. `git diff -- docs/index.md` — confirm only approved homepage scope changed.
2. `make quick` — repository fast checks, if available.
3. `sphinx-build -W -b html docs <temporary-output>` or the repository's
   documented equivalent — check MyST parsing, warnings and missing targets.
4. Run the project's link or documentation checks if defined by `Makefile`.
5. Inspect the rendered page at narrow and wide viewport widths.
6. Manually verify each of the five door titles, all 27 labels, audience
   routes, task routes, external-resource qualifiers and version wording.

Expected checks:

- no undefined MyST references;
- no broken local links;
- no removed audience/task routes;
- responsive link grids;
- no unsupported capability or compliance claims;
- no unqualified stable-version claim.

## Risks and rollback

Risks:

- Homepage becomes too dense if all 27 links are shown without hierarchy.
- External resources may change or be unavailable.
- Version inconsistency could make the release notice misleading.
- A new logical door could accidentally imply a new canonical page.

Rollback:

- Keep the change limited to `docs/index.md`.
- Review the diff before any commit.
- Revert only the approved homepage patch if validation fails; do not revert
  unrelated worktree changes.
- If a destination is unsuitable, remove or qualify that link rather than
  inventing replacement content.

## Approval gates

Approval is required for:

1. Direct homepage modification.
2. Any future Door 5 landing page.
3. Any future Door 1.1 educational page.
4. Final stable-version wording.
5. Whether notebook README links are appropriate in published docs.

