# RTD-anchored corrections and instructional figure review

Date: 16 November 2026. Scope: the approved Stage 1 corrections and the
subsequently explicit section 11A figure requirement. Broader tutorial
expansions remain proposals for Product Owner approval.

## Candidate and publication

- Baseline: `beta/source-faithful-refinement-20261116`,
  `dcf34907338c890a26986df226630939b7bf3818`.
- New isolated branch: `beta/rtd-tutorial-corrections-20261116`.
- Implementation commit: `9d08d9b65749e05f22879c83e050fbdc94ae9fd3`.
  The branch also contains this report in a subsequent commit.
- [Experimental GitHub branch](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/tree/beta/rtd-tutorial-corrections-20261116).
- RTD: not activated, built, or published for this branch. There is no new
  deployed commit or build ID to report. The current brief, section 14,
  requires explicit publication authorization after validation.
  After the normal GitHub push, the public RTD version endpoint returned
  HTTP 200 with `active=false`, `built=false`, and identifier
  `beta/rtd-tutorial-corrections-20261116`. The version is registered but
  remains inactive and unbuilt.
- Reserved preview address, **not a verified publication**:
  https://calibrated-explanations-beta.readthedocs.io/en/beta-rtd-tutorial-corrections-20261116/
- Official CE, experimental main/latest, and earlier candidate branches were
  not changed or promoted.

## Technical corrections and rationale

| Issue | Page and change | Verification |
|---|---|---|
| A1: obsolete call-time confidence | `practitioner/advanced/reject-policy.md`: four occurrences now use `reject_confidence=0.95`. `GuardedOptions.confidence` is unchanged. | Public wrapper keyword validation and executed default, override and ensured fragments; confidence metadata and result shapes checked. |
| A1: additional experimental incompatibility | The difficulty-normalized example also passed unsupported `strategy=`. It is now explicitly identified as a negative example raising `ConfigurationError`, rather than a runnable recipe. Unsupported metadata-print lines were removed. | Wrapper allowlist in `core/calibrated_explainer.py` and `core/wrap_explainer.py`; an execution test confirms rejection of `strategy`. No default strategy was silently substituted. |
| A2: individual-probability interpretation | `get-started/apply-to-your-data.md`: identifies the merged estimate and two Venn–Abers values, removes the individual true-probability containment claim, and links canonical semantics. | `calibration/venn_abers.py`, existing semantics and pair/merge scientific qualifications. Numeric outputs unchanged. |
| A3: target interval versus event bounds | `foundations/how-to/interpret_explanations.md`: restricts the CPS target-interval description to interval regression without a threshold. | Prediction routing and regression examples; the separate threshold-event interpretation is retained. |
| A4: task/mode qualifications | `get-started/ce-tasks-and-modes.md`: distinguishes the pair from its merged estimate and describes exchangeability with the method-specific protocol. | Existing canonical semantics and unchanged source implementation. No new theorem or unconditional frequency guarantee. |
| Agent-guide overclaims | `get-started/ce_first_agent_guide.md`: replaces unsupported actionability/hallucination-reduction assertions with inspectable API operations and limits; corrects `explorer` to `explainer` in the checklist. | Public API lifecycle; causal and agent-text correctness are not inferred from CE use. |
| Learning labels | `appendices/rtd_tier_map.md`: distinguishes audience tiers, L1/L2/L3 depth and A/B/C reader goals. | Existing STD-004 and navigation labels preserved. |

Representative before/after:

- Before: the calibration data support a probability anywhere between the
  reported endpoints. After: the endpoints and merged estimate have different
  qualifications; they are not a conventional confidence interval containing
  one case's unknown true probability.
- Before: all regression `prediction_interval` values were described as target
  conformal intervals. After: that description explicitly applies without a
  threshold; thresholded output concerns an event probability.
- Before: the agent workflow was said to reduce hallucinations and ensure
  auditable behavior. After: the concrete operations are inspectable, without
  guaranteeing surrounding agent prose or causal actionability.

## Figure-by-figure review

The rendered documentation contains **19 instructional instances on 12 pages**:
six SVG illustrations, five plot instances and eight Mermaid diagrams.
The downloadable notebook additionally repeats the walkthrough diagram and
plot. Responsive narrow SVGs express the same labelled workflows and were
reviewed alongside their desktop counterparts.

