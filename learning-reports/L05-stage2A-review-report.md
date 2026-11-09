# L05 Stage 2A Review Report

## Completion status

Stage 2A design and planning is complete. The homepage was not implemented.

## Files updated or created

Updated:

- `learning-reports/L05-homepage-wireframe.md`
- `learning-reports/L05-five-door-navigation-design.md`
- `learning-reports/L05-link-and-evidence-map.md`
- `LEARNING_JOURNAL.md`

Created:

- `learning-reports/L05-stage2A-implementation-specification.md`
- `learning-reports/L05-stage2A-review-report.md`

No files under `docs/`, `README.md`, `src/` or Sphinx configuration were
modified. No dependencies were installed, builds were run, files staged or
commits created.

## Evidence and method

The mapping was based on the L04 inventory, gap analysis and resource
verification, then checked against the current homepage, foundations,
quickstarts, tasks, practitioner, researcher, contributor, API, roadmap,
release and source architecture files.

Architecture boundaries were checked against:

- `docs/foundations/concepts/architecture.md:1-120`
- `src/calibrated_explanations/core/wrap_explainer.py:147-821`
- `src/calibrated_explanations/plugins/manager.py:145-554`
- `docs/api/index.md:1-10`

## Navigation destinations verified

The final map covers **27 sub-doors plus 5 main door cards**.

For the 27 sub-doors:

- **11**: existing and suitable.
- **12**: existing but needs improvement.
- **1**: new navigation landing page required.
- **1**: future educational content.
- **2**: external resource requiring verification.

Thus, **24 of 27 sub-door entries have repository-backed destinations or
evidence**, while the two external destinations remain only repository-documented
URLs and the future/new entries are intentionally not treated as verified
current pages. The five main doors have evidence-backed routing except Door 5,
which lacks one suitable consolidated landing page.

## Missing or unsuitable destinations

- No general AI/ML primer suitable for Door 1.1.
- No single Door 5.1 vision/origins/history landing page.
- No dedicated isotonic-regression educational page.
- No verified browser upload or Decision Labs own-data workflow.
- No single stable-version answer: local `1.1.0-dev`, citation `v1.0.2`,
  homepage `1.0.0`.
- No documentation build or external runtime verification was performed.

## Important architectural decisions requiring approval

1. Implement five doors as homepage navigation, not new physical directories.
2. Keep Door 4.3 internal architecture separate from Door 4.4 public API.
3. Keep Door 3.3 as a local Python workflow and avoid upload wording.
4. Treat Door 5.1 as a future landing-page decision, not an invented target.
5. Preserve audience and task routes alongside the five doors.
6. Reconcile release wording before presenting a current stable version.

## Recommended Stage 2B scope

If approved, make one incremental change to `docs/index.md` using the
implementation specification. Start with the header, five doors, qualified
links and preserved existing routes. Defer new educational and project-history
pages until separately approved.

## Next step

Wait for project-owner and ChatGPT review. Do not implement Stage 2B until the
approval gates in the implementation specification are resolved.

