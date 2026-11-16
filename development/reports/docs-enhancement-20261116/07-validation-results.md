# 07 — Test and validation results

**Environment:**
- Windows 11, Git Bash.
- `C:\Python313`: Python 3.13.7, Sphinx 7.4.7, myst-parser 3.0.1, pydata-sphinx-theme 0.16.1, scikit-learn 1.8.0, pandas 2.3.3, numpy 2.3.4, Playwright 1.65.0 with headless Edge.
- CE from `src/` (1.1.0.dev0) via `PYTHONPATH=src`.
- Worktree `wt-next`, branch `beta/next-docs-enhancement`.

Every result below was produced in this session. Nothing is carried over from
earlier runs.

## 1. Gates on the final tree

| Gate | Command | Result | Blocks? |
|---|---|---|---|
| Strict Beta build | `CE_DOCS_BETA=true python -m sphinx -W --keep-going -E -b html docs <out>` | exit 0, **0 warnings** | — |
| Strict standard build | same without `CE_DOCS_BETA` | exit 0, **0 warnings** | — |
| Internal links (both builds) | `python scripts/docs/check_internal_links.py <out>` | **158 pages, 0 broken** | — |
| Docs tests + Quick API smoke | `PYTHONPATH=src python -m pytest -q tests/docs "tests/integration/test_doc_examples_smoke.py::test_quick_api_python_examples_execute_without_error"` | **365 passed, 0 failed** (baseline `73048761`: 335 docs tests) | — |
| Responsive / theme | `scratchpad/repro/visual_check.py`: 9 changed pages × 390/1440 px × light/dark | 36 views: 0 page overflow, 0 broken images, 0 MathJax errors, Beta banner on all | — |
| Version reproductions | `repro_troubleshooting.py`, `repro_extra.py`, `quick_api_example.py`, `one_sided.py` on v1.0.2, Beta `src/`, official `main` | As in `02` and `05` §2 | — |
| Notebooks | `scripts/docs/run_notebooks.py` (kernel `python3`) | 5 passed, 2 failed (environment, `02` §3) | No: failing notebooks are not linked |
| Rollback dry run | `git read-tree -u --reset a55c7e9d` + commit in a scratch worktree | tree hash = `a55c7e9d` tree; fast-forward from `73048761` | — |

Two problems found and fixed during validation:
1. **Troubleshooting lookup links.** They used `[text](#label)`, which MyST
   does not resolve to labelled targets (13 build warnings). They now use
   `{ref}`.
2. **WP-14 test regex.** It read the reading-order items line by line and
   missed items that wrap onto a second line. It now matches flattened text.

## 2. Regression comparison with the baseline (`73048761`)

| Aspect | Baseline | New | Note |
|---|---|---|---|
| Pages built | 158 | 158 | No page added or removed; URLs unchanged |
| Broken internal links | 0 | 0 | — |
| Tests | 335 | 365 | +29 new docs tests, +1 smoke test in the gate |
| Tables scrolling at 390 px (9 checked pages) | 11 | 8 | Improved; none causes page overflow |
| Existing tests changed | — | 1 (`test_doc_examples_smoke.py`, block indices) | Same fragments still executed |

No new failure and no unintended change was found. The diff touches only the
files listed in `02`–`04`.

## 3. Not run, and why

| Check | Reason |
|---|---|
| Full repository suite (`pytest -q`) | No `src/`, dependency or non-docs test change other than one integration test, which was run |
| External-link crawl | Rate limits (RTD 429) and the scope of this cycle. The one new external link, PMLR `v70/guo17a`, was fetched and its title, authors, volume and pages match the citation. The notebook URLs are unchanged, and their targets exist on the official `main` |
| Published preview | Push is denied for the agent (`09`) |
