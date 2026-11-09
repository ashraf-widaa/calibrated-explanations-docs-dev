# L04 Addendum - Interactive Resources, Ecosystem and Software Verification

Date: 2026-11-08  
Status: Read-only verification completed; no implementation performed

## 1. Executive summary

The repository verifies four resource categories relevant to the five-door
architecture:

1. An external browser demo is linked from the README, homepage, Get started
   page, package metadata, and the static landing page. The repository
   describes it as an illustrative, no-installation companion with guided and
   expert interfaces, but does not independently verify its current runtime
   behavior.
2. Decision Labs is linked as a separate external resource for simulated
   learning scenarios. The inspected repository does not establish its exact
   functionality, data-upload support, ownership, or CE workflow.
3. The repository contains executable Jupyter notebooks, including tiny
   quickstarts, classification/regression demos, and advanced developer demos.
   `notebooks/README.md` documents their learning path, but the main homepage
   does not directly link to that README.
4. No verified repository/documentation workflow was found for uploading or
   testing a user's own data through a browser or Decision Labs. The documented
   route for custom data is local Python use through the public API and
   integration guides.

The checked-out software is development version `1.1.0-dev`
(`pyproject.toml:7-12`; fallback `1.1.0.dev0` in
`src/calibrated_explanations/__init__.py:16-28`). Release evidence identifies
`v1.0.2` as the released citation version (`CITATION.cff:68-69` and
`CHANGELOG.md:20-25`), while the documentation homepage still labels `1.0.0`
as stable (`docs/index.md:13-23`). This is a version-context discrepancy, not
evidence that a build or published site has been verified.

## 2. Evidence table

| Resource or topic | Verified evidence | Intended audience/purpose | Classification | Installation/coding/data requirement | Discoverability | Verification limitation |
|---|---|---|---|---|---|---|
| Calibrated Explanations browser demo | README calls it an interactive web demo and says it has a guided workflow and expert interface (`README.md:22-24`, `README.md:317`); homepage repeats the browser route (`docs/index.md:36-45`); package metadata exposes the Demo URL (`pyproject.toml:31-38`) | New users, practitioners and demonstrators; explore CE without local installation | Repository-linked external companion; current ownership not established by this inspection | No local installation is stated as required; no upload or data workflow is documented | High: README, homepage, Get started, metadata and landing page | No external service was opened or executed; current functionality and availability remain unverified |
| Decision Labs | README links the name to `https://games.grejna.ai/` (`README.md:12`); homepage calls it a resource for “simulated learning scenarios” (`docs/index.md:28-34`); static site links “Explore Decision Labs” (`site/index.html:62-63`) | Simulated learning scenarios; exact audience and activities are not specified | External resource linked by the repository; not enough evidence to classify ownership or endorsement | No installation, coding, or data-upload requirement is documented | Medium: README, homepage and static landing page | No repository evidence verifies its actual name beyond “Decision Labs,” functionality, CE integration, upload support, or current availability |
| `notebooks/quickstart_tiny.ipynb` | Listed as a 2–5 minute tiny quickstart using scikit-learn toy data (`notebooks/README.md:5-7`) | Beginners and fast demonstrations | Repository resource | Requires notebook environment and the notebook extras; uses toy data | Medium: documented in `notebooks/README.md`, not in homepage toctrees | Notebook execution was not run in this task |
| `notebooks/quickstart.ipynb` | Listed as a 5–10 minute classification/regression quickstart with plotting and uncertainty (`notebooks/README.md:8-9`) | Beginners/practitioners | Repository resource | Requires notebook environment; local code/data | Medium: notebook README only | Execution and outputs were not verified |
| `notebooks/core_demos/*.ipynb` | README lists binary, multiclass, regression and probabilistic regression demos (`notebooks/README.md:11-20`); files exist under `notebooks/core_demos/` | Practitioners learning task workflows | Repository resources | Requires notebook environment; coding and example data | Medium: notebook README and cross-references in docs | Execution was not run |
| `notebooks/advanced/*.ipynb` | README lists conditional, reject, narrative, feature-filtering, internals and plugin demos (`notebooks/README.md:22-33`) | Advanced practitioners and developers | Repository resources | Requires notebook environment and relevant optional dependencies | Low-medium: advanced notebook README route | Execution and dependency compatibility were not verified |
| Static landing page | `site/index.html` provides links to source, documentation, browser demo, Grejna AB and Decision Labs (`site/index.html:8-10`, `site/index.html:50-63`); visual explicitly says it is conceptual and not an empirical guarantee (`site/index.html:22-23`) | Public orientation and ecosystem routing | Repository static site, not a CE execution environment | No CE execution or data upload is implemented in the inspected HTML | Not part of `docs/` toctree; repository file only | Static HTML inspection cannot establish external link behavior |
| Try CE with your own data | No upload/import workflow was found in the inspected docs, README, site or resource inventory; local API and pipeline guides exist (`docs/foundations/how-to/integrate_with_pipelines.md:1-67`) | Practitioners with an existing model/data pipeline | Not found as an interactive resource; local-code route exists | Local Python coding is documented; browser upload is not documented | Low for a dedicated “own data” path | Absence is limited to inspected repository evidence; no external service was tested |

