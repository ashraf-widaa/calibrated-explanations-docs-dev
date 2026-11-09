# CE Documentation Learning Journal

## 1. Project overview and learning objectives

### Project title
Calibrated Explanations Documentation Review and Redesign.

### Purpose
This journal records what is learned while evaluating and redesigning documentation in a local independent copy of the Calibrated Explanations project.

### Long-term objective
Create a comprehensive, beginner-friendly student manual based on real project work, decisions, and lessons.

### Learning objectives
- Learn core Git and GitHub concepts for documentation work.
- Learn how VS Code supports editing and project navigation.
- Learn Markdown for structured technical writing.
- Learn how Sphinx turns source documentation into HTML pages.
- Learn how Read the Docs builds, hosts, and publishes documentation.
- Learn a repeatable documentation workflow: Understand -> Inspect -> Plan -> Approve -> Implement -> Verify -> Document.

## 2. Project resources and workspace

### Reference resources
- Original documentation: https://calibrated-explanations.readthedocs.io/en/stable/
- Original GitHub repository: https://github.com/Moffran/calibrated_explanations

### Local workspace
- Workspace path: D:/Jonkoping/CE-Documentation-Redesign/calibrated_explanations
- Scope: Local independent redesign effort.
- Rule: Original repository and published documentation must remain unchanged.

### Key documentation files (for orientation)
- docs/ : source documentation directory.
- docs/index.md : documentation homepage source.
- docs/conf.py : Sphinx configuration file.
- .readthedocs.yaml : Read the Docs build configuration file.

## 3. Roles and working methodology

### Roles
- Student or project owner: learns, evaluates, and approves changes.
- ChatGPT: tutor, documentation architect, and reviewer.
- GitHub Copilot: technical implementation assistant.

### Working methodology
Understand -> Inspect -> Plan -> Approve -> Implement -> Verify -> Document

### Practical example
Example flow for one lesson:
1. Understand the concept and expected output.
2. Inspect relevant files and project structure.
3. Plan one small safe change.
4. Approve the plan.
5. Implement only the approved change.
6. Verify the result.
7. Document what was learned and why decisions were made.

## 4. Learning roadmap

| Stage | Focus | Status | Notes |
|---|---|---|---|
| Stage 1 | Foundations: GitHub, Sphinx, Read the Docs, project layout | In progress | Started in Lesson 1 |
| Stage 2 | Documentation inspection and navigation analysis | Planned | Lesson 2 |
| Stage 3 | Redesign planning and information architecture | Planned | To be started after inspection |
| Stage 4 | Incremental implementation and verification | Planned | Changes approved before implementation |
| Stage 5 | Consolidation into student manual sections | Planned | Ongoing during all stages |

## 5. Chronological learning journal

Use this section to record lessons in order. Keep entries short, factual, and easy to expand.

### Entry template (reuse for each lesson)

#### Lesson [Number] - [Title]
- Date: [YYYY-MM-DD]
- Status: Planned | In progress | Completed | Completed (unverified in this task)
- Objective:
- Concepts learned:
- Actions performed:
- Evidence checked:
- Outcome:
- Open questions:
- Next step:

### Lesson 1 - Understanding GitHub, Sphinx and Read the Docs
- Date: Not recorded in this task
- Status: Completed (unverified in this task)
- Completion report: learning-reports/L01-completion-report.md
- Objective: Build a basic mental model of the documentation toolchain.
- Concepts learned:
  - GitHub stores source files and development history.
  - Sphinx builds documentation into HTML.
  - Read the Docs automates building, hosting, and publishing documentation.
  - docs/ contains documentation source files.
  - docs/index.md is the homepage source.
  - docs/conf.py contains Sphinx configuration.
  - .readthedocs.yaml contains Read the Docs build configuration.
- Actions performed (previously reported, not independently verified here):
  - Cloned the original repository into the local workspace.
  - Removed the original Git remote.
  - Opened the repository in VS Code.
- Evidence checked: Not independently verified in this task.
- Outcome: Foundational concepts documented.
- Open questions: None recorded yet.
- Next step: Continue with structural inspection in Lesson 2.

### Lesson 2 - Exploring the CE Documentation Structure
- Date: 2026-11-06
- Status: Completed
- Completion report: learning-reports/L02-completion-report.md
- Objective:
  - Inspect the documentation architecture before proposing any redesign.
  - Verify how navigation is defined and whether Contributor homepage links resolve.
