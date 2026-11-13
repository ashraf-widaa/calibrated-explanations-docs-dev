# 06 — Claude Code implementation prompts

One prompt per work package (WP) in `05-phased-implementation-roadmap.md`.
Paste one prompt at a time; each ends with a stop condition. Every prompt is
self-contained; the **standard block** below is repeated inside each prompt,
so nothing has to be pasted separately.

**Prompt index (revision 2).** WP-1 → Prompt 1 · WP-2 → Prompt 2a · WP-3 → Prompt 2b (add the two contrast tables from 12 WP-3) · WP-4 → Prompt WP-4 (+ 2c) · WP-5 → Prompt 4b (+ reorder the What & Why cards) · WP-6 → Prompts 3a, 3b, 3c · WP-7 → Prompt 3d · WP-8 → Prompt WP-8 (+ 3e) · WP-9 → Prompts 4a, 4c · WP-10 → Prompt 5 · WP-11 → Prompts 6a, 6b · WP-12 → Prompt 6c. Prompts 1a and 1b of revision 1 (learning-journey page) are withdrawn.

Paths were discovered at baseline `a55c7e9d`. If a path no longer exists when
you run a prompt, the agent must stop and report it, not guess.

---

## Prompt 1 — Quick Start as the five-stage roadmap (WP-1)

```text
ROLE AND OBJECTIVE
You are a senior documentation architect and technical educator for the Calibrated Explanations (CE) Beta
documentation. Objective: turn the Quick Start landing into the concise five-stage roadmap (Option B) over
existing canonical pages, relabel Quick Start-owned pages by stage, and fix stale transitions. Do not create
docs/learning-journey.md. Do not change the homepage.

REPOSITORY AND SAFETY (standard block)
- Work only in the local Beta repository D:\Jönkoping\CE-Documentation-Redesign\calibrated_explanations
  (GitHub ashraf-widaa/calibrated-explanations-docs-dev, remote "docs-dev").
- Moffran/calibrated_explanations and https://calibrated-explanations.readthedocs.io are read-only references.
- Do not push. Do not change src/. No git reset --hard, git clean, force-push or file deletion.
- Preserve LEARNING_JOURNAL.md, learning-reports/, HANDOVER_REPORT.md, session-checkpoint-*.md and all other
  unrelated modified or untracked files; never stage them.
- Before editing: `git status`, `git branch --show-current`, `git rev-parse --short HEAD`, `date`; record them.
  Create branch docs-dev/wp-1-quickstart-roadmap from the latest Beta main (fast-forward only).
- Edit with the editor tools, not shell heredocs. *.svg/*.png are git-ignored (use git add -f for figures).
- Read development/reports/docs-five-stage-plan-20261113/02-target-information-architecture.md (rev. 2 §2.1),
  10-concept-curriculum-matrix.md, 12-prioritised-improvement-plan.md (WP-1) and 07 first.

SCOPE AND TARGET FILES
- docs/get-started/index.md (landing and its toctree).
- In-page path labels ("Path A, step 1", "Path C, step 3", "Path B of the Quick Start", …) in:
  docs/get-started/{ml-foundations,why-ce,ce-tasks-and-modes,quickstart_classification,quickstart_regression,
  quickstart_guarded,apply-to-your-data,quick_api}.md → "Stage n" wording.
- scripts/docs/build_quickstart_walkthrough.py (its "Path B" wording and links), then regenerate with
  `PYTHONPATH=src /c/Python313/python.exe scripts/docs/build_quickstart_walkthrough.py`; never edit
  docs/get-started/quickstart_walkthrough.md or the notebook by hand.
- docs/get-started/ml-foundations.md: fix the stale A6 sentence "The next page shows which tasks and outputs CE
  supports" (the next page is why-ce).
- tests/docs/get_started/test_quickstart_continuity.py: the landing tests assert cards A/B/C and the workflow
  figure on the landing; rewrite them for five stages (see ACCEPTANCE). Keep the generator/page/notebook sync
  tests and the figure-wiring test for why-ce and ce_workflow (remove only the landing entry from it).

REQUIRED CONTENT (landing)
- Title may stay. One short paragraph defining CE (keep current wording).
- Five stage cards (sphinx-design grid), in order; Stages 1–3 marked "core", 4–5 "optional". Each card: one-line
  goal, prerequisites, and an ordered list of links to EXISTING pages only, per 02 rev. 2 §2.1 (omit proposed
  pages explainable-ai/calibration_intuition/development_setup until they exist).
- "Direct routes" list: know ML → Stage 2; code now → walkthrough or C2/C3; have a model → C1 then C5;
  need the maths → Stage 4; contribute → Stage 5.
- "Before you start" line: install, Quick API, glossary (exactly one glossary link — glossary test), API reference,
  semantics pointer (STD-004 Tier 1 MUST), web demo.
- Remove the workflow figure from the landing (it stays on why-ce and ce_workflow).
- Toctree: only Quick Start-owned pages, labelled "1 · Machine learning essentials", "2 · Why CE",
  "2 · Tasks, modes and capabilities", "3 · Guided Python walkthrough", "3 · Classification quickstart",
  "3 · Regression quickstart", "3 · Guarded explanations", "3 · Apply CE to your own data", "3 · Quick API".
  Note the reorder: ce-tasks-and-modes moves before the walkthrough (Stage 2). Update every page's "Next"
  line to follow the new order.
- Footer "Entry-point tier: Tier 1."

SCIENTIFIC AND EDITORIAL REQUIREMENTS
- Navigation and labels only; no new claims. Keep the PO-reviewed wording in ce-tasks-and-modes.md untouched.
- Landing prose ≤ ~350 words (cards excluded).

EXCLUSIONS
- No new concept pages, no figures, no homepage or section-landing changes, no changes to pages owned by other
  sections.

VERIFICATION
- CE_DOCS_BETA=true /c/Python313/python.exe -m sphinx -W --keep-going -E -b html docs _build/wp1  (0 warnings)
- /c/Python313/python.exe -m sphinx -W --keep-going -E -b html docs _build/wp1-std  (0 warnings)
- PYTHONPATH=src /c/Python313/python.exe -m pytest tests/docs -q -p no:cacheprovider
- /c/Python313/python.exe scripts/docs/check_internal_links.py _build/wp1
- Walkthrough regenerated; PROSE_NUMBERS guard passes; diff is prose/link-only (no number changes).
- Headless Edge (Python Playwright, C:\Python313, no -I): landing at 390 and 1440 px, light and dark — no
  horizontal overflow; cards stack on phones.

ACCEPTANCE CRITERIA
- Tests assert: five stage cards in order with "core"/"optional" labels; every stage link resolves; direct-routes
  section present; one glossary link; semantics pointer; no workflow figure on the landing; toctree labels and
  order as specified; each Quick Start page's "Next" target equals the next toctree entry (or the next stage's
  first page).
- All gates pass; no "Path A/B/C" wording remains in docs/get-started or the generator.

FINAL REPORT
- development/reports/docs-five-stage-plan-20261113/phase-reports/<YYYY-MM-DD_HHMM>_wp-1.md (time from `date`):
  baseline, files changed, problems, changes, duplication removed, evidence, tests and results, screenshots
  checked, limitations, open decisions.

COMMITS
- (1) landing + labels + tests; (2) generator + regenerated walkthrough/notebook; (3) report. Attribution trailer
  as the session provides. No push; print: git push docs-dev docs-dev/wp-1-quickstart-roadmap:main
  (for the PO, after approval).

STOP CONDITION
- Stop after the report. Do not start the next WP until the PO approves WP-1.
```

