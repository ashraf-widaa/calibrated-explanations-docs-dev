# Stage 03 — GitHub repository architecture

**Started:** 2026-11-12 10:21 · **Completed:** 2026-11-12 10:30
**Starting branch / commit:** `docs-dev/autonomous-20261112` / `802bf8cc`

## Audit

**Fork point:** `f908527f` (2026-11-04) is the merge base with `upstream/main`. Since then there are 32 Beta commits and 1 upstream commit (`371bd806`, CPS endpoint semantics).

| Class | Material | Count / evidence |
|---|---|---|
| 1 Inherited from CE | `src/calibrated_explanations` (137 files), `tests/` (401), `notebooks/` (24), `examples/use_cases/` (6), `evaluation/`, top-level `reports/` (187), `artifacts/` (73), `development/` (adrs, standards, capabilities, current-work, finished-work, schemas), `.github/` workflows (ci, maintenance, scheduled), agent configuration (`.claude`, `.codex`, `.agents`) | identical file counts in `upstream/main` except as listed below |
| 2 Beta documentation work | `docs/` (+20 pages: glossary, sections, ADD-1, ml-foundations, ce-tasks-and-modes, walkthrough), `tests/docs/*` (+6), `scripts/docs/build_quickstart_walkthrough.py`, STD-004 amendment (+10/−4), `pyproject.toml` (+`sphinx-design` in `dev`), `learning-reports/` (29 tracked), `LEARNING_JOURNAL.md`, run records | `git diff --name-status f908527f HEAD` |
| 3 Shared infrastructure | `.readthedocs.yaml`, `docs/conf.py`, `docs/requirements-doc.txt`, `Makefile`, CI strict docs job (`ci.yml` 149–174) | — |
| 4 Generated or temporary | `/_build/` (local builds), `/.playwright-mcp/` (browser-automation state) | untracked, now ignored |
| 5 Obsolete or duplicated | `docs/multiclass_all_classes_gap_analysis.md` (orphan analysis page); `docs/foundations/concepts/telemetry.md` (relocation stub) | handled in Stages 09–11 as documentation items |
| 6 Uncertain (PO-owned, untracked) | 108 files in `learning-reports/`, `HANDOVER_REPORT.md`, `learning/`, `session-checkpoint-batch-5-prep.md` | left untouched (not ignored, not moved) |

**Notebooks:**
- 4 core demos, 7 advanced, 3 miscellaneous, 1 paper-based, 3 quickstarts;
- governed by `docs/contributor/notebook_policy.md`;
- **none linked from the published docs** (gap, Stage 08).

**CI:** a strict docs build exists (`python -m sphinx -W --keep-going …`).

## Decisions

AD-01 to AD-07 in `ARCHITECTURE-DECISIONS.md`. In summary:
- keep the inherited layout;
- no `src/` or `research/` changes;
- `learning-reports/` stays;
- run records go in `development/reports/autonomous-runs/`;
- generated folders are ignored.

## Changes

| File | Change |
|---|---|
| `.gitignore` | `/_build/`, `/.playwright-mcp/` |
| `development/README.md` | Two rows in "Canonical Locations": run records; learning reports |
| `ARCHITECTURE-DECISIONS.md` | New |

## Validation

- No docs source changed, so no build is needed.
- `pytest tests -k "readme or development or governance or docs"`: 304 passed.
- No test references `development/README.md` (grep).
- Untracked count went from 114 to 112; only the two generated folders are now ignored.

## Remaining issues

The PO's untracked material should eventually be committed or archived by the PO.

## Commit, push, publication

- **Commit:** see `RUN-STATUS.md`.
- **Pushed:** no (B-01).
- **Published:** no.