## 3. Verified interactive resources and guided examples

### Browser demo

The browser demo URL is:

`https://calibrated-explanations-demo.ju.se/`

The repository describes it consistently as an interactive web demo and
illustrative companion. The homepage says users can explore a guided workflow
or expert interface without installing locally, while versioned documentation
remains authoritative for APIs, assumptions and guarantees
(`docs/index.md:36-45`). The README uses the same no-installation framing
(`README.md:22-24`).

**Verified status:** The link and documented description are verified in the
repository. Runtime availability, current screens, supported inputs, upload
capability and data handling were not verified.

### Decision Labs

The exact repository-visible name is **Decision Labs**. Its URL is:

`https://games.grejna.ai/`

The only documented purpose found is “simulated learning scenarios”
(`docs/index.md:28-34`). It is linked alongside the CE demo and Grejna AB
references, but no inspected source describes specific games, CE functionality,
user data handling, or upload support.

**Verified status:** A named external link and high-level purpose are verified.
Functionality and relationship to CE beyond the link are unresolved.

### Notebooks and guided examples

The repository contains:

- `notebooks/quickstart_tiny.ipynb`
- `notebooks/quickstart.ipynb`
- `notebooks/quickstart_guarded.ipynb`
- `notebooks/core_demos/`
- `notebooks/advanced/`
- `notebooks/paper_based/`
- `notebooks/miscellaneous/`

`notebooks/README.md:1-45` provides a learning path with estimated durations,
audiences and task categories. The installation page documents a
`notebooks` extra for Jupyter tutorials (`docs/get-started/installation.md:7-20`).
The repository also configures `nbsphinx` and notebook execution policy in
`docs/conf.py:229-250`, but the inspected homepage toctrees do not directly
include the notebook README.

**Verified status:** Repository notebook files and their documented learning
path exist. Their execution, outputs and current dependency compatibility were
not tested.

### Other interactive demonstrations

The inspected repository contains the static landing page at
`site/index.html`, but it is a link hub and conceptual presentation rather than
an additional CE execution environment. Its visual is explicitly labelled
“Conceptual image only; not an empirical coverage guarantee”
(`site/index.html:22-23`).

No other interactive browser or local data-upload demonstration was found in
the inspected repository inventory.

## 4. Grejna AB findings

The repository distinguishes the open-source CE library from commercial
services:

- `README.md:3` describes CE as a BSD-licensed Python library.
- `README.md:9-12` separates “Open source,” “Live demo,” and “Commercial
  solutions,” linking Grejna AB separately.
- `docs/index.md:25-34` calls CE an independent BSD-licensed open-source
  project and describes optional commercial integration, operational deployment
  or pilot discussions as separate from the open-source library and license.
- `site/index.html:50-63` presents Grejna AB as an optional commercial
  solutions route and keeps the OSS library distinct.
- `SUPPORT.md:14` directs commercial/support enquiries to Grejna AB.

### Evidence-based relationship statement

The documentation supports saying that Grejna AB is a separate organization
linked for optional commercial integration, operational deployment or pilot
discussions. It does **not** support inferring ownership of the CE library,
endorsement of Decision Labs, a particular commercial product capability, or a
guaranteed service relationship.

### Recommended placement

- **Door 3:** Place the browser demo and Decision Labs under practical
  exploration, with explicit labels distinguishing the CE demo from simulated
  learning scenarios. Keep Grejna AB as a separate optional commercial link,
  not as a CE usage requirement.
- **Door 5:** Place Grejna AB in an ecosystem/related-organizations section
  alongside the open-source repository and other documented companion projects.
  State the separation between the BSD-licensed library and optional services.

## 5. Version and installation findings

### Version context

| Evidence | Finding |
|---|---|
| `pyproject.toml:7-12` | Checked-out package metadata is `1.1.0-dev`, requiring Python `>=3.10` |
| `src/calibrated_explanations/__init__.py:16-28` | Uninstalled fallback version is `1.1.0.dev0` |
| `development/current-work/v1.1.0_plan.md:1-20` | `1.1.0` is the active development plan |
| `CITATION.cff:68-69` | Citation metadata identifies released version `v1.0.2` on 2026-10-20 |
| `CHANGELOG.md:20-25` | Changelog has a `v1.0.2` release section dated 2026-10-20 |
| `docs/index.md:13-23` | Homepage still presents `1.0.0` as the stable release |
| `docs/get-started/installation.md:40-43` | Installation verification text says package-manager version `1.0.0` or later |

The safest current description is therefore: **the local checkout is
1.1.0-dev; repository release evidence identifies v1.0.2 as the latest
documented release metadata; some public documentation still refers to 1.0.0
as stable and should be reconciled before making release claims.**

Users should find the current published package version through the PyPI
project link and conda-forge link in `README.md:15-17` and the package's
`project.urls` in `pyproject.toml:31-38`. This task did not query those
external services.