---

## Prompt WP-8 — Author-review sheet and non-blocked wording

```text
ROLE AND OBJECTIVE
Scientific documentation reviewer. Objective: produce one author-review sheet for every unresolved scientific
or terminology item, and correct only the items that have no open author question.

REPOSITORY AND SAFETY (standard block)
- Local Beta repository D:\Jönkoping\CE-Documentation-Redesign\calibrated_explanations (remote "docs-dev");
  official CE read-only; no push; no src/ changes; no destructive git; preserve unrelated files; record status,
  branch, HEAD and `date`; branch docs-dev/wp-8-author-review; editor tools only.

SCOPE
- New: development/reports/docs-five-stage-plan-20261113/author-review-sheet.md. One row per item:
  ID (SR-xx / C-xx / new N-xx), page:line, current text (quoted), issue, evidence (paper, code path, test, page),
  options for the authors, recommended interim wording. Include at least: SR-01, SR-02, SR-03, SR-05, SR-06,
  SR-07 (aleatoric/epistemic: tasks/classification.md:44, tasks/probabilistic_regression.md:81,
  practitioner/playbooks/ensured-explanations.md table), SR-08 (counterfactual; ensured playbook line 3
  "more reliable intervention recommendations"), SR-13, SR-14, SR-15, C-37, and the new items:
  N-01 practitioner/playbooks/eu-ai-act-compliance.md:478 ("Empirical coverage vs. nominal confidence
  (Venn-Abers guarantee) — Covered"); N-02 tasks/regression.md:58 ("arbitrary confidence levels" for
  percentiles); N-03 CE's regression plot label "Prediction interval with 90.0% confidence" (library code —
  report only); N-04 guarded `confidence` parameter naming. Re-read each source line before quoting it.
- Edits (only items without an open SR id): tasks/regression.md:58 → coverage/percentile wording;
  foundations/concepts/guarded_explanations.md → one sentence that `confidence` is the guard's conformity
  threshold (= 1 − significance), not a confidence level for a prediction.

EXCLUSIONS
- Do not resolve any SR item; do not edit the compliance playbooks (route N-01 to authors and the PO).

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Gates (07 §1). Accept when every [S] item in 08 and 10 appears on the sheet. Report
  phase-reports/<…>_wp-8.md. Commits: sheet; edits; report. No push. Stop.
```

