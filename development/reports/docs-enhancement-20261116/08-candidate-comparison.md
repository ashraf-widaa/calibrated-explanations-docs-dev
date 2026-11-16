# 08 — Next candidate vs published integrated baseline

**Baseline:** `beta/integrated-candidate` `73048761` (published at
`/en/beta-integrated-candidate/`).
**New:** `beta/next-docs-enhancement` (commit ids in `09`).
The new branch is a direct descendant of the baseline: four commits, no merges.

| Area | Baseline `73048761` | New candidate | Verdict |
|---|---|---|---|
| Quick API | Method map with four unexplained fragments | Entry questions answered; component table; one complete, executed example (walkthrough case 2) with real output; every call linked to its API entry | Improved |
| Troubleshooting | 9-row table; 3 rows wrong or speculative (NaN timing, `features_to_ignore` issue, telemetry), versions mislabelled | 12 reproduced entries with exact messages, lookup table, versions; tested against the library | Improved, with corrections |
| Notebooks | Linked without verification | Four core demos verified and labelled; two quickstart notebooks flagged (environment) | Improved |
| What & Why landing | Five cards, unordered; "Trustworthy AI" card | Problem/answer intro; seven-question reading order; ordered cards; regulation entry relabelled and qualified | Improved |
| `what-is-ce` | Problem, adds, guarantees, fit, comparison | + calibration vs accuracy, worked example, range ≠ correctness, potential vs demonstrated benefit, phone tables | Improved |
| How CE Works landing | Six cards, no order | Chain sentence, levelled reading order, sidebar in reading order, "Guarantees by Mode" | Improved |
| `ce_workflow` | Task/method/output table | + "read the range as", teaching-view note, explanation types ≠ modes, six distinctions, two markers, phone tables | Improved |
| `interpret_explanations` | Telemetry snippet (unverified keys), overclaim, wrong notebook path | Figure V-8, telemetry → link, overclaim removed, path fixed | Improved |
| `calibration_methods` | 4 wide tables scroll on phones | Compact layout; text unchanged | Improved (layout) |
| Quick Start A/B/C, tutorials, task semantics, V-6 | — | Unchanged | Unchanged |
| Build / links / tests | 0 warnings / 0 broken / 335 | 0 warnings / 0 broken / 365 | No regression |
| Open scientific items | SR-01…16, N-01…05 | Same, plus N-06 (fixed) and N-07…N-11 (open) | More visible, none resolved by the team |

**Regressions found:** none.
**Outstanding:**
- V-2, V-4 and V-7 (new page or figure work);
- the 8 residual scrolling tables;
- the two quickstart notebooks;
- the author register (`05`).
