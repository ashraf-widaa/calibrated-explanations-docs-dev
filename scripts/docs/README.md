# Documentation scripts

Maintainer tools for the documentation in `docs/`. They are not part of the
published site.

## `build_quickstart_walkthrough.py`

Generates the Quick Start walkthrough from executed notebook cells:

- `docs/get-started/quickstart_walkthrough.md` (the published page);
- `docs/get-started/walkthrough_assets/*.png` (figures);
- `docs/_static/notebooks/quickstart_walkthrough.ipynb` (the download).

**Edit the cells in this script, never the generated page.** Regenerate from
the repository root:

```bash
PYTHONPATH=src python scripts/docs/build_quickstart_walkthrough.py
```

Requirements: `nbformat`, `nbclient`, a Jupyter kernel named `python3`,
scikit-learn and matplotlib. Figures are git-ignored (`*.png`); add a changed
figure with `git add -f`.

**Safety checks built in:**

- Generation stops if a cell raises an error.
- Generation stops if a number quoted in the prose (`PROSE_NUMBERS`) does not
  appear in the executed outputs, so the text cannot silently go stale when
  CE's behaviour changes.

Related tests:

- `tests/docs/get_started/test_walkthrough_content.py` (section order and
  scientific wording);
- `tests/docs/get_started/test_quickstart_continuity.py` (generator and page
  stay in sync).

The teaching design follows
`learning-reports/quickstart-walkthrough-audit/05-content-specification.md`
(rev. 2).

## `check_internal_links.py`

Checks every internal link and `#anchor` in a built HTML site, and optionally
lists pages added or removed compared with a baseline build:

```bash
python -m sphinx -W --keep-going -E -b html docs _build/html
python scripts/docs/check_internal_links.py _build/html [_build/html-baseline]
```

It exits with status 1 when a link is broken. External links are not checked;
use `sphinx -b linkcheck` for those.

## `capture_browser_quickstart.py`

Re-creates the five Expert Hub screenshots of the browser Quick Start
(`docs/get-started/try-in-browser.md`) by driving the live application with
Playwright. It is a **manual** tool: it is not run by the Sphinx build, CI or the
documentation tests.

```bash
python -m pip install playwright pillow
python -m playwright install chromium
python scripts/docs/capture_browser_quickstart.py --out-dir _build/screenshots-new
```

- It refuses to write into `docs/_static/screenshots/` and never overwrites files
  unless `--overwrite` is given. Compare the new images and copy the approved ones by
  hand (`git add -f`, because `*.png` is ignored).
- When an application label changes, it stops and names the failed step.
- Decision Lab screenshots vary per session and are captured by hand; the checklist is
  in the script's docstring.
- After re-capturing, update the capture date in the Quick Start captions and check
  the callout positions.

## Recommended validation before publishing documentation

1. Strict build: `python -m sphinx -W --keep-going -E -b html docs _build/html`
   (add `CE_DOCS_BETA=true` to build the Beta variant with its banner and
   footer marker).
2. Documentation tests: `pytest tests/docs tests/scripts/test_check_parameter_naming.py`.
3. Internal links: `python scripts/docs/check_internal_links.py _build/html`.
