# 14 — Quick Start no-code migration (revision 4)

**Binding PO requirement (2026-11-13).** Quick Start is a universal
orientation and navigation hub: **no code blocks and no mathematical
derivations** on the landing page **or** any Quick Start learning page. Paths
A/B/C are kept and improved; "Where should I go next?" links the other six
entry points; the five-stage curriculum stays out of visible navigation. Code
and maths live on canonical practical and scientific pages, linked from the
Quick Start. Nothing valuable is deleted.

Baseline: `24797f9a` (docs identical to Beta `main` `a55c7e9d`).

## 1. Inventory: what would be removed or relocated

Counted in source (fenced blocks; inline names counted separately):

| Quick Start page (toctree label) | `python` | output (`text`) | `bash` | Other assets | Code-dependent tests / tools |
|---|---|---|---|---|---|
| `get-started/index.md` (landing) | 0 | 0 | 0 | workflow figure (`<picture>`) | continuity landing tests; glossary single-link test; reader-journeys test (landing must link `quickstart_walkthrough`) |
| `get-started/ml-foundations.md` (A1) | 0 | 0 | 0 | 3 mermaid diagrams | — |
| `get-started/why-ce.md` (A2) | 0 | 0 | 0 | 2 SVG figures | figure-wiring test |
| `get-started/quickstart_walkthrough.md` (B) | **14** | 0 (outputs in generated blocks) | **1** | 1 generated PNG, mermaid 1, downloadable notebook `docs/_static/notebooks/quickstart_walkthrough.ipynb` | `scripts/docs/build_quickstart_walkthrough.py` (generates page + notebook; PROSE_NUMBERS guard); `test_walkthrough_content.py`; continuity sync tests; reader journeys |
| `get-started/ce-tasks-and-modes.md` (C1) | 0 | 0 | 0 | mode cards contain inline call expressions such as `predict_proba(x, threshold=t, uq_interval=True)` | continuity tests (four terms; `## Choosing your workflow` anchor used by the 60-second redirect) |
| `get-started/quickstart_classification.md` (C2) | **7** | **4** | **1** | plot PNG | `test_quickstart_examples_execute.py` (execution + output match); `build_quickstart_figures.py` |
| `get-started/quickstart_regression.md` (C3) | **6** | **5** | **1** | — | execution + output match |
| `get-started/quickstart_guarded.md` (C4) | **5** | **2** | **1** | plot PNG; fast-explainer admonition | execution + output match; `tests/unit/core/explain/test_guarded_explain_api.py` wording checks; figure script |
| `get-started/apply-to-your-data.md` (C5) | **8** | **7** | 0 | plot PNG; AI-assistant prompt (`text` block) | execution + output match; figure script; continuity AI-prompt test |
| `get-started/quick_api.md` (Quick API) | **4** | 0 | 0 | — | `tests/integration/test_doc_examples_smoke.py` asserts exactly 4 blocks and executes them |
| **Total** | **44** | **18** | **4** | | |

Inbound links to these pages exist on 12 docs pages (concept pages,
`evaluate_ce`, `practitioner/index`, `tasks/capabilities`, research and
governance pages), 4 test files and 2 scripts. **No mathematical derivations
exist on any Quick Start page** (0 `{math}`/`$$`).

## 2. Strategy: relocate by toctree, keep every URL

Sphinx URLs follow the **file path**, not the sidebar. The lowest-risk way to
remove code from the Quick Start without breaking links, tests or generators
is to **keep the code-bearing files where they are** and move their **toctree
entries** to the canonical practical sections. Every URL, inbound link, test
path, generator path and notebook path stays valid.

| Page (URL unchanged) | Leaves Quick Start toctree → new sidebar home | Canonical function | Title change (proposal) |
|---|---|---|---|
| `get-started/quickstart_walkthrough` | CE in Practice → **Python tutorials** [N group] | Tutorial (L1→L2, executable) | "Python walkthrough: from a trained model to calibrated explanations" |
| `get-started/quickstart_classification` | CE in Practice → Python tutorials | Manual (L2) | "Classification tutorial" |
| `get-started/quickstart_regression` | CE in Practice → Python tutorials | Manual (L2) | "Regression tutorial" |
| `get-started/quickstart_guarded` | CE in Practice → Python tutorials | Manual (L2) | "Guarded explanations tutorial" |
| `get-started/apply-to-your-data` | CE in Practice → Python tutorials | Manual (L2) | unchanged |
| `get-started/quick_api` | Software & Integration → Development & Integration (before API reference) | Manual (L2 reference) | "Quick API: main calls" |

A small hub **`docs/tutorials/index.md` [N]** ("Python tutorials": who each is
for, prerequisites, what it produces, links) is added to the CE in Practice
toctree; it owns the group. Its URL is new; nothing existing moves.

## 3. What replaces the code in the Quick Start (code-free, verified content)

Paths stay A/B/C; their pages become code-free, but keep real, verified CE
results as **figures and tables** (not code or console blocks).