- Concepts learned:
  - Documentation source files are authored mainly in Markdown under `docs/`.
  - MyST extends Markdown so Sphinx can use directives such as `{toctree}` and `{admonition}`.
  - The homepage is defined in `docs/index.md` and routes users to audience hubs.
  - `docs/conf.py` defines Sphinx behavior, enabled extensions, source suffixes, and theme.
  - `.readthedocs.yaml` defines how Read the Docs builds the site.
  - `docs/requirements-doc.txt` lists Python dependencies needed for documentation builds.
  - Source files, generated HTML, and published webpages are different stages in the docs lifecycle.
- Actions performed:
  - Inspected main documentation directories and audience/task hubs.
  - Inspected homepage routing in `docs/index.md`.
  - Inspected Sphinx config in `docs/conf.py`.
  - Inspected RTD config in `.readthedocs.yaml`.
  - Inspected doc build dependency list in `docs/requirements-doc.txt`.
  - Performed focused Contributor path verification.
- Files inspected:
  - `docs/index.md`
  - `docs/conf.py`
  - `.readthedocs.yaml`
  - `docs/requirements-doc.txt`
  - `docs/get-started/index.md`
  - `docs/practitioner/index.md`
  - `docs/researcher/index.md`
  - `docs/foundations/index.md`
  - `docs/tasks/index.md`
  - `docs/api/index.md`
  - `docs/migration/index.md`
  - `docs/upgrade/index.md`
  - `docs/plugins.md`
  - `docs/appendices/contributor/index.md`
- Verified observations:
  - Main docs sections and purpose:
    - `docs/get-started/`: onboarding, installation, quickstarts, troubleshooting.
    - `docs/practitioner/`: applied workflows, playbooks, and advanced practitioner material.
    - `docs/researcher/`: replication and research-oriented material.
    - `docs/foundations/`: shared concepts, how-to, references, and governance.
    - `docs/tasks/`: task-oriented pages for classification/regression/probabilistic regression.
    - `docs/api/`: API reference landing pages.
    - `docs/migration/` and `docs/upgrade/`: migration and version upgrade guidance.
    - `docs/appendices/`: supplemental references.
    - `docs/_autosummary/`: autosummary-generated source stubs used by Sphinx.
  - Homepage role (`docs/index.md`):
    - Provides audience-first routing and several `toctree` groups: Start here, Core references, Companion projects, and Migration/project docs.
  - Sphinx role (`docs/conf.py`):
    - Enables MyST Markdown via `myst_parser`.
    - Accepts `.md` and `.rst` as source via `source_suffix`.
    - Uses theme `furo` via `html_theme = "furo"`.
    - Uses extensions for autodoc/autosummary/numpydoc/notebooks/mermaid.
  - RTD role (`.readthedocs.yaml`):
    - Uses config version 2, Ubuntu 22.04, Python 3.11.
    - Builds with Sphinx using `docs/conf.py`.
    - Installs dependencies from `docs/requirements-doc.txt`.
  - Source vs generated HTML vs published webpages:
    - Source: files under `docs/` plus config files.
    - Generated HTML: output produced by Sphinx during a build process.
    - Published webpages: hosted output served by Read the Docs after a successful remote build.
  - Contributor navigation verification:
    - `docs/contributor/index.md`: does not exist.
    - `docs/appendices/contributor/index.md`: exists.
    - `docs/index.md` references `contributor/index` in both prose and `toctree`.
- Possible issue (verified mismatch):
  - Contributor links in `docs/index.md` currently point to `contributor/index`, but the existing contributor hub file is under `docs/appendices/contributor/index.md`.
  - Under current Sphinx configuration (`master_doc = "index"`, Markdown enabled, normal toctree/doc resolution), these `contributor/index` references are expected to fail unless a matching source file exists at `docs/contributor/index.md` or an equivalent redirect/alias mechanism is defined elsewhere.
  - No build was run in this lesson, so this is a path-resolution analysis from source and configuration inspection only.
- Findings relevant to future documentation evaluation:
  - Audience-first architecture is already present and clearly organized around beginner-to-advanced pathways.
  - Navigation integrity must be checked systematically (especially cross-section links) before redesign decisions.
  - Build configuration and dependency definitions are explicit and suitable for reproducible evaluation.
- Future improvement ideas (not implemented in this lesson):
  - Create a navigation integrity checklist for hub links and toctree targets.
  - Track each audience hub path and verify that every homepage reference has a matching source file.
  - Add a lesson-by-lesson map from learning goals to specific documentation pages.
