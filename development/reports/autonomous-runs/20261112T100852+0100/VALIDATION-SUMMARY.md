# Validation summary — run 20261112T100852+0100

## Commands

| Check | Command |
|---|---|
| Strict Beta build | `CE_DOCS_BETA=true C:\Python313\python.exe -m sphinx -W --keep-going -E -b html docs _build/<stage>` |
| Strict standard build | same, without `CE_DOCS_BETA` |
| Docs tests | `C:\Python313\python.exe -m pytest tests/docs tests/scripts/test_check_parameter_naming.py -p no:cacheprovider -o addopts=""` |
| Link and anchor check | script `linkcheck.py`: every internal `href` and `#anchor` in the build resolves; page-set diff against the previous stage |
| Full suite | `C:\Python313\python.exe -m pytest tests -q -p no:cacheprovider -o addopts=""` |
| Visual and accessibility | Python Playwright with headless Edge: widths 390–1920, light and dark, grid rows, overlap, truncation, contrast, keyboard focus order, search |

## Results per stage

| Stage | Beta build | Docs tests | Links (150 pages) | Other |
|---|---|---|---|---|
| 02 | 0 warnings | 224 passed | 0 broken | Visual matrix from L07 (same source) |
| 03 | n/a (no docs change) | 304 passed (`-k readme/development/governance/docs`) | — | — |
| 04 | 0 warnings | 237 | 0 | Rendered admonition link; 25 autosummary links |
| 05 | 0 | 241 | 0 | Notebook JSON valid |
| 06 | 0 | 241 | 0 | Card anchor renders |
| 07 | 0 | 244 | 0 | Cross-mode anchor renders |
| 08 | 0 | 248 | 0 | External destinations checked (GitHub notebooks, Decision Lab; Expert Hub via the Step 9 browser check) |
| 09 | 0 (after replacing a fencing attempt that produced 16 docstring warnings) | 252 | 0 | PyPI version 1.0.2, requires-python ≥ 3.10 |
| 10 | 0 | 257 | 0 | Beta repository `has_issues: true`; official milestones page exists |
| 11 | 0; standard build 0 | 262 | 0 | Sidebar 129 → 134 (+5 Overview, 0 removed); Beta marker only in the Beta build |
| 12 | (unchanged) | 262 | 0 | Homepage layout re-checked at 390, 1280 and 1440 px, light and dark |

## Full repository suite (Stage 12)

**5309 passed, 4 skipped, 4 failed** (302 s). The four failures are **pre-existing and environmental**: the same four fail identically on the untouched baseline `e964a79c`, checked in a temporary worktree (since removed).
- 1 × wheel smoke: `python -m build --wheel` exits 1 in this environment;
- 2 × separate-process checksum: a child `C:\Python313\python.exe` cannot import the test helpers;
- 1 × import side-effect check: a child process cannot import the package.

The run changed **no** files under `src/`.

## Not performed

- screen-reader testing;
- real-device testing;
- execution of the repository notebooks;
- regeneration of the Quick Start walkthrough (deliberately avoided);
- live verification of the Read the Docs deployment (nothing was pushed, B-01);
- `ruff` (not installed in any local interpreter).
