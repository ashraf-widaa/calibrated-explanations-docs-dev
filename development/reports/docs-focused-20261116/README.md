# Focused CE documentation improvement cycle — 16 November 2026

## Scope and protected baseline

Approved Package A (verified corrections) and Package B (CE-centered educational
improvements), based exactly on `481ee05ba8abea826d6b135ab008d223b69fbdc4`.
Implementation branch: `beta/focused-ce-improvements-20261116`.

No public pages were added or removed. The seven homepage entries, Quick Start
Paths A/B/C, L1/L2/L3 distinction, sidebar structure, and page URLs remain intact.
Renamed regulatory headings retain their former anchors. Source code,
dependencies, notebook environments, the official repository, Beta main/latest,
and the published enhancement branch are outside this change.

## Package A — corrected issues

| Pages | Issue and correction | Evidence / boundary |
|---|---|---|
| `foundations/concepts/calibrated_interval_semantics` | Distinguish pair, merged estimate, multiclass rescaling, target coverage and explanation ranges. State the calibration protocol and keep exact validity wording under review. | ADR-021; existing methods page; Vovk et al. (2015). No author question is closed. |
| `get-started/quick_api`, `quickstart_classification`, `quickstart_regression`, `quickstart_guarded`; `tasks/classification`, `tasks/regression`, `tasks/probabilistic_regression` | Align repeated guarantee/assumption notes with that distinction. Mark the all-class support matrix experimental. | Public wrapper behavior, existing Path C qualifications, SR-01/03/13/15. |
| `compare` | Replace unsupported superiority/stability bullets with an output-and-assumptions comparison. | Existing CE method descriptions and cited method papers; SR-06 remains open. |
| `get-started/why-ce`, `what-is-ce` | Remove implied transfer of calibration to explanation guarantees; distinguish dependence on assumptions from conditional coverage. | Existing no-feature-guarantee statements and methods reference. |
| `foundations/how-to/interpret_explanations` | Correct rule-dictionary and public payload/telemetry descriptions, explain output units, and remove intervention-selection advice. | Executed public API fragments and worked-case assertions. |
| `foundations/concepts/explanation_structures` | Correct the rule-state flag names. | `explanations/explanation.py`. This remains internal reference material. |
| `foundations/how-to/integrate_with_pipelines` | Distinguish training-time transformer fitting from subsequent calibration-time transformation in the example. | `core/wrap_explainer.py` preprocessing paths. |
| `practitioner/playbooks/ensured-explanations`, `glossary/science` | Describe the implementation's no-wider filter; remove unsupported domain thresholds, uncertainty-decomposition claims, intervention promises and invented helper attributes. Preserve the review marker. | Public `ensured_explanations` source/docstring and existing examples. |
| `practitioner/playbooks/eu-ai-act-compliance` | Withdraw probability-containment-as-coverage and certification claims; replace compliance verdicts with review status; distinguish Articles 50 and 86. | Public API output shapes; official article references. Legal applicability remains open. |
| `practitioner/playbooks/eu-data-liability-compliance` | Correct COM(2022)496 withdrawal, Article 26/27 attribution, and repeated status/checklist claims; withdraw unreviewed draft-liability and local-to-global conclusions. | European Parliament withdrawal record and official DSA text. Other mappings remain explicitly subject to legal review. |

Commits:

- `88a331cf`: scientific/API qualifications and corrections.
- `bcd5a787`: regulatory facts, regression guards and author-review questions.
- `0a91337b`: preserve the exact established glossary review marker.

## Package B — educational changes

| Pages | Improvement |
|---|---|
| `get-started/ml-foundations` | Shorten peripheral AI/ML survey material while retaining features, targets, supervised tasks, training/inference, model compatibility, data roles, leakage and explanations. Keep section anchors; link deeper model-selection background externally. |
| `foundations/concepts/ce_workflow` | Explain the existing case through original prediction, factual condition, substituted values, scenario output, weight and derived range. State which class is being explained and retain the no-causality/no-feature-coverage boundary. |
| `sections/how-ce-works`, `sections/what-and-why` | Make the learning promise CE-specific and place construction/interpretation before derivations in the suggested reading list. Keep the existing sidebar and all destinations. |
| `sections/in-practice`, `sections/software-integration`, `api/index`, `foundations/index` | Route newcomers to the complete own-data workflow and Quick API, then to pipeline or method detail. Add cross-references without a new navigation level. |
| `get-started/apply-overview`, `foundations/how-to/conditional_calibration` | Qualify sample-size/width heuristics and explain why there is no universal adequate category count. |
| `get-started/apply-to-your-data` | Replace the unreproduced saturated-probability diagnosis for empty rules with a configuration check and a request for a reproducing case. |
| `foundations/how-to/interpret_explanations` | Explain fragment prerequisites and distinguish the original prediction range in factual metadata from alternative scenario ranges. |

