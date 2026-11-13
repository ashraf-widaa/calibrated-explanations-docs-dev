# Decision log and progress report (2026-11-13)

## Decisions

| ID | Decision | State | Note |
|---|---|---|---|
| D-16…D-22 | WP-1 decisions | **Approved** (PO, earlier today) | Implemented in `917a04e2` |
| M-1 | Master prompt: autonomous Beta work, experimental branches and RTD versions authorised; promotion and protected operations not | **Approved** (PO master prompt) | — |
| M-2 | Branch names `beta/v1-reference`, `beta/v2-learning`, `beta/v3-visual`, `beta/integrated-candidate` | **Taken** (agent, within M-1) | From `917a04e2`; no existing branch changed or deleted |
| M-3 | V-6 placed on the existing `calibrated_interval_semantics` page (no new page) | **Taken** (agent) | Master prompt: no new pages without approval |
| D-23 | Sync Beta `src/` with official `main` (`371bd806`, one commit) | **Proposed** | Docs were made version-neutral instead |
| D-24 | Adopt `beta/integrated-candidate` as the next Beta baseline (merge into `main`) | **Proposed** | Requires PO approval and a verified preview |
| D-25 | New pages from the plan (calibration intuition, explainable AI, contributor setup) | **Deferred** | Need explicit approval of new pages |
| N-01…N-05, SR-01…SR-16 | Scientific questions | **For author confirmation** | `02-author-review-sheet.md` |
| R-1 | Combine V2 and V3 by cherry-picking selected commits | **Rejected** | The merge was conflict-free; a merge keeps both histories traceable |

## Progress report

**Completed.**
1. WP-1 checkpoint committed (`917a04e2`), path-limited; PO-staged files left untouched.
2. Official-vs-Beta master audit (`01`): 23 findings, coverage and drift
   analysis, release-vs-dev verification (v1.0.2 reproduces every published
   tutorial output and the walkthrough byte for byte).
3. Beta V2 (`1e487429`), Beta V3 (`f06061b9`), integrated candidate (`944942cd`),
   each validated (see `05`).
4. Author-review sheet (`02`), version register (`03`), comparison (`04`).

**Evidence.** Build logs, test counts and link checks in `05`; Playwright
measurements; v1.0.2 worktree runs.

**Issues.**
- Push and RTD activation are blocked for the agent (`03`).
- Ports 8000 and 8001 on this machine are still held by preview servers from
  the previous session (old builds); use **8002** for the integrated
  candidate. Closing those terminals frees the ports.
- Untracked files from earlier work remain (`plotspec_example.png` in the
  repository root, an unused regression plot in `quickstart_assets/`, an
  untracked file whose name begins `s -ExecutionPolicy …` created by a
  PowerShell command); deleting files is outside the agent's permissions.

**Next actions.**
1. PO: push the four branches and activate their RTD versions (`03`).
2. Agent: verify the published versions, update `03`, then continue with the
   backlog in `12` (revision 5 mapping), next WP-6 (troubleshooting, Quick API
   components), WP-13/WP-14 landing intros, and the remaining WP-18 tables.
