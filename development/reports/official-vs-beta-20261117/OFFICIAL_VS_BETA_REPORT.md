# Official stable versus Beta author-review documentation

Review date: 17 November 2026. This is a source comparison and rendered-site assessment for CE authors, maintainers, the internship supervisor and Product Owner. It makes no documentation changes and does not recommend official release or promotion to Beta latest.

## Findings requiring attention

1. **Version-dependent endpoint wording needs correction or an implementing reference.** The Beta {doc} source `tasks/regression.md` describes true infinite open endpoints from v1.1.0, but this candidate identifies as 1.1.0.dev0 while its interval-regressor implementation is unchanged from stable. An independent public-API probe returned the calibration minimum, 47.0, for the open lower side. The text must not imply that future behavior is implemented in this candidate. [Beta page](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/tasks/regression.html); [source](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/blob/2bc637bc9b55febf77215783e2cbf3ab4288a520/docs/tasks/regression.md).
2. **Some official deep links are no longer compatible.** All original page URLs survive, but 24 official section IDs across 15 pages are absent in Beta. This is separate from successful internal-link checks: the current site need not link to a broken incoming bookmark. Add invisible compatibility aliases in a future scoped correction; do not restore navigation inventories. The exact list is in [Change evidence](CHANGE_EVIDENCE.md).
3. **Scientific and legal questions remain open.** Exact VA pair/merged and multiclass validity, CPS endpoint conditions, composed threshold-event validity, explanation-range interpretation, ensured filters and reject guarantees require author approval. Legal examples require qualified review rather than a compliance conclusion. The [review register](SCIENTIFIC_REVIEW_REGISTER.md) records original/Beta statements and specific decisions.
4. **Two short introductory statements still overgeneralize.** The Quick Start introduction promises a range for each prediction, while the corrected What & Why page properly says prediction uncertainty is returned when requested. The regression concepts introduction says calibration is the same for both questions, although the later text explains different CPS/VA paths. Proposed narrow replacements are in the register.

These findings do not prevent explicitly experimental author/supervisor review. They do prevent treating successful builds as full scientific acceptance or claiming complete official-anchor preservation.

## 1. Executive comparison

Official stable is an audience- and task-oriented reference collection: getting started, practitioner, researcher and contributor routes lead to shared foundations, tasks, API and governance references. Existing quickstarts prioritize a short call sequence; much interpretation is left to linked theory, notebooks and source. Its strengths are established technical coverage, practical API examples, research references and specialist guides. Its limitation for a new reader is the amount of conceptual bridging required between those resources.

The Beta candidate retains the official project as its scientific foundation and retains all 120 original tracked page source paths. It adds subject-led entry points, prerequisite material, an end-to-end example, worked calibration explanations and a glossary. Existing pages are clarified rather than uniformly replaced. Final refinement removes visible levels and repeated learning-route inventories from conceptual articles, while preserving A/B/C orientation in the Quick Start hub.

The full direct comparison contains **144 tracked page sources: 24 added, 80 modified and 40 byte-identical**. Documentation pages add 6,702 lines and remove 1,144; these are source-line counts, not a measure of educational quality. The candidate also inherits narrative API/code changes, a development-version increment and the sphinx-design build dependency, which are explicitly separated from editorial work. No comparison-task code or documentation changes were made.

Expected reader benefits are less prerequisite guessing, clearer distinctions between returned quantities and a concrete model-response example connecting prediction, factual weight and alternative. These are reasoned editorial expectations based on the changed text and rendered examples. No learner study, comprehension score or comparative completion-time result was obtained.

## 2. Verified deployment and source baseline