- Open questions:
  - Was contributor content intentionally moved to `docs/appendices/contributor/`, or is this an incomplete migration?
  - Is there any hidden redirect mechanism outside inspected files that resolves `contributor/index`?
  - Which audience paths contain the highest concentration of broken or outdated links?
- Next step:
  - Continue with a structured, read-only navigation integrity review (hub links, toctree targets, and cross-references) before proposing any restructuring.

- Correction record (2026-11-06):
  - Follow-up restoration task verified parity and restored Contributor files to `docs/contributor/`, then removed duplicate `docs/appendices/contributor/`.
  - The mismatch documented above remains valid as a historical observation from the original Lesson 2 inspection snapshot.
  - Restoration evidence report: `learning-reports/L02-contributor-restoration.md`.

### Lesson 3 - Homepage Evaluation: Baseline Inspection
- Date: 2026-11-06
- Status: Baseline inspection completed (redesign not started)
- Completion report: learning-reports/L03-completion-report.md
- Objective:
  - Evaluate the current documentation homepage for first-time users before proposing improvements.
- Actions performed:
  - Conducted read-only inspection of `docs/index.md` and directly linked audience/foundations hubs.
  - Mapped six beginner questions to exact source evidence and line numbers.
  - Recorded verified findings, usability hypotheses, open questions, and up to three small non-implemented improvements.
- Evidence checked:
  - Detailed baseline analysis report: `learning-reports/L03-homepage-evaluation.md`.
- Outcome:
  - Baseline inspection is complete and documented.
  - No homepage redesign changes were implemented.
- Open questions:
  - Which beginner-friction points are confirmed by user testing versus inferred from source review?
- Next step:
  - Wait for review approval before proposing or implementing homepage changes.

### Lesson 3 Part 2 - Beginner Readability Walkthrough
- Date: 2026-11-08
- Status: Completed (read-only; awaiting review)
- Objective:
  - Evaluate beginner and practitioner navigation from the homepage to quickstarts,
    interpretation, calibration/uncertainty guidance, integration, and limitations.
- Actions performed:
  - Inspected relevant homepage, hub, quickstart, foundations, task, and capability
    pages without changing documentation source files.
  - Recorded expected and actual paths, line-cited evidence, likely friction, and
    confidence for both personas.
  - Prepared no more than three small homepage improvements that reuse existing
    pages.
- Evidence checked:
  - `learning-reports/L03-beginner-walkthrough.md`
  - `learning-reports/L03-improvement-proposal.md`
  - `learning-reports/L03-part2-completion-report.md`
- Outcome:
  - Both personas have viable routes, but the homepage under-explains CE's purpose,
    leaves the first quickstart choice open, and does not show one onward sequence.
  - No redesign or implementation was performed.
- Open questions:
  - Do first-time readers experience the identified orientation and choice friction?
- Next step:
  - Wait for ChatGPT review before implementing any approved homepage changes.

### Lesson 4 - CE Documentation Architecture Mapping & Gap Analysis
- Date: 2026-11-08
- Status: Completed (read-only; awaiting review)
- Objective:
  - Map current documentation and repository material against the proposed
    five-door hybrid architecture.
- Actions performed:
  - Inventoried the 107 Markdown documentation pages and summarized the major
    physical sections.
  - Mapped proposed Door 1-5 topics to existing pages, source/runtime material,
    coverage status, discoverability, and recommended action.
  - Analysed audience-based and task-based navigation, cross-links, content gaps,
    and structural risks.
  - Prepared a conceptual blueprint without moving or renaming files.
- Evidence checked:
  - `learning-reports/L04-current-documentation-inventory.md`
  - `learning-reports/L04-five-door-content-mapping.md`
  - `learning-reports/L04-gap-analysis.md`
  - `learning-reports/L04-proposed-navigation-blueprint.md`
  - `learning-reports/L04-completion-report.md`
- Outcome:
  - Existing coverage is strongest for practical use and software integration.
  - The main gaps are Door 1 discoverability, progressive theory/prerequisite
    framing, and cross-door navigation.
  - No CE documentation source files were modified and no build was run.
- Open questions:
  - Should the five doors become visible public navigation or remain a planning
    model?
  - Should general ML/statistics prerequisites be part of CE documentation?
- Next step:
  - Wait for ChatGPT review and user approval before implementing a navigation-only
    pilot.

### Lesson 4 Addendum - Interactive Resources, Ecosystem and Software Verification
- Date: 2026-11-08
- Status: Completed (read-only; awaiting review)
- Objective:
  - Verify interactive resources, Grejna AB references, software version context,
    installation guidance, and updated Door 3/4/5 mappings.
