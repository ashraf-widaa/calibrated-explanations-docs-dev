# Targeted Beta review candidate

Date: 17 November 2026. Mode: documentation usability feature; public CE API
unchanged, with no migration required.

## Candidate

- Baseline: `beta/sidebar-learning-paths-20261116`,
  `62b38b27104b1f77f41798097069e3b461cfa7a7`.
- New branch: `beta/author-review-20261117`.
- Documentation implementation: `2f068527ca7e5b9a872d2a3cf9d4a45ad9577996`.
  A subsequent commit adds this validation record; the final review-package
  artifact records the complete candidate HEAD.
- Reserved preview URL:
  https://calibrated-explanations-beta.readthedocs.io/en/beta-author-review-20261117/
- This is an experimental review environment for CE authors and the internship
  supervisor, not official CE documentation.
- Publication requires authorization for this new version. Until activation
  and a successful build are verified, the reserved URL is not a published preview.

## Three targeted corrections

| Area | Change | Evidence |
|---|---|---|
| Regression transition | Before section 5, identifies the preceding threshold-event query and the following unthresholded target-value explanation. Weights in the latter use target units. | Original regression guide; candidate wrapper and explanation implementation; new public-API execution test confirms the threshold prediction does not alter the next factual explanation. |
| Range wording | What & Why now distinguishes requested prediction uncertainty from feature-weight ranges and method-specific interpretation. The workflow's matching prediction step explicitly names `uq_interval=True`. | Public prediction API and canonical interval semantics. No new individual-probability or explanation-coverage guarantee. |
| Plot and mobile selector | CE by Example provides a browser-opening full-size plot link after the explanatory paragraph. Mobile version selection moves into the existing sidebar once valid RTD data is available; desktop keeps the normal RTD widget. | Built-image navigation and responsive interactions; documented RTD addon event integration; actual RTD SDK test against the previous preview using browser-local HTML injection only. |

The full-size link is also present in the generator's code-free companion
template, so regeneration will preserve it. The figure, caption, alternative
text and immediate explanation are unchanged.

The mobile integration adds a native labelled select in the existing drawer.
It uses documented RTD version data, preserves the current page when switching
versions, supports keyboard focus and updates without duplicate controls.
It hides the floating addon only on small screens after a usable current
version has been installed. Without usable addon data, RTD's fallback remains.
The script and API-version metadata are enabled only for the experimental
Beta build. No project-wide RTD setting was changed.

Implementation files:

- `docs/get-started/quickstart_regression.md`
- `docs/sections/what-and-why.md`
- `docs/foundations/concepts/ce_workflow.md`
- `docs/get-started/ce-by-example.md`
- `scripts/docs/build_quickstart_walkthrough.py`
- `docs/_static/ce-docs.css`
- `docs/_static/ce-rtd-versions.js`
- `docs/_templates/base.html`
- `docs/conf.py`
- `tests/integration/test_doc_examples_smoke.py`

Reviewable commits:

1. `923c61c6`: regression quantities and uncertainty wording, including an
   execution test of the documented regression sequence.
2. `2f068527`: full-size image access and candidate-local mobile version selection.

## Technical and scientific traceability

