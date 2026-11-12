# Stage 05 — Quick Start

**Started:** 2026-11-12 10:46 · **Completed:** 2026-11-12 11:05
**Starting branch / commit:** `docs-dev/autonomous-20261112` / `258b65c6`

## Inspected

- `get-started/index.md`: learning path, task quickstarts, setup and help.
- `scripts/docs/build_quickstart_walkthrough.py`: generator; executes cells with `nbclient`.
- `get-started/quickstart_walkthrough.md`: generated.
- `_static/notebooks/quickstart_walkthrough.ipynb`: generated; links rewritten to absolute Beta URLs.
- Earlier audits: Step 9 Journey 1; full review C-13 and C-36.

## Problems

| ID | Problem | Evidence |
|---|---|---|
| QS-1 | No onward route after the Quick Start to the methods (ADD-1) or to Software & Integration | `get-started/index.md` only lists quickstarts, quick API, interpretation and semantics; the walkthrough "Where to go next" table lacks both |
| QS-2 | Generator, page and notebook can drift apart (no test) | `tests/docs/get_started` only checked that the agent-utilities module is not recommended |
| QS-3 | The teaching-first walkthrough rewrite is still pending | The spec in `learning-reports/quickstart-walkthrough-audit/` (rev. 2) was never approved; no "L07-QS" specification exists in the repository |

## Decisions

- **QS-1:**
  - Add an "After the Quick Start" section to the index (How CE calibrates; CE Software & Integration; Practitioner hub).
  - Add three rows to the walkthrough's "Where to go next" table (How CE Calibrates; Integrate with pipelines; CE Software & Integration).
- **QS-2:** The static Markdown table was edited identically in the generator, the page and the notebook (absolute Beta URLs, matching the generator's rewriting). The generator was **not** re-run: re-execution would rewrite every output and figure (≈ 277 KB notebook) for a text-only change. A new test now keeps generator and page identical.
- **QS-3:** **Deferred.** Rewriting the generated tutorial needs the unapproved spec and a full regeneration with output review. Recorded for the final report.

## Files changed

| File | Change |
|---|---|
| `docs/get-started/index.md` | New "After the Quick Start" section |
| `scripts/docs/build_quickstart_walkthrough.py` | +3 rows in "Where to go next" |
| `docs/get-started/quickstart_walkthrough.md` | Same 3 rows |
| `docs/_static/notebooks/quickstart_walkthrough.ipynb` | Same 3 rows (absolute URLs); JSON validated |
| `tests/docs/get_started/test_quickstart_continuity.py` | 4 tests: generator = page; routes to methods and Software; notebook carries the rows; index onward routes |

## Validation

| Gate | Result |
|---|---|
| Strict Beta build | exit 0, 0 warnings |
| `pytest tests/docs …` | 241 passed |
| Links and anchors | 150 pages, 0 broken |

**Not run:** regeneration of the walkthrough (deliberately, see QS-2).

## Commit, push, publication

- **Commit:** see `RUN-STATUS.md`.
- **Pushed:** no (B-01).
