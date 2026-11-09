# L03 Homepage Evaluation - Baseline Inspection

Date: 2026-11-06
Task: L03 - Homepage Evaluation: Baseline Inspection
Status: Baseline inspection completed (no redesign implemented)

## Objective
Evaluate the existing Calibrated Explanations documentation homepage for first-time users before proposing improvements.

## Scope and evidence base
Read-only inspection of:
- docs/index.md
- docs/get-started/index.md
- docs/practitioner/index.md
- docs/researcher/index.md
- docs/contributor/index.md
- docs/foundations/index.md

No build/test/package installation/staging/commit was performed.

## 1) Homepage structure in actual reading order (verified)
Based on docs/index.md in top-to-bottom reading order:
1. Title and orientation sentence: docs/index.md:1-3
2. Official project/source links (GitHub, PyPI, issues, release notes): docs/index.md:5-11
3. Stable release admonition with upgrade/schema references: docs/index.md:13-23
4. Open source vs commercial/demo clarification: docs/index.md:25-34
5. Browser demo admonition: docs/index.md:36-45
6. Audience routing bullets (new users, practitioners, researchers, contributors): docs/index.md:47-50
7. Semantics caveat and foundations semantics link: docs/index.md:52-55
8. Companion-project framing and links: docs/index.md:57-61
9. Toctree "Start here": docs/index.md:63-71
10. Toctree "Core references": docs/index.md:73-80
11. Toctree "Companion projects": docs/index.md:82-88
12. Toctree "Migration and project docs": docs/index.md:90-104
13. Tier label: docs/index.md:106

## 2) Beginner-question audit

### Q1. What is CE, and why is it needed?
- Existing content/link:
  - "Calibrated Explanations is an independent, BSD-licensed open-source project." (docs/index.md:28)
  - "Use this site by audience and by task." (docs/index.md:3)
- Source and lines:
  - docs/index.md:3
  - docs/index.md:28-31
- What is clear:
  - Project identity (open-source) and where official artifacts live are clear.
- What may be difficult for a beginner:
  - A plain-language "why CE" problem statement is not explicit on the homepage.
- Answer type:
  - Partly direct; "why needed" is not directly explained.

### Q2. What prerequisite knowledge is required?
- Existing content/link:
  - No explicit prerequisites section on homepage.
  - Quickstarts are linked through get-started hub.
- Source and lines:
  - docs/index.md:47, 67
  - docs/get-started/index.md:3-11
- What is clear:
  - Beginners are routed to Get started.
- What may be difficult for a beginner:
  - Expected background (Python, ML basics, calibration basics) is not explicitly stated here.
- Answer type:
  - Linked/implicit; explicit prerequisite list not found.

### Q3. How does a beginner get started?
- Existing content/link:
  - "New users start in get-started/index." (docs/index.md:47)
  - Get-started page provides quickstarts and routing links.
- Source and lines:
  - docs/index.md:47, 67
  - docs/get-started/index.md:1-3, 9-15, 20-30
- What is clear:
  - Strong starting pointer and concrete first actions (pick a quickstart).
- What may be difficult for a beginner:
  - Several route choices appear quickly, which may increase choice overload.
- Answer type:
  - Direct + linked.

### Q4. Where are calibration, uncertainty, and statistical foundations explained?
- Existing content/link:
  - Homepage semantics pointer to calibrated interval semantics.
  - Shared foundations section toctree.
- Source and lines:
  - docs/index.md:52-55, 77
  - docs/foundations/index.md:1-4, 9-12
- What is clear:
  - There is a specific foundations area and an explicit semantics anchor.
- What may be difficult for a beginner:
  - "Semantics" phrasing may be abstract before introductory examples.
- Answer type:
  - Linked.

### Q5. How are different audiences guided?
- Existing content/link:
  - Four audience bullets on homepage.
  - Dedicated hub pages for each audience.
- Source and lines:
  - docs/index.md:47-50, 63-71
  - docs/practitioner/index.md:1-4
  - docs/researcher/index.md:1-4
  - docs/contributor/index.md:1-4
- What is clear:
  - Audience segmentation is explicit and consistent in both bullets and toctree.
- What may be difficult for a beginner:
  - The difference between practitioner and researcher paths may not be obvious without opening both hubs.
- Answer type:
  - Direct.

### Q6. How can someone contribute?
- Existing content/link:
  - Homepage links to contributor hub.
  - Contributor hub gives a core path (plugin contract, guides, governance checks).
- Source and lines:
  - docs/index.md:50, 70
  - docs/contributor/index.md:1-3, 9-16, 23-36
- What is clear:
  - There is a dedicated contributor route with concrete steps.
- What may be difficult for a beginner:
  - Contributor hub starts with governance/contracts and may feel advanced for first-time contributors.
- Answer type:
  - Direct + linked.

## 3) Evaluation summary

### First impression
- Verified findings:
  - Homepage is structured, policy-aware, and clearly routes by audience and task (docs/index.md:3, 47-50, 63-104).
- Usability hypotheses requiring user testing:
  - The multiple admonitions and policy-heavy framing may feel dense before beginner motivation is established.

### Terminology and readability
- Verified findings:
  - Terms such as "semantics", "non-guarantees", "plugin trust model", and "extension contract" appear early (docs/index.md:16-17, 52-55).
- Usability hypotheses requiring user testing:
  - Some first-time users may need simpler wording or a glossary link near first mention.

### Navigation and discoverability
- Verified findings:
  - Navigation is explicit via bullets and multiple toctree groups (docs/index.md:47-50, 63-104).
  - Get-started hub provides concrete onward routes (docs/get-started/index.md:9-30).
- Usability hypotheses requiring user testing:
  - New users may not immediately know whether to follow audience route or task route first.

### Beginner learning sequence
- Verified findings:
  - A practical sequence exists: homepage -> get-started -> quickstart -> interpretation/semantics (docs/index.md:47; docs/get-started/index.md:3, 15, 17-18).
- Usability hypotheses requiring user testing:
  - The sequence may benefit from one explicitly numbered beginner path on homepage.

### Audience-specific guidance
- Verified findings:
  - Practitioner, researcher, and contributor hubs each provide focused core-path statements (docs/practitioner/index.md:3-11; docs/researcher/index.md:3-10; docs/contributor/index.md:9-16).
- Usability hypotheses requiring user testing:
  - First-time users may need a short "Who should use this path?" sentence per audience on homepage.

## 4) Small improvement recommendations (not implemented)
1. Add a one-paragraph beginner orientation block near docs/index.md:3-4 that explains CE in plain language and why a new user might need it.
2. Add a compact "Prerequisites" pointer on homepage (for example, Python/ML basics) that links to a beginner prep page.
3. Add a single numbered "First 3 steps for new users" mini-sequence on homepage that points to get-started quickstart, interpretation guide, and semantics page.

## Open questions
- Should homepage prioritize audience routing first, or a universal beginner route first?
- Are governance and contract terms too early for novice readers in the contributor path?
- Which wording best explains "calibrated interval semantics" without losing technical correctness?

## Recommended next step
Run a focused readability walkthrough with beginner personas (read-only) to validate whether the inferred usability issues are experienced in practice before proposing structural edits.