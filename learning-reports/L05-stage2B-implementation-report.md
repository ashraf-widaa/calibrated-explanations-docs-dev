# L05 Stage 2B - Homepage Navigation Implementation Report

Date: 2026-11-08  
Status: Implemented and visually refined; awaiting review

## 1. Exact files changed

Public documentation:

- `docs/index.md`

Learning record:

- `learning-reports/L05-stage2B-implementation-report.md`
- `LEARNING_JOURNAL.md`

No other public documentation, README, Sphinx configuration or source files
were modified. No dependencies were installed, files were staged, commits were
created, or remotes were changed.

## 2. Final rendered link status for all 27 sub-doors

| # | Sub-door | Final rendered destination/status |
|---|---|---|
| 1.1 | Understanding AI Models | **Future educational content:** no link; existing task hub is mentioned as supporting context |
| 1.2 | Can We Trust AI Outputs? | **Existing but needs improvement:** `{doc}` link to `foundations/concepts/calibrated_interval_semantics` |
| 1.3 | Trustworthy AI | **Existing but needs improvement:** qualified `{doc}` link to the contextual EU AI Act page |
| 1.4 | The Explainability Gap | **Existing but needs improvement:** README and `{doc}` comparison links |
| 1.5 | What Is CE & What Does It Add? | **Existing but needs improvement:** capabilities and semantics `{doc}` links |
| 2.1 | Essential Foundations | **Existing but needs improvement:** foundations hub and classification quickstart links |
| 2.2 | Calibration & Uncertainty | **Existing but needs improvement:** classification quickstart and canonical semantics links |
| 2.3 | Statistical Methods Behind CE | **Existing but needs improvement:** probabilistic regression and researcher theory links; isotonic tutorial explicitly absent |
| 2.4 | How CE Explanations Work | **Existing and suitable:** interpretation and alternatives links |
| 2.5 | Assumptions & Guarantees | **Existing and suitable:** canonical semantics link |
| 3.1 | CE Examples for New Users | **External resource requiring verification:** illustrative browser demo URL, with runtime/upload caveat |
| 3.2 | Explore Use-Case Examples | **External resource requiring verification:** external Decision Labs URL, with functionality/integration caveat |
| 3.3 | Test CE with Your Own Data | **Existing but needs improvement:** local pipeline, Quick API and notebook links; explicitly not browser upload |
| 3.4 | Practical Workflows | **Existing and suitable:** Get started, tasks and practitioner hub links |
| 3.5 | Evaluate & Compare | **Existing but needs improvement:** comparison and semantics links; benchmark limitation stated |
| 4.1 | Software Overview & Versions | **Existing but needs improvement:** capabilities, changelog and upgrade links; version conflict stated |
| 4.2 | Installation & Configuration | **Existing and suitable:** canonical installation link |
| 4.3 | Internal Software Architecture | **Existing and suitable:** prominent, separate architecture link |
| 4.4 | API & Technical Reference | **Existing and suitable:** public API and Quick API links |
| 4.5 | Model & Pipeline Integration | **Existing and suitable:** pipeline integration link |
| 4.6 | Extensions & Customization | **Existing and suitable:** plugins, plugin API and contributor contract links |
| 4.7 | Troubleshooting & Upgrades | **Existing and suitable:** troubleshooting, migration and upgrade links |
| 5.1 | Vision, Origins & History | **New landing page required:** qualified README link; dedicated history landing page explicitly identified as unavailable |
| 5.2 | Research & Publications | **Existing and suitable:** researcher, citation and replication links |
| 5.3 | Development & Roadmap | **Existing but needs improvement:** public roadmap, changelog and migration links; maintainer plans qualified |
| 5.4 | Community & Contributions | **Existing and suitable:** contributor hub and contribution guide links |
| 5.5 | CE Ecosystem | **Existing but needs improvement:** plugins and external-plugin appendix links; library/companion/commercial separation stated |

The implementation includes all five main door sections in the approved order.
Door 4 has a separate `Internal Software Architecture` heading and direct
link to `foundations/concepts/architecture`.

## 2a. Visual refinement

The long bullet descriptions were replaced with compact semantic definition
lists. Each entry has a bold navigation label followed by one concise
supporting phrase. Verified destinations use linked labels; Door 1.1 and Door
5.1 remain deliberately non-clickable because no suitable destinations exist.
Multiple-destination entries keep a primary link and a small set of named
secondary links.

The Sphinx configuration enables `myst_parser`, but it does not configure a
card/grid extension, and no card/grid directive is established elsewhere in
the repository. No new extension or CSS was added. The definition-list
fallback is responsive in normal document flow and remains keyboard- and
screen-reader-accessible without presentation dependencies.

## 3. Documentation build results and warnings

No Sphinx build was run because `sphinx-build` is unavailable in the current
environment. `make` is also unavailable, so the repository Makefile validation
targets could not be used. No dependency installation was performed, as
required.

Static validation performed:

- All 27 approved sub-door labels are present in `docs/index.md`.
- All 31 referenced local documentation targets checked by the static target
  probe exist.
- The homepage contains five H2 door headings and 27 compact navigation
  entries.
- No unsupported card/grid directive or custom CSS was introduced.
- `git diff --check` passes after removing unintended trailing whitespace.
- The browser demo and Decision Labs links remain explicitly external and
  qualified.
- No browser upload, regulatory compliance, ownership, endorsement or
  unqualified current-version claim was added.

## 4. Unresolved destination or rendering issues

- Sphinx/MyST rendering, warnings and generated navigation were not verified.
- External browser demo and Decision Labs availability and runtime behavior were
  not tested.
- The repository still contains inconsistent version references: homepage
  `1.0.0`, citation metadata `v1.0.2`, and local package metadata `1.1.0-dev`.
- Door 1.1 remains future educational content.
- Door 5.1 has no dedicated history landing page.
- Notebook README linking is a repository link rather than a verified published
  documentation destination.
- The definition-list appearance was not inspected in generated HTML because
  Sphinx is unavailable.

## 5. Actual git diff summary

The homepage diff is:

```text
docs/index.md | 171 insertions(+), 31 deletions(-)
```

The change replaces the former short audience-first introduction with the
approved header, five doors, 27 compact semantic navigation entries, guided
learning paths and preserved audience/toctree navigation. Existing release and
ecosystem notices were retained with the approved qualification language.

## Review gate

Stop here for project-owner and ChatGPT review. Do not make further public
documentation changes until the unresolved rendering, external-resource and
version questions are reviewed.
