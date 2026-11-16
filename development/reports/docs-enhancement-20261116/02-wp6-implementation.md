# 02 — WP-6: Quick API, troubleshooting and notebooks

**Status:** COMPLETED. Two quickstart notebooks are left unlinked; that part is
BLOCKED by the environment (§3).

## 1. Pages and tests changed

| File | Change |
|---|---|
| `docs/get-started/quick_api.md` | Title "Quick API: main components and calls". New: "What you need" table (import, model, data, minimum steps, call per task, output, failures); components table; **complete minimal example with its real printed output** (walkthrough data, split and model, case 2: `P(benign) = 0.286  range [0.167, 0.333]`); "Core calls by step" with a `{py:meth}` link per call to its API entry; note that the remaining snippets are fragments. STD-004 mode notes and the four reference fragments unchanged. Both new tables use the phone layout |
| `docs/get-started/troubleshooting.md` | Rewritten as the single owner of user-facing errors: a lookup table from message to entry, then 12 entries, each with symptom (exact message), cause, check where useful, fix, link and version. Title "Troubleshooting" (URL and sidebar label unchanged) |
| `docs/get-started/apply-to-your-data.md` | "Common problems" keeps its table; adds "Full list: troubleshooting" and the `features_to_ignore` caveat |
| `docs/tasks/{classification,regression,probabilistic_regression}.md` | Each core-demo notebook link now carries "ran without errors with CE 1.1.0.dev0 … on 2026-11-16" |
| `tests/docs/get_started/test_quick_api_example.py` (new, 3 tests) | Runs the example and compares the printed output; ties the numbers to the walkthrough; checks the entry questions and API links |
| `tests/docs/get_started/test_troubleshooting_reproductions.py` (new, 12 tests) | Triggers each reproduced entry through the public API and asserts that the page quotes the library's exact message; checks that every lookup row resolves |
| `tests/integration/test_doc_examples_smoke.py` | Quick API test updated for the new first block (5 blocks; block 0 runs standalone, fragments 1–4 as before) |

## 2. Troubleshooting evidence

Every entry was reproduced on Python 3.13.7, scikit-learn 1.8.0, against
**both** released v1.0.2 and Beta `src/` 1.1.0.dev0. Behaviour and messages were
identical in both. Scripts: `scratchpad/repro/repro_troubleshooting.py`,
`repro_extra.py`.

| Entry | Reproduced message / behaviour | Note |
|---|---|---|
| Calls in the wrong order | `NotFittedError` ×3 messages | Existing row confirmed |
| No `predict_proba` | `ConfigurationError: Calibration failed during explainer_construction: 'LinearSVC' object has no attribute 'predict_proba'` | The `CalibratedClassifierCV` fix was verified |
| NaN / inf | `ValidationError: Argument 'x' contains NaN or infinite values.` at `calibrate` | **Corrected**: the old row said NaN fails "when explaining". CE validates calibration data only; explained cases go to the model (a random forest accepts NaN; `LogisticRegression` fails) |
| `threshold=` with a classifier | `ValidationError: The threshold parameter is only supported for mode='regression'.` | New |
| NumPy integer index | `ValidationError: Invalid argument type.` | Accepted key types read from `explanations.py:315–375` |
| Guarded + fast | `ConfigurationError: Guarded explanations are not supported for fast explainers. …` | Also triggered after `explain_fast` on the same wrapper |
| DataFrame then array | scikit-learn `UserWarning: X does not have valid feature names, …` | Only when the DataFrame has string column names |
| Multiclass upper bound > 1 | max upper bound 1.18 (iris), rows sum to 1 | Routed to SR-13 |
| `features_to_ignore` known issue | `ConfigurationError: Explanation plugin execution failed for mode 'factual': 0` (cause `KeyError`) | **Corrected**: the old row (written by Beta in `c385730f`) blamed `add_conjunctions`. The failing call is any *later* `explain_factual` on the same explainer; the ignore call's own result works, including conjunctions |
| `filter_features` known issue | `TypeError: 'numpy.float64' object is not iterable` | Confirmed; the old row's "1.1.0-dev only" was wrong, since 1.0.2 has it too |
| Empty telemetry | `{}` after `calibrate` and `predict_proba`; 12 keys after `explain_factual` | **Corrected**: the old cause ("old version or attribute stripped") was speculative |
| Optional dependencies | Not reproducible here (both installed); messages read from `viz/__init__.py:58`, `narrative_generator.py:55–57` | Labelled as "not reproduced" on the page |

Backlog item "factual explanation with no rules for saturated cases" was **not
reproduced**: a saturated case (0.056 [0.000, 0.059]) still had rules. The
claim on `apply-to-your-data` is left unchanged and recorded as N-11.

## 3. Notebook verification (Prompt 3c)

Runner: `scripts/docs/run_notebooks.py`, kernel `python3`.

| Notebook | Result | Linked |
|---|---|---|
| `core_demos/demo_binary_classification` | passed (29 s) | yes, with note |
| `core_demos/demo_multiclass_glass` | passed (215 s; the default 30 s cell limit times out) | yes, with note "takes several minutes" |
| `core_demos/demo_regression` | passed (157 s) | yes, with note |
| `core_demos/demo_probabilistic_regression` | passed (134 s) | yes, with note |
| `quickstart_tiny` | passed (11 s) | not linked from these pages (no change) |
| `quickstart`, `quickstart_guarded` | **failed**: `TypeError` inside scikit-learn's OpenML ARFF parser | not linked (unchanged) |

**Environment caveat.** The `python3` Jupyter kernel on this machine is an old
session virtualenv (`venv-ce-run`: scikit-learn 1.9.1, pandas 3.1.1), not
`C:\Python313`. The two failures come from `fetch_openml` under that pandas
version, not from CE: the same download works under `C:\Python313`. A clean
re-run needs a kernel on the docs interpreter. `ipykernel` is not installed
there, and installing it was out of scope (decision D-29). The four linked
notebooks are byte-identical to the official copies.

## 4. Acceptance (master prompt §5 C)

- **Quick Start → executable example.** C2 and the tutorials hub link the Quick API, whose first example runs as written.
- **Troubleshooting is discoverable.** It is linked from the Quick API (table and "Continue"), `apply-to-your-data`, C1, the walkthrough and the Maintenance sidebar.
- **Examples use the API of the documented version.** Verified on 1.0.2 and 1.1.0.dev0.
- **Code executes or is marked.** The reference fragments are labelled as fragments, and the smoke test still runs them.
- **Deeper links work.** The `{py:meth}` links resolve in the build; 0 broken links.
- **No unsupported guarantee.** The example's reading note links the semantics page and says the bounds are not a confidence interval.

## 5. Limitations

- The component figure suggested in Prompt 3a was replaced by an accessible
  table (no new figure).
- `api/index.md` was not changed: it already links the Quick API through the
  Software & Integration landing.
