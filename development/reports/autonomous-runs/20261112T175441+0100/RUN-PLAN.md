# Autonomous run 2 — 20261112T175441+0100 — plan

**Started:** 2026-11-12 17:54:41 (UTC+01:00)
**Continues:** run 1 (`../20261112T100852+0100/`)
**Mission:** substantive content quality, not navigation: learning levels 1–3 in every entry point.

## Environment facts

| Fact | Consequence |
|---|---|
| `git push*` is still denied in `.claude/settings.json` (B-01) | Validated local commits; the PO pushes. The deployment is verified after the PO's push only |
| The package is importable with `PYTHONPATH=src`; a Jupyter kernel is available; the walkthrough generator reproduces the published page byte-for-byte | The walkthrough can be rewritten and regenerated safely |
| Run 1 is live (Stage 00) | Run 2 starts from a verified published baseline |

## Stage plan

| Stage | Focus | Evidence base |
|---|---|---|
| 00 | Deployment verification | Read the Docs API, live pages |
| 01 | Quick Start: ten-section teaching walkthrough; explanation basics; learning-path map; executable checks | Teaching-first specification `learning-reports/quickstart-walkthrough-audit/03`, `04`, `05` rev. 2; source code |
| 02 | CE: What & Why: a real "What is CE" page (problem, contribution, guarantees, non-guarantees, when to use, comparisons) | Original CE pages, CE papers, semantics |
| 03 | How CE Works: learning pathway (L1 → L3) across workflow, Venn–Abers, CPS, modes, explanations, guarantees | ADD-1, semantics, original pages, papers |
| 04 | CE in Practice: from simple example to reproducible application; evaluation methodology; common mistakes | Executed examples, original guides |
| 05 | Foundations and references | Claims register, citing |
| 06 | Repository and research assets | Run 1 AD-01–AD-07 |
| 07 | Reader journeys | Built site |
| 08 | Validation | Gates plus full suite |

## Rules carried over

- No change to disputed claims (SR-01–SR-16); qualified wording plus a register entry.
- Numbers on pages come from executed code.
- One commit per stage.
- Do not touch the PO's unrelated files.