Every rendered instructional figure is followed immediately by explanatory
text. Existing useful plot-reading material was retained and supplemented.
All original assets, figure captions, alternative text and diagram definitions
are preserved. Explanations identify labels, positions and signs as well as
colors. Verification below means correspondence to the visual and documented
implementation, **not acceptance of unresolved statistical guarantees**.

Evidence keys:

- **W:** actual desktop/narrow workflow SVG labels and arrows; public wrapper
  lifecycle; original RTD training/calibration/prediction workflow.
- **P:** actual PNG inspection; executed example source and stored output;
  `plotting.py`, `viz/plotspec.py`, `viz/matplotlib_adapter.py`, and CE
  classification paper section 4.1.2. Probability and weight axes are distinct.
- **V:** actual SVG or Mermaid labels; `calibration/venn_abers.py` and the
  Venn–Abers reference. Pair/merge qualifications remain open as SR-03.
- **R:** existing regression tutorial values, source prediction routing and CE
  regression paper. CPS coverage and threshold-event validity remain SR-02/SR-15.
- **A:** candidate `core/wrap_explainer.py`, `core/calibrated_explainer.py`,
  `core/plugin_manager.py`, `core/config_manager.py`, the prediction/explanation/
  reject orchestrators, and visualization/serialization contracts.
- **G:** actual guarded plot and candidate guarded implementation; the guard's
  mixed rule does not certify every value in a retained feature interval.

| Page | Figure | Explanatory text added or revised immediately afterward | Verification status |
|---|---|---|---|
| `get-started/index.md` | CE at a glance; desktop/narrow | Follows conventional arrows, calibration branch, Calibrate/Explain and the two outputs; distinguishes the ranges' meanings. | Verified W; responsive image rendered. |
| `get-started/why-ce.md` | CE in the ML workflow; desktop/narrow | Explains training, calibration and test inputs; reads the two output boxes before the retained numbered workflow. | Verified W. |
| `get-started/why-ce.md` | Reading a CE output, panels 1–3 | Explains probability/weight/probability scale changes, 0.5 versus zero, the alternative range crossing 0.5 and model-response limits. | Verified V/P; formal range qualifications retained. |
| `get-started/ml-foundations.md` | Three-way data split Mermaid | Explains the three branches as separate data roles, where the model and calibration data meet, and what test cases supply. | Verified W; diagram rendered. Concise prerequisite role preserved. |
| `get-started/ce-by-example.md` | Factual plot for case 2 | Adds upper/lower axis interpretation, zero crossings, actual feature values, nonadditivity and transition to alternative probability outputs. | Verified P; generator source synchronized. |
| `get-started/apply-to-your-data.md` | Factual plot for case 3 | Retains bar-style explanation; identifies benign/malignant, four wholly positive ranges versus two crossing zero, right-axis values and grey reference band. | Verified P; no individual-probability or causal guarantee. |
| `get-started/quickstart_classification.md` | Iris factual plot, case 1 | Identifies versicolor and its complement, sepal versus petal ranges, centimeter measurements and grey band; preserves default multiclass caveat. | Verified P; multiclass interpretation remains qualified by SR-13. |
| `get-started/quickstart_guarded.md` | Guarded factual plot, case 0 | Retains bounded-rule explanation; adds probability labels, weight zero, mean-concave-points range versus five crossing ranges, observed values, reference band and audit transition. | Verified P/G; no whole-interval or causal certification. |
| `get-started/quickstart_walkthrough.md` | Two-label Venn–Abers Mermaid | Explains hypothetical labels, curve readouts and merge; distinguishes calibration fits from retraining the predictive model and links to qualifications. | Verified V; diagram rendered; generator/notebook synchronized. |
| `get-started/quickstart_walkthrough.md` | Factual plot for case 2 | Retains detailed panel/bar/grey-band/right-axis reading guide; adds sign-first interpretation, crossing-zero caution and transition to alternatives. | Verified P; no formal weight coverage asserted. |
| `foundations/concepts/ce_workflow.md` | ML workflow; desktop/narrow | Adds data-to-step arrow reading and separates prediction from rule/weight outputs and their statistical meanings. Retains numbered lifecycle. | Verified W. |
| `foundations/concepts/calibrated_interval_semantics.md` | Three output types, panels A/B/C | Contrasts probability and target-unit axes; identifies estimate/observation markers, target interval and threshold event. One enclosed observation does not prove coverage. | Verified V/R; SR-02/SR-03/SR-15 remain open. |
| `foundations/how-to/interpret_explanations.md` | Reading a CE output, panels 1–3 | Explains each scale, rule sign and alternative crossing; connects panel values to the Python collections below. | Verified V/P; model response distinguished from intervention. |
| `foundations/concepts/architecture.md` | Public lifecycle Mermaid | Distinguishes incoming learner/data arrows and outgoing method choices from a mandatory execution chain. | Verified A; rendered. |
| Same page | Core runtime ownership Mermaid | Explains solid delegation arrows, dashed shared-state references and why all orchestrators need not execute. | Verified A; rendered. |
| Same page | Ordinary inference Mermaid | Follows API-to-output chains and the explanation-to-prediction evaluation link, without implying a second public prediction request. | Verified A; rendered. |
| Same page | Reject-policy execution Mermaid | Traces original-batch decision, policy-selected payload rows, optional branches, strict result and compatibility conversion. | Verified A, especially reject orchestrator source-index handling; rendered. |
| Same page | Plugin/configuration resolution Mermaid | Separates settings, registry/trust inputs, selection outputs and subsequent execution; transitions to existing precedence list. | Verified A; rendered. |
| Same page | Optional/downstream capabilities Mermaid | Explains dashed performance/observation branches and independent JSON/plot paths through PlotSpec and renderer. | Verified A; rendered. |
| `_static/notebooks/quickstart_walkthrough.ipynb` | Packaged Venn–Abers diagram | Mirrors the new walkthrough explanation. | Markdown synchronized; original computational cells/outputs/metadata unchanged. Notebook frontend rendering not rerun. |
| Same notebook | Packaged factual plot | Retains detailed reading guide and mirrors the new sign/limits/transition paragraph. | Existing output inspected; computation/output unchanged; no environment changes. |