---

## Prompt WP-4 — Internal CE workflow figure and Why CE / What CE Is ownership

```text
ROLE AND OBJECTIVE
Technical educator and figure designer. Objective: give foundations/concepts/ce_workflow.md its own figure of
CE's internal mechanism (distinct from the conventional-vs-CE comparison on why-ce), then remove restated
content between why-ce and what-is-ce (see Prompt 2c below for the dedupe rules).

REPOSITORY AND SAFETY (standard block)
- As in Prompt 1; branch docs-dev/wp-4-internal-workflow from the latest approved WP branch.

SCOPE
- New SVG docs/_static/figures/ce-internal-workflow.svg (and a narrow variant if text would fall below ~11 px at
  390 px; switch with <picture> as on why-ce). Content: calibration set + trained model → Calibrate
  (Venn–Abers for classification; CPS for interval regression; CPS then Venn–Abers for probabilistic regression)
  → calibrated prediction with lower/upper value; explanation: discretise each feature with calibration data →
  rule for the case → substitute values from other bins → calibrated predictions → weight = difference, with
  range. Verify every step against src/calibrated_explanations (read only) and walkthrough §6; label simplified
  steps "simplified" where C-37 applies.
- Style: blue/orange palette and rules of docs/_static/figures/ce-in-ml-workflow.svg (transparent background,
  text inside filled shapes, <title>/<desc>, alt text), checked at 390/1440 light/dark.
- docs/foundations/concepts/ce_workflow.md: replace the comparison figure with the new one; caption names it
  "inside CE"; link why-ce for the comparison.
- Then apply Prompt 2c (why-ce vs what-is-ce dedupe).

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Gates; update tests/docs/get_started/test_quickstart_continuity.py figure-wiring test (ce_workflow now uses
  ce-internal-workflow.svg). Accept when the two figures are distinct and each mechanism step has a code/test
  reference in the report. Report phase-reports/<…>_wp-4.md. Commits: figure+page+test; dedupe; report.
  No push. Stop.
```

---

## Prompt 2a — Stage 1 completion: AI systems, black boxes and explainable AI

