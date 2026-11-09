# L05 Stage 2C - Sphinx-Design Integration and Homepage Navigation Cards

Date: 2026-11-09  
Status: Implemented and validated locally; awaiting Product Owner review

The homepage now has five door sections and 27 `sphinx-design` cards. The
strict build using the project's pinned documentation versions finished with
zero warnings. Read the Docs (RTD) deployment has not been tested.

## 1. Files changed

| File | Change | Why |
|---|---|---|
| `docs/index.md` | Replaced inline-styled HTML blocks with five `grid` directives and 27 `grid-item-card` directives; removed redundant navigation text | Task 3 and Task 4 |
| `docs/requirements-doc.txt` | Changed `sphinx-design` to `sphinx-design==0.6.1` | Every other doc tool that affects rendering is pinned; RTD installs this file |
| `learning-reports/L05-stage2C-implementation-report.md` | New report | Task 6 |
| `LEARNING_JOURNAL.md` | Added the Stage 2C entry | Task 6 |

These changes were already in the working tree before this stage and were kept
unchanged:

- `docs/conf.py`: `sphinx_design` already enabled.
- `pyproject.toml`: `sphinx-design` already in the `dev` extra, unpinned like
  the other doc tools in that list.

No theme, custom CSS, JavaScript, directory structure or source code was
changed. Nothing was staged, committed or pushed.

## 2. Compatibility findings

| Question | Finding |
|---|---|
| Was `sphinx-design` declared? | Yes, in `docs/requirements-doc.txt` (unpinned), `pyproject.toml` and `docs/conf.py` |
| Was it installed? | Not in `.venv-docs`; a build there would have failed until it was added |
| Which file does RTD install? | `docs/requirements-doc.txt` (`.readthedocs.yaml`), on Python 3.11 |
| Is it compatible? | Yes. `sphinx-design` 0.6.1 installed alongside Sphinx 7.4.7, docutils 0.21.2 and Furo 2025.12.19, and `pip check` reported no broken requirements |
| Extra configuration needed? | None. The existing `colon_fence` MyST extension is enough |
| Does the local environment match RTD? | **No** (see below) |

| Component | RTD / pinned | `.venv-docs` |
|---|---|---|
| Python | 3.11 | 3.13.7 |
| Sphinx | 7.4.7 | 9.2.0 |
| MyST parser | 3.0.1 | 5.1.0 |
| docutils | 0.21.2 (resolved) | 0.22.4 |
| sphinx-design | 0.6.1 | 0.7.0 |
| numpy | installed | **missing** |

This mismatch did not block the work, but it means a `.venv-docs` build is not
evidence for RTD. I therefore built in two environments:

- **Pinned environment:** a temporary venv outside the repository, installed
  from `docs/requirements-doc.txt` with `constraints.txt`. Python 3.11 is not
  installed on this machine, so it used Python 3.10.
- **`.venv-docs`:** the only change was adding `sphinx-design`. Version 0.7.0
  was installed because pip selected it for this environment's Sphinx 9.2.

## 3. Homepage card implementation

- Each door uses `::::{grid} 1 2 3 3` with `:gutter: 3`: one column on narrow
  screens, two on small screens, three on medium and larger screens.
- Clickable cards use the whole-card `:link:` option, with `:link-type: doc`
  for internal pages and `url` for external ones. Missing internal targets
  would therefore be reported by the build.
- Internal Software Architecture keeps its approved position and has a primary
  coloured border and a larger shadow, using built-in classes only.
- Whole-card links cannot safely contain other links, so each clickable card
  now has one destination. Removed links are listed in section 7.

Removed text: the "five doors below" instruction, Door 2's sentence about not
repeating Door 1, and long card descriptions.

Kept: title, subtitle, introduction, GitHub link, both notices, guided learning
paths, the semantics paragraph, all toctrees, and caveats on semantics,
external demos, EU AI Act context, benchmarks and version references.

| # | Card | Destination |
|---|---|---|
| 1.1 | Understanding AI Models | Non-clickable, labelled **Planned** |
| 1.2 | Can We Trust AI Outputs? | `foundations/concepts/calibrated_interval_semantics` |
| 1.3 | Trustworthy AI | `practitioner/playbooks/eu-ai-act-compliance` |
| 1.4 | The Explainability Gap | `compare` |
| 1.5 | What Is CE & What Does It Add? | `tasks/capabilities` |
| 2.1 | Essential Foundations | `foundations/index` |
| 2.2 | Calibration & Uncertainty | `foundations/concepts/calibrated_interval_semantics` |
| 2.3 | Statistical Methods Behind CE | `foundations/concepts/probabilistic_regression` |
| 2.4 | How CE Explanations Work | `foundations/how-to/interpret_explanations` |
| 2.5 | Assumptions & Guarantees | `foundations/concepts/calibrated_interval_semantics` |
| 3.1 | CE Examples for New Users | External: `https://calibrated-explanations-demo.ju.se/` |
| 3.2 | Explore Use-Case Examples | External: `https://games.grejna.ai/` |
| 3.3 | Test CE with Your Own Data | Interim: `foundations/how-to/integrate_with_pipelines` |
| 3.4 | Practical Workflows | `get-started/index` |
| 3.5 | Evaluate & Compare | `compare` |
| 4.1 | Software Overview & Versions | `tasks/capabilities` |
| 4.2 | Installation & Configuration | `get-started/installation` |
| 4.3 | Internal Software Architecture | `foundations/concepts/architecture` |
| 4.4 | API & Technical Reference | `api/index` |
| 4.5 | Model & Pipeline Integration | `foundations/how-to/integrate_with_pipelines` |
| 4.6 | Extensions & Customization | `plugins` |
| 4.7 | Troubleshooting & Upgrades | `get-started/troubleshooting` |
| 5.1 | Vision, Origins & History | Non-clickable, labelled **No dedicated page yet**, with an inline README link |
| 5.2 | Research & Publications | `researcher/index` |
| 5.3 | Development & Roadmap | `ROADMAP` |
| 5.4 | Community & Contributions | `contributor/index` |
| 5.5 | CE Ecosystem | `plugins` |

