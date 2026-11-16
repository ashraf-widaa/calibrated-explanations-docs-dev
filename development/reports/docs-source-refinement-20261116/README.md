# Source-faithful CE documentation refinement — 16 November 2026

## Scope and baseline

Approved Packages 1–4 refine existing explanations and correct verified technical
errors. Base: `c28679db5de356b4a21b501a898ad1770c45cb63`, the published focused
candidate. New branch: `beta/source-faithful-refinement-20261116`.

The comparison used original CE documentation at v1.0.2 (`609d7b72`) and
official main (`371bd806`), public implementation behavior, ADR-021 and STD-004.
Original pages remain the foundation; inherited errors are not restored merely
because they appear in the original. No scientific theorem or legal sufficiency
finding is introduced. The existing author-review register is retained and
extended at [author-review.md](../docs-focused-20261116/author-review.md).

Primary comparison and reference sources:

- [Official v1.0.2 documentation source](https://github.com/Moffran/calibrated_explanations/tree/609d7b728b76b7bfc1e831a9ca7986689c1b43d1/docs)
  and [published stable documentation](https://calibrated-explanations.readthedocs.io/en/stable/).
- [Official source at 371bd806](https://github.com/Moffran/calibrated_explanations/tree/371bd8060bd279fbfd41f7509097617561ac1ae4/src/calibrated_explanations).
- European Commission AI Act text: [Article 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50),
  [Article 86](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-86),
  [Article 27](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-27).
- [Product Liability Directive 2024/2853](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853).
  Article-title mappings were checked against the official indexed text; direct
  EUR-Lex retrieval encountered a browser-verification challenge. This was not a
  comprehensive legal audit, and no statutory sufficiency is asserted.

Twenty-one existing public pages changed. No public page, URL, homepage entry,
Quick Start path, learning-depth structure or sidebar destination was added or
removed. Historical headings retain their anchors. Source code, dependencies,
notebook environments and RTD configuration are unchanged.

## Page-by-page changes and sources

Paths in this table are relative to `docs/`.

| Page | Original issue and resulting improvement | Source / interpretation boundary |
|---|---|---|
| `practitioner/playbooks/decision-policies` | Binary/event bounds indexed as matrices; distinguish two-column probabilities from per-query bounds. Label application policy examples separately from guarantees. | Public `predict_proba`; executable mask and decision checks. |
| `practitioner/playbooks/eu-ai-act-compliance` | Correct indexing, nonexistent payload/printing calls, data roles, multiclass qualification, Annex III numbering, Article 50/86 distinction and Article 27 FRIA reference. Replace compliance, actionability and fairness conclusions with deployment-specific questions. Keep integration examples. | Original playbook; public rule APIs; official AI Act texts. Legal applicability remains open. |
| `practitioner/playbooks/eu-data-liability-compliance` | Correct indexing and unsupported `as_json`/`print_rules` calls. Inspect actual rules instead of a nonexistent JSON weight field. Narrow PLD mappings and withdraw the unsupported monetary threshold. Remove implications that CE establishes legal grounds, utility, discrimination, proportionality or a retention duty. | Original playbook; public payload/rule APIs; official PLD references. Legal interpretations remain review questions. |
| `practitioner/advanced/normalization-guide` | Correct the automatic-difficulty claim and internal configuration advice. Show public opt-in configuration with a fitted difficulty estimator, and distinguish width scaling from coverage. | `wrap_explainer.py:set_difficulty_estimator`, calibration implementation, installed crepes API. SR-02 remains open. |
| `foundations/concepts/parameter-reference` | Classification rejects a non-None threshold; distinguish event tuples, percentiles, guard thresholds and singleton-set rejection from merged-probability cutoffs. | Validation paths, `GuardedOptions`, reject implementation. Exact reject validity remains SR-16. |
| `api/calibrated_explainer` | Remove the inherited "true underlying uncertainty" claim, use a genuine held-out test split and explain that alternatives need not flip a label or be actionable. | Original API page and current public implementation. |
| `practitioner/playbooks/mondrian-calibration` | Reconcile unsupported 30–50-sample advice with existing qualified category-size guidance. | Existing conditional guide, CPS endpoints; no new sufficient count is asserted. |
| `researcher/advanced/theory_and_literature` | Separate published contributions, software behavior and validity claims; replace broad guarantee/epistemic summaries with scoped descriptions and review qualifications. Clarify bibliography and replication routes. | Original literature page and citation list; SR-07/SR-09 remain open. |
| `what-is-ce` | Distinguish two prediction tasks from three output modes. Focus its introduction on overview and suitability; shorten the repeated attribution-method discussion. | Original README and task pages; existing comparison and semantics references. |
| `get-started/ml-foundations` | Remove the peripheral model-family survey and algorithm diagram; retain a short random-forest example, model-interface requirements, features/targets, tasks and data separation. Shorten general XAI background while preserving references. | Original quickstarts and model interface; deeper general ML routes to scikit-learn. |
| `get-started/why-ce` | Make its role the workflow change; shorten repeated data-role and calibration definitions through descriptive links. | Original fit/calibrate/explain workflow and existing prerequisite pages. |
| `get-started/ce-tasks-and-modes` | Introduce task/mode/method/configuration terminology before output interpretation. Put detailed uncertainty qualifications after the core workflow and capability lookup. | Original task pages and existing semantics. All section destinations remain. |
| `get-started/apply-overview` | Distinguish the planning guide from runnable integration and empirical evaluation. | Existing own-data and evaluation guides. |
| `practitioner/evaluate_ce` | State that the page checks a working application rather than introducing integration again. | Original evaluation concepts and existing own-data workflow. |
| `foundations/concepts/ce_workflow` | Preserve the numerical construction; replace a repeated guarantee checklist with quantity-specific reading guidance and canonical links. | Existing worked case, original explanation implementation and canonical semantics. |
| `foundations/concepts/calibration_methods` | Link explanation construction before derivations; distinguish mathematical fractions from Python percentile values; make isotonic background's CE role explicit. | Original calibration code, existing derivations and API convention. Derivations and review markers retained. |
| `foundations/how-to/interpret_explanations` | Start with the reader's inspection task, then connect construction, payloads and plots; consistently call factual/alternative outputs explanation types. | Original public payload guide and existing workflow. |
| `foundations/concepts/explanation_structures` | State the developer audience and internal/private scope before the storage reference. Route application users to public interfaces. | Original internal reference and implementation. |
| `foundations/concepts/terminology_thresholded_vs_probabilistic_regression` | Shorten repeated equivalence explanations; retain historical inventory and policy in an optional maintainer dropdown with existing anchors. | Original terminology page and ADR-021. |
| `api/visualization` | Explain the current default first, link the usage guide and label v0.11.2 material as historical evidence. | Original PlotSpec page; no plotting contract changes. |
| `glossary/science` | Separate exchangeability's definition from the unresolved alternative "distribution-matched" wording. | Existing semantics and SR-01; the review marker remains. |

Already-effective homepage, section landings, tutorials, project/resource routes,
generated API signatures, schemas, migration instructions and other specialized
references were preserved. No mechanical documentation-wide rewrite was made.

## Representative before and after

| Before | After | Reason |
|---|---|---|
| `low[:, 1] > threshold` in a binary example | `low > threshold`, with output shapes explained | Avoid indexing a one-dimensional vector as a matrix. |
| "default CPS configuration handles difficulty automatically" | No estimator by default; fit and attach one explicitly | Match actual opt-in behavior. |
| `exp.as_json()` / `exp.print_rules()` | `exp.build_rules_payload()` / `print(exp.list_rules())` | Use existing public methods and serializable rule records. |
| Proper training data described as fitting calibration | Proper training fits the predictive model; held-out data calibrates CE | Preserve data roles and prevent leakage. |
| A six-step "compliance-ready deployment" | Six integration steps for scientific/legal review | A working library integration does not establish compliance. |
| Three tasks | Two prediction tasks, three output modes | Keep task and output interpretation distinct. |
| A model-family survey before data roles | A short model/interface explanation, then separate data roles | Keep prerequisites proportional to CE. |

The ML page decreases from 1,472 to 1,268 whitespace-separated
tokens including markup and examples. Length is a scope observation, not a
claim of measured educational improvement.

## Review questions

The existing register remains open: exact Venn–Abers/CPS and threshold-event
validity, multiclass bounds, explanation-weight/scenario-range interpretation,
ensured filtering and uncertainty decomposition, category-size advice, reject
validity and regulatory applicability. Neither example execution nor a successful
build resolves these questions. No messages were sent to authors or legal reviewers.

## Validation and limits

- Documentation suite and existing integration example file, excluding the
  wheel-install test: **377 passed; 1 deselected**. The deselected test installs
  dependencies into a new environment and is outside this documentation cycle.
- Added example checks exercise binary policy masks, threshold-event decisions,
  opt-in difficulty configuration and reset, regulatory query fragments and JSON
  payload round-trips. They establish API behavior, not statistical/legal validity.
- Clean strict Beta and standard Sphinx builds: **exit 0, zero Sphinx warnings**.
  Strict incremental builds also cover the final historical-anchor alias.
- Internal-link checks: **158 pages in each build, zero broken links**.
- Baseline compatibility: **1,201 heading anchors preserved**, no missing pages;
  copied Markdown matches current sources.
- Local layout: **124 scenarios**, 31 pages at 390/1440 px in light/dark,
  **zero detected issues**. The mathematics page renders 137 containers per
  scenario, with no detected math errors or unrendered expressions. Representative
  mobile screenshot inspected.
- `git diff --check`: passed. The quick profile cannot start because **mypy is
  unavailable**; **Ruff is unavailable** as well. The environment was preserved.

Initial test failures reproduced the documented indexing errors and revealed
unsupported printing/payload calls. Two older wording/table checks were updated
to reflect the approved background reduction and canonical-semantics links.
Initial Sphinx outputs exceeded Windows path limits; a short temporary output
path resolved that local tooling issue without configuration changes.

Raw evidence is local under `reports/verification/docs-source-refinement-20261116/`.
Build output is under `C:/Users/ashra/AppData/Local/Temp/ce-sr-20261116/` to avoid
the Windows path limit. Commands from this worktree (PowerShell):

```powershell
$env:PYTHONPATH = 'src'
$env:MPLBACKEND = 'Agg'
python -B -m pytest -o addopts='' -ra -p no:cacheprovider tests/docs tests/integration/test_doc_examples_smoke.py -k 'not wheel_install'
$env:CE_DOCS_BETA = 'true'
python -B -m sphinx -W --keep-going -E -b html docs C:/Users/ashra/AppData/Local/Temp/ce-sr-20261116/beta
Remove-Item Env:CE_DOCS_BETA
python -B -m sphinx -W --keep-going -E -b html docs C:/Users/ashra/AppData/Local/Temp/ce-sr-20261116/standard
python -B scripts/docs/check_internal_links.py C:/Users/ashra/AppData/Local/Temp/ce-sr-20261116/beta
python -B scripts/docs/check_internal_links.py C:/Users/ashra/AppData/Local/Temp/ce-sr-20261116/standard
python -B development/reports/docs-source-refinement-20261116/validate-layout.py --base http://127.0.0.1:8772/
```

Automated layout checks and representative inspection do not constitute a full
accessibility audit or educational user study. No full source-code regression
suite, dependency changes or notebook-environment work was performed.

## Publication and next review

Target isolated preview:
https://calibrated-explanations-beta.readthedocs.io/en/beta-source-faithful-refinement-20261116/

The final publication record must identify the RTD build and full deployed
commit; publication is not inferred from this target URL. The final delivery
records that evidence after push and activation. The official repository,
Beta main/latest and previous candidates are protected throughout.

Recommend final educational review on the isolated preview: follow Paths A/B/C
and L1/L2/L3, explain the running case in one's own words, and check whether
transitions between overview, mechanism, usage and interpretation are clear.
Route remaining scientific and legal questions to their reviewers separately.
Beta latest promotion is not part of this cycle.
