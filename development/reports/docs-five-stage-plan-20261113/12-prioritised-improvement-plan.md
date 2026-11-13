# 12 — Prioritised improvement plan (Deliverable F)

Supersedes the phase/work-package split in `05` where they differ (05 keeps
the phase framing; this file is the authoritative WP list). Effort: S / M / L
relative (S ≈ one or two pages, no figure; M ≈ several pages or one figure or
generator; L ≈ new page with generated real content, or a cluster).

All WPs: no push; one branch per WP; gates and rules from `07`; author-review
items **[S]** are marked, never resolved.

---

### WP-1 — Quick Start as the five-stage roadmap (Option B) · P1 · M

- **Objective.** Turn the Quick Start landing into the concise five-stage
  roadmap with direct routes; relabel its own pages by stage; keep URLs.
- **Affected pages.** `docs/get-started/index.md`; in-page path labels in
  `ml-foundations.md`, `why-ce.md`, `ce-tasks-and-modes.md`,
  `quickstart_{classification,regression,guarded}.md`, `apply-to-your-data.md`,
  `quick_api.md`; walkthrough labels via `scripts/docs/build_quickstart_walkthrough.py`
  (regenerate); `tests/docs/get_started/test_quickstart_continuity.py` (landing
  tests currently assert cards A/B/C and the figure on the landing — rewrite
  them for five stages); fix the stale A6 pointer in ml-foundations.
- **Dependencies.** PO decisions D-11, D-12 (below). Stage cards may link only
  pages that exist; WP-2/3 add their pages to the cards when created.
- **Changes.** Five stage cards (Stages 1–3 "core", 4–5 "optional"), each:
  goal, prerequisites, ordered links; direct-routes list; install/API/glossary
  line; no workflow figure (it remains on `why-ce`); toctree labels "1 ·", "2 ·",
  "3 ·" for Quick Start-owned pages only.
- **Scientific verification.** None new (navigation only); keep the semantics
  pointer (STD-004 Tier 1).
- **Acceptance.** Landing readable in ≤ 3 minutes (≤ ~350 words of prose);
  five stages in order; every link resolves; continuity, journeys, navigation
  and glossary tests pass; 390/1440 light/dark layout check.
- **Risks.** Readers and tests depend on "Path A/B/C" wording; regenerating the
  walkthrough must stay number-identical (PROSE guard).

### WP-2 — Stage 1: AI systems, black boxes, explainable AI · P1 · L

- **Objective.** Complete Stage 1 (concepts 1, 2, 8, 9 in `10`).
- **Affected pages.** `get-started/ml-foundations.md` (§A0 AI systems vs
  models; rule-based vs ML in A1; A6–A7 moved out); **new**
  `docs/explainable-ai.md`; `docs/index.md` (What & Why toctree);
  `sections/what-and-why.md`; glossary "Taught in" links; tier map.
- **Dependencies.** WP-1; D-3.
- **Changes.** As 06 Prompt 2a; keep label `why-predictions-are-not-enough`.
- **Scientific verification.** Definitions against standard sources; citations
  only with resolvable DOI/arXiv; S3/S4/S8 wording tests.
- **Acceptance.** Concepts 1, 2, 8, 9 have L1 coverage; no broken anchors.
- **Risks.** Inbound links to A6/A7; scope creep into a general AI textbook
  (cap the page at core needs for CE).

### WP-3 — Stage 2: calibration and uncertainty intuition · P1 · L

- **Objective.** One L1 owner for concepts 11–14, 17, 29 (score vs probability,
  calibration, accuracy vs calibration vs confidence score vs uncertainty,
  probability bounds vs prediction intervals, confidence level vs coverage),
  with real generated figures.
- **Affected pages.** **new** `foundations/concepts/calibration_intuition.md`;
  **new** `scripts/docs/build_concept_figures.py`; `docs/index.md` (How CE
  Works order and labels, D-4); `sections/how-ce-works.md`;
  `sections/what-and-why.md` card; `why-ce.md`, `ce-tasks-and-modes.md`
  ("Before this" links).
