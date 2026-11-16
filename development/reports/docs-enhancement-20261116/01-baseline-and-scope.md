# 01 — Baseline and scope reconciliation

**Date:** 2026-11-16, 09:30–10:00 (Stockholm). **Status:** COMPLETED.

## 1. Verified Git baseline

| Item | Value |
|---|---|
| Main working tree | `D:\Jönkoping\CE-Documentation-Redesign\calibrated_explanations`, branch `beta/v3-visual` (`f06061b9`) |
| Integrated candidate | `beta/integrated-candidate` = `docs-dev/beta/integrated-candidate` = `73048761` (expected value confirmed) |
| Beta `latest` | `docs-dev/main` = `a55c7e9d`; RTD `latest` build 35878420 success; default version `latest` |
| Experimental versions | V1 `917a04e2`, V2 `1e487429`, V3 `f06061b9`, candidate `73048761`: all built successfully on 2026-11-13 |
| Official reference | `upstream/main` = `371bd806` (fetch-only remote; push URL `DISABLED_fetch_only`) |
| Released package | v1.0.2 = `609d7b72` (tag) |
| Remotes | `docs-dev` → `ashraf-widaa/calibrated-explanations-docs-dev`; `upstream` → `Moffran/calibrated_explanations` (fetch only) |
| New remote refs since 2026-11-13 | Dependabot branches for pip (`sphinx-8.1.3`, `pydata-sphinx-theme-0.19.0`, `myst-parser-4.0.1`, `numpydoc-1.11.0`) and `create-pull-request-8.1.3`; RTD built five pull-request previews (#11–#15) at 01:47 UTC, two failed (`09`) |

**Worktrees.**
- The main tree is unchanged.
- `…/76d54f45…/scratchpad/wt-integrated` (`73048761`) is clean; it was used read-only for the baseline build.
- `…/wt-v102` (v1.0.2) was used read-only for version comparisons. Its untracked files are from an earlier session and were left as they were.
- New in this cycle, all in this session's scratchpad:
  - `wt-next`: the enhancement branch.
  - `wt-upstream`: detached at `upstream/main`, read-only.
  - `wt-rollback-test`: dry-run only, now removed.

**Protected material.** None was touched:
- the user's staged files in the main index (`HANDOVER_REPORT.md`, `LEARNING_JOURNAL.md`, `learning-reports/…`);
- the modified `CLAUDE.md`;
- `m366 output/` (except one new timestamped report, as `CLAUDE.md` requires).

All work happened in a separate worktree, with path-limited commits.

## 2. Approved architecture (unchanged)

- Seven homepage entry points: Quick Start · CE: What & Why · How CE Works ·
  CE in Practice · CE Software & Integration · Project & Resources ·
  Commercial Services.
- Learning depths L1/L2/L3.
- Quick Start paths A/B/C, code-free (rule enforced by
  `test_quickstart_no_code.py`).
- Existing-page-first: **no new pages were created in this cycle**.

## 3. Scope from the backlog (`docs-five-stage-plan-20261113/12`, `15`)

| WP | Backlog scope | Master prompt | Reconciled scope this cycle |
|---|---|---|---|
| WP-6 | `quick_api` components and executed examples (3a); troubleshooting as single owner, each entry reproduced (3b); notebook verification and links (3c) | §5 A–C | All three; library code untouched |
| WP-13 | Landing intro and ordered cards; regulation card relabel; V-2 placement; phone table on `what-is-ce` | §6 (seven-question progression, calibration vs accuracy, example, limits) | Landing, reading order, relabel, `what-is-ce` additions and phone tables. **V-2 BLOCKED**: its planned home is the unapproved new page `explainable-ai` (D-25) |
| WP-14 | Landing "read in this order" with levels; V-8 reuse; telemetry section → link; phone tables on `calibration_methods`, `ce_workflow` | §7 (chain task → mode → method → output → assumptions; distinctions; V-6 check) | All; the chain and the distinctions go into `ce_workflow` (existing owner), not a new page. **V-4 and V-7 not in scope** (WP-4, WP-3) |

## 4. Conflicts recorded (not silently resolved)

| # | Conflict | Resolution |
|---|---|---|
| C-1 | Backlog: WP-13/14 "may not start before separate PO approval". Master prompt authorises them. | The master prompt is the later, explicit PO decision; proceeded |
| C-2 | Backlog: WP-13 depends on WP-2 (new page) and WP-14 on WP-3/WP-4 (new page, new figure). | Implemented the parts that do not need those pages; recorded the gaps (`06`) |
| C-3 | Prompt 3c says to link notebooks on the Beta repository. The task pages link the official repository. | Kept the official URLs: the five linked notebooks are byte-identical to the Beta copies, and the official URL is more durable |
| C-4 | Plan `02` §2.3 places "How Explanations Are Built" at `explanation_structures`. That page documents internal data structures. | Linked the conceptual owner (`ce_workflow` § How an explanation is built); `explanation_structures` stays reference material |
| C-5 | `07` §1 cites a 4-failure baseline for the full suite | Not applicable: no `src/` or dependency change; the docs suite and the affected integration smoke test were run |

## 5. Unresolved decisions carried forward

D-23 (sync Beta `src/` with official `main`), D-24 (promotion, see `00`),
D-25 (new pages), D-13 (fragment-page policy), the author answers for
SR-01…SR-16 and N-01…N-05, and the new D-26…D-29 (`09`).

## 6. Dependencies used

WP-6 → WP-13 → WP-14, as in the backlog's recommended sequence. WP-13 (L1)
was written before WP-14 (L1 → L3), so the deeper pages could refer to wording
that was already settled. Scientific reconciliation followed each WP; full
validation came at the end.
