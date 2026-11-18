# CE documentation — developer-experience changes (2026-11-18)

Release record for branch `docs/ce-devex-20261118`, which starts from the final
learning-journey candidate `0a0d35ad` (`ce-review-final-20261119`). It
implements the documentation-only recommendations of the developer-experience
review (`learning-reports/07-devex-documentation-review.md`, kept outside the
repository). Immutable snapshot: `ce-review-devex-20261118`.

## What changed for readers

| Area | Change |
|---|---|
| Homepage | Shorter hero; a primary *Quickstart: 10 minutes* button and a secondary *See an example, no code* button; a new *Your first explanation* section with the install line, four lines of code, the real output figure and a "Start here" table by reader type |
| Get Started (was Quick Start) | The sidebar holds the five-step journey in order: Install → Quickstart → Read your first explanation → Apply CE to your own data → Evaluate CE, then CE by Example (no code) and Coming from SHAP or LIME. The hub page stays code-free. |
| New Quickstart | `get-started/quickstart.md`: split, wrap, calibrate, predict with a range, explain, read as text, ask "what if", in about 10 minutes; every output is checked by `test_quickstart_examples_execute.py` |
| Journey pages | Progress bar (`nav.ce-journey`, current step marked with `aria-current`), time estimate on every step |
| Generated pages | CE by Example is now "step 2 without code"; the walkthrough is "step 2, in depth". Text only, changed through the generator; `walkthrough-figure-1.png` is byte-identical (SHA-256 `91eb7d8a…`). |
| How to read CE explanations | Classification first; regression outputs and structured payloads/telemetry moved to their own later sections |
| Comparison | Retitled. Adds a "which method answers your question" table and a side-by-side table covering SHAP, LIME, counterfactual methods and CE. Marked as part of the SR-06 author review, with no ranking claim. The previous text is kept unchanged below. |
| New: Coming from SHAP or LIME | A call-by-call mapping and three differences to unlearn (not additive, labelled calibration data, ranges) |
| API reference | `WrapCalibratedExplainer` first ("start here"), `CalibratedExplainer` marked advanced; the `get_rules()` keys documented; new `api/exceptions.md` with the hierarchy and the verified behaviour of common mistakes |
| Quick API | Retitled as a cheat sheet; the example passes `class_labels`; the mode-specific semantics notes moved, unchanged, to the end of the page |
| Installation | Journey step 1 with an onward link; the contributor section renamed |

## Not changed (needs a decision outside documentation)

- Section names other than *Get Started*.
- The STD-004 notes on the tutorials.
- Docstring return types and `Raises` sections in the library code.
- The open author questions (SR-01 … SR-16), including the SR-06 comparison
  wording.
- Splitting the walkthrough.
- The AI-assistant section on *Apply CE to your own data*, which is guarded
  by an existing test.
- Commercial Services stays a homepage section.

## Preservation

- **Anchors:** 0 lost against the `ce-review-final-20261119` build. Renamed
  headings keep their former ids:
  - `quick-start-understand-explore-and-apply-ce`
  - `quick-api-main-components-and-calls`
  - `optional-contributor-fast-path`
  - `provenance-and-telemetry`
  - `calibrated-explanations-comparisons-ce-first`
- **Existing text:** none removed from the comparison page or the semantics
  notes; the moved sections are verbatim.
- **Pages and URLs:** none removed or moved; three pages were added
  (`get-started/quickstart`, `get-started/coming-from-shap-lime`,
  `api/exceptions`).

## Validation

| Check | Result |
|---|---|
| `tests/docs` | 409 passed (was 395; new guards in `test_devex_20261118.py`; journey, architecture, hub and homepage guards updated to the new design) |
| `tests/scripts/test_check_parameter_naming.py` + `tests/integration/test_doc_examples_smoke.py` | 21 passed, 1 failed (pre-existing: the wheel test needs the uninstalled `build` package) |
| Strict Sphinx, Beta and standard | 0 warnings, 161 pages each |
| Internal links | 0 broken |
| Assets | 2,551 references, 0 missing; 0 images without alt text |
| Official test `test_top_level_toctree_targets_exist` | Unmodified and passing |
