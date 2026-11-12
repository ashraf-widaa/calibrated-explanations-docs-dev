# Quick Start content audit (before v3)

State at `e5fe7c23` (end of autonomous run 2).

| Page | Role before | Problems found |
|---|---|---|
| `get-started/index.md` | Landing | Long: a "CE in 60 seconds" table, a mermaid flowchart, a learning-path table, a "where each idea is taught" table, task quickstarts, onward routes, setup and help. No clear entry by reader goal; it read in well over 3 minutes. |
| `get-started/ml-foundations.md` | "Step 1" | Good content (A1–A7); labelled as step 1 of a single linear path. |
| `get-started/ce-tasks-and-modes.md` | "Step 2: CE tasks and outputs" | Good per-mode semantics (PO-reviewed X2 wording) and capability table, but the four distinct concepts (prediction task, CE mode, calibration method, explanation configuration) were not separated; no compact mode summary; compatibility checks lived on a separate page. |
| `get-started/quickstart_walkthrough.md` | Executed walkthrough | Strong and verified, but no explicit question for each section, no disclaimer on the medical dataset, no "common mistakes", no route to applying CE. |
| `quickstart_classification.md`, `quickstart_regression.md`, `quickstart_guarded.md` | Task quickstarts | Code only: no outputs, no interpretation, no common mistakes. The guarded quickstart presented guarded explanations as "for classification", reading like a separate task. |
| `getting_started_60s.md` | 60-second decision tree | Duplicated the compatibility and mode choice of the tasks page; outside `get-started/`. |
| *(missing)* | — | No page on why CE is needed / conventional vs CE workflow; no guide to applying CE to one's own data; no workflow illustration. |

## Duplication found

- Mode choice: landing table, 60-second page and tasks page.
- Compatibility requirements: 60-second page and tasks page.
- "What CE adds": landing table and `what-is-ce`.
- Calibration split rules: landing, ML basics A5, walkthrough §2.
