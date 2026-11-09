# L03 Part 2 - Homepage Improvement Proposal

Date: 2026-11-08  
Status: Proposal only; no changes implemented

## Proposal constraints

This proposal contains three small homepage changes at most. It reuses existing
pages and does not propose new documentation pages. The recommendations are
based on read-only source inspection, not observed user testing.

## Prioritized improvements

### 1. Add a plain-language CE orientation sentence

**Priority:** 1

**Problem addressed:** The homepage identifies CE as an open-source project but
does not explain what it helps a user do or why calibration matters.

**Supporting evidence:** The homepage currently says “Use this site by audience
and by task” and later identifies the project as open source
(`docs/index.md:3`, `docs/index.md:28-31`). The first concrete explanation of
calibrated predictions, uncertainty intervals, and factual/alternative
explanations appears in the interpretation guide
(`docs/foundations/how-to/interpret_explanations.md:1-16`).

**Proposed wording/navigation change:** Add two short sentences immediately
after the opening orientation, for example:

> Calibrated Explanations helps you understand what a machine-learning model
> predicts, how uncertain that prediction is, and which feature conditions
> support it. It also provides calibrated alternative scenarios so you can
> inspect possible changes without treating model explanations as causal
> guarantees.

Link “calibrated predictions and uncertainty” to the existing interpretation
guide and “guarantees” to the existing calibrated interval semantics page.

**Existing pages to reuse:**  
`docs/foundations/how-to/interpret_explanations.md` and  
`docs/foundations/concepts/calibrated_interval_semantics.md`.

**Expected benefit:** A beginner can form a correct mental model before
encountering installation or governance material; a practitioner can quickly
judge whether CE addresses their interpretation and uncertainty needs.

**Evaluation:** Ask first-time readers to answer “What does CE help with?” after
reading only the homepage. Success means they can mention prediction
interpretation and uncertainty without opening another page, while preserving
the existing non-causal caveat.

### 2. Label one quickstart as the recommended first example

**Priority:** 2

**Problem addressed:** The Get started page lists classification, regression,
and guarded quickstarts but does not identify which one a student should try
first.

**Supporting evidence:** The homepage routes new users to Get started
(`docs/index.md:47`), and Get started says “Pick one quickstart” before listing
three choices (`docs/get-started/index.md:1-15`). The classification quickstart
has a self-contained dataset and the standard fit/calibrate/explain flow
(`docs/get-started/quickstart_classification.md:1-8`,
`docs/get-started/quickstart_classification.md:20-48`).

**Proposed wording/navigation change:** On the homepage, add a small
“Recommended first try” link to `get-started/quickstart_classification`.
Alternatively, label that link in the Get started hub as “Start here if you
are new to CE”; leave regression and guarded quickstarts as task-specific
alternatives.

**Existing pages to reuse:**  
`docs/get-started/index.md` and  
`docs/get-started/quickstart_classification.md`.

**Expected benefit:** Reduces choice overload while preserving task-specific
routes for users who already know what they need.

**Evaluation:** Give a student the homepage and ask them to identify the first
example to run. Success means the student selects the classification
quickstart and can explain why it is the recommended general introduction.

### 3. Add a compact “after the quickstart” route

**Priority:** 3

**Problem addressed:** Existing quickstarts provide several valid next links,
but neither the homepage nor Get started gives one explicit continuation from
example to interpretation to limitations.

**Supporting evidence:** The classification quickstart links to interpretation,
alternatives, and citing (`docs/get-started/quickstart_classification.md:48-52`);
Get started separately links to Quick API, interpretation, and semantics
(`docs/get-started/index.md:17-20`). The practitioner hub already demonstrates
that a sequence can be expressed compactly:
quickstart -> interpretation -> API style -> playbooks
(`docs/practitioner/index.md:5-9`).

**Proposed wording/navigation change:** Add a three-step homepage block:

1. Run the recommended classification quickstart.
2. Read how to interpret factual and alternative explanations.
3. Read mode-specific semantics, assumptions, and non-guarantees.

Link the steps to the existing quickstart, interpretation guide, and semantics
page. This should complement, not replace, the existing audience and task
navigation.

**Existing pages to reuse:**  
`docs/get-started/quickstart_classification.md`,  
`docs/foundations/how-to/interpret_explanations.md`, and  
`docs/foundations/concepts/calibrated_interval_semantics.md`.

**Expected benefit:** Makes the learning sequence visible and gives the student
an intentional stopping point after the first successful run. It also gives
practitioners a compact route from capability discovery to responsible use.

**Evaluation:** Ask readers to identify what to read after completing the first
example and where to find limitations. Success means they choose interpretation
first and semantics/limitations second, without relying on search.

## Recommendation

Validate these three small changes with a short readability review before
implementation. If only one change can be tested first, test the plain-language
orientation sentence because it addresses the earliest information gap for both
personas. Do not treat the source-based friction observations as confirmed user
research until readers perform the walkthrough.

