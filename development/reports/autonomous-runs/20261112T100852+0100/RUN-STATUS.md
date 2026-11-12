# Run status — 20261112T100852+0100

**Resume rule:** read this file, then `git log docs-dev/autonomous-20261112`, then the latest stage report.

**Branch:** `docs-dev/autonomous-20261112` (linear; Beta `main` `e964a79c` is an ancestor, so publication is a fast-forward).

| Stage | Status | Commit | Pushed | Report |
|---|---|---|---|---|
| (pre-run) Glossary G-P1, G-P2 | complete | `9aea4f47`, `cbcccdfe` | no | `learning-reports/2026-11-12_0730_…`, `_0848_…` |
| 01 Baseline | complete | in `802bf8cc` | no (B-01) | STAGE-01-BASELINE-20261112T1012.md |
| 02 Homepage | complete | `802bf8cc` | no (B-01) | STAGE-02-HOMEPAGE-20261112T1020.md |
| 03 Repository | complete | `d418d106` | no (B-01) | STAGE-03-REPOSITORY-20261112T1030.md |
| 04 Foundations | complete | `258b65c6` | no (B-01) | STAGE-04-FOUNDATIONS-20261112T1045.md |
| 05 Quick Start | partially complete (onward routes done; teaching-first rewrite deferred) | `75cfddfa` | no (B-01) | STAGE-05-QUICKSTART-20261112T1105.md |
| 06 What & Why | partially complete (`compare.md` claims author-blocked) | `1ca82e60` | no (B-01) | STAGE-06-WHAT-WHY-20261112T1115.md |
| 07 How CE Works | partially complete (explanation construction author-blocked) | `f26e7024` | no (B-01) | STAGE-07-HOW-CE-WORKS-20261112T1130.md |
| 08 CE in Practice | partially complete (evaluation guide author-blocked) | `fc9bf5e4` | no (B-01) | STAGE-08-PRACTICE-20261112T1150.md |
| 09 Software | complete | `40f6a7bf` | no (B-01) | STAGE-09-SOFTWARE-20261112T1215.md |
| 10 Project | complete (vision page needs content) | `34ebe0ed` | no (B-01) | STAGE-10-PROJECT-20261112T1230.md |
| 11 Integration | complete | `6625df25` | no (B-01) | STAGE-11-INTEGRATION-20261112T1245.md |
| 12 Final validation | complete | (final records commit) | no (B-01) | STAGE-12-FINAL-VALIDATION-*.md, FINAL-REPORT.md |

**Deployment (15:19):** `b0b2cdc6` pushed by the PO; Read the Docs build #35840928 cancelled before Sphinx; site still at `e964a79c`. Canonical project: `calibrated-explanations-beta`; `calibrated-explanations-docs-dev` is redundant. Report: RTD-DEPLOYMENT-INVESTIGATION-20261112T1519.md.

**Blockers:** B-01 — push and publication are denied to the agent (`.claude/settings.json`).

**To publish:** `git push docs-dev docs-dev/autonomous-20261112:main`, then check Read the Docs project `calibrated-explanations-beta`.
