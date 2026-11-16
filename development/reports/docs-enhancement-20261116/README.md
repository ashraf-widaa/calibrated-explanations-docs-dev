# Documentation enhancement cycle — 2026-11-16

Branch `beta/next-docs-enhancement`, based on the published integrated
candidate `73048761`. Start with `10`.

| # | Report | Content |
|---|---|---|
| 00 | [Promotion readiness of 73048761](00-promotion-readiness-73048761.md) | Verdict, verified results vs pending scientific claims, promotion plan, tested rollback |
| 01 | [Baseline and scope](01-baseline-and-scope.md) | Git baseline, protected material, architecture, scope reconciliation, recorded conflicts |
| 02 | [WP-6](02-wp6-implementation.md) | Quick API, troubleshooting (reproduction evidence), notebooks |
| 03 | [WP-13](03-wp13-implementation.md) | What & Why progression, calibration vs accuracy |
| 04 | [WP-14](04-wp14-implementation.md) | How CE Works chain, levels, distinctions, V-8 |
| 05 | [Scientific review](05-scientific-review.md) | 14 topics, one-sided intervals across versions, full author register |
| 06 | [Education and architecture](06-educational-and-architecture-review.md) | Seven entries, three readers, duplication, accessibility, gaps |
| 07 | [Validation](07-validation-results.md) | Exact commands, results, regression comparison |
| 08 | [Candidate comparison](08-candidate-comparison.md) | `73048761` vs the new candidate |
| 09 | [Release readiness and decisions](09-release-readiness-and-decisions.md) | Publication steps, blockers, PO decisions |
| 10 | [Executive summary](10-executive-summary.md) | One-page overview |

`evidence/` holds the reproduction scripts (troubleshooting, Quick API
example, one-sided intervals, responsive check) and their raw outputs
(responsive measurements for the baseline and the new candidate, notebook
runs). Local paths have been reduced to file names. Run the scripts as
described in `07`, with `PYTHONPATH` pointing at the CE source to test.