## 4. Validation results

Both builds set `READTHEDOCS=True`, so notebooks were not executed, matching
RTD behaviour in `docs/conf.py`.

| Check | Pinned environment | `.venv-docs` |
|---|---|---|
| Command mode | `-E -W --keep-going` (strict) | `-E --keep-going` |
| Result | Build succeeded | Build succeeded |
| Warnings / errors | **0** | 20, all autodoc import failures from missing `numpy` |
| Output | Temporary directory | `_build/html/index.html` exists |
| Card structure | 5 grids, 27 `sd-card`, labels in approved order | Same |
| Plain lists inside door sections | 0 | Not separately checked |
| Internal card targets | 23 of 23 exist | 0 missing |

The 20 warnings in `.venv-docs` do not involve the homepage, but API pages in
`_build/html` are missing their autodoc content in that build.

External URLs from the homepage, requested once with a basic HTTP client; all
returned HTTP 200:

- `https://calibrated-explanations-demo.ju.se/`
- `https://games.grejna.ai/`
- `https://github.com/Moffran/calibrated_explanations` and its `#readme` link
- `https://github.com/Moffran/calibrated_explanations/blob/main/CHANGELOG.md`
- `https://grejna.ai/` (see issue 3 in section 7)

HTTP 200 shows that a page responded. It does not verify demo functionality,
data upload or CE integration.

Visual check: headless Edge screenshots of the pinned build, light theme.

- 1400px wide: three-column grids, consistent spacing and a distinct
  Architecture card.
- 500px wide: one column.

## 5. RTD compatibility and remaining uncertainty

Evidence for compatibility: `.readthedocs.yaml` installs the file containing the
new pin, the same pins build strictly with no warnings, and no RTD configuration
change is needed.

Not verified:

- An actual RTD build or deployment.
- Python 3.11 (the pinned build used 3.10).
- The CI docs job in full: it also installs `requirements.txt` and, without
  `READTHEDOCS`, executes notebooks.
- `make local-checks-pr`, which was not run.
- Dark theme, the two-column breakpoint, hover states, real-browser clicks and
  screen-reader behaviour.

## 6. Accessibility note

Whole-card link text comes from the target page title or URL and is visually
hidden. A screen reader may announce, for example, "Capabilities manifest" for
a card titled "What Is CE & What Does It Add?", or a raw URL for the external
cards. The `:link-alt:` option could supply the card label if wanted.

## 7. Issues for Product Owner review

Decisions needed:

1. **Card 3.3 interim link.** It was non-clickable, with supporting links, in
   the previous version. It now links to pipeline integration, labelled
   "Interim route". Keep it, or return it to a placeholder?
2. **Seven links no longer appear in the homepage content:** alternative
   explanations, Quick API, the notebooks folder, the plugin API, the
   contributor plugin contract, `CONTRIBUTING.md` and the external plugin
   appendix. The pages themselves were not changed. Should any return, for
   example in a short list under a door?

Follow-up issues, not changed in this stage:

3. **Malformed Grejna link in the existing notice.** Under the pinned MyST
   3.0.1 build, `&` in the `grejna.ai` URL is double-escaped (`&amp;amp;`) in
   the HTML. The page loads, but its `utm_medium` and `utm_campaign` parameters
   are malformed. The MyST 5.1 build escapes it correctly.
4. **Version claims conflict.** The homepage notice says `1.0.0` stable,
   citation metadata says `v1.0.2`, and the site title shows `v1.1.0.dev0`.
5. **`.venv-docs` differs from the pins and lacks `numpy`.** Recommendation:
   rebuild it from `docs/requirements-doc.txt` so local previews match RTD.
6. **Sidebar duplicate.** "Roadmap" appears twice in the rendered sidebar. The
   toctrees were not edited in this stage; the cause has not been investigated.
7. **Content still missing.** Door 1.1 needs educational content and Door 5.1
   needs a history page.

## Review gate

Stop here for Product Owner visual review before any publication to Read the
Docs.