| Item | Official stable | Beta author-review |
|---|---|---|
| Published URL | [Official stable](https://calibrated-explanations.readthedocs.io/en/stable/) | [Beta author review](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/) |
| Source commit | `609d7b728b76b7bfc1e831a9ca7986689c1b43d1` | `2bc637bc9b55febf77215783e2cbf3ab4288a520` |
| Ref | `v1.0.2`, RTD `stable` | `beta/author-review-20261117`, RTD `beta-author-review-20261117` |
| Successful RTD build | [35281189](https://app.readthedocs.org/projects/calibrated-explanations/builds/35281189/) | [35951339](https://app.readthedocs.org/projects/calibrated-explanations-beta/builds/35951339/) |
| Build completion, UTC | 2026-10-20 21:03:48 | 2026-11-17 08:57:49 |
| Source version context | 1.0.2 | 1.1.0 development candidate; not an official release |

Public RTD version/build records independently identify both exact commits. The comparison uses these two trees directly, not the current official main branch and not a sum of successive Beta diffs. Live HTML was separately retrieved: 120 official source-page URLs and 158 Beta HTML pages, including the tracked API references and generated utility/viewcode pages, returned HTTP 200. Source and deployment evidence agree on the baseline; live pages are observations at the review date, not immutable artifacts.

## 3. Architecture and navigation

| Area | Official structure/presentation | Beta structure/presentation | Change and evidence / expected benefit |
|---|---|---|---|
| Homepage | Audience/task introduction, project and release notices, compact toctrees | Quick Start plus What & Why, How CE Works, In Practice, Software & Integration, Project/Evolution and Glossary; official repository/license remain accessible | Structural regrouping and presentation change, demonstrated in `docs/index.md`; subject-first discovery is an anticipated benefit |
| Sidebar | Audience hubs plus core reference/migration/project groups | Subject hierarchy with retained practitioner/researcher/contributor routes and software/project subgroups | Structural; live sidebar contains 142 distinct source-page destinations |
| Quick Start | Installation and short task quickstarts | Non-code A/B/C orientation, same-case prerequisite/example/application route, runnable tutorials in a dedicated tutorial hub | New hubs and content; original quickstart URLs retained |
| Concepts/theory | Concepts index and short mode/semantics pages | Workflow first, expanded calibration methods, task-specific semantics and interpretation references | Both added content and editorial expansion; mathematical notation precedes derivations |
| Practical work | Task pages, practitioner playbooks, linked notebooks | Expanded printed-output tutorials, own-data workflow and evaluation guide; practical hub also links demos | Added teaching material; demos explicitly do not validate a user's deployment |
| Software/integration | API, plugin, configuration and contributor references spread across hubs | Groups foundations, integration, operations and maintenance; retains generated API references | Structural cross-linking with some corrected examples; no page URL migration |
| Resources/research | Researcher/citing/roadmap/governance pages | Project hub, alphabetical/scientific/software glossary and retained full bibliography | New lookup routes; citation hierarchy corrected without removing scientific references |

The change is broader than a purely editorial patch when measured from official stable: 24 pages and global presentation assets were added in earlier stages. The latest continuous-tutorial work is editorial within that inherited architecture. This distinction matters when assessing project scope. `STD-004` ownership remains a governance question; the Beta crosswalk explicitly marks the amendment as pending.

Useful destinations were checked against the actual sidebar. **142 of 144 tracked page sources appear as distinct sidebar targets.** The two exceptions are the intentional `getting_started_60s.html` compatibility page (which links to Quick Start) and unchanged `multiclass_all_classes_gap_analysis.html`, a technical gap-analysis page. No removed learning matrix destination needs that obsolete matrix to remain accessible. Contextual concept/example/reference links remain; scientific comparison and parameter tables have not been treated as redundant navigation.

## 4. Page-by-page coverage

[Page change inventory](PAGE_CHANGE_INVENTORY.md) contains one individually annotated row for every added or changed tracked page source, with original/Beta URLs, immutable source links, original presentation, additions/removals/reorganisation, technical differences, rationale, anticipated benefit and review owner. Forty unchanged pages have their own inventory. Small footer or sidebar-parent edits are not represented as substantive rewrites.

Representative groups include the homepage and nine subject/software hubs; the Quick Start, three expanded task tutorials and new walkthrough/own-data pages; methods/workflow/semantics and alternatives; interpretation/glossaries/evaluation; corrected normalization, reject, parameter and regulatory references; plugin registration/retrieval examples; and narrative/schema documentation. This covers inherited stages as well as the final three targeted changes.

## 5. Educational comparison with concrete examples

| Page/section | Official presentation | Demonstrated Beta change | Anticipated educational benefit and limitation |
|---|---|---|---|
| [Regression introduction](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/probabilistic_regression.html) | Says the page explains two regression modes, then gives fragments | Introduces numeric-target versus target-event questions and a complete diabetes example with target units and probability columns | Reader can identify the quantity being explained; introductory same-calibration sentence still needs qualification |
| [Regression tutorial, §4–5](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_regression.html) | Interval/threshold/factual calls appear in a short sequence | Explicitly states the prior call asks about `y <= 150`, but the next `explain_factual` omits threshold and returns target-unit weights | Prevents carrying event-probability meaning into numeric weights; independently exercised by the tutorial smoke test |
| [Classification example](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/tasks/classification.html) | Example indexes binary bounds as `low[0, 1]` | Uses `low[0]`/`high[0]`, explains binary versus multiclass shapes | Demonstrated correction of a reproducible indexing error, rather than a stylistic change |
| [Normalization, configuration](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/practitioner/advanced/normalization-guide.html) | States default CPS handles difficulty automatically | States no default estimator, shows `DifficultyEstimator` fitted on proper-training inputs and public `set_difficulty_estimator` | Makes optional configuration explicit; does not establish better conditional coverage |
| [Alternatives, worked example](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/alternatives.html) | Short call and filter list | Connects base P(benign) 0.286 with substituted prediction 0.476 and factual weight −0.190; explains lower/higher alternatives | Demonstrates how a weight relates to another model response; does not establish causality, feasibility or additive attribution |
| [What & Why, introduction](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/sections/what-and-why.html) | No standalone official subject introduction | Separates calibration from accuracy; says prediction uncertainty can be requested, and feature-weight ranges describe another quantity | More accurate first-use expectation; parallel Quick Start sentence still needs alignment |
| [ML prerequisites](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/ml-foundations.html) | No standalone introductory prerequisite overview | Features/targets, task types and proper-training/calibration/test roles use the walkthrough's classification example | Shared vocabulary reduces conceptual switching; no measured learning result; A1–A6 prefixes could be reviewed for readability |
| [Calibration methods, notation and derivations](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/calibration_methods.html) | Related facts distributed across mode guides/references | Defines symbols, API percent-versus-fraction convention, VA pair/merge and CPS residual order before connecting them to returned output | Offers traceable technical depth; conditional expectation/order-statistics prerequisites remain substantial |
| [CE by example, factual plot](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/ce-by-example.html) | No standalone non-code worked-case page | Follows one case through data roles, raw output, calibrated prediction, factual rule and alternative; plot explanation follows caption | Gives an explicit interpretation chain; biological measurements do not make the comparisons clinical advice |
| [Pipeline integration](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/how-to/integrate_with_pipelines.html) | Says fit and calibrate fit the preprocessing pipeline | Distinguishes fitting preprocessing on proper-training data from transforming calibration data | Explains a leakage-sensitive relationship, verified against the wrapper implementation |
| [Concept index/foundations](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/index.html) | Topic inventory and toctree-oriented introduction | Connected prose introduces data roles, interpretation, calibration and architecture while sidebar keeps topics | Main article explains relationships instead of repeating a navigation catalogue |

Introductions now more often identify the CE quantity before an API call. Worked output tables are followed by interpretations, common mistakes connect to assumptions and contextual transitions lead from prediction to condition/substitution/weight/alternative. This is visible editorial improvement. It is not uniform perfection: some hubs remain card collections by design, the methods page is long, some prose still uses confidence/support informally, and reviewer feedback is needed on statistical accessibility. The report does not recommend another broad rewriting cycle.

## 6. Scientific content and implementation fidelity

Classification: **P** preserved; **C** clarification; **E** educational context; **T** terminology change; **F** verified correction; **R** new or retained claim needing scientific review.

| Subject | Classification | Observed difference and verification boundary |
|---|---|---|
| Motivation and traditional XAI | P/C/E/R | Calibrated model-response questions distinguished from explaining raw scores; purpose comparison replaces unsupported general stability ranking (SR-06) |
| Training/calibration/test roles | C/E/F | Explicit separate splits and fixed fitted preprocessing; source wrapper confirms the fit-versus-transform distinction |
| Venn–Abers | P/C/E/R | Pair construction and merge are made explicit; implementation merge is inspectable; exact validity is not assigned wholesale to the merged scalar |
| Probability pair versus merged estimate | C/F/R | Corrects broad summary language; the primary VA paper distinguishes its pair property from merged output; multiclass rescaling remains SR-13 |
| Conformal predictive systems | P/C/E/R | Residual ordering, percentile units and CPS median explained; exact tie/endpoint/normalization conditions remain SR-02 |
| Interval regression | C/E/F/R | Numeric target units and median distinguished from raw model prediction; open-side version note needs implementing evidence |
| Threshold/probabilistic regression | C/E/T/R | Same prediction task, different event question; CPS/VA calibration halves and event column explained; exact composed validity SR-15 |
| Factual explanations | P/C/E/R | Condition holding for the case compared with substituted calibrated predictions; example weight linked to actual scenario result |
| Alternatives | P/C/E/T | Substituted feature ranges may strengthen, weaken or change class; not synonymous with a label flip or actionable recourse |
| Weights and ranges | C/F/R | Corrects returned base-bound metadata interpretation; avoids automatically transferring prediction guarantees to derived ranges |
| Uncertainty | C/T/R | Bounds, target intervals and weight ranges separated; epistemic/aleatoric interpretation of weights/filters remains open |
| Exchangeability | C/R | Distribution-match shorthand is not silently treated as a substitute theorem; future deployment assumptions cannot be certified by a docs build |
| Coverage/calibration guarantees | C/F/R | Distinguishes marginal from individual-case statements and model calibration from accuracy; no new feature-weight coverage proof |
| Mondrian/subgroups | P/C/F/R | Per-group calibration counts and percentile limitations replace universal 30–50 advice; no arbitrary subgroup guarantee |
| Reject/decision support | F/C/R | Correct alias and singleton-set mechanism; application probability gates are separate from reject significance and accepted-case error guarantees |

Primary literature was checked for the conceptual distinctions: [original CE classification](https://arxiv.org/html/2305.02305v3), [CE regression](https://arxiv.org/html/2308.16245v3), [VA pair and merged probabilities](https://arxiv.org/abs/1511.00213), and [crepes methods](https://crepes.readthedocs.io/en/latest/). Implementation references and exact method locations are in CHANGE_EVIDENCE. These checks establish consistency of described computations and identify review questions; they do not supply CE-author approval of every mathematical statement.

## 7. Instructional figures and following explanations

There are **19 instructional placements** in Beta: 11 image-based figures and eight Mermaid diagrams. Compared with stable, six architecture Mermaid definitions are preserved and their explanations expanded; 13 placements are new. The new physical assets comprise six SVG files (including two responsive alternate layouts) and four plot PNGs. Reusing a diagram/plot on two pages counts as two placements, not two scientific figures or two new files. The notebook repeats walkthrough visuals and is a companion download, excluded from the HTML-placement total. Decorative wave/icons are excluded.

| Source page / figure | Official → Beta status | Immediately following explanation and CE interpretation | Display/accessibility / verification status |
|---|---|---|---|
| [Quick Start](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/index.html), CE at a glance | New placement / new responsive SVG | Arrows from labelled data through training/prediction; held-out calibration branch and explain outputs; distinct range meanings | Descriptive alt and narrow variant; source/live elements match; universal-range summary still flagged |
| [Why CE](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/why-ce.html), ML/CE workflow | New responsive SVG | Training, calibration and test roles; model remains fitted; added CE stages use held-out data | Alt describes roles; narrow variant; schematic is not an execution trace |
| [Why CE](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/why-ce.html), reading an output | New SVG placement | Base probability/range, factual condition/weight and alternative prediction linked in the same case | Text covers labels and values independently of color; interpretation SR-14 remains open |
| [CE workflow](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/ce_workflow.html), workflow | New placement, reuses ML/CE-workflow SVG | Fit/calibrate/predict/explain roles and separate output branches; not every call returns every object | Responsive asset and following prose; source/call sequence checked |
| [Interval semantics](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/calibrated_interval_semantics.html), output types | New SVG | Classification probability, numeric target interval and threshold-event probability; units and true outcome distinguished | Meaningful alternative text; diagram contrasts quantities, not equal guarantees |
| [Interpretation guide](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/how-to/interpret_explanations.html), reading an output | New placement, shared SVG | Reads base prediction, factual weight/range, substituted output; warns against adding weights or causal interpretation | Following prose plus data-record discussion; SR-08/SR-14 retained |
| [Own-data tutorial](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/apply-to-your-data.html), factual case 3 | New PNG | Upper probability scale/estimate and lower feature-weight ranges; zero line, conditions and measured feature values | Descriptive alt; explanatory prose identifies sign/zero crossing without relying only on color; live image loads |
| [CE by example](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/ce-by-example.html), factual case 2 | New placement, shared walkthrough PNG | Separate probability/weight axes, vertical estimates, negative first rule, zero-crossing later ranges and right-side measured values | Explicit full-size link after prose; live desktop/mobile light/dark checks; plot labels remain small inline on phones |
| [Classification tutorial](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_classification.html), Iris factual case 1 | New PNG | Class-specific probability, upper range, lower weight ranges, zero crossing and feature conditions | Following interpretation; multiclass range/rescaling review SR-13 remains visible |
| [Guarded tutorial](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_guarded.html), factual case 0 | New PNG | Probability versus weights, negative versus zero-crossing ranges; guard filtering is distinct from displayed uncertainty | Alt and immediate prose; no whole-range or clinical guarantee inferred |
| [Python walkthrough](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_walkthrough.html), factual case 2 | New PNG | Upper benign/malignant probability information, first negative weight, other ranges and non-additivity | Native image access plus following prose; independently viewed PNG content; supports SR-14 review |
| [ML essentials](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/ml-foundations.html), data split | New Mermaid | Labelled data divide into proper-training/calibration/test roles; separate fitting, calibrating and evaluation | Text explains arrows and roles; live SVG render sampled; no theorem inferred from split schematic |
| [Python walkthrough](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/get-started/quickstart_walkthrough.html), VA pair/merge | New Mermaid | Two hypothetical labels lead to two fitted calibrators/bounds then a merged scalar; unknown true label distinguishes pair from merge | Following prose and numerical example; source matches VA implementation; validity question SR-03 retained |
| [Architecture](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/architecture.html#public-lifecycle), lifecycle | Mermaid preserved; prose added | Learner/data arrows enter wrapper; fit and calibrate precede selectable prediction/explanation branches | Definition unchanged; following explanation avoids saying every branch runs |
| [Architecture](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/architecture.html#core-runtime-ownership), runtime ownership | Mermaid preserved; prose added | Wrapper/shared runtime/PluginManager/orchestrators; dashed references mean shared state | Matched to source responsibilities; diagram is ownership, not request order |
| [Architecture](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/architecture.html#ordinary-inference), inference | Mermaid preserved; prose added | Solid API-to-output paths and dashed shared state; explains prediction data versus explanation objects | Rendered Mermaid checked; reject path is separate |
| [Architecture](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/architecture.html#reject-policy-execution), rejection | Mermaid preserved; prose added | Full-batch decision chain versus payload-source-row branch; policy shapes payload | Distinguishes result shape from statistical guarantee; SR-16 open |
| [Architecture](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/architecture.html#plugin-and-configuration-resolution), configuration | Mermaid preserved; prose added | Settings enter ConfigManager, registry supplies implementations, trust policy constrains resolution | Following prose explains dependency arrows; not another learner pipeline |
| [Architecture](https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/foundations/concepts/architecture.html#optional-and-downstream-capabilities), downstream | Mermaid preserved; prose added | Explanation objects feed plotting/export/narratives and optional downstream adapters | Distinguishes consumers from core calibration; maintainer review appropriate |

All 11 image figure blocks had a paragraph immediately after the figure/caption in fetched HTML. Mermaid explanations follow their directive output in source and are integrated with section-specific responsibilities. Alt text complements the paragraphs; mathematical or model-response validity is not inferred merely because an SVG renders. Layout checks covered all six preserved architecture diagrams and the new VA diagram on the sampled pages. The ML split diagram's prior rendering check is inherited; its source structure and current HTML were independently inspected.

## 8. Learning-framework removal and retained navigation

Chronology matters: official stable already had audience-tier footers and topic inventories. Intermediate Beta stages added more explicit learning-depth matrices and reading routes. The final candidate removes those intermediate matrices, L1/L2/L3 instructions, reading-depth explanations, repeated conceptual-page route inventories and public tier footers. Direct stable→Beta metrics therefore do not count removal of every intermediate matrix: some never existed in stable.

For example, the final workflow article teaches prediction→condition→substitution→weight→alternative rather than showing a ten-concept three-level matrix; What & Why uses subject headings rather than a reading-order inventory; the concepts hub and maintenance tier-map no longer display their old inventories. Compatibility span IDs preserve several intermediate headings even when headings change. A/B/C cards remain on the Quick Start hub as authorized orientation, not repeated instructions on conceptual pages.

The final live-article scan found no `Entry-point tier`, `Level 1/2/3`, `L1/L2/L3`, learning-depth or reading-depth markers. This is a bounded pattern check, not proof of the absence of every possible navigation sentence. Main subject hubs still contain cards and contextual links. Genuine mode/parameter/method comparison tables, data-role/output examples, references and mathematical notation remain. Do not reinstate removed matrices to solve the old-anchor compatibility gap; invisible aliases suffice.

## 9. Code examples and technical behavior

The direct source comparison identifies 57 modified, 40 added and seven removed Python example blocks under the defined sequence-alignment metric. This is not 104 independently executable programs: fragments share state, outputs are separate blocks and notebook code is excluded. Tests execute representative whole-page lifecycles and reproduce identified API boundary cases.

Verified corrections include binary bounds indexed as one-dimensional arrays; public explanation collection indexing rather than nonexistent nested factual/alternative objects; `reject_confidence` replacing removed `confidence`; classification threshold misuse explicitly raising; optional difficulty estimation and public attachment; plugin metadata containing `data_modalities`; application payload/rule methods replacing stale examples; and training-only preprocessing fit. Some plugin snippets are explicitly scaffolds rather than complete runnable plugins.

The final regression transition is a prose correction: omitting threshold in that call returns numeric-target explanation weights. A preceding threshold prediction does not turn that later default call into event-probability weights. The corresponding integration test verifies the distinction. Corrected What & Why uncertainty wording and full-size plot access are likewise presentation changes, not statistical-method changes. Mobile version-selector integration is Beta-project-specific CSS/JS/template behavior.

Reproducibility limits remain: printed values depend on dataset/model/library versions, seeded examples are not independent statistical validation, snippets may assume a calibrated wrapper, and linked GitHub `main` notebooks can evolve. Original research notebooks are not silently rerun in new environments here. The packaged walkthrough notebook/generator and figure-build scripts are accounted for as assets/tooling.

## 10. Quantitative extent

| Metric | Direct tree comparison result |
|---|---|
| Tracked documentation page sources | 120 official → 144 Beta |
| Added / modified / removed / unchanged | 24 / 80 / 0 / 40 |
| Changed heading/preamble slots | 586; includes added/deleted/renamed headings and changed section bodies, not 586 scientific claims |
| Python blocks modified / added / removed | 57 / 40 / 7; sequence-aligned per page |
| Documentation hyperlink/reference occurrences added / removed | 567 / 43; lexical occurrence metric, excluding image src and Markdown image syntax |
| Instructional figure placements | 6 official → 19 Beta; 13 new placements, six preserved definitions with expanded explanation |
| New physical instructional image files | 10: six SVGs including narrow variants, four PNGs |
| Documentation page lines + / − | 6,702 / 1,144 |
| Docs pages + assets/templates + build configuration | 122 changed path records; 9,422 text lines added / 1,144 removed; four binary files |
| Entire repository, no rename detection | 306 path records; 27,321 text lines added / 1,274 removed |
| Entire repository, rename-aware Git presentation | 305 entries; 27,224 insertions / 1,177 deletions; one unchanged 97-line plan move explains the difference |

The category table, definitions, limitations and reproduction commands are in [Change evidence](CHANGE_EVIDENCE.md). Reports account for much of total repository growth and are not public documentation page additions. No branch-stage counts are summed.

## 11. Validation and preservation

Independent comparison checks: exact RTD commits/builds re-read; direct Git tree analysis; 278 successful live page requests; no broken current Beta internal HTML targets among 2,352 unique page/fragment or asset destinations; 142 sidebar page destinations; 24 missing official section anchors explicitly recorded; six sampled primary/reference external URLs returned HTTP 200; fresh strict Sphinx build passed after repairing an incomplete temporary snapshot; **381 tests passed, one wheel-install test deselected**; **48 live layout/theme cases** had no document overflow, unloaded sampled images or MathJax error elements. The API probe confirmed binary/event bound shapes, no default difficulty estimator and finite open-side placeholder behavior.

Inherited evidence is identified separately: the original published RTD Sphinx command succeeded without warnings; prior publication included 100 live layout/theme cases and ten selector/full-size-image interactions, preservation checks relative to the immediate parent, and 19-visual review. Prior local standard-theme and wider 320/768px selector checks are not represented as rerun here. Mypy remains unavailable. No new RTD build/version was created for this comparison.

The official repository/documentation, Beta main/latest and all published candidate commits were left untouched. The only deliverable changes are five report files on a separate reporting branch. Build-generated files were written to a temporary source/output snapshot, not candidate documentation. A temporary-snapshot include failure was diagnosed, disclosed and corrected; it was not a candidate defect and is not hidden in the final successful build result.

## 12. Assessment and review recommendation

| Objective | Evidence-backed assessment | Remaining limitation |
|---|---|---|
| Scientific fidelity | Original CE methods, implementation and references anchor the explanation; qualifications are more explicit | Exact validity and uncertainty interpretations still require authors; legal sufficiency is unapproved |
| Tutorial coherence | Shared worked case and prediction-to-explanation chain connect previously dispersed topics | Human reading review needed; some long methods material and short summary contradictions remain |
| Conceptual clarity | Output units, probability/interval/weight distinctions and calibration-versus-accuracy are explicit | Informal confidence/support terms and future-version behavior need targeted review |
| Practical usefulness | Expanded runnable outputs, API corrections and own-data/evaluation routes; fresh tests pass | Not all fragments/notebooks are independent tested programs; wheel-install check excluded |
| Navigation simplicity | Subject sidebar, preserved audience routes, no visible learning-level framework in scan | Two deliberate/specialist sidebar exceptions and 24 lost old section anchors |
| Figure interpretation | Every image figure has immediate explanatory prose; architecture diagrams explain their different relationships | Inline plots remain small on phones; full-size access mitigates this rather than making every label large |
| Technical accuracy | Corrected shapes/defaults/aliases/public object usage supported by source and tests | One-sided future-version note needs implementing evidence; mypy unavailable |
| Maintainability | Reuses existing URLs, figures and sidebar; tests/generators cover key examples | Added source volume, custom CSS/version-picker integration and inherited narrative code need ownership |

**Recommendation: ready for CE-author and internship-supervisor review as an explicitly experimental Beta candidate.** Ask authors first about the P1 register, then ask the supervisor to read Why CE → CE by example → workflow and one task tutorial for conceptual continuity. Request concrete confusing sentences, misleading mathematical interpretations and example-to-theory gaps. Keep the candidate stable while collecting feedback. Resolve the endpoint note, incoming-anchor aliases and identified summary inconsistencies through targeted future corrections; do not begin another redesign or promote to official/latest based on this report.

Related deliverables: [Executive summary](EXECUTIVE_SUMMARY.md), [page inventory](PAGE_CHANGE_INVENTORY.md), [scientific register](SCIENTIFIC_REVIEW_REGISTER.md), [evidence and methodology](CHANGE_EVIDENCE.md).
