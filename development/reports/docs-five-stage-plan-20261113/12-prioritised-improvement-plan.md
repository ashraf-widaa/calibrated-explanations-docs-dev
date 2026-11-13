# 12 — Prioritised improvement plan (Deliverable F)

**Revision 3:** WP-1 and WP-2 revised, D-12 withdrawn, D-16 and D-17 added, per `13-architecture-reconciliation.md` (binding).

Supersedes the phase/work-package split in `05` where they differ (05 keeps
the phase framing; this file is the authoritative WP list). Effort: S / M / L
relative (S ≈ one or two pages, no figure; M ≈ several pages or one figure or
generator; L ≈ new page with generated real content, or a cluster).

All WPs: no push; one branch per WP; gates and rules from `07`; author-review
items **[S]** are marked, never resolved.

---

### WP-1 — Quick Start A/B/C improvements and "Where should I go next?" · P1 · M

- **Objective.** Keep Paths A/B/C (structure, order, labels); improve
  orientation and navigation so every reader can leave the Quick Start at
  their level and goal.
- **Affected pages.** `docs/get-started/index.md`; end-of-page navigation
  lines on `ml-foundations.md`, `why-ce.md`, `ce-tasks-and-modes.md`,
  `quickstart_{classification,regression,guarded}.md`, `apply-to-your-data.md`,
  `quick_api.md`; walkthrough via `scripts/docs/build_quickstart_walkthrough.py`
  (regenerate); `tests/docs/get_started/test_quickstart_continuity.py`
  (extend; the A/B/C landing tests stay).
- **Dependencies.** D-11, D-16, D-17.
- **Changes.** (1) Landing: "Where should I go next?" with the six other
  entry points (one line each, existing landing pages as targets); figure
  per D-16 with a link to `why-ce`; cards stay A/B/C (no reading-level
  labels). (2) Every Quick Start page: **Next** (path order), **Go deeper**
  (L3 owner for the concepts on that page — `calibration_methods` section,
  `calibrated_interval_semantics` mode, `explanation_structures`), **See
  also** (across), **Before this** (prerequisite). (3) ml-foundations: fix
  the stale A6 pointer. (4) Walkthrough: "Optional A/B/C" → "Extra 1/2/3";
  "Go deeper" after §5 and §6; next-steps table rows for the six entry
  points.
- **Scientific verification.** Each "Go deeper" target must actually treat
  the concept at L3 (check the section anchor exists and matches the
  mode); no new claims.
- **Acceptance.** A/B/C cards, order and labels unchanged; six entry-point
  links resolve; every Quick Start page has Next and Go deeper (Before this
  where a prerequisite exists); no "Optional A/B/C" wording remains;
  continuity, journeys, navigation, homepage and glossary tests pass;
  walkthrough numbers unchanged; 390/1440 light/dark check.
- **Risks.** Link lines must stay short (orientation, not repetition);
  regeneration must keep the PROSE guard green.

### WP-2 — Foundations: AI systems, black boxes, explainable AI · P1 · L

- **Objective.** Complete Stage 1 (concepts 1, 2, 8, 9 in `10`).
- **Affected pages.** `get-started/ml-foundations.md` (§A0 AI systems vs
  models; rule-based vs ML in A1; A7 kept short with a "Go deeper" link; A6
  shortened to a bridge to `why-ce`, anchor kept — `13` R-8); **new**
  `docs/explainable-ai.md`; `docs/index.md` (What & Why toctree);
  `sections/what-and-why.md`; glossary "Taught in" links; tier map.
- **Dependencies.** WP-1; D-3.
- **Changes.** As 06 Prompt 2a (rev. 3); keep label `why-predictions-are-not-enough`; no material removed from Path A beyond the duplicated A6 text.
- **Scientific verification.** Definitions against standard sources; citations
  only with resolvable DOI/arXiv; S3/S4/S8 wording tests.
- **Acceptance.** Concepts 1, 2, 8, 9 have L1 coverage; no broken anchors.
- **Risks.** Inbound links to A6/A7; scope creep into a general AI textbook
  (cap the page at core needs for CE).

### WP-3 — Calibration and uncertainty intuition (L1 owner) · P1 · L

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

### WP-9 — L1↔L3 bridges and research pathway · P2 · M

- **Objective.** Deeper/backward links (Stage 2 ↔ Stage 4); research history;
  labelled open questions; an L1 bridge for marginal vs conditional coverage
  (concept 34) inside `calibration_intuition` or `conditional_calibration`.
- **Affected pages.** 06 Prompts 4a, 4c; `foundations/how-to/conditional_calibration.md`
  (one "Why conditional coverage" paragraph linking calibration_methods).
- **Dependencies.** WP-3; author answers for SR-02 wording.
- **Acceptance.** Journey edges in `tests/docs/test_reader_journeys.py`.

### WP-10 — Contributor path · P2 · S–M

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
out early because several later WPs wait on answers; beginner-facing concepts before
advanced and contributor material; housekeeping last.

## New decisions (in addition to D-1…D-10 in `00-README.md`)

| ID | Decision | Recommendation |
|---|---|---|
| D-11 | Quick Start toctree holds only Quick Start-owned pages, in the current order and labels; pages owned elsewhere are linked, not duplicated in the sidebar | Approve |
| D-12 | ~~Replace "Path A/B/C" labels with "Stage n"~~ **Withdrawn (rev. 3)** | — |
| D-13 | Policy for the 32 non-runnable fragment pages: (a) leave as fragments with a one-line "assumes `explainer` from …" note, or (b) make each self-contained and tested | (a) now, (b) for pages on the Stage 1–3 path |
| D-14 | Send the author-review sheet (WP-8) before WP-3 starts | Approve |
| D-15 | `ce_workflow` gets a new internal-mechanism figure and stops reusing the comparison figure | Approve |
| D-16 | Quick Start landing figure: keep smaller (≤ ~560 px) with a link to `why-ce`, or remove | Keep smaller |
| D-17 | Rename the walkthrough's "Optional A/B/C" to "Extra 1/2/3" | Approve |
