# Stage 07 — How CE Works

**Started:** 2026-11-12 11:16 · **Completed:** 2026-11-12 11:30
**Starting branch / commit:** `docs-dev/autonomous-20261112` / `1ca82e60`

## Inspected

- `sections/how-ce-works.md`, `foundations/index.md`;
- `calibrated_interval_semantics.md` (original CE page plus Beta further reading);
- ADD-1 `calibration_methods.md`;
- `interpret_explanations.md`;
- the three task pages;
- renderer: `viz/matplotlib_adapter.py`, `utils/configurations/plot_config.ini`, `plotting.py` 877–886.

## Problems

| ID | Problem | Evidence |
|---|---|---|
| HW-1 | **Factually wrong:** the guide says plots use green for positive and purple for negative | Default style `plot_config.ini` `positive = red`, `negative = blue` (also hard-coded defaults, `plotting.py:877`). Dual-header (classification/probabilistic) bodies use positive → red, negative → blue (`matplotlib_adapter.py:1545`). Plain regression swaps them via `_regression_sign_colors` (lines 1037–1055) |
| HW-2 | Semantics page and task pages do not link the methods page (ADD-1) | 0 links (Report A–E, C-14) |
| HW-3 | Two How CE Works cards open the same page ("Calibration & Uncertainty" and "Assumptions & Guarantees") | `sections/how-ce-works.md` |
| HW-4 | No canonical page on explanation construction | SR-14 (author-dependent; ADD-2) |

## Decisions and changes

| File | Change | Evidence level |
|---|---|---|
| `docs/foundations/how-to/interpret_explanations.md` | HW-1: colour sentence now describes the default rendering, red/blue with regression swapped, and that the style is configurable | B (implementation) |
| `tests/docs/foundations/how_to/test_interpret_plot_colours.py` | 3 tests: config defaults, regression swap in source, guide wording (no green/purple) | — |
| `docs/tasks/classification.md`, `regression.md`, `probabilistic_regression.md` | HW-2: one bullet "How CE computes these outputs" → ADD-1, directly after "Formal semantics" | — (link only) |
| `docs/foundations/concepts/calibrated_interval_semantics.md` | HW-2: ADD-1 first in "Further reading", with its under-review status stated; HW-3: label `cross-mode-non-guarantees` before the existing heading. **No guarantee wording changed** | — |
| `docs/sections/how-ce-works.md` | HW-3: "Assumptions & Guarantees" now opens the cross-mode section, with the description "What holds in every mode, and what CE does not guarantee." | — |

**HW-4 deferred** (SR-14). No new teaching content was written on explanation construction, because the mechanism's intended reading needs the authors.

## Validation

| Gate | Result |
|---|---|
| Strict Beta build | exit 0, 0 warnings |
| `pytest tests/docs …` | 244 passed |
| Links and anchors | 150 pages, 0 broken; card renders `…calibrated_interval_semantics.html#cross-mode-non-guarantees` |

The colour behaviour was verified from source and configuration, not by rendering and sampling pixels.

## Commit, push, publication

- **Commit:** see `RUN-STATUS.md`.
- **Pushed:** no (B-01).
