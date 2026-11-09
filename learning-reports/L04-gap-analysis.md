# L04 - Gap Analysis and Recommendations

Date: 2026-11-08  
Status: Read-only analysis completed; recommendations are not implemented

## Objective and method

This analysis identifies navigation, content, potential-new-content and
structural gaps between the current documentation and the prop# L04 - Five-Door Content Mapping

Date: 2026-11-08  
Status: Read-only mapping completed; no structural changes implemented

## Objective and method

The current documentation was compared with every topic in the proposed five
doors. A topic is marked **Explained**, **Partially explained**, **Mentioned or
linked only**, **Not found**, or **Not yet verified**. Coverage and
discoverability are assessed separately.

The mapping treats `development/` as maintainer/project material, not as public
user documentation. The superseded ADR-022 is historical evidence only:
`development/adrs/superseded ADR-022-documentation-information-architecture.md:5`
explicitly says not to use it for new documentation.

## Door 1 - CE: What & Why

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| CE overview and motivation | `README.md:28-32` explains the miscalibrated-XAI problem and CE's calibration-first approach | Explained | Low from `docs/index.md`; README is external to docs navigation | Add a short homepage overview reusing README concepts |
| AI/ML in decision-making | No focused public CE page found in inspected inventory | Not found | None | Potential new contextual content only after audience need is confirmed |
| Trustworthy/responsible AI | `docs/index.md:28-31` establishes open-source context; practical limitations appear in `docs/foundations/concepts/calibrated_interval_semantics.md:51-60` | Partially explained | Medium | Link the limitations as responsible-use guidance; do not broaden into unsupported claims |
| European trustworthy AI/EU AI Act | `docs/practitioner/playbooks/eu-ai-act-compliance.md:1` exists | Mentioned or linked only | Medium for practitioners, low for beginners | Keep contextual and clearly distinguish documentation support from regulatory compliance |
| Limits of conventional explainability | README contrasts LIME/SHAP with miscalibrated outputs (`README.md:28-32`); `docs/compare.md` exists | Partially explained | Low in docs homepage | Link comparison/README-derived context from Door 1 |
| CE contribution | `README.md:30-32`; capability and semantics pages | Explained | Medium | Reuse concise wording in homepage and capabilities |
| Benefits, boundaries, non-guarantees | `docs/foundations/concepts/calibrated_interval_semantics.md:5-60` | Explained | Medium | Retitle/link as “guarantees, assumptions and limits” where appropriate |

## Door 2 - How CE Works

### A. Prerequisite foundations

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| AI/ML fundamentals | No dedicated prerequisite page found | Not found | None | Potential new content; do not assume CE docs must teach general ML |
| Supervised learning | No dedicated page found | Not found | None | Potential new content if student manual scope is approved |
| Classification and regression | `docs/tasks/classification.md:1-99`; `docs/tasks/regression.md`; `docs/tasks/probabilistic_regression.md` | Explained | High from task hub, medium from homepage | Preserve task hub and cross-link from theory |
| Data splitting/model evaluation | Quickstarts show proper/calibration/test splits (`docs/get-started/quickstart_classification.md:20-35`) | Partially explained | High after quickstart, low as prerequisite | Add a conceptual pointer rather than duplicate tutorial text |
| Predictions, probabilities, uncertainty | Quick API and interpretation guide (`docs/get-started/quick_api.md:1-70`; `docs/foundations/how-to/interpret_explanations.md:1-16`) | Explained | Medium | Create guided links from Door 2 and Door 3 |
| Explainable AI concepts | Interpretation, alternatives and explanation structures pages | Partially explained | Medium | Use existing interpretation page as conceptual entry |
| Basic probability/statistics | Statistical assumptions are described, but no general primer found | Partially explained | Low | Potential new content, subject to scope |

### B. CE-specific foundations

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| Calibration and calibrated explanations | Quickstarts, semantics and README | Explained | Medium | Add a direct “how calibration works” label/link |
| Factual and alternative explanations | `docs/foundations/how-to/interpret_explanations.md:8-16`; `docs/foundations/concepts/alternatives.md` | Explained | High after quickstart, medium from concepts | Preserve and cross-link |
| Venn-Abers predictors | Quickstart semantics and README method summary; API/source references | Partially explained | Medium | Add a concise theory pointer if mathematical depth is needed |
| Isotonic regression | No dedicated page found in inspected docs | Not found | None | Potential new content; verify desired depth before adding |
| Conformal prediction/CPS | Regression quickstart and semantics (`quickstart_regression.md:1-18`; semantics page) | Explained | Medium | Use regression as the practical entry and add theory cross-link |
| Classification, interval and probabilistic regression | Semantics page explicitly separates all three modes (`calibrated_interval_semantics.md:5-18`) | Explained | High | Preserve mode-specific structure |
| Aleatoric and epistemic uncertainty | No dedicated CE page found | Not found | None | Potential new content; avoid implying unsupported decomposition |
| Exchangeability and assumptions | Semantics page states exchangeability/distribution-match assumptions | Explained | Medium | Label as assumptions/limits in navigation |
| Interval interpretation/guarantees/non-guarantees | Semantics page | Explained | Medium | Promote as a named limits page/link |
| Conceptual CE workflow | Architecture page public lifecycle and practitioner core path | Explained | Medium | Cross-link architecture lifecycle from Door 2 and Door 3 |

