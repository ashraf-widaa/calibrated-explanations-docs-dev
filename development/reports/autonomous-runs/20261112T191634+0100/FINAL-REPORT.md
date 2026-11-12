# Final report — CE Quick Start v3

**Outcome:** the Quick Start is now a three-path learning experience. It is
implemented, validated and committed locally on `docs-dev/autonomous-20261112`.
It is **not yet published**: the push is blocked by the agent's permission
policy, so the Project Owner needs to push (command below).

## What changed

- **Landing** (`get-started/index`): a short page with a definition, a new
  workflow figure, three path cards, the order A → B → C, and links to
  installation, Quick API, glossary, API reference and the deeper science.
- **Path A — Understand CE:** A1 *Machine learning essentials*; **new** A2
  *Why CE: from a conventional to a CE workflow* (a running example, the
  conventional vs CE workflow, requirements, data roles, four ideas,
  assumptions and limitations).
- **Path B — Learn CE by example:** the walkthrough now opens each section
  with a **Question** and includes an educational disclaimer, common mistakes
  and routes into Path C. It was regenerated, and no output number changed.
- **Path C — Apply CE to your data:**
  - C1 *Tasks, modes and capabilities*: four distinct terms, an at-a-glance
    mode table, and the workflow selection merged from the 60-second page;
  - C2–C4 quickstarts: real printed output, interpretation and common mistakes;
    guarded explanations are framed as an explanation configuration;
  - **new** C5 *Apply CE to your own data*: seven executed steps, common
    problems, and an optional AI coding assistant section with a reusable
    prompt.
- **Figure** (PO request during the run): `ce-in-ml-workflow.svg`, used on
  the landing, on *Why CE* and in *How CE Works → The CE workflow*.
- **Retired:** `getting_started_60s` is now a redirect stub. All URLs are preserved.

## Navigation tree

```text
Quick Start — Understand, Explore and Apply CE
├── A1 · Machine learning essentials
├── A2 · Why CE: from a conventional to a CE workflow      (new)
├── B  · Guided Python walkthrough
├── C1 · Tasks, modes and capabilities
├── C2 · Classification quickstart
├── C3 · Regression quickstart
├── C4 · Guarded explanations
├── C5 · Apply CE to your own data                          (new)
└── Quick API
(orphan) getting_started_60s → C1#choosing-your-workflow
```

## Reader experience

- **Newcomer or decision-maker:** reads the landing (2–3 min) and the figure,
  then Path A. They learn why CE is needed and what it does and does not
  promise, without code.
- **Learner:** follows Path B. Every step asks a question, runs code, shows
  real output and says what to conclude, with the mistakes to avoid at the end.
- **Practitioner:** goes to C1 to check task, model and data. They pick a mode
  and run its quickstart with visible expected output. Then C5 brings CE to
  their own data, with troubleshooting from executed behaviour and an
  optional, reviewable AI assistant prompt.

## Findings worth author attention

New, verified behaviour now documented on the pages:

- a factual explanation can contain no rules (15 of 114 cases in C5);
- indexing explanations with a NumPy integer raises `ValidationError`;
- the multiclass default bounds exceed 1 in the published examples.

The SR-02 coverage wording is marked "under review". SR-01 to SR-16 remain open.

## Validation

- Strict Beta and standard builds: 0 warnings.
- Docs tests: 298 passed.
- All quickstart outputs match execution.
- Links: 0 broken across 155 pages.
- Full test suite: 5338 passed, 4 inherited environment failures.

Details: VALIDATION-SUMMARY.md.

## Limitations

- At phone width the figure's labels are small; tapping opens it full size.
- The quickstarts use small public datasets; their wide ranges are explained
  on the pages, not hidden.
- The live Beta site is not verified, because the branch is not pushed.

## Publish (Project Owner)

```powershell
Set-Location "D:\Jönkoping\CE-Documentation-Redesign\calibrated_explanations"
git push docs-dev docs-dev/autonomous-20261112:main
```

This is a fast-forward from `e5fe7c23`. Then verify the RTD build and the
pages listed in PUBLICATION-HISTORY.md.