```text
ROLE AND OBJECTIVE
AI/ML educator and scientific reviewer for the CE Beta docs. Objective: complete Stage 1 (Foundations)
with accurate, beginner-level content: AI systems vs AI models, rule-based AI vs machine learning,
black-box models and transparency, what explainable AI (XAI) is and its limits. Remove the duplication
between ml-foundations A6/A7 and why-ce.

REPOSITORY AND SAFETY (standard block)
- Local Beta repository D:\Jönkoping\CE-Documentation-Redesign\calibrated_explanations (remote "docs-dev").
  Official CE repository/docs read-only. No push; no src/ changes; no destructive git; preserve unrelated
  files. Record git status, branch, HEAD, `date`. Branch docs-dev/phase-2a-foundations from the approved
  Phase 1 branch. Editor tools only. Read 02, 03, 07 in development/reports/docs-five-stage-plan-20261113/.

SCOPE AND TARGET FILES
- docs/get-started/ml-foundations.md: add a short section before A1 "AI systems and AI models" (a system
  = model + data pipeline + interface + people/processes; a model = the learned function); extend A1 with
  rule-based AI vs machine learning (hand-written rules vs rules learned from data; both exist today).
  Keep training vs inference (already in A1), A2-A5 unchanged. Move A6 and A7 out (below).
- New: docs/explainable-ai.md "Black boxes, transparency and explainable AI" (Tier 3), in the
  "CE: What & Why" sidebar group of docs/index.md after "Overview". Content: (1) why some models are hard
  to inspect (size, non-linearity, interactions) and some are not (small linear models, short trees) —
  never "all AI models are black boxes"; (2) transparency vs explainability; (3) what an explanation is:
  local vs global, attributions vs rules (moved from A7, keep its references Ribeiro et al. 2016 and
  Lundberg & Lee 2017 and the CE 2024 ESWA paper); (4) limits of XAI: explanations describe the model,
  not causes; different methods can disagree; no single method fits every model, task and question;
  explanations usually lack a reliability measure (moved from A6, last bullet); (5) bridge to Stage 2:
  link get-started/why-ce.
- Keep the MyST label (why-predictions-are-not-enough)= : move it with the A6 content so the
  "Can We Trust AI Outputs?" card in docs/sections/what-and-why.md still resolves; update that card text
  if its description no longer fits.
- docs/sections/what-and-why.md: add a card for the new page.
- Search all docs (and scripts/docs/build_quickstart_walkthrough.py) for links to ml-foundations anchors
  A6/A7 and to "ml-foundations" with section numbers (e.g. "section A5" is fine, "A7" must be retargeted);
  update them. Glossary "Taught in" links: retarget in docs/glossary/*.md if they point at A6/A7.
- docs/appendices/rtd_tier_map.md: add the page.

SCIENTIFIC AND EDITORIAL REQUIREMENTS
- Rules S1–S4, S8, S12 of 07 §2. Define each term before use. One running example: the breast-cancer case
  (walkthrough case 2). Cite only sources you can verify (DOI/arXiv links that resolve); do not invent
  citations. Mark editorial judgements as such.
- Figures: if you add one (optional: "transparent vs hard-to-inspect models" or "local vs global"), it must
  show a mechanism, follow the blue/orange palette of docs/_static/figures/ce-in-ml-workflow.svg, have
  <title>/<desc>/alt text, a transparent background with text inside filled shapes, and be checked at
  390/1440 px light/dark.

REUSE
- Reuse A6/A7 text (edit, do not rewrite from scratch). Reuse the glossary definitions in
  docs/glossary/science.md for terms that exist there.

EXCLUSIONS
- No calibration intuition content (WP 2b). No CE API code. Do not change why-ce beyond links.

VERIFICATION
- Both strict builds (0 warnings); pytest tests/docs; link checker; visual check of the new page.
- New tests in tests/docs/test_explainable_ai.py: page reachable from the sidebar and the What & Why
  landing; label why-predictions-are-not-enough resolves (exists in exactly one page); blocked phrases
  ("all AI models are black boxes", "proves", "causes the outcome") absent from ml-foundations and
  explainable-ai.

ACCEPTANCE CRITERIA
- ml-foundations no longer contains A6/A7; explainable-ai owns them; no broken anchor; glossary tests pass;
  S1–S4/S8 hold; all gates pass.

FINAL REPORT
- phase-reports/<YYYY-MM-DD_HHMM>_phase-2a.md with standard sections plus an evidence table per new claim.

COMMITS
- (1) ml-foundations + explainable-ai + links + tests; (2) report. Attribution trailer. No push.

STOP CONDITION
- Stop for PO review before WP 2b.
```

---

## Prompt 2b — Calibration and uncertainty intuition with real figures

