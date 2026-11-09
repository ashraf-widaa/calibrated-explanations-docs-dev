# L03 Part 2 - Beginner Readability Walkthrough

Date: 2026-11-08  
Task: L03 - Part 2: Beginner Readability Walkthrough  
Status: Read-only walkthrough completed; no documentation redesign implemented

## Objective and method

This report evaluates whether a first-time user can move from the documentation
homepage to a useful first example, understand the role of calibration and
uncertainty, and identify a next step.

Persona A is a student who knows basic Python and machine learning but has never
used Calibrated Explanations (CE). Persona B is an ML practitioner with an
already-trained model who is deciding whether CE is relevant.

The walkthrough is a source-based inspection, not user testing. Friction
observations are therefore hypotheses about likely readability or navigation
problems, not measured user behaviour.

## Persona A - Student beginner

### Walkthrough summary

The student can reach a runnable classification example quickly:

`docs/index.md` -> `docs/get-started/index.md` ->
`docs/get-started/quickstart_classification.md` ->
`docs/foundations/how-to/interpret_explanations.md` ->
`docs/foundations/concepts/calibrated_interval_semantics.md`

The path is present and technically coherent. The main weakness is that the
homepage routes the student to the path without first explaining CE in
plain-language terms or naming the recommended first quickstart.

### Evidence table

| User goal | Expected navigation path | Actual available path | Source and lines | Clear information | Possible friction | Confidence |
|---|---|---|---|---|---|---|
| Understand what CE is and why it was developed | Homepage orientation -> short CE explanation | Homepage says to use the site by audience/task and identifies CE as an open-source project, but does not state the problem CE solves | `docs/index.md:3`, `docs/index.md:28-31` | Project identity and documentation purpose are clear | A beginner must infer the value of calibrated explanations from later pages | High |
| Find the recommended starting point | Homepage -> one beginner entry point | Homepage sends new users to Get started; Get started says to pick one quickstart | `docs/index.md:47`, `docs/get-started/index.md:1-3` | The starting hub is explicit | “Pick one” leaves the first choice unresolved for a student | High |
| Identify a suitable first example | Get started -> classification quickstart | Classification, regression, and guarded quickstarts are listed; classification is a reasonable general first example but is not labelled as recommended | `docs/get-started/index.md:9-15`, `docs/get-started/quickstart_classification.md:1-8` | The classification quickstart has prerequisites and a complete fit/calibrate/explain sequence | Three options can create choice overload; guarded mode introduces advanced semantics early | High |
| Locate explanations of calibration and uncertainty | Quickstart -> interpretation -> semantics | Quickstarts link to interpretation and calibrated interval semantics; the semantics page separates classification, interval regression, and probabilistic regression | `docs/get-started/index.md:17-18`, `docs/get-started/quickstart_classification.md:8-14`, `docs/foundations/concepts/calibrated_interval_semantics.md:1-18` | Mode-specific guarantees, assumptions, and non-guarantees are explicit | “Semantics” is an abstract label for a beginner and appears before a simple conceptual explanation | High |
| Understand what to do after a quickstart | Quickstart -> interpretation -> task/API/reference material | Classification points to interpretation, alternatives, and citing; Get started also links to Quick API and troubleshooting | `docs/get-started/quickstart_classification.md:48-52`, `docs/get-started/index.md:17-20` | Concrete next links exist | Several possible next steps are presented without a single “continue here” recommendation | High |

### Beginner readability observations

1. **The route is discoverable.** The homepage provides a direct new-user
   pointer, and the Get started hub immediately lists runnable quickstarts.
2. **The first example is complete.** The classification quickstart includes
   installation, data splitting, fitting, calibration, factual explanations,
   alternatives, and next steps.
3. **Calibration is visible but not introduced.** The quickstart accurately
   requires a proper training split and held-out calibration split, but the
   student first encounters this as procedure rather than as an explanation of
   why calibration is needed.
4. **Uncertainty is documented responsibly.** The semantics page distinguishes
   the three modes and states assumptions and non-guarantees. This is strong
   technical guidance, but its placement and terminology are more suitable
   after a first worked example.
5. **The onward path is fragmented.** Interpretation, alternatives, semantics,
   Quick API, and citing are all valid destinations, but the student is not
   told which one to choose next.

