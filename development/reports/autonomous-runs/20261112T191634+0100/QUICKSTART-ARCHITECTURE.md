# Quick Start v3 architecture

## Principles

- **One landing, three paths.** The landing is short (2–3 minutes): a one-paragraph
  definition, the workflow figure, three path cards, the recommended order
  A → B → C, and links to installation, API reference and deeper science.
- **Each path stands alone** and links to the others at its edges.
- **Smallest coherent set of pages:** one new conceptual page (`why-ce`), one new
  practical page (`apply-to-your-data`); one page retired to a redirect stub.
- **Four terms kept distinct:** prediction task, CE mode, calibration method,
  explanation configuration (table on C1). Guarded explanations are an
  explanation configuration in every mode.
- **Real output:** every quickstart and the apply page show the output their
  code prints; a test checks that the printed output equals the page.

## Navigation tree (Quick Start section)

```text
Quick Start — Understand, Explore and Apply CE      get-started/index        Tier 1
├── A1 · Machine learning essentials                 get-started/ml-foundations   Tier 1
├── A2 · Why CE: from a conventional to a CE workflow get-started/why-ce      Tier 3 (new)
├── B  · Guided Python walkthrough                   get-started/quickstart_walkthrough  Tier 1
├── C1 · Tasks, modes and capabilities               get-started/ce-tasks-and-modes      Tier 1
├── C2 · Classification quickstart                   get-started/quickstart_classification  Tier 2
├── C3 · Regression quickstart                       get-started/quickstart_regression      Tier 2
├── C4 · Guarded explanations                        get-started/quickstart_guarded         Tier 2
├── C5 · Apply CE to your own data                   get-started/apply-to-your-data   Tier 3 (new)
└── Quick API                                        get-started/quick_api            Tier 2

Not in the toctree: getting_started_60s (orphan redirect stub → C1#choosing-your-workflow)
```

## Path content pattern

| Path | Pattern |
|---|---|
| A | Question → running example (numbers from Path B) → conventional workflow → CE workflow (figure) → requirements → data roles → four ideas → assumptions and limitations → next |
| B | Per section: **Question** → code → real output → concept → interpretation → next |
| C (quickstarts) | Purpose → prerequisites → semantics note (STD-004) → code → real output → interpretation → common mistakes → next |
| C5 | Four checks → seven steps with real output → common problems → optional AI-assistant section with reusable prompt → next |

## Figure

`docs/_static/figures/ce-in-ml-workflow.svg` (added at the PO's request
during the run): conventional ML steps in grey, CE components in purple
(calibration set, Calibrate with Venn-Abers / CPS, Explain with factual and
alternative explanations, calibrated prediction and explanation outputs). It
has `<title>`/`<desc>` and page alt text, a white card background for dark
mode, and opens full size when tapped. Used on the landing, `why-ce` and
How CE Works → The CE workflow (replacing two mermaid diagrams).
