# 13 — Architecture reconciliation (revisions 3 and 4)

**Date:** 2026-11-13. **Trigger:** PO instruction "Mandatory Architectural
Requirements — Preserve Previous Decisions". **Rule applied:** every conflict
with earlier planning is resolved in favour of that instruction. This file is
the authoritative decision record; other planning documents were updated to
match (see §4).

## 1. The approved architecture (binding)

1. **Three reading levels** — L1 conceptual, L2 practical, L3
   mathematical/scientific — on every major concept where relevant.
2. **Prerequisite-aware progression** — motivation, definition, mechanism,
   example, interpretation, assumptions, limitations, deeper treatment.
3. **Interconnected navigation** — forward, deeper, across, backward.
4. **Three integrated functions** — Tutorial, Academic Compendium, Technical
   Reference Manual — over shared canonical pages.
5. **Scientific accuracy** — task ≠ mode ≠ method ≠ output semantics ≠
   assumptions ≠ guarantees; claims verified against CE sources.
6. **Canonical ownership** — one authoritative location per major concept;
   elsewhere introduce briefly and link.
7. **Audience flexibility** — beginners, practitioners, researchers and
   developers enter at their level; no forced linear curriculum.

**Quick Start:** keep Paths A/B/C and improve their content and navigation;
concise orientation with links to deeper material; a **"Where should I go
next?"** section linking the other six homepage entry points; **no five-stage
curriculum as a competing Quick Start navigation**; A/B/C are **not** mapped
onto L1/L2/L3 unless the content supports it; no removal of advanced material
to simplify the introduction.

## 2. Verified purposes of Paths A/B/C (inspection, 2026-11-13)

| Path | Pages | Verified purpose | Reading levels present | Deeper links to L3 today |
|---|---|---|---|---|
| **A — Understand CE** | `get-started/ml-foundations.md` (226 lines, 0 code), `get-started/why-ce.md` (138 lines, 0 code) | Conceptual orientation: ML essentials, why CE is needed, how a CE workflow differs, how to read one output | **L1** (no code, no maths) | ml-foundations: 1 to `calibration_methods`, 1 semantics; why-ce: 0 to methods, 1 semantics |
| **B — Learn CE by example** | `get-started/quickstart_walkthrough.md` (709 lines, 14 code blocks, generated) | One case from code to verified output to interpretation; explains the Venn–Abers mechanism (§5) and explanation construction (§6) in words and numbers | **L1 → L2**, with an intuitive (not formal) treatment of mechanisms | 2 to `calibration_methods`, 2 semantics |
| **C — Apply CE to your data** | C1 `ce-tasks-and-modes.md` (concepts, mode choice, semantics summary, capability table); C2–C4 quickstarts; C5 `apply-to-your-data.md`; `quick_api.md` | Choose the task/mode, run it, read and check the output, integrate | C1 **L1–L2**; C2–C5 **L2**; quick_api L2 reference | C1: 1 to methods; C2–C5: 0 to methods (semantics pointer only) |

**Conclusion.** A/B/C are organised by **reader goal** (understand / see /
apply), not by reading level. A is L1 only; B spans L1–L2; C spans L1–L2. No
Quick Start page carries L3 content (no formal definitions or derivations),
which is correct for orientation; L3 must be reached by **deeper links**, and
those are missing on six of nine pages.

**Collision found.** The walkthrough's optional sections are titled "Optional
A/B/C" (regression, guarded, shaping explanations), which reads as Paths A/B/C.
Rename (e.g. "Extra 1/2/3") via the generator.

## 3. Conflicts with earlier planning and their resolution

