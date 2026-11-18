# CE documentation — final learning-journey release candidate (2026-11-19)

Release record for branch `docs/ce-final-learning-journey-20261119`. The branch
starts from `56f884ad` (`docs/overnight-refinement-20261118`). The full phase
reports are kept outside the repository in `learning-reports/`.

## Phases and snapshots

| Phase | Commit | Immutable snapshot branch | Summary |
|---|---|---|---|
| 1 | — | — | Read-only content audit and architecture (`learning-reports/01-content-audit-and-architecture.md`) |
| 2 | `92143bf9` | `ce-review-02-navigation` | Sidebar root reduced to Home, Quick Start, the four sections and Project & Resources; section hubs parent their pages; thin hubs and `ml-foundations` removed from navigation (URLs kept); official direct routes restored on the homepage |
| 3 | `230d77f1` | `ce-review-03-quickstart` | One five-step learning journey (CE by example → Python walkthrough → reading explanations → apply → evaluate); generated pages changed through the generator, outputs unchanged |
| 4 | `5539867b` | `ce-review-04-sections` | Section reading orders and handovers; one table of open author questions on the canonical semantics page; How-to guides grouped and described |
| 5 | `ba7d0183` | `ce-review-05-validation` | Named navigation landmark; homepage section icons restored after the navigation change |
| 6 | this commit | `ce-review-final-20261119` | Release record only (no documentation change) |

## Preservation evidence

Measured against official v1.0.2 (`609d7b72`) and baseline `56f884ad`:

| Item | Result |
|---|---|
| Official page paths | 107/107 present |
| Official and baseline paper references | 0 missing |
| Baseline code blocks | 0 lost |
| Official code blocks not verbatim | 56, unchanged from baseline; earlier documented corrections |
| Formulas | 136 → 136 |
| Figure files | Unchanged (10); `walkthrough-figure-1.png` byte-identical after regeneration |
| "Under review" markers | 42 → 43 |
| Official sentences present verbatim | 84.8%, unchanged from baseline |
| Anchors | 0 lost against the baseline build |

## Validation

| Check | Result |
|---|---|
| `tests/docs` | 395 passed |
| `tests/scripts/test_check_parameter_naming.py` | 5 passed |
| `tests/integration/test_doc_examples_smoke.py` | 16 passed, 1 failed (pre-existing: the wheel-packaging test needs the uninstalled `build` package) |
| Strict Sphinx, Beta and standard | 0 warnings |
| Internal links | 0 broken |
| Assets | All resolve; every image has alt text |

## Open scientific questions

None was resolved. See "Open questions for the CE authors" in
`docs/foundations/concepts/calibrated_interval_semantics.md`.
