# Autonomous run 20261112T100852+0100 — Run plan

**Started:** 2026-11-12 10:08:52 (Europe/Stockholm, UTC+01:00)
**Agent:** Claude Code (session-bound; no persistent background executor is configured, so the run proceeds sequentially in one session and stops when the session ends)
**Authority:** PO master instruction "CE Beta — Autonomous documentation, scientific content & GitHub architecture improvement program"

## Environment facts that shape the plan

| Fact | Evidence | Consequence |
|---|---|---|
| Authorized repository | remote `docs-dev` = `https://github.com/ashraf-widaa/calibrated-explanations-docs-dev.git`; `upstream` (official CE) is fetch-only (`DISABLED_fetch_only` push URL) | All commits target the Beta repository only |
| **`git push` is denied** | `.claude/settings.json` → `permissions.deny` contains `Bash(git push*)`; CLAUDE.md §2: "Do not bypass permission constraints" | **Push and publication are blocked for the agent.** Every stage ends with a validated local commit; the PO pushes. This is recorded as a blocker, not bypassed |
| Beta publication | Read the Docs project `calibrated-explanations-beta` builds Beta `main` on push (L06 records) | Publication happens when the PO pushes; the agent verifies the live site afterwards only if a push has occurred |
| Starting state | branch `docs-dev/l07-homepage` at `cbcccdfe` (Beta main `e964a79c` + glossary G-P1/G-P2), with the approved homepage implemented but uncommitted | Stage 02 commits the validated homepage |
| Unrelated local changes | `LEARNING_JOURNAL.md`, `learning-reports/L05-stage2D-implementation-report.md` (modified); 100+ untracked reports in `learning-reports/` | Never staged, moved or deleted |
| Local toolchain | `C:\Python313` has Sphinx, pytest, Playwright; `.venv` lacks Sphinx; `ruff` not installed | Strict build: `C:\Python313\python.exe -m sphinx -W --keep-going -E`; tests: `pytest tests/docs …` |

## Branch strategy

- Stage 02 commits on `docs-dev/l07-homepage`.
- Stages 03+ continue on the run branch `docs-dev/autonomous-20261112`, created from the Stage 02 commit.
- One focused commit per stage (more if a stage has independent parts). Linear history, so the result fast-forwards onto Beta `main` (`e964a79c`).
- **To publish (PO):** `git push docs-dev docs-dev/autonomous-20261112:main`.

## Stage plan and scope rules

| Stage | Scope in this run | Guardrails |
|---|---|---|
| 01 Baseline | This plan, status file, baseline record | — |
| 02 Homepage | Commit the approved, validated homepage | Already validated (L07 report 09:59); re-run gates before commit |
| 03 Repository | Audit; ignore generated artifacts; establish the run-report location; record a target structure | No moves of inherited CE code or notebooks; no moves of untracked user material |
| 04 Foundations | Scientific claims register (all open author questions in one place); glossary weak-link retargeting (R2) and contextual cross-links (G-P3) | No change to disputed claims (Q-1–Q-7, S1–S8, ADD-1 R1–R11) |
| 05 Quick Start | Exits after the Quick Start; glossary route | The walkthrough is generated; no generator rewrite without an approved spec (none exists in the repo as "L07-QS") |
| 06 What & Why | Landing-card accuracy; remove audit wording | `compare.md` claims stay (author-blocked, Q-B1-4) |
| 07 How CE Works | Theory ↔ practice links (ADD-1); duplicate card; plot-colour fact (S8) only if verified in source | No guarantee wording changes |
| 08 CE in Practice | Accurate external-resource cards (Expert Hub, Decision Lab), notebook links verified on the official repository, card relabels | Links verified before adding |
| 09 Software | API page autodoc repair; version and install facts; configuration group on the landing page | Verify against `pyproject.toml`, CHANGELOG, source |
| 10 Project | Feedback route; researcher hub links; roadmap reader links; vision card | No change to the root `ROADMAP.md` (inherited file) |
| 11 Integration | Landing pages into the sidebar; full link and journey check | Strict build, navigation diff |
| 12 Final | Validation summary, quality matrix update, final report | — |

## Quality gates (every stage)

1. Strict Sphinx build: `-W --keep-going -E`, 0 warnings.
2. `pytest tests/docs tests/scripts/test_check_parameter_naming.py`, all passing.
3. Internal link and anchor check over the whole build: 0 broken.
4. Page-set comparison with the previous stage (no unintended removals).
5. Visual check (headless Edge) when layout or landing pages change.
6. `git diff --cached` review: only stage files staged; no secrets; unrelated files untouched.
