# Master audit — official CE vs Beta documentation

**Date:** 2026-11-13 18:00–19:00 (+01:00). **Auditor:** Claude Code (autonomous
run under the PO master prompt). **Status:** findings verified as marked;
nothing here changes official resources.

## 1. Scope and sources

| # | Source | State audited | How |
|---|---|---|---|
| S1 | Official GitHub `Moffran/calibrated_explanations` | `upstream/main` = `371bd806` (2026-11-07), fetched read-only; tag `v1.0.2` (`609d7b72`, current PyPI release per `pyproject.toml`) | local remote `upstream`, `git ls-tree`/`git diff`/`git grep` |
| S2 | Official Read the Docs (stable) | sidebar v1.0.2; audience-hub navigation (Get started, Practitioner, Researcher, Contributor, Core references) | WebFetch 2026-11-13 (earlier session) |
| S3 | Beta GitHub `ashraf-widaa/calibrated-explanations-docs-dev` | `main` = `a55c7e9d` | `git ls-remote docs-dev` |
| S4 | Published Beta RTD | `latest` = `a55c7e9d`, build 35848974 success (2026-11-12 19:36 UTC); 6 versions, only `latest` active | RTD API v3 (public) |
| S5 | Local Beta | `beta/v1-reference` = `917a04e2` (WP-1 checkpoint) | working repository |

**Synchronisation finding.** S3 = S4 (`a55c7e9d`). S5 is ahead by the planning
commits and WP-1 (`8fedaf4d`…`917a04e2`), none published. Beta's code (`src/`,
version `1.1.0-dev`) is **one official commit behind** S1 (`371bd806`).

## 2. Coverage

- **Pages.** All 107 official documentation pages exist in Beta (same paths);
  Beta adds 24 pages (Quick Start paths, glossary, section landings, methods
  page, workflow page, evaluation guide, what-is-ce, tutorials hub). No official
  page is missing from Beta.
- **Official documentation drift since the Beta fork.** None: between the fork
  point `f908527f` (2026-11-04) and `upstream/main`, only code, ADR-021 and the
  CHANGELOG changed (`371bd806`).
- **Release vs development.** Every feature used by the Beta tutorials exists
  in released v1.0.2 (`GuardedOptions`, `get_guarded_audit`, `save_state`/
  `load_state`, `normalization="simplex"`, `multi_labels_enabled`,
  `explore_alternatives`, `low_high_percentiles`, `features_to_ignore`,
  `add_conjunctions`, `to_narrative`). **Verified by execution:** with the
  v1.0.2 source (worktree of the tag), the four executed tutorials print exactly
  the outputs shown on their pages (8/8 tests pass), and the walkthrough
  generator reproduces `quickstart_walkthrough.md` and `ce-by-example.md`
  byte for byte. Readers who install the PyPI release see the published
  numbers.

## 3. Comparison matrix

Severity: **C** critical (wrong fact a reader will act on) · **H** high · **M**
medium · **L** low. Status: **V** verified · **P** pending author/PO · **R**
resolved in this run (see register).

