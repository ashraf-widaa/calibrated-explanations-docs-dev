# Run plan — CE Quick Start v3

- **Run start:** 2026-11-12 19:16 (+01:00, Stockholm)
- **Branch:** `docs-dev/autonomous-20261112` (starting HEAD `e5fe7c23`)
- **Target:** Beta repository `ashraf-widaa/calibrated-explanations-docs-dev`;
  Beta site <https://calibrated-explanations-beta.readthedocs.io/en/latest/>.
  The official CE repository is read-only and is not modified.

## Goal

Redesign and implement the Quick Start as three learning paths:

| Path | Question | Reader |
|---|---|---|
| A · Understand CE | Why is CE needed, and how does a CE workflow differ from a conventional one? | Newcomers, students, decision-makers |
| B · Learn CE by example | How does CE work in practice? | Anyone who wants to see CE run |
| C · Apply CE to your data | What does CE support, and how do I use it on my problem? | Practitioners |

## Stages

| # | Stage | Output |
|---|---|---|
| 1 | Audit the current Quick Start | QUICKSTART-CONTENT-AUDIT.md |
| 2 | Design the architecture and migration | QUICKSTART-ARCHITECTURE.md, PAGE-MIGRATION-MAP.md |
| 3 | Path A: landing, `why-ce`, ML essentials; workflow figure (PO's mid-run request) | Pages and SVG figure |
| 4 | Path C: tasks/modes/capabilities, quickstarts with real output, `apply-to-your-data` with AI-assistant prompt; retire the 60-second page | Pages, redirect stub |
| 5 | Path B: walkthrough generator (question cues, disclaimer, mistakes, Path C links); regenerate | Page, notebook |
| 6 | Science check against the evidence hierarchy and the open claims register | SCIENTIFIC-VERIFICATION.md |
| 7 | Validation: strict builds, executed examples, output-match tests, link checks, visual checks | VALIDATION-SUMMARY.md |
| 8 | Staged commits; push (or the push command if blocked); report | PUBLICATION-HISTORY.md, FINAL-REPORT.md |

## Constraints

- Never modify or push to the official CE repository; no force-push; no
  destructive Git operations; preserve unrelated and PO-owned work
  (`LEARNING_JOURNAL.md`, `learning-reports/`, untracked files).
- Do not change the CE library (`src/`).
- Do not resolve author questions SR-01 to SR-16; keep "under review" wording.
- Do not claim deployment success unless the live Beta site has been verified.