```text
Quick Start  get-started/index.md                    (no code; figure per D-16)
├── A1 · Machine learning essentials   get-started/ml-foundations   (unchanged URL; mermaid → accessible SVG, see 15 V-10)
├── A2 · Why CE                         get-started/why-ce           (unchanged)
├── B  · CE by example                  get-started/ce-by-example    [N] code-free, GENERATED
│      one case, the same run as the Python walkthrough: data roles; model alone vs calibrated;
│      the calibrated probability with its range; the factual explanation (table + plot); alternatives;
│      what we can and cannot conclude; "Run it yourself" → Python walkthrough + notebook
├── C1 · Tasks, modes and capabilities  get-started/ce-tasks-and-modes (code-free; inline call
│      expressions replaced by method names linked to Quick API — D-19)
└── C2 · Apply CE: the practical workflow get-started/apply-overview  [N] code-free
       steps (check fit → split → wrap and calibrate → predict → explain → evaluate → integrate),
       what each step produces, a checklist, common mistakes, which tutorial to run for which task,
       with links to the five Python tutorials and Quick API
Landing "Where should I go next?" → six entry points (as in 13 §5)
```

**Why B is generated.** `ce-by-example.md` is a second output of
`scripts/docs/build_quickstart_walkthrough.py` from the same executed cells:
its numbers, tables and plot are taken from the run, guarded by the existing
PROSE_NUMBERS check. The two pages cannot drift apart.

**Path C size.** C shrinks from C1–C5 to C1–C2 because C2–C5 were executable
tutorials; their content is preserved verbatim in CE in Practice. Alternative
(D-18): keep four short code-free C pages (one per tutorial: purpose, real
output figure, interpretation, link). Recommendation: C1–C2 — less
duplication, one owner per interpretation.

## 4. Files affected by WP-1 (revised)

| File | Change |
|---|---|
| `docs/get-started/index.md` | Landing: no code (install as a link, not a command); B card → `ce-by-example`; C card → `ce-tasks-and-modes` (unchanged); "Where should I go next?"; toctree: A1, A2, B, C1, C2 |
| `docs/get-started/ce-by-example.md` | **New, generated** (code-free) |
| `docs/get-started/apply-overview.md` | **New** (code-free) |
| `docs/get-started/ce-tasks-and-modes.md` | Replace call expressions in cards with method names + link; navigation lines |
| `docs/get-started/ml-foundations.md`, `why-ce.md` | Navigation lines; stale A6 pointer; (mermaid → SVG in WP-V) |
| `docs/tutorials/index.md` | **New** hub |
| `docs/index.md` | CE in Practice toctree gains `tutorials/index` (which lists the five moved pages); Software & Integration gains `get-started/quick_api` via `sections/development-integration.md` toctree |
| `docs/sections/in-practice.md`, `sections/development-integration.md` | One card/link each for the moved pages |
| `docs/get-started/{quickstart_walkthrough (via generator), quickstart_classification, quickstart_regression, quickstart_guarded, apply-to-your-data, quick_api}.md` | Titles and "Path …" wording → tutorial wording; navigation lines; **code unchanged** |
| `scripts/docs/build_quickstart_walkthrough.py` | Emit `ce-by-example.md` (code-free) in addition to the walkthrough and notebook; rename "Optional A/B/C" → "Extra 1/2/3" |
| `docs/appendices/rtd_tier_map.md` | New pages (tiers: `ce-by-example` Tier 1, `apply-overview` Tier 1, `tutorials/index` Tier 1 — each with a semantics pointer) |
| Tests | New `tests/docs/get_started/test_quickstart_no_code.py` (no fenced code, no `{code-cell}`, no `code-block`, no `{math}`/`$$` on every page in the Quick Start toctree and its landing); update continuity tests (landing B link, toctree, figure wiring), `tests/docs/test_reader_journeys.py` (beginner journey: landing → `ce-by-example` → walkthrough), `tests/docs/test_navigation.py` if it asserts sidebar groups; **unchanged**: execution, output-match, smoke and walkthrough-content tests (paths unchanged) |

## 5. Migration risks

| Risk | Mitigation |
|---|---|
| Returning readers look for the quickstarts under Quick Start | B and C2 link prominently to the tutorials; the tutorials hub is linked from the landing ("Where should I go next?" → CE in Practice) |
| Pages under `get-started/` now appear in another section (URL prefix vs sidebar mismatch) | Accept (URL stability wins); record; revisit only with redirects if the PO wants clean paths later (D-20) |
| The generated `ce-by-example` and the walkthrough drift | One generator, one run, PROSE_NUMBERS guard on both outputs; a test that every number on `ce-by-example` appears in the walkthrough output |
| Tier labels and STD-004 semantics notes | Moved pages keep their Tier 2 notes; new pages get Tier 1 pointers; tier map updated |
| Glossary single-link rule on the landing | "Where should I go next?" must not add a second glossary link |
| `get-started/index.md` loses the walkthrough link → journey test | Update the test deliberately (documented in the WP-1 report) |
| Inline code on C1 (method names) read as "code" | D-19: allow single identifiers, forbid call expressions and runnable snippets on Quick Start pages; test enforces fenced blocks only |
| Prev/next order changes for moved pages | Expected; check the tutorials sequence reads well in the CE in Practice order |

## 6. Decisions for this migration

| ID | Decision | Recommendation |
|---|---|---|
| D-18 | Path C after migration: C1 + C2 overview (recommended) or C1 + four short code-free C pages | C1 + C2 |
| D-19 | Inline code on Quick Start pages: allow single identifiers (e.g. `predict_proba`, `threshold`), forbid call expressions and runnable snippets | Approve |
| D-20 | Keep moved files at `get-started/…` URLs (recommended), or move files to `tutorials/…` with redirect stubs | Keep URLs |
| D-21 | Path B becomes the generated, code-free "CE by example"; the executable walkthrough becomes "Python walkthrough" under CE in Practice | Approve |
