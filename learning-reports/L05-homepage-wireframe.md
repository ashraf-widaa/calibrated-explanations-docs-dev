# L05 Stage 2A - Final Homepage Navigation Wireframe

Date: 2026-11-08  
Status: Design and implementation specification only; no public documentation changed

## Objective

Define the final homepage structure approved for Stage 2A. The homepage is a
router, not a replacement for the existing audience, task, concept, API or
project pages. The five doors are logical navigation layers; existing physical
paths remain canonical.

## Header

**Title:** `Calibrated Explanations`

**Subtitle:** `Explain machine-learning predictions with calibrated uncertainty.`

**Introduction:**

> An open-source Python library combining calibrated predictive information
> with factual and alternative explanations, helping users interpret model
> predictions and their uncertainty.

The header includes a link to the
[GitHub repository](https://github.com/Moffran/calibrated_explanations).

The homepage must not include separate top-level buttons for Try CE, Get
Started or Explore Theory. Those activities belong within the five-door
navigation.

## Homepage structure

```text
Header
  Title, subtitle, short introduction, GitHub link

Five primary doors
  Door 1 - CE: What & Why
  Door 2 - How CE Works: The Theory Behind It
  Door 3 - CE in Practice: Explore & Apply
  Door 4 - CE Software & Integration
  Door 5 - CE Project, Vision & Evolution

Guided learning paths
  New to CE | Practitioner | Researcher | Developer / Contributor

Existing release, demo, ecosystem and audience notices
```

There is no separate “Why CE” homepage section. Door 1 owns that progression.

## Door card pattern

Each door contains:

1. A prominent bold title linked to its overview destination when one exists.
2. One concise description.
3. A compact grid of task-oriented square or rectangular links.
4. Status-appropriate wording: existing destination, proposed landing page,
   future content, or external resource requiring verification.

The grid must be responsive: one column on narrow screens, two or more columns
on wider screens, with link text allowed to wrap and no dependence on fixed
square dimensions.

## Door cards

### Door 1 - CE: What & Why

**Description:** Understand how AI models work, why trusting their outputs is
challenging and what Calibrated Explanations contributes.

Progression: **AI models -> Trust -> Trustworthy AI -> Explainability gap -> CE.**

| Link label | Intended destination |
|---|---|
| Understanding AI Models | Future educational landing/content; task pages are supporting evidence |
| Can We Trust AI Outputs? | Existing semantics and calibration material, with a beginner bridge |
| Trustworthy AI | Existing contextual EU AI Act and decision-policy material |
| The Explainability Gap | Existing comparison and README motivation material |
| What Is CE & What Does It Add? | Existing README, capabilities and semantics evidence |

### Door 2 - How CE Works: The Theory Behind It

**Description:** Explore the scientific foundations, statistical mechanisms and
assumptions behind calibrated explanations.

| Link label | Intended destination |
|---|---|
| Essential Foundations | Existing foundations and quickstarts, needing a guided prerequisite label |
| Calibration & Uncertainty | Existing calibration and semantics material |
| Statistical Methods Behind CE | Existing Venn-Abers/conformal references; isotonic coverage is incomplete |
| How CE Explanations Work | Existing interpretation and alternatives guides |
| Assumptions & Guarantees | Existing canonical interval semantics page |

Door 1 introduces reliability and uncertainty. Door 2 explains mechanisms,
formal semantics, assumptions and guarantees without repeating the motivation.

### Door 3 - CE in Practice: Explore & Apply

**Description:** Discover applications, experience CE interactively, experiment
with predictive models and evaluate the results.

| Link label | Intended destination |
|---|---|
| CE Examples for New Users | Officially documented CE browser demo; external runtime remains unverified |
| Explore Use-Case Examples | Decision Labs or documented simulated learning scenarios; external and limited |
| Test CE with Your Own Data | Local Python workflow using quickstarts, notebooks and pipeline integration |
| Practical Workflows | Existing get-started, task, practitioner and interpretation guides |
| Evaluate & Compare | Existing comparison, semantics and evaluation material |

The three experiences remain distinct: beginner interaction, decision-oriented
use-case exploration, and local coding with the user's own predictive data.
There is no claim of browser dataset upload.

### Door 4 - CE Software & Integration

**Description:** Understand how the CE library is built, installed, integrated,
extended and maintained.

| Link label | Intended destination |
|---|---|
| Software Overview & Versions | Capabilities, metadata, changelog and upgrade material |
| Installation & Configuration | `docs/get-started/installation.md` |
| Internal Software Architecture | `docs/foundations/concepts/architecture.md` plus verified source boundaries |
| API & Technical Reference | `docs/api/index.md` and API reference pages |
| Model & Pipeline Integration | `docs/foundations/how-to/integrate_with_pipelines.md` |
| Extensions & Customization | Plugin and contributor extension contracts |
| Troubleshooting & Upgrades | Troubleshooting, migration and upgrade hubs |

Internal architecture and public API are separate destinations. Architecture
descriptions must not imply that every internal component is public or stable.

### Door 5 - CE Project, Vision & Evolution

**Description:** Learn about CE's origins, research contributions, development
history, future direction and ecosystem.

| Link label | Intended destination |
|---|---|
| Vision, Origins & History | README/project evidence; a coherent landing page is not yet verified |
| Research & Publications | Researcher hub, citing page and replication material |
| Development & Roadmap | Roadmap, changelog, current-work plans and release guidance |
| Community & Contributions | Contributor hub and contribution guide |
| CE Ecosystem | Demo, plugins, companion projects and separately documented Grejna AB link |

The ecosystem card must distinguish the open-source CE library, official
companion resources, external tools and optional commercial services. It must
not infer ownership, endorsement or functionality.

## Guided learning paths

Place these below the five doors:

- **New to CE:** Concepts -> Demo -> First example.
- **Practitioner:** Applications -> Workflows -> Integration.
- **Researcher:** Theory -> Semantics -> Research.
- **Developer / Contributor:** Architecture -> API -> Contributions.

Reuse existing audience hubs rather than replacing them:
`docs/get-started/index.md`, `docs/practitioner/index.md`,
`docs/researcher/index.md`, and `docs/contributor/index.md`.

## Evidence and unresolved wording

- The browser demo is documented at `docs/index.md:36-45`; its runtime and
  upload behavior were not tested.
- Decision Labs is linked at `docs/index.md:25-34`; only simulated learning
  scenarios are repository-verified.
- Local package metadata says `1.1.0-dev` at `pyproject.toml:10`, citation
  metadata says `v1.0.2` at `CITATION.cff:68`, and the homepage says `1.0.0`
  stable at `docs/index.md:13-23`. The homepage must avoid a single “current
  stable version” claim until reconciled.
- Canonical semantics are mode-specific at
  `docs/foundations/concepts/calibrated_interval_semantics.md:5-60`.

## Approval decisions required before Stage 2B

1. Whether the five doors should be implemented directly in `docs/index.md`.
2. Whether a navigation-only landing page is acceptable for Door 5, and
   whether Door 1 should remain homepage-only.
3. Whether a future educational page for “Understanding AI Models” is in scope.
4. Whether notebook links belong in the Door 3 homepage grid.
5. Which version wording is authoritative for the homepage notice.

