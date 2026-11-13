# 11 — Cross-entry navigation matrix (Deliverable D)

**Revision 4:** Quick Start pages link the Python tutorials (CE in Practice) and Quick API (Software & Integration) as **See also**; the moved pages link back to their Quick Start orientation page as **Before this** (`14`).

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
| `explainable-ai` [N] (What & Why) | Path A (ml-foundations A7) | D | Full treatment of black boxes and XAI limits after A7's short intro | "Go deeper" line |
| | `why-ce`, `what-is-ce`, `compare` | B | Conventional-XAI limits motivate CE and the comparison | "Before this:" line |
| `get-started/why-ce` (Quick Start) | What & Why landing, `what-is-ce`, `ce_workflow` | A / B | Canonical conventional-vs-CE comparison | Card or in-text link |
| `foundations/concepts/calibration_intuition` [N] (How CE Works) | Path A (`why-ce`), Path C (`ce-tasks-and-modes`), What & Why card "Can we trust AI outputs?", `evaluate_ce` | D / A / B | First explanation of scores, calibration, uncertainty and interval meaning for every audience | "Go deeper" / "Before this" lines; card |
| `get-started/ce-tasks-and-modes` (Quick Start) | CE in Practice (tasks/index), Software (quick_api), How CE Works (`calibration_methods` §4) | A / B | One owner of task → mode → method → output | In-text links (tasks/index top line) |
| `foundations/concepts/ce_workflow` (How CE Works) | `why-ce` "Read more" [V], Quick Start landing "Before you start" [V], walkthrough §6 | D | Internal mechanism after the comparison | "Go deeper" lines |
| `foundations/concepts/calibration_methods` (How CE Works) | Every Quick Start page where a method appears (why-ce, walkthrough §5, C1–C5; 6/9 lack it today), `calibration_intuition`, `tasks/*` [V partly], researcher hub [V] | D | L3 owner for Venn–Abers and CPS | "Go deeper" lines |
| `foundations/concepts/calibrated_interval_semantics` (How CE Works) | All Tier 1/2 pages (STD-004) [V], quickstart semantics notes [V], `what-is-ce`, `calibration_intuition` | D | Canonical guarantees; never paraphrased | Semantics pointer (mandated) |
| `foundations/how-to/interpret_explanations` (How CE Works) | Paths B and C (quickstarts' "Reading the plot" [V]), CE in Practice cards | A / D | One owner for reading rules, weights and plots | "See also" line |
| `get-started/apply-to-your-data` (Quick Start) | CE in Practice card "Use CE on your own data" (currently → integrate_with_pipelines) | A | One practical route for own data | Card target change |
| `foundations/how-to/integrate_with_pipelines` (Software) | C5, CE in Practice | D | Pipeline detail behind C5 | "Go deeper" line [V from C5] |
| `practitioner/evaluate_ce` (CE in Practice) | C5 [V], walkthrough [V], `calibration_intuition` | F / A | Evaluation after applying | "Next" line |
| `get-started/troubleshooting` (Software) | C5 table, quickstarts C2–C4 | A | One owner for errors | "Full list:" line |
| `get-started/quick_api` (Quick Start) | Software landing (API group), `api/index` | A | Components overview before signatures | Card / in-text |
| `foundations/concepts/architecture` (Software) | Contributor hub, Quick API ("See also") | F / A | Contributors start here after setup | Contributor path; "See also" |
| `contributor/development_setup` [N] (Project) | Quick Start "Where should I go next?" (via Project & Resources), Software landing | F / A | Setup is both a contributor and developer need | Card; landing line |
| `researcher/future_work` (Project) | `calibration_methods` §5, semantics "Further reading", researcher hub | D | Open questions, labelled | "Go deeper" |
| `glossary/science`, `glossary/software` (Resources) | Every section landing (one link each, G-P3 rule) [V] | A | Definitions on demand | Existing single link per landing |
| External demo app | Quick Start landing [V], CE in Practice [V] | A | No-install exploration (not validation) | Card with disclaimer |
| **The six other homepage entry points** | Quick Start landing "Where should I go next?" [N] | F / A | Readers leave the Quick Start at their level and goal | One line per entry point |

## Return paths

Quick Start pages end with "Next" in their own path (A1→A2→B→C1→…). Pages
owned by other sections end with their own section's "Next" and, where a
Quick Start page links to them as "Go deeper", a "Before this" line back to it.
No "stage" back-links (`13` R-5, R-9).