| # | Earlier decision (document) | Conflict | Resolution (rev. 3) |
|---|---|---|---|
| R-1 | Quick Start landing = five-stage roadmap, Option B (02 rev. 2 §2.1; 12 WP-1; 06 Prompt 1; 00 D-1) | Competes with A/B/C | **Withdrawn.** Landing keeps the A/B/C cards; improved per §5 below |
| R-2 | Relabel pages and toctree "1 ·/2 ·/3 ·" and replace "Path A/B/C" wording (12 D-12; 06 Prompt 1) | Removes A/B/C | **Withdrawn.** Keep "A1, A2, B, C1–C5" labels and in-page "Path X" wording |
| R-3 | Quick Start toctree reordered by stage, C1 before B (06 Prompt 1) | Changes path order | **Withdrawn.** Order stays A1, A2, B, C1–C5, Quick API |
| R-4 | Quick Start toctree holds only Quick Start-owned pages (12 D-11) | Not a conflict (already true) | **Kept** as a rule: pages owned elsewhere are linked, not added to the Quick Start toctree |
| R-5 | Section landings carry "Stage n" lines (rev. 1 Prompt 1a; 00 D-2) | A second navigation layer | **Withdrawn.** Landings instead carry their own forward/deeper/across/backward links |
| R-6 | Separate `learning-journey.md` (rev. 1) | Competing structure | **Withdrawn** (already withdrawn in rev. 2) |
| R-7 | Remove the workflow figure from the landing (02 rev. 2; 06 Prompt 1) | "Concise orientation" vs "do not let the comparison dominate the landing" (earlier PO brief, not revoked) | **Decision D-16 (PO).** Recommended: keep a smaller figure (max ~560 px) as orientation with a link "full explanation: Why CE"; the explanatory text stays on `why-ce` |
| R-8 | Move ml-foundations A6–A7 entirely to `explainable-ai.md` (12 WP-2; 06 Prompt 2a) | Would remove material from Path A | **Revised.** A7 stays in Path A as a short L1 section; A6 is shortened to a bridge to `why-ce` (keeps the anchor `why-predictions-are-not-enough`); the new `explainable-ai.md` (What & Why) owns black boxes, transparency and the limits of XAI at full depth; A1 links to it as "Go deeper / across" |
| R-9 | Five stages as a navigation over sections (02 rev. 2 title, 10 "Stage" column, 11 "Stage cards") | Must not become a competing navigation | **Re-scoped.** The five-stage list survives only as a **planning aid** for ordering concepts (curriculum bands in 10). It does not appear in navigation, page labels or landing pages |
| R-10 | WP order starting with "Quick Start roadmap" (12) | Depends on R-1 | **Revised.** WP-1 becomes "Quick Start A/B/C improvements and 'Where should I go next?'" |
| R-11 | Remove duplicated "why predictions are not enough" text | Compatible | **Kept**, applied via R-8 |
| R-12 | Treat B as "L2" and A as "L1" anywhere | Not supported for B and C (§2) | **Rule:** never label paths with levels; label **sections** with L1/L2/L3 cues only where content supports it |

All other earlier decisions (D-3 … D-10, D-13 … D-15) are compatible and stay.

## 4. Documents updated in revision 3

`00-README.md` (decisions), `02-target-information-architecture.md` (rev. 3:
§1, §2.1, §3), `03-content-migration-matrix.md` (Quick Start rows),
`05-phased-implementation-roadmap.md` (banner, Phase 1), `06-implementation-prompts.md`
(Prompt 1 replaced; Prompt 2a adjusted), `08` (Quick Start target line),
`09` (Quick Start row), `10` (column renamed to curriculum band),
`11` (Quick Start links), `12` (WP-1, WP-2, decisions).

## 5. Quick Start target (rev. 3)

```text
get-started/index.md  "Quick Start — Understand, Explore and Apply CE"
├── Short definition of CE (unchanged)
├── Where CE fits ............ figure per D-16 + one sentence + link "Why CE explains it"
├── Choose your path ......... cards A · Understand CE, B · Learn CE by example, C · Apply CE to your data
│                              each card: purpose, audience, what you will be able to do, starting page
│                              (no reading-level labels on cards)
├── Recommended order A → B → C; each path stands alone (unchanged)
├── Before you start ......... install, Quick API, glossary (single link), API reference, semantics pointer, demo
├── Where should I go next? .. [N] six links, one line each:
│     CE: What & Why (why trust is hard, what CE adds) · How CE Works (methods, guarantees, L3)
│     · CE in Practice (demos, task guides, evaluation, playbooks) · CE Software & Integration (install, API,
│     integration, troubleshooting) · Project & Resources (research, glossary, contributing)
│     · Commercial Services (commercial support, separate from the open-source library)
└── toctree (unchanged order and labels): A1 · A2 · B · C1 · C2 · C3 · C4 · C5 · Quick API
```

