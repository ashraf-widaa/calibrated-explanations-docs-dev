# Stage 06 — Repository organisation and research assets

**Started:** 18:31 · **Completed:** 18:32 (clock-read)
**Starting commit:** `5a48de93`

## Audit (building on run 1, AD-01 to AD-07)

| Asset | State | Decision |
|---|---|---|
| Inherited CE layout (`src/`, `tests/`, `notebooks/`, `examples/`, `development/`) | Unchanged; upstream traceability intact | Keep (AD-01) |
| Bibliography | Canonical in `docs/citing.md`; method references in ADD-1, semantics and the new pages | Keep; run 2 pages cite the same DOIs |
| Notebooks | Linked from the In Practice landing page and the interpretation guide (run 1) | Keep in place (AD-05) |
| Walkthrough generator | Regeneration procedure, kernel requirement and safety checks were undocumented | **Fix:** `scripts/docs/README.md` |
| Internal link checker | Used in every gate but held only in the agent's scratchpad | **Fix:** `scripts/docs/check_internal_links.py`, with unit tests |
| Run records | `development/reports/autonomous-runs/` (AD-02) | Keep |

## Changes

| File | Change |
|---|---|
| `scripts/docs/check_internal_links.py` | New maintainer tool: checks internal hrefs and anchors in a built site; optional page-set diff against a baseline; exit status 1 on breakage |
| `scripts/docs/README.md` | New: how to regenerate the walkthrough (`PYTHONPATH=src`, kernel, `git add -f` for figures), its built-in guards, related tests, and the recommended validation sequence |
| `tests/scripts/test_check_internal_links.py` | 2 tests on a synthetic site (missing page, missing anchor, external ignored, exit codes) |

## Validation

| Check | Result |
|---|---|
| `check_internal_links.py` on the latest build | 153 pages, 0 broken, exit 0 |
| New unit tests | 2 passed |

No library code, import path or build path changed.

## Commit, push, publication

- **Commit:** see `RUN-STATUS.md`.
- **Pushed:** no (B-01).
