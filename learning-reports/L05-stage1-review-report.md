# L05 Stage 1 Review Report

## Task ID and title

- Task ID: L05 Stage 1
- Title: CE Homepage and Five-Door Navigation Design

## Completion status

- Homepage wireframe completed.
- Five-door navigation design completed.
- Homepage link and evidence map completed.
- No documentation source files were modified.
- No new public documentation pages were created.
- No files were moved or renamed.
- No Sphinx/Read the Docs build was run.
- No packages were installed.
- No files were staged or committed.
- Waiting for review and explicit approval before Stage 2 implementation.

## Objective

Prepare an evidence-based homepage and navigation design using the five-door
hybrid architecture while preserving existing audience, task and physical
documentation paths.

## Inspection and evidence used

- L04 current documentation inventory, five-door mapping, gap analysis and
  navigation blueprint.
- L04 addendum resource verification for browser demo, Decision Labs, notebooks,
  Grejna AB, versions and installation.
- Existing homepage, Get started, foundations, task, practitioner, researcher,
  contributor, API, migration and upgrade pages.
- README, package metadata, changelog, citation metadata, roadmap, development
  map and relevant source/API locations.

## Design conclusions

1. The homepage should explain CE briefly before routing users.
2. Five doors should be visible as logical questions, while audience and task
   journeys remain parallel routes.
3. Door 3 should distinguish the verified browser demo, the limited
   repository evidence for Decision Labs, notebook learning resources, and the
   verified local-code pipeline route.
4. Door 4 should link canonical installation, API, architecture and integration
   pages without presenting internal modules as stable public API.
5. Door 5 should distinguish public project information, maintainer records,
   research directions, companion projects and optional commercial services.
6. No homepage wording should promise browser upload, Decision Labs CE
   functionality, regulatory compliance, ownership, or a specific current stable
   version until those questions are resolved.

## Important blockers

- No verified browser or Decision Labs own-data upload workflow.
- External demo and Decision Labs runtime behavior were not tested.
- Version references are inconsistent: local `1.1.0-dev`, release metadata
  `v1.0.2`, and homepage wording `1.0.0`.
- Door 1 and the prerequisite layer of Door 2 do not yet have single canonical
  public landing pages.
- The intended status of the five doors (visible navigation versus planning
  model) still requires approval.

## Deliverables

- `learning-reports/L05-homepage-wireframe.md`
- `learning-reports/L05-five-door-navigation-design.md`
- `learning-reports/L05-link-and-evidence-map.md`
- `learning-reports/L05-stage1-review-report.md`
- `LEARNING_JOURNAL.md` updated with a concise L05 Stage 1 entry

## Recommended approval decision

Approve a navigation-first Stage 2 pilot only after deciding:

1. whether five-door labels should appear publicly on the homepage;
2. which existing page should be the Door 1 and Door 5 landing destination;
3. how the `1.0.0`/`v1.0.2`/`1.1.0-dev` version wording will be reconciled;
4. whether notebooks should receive a homepage link;
5. whether the practical “own data” route should be explicitly labelled as local
   Python/API integration.

## Recommended Stage 2 scope if approved

Use existing pages only:

- add a concise homepage value proposition and What & Why block;
- add five qualified door links;
- add quick actions for demo, first quickstart, installation and integration;
- preserve audience/task routes;
- add explicit caveats for external resources and version status.

No new page or folder should be created until the navigation pilot is reviewed.

