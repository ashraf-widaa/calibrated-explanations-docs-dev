# Page migration map

All URLs are preserved; one page becomes a redirect stub. No page was deleted.

| Previous location | New location | Change |
|---|---|---|
| `get-started/index` | same | Rewritten as the three-path landing |
| `get-started/ml-foundations` ("Step 1: Machine learning basics") | same, "A1 · Machine learning essentials" | Retitled; Path A framing; next → `why-ce` |
| — | `get-started/why-ce` | **New** (A2) |
| `get-started/quickstart_walkthrough` | same (B) | Regenerated with question cues, disclaimer, mistakes, Path C links |
| `get-started/ce-tasks-and-modes` ("CE tasks and outputs") | same, "C1 · Tasks, modes and capabilities" | Four-term table, at-a-glance table, compatibility checks merged in |
| `get-started/quickstart_classification` | same (C2) | Real output, interpretation, mistakes |
| `get-started/quickstart_regression` | same (C3) | Real output, interpretation, mistakes |
| `get-started/quickstart_guarded` | same (C4) | Reframed as explanation configuration; real output; mistakes |
| — | `get-started/apply-to-your-data` | **New** (C5) |
| `getting_started_60s` | stub → `get-started/ce-tasks-and-modes.html#choosing-your-workflow` | Content merged into C1; orphan page with meta refresh and a link |
| `foundations/concepts/ce_workflow` | same | Mermaid diagram replaced by the workflow figure |

## Content moved

| Content | From | To |
|---|---|---|
| "CE in 60 seconds" comparison | landing table | `why-ce` running example |
| Mode decision tree | landing, 60-second page | C1 "Choosing your workflow" |
| Model compatibility | 60-second page | C1 "Choosing your workflow", C5 "Four checks" |
| Onward routes (methods, integration, practitioner) | landing "After the Quick Start" | walkthrough "Where to go next", C5 "Next" |

## References updated

`docs/appendices/rtd_tier_map.md` (new pages; stub marked), `README.md`
(documentation link now points to the Quick Start), tests in
`tests/docs/get_started/`.