## Door 3 - CE in Practice

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| Audiences/application areas | Homepage audience bullets and practitioner/researcher hubs | Explained | High | Preserve audience routing |
| Use cases/decision contexts | Practitioner decision policies and README illustrative examples | Partially explained | Medium | Link decision-policy playbook; avoid unsupported domain claims |
| Browser demo | Homepage and README demo admonitions | Explained | High | Preserve demo/docs distinction |
| Installation/quickstarts | Get started pages | Explained | High | Preserve and label a recommended first quickstart |
| Classification/regression examples | Three quickstarts and task pages | Explained | High | Preserve task-first navigation |
| Factual/alternative explanations in practice | Interpretation guide and quickstarts | Explained | High after quickstart | Add an explicit continuation route |
| Task-oriented how-to guides | `docs/tasks/` and foundations how-to | Explained | Medium | Cross-link task pages to integration and interpretation |
| Practical evaluation/comparisons | `docs/compare.md`, practitioner playbooks, researcher theory | Partially explained | Low-medium | Add a discoverable comparison/evaluation link |
| Troubleshooting/next steps | `docs/get-started/troubleshooting.md`, quickstart next links | Explained | Medium | Add to a practical journey rather than homepage clutter |

## Door 4 - CE Software & Integration

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| Stable release/capabilities | Homepage 1.0.0 notice (`docs/index.md:13-23`), changelog, active 1.1.0 plan | Explained | Medium; release context is split | Keep public release notice and link project release material |
| High-level architecture | `docs/foundations/concepts/architecture.md:1-80+` | Explained | Medium | Link architecture from API and practitioner routes |
| Internal modules/components/data flow | Architecture page plus `src/calibrated_explanations/core`, `plugins`, `calibration`, `explanations`, `viz` | Partially explained | Low for public users | Keep details in technical/contributor pages; avoid exposing unstable internals as API |
| Public API/technical reference | `docs/api/`, Quick API, public lazy exports | Explained | High from API and Get started, medium from homepage | Add one direct API choice link for practitioners |
| Model adapters/supported interfaces | README scikit-learn compatibility; pipeline integration page | Partially explained | Medium | Link pipeline guide from practitioner/task paths |
| External ML pipeline/application integration | `docs/foundations/how-to/integrate_with_pipelines.md:1-67` | Explained | Low-medium | Promote integration link |
| Extension/customization | Plugin docs, contributor contract, practitioner plugin guides | Explained | Medium | Preserve separate user/contributor plugin routes |
| Dependencies/compatibility/constraints | Installation, README, migration and upgrade pages | Explained | Medium | Cross-link from Door 4 entry point |

## Door 5 - CE Project, Vision & Evolution

| Proposed topic | Existing evidence | Coverage | Discoverability | Recommended action |
|---|---|---|---|---|
| Project vision/mission | README summary and project description | Partially explained | Medium in README, low in docs | Reuse only if a public overview is approved |
| Origins/research history | README publications/funding sections; researcher theory page | Partially explained | Medium | Link researcher hub and citing rather than duplicate history |
| Publications/milestones | `docs/citing.md`, `docs/researcher/advanced/theory_and_literature.md` | Explained | Medium | Preserve researcher route |
| Development journey | Changelog, migration, finished plans | Explained | Low for general users | Link release history from project door |
| ADRs | `development/adrs/` and contributor references | Explained for maintainers | Low and intentionally not user-facing | Keep ADRs maintainer-facing; link selected decisions only |
| Version control/development workflow | `CONTRIBUTING.md`, `development/README.md` | Explained | Medium for contributors | Preserve contributor path |
| Releases/changelog/migration | `CHANGELOG.md`, `docs/migration`, `docs/upgrade`, `release.md` | Explained | Medium | Add one project evolution landing link |
| Contribution/governance | Contributor hub and foundations governance | Explained | High for contributors | Preserve audience route |
| Research directions/open questions | `docs/researcher/future_work.md:1-68` | Explained | High within researcher hub | Preserve distinction from committed work |
| Development roadmap/future opportunities | `ROADMAP.md`, `docs/ROADMAP.md` | Explained | Medium | Label official plan versus exploratory research |

