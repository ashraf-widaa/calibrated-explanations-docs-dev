# Entry-point quality matrix — run 2

**Scale:** 1–5. Each cell shows **after run 1 → after run 2**. Run 1 values are from
`../20261112T100852+0100/ENTRY-POINT-QUALITY-MATRIX.md`. Scores rise only where a
run 2 change is verified.

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
| Homepage | 5→5 | 5→5 | 4→4 | 4→4 | 4→4 | 4→4 | 4→4 | 3→3 | 5→5 | 4→4 | 4→4 | 4→4 |
| Quick Start | 4→5 | 4→5 | 4→5 | 4→5 | 4→5 | 4→5 | 4→5 | 4→4 | 4→5 | 4→4 | 4→4 | 4→5 |
| CE: What & Why | 4→5 | 4→5 | 3→4 | 3→4 | 2→4 | 3→4 | 2→3 | 2→4 | 3→5 | 3→4 | 4→4 | 4→4 |
| How CE Works | 4→5 | 4→5 | 3→4 | 4→4 | 3→4 | 4→5 | 3→4 | 4→5 | 4→5 | 4→5 | 4→5 | 4→4 |
| CE in Practice | 4→4 | 4→4 | 3→4 | 3→4 | 3→4 | 3→4 | 4→5 | 3→4 | 4→4 | 4→5 | 4→4 | 4→5 |
| Software & Integration | 4→4 | 4→4 | 3→3 | 4→4 | 4→4 | 3→3 | 4→4 | 4→4 | 4→4 | 4→5 | 4→4 | 4→5 |
| Project & Resources (incl. glossary) | 4→4 | 4→4 | 3→3 | 4→4 | 3→4 | 3→3 | 4→4 | 4→4 | 4→4 | 4→4 | 4→4 | 4→4 |

## Evidence for each rise

- **Quick Start:**
  - ten-section teaching walkthrough (spec `05` rev. 2) with an explained mechanism, a raw vs calibrated comparison, qualified guarantees and "can/cannot conclude";
  - ML basics §A7;
  - an idea-to-section map;
  - executed task quickstarts;
  - generator prose guard and wording tests.
- **What & Why:**
  - new `what-is-ce` covering problem, contribution, guarantees table, fit, design comparison and references;
  - reachable from its card and the sidebar;
  - tests block superiority phrasing.

  Practical usefulness stays modest because the section is conceptual.
- **How CE Works:**
  - new workflow page with a Level 1/2/3 learning path linking papers, ADD-1 sections and source files and tests;
  - probabilistic regression and alternatives rewritten with executed, test-checked examples;
  - journeys verified.

  Accuracy stays 4 because SR-02, SR-03, SR-09, SR-10, SR-14 and SR-15 are open.
- **CE in Practice:**
  - new evaluation guide (reproducible set-up, empirical checks, common mistakes, failure cases);
  - task guides link notebooks and the API.
- **Software & Integration:** route to source and tests; tooling documentation and link checker in `scripts/docs/`.
- **Project & Resources:** four new glossary entries with teaching owners.

**Unchanged scores** reflect areas this run did not touch, or open author questions.
