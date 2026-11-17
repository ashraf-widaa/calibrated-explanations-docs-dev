# Batch 1 — Scientific consistency

## Authorization and baseline

- Approved implementation base: `beta/author-review-20261117`,
  `2bc637bc9b55febf77215783e2cbf3ab4288a520`.
- Implementation branch: `beta/enhancement-20261117-b1`.
- Isolated worktree: `D:/Jönkoping/CE-Documentation-Redesign/ce-enhancement-20261117`.
- Official comparison remains pinned to
  `371bd8060bd279fbfd41f7509097617561ac1ae4`; this cycle does not adopt later upstream changes.
- The worktree path and branch were absent before creation. The original ten
  worktrees had no tracked changes. The original checkout retained its existing
  untracked `artifacts/worktrees/` directory.
- Authorization covers Batch 1 implementation and validation only. No commits,
  staging, merges, pushes, resets, cleaning or publication are authorized.

These edits clarify existing explanations. They do not change CE source code,
scientific equations, example code, published numeric outputs, figures, notebook
artifacts, navigation or the four main documentation sections and resource links.
The continuous worked example, unfavorable Brier result, non-additivity explanation,
guarded audit and existing author-review register are preserved.

## File-by-file correction and evidence register

All documentation paths below are relative to `docs/`. Each row records a
remaining inconsistency in the approved base, rather than reopening already
corrected material.

| File | Correction | Scientific justification and evidence | Review boundary |
|---|---|---|---|
| `get-started/index.md` | Distinguish probability pair, merged estimate and target interval; link protocol qualifications. | Existing canonical semantics, modes 1–3; Vovk et al. (2015). | Exact validity statements remain open. |
| `what-is-ce.md` | Qualify calibration/accuracy language, request-dependent prediction bounds and fitted-component/data prerequisites. | Canonical semantics; `core/wrap_explainer.py:predict`/`predict_proba` default `uq_interval=False`; methods assumptions. | No new guarantee for a merged estimate or feature range. |
| `get-started/why-ce.md` | State joint exchangeability and fixed model/preprocessing; replace ambiguous denial of all individual information with no correctness/probability-containment guarantee. | Existing exchangeability definition; calibration methods assumptions; held-out-data protocol. | Empirical calibration checks do not establish exchangeability. |
| `glossary/science.md` | Align Venn–Abers, uncertainty interval and probabilistic regression definitions with the pair/merge and target/event distinctions. | Canonical semantics and methods; `calibration/venn_abers.py:predict_proba`; CE regression paper §3.3. | Multiclass and event validity wording remains open. |
| `foundations/concepts/probabilistic_regression.md` | Replace "the calibration [is] the same" with the full-set CPS versus split CPS/VA construction. | `calibration/interval_regressor.py:pre_fit_for_probabilistic`, `compute_proba_cal`; CE regression paper §3.3. | Computational construction does not settle SR-15. |
| `get-started/ce-tasks-and-modes.md` | Remove unsupported advice to compare rescaled uncertainty across classes; distinguish preserved raw pairs from normalized estimates. | `calibration/venn_abers.py:344–359`: SIMPLEX preserves bounds, SCALE rescales them. | Joint multiclass and predicted-class-selection validity remains SR-13. |
| `get-started/quickstart_classification.md` | Identify the call-local SIMPLEX-to-default-SCALE transition without changing calls or outputs; qualify a deterministic narrowing claim. | Same normalization implementation; existing prediction table and explanation plot. | More data is not a per-case monotonic-width theorem. |
| `foundations/concepts/ce_workflow.md` | Align mode table with merged estimates, raw versus rescaled bounds and marginal target coverage. | Existing canonical semantics; Venn–Abers merge implementation. | Exact coverage wording remains under review. |
| `foundations/how-to/interpret_explanations.md` | Correct point-weight versus interval-bar meaning, dark/light portions, grey baseline band and prediction marker. | Existing walkthrough §7; `explanations/explanation.py:2056–2065`; default factual uncertainty renderer in `viz/matplotlib_adapter.py`. | Zero exclusion is descriptive, not a significance test or feature-coverage theorem. |
| `foundations/concepts/calibration_methods.md` | Qualify default `interval_summary`, width intuition, multiclass normalization and the scope/conditions of the CPS derivation; replace version-only endpoint claims with pinned-source behavior. | `venn_abers.py:396–405`; split-CPS implementation; retained mathematical derivation and review markers. | No equations or author decisions changed. |
| `tasks/regression.md` | Identify Beta and official endpoint behavior by source revision instead of promising that `1.1.0-dev` determines it. | Both `pyproject.toml` files say `1.1.0-dev`. Beta `interval_regressor.py:299–307` uses calibration extrema; official `371bd806:299–306` returns infinities. | Intended release behavior and implementation reconciliation require maintainer review. |
| `tests/docs/test_beta_v2_corrections.py` | Update the existing endpoint documentation guard to require both pinned behaviors and the shared-version caveat. | The old assertion required the incorrect version-only distinction. | This is a documentation consistency check, not proof of coverage or runtime behavior. |

## Scientific sources