```text
ROLE AND OBJECTIVE
AI/ML educator and Python documentation engineer. Objective: one Stage 2 page that builds intuition for
scores vs probabilities, calibration, reliability and uncertainty, with figures generated from real data
and CE output, before readers meet the formal semantics.

REPOSITORY AND SAFETY (standard block)
- Local Beta repository D:\Jönkoping\CE-Documentation-Redesign\calibrated_explanations (remote "docs-dev").
  Official CE read-only. No push; no src/ changes; no destructive git; preserve unrelated files. Record
  git status, branch, HEAD, `date`. Branch docs-dev/phase-2b-calibration-intuition from the approved 2a
  branch. Editor tools only. Read 02 and 07 first.

SCOPE AND TARGET FILES
- New: docs/foundations/concepts/calibration_intuition.md (Tier 3).
- New: scripts/docs/build_concept_figures.py — generates figures into docs/_static/figures/ (commit with
  git add -f) from the SAME data and model as the walkthrough (read scripts/docs/build_quickstart_walkthrough.py
  to reuse its split, seed and model exactly; do not invent a different setup).
- docs/index.md: insert the page in the "How CE Works" group before the semantics entry. If the PO approved
  D-4, relabel the semantics entry "Guarantees by mode" (URL unchanged).
- docs/sections/how-ce-works.md: card for the page; docs/get-started/why-ce.md: one "Go deeper" link;
  docs/sections/what-and-why.md: retarget "Can We Trust AI Outputs?" only if the PO approved it (D-4).
- docs/appendices/rtd_tier_map.md.

REQUIRED CONTENT
- A table contrasting accuracy, confidence score, calibrated probability and uncertainty range (what each
  answers; what it does not).
- Reliability diagram: raw model scores vs CE calibrated probabilities on the walkthrough test set (or
  calibration-curve bins), produced by the script, with bin counts shown; text explains that one small
  test set cannot prove improvement (consistent with walkthrough C2-03: calibrated Brier 0.0445 vs raw
  0.0366 on that split).
- Uncertainty: what a narrow vs wide range means, using two real cases from the same model; state that
  ranges are statements over many cases and that their meaning is mode-specific, linking
  foundations/concepts/calibrated_interval_semantics.
- "Go deeper" to foundations/concepts/calibration_methods.

SCIENTIFIC AND EDITORIAL REQUIREMENTS
- S5, S6, S7, S10, S11 of 07 §2. Do not paraphrase guarantees; link the semantics page. Keep any
  wording touching SR-01/SR-02/SR-03 marked "under review by the CE authors".
- Every number in the prose must come from the generator output; add a PROSE_NUMBERS-style guard in
  the generator (copy the pattern from build_quickstart_walkthrough.py).
- Figures: blue = model alone, orange = CE; validated palette; transparent background, labels readable in
  light and dark; <title>/<desc>/alt; 390/1440 px check.

EXCLUSIONS
- No change to calibrated_interval_semantics.md or calibration_methods.md content (Phase 4 only links).

VERIFICATION
- Run the generator twice; outputs must be identical (deterministic).
- Strict builds; pytest tests/docs; link checker; visual check.
- New test: tests/docs/foundations/concepts/test_calibration_intuition.py — page reachable; figures exist;
  numbers quoted in the page equal the generator's recorded values (store them in a small JSON next to
  the figures, or re-run the computation in the test if it is fast).

ACCEPTANCE CRITERIA
- Figures are real (generated), reproducible and readable; S5–S7 hold; gates pass.

FINAL REPORT, COMMITS, STOP
- phase-reports/<YYYY-MM-DD_HHMM>_phase-2b.md (standard sections + evidence table). Commits:
  (1) generator + figures, (2) page + nav + tests, (3) report. No push. Stop for PO review.
```

---

## Prompt 2c — Ownership clean-up: Why CE vs What CE Is

```text
ROLE AND OBJECTIVE
Technical editor. Objective: remove restated content between docs/get-started/why-ce.md (owner: workflow
difference, reading one output) and docs/what-is-ce.md (owner: what CE adds, guarantees vs non-guarantees,
fit, comparison), using links instead of repetition.

REPOSITORY AND SAFETY (standard block)
- Local Beta repository (remote "docs-dev"); official CE read-only; no push; no src/; no destructive git;
  preserve unrelated files; record status/branch/HEAD/date; branch docs-dev/phase-2c-ownership from 2b;
  editor tools only; read 02 §5 and 07.

SCOPE
- docs/what-is-ce.md: shorten "The problem: a prediction and an explanation are not enough" to two
  sentences plus links to explainable-ai (2a) and get-started/why-ce. Keep "What CE adds", the guarantees
  table, "When CE is a good fit", "How CE relates to other methods" and references.
- docs/get-started/why-ce.md: where it states guarantees, keep one sentence and link what-is-ce
  ("What CE guarantees, and what it does not") and the semantics page.
- tests/docs/test_what_is_ce.py must still pass; extend it: the page links why-ce and explainable-ai.

EXCLUSIONS
- No new claims; do not touch the assumption wording marked under review.

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Strict builds, pytest tests/docs, link checker. Accept when no paragraph is restated across the two
  pages (list compared paragraphs in the report). Report phase-reports/<…>_phase-2c.md. One docs commit,
  one report commit. No push. Stop: Phase 3 starts only after PO approval of Phase 2.
```

---

## Prompt 3a — "Main components and calls"