### Installation and compatibility

Canonical user installation is:

```bash
pip install calibrated-explanations
```

This is documented in `docs/get-started/installation.md:1-10` and
`README.md:291-299`. A conda-forge method is also documented:

```bash
conda install -c conda-forge calibrated-explanations
```

(`docs/get-started/installation.md:22-29`).

The repository documents:

- Python `>=3.10` (`pyproject.toml:10`; `README.md:294-299`).
- scikit-learn `>=1.3`, crepes `>=0.8.0`, venn-abers `>=1.4.0`, numpy
  `>=1.24`, and pandas `>=2.0` (`pyproject.toml:13-19`; `README.md:294-299`).
- Optional `matplotlib` for plotting (`README.md:299`).
- Optional `viz`, `notebooks`, `dev` and `external-plugins` installation
  extras (`docs/get-started/installation.md:11-20`).
- Editable contributor installation through pip, with uv as an optional
  constrained workflow (`docs/get-started/installation.md:31-53`).

Canonical supporting pages are:

- Installation: `docs/get-started/installation.md`
- Troubleshooting: `docs/get-started/troubleshooting.md`
- Release notes: `CHANGELOG.md` and `docs/foundations/governance/release_notes.md`
- Migration: `docs/migration/index.md`
- Upgrade checklists: `docs/upgrade/index.md`
- Release procedure: `release.md`

No installation, environment setup, or package verification was executed in
this addendum.

## 6. Updated Door 3, 4 and 5 mapping

| Target architecture item | Status | Verified resource/page | Recommendation |
|---|---|---|---|
| **3.1 Discover CE Applications** | Existing but needs clarification | README problem statement/output examples (`README.md:28-84`), practitioner playbooks and task capabilities | Link the capability map and practical use cases; avoid presenting illustrative output as empirical evidence |
| **3.2 Learn by Doing - Interactive Demo** | Verified existing resource | Browser demo URL and description (`docs/index.md:36-45`; `README.md:22-24`) | Link as an illustrative no-installation companion and keep versioned docs authoritative |
| **3.2 Learn by Doing - Decision Lab** | Existing but needs clarification | Decision Labs link and simulated-learning description (`docs/index.md:28-34`; `README.md:12`) | Link with the exact documented purpose only; do not claim CE features, uploads or ownership |
| **3.2 Learn by Doing - Try CE with Your Own Data** | Not found | Local pipeline integration is documented (`docs/foundations/how-to/integrate_with_pipelines.md:1-67`) | Route users to local Python/API integration; treat browser upload as a proposed future capability only if confirmed later |
| **3.3 Practical Guides** | Verified existing resource | Get started, quickstarts, task pages and foundations how-to index (`docs/get-started/index.md:1-30`; `docs/foundations/how-to/index.md:1-18`) | Preserve existing routes; add notebook link only if desired |
| **3.4 Evaluate & Compare** | Existing but needs clarification | `docs/compare.md`, researcher theory/literature and notebook README | Add a clearer comparison/evaluation label; distinguish source-based comparison from executed benchmark evidence |
| **4.2 Versions and Releases** | Existing but needs clarification | `CHANGELOG.md`, `CITATION.cff`, upgrade/migration pages, homepage release notice | Reconcile `1.0.0` homepage wording with `v1.0.2` release metadata and local `1.1.0-dev` context |
| **4.3 Installation and Setup** | Verified existing resource | Installation page, README requirements and package metadata | Use `docs/get-started/installation.md` as canonical user entry; keep README concise and aligned |
| **1. CE Ecosystem & Related Organizations** | Existing but needs clarification | Grejna AB, browser demo, Decision Labs and plugin/studies references (`README.md:9-12`, `README.md:127-133`, `docs/index.md:25-34`) | Separate OSS CE, browser/demo resources, companion projects and optional commercial services with evidence-based labels |

## 7. Unresolved questions

1. Is the browser demo maintained by the CE project, a university group, or
   another party? The repository links it but does not establish ownership.
2. What exact functionality does Decision Labs provide, and does it use CE?
3. Can either external resource accept user-supplied data? No repository
   evidence confirms this.
4. Should notebooks receive a direct public documentation entry point, or remain
   a repository learning resource?
5. Which version should the homepage call stable after reconciling the
   `1.0.0`, `v1.0.2` and `1.1.0-dev` references?
6. Should Door 3 offer a documented local “bring your own model/data” recipe
   using the existing pipeline integration page?

## 8. Recommendations for L05

1. Treat external interactive resources as linkable companions, not as verified
   CE capabilities, until their functionality and ownership are confirmed.
2. Add a navigation-only resource block that links the browser demo, Decision
   Labs, notebooks and local pipeline integration with precise descriptions.
3. Add an ecosystem distinction separating the open-source library, companion
   research/plugins, external learning resources and optional commercial
   services.
4. Reconcile release/version language before presenting Door 4 version claims.
5. Prefer a local-code “use your own model/data” route over promising browser
   upload functionality that is not evidenced.

No changes to CE documentation or software were made in this task.

