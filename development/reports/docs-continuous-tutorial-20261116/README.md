# Continuous tutorial presentation: focused plan and evidence

## Scope and baseline

The latest Product Owner direction supersedes the earlier requirement to
display L1/L2/L3 guidance. Existing Quick Start routes remain in navigation;
concept pages should teach their subjects without repeated route descriptions.

The isolated branch is `beta/sidebar-learning-paths-20261116`, based on
`812c06aed15261cfbaf4e91308f47450246dc9ce`. This carries forward the four
verified acceptance corrections and all figure explanations from the
source-faithful candidate lineage rooted at `dcf34907`. No previous candidate
or official branch is edited.

## Inventory and approved presentation changes

| Area | Existing problem | Focused change |
|---|---|---|
| CE workflow | Ten-row concept/depth matrix repeats sidebar; replacement depth legend also conflicts with the latest instruction. | Remove the matrix and visible levels; retain relevant prerequisite/example links and relocate scientific citations and source references alongside the concepts. |
| What & Why overview | Seven-row question/reading/deeper table and repeated topic cards frame the subject as navigation. | Use connected paragraphs explaining prediction, calibration, CE and interpretation; retain contextual examples and regulatory qualification. |
| How CE Works overview | Numbered depth route and repeated level badges/cards. | Explain the task-to-method-to-output chain in prose, retaining links to the worked construction and formal assumptions. |
| Concepts hub | Twelve-row link inventory repeats sidebar. | Use a short subject introduction; retain the existing toctree for sidebar navigation while hiding its repeated body list. |
| What CE Is and Python walkthrough | Large next-step tables repeat topic routes. | Replace with a few contextual links associated with the example and its interpretation. |
| Introductory CE pages | Repeated Path A/B/C and step labels interrupt otherwise useful explanations. | Remove route labels from concept prose; retain the Quick Start navigation routes and relevant prerequisite links. |
| Methods page | Learning-objective list and how-to-read instructions interrupt the scientific introduction. | Lead into the subject and prerequisites directly; retain the distinction between theorem, implementation, example and unresolved review. |
| Public tier footers and tier-map appendix | Reader-facing audience metadata and a large page/tier inventory add framework presentation. | Remove visible tier footers; retain the appendix URL and legacy title anchor with concise documentation-maintenance context. Governance source standards remain unchanged. |
| Generated content | The walkthrough generator could reintroduce removed framework wording or navigation tables. | Synchronize generator, existing pages and notebook Markdown without changing computational cells, output images or environment metadata. |

Scientific explanations, numerical examples, code, figures, captions,
mathematical definitions and open CE-author questions remain the foundation.
This pass does not introduce a new method or resolve an open guarantee.

## Validation plan

Before removal, check all useful table destinations against the rendered
sidebar and retain any necessary contextual links. Preserve scientific
citations and implementation/test URLs. After editing, compare page sets,
anchors, figures, mathematical blocks, code and notebook computations to the
baseline; run documentation tests, strict Beta and standard Sphinx builds,
internal-link checks and desktop/mobile checks in both themes.

Keep temporary build and browser evidence outside the worktree. Use normal
commits/pushes only to the new experimental branch. RTD activation/publication
continues to require the explicit authorization specified in the current
publication brief.

## Implementation outcome

Mode: documentation presentation refinement. The plan above was implemented
under the explicit removal and tutorial-presentation instructions.

- Removed visible tier footers from **58 pages**. Of the modified public
  Markdown pages, **45 contain only footer removal** and **15 contain prose
  or presentation changes**. The [page inventory](pages.md) lists each one.
- Removed five large navigation tables: the workflow depth matrix, What & Why
  reading table, concepts inventory, What CE Is next-step table, and
  walkthrough next-step table. The public tier-map inventory was also removed;
  its URL and original title anchor remain available.
- Removed learning-level prose and badges from the theory overview and
  workflow, repeated route labels from introductory pages, and the methods
  page's learning-objective/how-to-read framing.