```text
ROLE AND OBJECTIVE
Python documentation engineer. Objective: turn docs/get-started/quick_api.md into a short, correct map of
CE's main user-facing components and calls, with executed examples and real output.

REPOSITORY AND SAFETY (standard block)
- Local Beta repository (remote "docs-dev"); official CE read-only; no push; no src/; no destructive git;
  preserve unrelated files; record status/branch/HEAD/date; branch docs-dev/phase-3a-components from the
  approved Phase 2 branch; editor tools only; read 02, 07.

SCOPE
- docs/get-started/quick_api.md (same URL; title "Quick API: main components and calls"). Keep its
  mode-specific semantics notes (STD-004 Tier 2). Add: a component figure (your model →
  WrapCalibratedExplainer → calibrated predictions | explanation collections → plots/export), the core
  calls grouped by step (fit / calibrate / predict / predict_proba / explain_factual / explore_alternatives /
  plot / save_state, load_state), each with one-line purpose and a link to its autosummary page
  (docs/_autosummary is generated: link the built page names; check them in _build).
- Verify every signature against src/calibrated_explanations (read, do not edit). Execute every example.
- Add the page to tests/docs/get_started/test_quickstart_examples_execute.py (PAGES) so its printed output
  is checked.

REQUIREMENTS
- S9 (every call exists and runs; outputs real). Figure rules as in 07 §3.
- Do not use ce_agent_utils (tests/docs/get_started/test_no_ce_agent_utils_recommendation.py).

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Strict builds, pytest tests/docs, link checker, visual check. Accept when every call shown executes and
  links to its reference page. Report phase-reports/<…>_phase-3a.md. Commits: figure; page+tests; report.
  No push. Stop for PO review.
```

---

## Prompt 3b — Troubleshooting as the single owner of errors

```text
ROLE AND OBJECTIVE
Python documentation engineer. Objective: make docs/get-started/troubleshooting.md the canonical list of
user-facing errors and surprises, each reproduced by code.

REPOSITORY AND SAFETY (standard block)
- As in 3a; branch docs-dev/phase-3b-troubleshooting from 3a.

SCOPE
- docs/get-started/troubleshooting.md: add entries, each with symptom (exact message), cause, fix, and a
  minimal reproduction run by you: (1) classifier without predict_proba → ConfigurationError at calibrate;
  (2) indexing explanations with a NumPy integer → ValidationError "Invalid argument type."; (3) factual
  explanation with no rules for saturated cases; (4) pipeline fitted on a pandas DataFrame → scikit-learn
  feature-name UserWarning; (5) guarded options with a fast explainer → ConfigurationError (see
  docs/get-started/quickstart_guarded.md); (6) multiclass bounds above 1 by default (link limitation 1 in
  ce-tasks-and-modes). Re-verify each against the current src/ before writing it.
- docs/get-started/apply-to-your-data.md "Common problems": keep the table, add "Full list:" link.

REQUIREMENTS / EXCLUSIONS
- Only behaviour you reproduced; no speculative causes. Do not change library code to "fix" anything.

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Add tests/docs/get_started/test_troubleshooting_reproductions.py that runs each reproduction and asserts
  the documented exception type/message. Gates as usual. Report phase-3b. Commits: page+tests; report.
  No push. Stop.
```

---

## Prompt 3c — Notebook verification and linking

```text
ROLE AND OBJECTIVE
Python documentation engineer. Objective: find out which repository notebooks run against the current CE
and link only those, with a verification note.

REPOSITORY AND SAFETY (standard block)
- As in 3a; branch docs-dev/phase-3c-notebooks. Notebooks under notebooks/ mirror the official project:
  DO NOT edit them unless the PO approved decision D-5; report failures instead.

SCOPE
- Read scripts/docs/run_notebooks.py and its tests to learn its CLI; run it on notebooks/quickstart_tiny.ipynb,
  notebooks/quickstart.ipynb and notebooks/core_demos/*.ipynb (run from a scratch working directory so
  outputs do not land in the repository). Record pass/fail, runtime, CE and Python versions.
- docs/sections/in-practice.md ("Example notebooks" card) and docs/tasks/{classification,regression,
  probabilistic_regression}.md: link passing notebooks (GitHub URLs on the Beta repository), each with
  "verified with CE <version> on <date>". Remove or flag links to failing notebooks (PO decides).

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Gates as usual. Accept when every linked notebook passed in this run. Report phase-3c with a notebook
  table. Commits: links; report. No push. Stop.
```

---

## Prompt 3d — Correct the code examples flagged by the execution audit

```text
ROLE AND OBJECTIVE
Python documentation engineer. Objective: fix documentation code examples that fail against the current
CE API, as listed in development/reports/docs-five-stage-plan-20261113/01-current-state-audit.md §4
(classes API and OTHER; FRAGMENT pages only where a reader would copy the block as runnable).

REPOSITORY AND SAFETY (standard block)
- As in 3a; branch docs-dev/phase-3d-code-examples.

SCOPE
- For each listed page: reproduce the failure (run the page's python blocks in order from a scratch
  directory), find the current API in src/ (read only), correct the example, and add output blocks where
  the page should show output. Pages that are deliberately fragments get a one-line note naming the
  prerequisite variables, or are made self-contained (choose per page; record why).
- Add each corrected page to an execution test (extend the PAGES list pattern of
  tests/docs/get_started/test_quickstart_examples_execute.py, or a parallel test under the page's tests
  folder).

EXCLUSIONS
- Do not change src/. Do not change pages whose failures come only from missing optional dependencies;
  list them.

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Gates as usual; accept when every corrected page executes in tests. Report phase-3d with a before/after
  table. One commit per page cluster; report commit. No push. Stop.
```

