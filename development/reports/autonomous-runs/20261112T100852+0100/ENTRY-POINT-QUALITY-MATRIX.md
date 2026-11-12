# Entry-point quality matrix — run 20261112T100852+0100

**Scale:** 1–5. Each cell shows **baseline → after this run**.

**Baseline sources:**
- Step 9 audit (`learning-reports/2026-11-12_0151_…`);
- full review A–E (`…_0910_…`), whose area ratings are refined here to 12 criteria.

**"After" evidence:** the stage reports in this directory (S02–S11). Scores rise only where a verified change supports them.

**Criteria:**

| # | Criterion | # | Criterion |
|---|---|---|---|
| 1 | Goal clarity | 7 | Practical usefulness |
| 2 | Audience suitability | 8 | Advanced references |
| 3 | Beginner readability | 9 | Independent usability |
| 4 | Scientific accuracy | 10 | Cross-section integration |
| 5 | Conceptual completeness | 11 | Navigation |
| 6 | Learning progression | 12 | Maintainability |

| Entry point | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Homepage | 4→5 | 4→5 | 4→4 | 4→4 | 4→4 | 4→4 | 3→4 | 3→3 | 4→5 | 3→4 | 3→4 | 3→4 |
| Quick Start | 4→4 | 4→4 | 4→4 | 4→4 | 4→4 | 4→4 | 4→4 | 3→4 | 4→4 | 2→4 | 4→4 | 3→4 |
| CE: What & Why | 2→4 | 3→4 | 2→3 | 3→3 | 2→2 | 2→3 | 2→2 | 2→2 | 2→3 | 2→3 | 2→4 | 3→4 |
| How CE Works | 4→4 | 3→4 | 3→3 | 4→4 | 3→3 | 4→4 | 3→3 | 4→4 | 3→4 | 2→4 | 3→4 | 3→4 |
| CE in Practice | 2→4 | 3→4 | 3→3 | 3→3 | 2→3 | 2→3 | 3→4 | 2→3 | 2→4 | 2→4 | 2→4 | 2→4 |
| Software & Integration | 3→4 | 4→4 | 3→3 | 3→4 | 2→4 | 3→3 | 3→4 | 2→4 | 3→4 | 2→4 | 2→4 | 3→4 |
| Project & Resources (incl. glossary) | 3→4 | 3→4 | 3→3 | 4→4 | 3→3 | 3→3 | 3→4 | 3→4 | 2→4 | 2→4 | 2→4 | 3→4 |

## Evidence for the changes

- **Homepage:** approved design implemented (S02). Fixed:
  - 3 + 1 and empty-slot layouts;
  - unstyled resources block;
  - wrong external-link arrows;
  - undefined icon.

  Commercial Services is separate. 7 structural tests. Contrast ≥ 5.7:1; keyboard order verified.
- **Quick Start:** onward routes to methods and Software (S05); generator and page kept in sync by a test. *Not raised:* readability and progression, because the teaching-first rewrite is deferred.
- **What & Why:**
  - the card now leads to the Level 1 explanation;
  - a non-guarantee statement was added;
  - comparison card made accurate (S06).

  *Completeness stays 2:* `compare.md` is thin and its claims are author-blocked (SR-05, SR-06).
- **How CE Works:**
  - plot-colour fact corrected and guarded by a test (S07);
  - semantics and tasks link the methods page;
  - duplicate card resolved;
  - sidebar Overview (S11).

  *Completeness stays 3:* explanation construction (SR-14) is missing.
- **CE in Practice:** audit wording removed; Expert Hub, notebooks, playbooks and an accurate Decision Lab card (S08); sidebar Overview (S11). *Completeness 3, not higher:* there is no evaluation guide (needs SR-02).
- **Software & Integration:**
  - the API page now leads to rendered signatures;
  - versions, Python and release-notes facts verified against PyPI, `pyproject.toml` and the CHANGELOG;
  - configuration group and Upgrades card added (S09).
- **Project & Resources:**
  - README and support/feedback routes;
  - roadmap reader links;
  - researcher hub → methods and citing (S10);
  - glossary connected from 11 landing points, with API terms pointing to signatures (S04).

**Scientific accuracy did not rise anywhere except the plot-colour fact**, because every other accuracy item depends on author decisions (SR-01–SR-16).