- Actions performed:
  - Inspected repository references to the browser demo, Decision Labs, Grejna AB,
    notebooks, installation methods and release metadata.
  - Distinguished verified repository descriptions from external functionality
    that was not tested.
  - Recorded that no browser upload or own-data workflow was verified.
- Evidence checked:
  - `learning-reports/L04-addendum-resource-verification.md`
- Outcome:
  - Browser demo, Decision Labs link, notebook learning path and local integration
    route are documented at different levels of discoverability.
  - Local version `1.1.0-dev`, release metadata `v1.0.2`, and homepage stable
    wording `1.0.0` require reconciliation.
  - No CE documentation, software, configuration or repository structure was
    modified; no build or installation was run.
- Open questions:
  - What functionality and ownership should be attributed to the external demo
    and Decision Labs?
  - Which release should public documentation identify as stable?
- Next step:
  - Wait for review before any navigation or documentation implementation.

### Lesson 5 Stage 1 - CE Homepage and Five-Door Navigation Design
- Date: 2026-11-08
- Status: Completed (design-only; awaiting review)
- Objective:
  - Prepare an evidence-based homepage wireframe, five-door navigation design,
    and link map without implementing documentation changes.
- Actions performed:
  - Converted L04 inventory, mapping, gap analysis and resource addendum into a
    homepage wireframe and logical five-door design.
  - Mapped proposed homepage links to existing pages or verified external URLs.
  - Marked unsupported browser upload, Decision Labs functionality, regulatory,
    ownership and stable-version claims as unresolved or prohibited.
- Evidence checked:
  - `learning-reports/L05-homepage-wireframe.md`
  - `learning-reports/L05-five-door-navigation-design.md`
  - `learning-reports/L05-link-and-evidence-map.md`
  - `learning-reports/L05-stage1-review-report.md`
- Outcome:
  - A navigation-first design is ready for review while preserving audience,
    task and physical documentation paths.
  - No documentation source, software, configuration or repository structure was
    modified; no build or installation was run.
- Open questions:
  - Should the five doors become visible homepage navigation?
  - Which current pages should serve as Door 1 and Door 5 landing destinations?
  - How should inconsistent version references be reconciled?
- Next step:
  - Wait for review and explicit approval before Stage 2 implementation.

### Lesson 5 Stage 2A - Final Homepage Navigation Mapping and Specification
- Date: 2026-11-08
- Status: Completed (design-only; awaiting review)
- Objective:
  - Convert the approved five-door concept into an exact homepage navigation
    map and implementation specification.
- Actions performed:
  - Updated the homepage wireframe to use the approved header, subtitle,
    introduction, five doors and guided learning paths.
  - Mapped all 27 sub-doors with exact labels, evidence, status, action and
    priority.
  - Separated internal software architecture from public API reference.
  - Prepared a minimal `docs/index.md` implementation plan with Sphinx/MyST,
    responsive-layout, validation and rollback guidance.
- Outcome:
  - 11 sub-doors have suitable existing destinations; 12 need improvement; 1
    needs a new landing-page decision; 1 is future educational content; and 2
    are external resources requiring verification.
  - No public documentation, software, configuration or repository structure
    was modified.
- Open questions:
  - Whether to implement the five doors directly in `docs/index.md`.
  - Whether Door 5 needs a new landing page.
  - Which version reference should be presented as current stable.
- Next step:
  - Wait for review and explicit approval before Stage 2B implementation.

### Lesson 5 Stage 2B - Homepage Navigation Implementation
- Date: 2026-11-08
- Status: Completed (implementation awaiting review)
- Objective:
  - Implement the approved five-door homepage navigation while preserving
    existing canonical routes.
- Actions performed:
  - Updated `docs/index.md` with the approved header, five main doors, all 27
    compact semantic sub-door navigation entries, guided learning paths and
    preserved toctrees.
  - Added a separate, prominent Internal Software Architecture destination
    linked to the verified architecture documentation.
  - Qualified external demo, Decision Labs, local own-data workflow, version,
    compliance and ecosystem wording.
- Validation:
  - Confirmed all 27 sub-door labels and all 31 referenced local targets.
  - Sphinx and Make were unavailable; no build or dependency installation was
    performed.
- Outcome:
  - Homepage implementation is complete and documented in
    `learning-reports/L05-stage2B-implementation-report.md`.
- Open questions:
  - Sphinx/MyST rendering, external resource availability and version wording
    remain unverified.