- Replaced the repeated topic cards on the What & Why and How CE Works
  overviews with paragraphs about the CE subject. Homepage entry points,
  resource destinations, sidebar groups and Quick Start navigation remain.
- Replaced repeated Continue/Next/Go deeper inventories on the affected
  conceptual introductions with contextual prose. The walkthrough now begins
  with its binary-classification example and retained execution instructions.
- Retained scientific comparison tables, notation tables, worked examples,
  interpretation qualifications and figure explanations.
- Synchronized the walkthrough generator, code-free companion and notebook
  Markdown. The executable cells and existing outputs were preserved.
- Updated existing presentation tests that required the superseded matrices,
  footer labels or Next/Go deeper formatting. Existing scientific, public-API
  and destination checks remain in place.

No new public pages, scientific methods, dependencies, environment changes,
library source changes or major navigation restructuring were introduced.

## Representative changes and scientific rationale

| Before | After | Purpose |
|---|---|---|
| Workflow ended with ten concepts crossed with three learning depths. | The main explanation retains its workflow, task/method comparison, substituted-value calculation and assumptions; a short worked-example paragraph supplies context. | Readers encounter the CE mechanism instead of a navigation matrix. |
| How CE Works repeated numbered levels and six topic cards. | Connected paragraphs follow prediction, factual weight, alternative output, calibration method and interpretation limits. | The existing 0.286 − 0.476 = −0.190 example connects quantities concretely. |
| What & Why contained a seven-row reading route and repeated topic cards. | Prose distinguishes prediction, calibration, explanation and the scope of CE, with a concrete-example link and retained regulatory caveat. | Introduces the relationship between concepts without announcing a learning framework. |
| Walkthrough began with a repeated instructional pattern and eight learning objectives. | Introduction states the prediction/calibration problem, identifies the executable example and gives notebook/install instructions. | Gets readers to the example while preserving prerequisites and reproducibility. |
| Every entry page ended with audience-tier metadata. | Those footer labels are absent; the Beta identification remains. | Removes editorial metadata from the reader's explanation. |

