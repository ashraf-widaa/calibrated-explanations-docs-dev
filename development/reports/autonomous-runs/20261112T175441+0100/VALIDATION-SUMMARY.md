# Validation summary — run 2

Commands as in `scripts/docs/README.md`:
- strict Sphinx build (`-W --keep-going -E`);
- `pytest tests/docs tests/scripts/test_check_parameter_naming.py`;
- `scripts/docs/check_internal_links.py`;
- full `pytest tests`.

| Stage | Beta build | Docs tests | Links | Other |
|---|---|---|---|---|
| 01 | 0 warnings | 270 | 150 pages, 0 broken | Generator reproduced byte-identical before edits; regenerated values equal spec `05` [N] values; task quickstarts execute |
| 02 | 0 | 274 | 151, 0 | — |
| 03 | 0 | 276 | 152, 0 | Concept-page outputs equal the page |
| 04 | 0 | 277 | 153, 0 | Evaluation page outputs equal the page |
| 05 | 0 | 285 | 153, 0 | — |
| 06 | — | +2 script tests | 153, 0 (repository checker) | — |
| 07 | 0 | 289 | 153, 0 | Journeys test; light/dark at 390/1440 px on 7 pages: no page overflow; diagram legible on mobile |
| 08 | 0; standard build 0 | 289 | 153, 0 | Full suite: **5338 passed, 4 skipped, 4 failed** |

## Comparison with the run 1 baseline

| Measure | Run 1 end | Run 2 end |
|---|---|---|
| Docs tests | 262 | 289 (+27) |
| Full suite passed | 5309 | 5338 (+29) |
| Full suite failures | 4 (environmental, reproduced on `e964a79c`) | the same 4 tests, same causes |
| Pages | 150 | 153 (+3 new) |
| Broken internal links | 0 | 0 |
| `src/` changes | 0 | 0 |

## Executed-example coverage added in run 2

- walkthrough (generated);
- 3 task quickstarts;
- `probabilistic_regression`;
- `alternatives`;
- `evaluate_ce`.

The four concept/guide pages are checked output-for-output.

## Not performed

- notebook re-execution (`notebooks/`);
- screen-reader testing;
- external link check;
- live verification of run 2 (not pushed, B-01).