Commits: `95b475c7` (CE worked case/background) and `efdc9ad1`
(practical routes and interpretation context).

The ML essentials page falls from 1,766 to 1,491 word tokens under the same
word-count script, approximately 16% shorter. This is a size observation, not
a measure of educational quality.

## Significant before/after examples

| Before | After |
|---|---|
| "every explanation inherits the calibration" | Explanations are computed from calibrated outputs; this does not transfer a prediction guarantee to a feature weight. |
| "actively reduce epistemic uncertainty" and "more reliable intervention recommendations" | The ensured filter compares reported widths; scientific interpretation remains under review and no intervention guarantee is claimed. |
| Predicted probability inside its own bounds labeled empirical coverage | Remove that calculation; link separately to held-out probability metrics and regression target coverage. |
| AI Liability Directive still in progress in February 2026 | Commission withdrawal recorded on 6 October 2025; draft effects are not presented as current obligations. |
| A one-paragraph rule/weight construction | Worked case: original P(benign)=0.286; substituted scenario=0.476; factual weight=−0.190; scenario range [0.333, 0.600]; derived weight range approximately [−0.31, −0.05]. |

The numerical explanation is an implementation/example observation. Its ranges
are not promoted to a theorem about feature coverage or causal actionability.

## Validation

Raw outputs are local under `reports/verification/docs-focused-20261116/`.

| Gate | Result |
|---|---|
| Docs suite plus affected interpretation/Quick API integration examples | **369 passed** |
| Strict Beta and standard Sphinx builds, including clean `-E` builds | **Exit 0; zero Sphinx warnings** |
| Internal links in both builds | **158 pages each; zero broken links** |
| Layout audit | **128 scenarios: 32 pages × 390/1440 px × light/dark; zero detected issues** |
| Figure/math/accessibility-oriented checks | No broken images, missing image alt text, detected MathJax errors, unrendered math, or missing Beta notices on sampled pages |
| Build/source consistency | Copied Markdown sources match the final documentation files in both builds |
| `git diff --check` | Passed |
| `make quick` equivalent | `python scripts/local_checks.py --profile quick` cannot start: **mypy unavailable** |
| Targeted Ruff invocation | **Ruff unavailable** in the existing interpreter |

The environment was left unchanged. No dependency installation, notebook
environment repair, full repository test run or statistical/legal certification
was performed. Automated layout checks and representative screenshot inspection
do not constitute a complete accessibility or educational user study.

Commands (PowerShell; use the repository's existing documentation interpreter):

```powershell
$env:PYTHONPATH = "src"
$env:MPLBACKEND = "Agg"
python -B -m pytest -o addopts='' -ra -p no:cacheprovider tests/docs tests/integration/test_doc_examples_smoke.py::test_should_execute_interpretation_fragments_with_public_payloads tests/integration/test_doc_examples_smoke.py::test_quick_api_python_examples_execute_without_error
$env:CE_DOCS_BETA = "true"
python -B -m sphinx -W --keep-going -E -b html docs reports/verification/docs-focused-20261116/build-beta
Remove-Item Env:CE_DOCS_BETA
python -B -m sphinx -W --keep-going -E -b html docs reports/verification/docs-focused-20261116/build-standard
python -B scripts/docs/check_internal_links.py reports/verification/docs-focused-20261116/build-beta
python -B scripts/docs/check_internal_links.py reports/verification/docs-focused-20261116/build-standard
python -B development/reports/docs-focused-20261116/validate-layout.py --base http://127.0.0.1:8771/
```

Run the layout script from the repository root while the Beta build is served
locally; the output path is relative to the repository root.

## Review and publication

The new branch's isolated preview location is:
https://calibrated-explanations-beta.readthedocs.io/en/beta-focused-ce-improvements-20261116/

Deployment must be verified from the RTD version's build record and full Git
commit, rather than inferred from the URL or this report's own commit.
Publication evidence is recorded separately after the push; the final delivery
identifies the deployed commit and build.

Review [author-review.md](author-review.md) for unresolved questions. No author or
legal-review messages were sent. The next review should check the scientific
qualifications and the CE learning sequence on the isolated preview. Beta
main/latest promotion remains a separate Product Owner decision.
