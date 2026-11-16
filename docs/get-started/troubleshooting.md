# Troubleshooting

This page lists the errors and surprises that users of CE most often meet, with
the exact message, the cause, how to check it and how to fix it. Every entry
was reproduced on 2026-11-16 with CE 1.0.2 (the released version) and
1.1.0.dev0 (this Beta's source), unless the entry says otherwise; the
reproductions run in the documentation tests.

For the calls themselves, see the {doc}`Quick API <quick_api>`; for a full,
working example, see the {doc}`Python tutorials <../tutorials/index>`.

## Find your message

| Message or symptom (start of text) | Entry |
|---|---|
| `NotFittedError: The WrapCalibratedExplainer must be ...` | {ref}`Calls in the wrong order <ts-order>` |
| `ConfigurationError: Calibration failed during explainer_construction: '...' object has no attribute 'predict_proba'` | {ref}`Classifier without predict_proba <ts-predict-proba>` |
| `ValidationError: Argument 'x' contains NaN or infinite values.` | {ref}`Missing or infinite values <ts-nan>` |
| `ValidationError: The threshold parameter is only supported for mode='regression'.` | {ref}`threshold with a classifier <ts-threshold>` |
| `ValidationError: Invalid argument type.` | {ref}`Indexing explanations with a NumPy integer <ts-index>` |
| `ConfigurationError: Guarded explanations are not supported for fast explainers. ...` | {ref}`Guarded options with a fast explainer <ts-guarded-fast>` |
| `UserWarning: X does not have valid feature names, ...` | {ref}`Model fitted on a DataFrame <ts-feature-names>` |
| Multiclass upper bound above 1 | {ref}`Multiclass upper bounds above 1 <ts-multiclass>` |
| `ConfigurationError: Explanation plugin execution failed for mode 'factual': 0` | {ref}`Known issue: explaining again after features_to_ignore <ts-conjunctions>` |
| `TypeError: 'numpy.float64' object is not iterable` | {ref}`Known issue: filter_features <ts-filter>` |
| `runtime_telemetry` is empty | {ref}`Empty telemetry <ts-telemetry>` |
| Import error mentioning the `viz` extra, or PyYAML | {ref}`Optional dependencies <ts-extras>` |

## Setup and order of calls

(ts-order)=

### Calls in the wrong order

- **Symptom.** One of:
  `NotFittedError: The WrapCalibratedExplainer must be fitted before calibration.`,
  `... must be calibrated before explaining.` or
  `... must be fitted and calibrated before explaining.`
- **Cause.** The wrapper needs `fit` (or an already fitted model) and then
  `calibrate` before it can predict with ranges or explain.
- **Fix.** Call `fit` on the proper training set, then `calibrate` on the
  held-out calibration set, then predict or explain.
- **See also.** {doc}`quick_api` (minimum steps).

(ts-predict-proba)=

### Classifier without `predict_proba`

- **Symptom.** At `calibrate`:
  `ConfigurationError: Calibration failed during explainer_construction: 'LinearSVC' object has no attribute 'predict_proba'`
  (with your model's class name).
- **Cause.** CE's classification calibration needs class probabilities from
  the model. Some classifiers, such as `LinearSVC`, only provide `predict`.
- **Check.** `hasattr(model, "predict_proba")`.
- **Fix.** Use a classifier with `predict_proba`, enable it where the model
  offers an option (for example `SVC(probability=True)`), or wrap the model in
  scikit-learn's `CalibratedClassifierCV`, which provides `predict_proba`.

(ts-nan)=

### Missing or infinite values

- **Symptom.** At `calibrate`:
  `ValidationError: Argument 'x' contains NaN or infinite values.`
- **Cause.** CE checks the calibration data and rejects NaN and infinite
  values. The cases you predict or explain are passed to your model, so what
  happens with a NaN there depends on the model: a scikit-learn random forest
  accepts it, while `LogisticRegression` fails with
  `Input X contains NaN.` (wrapped in a `ConfigurationError` when it happens
  during an explanation).
- **Fix.** Impute or remove missing values before `fit` and `calibrate`, and
  apply the same preprocessing to new cases.
- **See also.** {doc}`apply-to-your-data`.

(ts-threshold)=

### `threshold` with a classifier

- **Symptom.**
  `ValidationError: The threshold parameter is only supported for mode='regression'.`
- **Cause.** `threshold=` asks for the probability that a numeric outcome is
  at or below a value: probabilistic regression. A classifier already returns
  class probabilities.
- **Fix.** Drop `threshold=` for classification. For probabilistic
  regression, wrap a regressor.
- **See also.** {doc}`ce-tasks-and-modes`.

## Working with results

(ts-index)=

### Indexing explanations with a NumPy integer

- **Symptom.** `ValidationError: Invalid argument type.` when you select one
  explanation, for example `explanations[np.argmax(scores)]`.
- **Cause.** Explanation collections accept a Python `int`, a slice, or a list
  of Python `int` or `bool` values; a single NumPy integer such as `np.int64`
  is rejected.
- **Fix.** Convert first: `explanations[int(index)]`.

(ts-guarded-fast)=

### Guarded options with a fast explainer

- **Symptom.**
  `ConfigurationError: Guarded explanations are not supported for fast explainers. Use a standard (non-fast) explainer for guarded entrypoints.`
- **Cause.** Guarded explanations need the standard explainer. The error
  appears after `calibrate(..., fast=True)`, and also after a call to
  `explain_fast` on the same wrapper.
- **Fix.** Use a separate wrapper, calibrated without `fast=True`, for guarded
  explanations.
- **See also.** {doc}`quickstart_guarded`.

(ts-feature-names)=

### Model fitted on a DataFrame

- **Symptom.**
  `UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names`
  (from scikit-learn, with your model's class name), often repeated.
- **Cause.** The model was fitted on a pandas DataFrame and is now given a
  NumPy array, or the reverse. Predictions are still made by column position.
- **Fix.** Pass the same type of input throughout (all DataFrames with the
  same columns, or all arrays).

(ts-multiclass)=

### Multiclass upper bounds above 1

- **Symptom.** In multiclass classification, an upper bound from
  `predict_proba(..., uq_interval=True)` is greater than 1 (1.18 in our
  reproduction with the iris data), although the calibrated probabilities in
  each row sum to 1.
- **Cause.** This is how the bounds are computed by default for multiclass
  problems in the current versions; it is not a fault in your data. Whether
  this default is intended is an open question for the CE authors.
- **See also.** The limitations in {doc}`ce-tasks-and-modes`.

## Known issues

(ts-conjunctions)=

### Explaining again after `features_to_ignore`

- **Symptom.** After `explain_factual(..., features_to_ignore=[...])`, a later
  `explain_factual(...)` on the same explainer fails with
  `ConfigurationError: Explanation plugin execution failed for mode 'factual': 0`,
  caused by a `KeyError`.
- **Cause.** A known issue: the call with `features_to_ignore=` leaves state
  behind on the explainer that breaks later factual explanations. The
  explanations returned by the `features_to_ignore` call itself work,
  including `add_conjunctions()`.
- **Fix.** Use a separate, freshly calibrated explainer for explanations with
  `features_to_ignore=`.
- **Applies to.** 1.0.2 and 1.1.0.dev0.

(ts-filter)=

### `filter_features`

- **Symptom.** `explanations.filter_features(exclude_features=[...])` fails with
  `TypeError: 'numpy.float64' object is not iterable`.
- **Cause.** A known issue in filtering an explanation collection after it was
  created.
- **Fix.** Pass `features_to_ignore=` to `explain_factual` or
  `explore_alternatives` instead.
- **Applies to.** 1.0.2 and 1.1.0.dev0.

## Environment

(ts-telemetry)=

### Empty telemetry

- **Symptom.** `explainer.runtime_telemetry` is an empty dictionary.
- **Cause.** The telemetry holds the payload of the most recent explanation
  call. It stays empty after `calibrate` and after `predict_proba`, and is
  filled by a call such as `explain_factual`.
- **Fix.** Read it after an explanation call.

(ts-extras)=

### Optional dependencies

Not reproduced (both packages were installed); messages taken from the CE
source code.

- **Plotting.** If matplotlib is missing, plotting fails with a message that
  ends `pip install calibrated_explanations[viz]`. Install the `viz` extra in
  the same environment.
- **Narratives.** If PyYAML is missing, `to_narrative()` with a YAML template
  (including the default one) raises a `SerializationError` containing
  `PyYAML not installed`. Install it with
  `pip install "calibrated-explanations[narrative]"` or `pip install pyyaml`.

## Collect diagnostics

```bash
python -m calibrated_explanations.plugins.cli list explanations --trusted-only
python -c "from calibrated_explanations import __version__; print(__version__)"
```

Attach the command outputs when filing an issue so maintainers can reproduce
setup differences quickly. If the plugin command is not found on your `PATH`,
the `python -m` form above runs it directly.