- [Vovk, Petej and Fedorova (2015), Large-scale probabilistic predictors](https://arxiv.org/abs/1511.00213):
  merging loses the multiprobability predictor's theoretical perfect-calibration property.
- [Löfström et al. (2025), Calibrated explanations for regression](https://doi.org/10.1007/s10994-024-06642-8),
  §§3.3–3.4: CPS/VA calibration split and limits on transferring prediction
  guarantees to artificial feature perturbations.
- Official documentation at `371bd806`, especially
  `docs/foundations/concepts/calibrated_interval_semantics.md`, and ADR-021.
- Approved-base source at `2bc637bc`; no later implementation is inferred from
  a development version label or a moving `main` URL.

## Unresolved scientific and compatibility questions

The existing register at
`development/reports/docs-focused-20261116/author-review.md` remains authoritative
for the open items. This batch closes none of them:

1. **SR-01:** approved exchangeability/data-use formulation and fitted-component
   conditions; whether any alternative distribution-match formulation is sufficient.
2. **SR-02:** exact finite-sample CPS statement, ties, extreme/open endpoints,
   difficulty estimates and conditions for category-wise coverage.
3. **SR-03/SR-13:** exact pair/merged wording, rescaled multiclass bounds,
   cross-class comparisons and any validity after selecting the predicted class.
4. **SR-07/SR-09/SR-14:** interpretation of averaged scenario bounds, feature-weight
   ranges, ensured filtering and conjunctions. No significance or causal claim is added.
5. **SR-15:** validity of the implemented split-CPS-score/VA event construction
   and its merged output.
6. **Endpoint compatibility:** intended release behavior given the two pinned
   implementations sharing `1.1.0-dev`; resolve in the library's own process.

The live upstream previously advertised `5c16eda8`, absent locally. It is not
fetched, incorporated or represented as reviewed here. Installation fixes,
executable Quick Start changes, evaluation extensions, layout and figure-numbering
work remain outside Batch 1. No author or reviewer has been contacted.

## Validation

Executed against this worktree's source with the existing system Python; the
project virtual environments lacked the example-test dependencies. No packages
were installed and no shared environment was changed.

| Check | Result and interpretation |
|---|---|
| Existing documentation suite | **365 passed**, including executed quickstarts, methods-page examples and recomputed toy numbers. This establishes tested example/API behavior, not statistical validity. |
| Strict Beta HTML build | **Exit 0**, no Sphinx warnings. Built from a temporary copy with `nbsphinx_execute=never`; this does not claim fresh notebook execution. |
| Built internal links | **158 pages; zero broken links**. |
| Validation integrity | SHA-256 comparison of every tracked file before/after validation: **zero changes**. Tests also had an audit hook denying writes into the project workspace. |
| Whitespace | `git diff --check` passed. |

The first run had 362 passes and three exact-phrase failures. Two compatible
phrases were retained in the revised prose; the endpoint guard was corrected
to require source-revision evidence rather than the misleading version-only
claim. The complete suite then passed. No runtime example failure was hidden.

One visible Python `UserWarning` says `CE_DOCS_BETA` is an unknown CE configuration
variable and is ignored by `ConfigManager`. The variable enables the existing
documentation banner; it does not configure model behavior. It was not suppressed.
The same notice appears during autodoc imports and is distinct from a Sphinx warning.

Environment: Python 3.13.7; pytest 9.0.3; Sphinx 7.4.7; NumPy 2.3.4;
scikit-learn 1.8.0; crepes 0.9.1; venn-abers 1.5.4; Matplotlib 3.11.2;
numpydoc 1.10.0; MyST 3.0.1; Furo 2025.12.19. The imported CE module was
verified to come from this worktree, version `1.1.0.dev0`. This is not a clean
installation test or RTD's Python 3.11 environment.

Raw evidence is outside the repository:
`C:/Users/ashra/AppData/Local/Temp/ce-batch1-final-20261117-zauy62sv/`:
`pytest.log`, `pytest.xml`, `sphinx.log`, `internal-links.log`,
`protected-before.json` and `summary.json`. No generated build files were
written into a surviving checkout. The parent pytest conftest was excluded
because it writes workspace diagnostic files; no required fixtures for these
documentation tests were omitted.

After a final grammar correction, the copied methods page was refreshed and
the strict incremental build also passed (`sphinx-final.log`). Fenced example
code, printed outputs, display equations and raw-HTML figures were compared
with the approved base and remain byte-for-byte equal; glossary-definition
fences are intentionally excluded. All edited page headings remain equal.
The homepage, section pages, CSS/SVG/PNG assets, templates, generated walkthrough,
generator and existing author-review register have no diff. All ten original
worktrees still have no tracked modifications; the new worktree makes eleven.

Git scope: 11 documentation files and one existing test modified, plus this
new report. The tracked diff is 147 insertions and 82 deletions; Git's normal
diff statistics omit this untracked report. Nothing is staged, and HEAD remains
the approved `2bc637bc` base. The broader library/quick-profile suite is not a
substitute for these documentation checks and was not run; the existing
environment lacks mypy and ruff. No dependency or tool installation was attempted.

Equivalent commands (the runner also applies the workspace-write audit hook):

```text
PYTHONPATH=<worktree>/src;<worktree>
PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 MPLBACKEND=Agg
CE_DOCS_BETA=true MPLCONFIGDIR=<temporary-output>/matplotlib
python -B -m pytest -c <worktree>/pyproject.toml --rootdir <temporary-output> --confcutdir <worktree>/tests/docs -o addopts= -p no:cacheprovider --basetemp <temporary-output>/pytest-temp --junitxml <temporary-output>/pytest.xml -q tests/docs
python -B -m sphinx -W --keep-going -E -b html -D nbsphinx_execute=never <temporary-source-copy>/docs <temporary-output>/html
python -B scripts/docs/check_internal_links.py <temporary-output>/html
git diff --check
```

No library/API migration is introduced. Batch 1 remains uncommitted and awaits
Product Owner review; Batches 2–5 have not started.