---

## Prompt 3e — Task-page wording (non-causal, defined terms)

```text
ROLE AND OBJECTIVE
Scientific editor. Objective: remove causal or undefined wording from the task guides where no author
decision is pending.

REPOSITORY AND SAFETY (standard block)
- As in 3a; branch docs-dev/phase-3e-task-wording.

SCOPE
- docs/tasks/classification.md lines with "Alternative explanations (counterfactuals)", "epistemic and
  aleatoric explanation envelopes", "necessary to flip the prediction"; docs/tasks/probabilistic_regression.md
  "aleatoric + epistemic uncertainty on the score". Check the open author-question list
  (development/reports/autonomous-runs/20261112T175441+0100/SCIENTIFIC-CLAIMS-REGISTER.md: SR-07
  epistemic/aleatoric, SR-08 counterfactual). For items tied to an open SR question: replace with neutral
  wording that makes no claim either way and add "(terminology under review by the CE authors)"; do not
  resolve the question.

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Wording test in tests/docs/tasks/test_classification.py (extend) for the removed phrases. Gates. Report
  phase-3e. Commits: docs+test; report. No push. Stop: Phase 4 after PO approval of Phase 3.
```

---

## Prompt 4a — Two-way links between intuition and theory

```text
ROLE AND OBJECTIVE
Technical editor. Objective: connect Stage 4 pages to their Stage 2 intuitions and back, with no content
changes to the theory.

REPOSITORY AND SAFETY (standard block)
- As above; branch docs-dev/phase-4a-links from the approved Phase 3 branch.

SCOPE
- Add an "Intuition first:" line at the top and "Next:" at the bottom of:
  docs/foundations/concepts/{calibration_methods,calibrated_interval_semantics,ce_workflow,
  explanation_structures,alternatives,probabilistic_regression}.md, pointing to the Stage 2 owners in 02 §5
  and to the next Stage 4 page in 02 §2.
- Check that docs/foundations/concepts/calibration_intuition.md (2b) and get-started/why-ce.md link forward.

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- tests/docs/test_reader_journeys.py: add the new edges. Gates. Report phase-4a. No push. Stop.
```

---

## Prompt 4b — Comparison page as a design comparison

```text
ROLE AND OBJECTIVE
Scientific reviewer and writer. Objective: rewrite docs/compare.md ("The Explainability Gap") as an
evidence-based design comparison of CE with SHAP, LIME and conformal-prediction packages, with no
performance or superiority claims.

REPOSITORY AND SAFETY (standard block)
- As above; branch docs-dev/phase-4b-compare.

SCOPE
- docs/compare.md: remove "more stable rules" (unsupported). Provide a table: what each method outputs,
  what it assumes, whether it reports uncertainty for predictions and for explanations, model access needed,
  local/global. Cite primary method papers (Ribeiro et al. 2016; Lundberg & Lee 2017; Vovk et al. for
  conformal prediction; CE 2024 ESWA) with resolvable links. Link explainable-ai (2a) for XAI limits and
  what-is-ce for CE's guarantees.
- Respect SR-05/SR-06 (open): state differences in design only.

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Extend tests/docs/test_what_is_ce.py's superiority-phrase check to compare.md. Gates. Report phase-4b
  with a claim/evidence table. No push. Stop.
```

---

## Prompt 4c — Research history and labelled open questions

```text
ROLE AND OBJECTIVE
Research documentation editor. Objective: give researchers a short research history and make every open
item's status explicit.

REPOSITORY AND SAFETY (standard block)
- As above; branch docs-dev/phase-4c-research.

SCOPE
- docs/researcher/index.md: add "Research history" — a dated list of CE publications taken from
  docs/citing.md and docs/researcher/advanced/theory_and_literature.md only (no new citations unless you
  verify them via DOI). Link calibration_methods and the semantics page.
- docs/researcher/future_work.md: tag every item as "Verified limitation" (with evidence: code/test/page),
  "Open question to the CE authors" (with SR id where one exists) or "Proposed extension". Do not resolve
  any SR item.

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Test: every future_work item carries exactly one of the three tags. Gates. Report phase-4c. No push.
  Stop: Phase 5 after PO approval of Phase 4.
```

---