## Overall interpretation

Coverage is strongest for Doors 3 and 4, followed by the CE-specific portion
of Door 2 and the project/evolution portion of Door 5. Door 1 is represented
in README and limitations pages but is not a first-class public documentation
entry point. The prerequisite layer of Door 2 is the largest genuine content
gap, although it may be outside the library's appropriate scope.

## Open questions and recommended next step

Before creating new pages, decide whether the project wants to teach general
AI/ML foundations or only provide CE prerequisites. Then test a navigation-only
blueprint that exposes the existing motivation, capability, theory, API and
project-history pages without moving files.

osed five-door
architecture. Recommendations are prioritized and intentionally prefer
cross-links or labels over relocation.

Findings are based on source inspection. No build was run, so link resolution
and rendered navigation remain unverified.

## Key findings

1. **The current system is a hybrid already, but its labels are not five-door
   labels.** The homepage combines audience routing with task/core-reference
   toctrees (`docs/index.md:47-104`).
2. **Door 3 is the strongest existing door.** Get started, task pages,
   quickstarts and practitioner playbooks provide practical routes.
3. **Door 4 is substantially covered.** API, architecture, plugin, pipeline,
   serialization and visualization pages exist, with public wrapper methods
   represented in source (`src/calibrated_explanations/core/wrap_explainer.py:
   147-181, 380-419, 643-699, 768-821`).
4. **Door 1 is the main discoverability gap.** The README has a clear
   motivation statement (`README.md:28-32`), but `docs/index.md` begins with
   routing and release/policy notices rather than a “what and why” explanation.
5. **Door 2 is uneven.** CE-specific semantics are explicit, while general ML,
   probability and statistics prerequisites are not a dedicated curriculum.
6. **Door 5 is split by authority.** Public project material is in docs,
   while release plans, ADRs and standards are intentionally in `development/`
   (`development/README.md:1-58`).

## A. Navigation improvements

### N1 - Add five-door labels without replacing audience/task routes

**Priority:** High  
**Evidence:** Homepage currently has audience bullets and four toctree groups
(`docs/index.md:47-104`); the five-door topics are distributed across them.  
**Action:** Add a compact conceptual “Explore by question” block linking each
door to existing hubs. Keep audience bullets and task navigation unchanged.  
**Benefit:** Makes the proposed logical architecture visible without moving
files.  
**Scope:** `docs/index.md` only, subject to approval.  
**Risk:** More homepage choices; mitigate with short labels and a recommended
beginner route.

### N2 - Add a guided cross-door journey

**Priority:** High  
**Evidence:** Practitioner already has an ordered path
quickstart -> interpretation -> API style -> playbooks
(`docs/practitioner/index.md:5-9`), while Get started presents several
parallel links (`docs/get-started/index.md:9-20`).  
**Action:** Add a small sequence linking Door 1 overview -> Door 3 quickstart
-> Door 2 interpretation/semantics -> Door 4 integration/API.  
**Benefit:** Reduces the need for users to infer relationships between hubs.  
**Risk:** A universal path may not suit researchers or contributors; present it
as optional and retain audience paths.

### N3 - Promote existing integration and capability maps

**Priority:** Medium  
**Evidence:** Capabilities map exists at `docs/tasks/capabilities.md:9-25`,
and pipeline integration exists at
`docs/foundations/how-to/integrate_with_pipelines.md:1-67`, but neither is
prominent in the homepage/practitioner entry path.  
**Action:** Add links labelled “Supported tasks” and “Integrate an existing
pipeline” to practitioner/task navigation.  
**Benefit:** Helps practitioners decide relevance faster.  
**Risk:** Link proliferation; use one compact practitioner callout.

### N4 - Make “semantics” discoverable as limits and assumptions

**Priority:** Medium  
**Evidence:** The semantics page contains assumptions, guarantees and
non-guarantees (`docs/foundations/concepts/calibrated_interval_semantics.md:
5-60`), but “semantics” may be opaque to new readers.  
**Action:** Use a navigation label such as “Guarantees, assumptions and limits
 (mode-specific semantics)” while preserving the canonical page title.  
**Benefit:** Improves responsible-use discoverability.  
**Risk:** Wording could overpromise guarantees if shortened incorrectly; retain
the mode-specific qualifier.

## B. Content improvements

### C1 - Add a concise Door 1 overview