- **Dependencies.** WP-1; D-4.
- **Changes.** As 06 Prompt 2b, plus two contrast tables (bounds vs intervals;
  confidence level vs coverage) that **link** the semantics page for exact
  statements.
- **Scientific verification.** [S] Coverage wording must reuse the PO-reviewed
  X2 text with its SR-02 marker; no new guarantee statements; numbers from the
  generator only.
- **Acceptance.** Concepts 11–14, 17, 29 have an L1 owner; figures real and
  reproducible; S5–S7.
- **Risks.** Paraphrasing guarantees (forbidden: link instead).

### WP-4 — Internal CE workflow figure; Why CE vs What CE Is ownership · P2 · M

- **Objective.** Distinguish the **internal** CE workflow from the
  conventional-vs-CE comparison; remove restated content between `why-ce` and
  `what-is-ce`.
- **Affected pages.** `foundations/concepts/ce_workflow.md` (replace the
  comparison figure with a new mechanism figure: calibration set → Venn–Abers
  / CPS → calibrated output; case → perturbed copies → calibrated predictions →
  weights and ranges); new SVG in `docs/_static/figures/`; `what-is-ce.md`,
  `why-ce.md` (06 Prompt 2c).
- **Dependencies.** WP-3 (links).
- **Scientific verification.** Mechanism must match `explanation_structures`
  and the walkthrough §6 description (code: `calibrated_explainer.py`, discretizer);
  mark any step tied to C-37 as simplified.
- **Acceptance.** Two distinct figures with distinct captions; no paragraph
  restated across why-ce/what-is-ce.
- **Risks.** Oversimplifying perturbation/discretisation.

### WP-5 — What & Why progression and comparison page · P2 · M

- **Objective.** Order the What & Why cards as a progression; rewrite
  `compare.md` as a design comparison.
- **Affected pages.** `sections/what-and-why.md`, `docs/index.md` (group
  order), `compare.md` (06 Prompt 4b).
- **Dependencies.** WP-2, WP-3; D-6.
- **Scientific verification.** [S] SR-05/SR-06 (comparison claims); remove
  "more stable rules"; cite method papers.
- **Acceptance.** Superiority-phrase test covers compare.md; cards ordered.
- **Risks.** Regulatory card wording (see WP-8).

### WP-6 — Using CE: components, troubleshooting, own data, notebooks · P1 · M

- **Objective.** Stage 3 completeness (concepts 23, 27, 30) and verified
  notebooks.
- **Affected pages.** `get-started/quick_api.md` (components + executed
  examples), `api/index.md` (one paragraph linking the overview),
  `get-started/troubleshooting.md`, `apply-to-your-data.md` (link),
  `sections/in-practice.md` (own-data card → C5; notebooks), `tasks/*.md`
  (notebook links).
- **Dependencies.** WP-1; D-5.
- **Changes.** 06 Prompts 3a, 3b, 3c.
- **Scientific verification.** Every call and error reproduced against `src/`.
- **Acceptance.** Execution and reproduction tests pass; only passing
  notebooks linked.
- **Risks.** Notebook failures (report only).

### WP-7 — Correct outdated and non-runnable code examples · P1 · M

- **Objective.** Fix the confirmed outdated examples and the ordering trap;
  set a policy for the 32 fragment pages.
- **Affected pages.** `get-started/ce_first_agent_guide.md`,
  `contributor/plugin-contract.md`, `contributor/extending/plugin-advanced-contract.md`,
  `practitioner/advanced/explanation_retrieval.md`,
  `foundations/how-to/configure_runtime.md`,
  `foundations/concepts/explanation_structures.md` (fence type); fragment pages
  per policy D-13.
- **Dependencies.** D-10, D-13.
- **Changes.** 06 Prompt 3d.
- **Scientific verification.** API behaviour from `src/` and tests only.
- **Acceptance.** Every corrected page executes in a test; divergence list for
  upstream.
- **Risks.** Divergence from official docs.

### WP-8 — Scientific wording and author-review package · P1 · M

- **Objective.** Neutralise wording where no author decision is pending, and
  assemble one review sheet for the rest.