| # | Topic | Official source | Beta counterpart | Finding | Evidence | Sev. | Recommendation | WP | Status |
|---|---|---|---|---|---|---|---|---|---|
| A-01 | One-sided interval regression endpoints | `371bd806` CHANGELOG; ADR-021 §2/§4 | `tasks/regression.md:34–40`; `foundations/concepts/calibration_methods.md:587` | Beta (and official docs) still say the open side "is reported as the smallest/largest target value in the calibration set"; from v1.1.0 (`371bd806`) the open side is `-inf`/`inf` and JSON encodes `"-inf"`/`"inf"`; v1.0.2 keeps the placeholder | upstream diff; Beta pages | **H** | Version-aware wording: placeholder in v1.0.2, unbounded from v1.1.0; never a calibrated bound | WP-19 (new) | V |
| A-02 | Beta code vs official main | `371bd806` | Beta `src/` | Beta's development code lacks the one-sided fix; docs examples run against Beta `src/` | `git rev-list HEAD..upstream/main` = 1 | M | Keep docs version-neutral now; sync `src/` with upstream only by PO decision (D-23) | — | P |
| A-03 | Version shown vs version readers install | `pyproject.toml` v1.0.2 (tag) | Beta sidebar "v1.1.0.dev0" | Readers install 1.0.2; the docs label says 1.1.0.dev0 without saying which version the examples were verified with | A-02 verification above | M | State "examples verified with v1.0.2 and 1.1.0-dev" on the tutorials hub and Quick API | WP-6 | V |
| A-04 | Regulatory claims in a beginner section | — (Beta adds the card) | `practitioner/playbooks/eu-ai-act-compliance.md:478`, linked as "Trustworthy AI" from CE: What & Why | "Empirical coverage vs. nominal confidence (Venn-Abers guarantee) — **Covered**" conflates coverage, confidence and Venn–Abers and asserts compliance coverage | page line 478 | **H** | Author review (N-01); relabel the card as regulation context | WP-8, WP-13 | P |
| A-05 | Percentiles described as "confidence levels" | official `tasks/regression.md` (same text) | `tasks/regression.md:58` | Percentile choice (coverage level of a prediction interval) called "confidence levels" | page line 58 | M | "coverage level"/"percentiles" | WP-8 | V |
| A-06 | Aleatoric/epistemic terminology | official task pages, ensured playbook | `tasks/classification.md:44`, `tasks/probabilistic_regression.md:81`, `practitioner/playbooks/ensured-explanations.md` | Terms used without a canonical definition; "more reliable intervention recommendations" is causal-sounding | concept locator | M | Author review (SR-07, SR-08); neutral interim wording | WP-8 | P |
| A-07 | Counterfactual / "necessary to flip" | official `tasks/classification.md` | `tasks/classification.md:23,52` | Causal wording for alternatives | page lines | M | Neutral wording with SR-08 marker | WP-8 | V |
| A-08 | Outdated agent-guide call | official `get-started/ce_first_agent_guide.md` (same) | same page, block 6 | `explore_alternatives(..., ensure_coverage=True, ensure_order=True)` → `ConfigurationError`; neither name in `src/` (v1.0.2 or dev) | execution audit | **H** | Replace with supported calls | WP-7 | V |
| A-09 | Outdated plugin contract example | official `contributor/plugin-contract.md` | same | `plugin_meta` lacks required `data_modalities` (ADR-033) → `ValidationError` | execution audit | **H** | Add `data_modalities` | WP-7 | V |
| A-10 | Removed private import | official `contributor/extending/plugin-advanced-contract.md` | same | imports `_EXPLANATION_PLUGINS` (absent) | execution audit | M | Use the public registry API | WP-7 | V |
| A-11 | Retrieval example | official `practitioner/advanced/explanation_retrieval.md` | same | indented block; `expl.factual` not found in `src/` | execution audit | M | Correct after reproducing | WP-7 | V |
| A-12 | Config manager ordering trap | official `foundations/how-to/configure_runtime.md` | same | block 1 fails after block 0 ("already been initialized") | execution audit | L | Explain the order | WP-7 | V |
| A-13 | Schema sketch in a `python` fence | official `foundations/concepts/explanation_structures.md` | same | not valid Python | execution audit | L | Use a `text` fence | WP-7 | V |
| A-14 | Unsupported comparison claim | official `compare.md` | same | "more stable rules" without evidence; 20-line page | page | M | Design comparison (D-6) | WP-5 | P |
| A-15 | Release notes stale | official `foundations/governance/release_notes.md` | same | latest entry v0.10.2; CHANGELOG at v1.0.2 / 1.1.0-dev | file | M | Pointer to CHANGELOG | WP-11 | V |
| A-16 | Assumption wording | official semantics notes | 9 Beta pages | "exchangeable or distribution-matched" vs exchangeability-only wording elsewhere | grep | M | Author answer SR-01 | WP-4d | P |
| A-17 | Calibration intuition (L1) | official has none | sidebar "Calibration & Uncertainty" opens the L3 semantics page | No L1 entry for calibration/uncertainty; V-6 (three output types) missing | 08/15 | M | V-6 on the existing semantics page (no new page) | WP-3/V-6 | V |
| A-18 | Phone tables | — | C1 capability table (+244 px), A1 task table (+67 px) and 13 tables elsewhere | Tables scroll inside their container at 390 px | Playwright | L | Phone-stack pattern | WP-18 | V |
| A-19 | Interpret page mixes audiences | official same | `foundations/how-to/interpret_explanations.md` §4 telemetry | Operations content in a reading guide | page | L | Link instead | WP-14 | V |
| A-20 | Thin hubs | official same | `tasks/index` 59 words, `practitioner/index` 81, `researcher/index` 73, `contributor/index` 79, `api/index` 102 | Little orientation | Playwright word counts | L | Purpose + "which page" tables | WP-15/16/17 | V |
| A-21 | Missing contributor setup page | official CONTRIBUTING.md (not rendered) | contributor hub | No setup page; hub cites unreachable files | 01/08 | M | Requires new page approval (D-7) | WP-10 | P |
| A-22 | Navigation and learning design | audience hubs | seven entry points + Quick Start A/B/C | **Intentional Beta improvement**: entry points by reader goal, code-free Quick Start, verified tutorials, glossary, methods page | — | — | Keep | — | V |
| A-23 | Reproducibility of examples | official quickstarts (fragments, no output) | executed tutorials with output-match tests | **Intentional Beta improvement**, now verified on v1.0.2 too | §2 | — | Keep | — | V |

## 4. Scientific risks (summary)

High: A-01 (wrong endpoint semantics for v1.1.0), A-04 (compliance claim). Open
author questions remain SR-01…SR-16 plus N-01…N-04 (`15`, WP-8); none is
resolved by this audit.

## 5. Prioritised recommendations

1. Correct A-01, A-05, A-07, A-08…A-13 (scientific errors and outdated code) —
   **Beta V2**.
2. Author-review sheet for A-04, A-06, A-16 and SR items — **Beta V2**.
3. V-6 (three output types) on the existing semantics page; phone tables
   (A-18) — **Beta V3**.
4. A-03 version statement — **Beta V2**.
5. New pages (calibration intuition as a separate page, contributor setup,
   explainable-AI page) wait for PO approval of new pages.