Path-level improvements (content and navigation, no structural change):

- **Every Quick Start page** ends with the four navigation lines where they
  apply: **Next** (next page in its path), **Go deeper** (L3 owner:
  `calibration_methods`, `calibrated_interval_semantics`,
  `explanation_structures`), **See also** (examples/reference across
  sections), **Before this** (prerequisite page). Six pages currently lack any
  deeper link to the methods page.
- **Path A:** add AI systems vs models and rule-based vs ML (A1); keep A7 (L1)
  with a deeper link to `explainable-ai`; shorten A6 to a bridge (R-8); add a
  deeper link from `why-ce` to `calibration_methods` and to the new
  `calibration_intuition` (How CE Works).
- **Path B:** rename "Optional A/B/C" → "Extra 1/2/3" (generator); add "Go
  deeper" lines after §5 (methods §2) and §6 (explanation construction); its
  "Where to go next" table gains rows for the six entry points.
- **Path C:** C2–C5 each get one "Go deeper" line (methods section for their
  mode) and "Before this" → C1; C1 links the new `calibration_intuition` for
  bounds vs intervals and confidence vs coverage; quick_api becomes the
  components overview (WP-6).

## 6. Revision 4 (2026-11-13) — Quick Start without code; all seven entry points

**New binding requirements.** (1) Quick Start — landing **and** learning
pages — contains **no code blocks and no mathematical derivations**, yet gives
a meaningful big picture (motivation, capabilities, task/mode distinctions,
conceptual workflow, reading outputs). (2) L1/L2/L3 progression and the four
navigation directions everywhere. (3) All seven entry points are improved
(purpose, landing intro, hierarchy, depth, visuals, cross-links,
accessibility, mobile). (4) Visuals explain relationships; each has a purpose,
readable labels, alt text and accurate terms. (5) Claims verified; open
questions to authors. (6) WP-1 first; other entry points planned only.

| # | Earlier statement | Conflict | Resolution (rev. 4) |
|---|---|---|---|
| R-13 | Quick Start Path B = executable walkthrough; Path C = C1–C5 executable quickstarts (rev. 3 §5) | Code blocks on Quick Start pages | The six code-bearing pages leave the Quick Start **toctree** (files and URLs unchanged) and join CE in Practice → *Python tutorials* (five pages) and Software & Integration (Quick API). Path B becomes the generated, code-free *CE by example*; Path C becomes C1 + C2 *Apply CE: the practical workflow* (D-18, D-21). Detail: `14` |
| R-14 | "Each Quick Start page ends with Next / Go deeper / See also / Before this" (rev. 3) | Compatible | Kept; "See also" on Quick Start pages now includes the matching Python tutorial |
| R-15 | WP-1 = navigation-only change (rev. 3) | Too narrow | WP-1 = no-code migration + navigation (`12` WP-1 rev. 4) |
| R-16 | "Inline call expressions" on C1 cards | Code on a Quick Start page | D-19: single identifiers allowed; call expressions replaced by method names linked to Quick API |
| R-17 | Entry points other than Quick Start covered by WP-2…WP-12 only | Requirement (3) asks for landing, hierarchy, visual and mobile work per section | New WP-13…WP-18 (`15`) |
| R-18 | Earlier rule "examples are executed and shown with real output" on Quick Start | No code on Quick Start | Real outputs stay — as figures and tables on code-free pages, generated from the same runs; executable code moves with its tests |

Quick Start target (rev. 4) supersedes §5's tree:

```text
get-started/index.md — definition · Where CE fits (figure, D-16) · cards A/B/C · order · Before you start (links)
                       · Where should I go next? (six entry points) — no code
├── A1 · Machine learning essentials   get-started/ml-foundations
├── A2 · Why CE                         get-started/why-ce
├── B  · CE by example                  get-started/ce-by-example      [N, generated, code-free]
├── C1 · Tasks, modes and capabilities  get-started/ce-tasks-and-modes
└── C2 · Apply CE: the practical workflow get-started/apply-overview   [N, code-free]
```
