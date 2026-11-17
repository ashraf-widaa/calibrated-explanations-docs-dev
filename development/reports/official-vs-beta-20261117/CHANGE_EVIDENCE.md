# Comparison evidence and methodology

Evidence collected 17 November 2026. Scope is read-only source/site analysis plus these five reporting artifacts. No official source/doc changes, candidate edits, new RTD build/version, merges or latest promotion are part of this task.

## Exact baselines and deployment proof

| Source | Immutable source baseline | Independent RTD evidence |
|---|---|---|
| Official stable | `609d7b728b76b7bfc1e831a9ca7986689c1b43d1`; `v1.0.2` | [Version metadata](https://readthedocs.org/api/v3/projects/calibrated-explanations/versions/stable/) identifies tag/commit; [build 35281189](https://readthedocs.org/api/v3/projects/calibrated-explanations/builds/35281189/) reports success at the same commit |
| Beta review | `2bc637bc9b55febf77215783e2cbf3ab4288a520`; `beta/author-review-20261117` | [Version metadata](https://readthedocs.org/api/v3/projects/calibrated-explanations-beta/versions/beta-author-review-20261117/) reports active/built; [build 35951339](https://readthedocs.org/api/v3/projects/calibrated-explanations-beta/builds/35951339/) reports success at the exact candidate commit |

These are public authenticated-free GET observations, not activation/build actions. Official stable's successful build completed 20 October 2026; Beta's completed 17 November 2026. No ambiguity between current official main and deployed stable is used to attribute the changes. Source comparisons use the exact commits even if stable/main change later.

## Reproducing the direct tree comparison

Run in a clone containing both commits. Use two endpoints, not a sum of work-package diffs and not a three-dot merge-base comparison:

```powershell
git diff --no-renames --name-status 609d7b728b76b7bfc1e831a9ca7986689c1b43d1 2bc637bc9b55febf77215783e2cbf3ab4288a520
git diff --no-renames --numstat 609d7b728b76b7bfc1e831a9ca7986689c1b43d1 2bc637bc9b55febf77215783e2cbf3ab4288a520
git diff --no-renames 609d7b728b76b7bfc1e831a9ca7986689c1b43d1 2bc637bc9b55febf77215783e2cbf3ab4288a520 -- docs
git diff --no-renames 609d7b728b76b7bfc1e831a9ca7986689c1b43d1 2bc637bc9b55febf77215783e2cbf3ab4288a520 -- src tests pyproject.toml scripts/docs
git ls-tree -r --name-only 609d7b728b76b7bfc1e831a9ca7986689c1b43d1 -- docs
git ls-tree -r --name-only 2bc637bc9b55febf77215783e2cbf3ab4288a520 -- docs
git diff --stat 609d7b728b76b7bfc1e831a9ca7986689c1b43d1 2bc637bc9b55febf77215783e2cbf3ab4288a520
```

Git object bytes, rather than Windows checkout line endings, were extracted with `git archive --format=zip <commit>` for each endpoint. Each tracked page source was compared from those bytes. Relevant source and build snapshots were kept outside the repository; they are not deliverables requiring access to a Windows temporary path. All report conclusions can be traced to the immutable GitHub sources below and the public RTD records.

## Counting definitions and results

**Tracked page source:** tracked `docs/**/*.md` or `.rst` source, including hubs, compatibility pages and maintenance references. Includes 13 unchanged tracked autosummary RST stubs; excludes generated HTML outputs, assets, Python/config files, notebook download and reports outside docs. Official has 120 (107 Markdown pages + 13 RST API stubs), Beta 144 (131 Markdown pages + the same 13 RST stubs): 24 additions, 80 modifications, zero deletions, 40 byte-identical pages. Beta's 158 rendered HTML files include 14 generated index/search/viewcode pages beyond these tracked page sources; the two counts are intentionally different.

**Changed section slot:** split Markdown outside triple-backtick fenced blocks at ATX headings; key each block by path, literal heading and occurrence index, with a separate preamble slot. Compare block text including the heading. Count the union of changed/added/deleted keys: **586**. There are 510 incoming section blocks added/revised and 290 outgoing blocks removed/replaced under content-multiset comparison. These are alternative views, not additive figures. A renamed heading can produce two changed slots; moves and edits to footer/links can count a slot. This is a reproducible syntactic extent metric, not 586 independent pedagogical edits or scientific changes. Setext/RST heading parsing is not inferred from ATX syntax; the 13 tracked RST API stubs are unchanged and contribute no changed section slots.

**Python example block:** triple-backtick `python`, `py` or `{code-block} python` fence. Compare ordered full block bodies per page with `difflib.SequenceMatcher(autojunk=False)`. For a replace opcode, pair the shorter side as modified blocks and count surplus blocks as added/deleted. Result: **57 modified, 40 added, seven removed**. Other code/output languages, inline calls, notebook cells and prose-only interpretation changes are excluded. A block can be a stateful fragment, not an independently executable example; block alignment is structural rather than a semantic program identity test.

**Documentation link occurrence:** per-page multiset difference of Markdown hyperlinks excluding image syntax, MyST `doc`/`ref` roles and raw HTML `href`. Count repeated occurrences; do not count image `src`/`srcset`, generated sidebar links or code-generated links. Result: **567 additions, 43 removals**. Literal role bodies include display labels, so a relabelled role may count as removal/addition even if the destination is unchanged. The regex operates on source, including literal examples, rather than an AST-resolved unique-destination graph; these numbers must not be interpreted as 567 newly reachable pages. Sphinx directive `:link:` destinations are excluded. Rendered navigation is checked separately.

**Figures:** instructional placements in authored HTML: six original architecture Mermaid diagrams; Beta has those six plus two new Mermaid diagrams, six SVG-image placements and five PNG placements = **19**. Six diagrams are preserved with added explanatory prose; **13 placements are new**, using ten new physical SVG/PNG files (six SVG files include two narrow alternates; four PNG files include a shared walkthrough image). There are no modified existing instructional image files because official's instructional figures were Mermaid, whose definitions are preserved. The notebook repeats figures and is not counted again. Decorative GitHub/home icons, wave and index-collapse image are excluded.

**Lines/category:** Git `--no-renames --numstat` text lines; binary files have no line count. Categories are disjoint, assigned once from the final two-tree delta, not by stage history.

| Category | Changed path records | Lines added | Lines removed | Binary files |
|---|---:|---:|---:|---:|
| Other repository files | 15 | 482 | 121 | 0 |
| Development/learning reports | 135 | 12,984 | 0 | 0 |
| Documentation pages | 104 | 6,702 | 1,144 | 0 |
| Documentation assets/templates | 16 | 2,687 | 0 | 4 |
| Documentation build/configuration | 2 | 33 | 0 | 0 |
| Documentation tooling | 4 | 1,249 | 0 | 0 |
| Library implementation | 4 | 568 | 1 | 0 |
| Tests | 26 | 2,616 | 8 | 0 |

The total is **306 path records, +27,321/−1,274 text lines**. Default rename-aware Git reports **305 entries, +27,224/−1,177**: a pure 97-line release-plan move is represented as one zero-line rename instead of a deletion/addition. This is a counting-policy difference, not extra documentation work. Documentation-only pages/assets/templates/build configuration account for **122 paths, +9,422/−1,144**, including four PNG binaries. Root metadata, version/dependency/CI/governance changes and an unchanged-content plan move are under Other; they are not hidden within educational improvements. Development/learning reports are not published CE pages.

### Changed page files by documentation category

| Source subtree | Added | Modified | Removed | Unchanged |
|---|---:|---:|---:|---:|
| (docs root) | 1 | 7 | 0 | 1 |
| _autosummary | 0 | 0 | 0 | 13 |
| api | 0 | 4 | 0 | 2 |
| appendices | 0 | 2 | 0 | 1 |
| contributor | 0 | 6 | 0 | 3 |
| foundations | 2 | 26 | 0 | 10 |
| get-started | 7 | 8 | 0 | 1 |
| glossary | 3 | 0 | 0 | 0 |
| maintenance | 0 | 0 | 0 | 1 |
| migration | 0 | 1 | 0 | 2 |
| practitioner | 1 | 14 | 0 | 3 |
| researcher | 0 | 5 | 0 | 1 |
| sections | 9 | 0 | 0 | 0 |
| tasks | 0 | 5 | 0 | 0 |
| tutorials | 1 | 0 | 0 | 0 |
| upgrade | 0 | 2 | 0 | 2 |

## Source and API verification map

| Claim/difference | Immutable implementation or test reference | Evidence and limit |
|---|---|---|
| Binary and multiclass bounds / merging | [VennAbers.predict_proba](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/calibration/venn_abers.py#L225), binary bounds around L388, merge around L405 | Binary low/high are one-dimensional; default multiclass path differs. Shape verification is not a calibration theorem |
| Interval median/open sides | [IntervalRegressor.predict_uncertainty](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/calibration/interval_regressor.py#L256) | Requests percentile 50 for central estimate; open side returns calibration min/max at L303–307. This file has no direct official→Beta diff |
| Event probabilities and calibration halves | [predict_probability](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/calibration/interval_regressor.py#L162), [pre_fit_for_probabilistic](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/calibration/interval_regressor.py#L379) | Event path is not an ordinary target-interval query; composed validity remains SR-15 |
| Pipeline/difficulty setup | [WrapCalibratedExplainer.calibrate](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/core/wrap_explainer.py#L419), [set_difficulty_estimator](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/core/wrap_explainer.py#L902) | Proper-training fit and calibration transform are distinct; estimator is optional |
| Public rules/retrieval | [build_rules_payload](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/explanations/explanation.py#L402), [get_rules_by_feature](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/explanations/explanation.py#L1988) | Returned object method names support corrected snippets; private storage is not the application interface |
| Ensured filter | [ensured_explanations](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/explanations/explanation.py#L3579) | Width-filter behavior is inspectable; uncertainty-component or causal interpretations remain open |
| Final target/event tutorial transition | [integration test](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/tests/integration/test_doc_examples_smoke.py#L112) | Executes documented fragments and checks that a preceding threshold query does not change later target explanation semantics |
| Difficulty attachment | [integration test](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/tests/integration/test_doc_examples_smoke.py#L133) | Verifies reinitialization after public attachment; does not prove coverage |
| Binary decision masks and regulatory fragments | [integration tests](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/tests/integration/test_doc_examples_smoke.py#L78) | Correct low/high array indexing and public payload usage; no legal conclusion follows |
| Reject aliases and unsupported strategy | [integration tests](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/tests/integration/test_doc_examples_smoke.py#L193) | Supported public calls execute; unsupported wrapper keyword is documented as an error case |
| Inherited narrative API/schema | [narrative_spec.py](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/explanations/narrative_spec.py), [narrative_context serialization](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/src/calibrated_explanations/explanations/explanations.py#L849) | New immutable facts API and metadata are real library changes, separately reviewable from documentation prose |

### Independent public-API probe

Using the candidate's `src`, scikit-learn diabetes/breast-cancer datasets, seeded splits, 20-tree random forests and public `WrapCalibratedExplainer.fit`/`calibrate` (both lifecycle flags asserted):

```text
binary probability / lower / upper shapes: (2, 2), (2,), (2,)
threshold-event probability / lower / upper shapes: (1, 2), (1,), (1,)
regression default difficulty_estimator is None: True
predict(..., low_high_percentiles=(-inf, 95), uq_interval=True):
  lower = [47.0], calibration target minimum = 47.0, lower is finite = True
```

This validates the indexing/default corrections and exposes why the future one-sided note needs version scoping. It is not the tutorial's 100-tree numerical run and should not be used to replace its captured numbers.

## Independently rerun validation

| Check | Result in this comparison | Coverage / limitation |
|---|---|---|
| RTD identity | Both successful build records match exact source commits | Public metadata re-read; no new build triggered |
| Tests | **381 passed, one deselected**, 95.59 seconds | Candidate docs suite and integration examples; excludes wheel-install test; no dependency/environment changes |
| Fresh strict Beta Sphinx | **Exit 0, build succeeded**, no WARNING/ERROR/CRITICAL/UserWarning lines in final log | Python 3.13, Sphinx 7.4.7; a complete temporary source snapshot; no candidate page writes |
| Built internal checker | 158 HTML pages, zero broken links | Repository checker verifies pages/assets and fragments; run again on final complete build below |
| Published requests | 120 official source-page URLs + 158 Beta HTML URLs = **278 HTTP 200** | Existing full Beta HTML list includes generated/utility pages; official generated index/search/viewcode pages not all crawled |
| Published Beta internal destinations | **2,352 unique internal page/fragment or asset destinations; zero broken HTML targets** | HTML existence/fragment checks; all asset response statuses are not implied by the count; image loads sampled separately |
| Sidebar | **142 distinct source-page destinations**, two exceptions disclosed | getting_started_60s compatibility and unchanged multiclass gap-analysis page |
| Framework markers | Zero matches in Beta article text for tier/Level 1–3/L1–L3/learning-depth/reading-depth pattern | Exact bounded lexical scan, not a semantic guarantee that every navigational sentence is gone |
| Image figure prose | 11 figure blocks; each immediately followed by paragraph | Figure meanings assessed with actual assets/source; scientific interpretation remains reviewable |
| Math | 137 live HTML math elements; sampled browser pages contain rendered MathJax with no error elements | Does not prove every equation or mathematical claim correct |
| Live responsive/theme checks | **48 cases**, no document overflow, broken sampled images or MathJax error nodes | Four shared official/Beta pages × two widths × two themes = 32; four extra Beta pages × two widths × two themes = 16 |
| External references | Six sampled primary/reference URLs returned HTTP 200 | VA/CE papers, crepes, Guo paper and EP legislative procedure; not a full external-link audit |
| Incoming official anchors | **24 missing section IDs on 15 pages** | Full list below; successful internal checker cannot detect bookmarks from outside the current site |
| Mypy | Unavailable: `No module named mypy` | Not installed for this reporting task; no claim of complete quick-profile/type validation |

Reproduction commands (use a temporary output/source copy if preserving every candidate filesystem byte):

```powershell
$env:PYTHONPATH = 'src'
$env:MPLBACKEND = 'Agg'
python -B -m pytest -o addopts='' -q --tb=short -p no:cacheprovider tests/docs tests/integration/test_doc_examples_smoke.py -k 'not wheel_install'
$env:READTHEDOCS_PROJECT = 'calibrated-explanations-beta'
python -B -m sphinx -W --keep-going -E -b html <snapshot>/docs <temporary-html>
python scripts/docs/check_internal_links.py <temporary-html>
python -m mypy --version
```

The first temporary snapshot omitted root `ROADMAP.md`, causing a missing-include critical diagnostic and a consequent heading warning. It also used `CE_DOCS_BETA`, which ConfigManager warned was unknown. The final run restored root files from the candidate and used `READTHEDOCS_PROJECT=calibrated-explanations-beta`, the actual conditional used on RTD. No source-page repair or warning suppression was used. The final strict result supersedes that incomplete-snapshot failure, whose cause is disclosed here.

Live browser sample: shared `index`, regression tutorial, interpretation and architecture pages on both sites; additional Beta CE by example, walkthrough, calibration methods and interval semantics. Viewports 390×900 and 1365×900, light/dark. Browser observations included image complete/naturalWidth, Mermaid SVG existence, MathJax render/error state, document overflow and Beta picker-ready state. CE-by-example screenshots were visually inspected; the plot remains small inline on mobile, with a full-size link immediately after explanatory prose. These checks do not replace assistive-technology testing or every browser/device combination.

## Inherited evidence, independently labelled

- [Published candidate validation report](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/development/reports/docs-beta-review-20261117/README.md): targeted corrections, earlier strict local Beta/standard builds, 381-test result, immediate-parent anchor/content preservation and responsive checks. This is supporting history, not the source of the direct official→Beta metrics.
- [RTD build commands/log API](https://app.readthedocs.org/api/v2/build/35951339/): prior publication inspected Sphinx exit 0 and build-succeeded output without documentation warnings. The current task re-read build identity; the new local strict run is separate evidence.
- Prior publication validation covered 100 live layout/theme combinations and ten selector/full-size-image interactions, including 320/768px mobile-selector checks and a recoverable addon data-ready event retry. These interaction counts were **not** rerun in the 48-case comparison sample.
- Earlier all-article local/published text equivalence, figure asset decoded-pixel preservation relative to the immediately preceding candidate, and notebook execution reports are inherited. They do not imply the 24 missing official anchors are preserved.
- [Existing author-review register](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/development/reports/docs-focused-20261116/author-review.md) remains open and unchanged. Builds/tests do not close its scientific/legal questions.

## Official section anchors absent in Beta

For every official `article section[id]`, check whether any Beta article element on the same preserved page has that ID. Missing IDs are listed below. They include title IDs and replaced section IDs; no external inbound-link usage was measured. Some are historical/generated IDs rather than high-value bookmarks. Preserve important incoming links with explicit empty spans in a future authorized correction, without reintroducing removed instructional-framework content.

| Page | Missing official fragment | Current Beta page / proposed action |
|---|---|---|
| [compare.html](https://calibrated-explanations.readthedocs.io/en/stable/compare.html#vs-shap) | `vs-shap` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/compare.html); add compatibility alias if retained for inbound links |
| [compare.html](https://calibrated-explanations.readthedocs.io/en/stable/compare.html#vs-lime) | `vs-lime` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/compare.html); add compatibility alias if retained for inbound links |
| [compare.html](https://calibrated-explanations.readthedocs.io/en/stable/compare.html#vs-conformal-prediction-packages) | `vs-conformal-prediction-packages` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/compare.html); add compatibility alias if retained for inbound links |
| [getting_started_60s.html](https://calibrated-explanations.readthedocs.io/en/stable/getting_started_60s.html#second-decision-tree) | `second-decision-tree` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/getting_started_60s.html); add compatibility alias if retained for inbound links |
| [getting_started_60s.html](https://calibrated-explanations.readthedocs.io/en/stable/getting_started_60s.html#model-compatibility) | `model-compatibility` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/getting_started_60s.html); add compatibility alias if retained for inbound links |
| [getting_started_60s.html](https://calibrated-explanations.readthedocs.io/en/stable/getting_started_60s.html#calibration-split) | `calibration-split` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/getting_started_60s.html); add compatibility alias if retained for inbound links |
| [getting_started_60s.html](https://calibrated-explanations.readthedocs.io/en/stable/getting_started_60s.html#choose-mode) | `choose-mode` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/getting_started_60s.html); add compatibility alias if retained for inbound links |
| [getting_started_60s.html](https://calibrated-explanations.readthedocs.io/en/stable/getting_started_60s.html#minimal-flow) | `minimal-flow` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/getting_started_60s.html); add compatibility alias if retained for inbound links |
| [index.html](https://calibrated-explanations.readthedocs.io/en/stable/index.html#calibrated-explanations-documentation) | `calibrated-explanations-documentation` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/index.html); add compatibility alias if retained for inbound links |
| [index.html](https://calibrated-explanations.readthedocs.io/en/stable/index.html#companion-projects) | `companion-projects` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/index.html); add compatibility alias if retained for inbound links |
| [ROADMAP.html](https://calibrated-explanations.readthedocs.io/en/stable/ROADMAP.html#id1) | `id1` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/ROADMAP.html); add compatibility alias if retained for inbound links |
| [foundations/index.html](https://calibrated-explanations.readthedocs.io/en/stable/foundations/index.html#shared-foundations) | `shared-foundations` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/index.html); add compatibility alias if retained for inbound links |
| [get-started/index.html](https://calibrated-explanations.readthedocs.io/en/stable/get-started/index.html#get-started) | `get-started` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/index.html); add compatibility alias if retained for inbound links |
| [get-started/quickstart_classification.html](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_classification.html#classification-quickstart) | `classification-quickstart` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_classification.html); add compatibility alias if retained for inbound links |
| [get-started/quickstart_guarded.html](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_guarded.html#guarded-explanations-quickstart) | `guarded-explanations-quickstart` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_guarded.html); add compatibility alias if retained for inbound links |
| [get-started/quickstart_regression.html](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_regression.html#regression-quickstart) | `regression-quickstart` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_regression.html); add compatibility alias if retained for inbound links |
| [get-started/quickstart_regression.html](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_regression.html#interval-and-threshold-predictions) | `interval-and-threshold-predictions` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_regression.html); add compatibility alias if retained for inbound links |
| [get-started/quickstart_regression.html](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_regression.html#explore-alternatives) | `explore-alternatives` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_regression.html); add compatibility alias if retained for inbound links |
| [get-started/quick_api.html](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quick_api.html#quick-api) | `quick-api` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quick_api.html); add compatibility alias if retained for inbound links |
| [get-started/troubleshooting.html](https://calibrated-explanations.readthedocs.io/en/stable/get-started/troubleshooting.html#environment-troubleshooting) | `environment-troubleshooting` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/troubleshooting.html); add compatibility alias if retained for inbound links |
| [foundations/concepts/alternatives.html](https://calibrated-explanations.readthedocs.io/en/stable/foundations/concepts/alternatives.html#generate-alternatives) | `generate-alternatives` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/alternatives.html); add compatibility alias if retained for inbound links |
| [foundations/concepts/probabilistic_regression.html](https://calibrated-explanations.readthedocs.io/en/stable/foundations/concepts/probabilistic_regression.html#examples) | `examples` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/probabilistic_regression.html); add compatibility alias if retained for inbound links |
| [foundations/governance/nav_crosswalk.html](https://calibrated-explanations.readthedocs.io/en/stable/foundations/governance/nav_crosswalk.html#audience-first-structure-verification) | `audience-first-structure-verification` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/governance/nav_crosswalk.html); add compatibility alias if retained for inbound links |
| [foundations/how-to/interpret_explanations.html](https://calibrated-explanations.readthedocs.io/en/stable/foundations/how-to/interpret_explanations.html#tie-everything-back-to-telemetry) | `tie-everything-back-to-telemetry` | [Beta](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/how-to/interpret_explanations.html); add compatibility alias if retained for inbound links |

## Scientific references and access limits

- [CE classification paper](https://arxiv.org/html/2305.02305v3): construction/presentation context checked against the worked rule/scenario explanation; not proof that the newly written pedagogical prose is approved.
- [CE regression paper](https://arxiv.org/html/2308.16245v3): interval/event distinction and model-response explanation context.
- [VA primary paper](https://arxiv.org/abs/1511.00213): pair/merged validity distinction explicitly supported.
- [crepes documentation](https://crepes.readthedocs.io/en/latest/): standard/normalized/Mondrian implementations and optional difficulty-estimator context.
- [Guo et al., calibration](https://proceedings.mlr.press/v70/guo17a.html): predictive calibration background; no general CE accuracy-improvement inference.
- [EP procedure 2022/0303(COD)](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2022%2F0303%28COD%29): directly confirms proposal withdrawal on 6 October 2025.
- Detailed AI Act/DSA/PLD article corrections were traced through the source diff and existing cited legal register. EUR-Lex full-text requests encountered automated-access challenges during this comparison. That part is therefore an inherited fact-check, not a new complete legal verification or advice.

## Preservation and reporting-only branch

Reporting branch: `reports/official-vs-beta-20261117`, based on exact candidate `2bc637bc9b55febf77215783e2cbf3ab4288a520`. Only the five requested Markdown reports are added under `development/reports/official-vs-beta-20261117/`. No changes to candidate docs/src/dependencies/assets, official refs, Beta main/latest or previous candidates are authorized or made by this comparison.

The primary checkout has user-owned staged work and an unstaged CLAUDE.md change. Its staged binary-diff SHA-256 was recorded as `C9186FF498C07E76EE43D484845F91200DC43E22341953A0F454751307177527`; the end-of-task comparison checks that fingerprint and candidate/remote refs. This protects session work but is not published user-file content. Normal reporting-branch push only; no force push, deletion or RTD API credential use.

## Evidence-log hashes

Hashes identify local verification outputs without requiring reviewers to access a local temporary path. Results and reproduction methods above are the shareable evidence; immutable source and public RTD metadata provide independent traceability.

| Verification output | SHA-256 |
|---|---|
| tests.log | `053118241d8bffe8dd5ff74e0ae5b667f942365f1e1e11f808a7165718f2e7b1` |
| sphinx-final.log | `ecae2e61a4d09e31ee4406f67ab4cfd23751f87ff2ba35631c023c8f9bf2adcb` |
| live-validation.json | `5b15ebdfa078c547c918ec90097e1c58d653ddc7b2d8e0e89a53737f7191f680` |
| layout-validation.json | `7b497a6abbd5152f362894c76513a0f1f1314c4272d60ce265dad47f6ba4671a` |
| api-probe.log | `3fc58b1ac4c06d26005d82eb4405332412423a87fa1194e187ab06ea4b8c2a20` |
| supplement-metrics.json | `ab0fa9da9c00ab6eced4a681861746f066b274e31ba2e33ac82d45ce518a31cb` |

The 14 extra generated HTML pages are genindex, py-modindex, search, the viewcode module index and ten module-source views. They are not additional tutorial or API source-page additions.
