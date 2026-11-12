# Page inventory — run 2

Source: `git diff --numstat 22629495 HEAD -- docs` (126 tracked Markdown pages in total).

## Substantially rewritten (3)

| Page | Lines + / − | Level |
|---|---|---|
| `get-started/quickstart_walkthrough.md` (generated; generator `scripts/docs/build_quickstart_walkthrough.py`) | +397 / −367 | 1–2, links to 3 |
| `foundations/concepts/probabilistic_regression.md` | +133 / −18 | 2 |
| `foundations/concepts/alternatives.md` | +109 / −5 | 2 |

## Newly created (3 pages, 1 section)

| Page | Lines | Level |
|---|---|---|
| `what-is-ce.md` | 146 | 1–2 |
| `foundations/concepts/ce_workflow.md` | 89 | 1, learning path to 3 |
| `practitioner/evaluate_ce.md` | 168 | 2 |
| `get-started/ml-foundations.md` §A7 (new section) | +38 | 1 |

## Reorganised (navigation, cards, routes)

`index.md` (2 sidebar entries) · `sections/what-and-why.md` · `sections/how-ce-works.md` ·
`sections/in-practice.md` · `sections/software-integration.md` ·
`foundations/concepts/index.md` · `practitioner/index.md` · `get-started/index.md`
(idea-to-section map)

## Minor edits

- `tasks/classification.md`, `tasks/regression.md`, `tasks/probabilistic_regression.md` ("Go further");
- `glossary/science.md` (+4 entries) and `glossary/index.md` (A–Z);
- `appendices/rtd_tier_map.md`.

## Deferred for CE-author review (unchanged content on purpose)

| Page / passage | Register |
|---|---|
| `compare.md` (performance claims, "conformal" umbrella) | SR-05, SR-06 |
| `tasks/classification.md` "(counterfactuals)", "epistemic and aleatoric", "necessary to flip" | SR-07, SR-08 |
| `tasks/probabilistic_regression.md` "aleatoric + epistemic" | SR-07 |
| `foundations/concepts/explanation_structures.md` filter semantics | SR-09, SR-10 |
| "Exchangeable or distribution-matched" (9 pages) | SR-01 |
| `calibration_methods.md` (ADD-1) R1–R11 | SR-02, SR-03, SR-15 |
| Explanation construction page (ADD-2), vision page (ADD-4) | SR-14; content needed |

## Unchanged

The remaining 105 tracked pages, including:
- the semantics page (one label and one further-reading link added in run 1, none in run 2);
- ADD-1;
- the API pages;
- the playbooks;
- the governance and contributor pages;
- the upgrade and migration guides.