- [Original CE regression tutorial](https://calibrated-explanations.readthedocs.io/en/stable/get-started/quickstart_regression.html).
- [Original CE explanation interpretation](https://calibrated-explanations.readthedocs.io/en/stable/foundations/how-to/interpret_explanations.html).
- Candidate `core/wrap_explainer.py`: prediction and explanation calls resolve
  their arguments separately. The tutorial does not set a configured default
  threshold; the correction describes this example, rather than denying that
  configured defaults exist.
- Candidate `explanations/explanation.py`: public `is_regression`,
  `is_thresholded` and `is_probabilistic` distinguish the returned quantities.
- Existing canonical semantics and ADR-021: probability information, target
  intervals and derived explanation ranges have different interpretations.
- [RTD addon event integration](https://docs.readthedocs.com/platform/stable/addons.html#custom-event-integration):
  API-version metadata and the `readthedocs-addons-data-ready` event.
- [RTD flyout documentation](https://docs.readthedocs.com/platform/stable/flyout-menu.html):
  the floating widget and theme integration. Its project-wide settings were
  deliberately left untouched to preserve previous previews.

These are technical and editorial corrections. Neither example execution nor
successful rendering establishes a new statistical guarantee.

## Validation

| Check | Result |
|---|---|
| Documentation and example suite | **381 passed, 1 deselected**. The wheel-install test was excluded to avoid creating/installing another environment. |
| New regression sequence test | Executes the tutorial's fit/calibrate, interval prediction, event-probability query and factual explanation. The target explanation retains its weights; an explicit threshold explanation is probabilistic. |
| Strict Beta Sphinx | Passed with `-W --keep-going`; API-v1 metadata and the candidate script are present in generated HTML. |
| Strict standard Sphinx | Passed; the Beta-only metadata/script are absent. |
| Internal links | Both builds: **158 pages, 0 broken links**. |
| JavaScript syntax | `node --check docs/_static/ce-rtd-versions.js` passed. |
| Generated Beta UI interaction checks | Eight layout/theme cases: 320, 390, 768 and 1365px × light/dark. Mobile drawer placement, on-screen bounds, keyboard focus, repeated-event handling and full-size-image opening passed. |
| Real RTD SDK integration | Eight cases at the same widths/themes passed, including a real switch to another existing version while retaining the page path. Testing intercepted HTML only inside an isolated browser; the old published preview was not changed. |
| Affected content layouts | **40 cases passed**: five relevant pages × desktop/mobile × light/dark × Beta/standard. No page overflow or broken article images; Beta-only integration is absent from standard pages. |
| Preservation comparison | All **19 figure blocks, 6 math blocks and 379 code/output blocks** are unchanged; no prior article anchors were lost. |
| Preserved scope | Scientific examples, figures, captions, math, library source, dependencies, notebook outputs and the author-review register were preserved. |
| Quick validation profile | Cannot complete: `mypy` is unavailable in the existing environment. No unrelated dependency installation was attempted. |
| Whitespace | `git diff --check` passed. |
| User-owned staged files | Main checkout index fingerprint remains `C9186FF498C07E76EE43D484845F91200DC43E22341953A0F454751307177527`. |

Commands:

```text
PYTHONPATH=src MPLBACKEND=Agg python -B -m pytest -o addopts='' -q --tb=short -p no:cacheprovider tests/docs tests/integration/test_doc_examples_smoke.py -k 'not wheel_install'
CE_DOCS_BETA=true python -B -m sphinx -W --keep-going -E -b html docs <beta-output>
python -B -m sphinx -W --keep-going -E -b html docs <standard-output>
python -B scripts/docs/check_internal_links.py <output>
node --check docs/_static/ce-rtd-versions.js
python -B scripts/local_checks.py --profile quick
```

Temporary HTML and browser evidence:
`C:/Users/ashra/AppData/Local/Temp/ce-review-20261117/`.
Test/build logs use the `ce-review-*` prefix in the parent temporary directory.

## Author questions retained for review

The [existing register](../docs-focused-20261116/author-review.md) is unchanged.
Feedback is still needed on:

- SR-01/SR-02: protocol assumptions and the exact finite-sample CPS statement,
  including ties, endpoints and conditional groups.
- SR-03/SR-13: Venn–Abers pair versus merged probability and default multiclass
  bounds.
- SR-07/SR-09/SR-14: ensured filtering and the scientific interpretation of
  derived explanation-weight ranges.
- SR-15: validity wording for the implemented CPS-score/Venn–Abers
  threshold-event construction.
- SR-16 and the existing regulatory register: reject-policy guarantees and
  legal interpretations require their respective owners' review.

Recommended feedback asks whether the distinctions are scientifically
accurate, whether the worked examples connect the concepts naturally, and
where a newcomer would still encounter an unexplained term or abrupt
transition. This candidate is prepared for that review, without promotion to
Beta latest or changes to official CE.
