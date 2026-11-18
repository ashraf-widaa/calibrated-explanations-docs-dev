# Exceptions

CE raises its own exception types, all subclasses of `CalibratedError`. Import
them from `calibrated_explanations.utils.exceptions`; the older path
`calibrated_explanations.core.exceptions` re-exports the same classes.

## The hierarchy

| Exception | Parent | Raised when |
|---|---|---|
| `CalibratedError` | `Exception` | Base class of every CE error; carries an optional `details` dictionary |
| `ValidationError` | `CalibratedError` | Inputs or configuration fail validation |
| `DataShapeError` | `ValidationError` | Data has an incompatible shape or type, for example `x` and `y` of different lengths |
| `ConfigurationError` | `CalibratedError` | Parameters are invalid or conflict with each other |
| `ModelNotSupportedError` | `CalibratedError` | The model lacks a required method for the task, for example `predict_proba` |
| `NotFittedError` | `CalibratedError` | A call needs a fitted or calibrated explainer |
| `ConvergenceError` | `CalibratedError` | An optimisation or calibration step does not converge |
| `SerializationError` | `CalibratedError` | Saving or loading explanation artefacts fails |
| `IncompatibleStateError` | `SerializationError` | A saved state cannot be loaded because of a schema or checksum mismatch |
| `PlotPluginError` | `CalibratedError` | A plot plugin fails or is misconfigured |
| `MissingExtensionError` | `CalibratedError`, `ImportError` | An optional modality extension package is not installed |

## Common mistakes and what they raise

Checked against the library for this documentation version:

| Mistake | Result |
|---|---|
| `predict` before `fit` | `NotFittedError`: "The WrapCalibratedExplainer must be fitted before predicting." |
| `calibrate` before `fit` | `NotFittedError`: "The WrapCalibratedExplainer must be fitted before calibration." |
| `explain_factual` before `calibrate` | `NotFittedError`: "The WrapCalibratedExplainer must be calibrated before explaining." |
| `calibrate(x, y)` with different numbers of rows | `DataShapeError`, naming both lengths |
| `predict_proba` before `calibrate` | **No error.** The model's uncalibrated probabilities are returned with a `UserWarning`: "The WrapCalibratedExplainer must be calibrated to get calibrated probabilities." |

The last row matters in production: treat that warning as an error if your
code must only ever return calibrated values, for example with
`warnings.simplefilter("error", UserWarning)` around the call.

## Reading an error

`explain_exception` formats any CE error with its details:

```python
from calibrated_explanations.utils.exceptions import ValidationError, explain_exception

error = ValidationError("x must not be empty", details={"param": "x", "requirement": "non-empty"})
print(explain_exception(error))
```

```text
ValidationError: x must not be empty
  Details: {'param': 'x', 'requirement': 'non-empty'}
```

Validation rules and parameter aliases are described in
{doc}`../foundations/concepts/error_handling`; fixes for common failures are
in {doc}`../get-started/troubleshooting`.