The substantive explanations remain anchored in the original CE
[classification tutorial](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_classification.html),
[regression tutorial](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_regression.html)
and [interpretation guide](https://calibrated-explanations.readthedocs.io/en/stable/foundations/how-to/interpret_explanations.html).
The existing candidate's worked example supplies the numbers; no new
measurements or guarantees were invented.

The four acceptance corrections are inherited from the validated parent:
canonical reject-confidence arguments and explicit unsupported-strategy
boundary; qualified individual-probability wording; target intervals versus
threshold-event probabilities; and pair/merged-estimate/protocol distinctions.
Their public-API smoke tests passed again.

Scientific references removed from the workflow matrix were relocated beside
the relevant method, substitution and calibration discussions. All six
external implementation/test URLs from that page remain. Vovk and Petej
(2014), Vovk et al. (2019), the CE classification/regression papers and the
conditional CE reference remain connected through the existing citing page.
The distinction between theorem, implementation, example and author review
remains on the methods page.

The [existing figure-by-figure review](../docs-rtd-corrections-20261116/README.md#figure-by-figure-review)
continues to apply to all 19 instructional instances. This candidate changes
neither their figure definitions nor the immediate explanatory text.

## Navigation and anchor evidence

Before removal, every useful destination in the workflow, reading and concepts
tables was checked against the previous rendered sidebar. The sidebar already
included the introductory pages, examples, methods, semantics, alternatives,
conditional calibration, architecture, terminology and parameter references.
No destination needed to be silently dropped.

After editing:

- The rendered workflow sidebar has the same **142 distinct target URLs** as
  the baseline. The original hierarchy and ordering are preserved.
- Both builds contain **158 HTML pages**. No existing page is missing.
- Comparison of article IDs across all 158 baseline/new HTML pages found
  **zero lost anchors**. Renamed framework headings retain their original
  fragment IDs as page-local anchors.
- Scientific citations and source links were retained in context rather than
  converted into another topic inventory.
- A small set of direct worked-example links was retained where the existing
  reader-journey checks demonstrated their usefulness.

## Validation results

| Check | Result |
|---|---|
| Documentation and public-API example tests | **380 passed, 1 deselected**. The wheel-install test was excluded to avoid creating/installing a separate environment. One obsolete test requiring seven navigation-table rows was removed; remaining presentation checks reflect the new requirements. |
| Strict Beta Sphinx build | Passed with `-W --keep-going`; fresh build followed by strict incremental validation after final prose edits. |
| Strict standard Sphinx build | Passed using the same flags without the Beta environment setting. |
| Internal-link checker | Both builds: **158 pages, 0 broken links**. |
| Chromium layout/theme checks | **80 passed**: 20 relevant pages × 1365/390px × light/dark. No document overflow, broken article images, Mermaid render errors, MathJax errors or visible tier/level framework text on checked pages. |
| Sidebar interactions | Four successful real link clicks: desktop/mobile × light/dark, including opening the mobile menu. |
| Mathematical rendering | Methods-page mathematics rendered in all four layout/theme combinations; no MathJax error nodes. |
| Manual visual review | What & Why and How CE Works screenshots inspected; continuous prose, sidebar and mobile layout are readable. Existing dense scientific plot labels still benefit from full-size viewing. |
| Figure preservation | All **19 figure/diagram blocks** unchanged; existing explanations remain immediately afterward. |
| Computational content | All **6 math blocks** and **379 code/output blocks** unchanged. Generator executable cells unchanged. |
| Notebook preservation | Only Markdown cells **0 and 41** changed. Code, execution counts, outputs and environment metadata unchanged. |
| Scientific review markers | Existing SR identifiers retained on every page that contained them. Author-review register unchanged. |
| Source/configuration/assets | Library source, dependencies, Sphinx configuration and figure assets unchanged. |
| Quick verification profile | Could not complete because `mypy` is unavailable; no unrelated installation attempted. |
| Whitespace validation | `git diff --check` passed. |
| User-owned index | Main checkout staged fingerprint remains `C9186FF498C07E76EE43D484845F91200DC43E22341953A0F454751307177527`. |

Commands used the existing Python 3.13 environment:

```text
PYTHONPATH=src MPLBACKEND=Agg python -B -m pytest -o addopts='' -q --tb=short -p no:cacheprovider tests/docs tests/integration/test_doc_examples_smoke.py -k 'not wheel_install'
CE_DOCS_BETA=true python -B -m sphinx -W --keep-going -E -b html docs <beta-output>
python -B -m sphinx -W --keep-going -E -b html docs <standard-output>
python -B scripts/docs/check_internal_links.py <output>
python -B scripts/local_checks.py --profile quick
```

Local HTML, screenshots and machine-readable evidence:
`C:/Users/ashra/AppData/Local/Temp/ce-continuous-20261116/`.
The `verification/` directory contains `layout.json`, `anchors.json`,
`preservation.txt` and screenshots. Test/build logs use the same
`ce-continuous-*` prefix in the parent temporary directory.

## Remaining review and publication

No open scientific or legal issue was silently resolved. The existing
author-review register still governs the exchangeability/protocol wording,
CPS finite-sample coverage, Venn–Abers pair/merged/default-multiclass output,
explanation ranges, threshold-event construction and reject-policy validity.

Recommend educational review of the revised conceptual introductions and
worked-example transitions, followed by CE-author review of those existing
scientific qualifications. The current pass improves presentation without
claiming that build success proves statistical validity.

The isolated candidate is prepared for review, with no promotion to Beta
main/latest or modification of previous previews. RTD publication remains
pending explicit publication authorization under the current brief.

Reviewable commits:

- `84652a89`: remove visible tier footers, including matching generator and
  existing presentation-test adjustments.
- `276f4ea6`: continuous conceptual prose, navigation-table removal,
  contextual references, preserved anchors and generator/notebook synchronization.
- The subsequent report commit contains this plan, validation evidence and
  the complete modified-page inventory.

[Experimental GitHub branch](https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/tree/beta/sidebar-learning-paths-20261116).
No RTD build has been requested for this candidate.