- Next step:
  - Wait for review before further documentation changes.

### Lesson 5 Stage 2C - Sphinx-Design Integration and Homepage Cards
- Date: 2026-11-09
- Status: Completed (implementation awaiting Product Owner review)
- Objective:
  - Replace the homepage's long navigation entries with responsive, clickable
    `sphinx-design` cards while preserving the five doors and 27 labels.
- Actions performed:
  - Pinned `sphinx-design==0.6.1` in `docs/requirements-doc.txt`, the file RTD
    installs.
  - Replaced inline-styled HTML in `docs/index.md` with five grids and 27 cards.
  - Kept Door 1.1 and Door 5.1 as labelled non-clickable placeholders and gave
    Door 3.3 a labelled interim link.
  - Added `sphinx-design` to `.venv-docs`, and built separately in a temporary
    environment using the project's pinned versions.
- Validation:
  - Pinned strict build: succeeded with 0 warnings (Python 3.10; RTD uses 3.11).
  - `.venv-docs` build: `_build/html/index.html` created; 20 autodoc warnings
    from missing `numpy`.
  - Generated HTML contains 5 grids and 27 cards in approved order; all 23
    internal card targets exist; homepage external URLs returned HTTP 200.
  - Headless Edge screenshots checked at 1400px and 500px in the light theme.
  - Actual RTD deployment, Python 3.11, dark theme and the full CI docs job
    were not verified.
- Outcome:
  - Details are in `learning-reports/L05-stage2C-implementation-report.md`.
- Lesson learned:
  - A successful local build only says something about the published site if
    its package versions match the versions the publishing service installs.
- Open questions:
  - Door 3.3 interim link, seven links no longer on the homepage, malformed
    Grejna URL under MyST 3.0.1, conflicting version claims, and a duplicate
    Roadmap sidebar entry.
- Next step:
  - Wait for Product Owner visual review before publication to Read the Docs.

### Lesson 5 Stage 2D - Unified Navigation Audit and Proposal (Phases A and B)
- Date: 2026-11-09
- Status: Audit and proposal completed; Phase C not started and awaiting approval
- Objective:
  - Audit the current sidebar and propose a navigation hierarchy matching the
    approved five homepage sections.
- Actions performed:
  - Audited the toctree graph and rendered sidebar from the last pinned build.
  - Wrote the navigation audit, proposed navigation and mapping table.
  - Simulated the proposed toctree graph in memory.
- Validation:
  - Simulation: 119 of 120 pages reachable as today, the one exception being an
    existing intentional orphan; multi-parent pages fell from 16 to 0.
  - A trial build was not run because the temporary copy was denied.
  - No documentation, navigation or configuration file was changed.
- Outcome:
  - Reports are `learning-reports/L05-stage2D-navigation-audit.md`,
    `L05-stage2D-proposed-navigation.md` and `L05-stage2D-mapping-table.md`.
- Lesson learned:
  - A sidebar duplicate may come from page headings rather than toctrees, so
    check the rendered link target before choosing a fix.
- Open questions:
  - Active standard STD-004 requires audience-first navigation, which conflicts
    with the approved section order. Five design decisions are listed in the
    proposal.
- Next step:
  - Wait for Product Owner decisions before Phase C.

### Lesson 5 Stage 2D - Phase C Navigation Implementation
- Date: 2026-11-09
- Status: Completed (implementation awaiting Product Owner review)
- Objective:
  - Implement the approved five-section homepage and sidebar with one parent per
    page, including the revised CE Software & Integration grouping.
- Actions performed:
  - Replaced the homepage toctrees, removed "Door" headings and fixed the Roadmap
    and BibTeX duplicate headings.
  - Removed duplicate toctree parents and kept hub access through `{doc}` links.
  - Added three minimal grouping pages and their tier-map rows.
  - Amended STD-004 and `nav_crosswalk.md`, recorded as pending formal
    standard-owner approval.
- Validation:
  - Pinned strict build: 0 warnings (Python 3.10; RTD uses 3.11).
  - `tests/docs/test_navigation.py`: 6 passed, using pytest 8.4.2 in a temporary
    environment because pytest 9.2.0 crashed.
  - Duplicate parents fell from 16 to 0; 27 cards and all previous page paths are
    unchanged; no new orphans.
  - Actual RTD deployment was not verified.
- Outcome:
  - Details are in `learning-reports/L05-stage2D-implementation-report.md`.
- Lesson learned:
  - Tests can depend on literal homepage text, so check them before moving
    navigation entries.