**Priority:** High  
**Evidence:** README explains the motivation and calibration-first contribution
(`README.md:28-32`), while the docs homepage does not.  
**Action:** Add or adapt a short, technically bounded explanation of
miscalibrated predictions, uncertainty intervals and alternative explanations.
Reuse existing semantics caveats.  
**Benefit:** Gives beginners and practitioners a correct mental model before
navigation.  
**Risk:** Duplicate wording between README and docs; select one canonical
overview and link rather than copying long passages.

### C2 - Clarify the prerequisite boundary

**Priority:** Medium  
**Evidence:** Quickstarts assume Python/scikit-learn and model-training
knowledge (`docs/get-started/quickstart_classification.md:5-8`), but no
explicit prerequisite map covers supervised learning, evaluation or basic
probability.  
**Action:** Add a short prerequisite list or links to authoritative external
learning resources only if the project wants to teach that context.  
**Benefit:** Prevents students from misreading CE-specific pages as a general
ML course.  
**Risk:** Scope creep and external-link maintenance.

### C3 - Add a theory bridge before mathematical detail

**Priority:** Medium  
**Evidence:** Concepts index links directly to technical concepts and
semantics (`docs/foundations/concepts/index.md:1-32`), while the researcher
hub links formal semantics and theory (`docs/researcher/index.md:5-10`).  
**Action:** Add a short conceptual bridge explaining calibration, conformal
prediction and Venn-Abers before the formal semantics page.  
**Benefit:** Supports progressive learning.  
**Risk:** Could duplicate quickstart semantics; keep it conceptual and link
to canonical details.

## C. Potential new content

### P1 - Prerequisite foundations mini-index

**Priority:** Low pending scope decision  
**Evidence:** No dedicated pages for supervised learning, basic probability,
statistics, aleatoric/epistemic uncertainty or isotonic regression were found
in the inspected `docs/` inventory.  
**Recommendation:** Consider a small curated prerequisite index only if the
student-manual objective requires it. Otherwise link outward and keep CE docs
focused.  
**Risk:** Turning a focused library manual into a general ML textbook.

### P2 - CE overview page

**Priority:** Medium  
**Evidence:** Door 1 content exists in README but lacks a documentation page
with incoming links.  
**Recommendation:** A new overview page could become the canonical Door 1
landing page, but a homepage block is a lower-risk first experiment.  
**Risk:** New-page maintenance and duplicate project descriptions.

### P3 - Theory bridge page

**Priority:** Low-medium  
**Evidence:** CE-specific theory is distributed between concepts, quickstarts,
and researcher pages.  
**Recommendation:** Defer until navigation-only changes show that existing
pages cannot support progressive learning.  
**Risk:** Additional terminology and competing explanations.

## D. Structural changes

### S1 - Do not move or rename pages in the first iteration

**Priority:** High  
**Evidence:** Existing paths are linked across homepage, audience hubs,
quickstarts, task pages and foundations. `docs/conf.py:67-86` also defines
source and exclusion behavior.  
**Recommendation:** Keep physical folders and implement logical doors through
labels, cross-links and landing-page sections.  
**Benefit:** Minimizes broken-link and migration risk.  
**Risk:** The logical architecture remains partly virtual until navigation is
tested.

### S2 - Keep maintainer authority separate from public docs

**Priority:** High  
**Evidence:** `development/README.md:1-58` explicitly separates user-facing
`docs/` from ADRs, standards, capability claims and evidence.  
**Recommendation:** Link selected project-history or contribution material,
but do not copy active plans or ADR catalogs into public user journeys.  
**Benefit:** Preserves authority boundaries and prevents exploratory plans from
appearing as product commitments.

### S3 - Defer consolidation of audience hubs

**Priority:** Medium  
**Evidence:** Practitioner, researcher and contributor hubs each have explicit
core paths (`docs/practitioner/index.md:5-15`; `docs/researcher/index.md:5-18`;
`docs/contributor/index.md:9-35`).  
**Recommendation:** Preserve these routes and cross-link them to doors rather
than merging them.  
**Benefit:** Maintains audience-specific journeys already documented.

## Prioritized implementation sequence after approval

1. Test/approve a homepage Door 1 summary and five-door link block.
2. Add practitioner links to capabilities and pipeline integration.
3. Add a guided quickstart -> interpretation/limits -> API/integration route.
4. Reassess whether prerequisite or theory pages are still needed.

## Open questions and recommended next step

- Is the five-door architecture intended as a visible public navigation model
  or as an analysis framework only?
- Should Door 1 reuse README wording or become a new canonical page?
- Which external prerequisite resources, if any, are acceptable?
- Which `development/` references should be exposed to contributors?

Recommended next step: review this report and the proposed blueprint, then
approve a navigation-only pilot before any new page or folder is created.