Excluded from the instructional count: navigation icons, GitHub marks,
decorative wave/background artwork, the agent-guide pseudocode string
`"<svg>..."`, and figures in externally linked papers or repositories.
External references were consulted as evidence, not edited.

No new numerical values were invented. Existing infographic wording about
probability validity and nominal CPS coverage must still be checked by CE
authors alongside SR-02/SR-03/SR-15; the new prose explicitly refers readers
to the qualified semantics. These are review questions, not resolved theorems.

Before/after figure examples:

- CE by example previously followed the caption only with a link to another
  guide. It now explains the axes, first negative rule, crossing ranges,
  measured values and what the next alternative section changes.
- The output-types figure previously led directly into source links. It now
  explains why a target interval in B cannot be compared numerically with
  probability bounds in A/C and why one enclosed observation proves no coverage.
- The architecture reject figure previously led into separate decision/payload
  sections. Its new paragraph first traces the actual arrows and explains the
  original-batch versus selected-payload distinction.

## Original-source traceability

Primary foundation:

- [Original CE stable interpretation guide](https://calibrated-explanations.readthedocs.io/en/stable/foundations/how-to/interpret_explanations.html)
  and [classification tutorial](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_classification.html).
- [Original guarded tutorial](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_guarded.html)
  and [regression tutorial](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_regression.html).
- [Original architecture page](https://calibrated-explanations.readthedocs.io/en/stable/foundations/concepts/architecture.html).
  The retrieved page describes an older architecture; current candidate runtime
  details were checked against the pinned implementation, not inferred from
  that older diagram.
- [Pinned candidate implementation](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/tree/dcf34907338c890a26986df226630939b7bf3818/src/calibrated_explanations).
  No source files differ from that baseline.

Scientific references:

- [CE classification paper, sections 3–4](https://arxiv.org/html/2305.02305v3):
  rule/substitution/weight construction and factual plots.
- [CE regression paper, sections 3 and 4.1](https://arxiv.org/html/2308.16245v3):
  CPS target outputs, event queries and explanation quantities.
- [Vovk, Petej and Fedorova, 2015](https://arxiv.org/abs/1511.00213):
  the distinction between Venn–Abers validity and merged probabilities.

Candidate-specific infographic numbers come from the preserved executable
walkthrough and regression tutorial. The original RTD provides the conceptual
foundation; it is not claimed to contain these newly authored candidate assets.
Successful execution and rendering do not establish statistical validity.

## Focused tutorial assessment and next proposals

The section 11A changes above were explicitly approved and implemented.
The previous educational assessment remains the starting point; this is a
targeted follow-up, not a replacement documentation-wide assessment.

| Existing page/section | Comprehension result and disposition |
|---|---|
| Quick Start index, Where CE fits | Arrow roles and range distinctions now explained; three paths preserved. |
| Why CE, workflow and one example | New figure paragraphs bridge the retained motivation, lifecycle and four ideas. No new tutorial needed. |
| ML Foundations, data roles | One diagram-reading paragraph added for 11A; prerequisite overview retained. |
| CE by example, sections 5–6 | Figure is now interpretable locally; existing numerical weight-to-alternative bridge retained. |
| Tasks and modes, output table and assumptions | Stage 1 removes pair/merge ambiguity and broad assumption wording. |
| Apply overview, steps 1–7 | Purpose, inputs, outputs and checks already explicit; retain without expansion. |
| Apply to your data, predictions and plot | Stage 1 and figure text address the identified interpretation gaps; examples retained. |
| Classification tutorial, factual plot | Actual multiclass plot now explained; existing experimental option caveat retained. |
| Regression tutorial, sections 4–6 | A remaining transition can obscure the switch from event probability back to target-value factual weights. See P1 below. No change implemented. |
| Guarded tutorial, explanation and audit | Figure-to-audit transition now explicit; existing guard limitations retained. |
| Python walkthrough, calibration and factual plot | Diagram and plot now have local explanations; running example, code and outputs preserved. |
| CE workflow, explanation construction | Existing step-by-step substitution/weight/alternative chain retained; figure has a local reading bridge. |
| Interpretation guide, introduction and collections | Stage 1 distinguishes target/event quantities; panel-reading paragraph connects to collections. |
| Canonical semantics, output types | New paragraph distinguishes quantities; pending author qualifications remain visible. |
| Calibration methods, Venn–Abers/CPS derivations | Existing mathematical depth and notation retained; formulas rendered successfully. No broad rewrite proposed. |
| Architecture, six views | Each diagram now has an immediate reading paragraph; software-contract format retained. |
| Agent guide and tier map | Associated Stage 1 consistency corrections completed; no navigation redesign. |
| Seven homepage entries and L1/L2/L3 routes | Homepage and headings/anchors preserved; existing entry structure retained. |

Proposed follow-up, **not implemented**:

| Proposal | Exact location and existing gap | Original source | Smallest change and benefit | Verification needed |
|---|---|---|---|---|
| P1 | `get-started/quickstart_regression.md`, between sections 4 and 5: section 4 passes a threshold, while section 5 explains without one. A newcomer could assume the event query persists. | Original regression tutorial; candidate public explanation routing; existing target-unit weight table. | Two sentences identifying the per-call threshold and the return to target units. Helps readers interpret the existing +128.2 weight correctly without adding an example or page. | Execute both existing calls and confirm task/output quantity and source routing; CE-author confirmation if stronger interpretation is proposed. |
| P2 | `practitioner/advanced/reject-policy.md`, difficulty-normalized example: the public wrapper does not expose the documented strategy selector. | Candidate wrapper allowlist and internal reject orchestrator. | Maintainer decision on whether to retain the explicit limitation, remove the negative example, or authorize a separate API task. No unsupported runnable replacement. | Public API owner decision; any software change needs separate scope and tests. |

P1 needs Product Owner approval before implementation under section 12 of the
brief. P2 is an API-owner question, not authorization to change source code.
Already clear pages should remain unchanged.

## Validation evidence

All checks used the existing Python 3.13 environment; no dependency or notebook
environment was installed or upgraded.

| Check | Result |
|---|---|
| Four documented reject fragments | 4 passed; default, override and ensured return shapes/confidence metadata checked; difficulty fragment raises the explicitly documented unsupported-keyword error. |
| `pytest tests/docs tests/integration/test_doc_examples_smoke.py -k 'not wheel_install'` with `PYTHONPATH=src`, `MPLBACKEND=Agg`, `-o addopts='' -ra --tb=short --show-capture=no -p no:cacheprovider` | **381 passed, 1 deselected**. Wheel-install test excluded to avoid constructing/installing a separate environment. |
| Strict Beta Sphinx: `CE_DOCS_BETA=true python -B -m sphinx -W --keep-going -E -b html docs <beta-output>` | Passed; no warnings promoted to errors. |
| Same strict standard build without `CE_DOCS_BETA` | Passed. |
| `python -B scripts/docs/check_internal_links.py <output>`, both builds | Each: **158 pages, 0 broken links**. |
| Chromium layout/asset/diagram checks | **80 cases passed**: 20 relevant pages × 1365/390px × light/dark. No document overflow, missing figure images, Mermaid parse/render failures, or MathJax error nodes. All eight diagrams rendered in each layout/theme combination (32 diagram checks). |
| Mathematics | Methods-page formulas rendered in all four layout/theme combinations; no MathJax error nodes. |
| Figure adjacency | Rendered figure elements are followed by explanatory paragraphs. Mermaid explanations appear immediately below their rendered diagrams. |
| Manual visual inspection | Original four distinct PNGs inspected; representative workflow, guarded plot, output-types and architecture screenshots inspected. Mobile prose and responsive workflow figures are readable; dense plot labels/architecture diagrams still benefit from zoom/full-size viewing. Assets preserved as requested. |
| Preservation against `dcf34907` | All 19 figure/diagram blocks, captions, alternative text, Markdown headings and explicit anchors unchanged; SVG content unchanged (Windows text line endings normalized), PNG bytes identical. |
| Notebook preservation | Only Markdown cells 13 and 25 changed. Code, image output, execution counts and environment metadata unchanged. Full notebook execution was not repeated for prose-only changes. |
| Generator synchronization | Both walkthrough explanations and code-free companion paragraph updated in generator source as well as generated pages; notebook prose synchronized. |
| Source/configuration/navigation preservation | No changes to `src/`, dependencies, `docs/conf.py`, homepage, figures or prior author-review register. No new public pages. |
| `python -B scripts/local_checks.py --profile quick` | Could not complete: **mypy not found**. Ruff is also unavailable. No unrelated installation attempted. |
| `git diff --check` | Passed. |
| User-owned staged changes | Main-checkout index fingerprint remained `C9186FF498C07E76EE43D484845F91200DC43E22341953A0F454751307177527`; work performed in the new worktree. |
| GitHub publication | Normal push succeeded; remote branch HEAD matched local HEAD. Protected main, enhancement and source-faithful candidate refs retained their baseline commits. |

Local raw evidence and screenshots:
`C:/Users/ashra/AppData/Local/Temp/ce-rtd-corr-20261116/verification/`.
Build HTML is in the sibling `beta/` and `standard/` directories.
Evidence includes test/build logs, `layout.json`, screenshots and
`preservation.txt`. These are local temporary artifacts, not published pages.

Reviewable implementation commits:

1. `06bb4058`: A1 confidence and unsupported strategy, with example tests.
2. `4a95e317`: A2 individual-probability wording.
3. `a568c181`: A3 target/event distinction.
4. `6340f8bc`: A4 outputs and assumptions.
5. `baa53806`: associated agent/tier consistency.
6. `1d6f21e9`: architecture figure explanations.
7. `9d08d9b6`: remaining instructional figures and generator/notebook prose.

## Remaining author decisions and recommendation

The existing [author-review register](../docs-focused-20261116/author-review.md)
is preserved. In particular, this work does not resolve:

- SR-01: exchangeability/protocol versus distribution-match wording.
- SR-02: exact CPS finite-sample coverage, ties, endpoints and subgroups.
- SR-03/SR-13: Venn–Abers pair/merge and default multiclass-bound interpretation.
- SR-07/SR-09/SR-14: ensured filtering and averaged explanation-weight ranges.
- SR-15: the implemented CPS-score/Venn–Abers threshold-event construction.
- SR-16: reject confidence/rate and validity claims; correcting keywords does
  not settle these claims.
- Existing regulatory/legal questions; no new legal conclusions were introduced.

Recommend a focused educational review of the new figure explanations and the
P1 regression transition, followed by CE-author scientific acceptance of the
open qualifications. The candidate is locally validated for that review.
It has not been approved or promoted to Beta latest. Publication and any
substantial follow-up remain pending the explicit decisions described above.