- Open questions:
  - Standard-owner approval of the STD-004 amendment; a future destination for
    Software Overview & Versions.
- Next step:
  - Wait for Product Owner review before publication to Read the Docs.

### Lesson 5 Stage 2D - Local Closeout
- Date: 2026-11-09
- Status: Conditionally accepted by the Product Owner; publication not approved
- Publication conditions:
  - Formal approval of the STD-004 amendment: open.
  - RTD build and mobile/dark-theme navigation: verified locally for mobile and
    dark theme; RTD build not run.
  - Malformed external link and heading anchors: closed locally.
  - Repository CI checks: open.
- Actions performed:
  - Fixed the double-escaped Grejna link with `{eval-rst}`, because every
    Markdown link form double-escapes `&` under pinned MyST 3.0.1.
  - Checked Roadmap, citation and homepage anchors and preserved
    `#companion-projects` with a target.
  - Tested the mobile drawer and dark theme with Furo's real controls on a
    scratch copy of the built site.
- Validation:
  - Pinned strict build: 0 warnings (Python 3.10).
  - `tests/docs/test_navigation.py`: 6 passed.
  - 27 cards and all previous page paths unchanged; no duplicate parents.
  - RTD, Python 3.11, CI and physical-device behaviour were not verified.
- Outcome:
  - Results are in the Closeout section of
    `learning-reports/L05-stage2D-implementation-report.md`.
- Lesson learned:
  - When the same defect appears for every source syntax, suspect the parser and
    test a small example before changing the page.
- Open questions:
  - Standard-owner approval; when to push a branch for RTD and CI verification.
- Next step:
  - L06 - Documentation Content, Learning Paths & Cross-Linking.

## 6. Decisions and rationale

Record important choices and why they were made.

| Decision ID | Decision | Rationale | Status | Verification |
|---|---|---|---|---|
| D-001 | Keep redesign in an independent local copy | Protect original project and published docs from accidental changes | Active | Rule documented in this journal |
| D-002 | Use a lesson-based learning journal | Supports beginner learning and future student manual development | Active | Template included and ready to reuse |

## 7. Problems and resolutions

Use this table to track blockers and how they were resolved.

| Problem ID | Problem summary | Status | Resolution | Notes |
|---|---|---|---|---|
| P-001 | No problems recorded yet | Open | Pending | Update when first issue appears |

## 8. Glossary of technical terms

| Term | Beginner-friendly meaning |
|---|---|
| Git | A version control system that tracks file changes over time. |
| GitHub | A web platform for hosting Git repositories and collaborating on changes. |
| Repository | A project folder tracked by Git, including files and history. |
| Clone | A local copy of a repository. |
| Remote | A linked repository location, usually on a server like GitHub. |
| Markdown | A lightweight plain-text format for structured documents. |
| MyST | A Markdown flavor used by Sphinx that supports directives and roles, such as `{toctree}` and `{doc}`. |
| toctree | A Sphinx directive that defines the document tree and navigation structure. |
| Sphinx | A documentation generator that builds publishable pages from source files. |
| Furo | The Sphinx HTML theme used by this documentation site. |
| Read the Docs | A service that automatically builds and hosts Sphinx documentation. |
| Configuration file | A file that controls tool behavior, such as build settings. |

## 9. Open questions and next steps

### Open questions
- Which documentation areas are hardest for beginners in the current CE docs?
- What navigation changes would make the learning path clearer?
- Which topics should be prioritized for the first student manual draft?

### Next steps
1. Start Lesson 2 inspection and capture concrete findings.
2. Map the current documentation structure into a beginner learning sequence.
3. Record the first redesign candidate areas with reasons.

## 10. Student manual development notes

This section converts lesson outputs into reusable material for the future manual.

### Candidate manual structure (initial draft)
1. Orientation: What this project is and why documentation matters.
2. Toolchain basics: GitHub, Sphinx, Read the Docs.
3. Workspace navigation in VS Code.
4. Reading and editing documentation source files.
5. Planning and validating documentation changes.
6. Publishing workflow concepts and quality checks.

### Content capture checklist
- Concept explained in beginner language.
- Real example from project work.
- Common mistake and how to avoid it.
- Verification step.
- Short reflection for learning transfer.

### Note for future updates
When a lesson is completed, update:
- Section 5 with the lesson entry.
- Section 6 for key decisions.
- Section 7 if any problem occurred.
- Section 8 for new terms.
- Section 10 with reusable manual material.