- **Affected pages.** `tasks/classification.md:23,44,52`,
  `tasks/probabilistic_regression.md:81`, `tasks/regression.md:58`
  ("confidence levels"), `practitioner/playbooks/ensured-explanations.md`
  (epistemic/aleatoric table; "intervention recommendations"),
  `practitioner/playbooks/eu-ai-act-compliance.md:478` (coverage vs confidence
  "Venn-Abers guarantee — Covered"), `foundations/concepts/guarded_explanations.md`
  (state that `confidence` is a guard threshold).
- **Dependencies.** None for the sheet; edits follow 06 Prompt 3e rules.
- **Changes.** **New** author sheet
  `development/reports/docs-five-stage-plan-20261113/author-review-sheet.md`
  listing each [S] item: page:line, current text, issue, options, evidence —
  covering SR-01, 02, 03, 05, 06, 07, 08, 13, 14, 15, C-37 and the new items
  above. Wording edits only for items with no open SR id
  (`tasks/regression.md:58`, the guarded `confidence` clarification).
- **Scientific verification.** This WP **is** the verification step.
- **Acceptance.** Every [S] item in `08`/`10` appears on the sheet; no SR item
  resolved by the agent.
- **Risks.** Compliance-playbook claims have legal reading; route to authors
  and the PO.

### WP-9 — Stage 4 bridges and research pathway · P2 · M

- **Objective.** Deeper/backward links (Stage 2 ↔ Stage 4); research history;
  labelled open questions; an L1 bridge for marginal vs conditional coverage
  (concept 34) inside `calibration_intuition` or `conditional_calibration`.
- **Affected pages.** 06 Prompts 4a, 4c; `foundations/how-to/conditional_calibration.md`
  (one "Why conditional coverage" paragraph linking calibration_methods).
- **Dependencies.** WP-3; author answers for SR-02 wording.
- **Acceptance.** Journey edges in `tests/docs/test_reader_journeys.py`.

### WP-10 — Stage 5 contributor path · P2 · S–M

- **Objective.** Setup page, ordered hub, architecture reading guide.
- **Affected pages.** 06 Prompt 5.
- **Dependencies.** WP-7 (contract examples fixed first); D-7.

### WP-11 — Reference-manual housekeeping · P3 · M

- **Objective.** Owners for overlapping clusters; "Configuration &
  operations" group on the Software landing; sub-hub prose removed;
  `interpret_explanations` §4 telemetry → one link; terminology (C-31) incl.
  `calibration_methods` §4 heading; release notes pointer.
- **Affected pages.** 06 Prompts 6a, 6b; `sections/software-integration.md`;
  `sections/{software-foundations,development-integration,maintenance-support}.md`;
  `foundations/how-to/interpret_explanations.md`.
- **Dependencies.** D-8 (terminology), C-33 visibility decision.

### WP-12 — Integration and QA · P1 · M

- **Objective.** Walk all five stages and seven entry points; final gates and
  reports (06 Prompt 6c), including a regenerated `08`-style navigation tree.

## Recommended sequence

WP-1 → WP-8 (sheet, in parallel with WP-2) → WP-2 → WP-3 → WP-4 → WP-6 → WP-7
→ WP-5 → WP-9 → WP-10 → WP-11 → WP-12.

Rationale: the roadmap (WP-1) frames everything; the author sheet (WP-8) goes
out early because several later WPs wait on answers; Stage 1–3 (core) before
Stage 4–5 (optional); housekeeping last.

## New decisions (in addition to D-1…D-10 in `00-README.md`)

| ID | Decision | Recommendation |
|---|---|---|
| D-11 | Quick Start toctree holds only Quick Start-owned pages; pages owned elsewhere are linked from stage cards, not duplicated in the sidebar | Approve |
| D-12 | Replace "Path A/B/C, step n" labels with "Stage n" in pages, toctree and walkthrough generator | Approve |
| D-13 | Policy for the 32 non-runnable fragment pages: (a) leave as fragments with a one-line "assumes `explainer` from …" note, or (b) make each self-contained and tested | (a) now, (b) for pages on the Stage 1–3 path |
| D-14 | Send the author-review sheet (WP-8) before WP-3 starts | Approve |
| D-15 | `ce_workflow` gets a new internal-mechanism figure and stops reusing the comparison figure | Approve |
