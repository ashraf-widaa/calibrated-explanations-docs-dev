# Validation summary — Quick Start v3

All checks were run locally on 2026-11-12 on the final working tree
(commits `e44bb875`…`501911e1`).

| Check | Command / method | Result |
|---|---|---|
| Strict Beta build | `CE_DOCS_BETA=true python -m sphinx -W --keep-going -E -b html docs _build/qsv3` | Exit 0, **0 warnings** |
| Strict standard build | same without `CE_DOCS_BETA` → `_build/qsv3-std` | Exit 0, **0 warnings** |
| Docs tests | `pytest tests/docs tests/scripts/test_check_parameter_naming.py` | **298 passed** |
| Get-started tests | `pytest tests/docs/get_started/` | 23 passed (incl. 8 execution/output-match, 5 new landing/Path C tests) |
| Guarded wording tests | `pytest tests/unit/core/explain/test_guarded_explain_api.py -k docs` | 2 passed |
| Executable examples | Every python block of C2, C3, C4, C5 executed in order; printed output compared with the page | All match |
| Walkthrough | Regenerated with `scripts/docs/build_quickstart_walkthrough.py`; `PROSE_NUMBERS` guard | Passed; prose-only diff, no output number changed |
| Internal links | Scratchpad link checker and `scripts/docs/check_internal_links.py` | 155 pages, **0 broken links** |
| Full test suite | `pytest -q` | 5338 passed, 4 skipped, **4 failed**, all four inherited and failing on baseline `e964a79c` too: wheel build (`build` module not installed) and separate-process import/checksum tests. None touches docs. |
| Responsive / theme | Headless Edge at 390 and 1440 px, light and dark, 7 pages | No horizontal page overflow on any page; figure 358 px (phone) / 560 px (desktop) |
| Accessibility | Figure has `<title>`, `<desc>`, 457-character alt text, card background for dark mode, and opens full size when tapped | Checked |
| Mojibake scan | All changed files scanned for double-encoded UTF-8 | Clean (two test-file artefacts fixed before commit) |

## Not verified

- The live Beta site: the branch is **not pushed** (see PUBLICATION-HISTORY.md).
- Screen-reader testing with assistive technology was not performed.