## Persona B - ML practitioner

### Walkthrough summary

The practitioner can determine that CE supports classification, interval
regression, probabilistic/thresholded regression, factual explanations,
alternative explanations, and guarded explanations. The clearest route is:

`docs/index.md` -> `docs/practitioner/index.md` ->
`docs/tasks/index.md` or a task quickstart ->
`docs/foundations/how-to/integrate_with_pipelines.md` and
`docs/foundations/how-to/interpret_explanations.md` ->
`docs/foundations/concepts/calibrated_interval_semantics.md`

The practitioner value proposition is implied by the workflows and capability
map rather than stated directly on the homepage. Integration and limitations
guidance exists, but it is distributed across task, how-to, and concepts pages.

### Evidence table

| User goal | Expected navigation path | Actual available path | Source and lines | Clear information | Possible friction | Confidence |
|---|---|---|---|---|---|---|
| Understand CE's potential value | Homepage -> practitioner hub -> interpretation/capabilities | Practitioner hub promises task quickstarts, interpretation, and deployment playbooks; interpretation explains calibrated predictions, intervals, rules, and alternatives | `docs/practitioner/index.md:1-11`, `docs/foundations/how-to/interpret_explanations.md:1-16` | The practical workflow and output types are clear after opening the hub | Homepage does not summarize the value for someone who already has a model | High |
| Identify supported prediction tasks | Practitioner hub -> tasks/capability map | Tasks hub lists classification, regression, and probabilistic regression; capabilities maps each to an entry point | `docs/tasks/index.md:1-14`, `docs/tasks/capabilities.md:1-21` | Supported modes and primary pages are explicit | The homepage itself does not expose the capability map; a practitioner must discover the task hub | High |
| Find integration guidance | Practitioner hub -> integration how-to | Pipeline integration page explains preprocessing, `WrapCalibratedExplainer.from_config`, fit, calibrate, and inference | `docs/practitioner/index.md:3-11`, `docs/foundations/how-to/integrate_with_pipelines.md:1-6`, `docs/foundations/how-to/integrate_with_pipelines.md:48-67` | A concrete scikit-learn pipeline path is available | Integration is not linked from the homepage or practitioner core path; it is found through foundations navigation | Medium |
| Locate interpretation guidance | Practitioner hub -> interpretation | Practitioner core path explicitly sends users to interpretation after a task quickstart | `docs/practitioner/index.md:5-8` | The recommended sequence is concise and actionable | The user must already select a task before reaching interpretation | High |
| Locate limitations and assumptions | Practitioner hub -> semantics | Practitioner hub links to mode-specific semantics; semantics states exchangeability/distribution-match assumptions and drift/non-causal limits | `docs/practitioner/index.md:11`, `docs/foundations/concepts/calibrated_interval_semantics.md:5-18`, `docs/foundations/concepts/calibrated_interval_semantics.md:51-60` | Limitations are explicit and technically careful | The word “semantics” may not signal “limitations and assumptions” to a practitioner scanning navigation | High |

### Practitioner readability observations

1. **Task coverage is strong once the user reaches the task hub.** The
   capability table gives a compact answer to “does CE support my task?”
2. **The practitioner path is better sequenced than the general homepage.**
   It explicitly recommends quickstart -> interpretation -> API style ->
   production playbooks.
3. **Value is demonstrated rather than stated.** A practitioner can see what CE
   produces, but must read interpretation material to connect those outputs to
   practical use.
4. **Integration guidance is concrete but not prominent.** The pipeline page
   directly addresses a common existing-model workflow, yet it is not part of
   the homepage’s visible routing.
5. **Limitations are present and trustworthy.** The semantics page avoids one
   universal guarantee statement and clearly separates mode-specific claims.
   The navigation label could make this guidance easier to recognize.

## Overall conclusion

Both personas can reach relevant material without a missing conceptual section:

- The student has a runnable first example and a technically sound route into
  interpretation and uncertainty.
- The practitioner has task coverage, integration guidance, interpretation
  guidance, and limitations guidance.

The main readability issue is not absent content. It is **orientation**:
the homepage does not explain CE's purpose in beginner language, choose a
first quickstart, or show one short next-step sequence. These are source-review
observations and should be validated with actual readers before implementation.

