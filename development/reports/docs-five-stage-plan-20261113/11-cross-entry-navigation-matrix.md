# 11 — Cross-entry navigation matrix (Deliverable D)

Canonical pages that should be reachable from more than one homepage entry
point. Direction: **F** forward · **D** deeper · **A** across · **B** backward.
"Link placement" names where the link goes (card, sidebar entry, or in-text
"Next/Go deeper/See it in practice/Before this" line). A page keeps **one
sidebar home** (its owner section); other sections link to it from cards or
text, not by repeating it in their toctree.

| Canonical page (owner section) | Linked from | Direction | Why useful | Link placement |
|---|---|---|---|---|
| `get-started/ml-foundations` (Quick Start) | What & Why | A | What & Why readers need the ML basics without entering the tutorial | Card "Understanding AI models" [V] |
| | `explainable-ai` [N], `why-ce`, glossary | B | Prerequisite for XAI and CE | "Before this:" line |
| `explainable-ai` [N] (What & Why) | Quick Start Stage 1 | F | Completes Stage 1 | Stage card |
| | `why-ce`, `what-is-ce`, `compare` | B | Conventional-XAI limits motivate CE and the comparison | "Before this:" line |
| `get-started/why-ce` (Quick Start) | What & Why landing, `what-is-ce`, `ce_workflow` | A / B | Canonical conventional-vs-CE comparison | Card or in-text link |
| `foundations/concepts/calibration_intuition` [N] (How CE Works) | Quick Start Stage 2, What & Why card "Can we trust AI outputs?", `why-ce`, `ce-tasks-and-modes`, `evaluate_ce` | F / A / B | First explanation of scores, calibration, uncertainty and interval meaning for every audience | Stage card; card; "Before this:" lines |
| `get-started/ce-tasks-and-modes` (Quick Start) | CE in Practice (tasks/index), Software (quick_api), How CE Works (`calibration_methods` §4) | A / B | One owner of task → mode → method → output | In-text links (tasks/index top line) |
| `foundations/concepts/ce_workflow` (How CE Works) | Quick Start Stage 2, `why-ce` "Read more" [V] | F / D | Internal mechanism after the comparison | Stage card; "Go deeper" |
| `foundations/concepts/calibration_methods` (How CE Works) | Quick Start Stage 4, `calibration_intuition`, walkthrough §5, `tasks/*` [V partly], researcher hub [V] | D | L3 owner for Venn–Abers and CPS | "Go deeper" lines |
| `foundations/concepts/calibrated_interval_semantics` (How CE Works) | All Tier 1/2 pages (STD-004) [V], quickstart semantics notes [V], `what-is-ce`, `calibration_intuition` | D | Canonical guarantees; never paraphrased | Semantics pointer (mandated) |
| `foundations/how-to/interpret_explanations` (How CE Works) | Quick Start Stage 2–3, quickstarts' "Reading the plot" [V], CE in Practice cards | A / D | One owner for reading rules, weights and plots | "See also" line |
| `get-started/apply-to-your-data` (Quick Start) | CE in Practice card "Use CE on your own data" (currently → integrate_with_pipelines) | A | One practical route for own data | Card target change |
| `foundations/how-to/integrate_with_pipelines` (Software) | C5, CE in Practice | D | Pipeline detail behind C5 | "Go deeper" line [V from C5] |
| `practitioner/evaluate_ce` (CE in Practice) | Quick Start Stage 3, C5 [V], walkthrough [V], `calibration_intuition` | F / A | Evaluation after applying | Stage card; "Next" |
| `get-started/troubleshooting` (Software) | Quick Start Stage 3, C5 table, quickstarts | A | One owner for errors | "Full list:" line |
| `get-started/quick_api` (Quick Start) | Software landing (API group), `api/index` | A | Components overview before signatures | Card / in-text |
| `foundations/concepts/architecture` (Software) | Quick Start Stage 5, contributor hub | F / A | Contributors start here after setup | Stage card; contributor path |
| `contributor/development_setup` [N] (Project) | Quick Start Stage 5, Software landing (Maintenance & Support) | F / A | Setup is both a contributor and developer need | Stage card; card |
| `researcher/future_work` (Project) | Quick Start Stage 4–5, `calibration_methods` §5, semantics "Further reading" | D | Open questions, labelled | "Go deeper" |
| `glossary/science`, `glossary/software` (Resources) | Every section landing (one link each, G-P3 rule) [V] | A | Definitions on demand | Existing single link per landing |
| External demo app | Quick Start Stage 3 [V], CE in Practice [V] | A | No-install exploration (not validation) | Card with disclaimer |

## Return paths

Every page reached from a Quick Start stage card ends with "Back to the Quick
Start roadmap (Stage n)" **only if** it is a Stage 1–3 core page; Stage 4–5
pages end with their own section's "Next". This keeps the roadmap visible for
beginners without making advanced pages tutorial-shaped.
