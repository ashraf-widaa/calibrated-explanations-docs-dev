# Content change register — Quick Start v3

For each edited page: previous and new location, problems, changes,
duplication removed, evidence, tests and limitations.

## `get-started/index.md` — landing (Tier 1)

- **Location:** unchanged.
- **Problems:** too long; no entry by reader goal; duplicated tables.
- **Changes:** definition paragraph; workflow figure; three path cards (A, B, C)
  with reader and question; recommended order A → B → C; "Before you start"
  (installation, Quick API, glossary, API reference, CE workflow, interval
  semantics, web demo); new toctree labels A1–C5.
- **Duplication removed:** 60-second table, mermaid flowchart, learning-path
  table, "where each idea is taught" table, task-quickstart list, onward routes.
- **Evidence:** Q3-18. **Tests:** `test_quick_start_landing_offers_three_paths_in_order`,
  `test_quick_start_landing_links_setup_api_and_deeper_science`, glossary
  single-link test. **Limitations:** the figure's small labels are hard to read
  at phone width without tapping it.

## `get-started/why-ce.md` — new (A2, Tier 3)

- **Changes:** running example; conventional workflow; CE workflow with
  figure; requirements; three data sets; four ideas; assumptions and
  limitations; next.
- **Duplication removed:** absorbs the landing's 60-second comparison.
- **Evidence:** Q3-01 to Q3-04. **Tests:** built strictly; links checked.
- **Limitations:** no code by design.

## `get-started/ml-foundations.md` (A1)

- **Changes:** title "Machine learning essentials"; Path A framing; next → `why-ce`.

## `get-started/quickstart_walkthrough.md` (B, generated)

- **Changes (in the generator):** Path B pattern statement; links to Path A and
  C; educational disclaimer; **Question** cue in §2–§8; "Common mistakes to
  avoid"; next-steps rows to C1 and C5. Regenerated: no output number changed.
- **Tests:** generator/page/notebook sync tests; `PROSE_NUMBERS` guard;
  walkthrough content test.

## `get-started/ce-tasks-and-modes.md` (C1)

- **Changes:** title "Tasks, modes and capabilities"; "Four terms that are easy
  to mix up" table; "At a glance" table (mode, method, model needs, output,
  explanations, key limitation, quickstart); three pre-checks merged from the
  60-second page; SR-02 "under review" marker; next → quickstarts and C5.
- **Duplication removed:** 60-second page content.
- **Evidence:** Q3-02, Q3-05, Q3-06. **Tests:** `test_path_c_keeps_the_four_concepts_distinct`.

## `get-started/quickstart_classification.md` (C2)

- **Changes:** purpose and prerequisites; printed output for split,
  probabilities with ranges (`normalization="simplex"`), factual rules,
  alternatives; interpretation of each; common mistakes; next.
- **Evidence:** Q3-07, Q3-08. **Tests:** execution and output-match tests.
- **Limitations:** 30 calibration cases give very wide ranges; stated on the page.

## `get-started/quickstart_regression.md` (C3)

- **Changes:** two modes explained; printed intervals with actual values,
  threshold probabilities, factual weights, alternatives; interpretation;
  common mistakes.
- **Evidence:** Q3-08 to Q3-10. **Tests:** execution and output-match tests.

## `get-started/quickstart_guarded.md` (C4)

- **Changes:** reframed as an explanation configuration for any mode; rule
  counts and audit summary printed and interpreted; common mistakes. The
  semantics note, fast-explainer warning and migration note are kept.
- **Evidence:** Q3-11, Q3-12. **Tests:** execution and output-match tests;
  guarded wording tests in `tests/unit/core/explain/test_guarded_explain_api.py`.

## `get-started/apply-to-your-data.md` — new (C5, Tier 3)

- **Changes:** four checks; seven steps with real output (split, pre-trained
  pipeline, wrap and calibrate, predictions, explanation, test-set check,
  save/load); common problems; optional AI-assistant section with a
  ten-point reusable prompt and review advice.
- **Evidence:** Q3-01, Q3-02, Q3-13 to Q3-17. **Tests:** execution and
  output-match tests; `test_apply_page_offers_a_reviewable_ai_assistant_prompt`.

## `getting_started_60s.md` — retired

- **Changes:** orphan redirect stub (meta refresh + link) to C1.
- **Tests:** `test_retired_sixty_second_page_redirects_to_path_c`.

## `foundations/concepts/ce_workflow.md`

- **Changes:** mermaid diagram replaced by the workflow figure.

## Other files

- `docs/_static/figures/ce-in-ml-workflow.svg` (new; added with `git add -f`
  because `*.svg` is ignored).
- `docs/appendices/rtd_tier_map.md`, `README.md`.
- `tests/docs/get_started/test_quickstart_examples_execute.py` (output-match,
  C5 added), `tests/docs/get_started/test_quickstart_continuity.py`.
