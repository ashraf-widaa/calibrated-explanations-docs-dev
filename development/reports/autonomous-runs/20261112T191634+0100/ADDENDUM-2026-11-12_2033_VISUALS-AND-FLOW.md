# Addendum — visuals, content and flow (2026-11-12 20:33)

## 1. Deployment investigation (before this change)

The PO reported that the live Quick Start still showed the old three-step
structure after `99678028` was pushed. Read-only investigation found:

- `99678028:docs/get-started/index.md` is the v3 landing; the old phrases
  ("CE in 60 seconds", "Your learning path", "Where each idea is taught") exist
  only at `e5fe7c23`.
- Remote `main` = `99678028`; RTD build #35848162 built it successfully
  (18:57:16–18:58:44 UTC); `latest` tracks `main`.
- The live page (normal and cache-busted fetch) shows v3.

**Root cause:** an outdated view (the page was opened before the build
finished, or a cached copy was served), not a source, build or configuration
defect. No change was needed.

## 2. PO request

Transparent figure backgrounds; adjusted figure sizes; distinct colours (blue
and orange) for the conventional and CE workflow in one figure; real
improvements to the visuals, content and flow of the Quick Start and related
pages, with clarity and correctness.

## 3. Changes

| Item | Change |
|---|---|
| Workflow figure | Redrawn with transparent background; **blue = conventional workflow, orange = added by CE** in one figure (conventional `Predict` output shown next to CE's calibrated outputs); all text inside filled shapes so it reads in light and dark themes. Two layouts: `ce-in-ml-workflow.svg` (wide, desktop) and `ce-in-ml-workflow-narrow.svg` (phone), switched with `<picture>` at 600 px. Used on the landing, `why-ce` and *The CE workflow*. |
| Colours | Strokes `#2563eb` / `#ea580c` validated with the dataviz palette validator on light and dark surfaces (all checks pass; CVD ΔE ≥ 31). Arrows `#7c8796` (3.6:1 on white, 5.1:1 on dark). |
| New figure | `ce-reading-an-output.svg`: how to read a calibrated prediction, a factual rule and an alternative, drawn from the walkthrough's real numbers (0.286 [0.167, 0.333]; −0.190 [−0.314, −0.048]; 0.476 [0.333, 0.600]). |
| `why-ce` | New flow: what a conventional workflow leaves open → the CE workflow (figure) → one example (table + reading figure) → four ideas (linked to the figure panels) → requirements and data roles (merged) → assumptions → next. The separate conventional-workflow mermaid diagram was removed (the figure shows both). |
| C1 `ce-tasks-and-modes` | New flow under "Choosing your workflow": Step 1 check that CE fits → Step 2 pick the mode, as three responsive, theme-aware cards (question, call, calibration method, quickstart link) replacing the mermaid chart → what the outputs mean → the four terms → capability reference and limitations. Removed duplication: the "Supported tasks" section, the "At a glance" table and the eight-step list (their content is in the cards, the output table and C5). The PO-reviewed uncertainty wording is unchanged. |
| Landing | Tighter copy; the responsive figure; cards rephrased. |
| Quickstarts and C5 | Real CE plots added to C2, C4 and C5, generated from each page's own code by the new `scripts/docs/build_quickstart_figures.py`; each with alt text and a short "Reading the plot" note consistent with the walkthrough. |
| Styling | New `docs/_static/ce-docs.css` (figure layout, captions), registered in `conf.py`. |
| Tests | Figure wiring (both layouts on all three pages, `<title>`/`<desc>`), plot files exist for every figure reference. |

## 4. Findings for the CE authors

- CE's regression factual plot (`plot(..., uncertainty=True)`) at default
  size draws its top-panel axis label ("Prediction interval with 90.0%
  confidence") underneath the lower panel, and colours positive weights blue,
  the reverse of the classification plot. The regression quickstart therefore
  shows no plot.
- `plot(filename=...)` saves under a `plots/` folder relative to the working
  directory and appends the index to the name; the figure script therefore
  saves the figure itself.

## 5. Validation

- Strict Beta build and strict standard build: 0 warnings.
- Docs tests: 298 passed; `tests/docs/get_started`: 25 passed (execution and
  output-match tests included).
- Links: 155 pages, 0 broken (scratchpad checker and `check_internal_links.py`).
- Headless Edge at 390 and 1440 px, light and dark, 7 pages: no horizontal
  overflow; the phone layout loads `ce-in-ml-workflow-narrow.svg` and the
  desktop layout loads `ce-in-ml-workflow.svg`.

## 6. Not done

- Not pushed (`git push` is denied for the agent). The live site is unchanged
  until the PO pushes.
- An empty, git-ignored `plots/` folder was created by a first attempt to use
  `plot(filename=...)`; deleting files is outside the agent's permissions.