## Prompt 5 — Development setup and contributor path (WP 5a–5c)

```text
ROLE AND OBJECTIVE
Python documentation engineer for contributors. Objective: a contributor can set up the environment, find
the architecture, run the tests and docs build, and submit a change, from the docs alone.

REPOSITORY AND SAFETY (standard block)
- As above; branch docs-dev/phase-5-contributing from the approved Phase 4 branch.

SCOPE
- New docs/contributor/development_setup.md: per decision D-7 either (a) MyST {include} of the relevant
  parts of ../../CONTRIBUTING.md (check relative links render in both builds), or (b) a summary with a
  GitHub link to CONTRIBUTING.md. Add: how to build the docs strictly and run tests/docs (commands from
  07 §1), and the generators in scripts/docs/ with their purpose.
- docs/contributor/index.md: ordered path setup → architecture (foundations/concepts/architecture) →
  plugin-contract and extending guides → test_policy and pr_guide → researcher/future_work. Replace the
  plain-text references to development/standards and development/adrs files with GitHub links to the
  official repository (read-only links).
- docs/foundations/concepts/architecture.md: a short "How to read this page" introduction and links to
  the source tree and tests; no restructuring.

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Both strict builds (include paths!), pytest tests/docs, link checker. Test: contributor hub links the
  setup page and architecture. Report phase-5. No push. Stop: Phase 6 after PO approval.
```

---

## Prompt 6a — Cluster housekeeping (performance, reject, plugins, Mondrian, telemetry)

```text
ROLE AND OBJECTIVE
Documentation architect. Objective: give each overlapping cluster one owner page and one-line role
statements on the others, with no deletions and no URL changes.

REPOSITORY AND SAFETY (standard block)
- As above; branch docs-dev/phase-6a-clusters.

SCOPE
- Clusters and owners from learning-reports/2026-11-12_0910_L06-FULL-DOCS-REVIEW-A-E.md Report C:
  C-23 performance (owner foundations/how-to/tune_runtime_performance.md), C-24 reject (owner
  practitioner/advanced/reject-policy.md), C-25 plugins (role statements on plugins.md,
  practitioner/advanced/use_plugins.md, api/plugins.md, contributor/plugin-contract.md,
  appendices/external_plugins.md), C-27 Mondrian (owner foundations/how-to/conditional_calibration.md),
  C-28 telemetry (owner foundations/how-to/configure_telemetry.md; keep the relocated stub URL).
  Re-verify each finding first; skip and report any that no longer applies.

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Gates; report with a cluster table; one commit per cluster; no push; stop.
```

---

## Prompt 6b — Terminology and release notes

```text
ROLE AND OBJECTIVE
Technical editor. Objective: apply the documented terminology policy and remove the stale release notes.

REPOSITORY AND SAFETY (standard block)
- As above; branch docs-dev/phase-6b-terminology. Requires PO decision on Q-5 / terminology (D-8).

SCOPE
- 16 pages contain "thresholded regression" (list them with grep at start). Per
  docs/foundations/concepts/terminology_thresholded_vs_probabilistic_regression.md, user-facing text uses
  "probabilistic regression"; mechanism or parameter contexts keep "threshold". Change only user-facing
  occurrences; list each decision.
- docs/foundations/governance/release_notes.md (latest entry v0.10.2): replace with a pointer to the
  CHANGELOG and GitHub releases of the official project, keeping the URL.

VERIFICATION, ACCEPTANCE, REPORT, COMMITS, STOP
- Gates; report with a per-occurrence table; no push; stop.
```

---

## Prompt 6c — Final integration and QA

```text
ROLE AND OBJECTIVE
Documentation QA lead. Objective: verify the whole journey and site after Phases 1–6b and report.

REPOSITORY AND SAFETY (standard block)
- As above; branch docs-dev/phase-6c-qa. Read-only except for test additions and the report, unless a
  defect fix is trivial (typo, broken link) — list every such fix.

SCOPE
- Run all gates in 07 §1 (both builds, docs tests, link checker, full test suite once).
- Walk the five stages in order in a local build: every "Next" link leads to the next stage page; every page
  in the journey passes the 07 §4 layout check (390/1440, light/dark).
- Terminology spot-check on journey pages: the four terms of ce-tasks-and-modes are used consistently.
- Page inventory and final navigation tree.

FINAL REPORT
- phase-reports/<…>_phase-6c-final.md: gates, journey walk results, remaining open items (author
  questions, blocked WPs), navigation tree, reader-experience summary per audience.

COMMITS, STOP
- Tests and report commits only. No push; print the PowerShell push command. Stop.
```
