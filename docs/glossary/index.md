# Glossary

Short definitions of the terms used across the Calibrated Explanations (CE)
documentation. Each term is defined once and links to the page that teaches it.
Full method signatures are in the {doc}`API reference <../api/index>`.

The glossary has two categories:

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Scientific & Theoretical
:link: science
:link-type: doc

Machine learning, explainability, probability, calibration, uncertainty,
statistical methods, assumptions and guarantees.
:::

:::{grid-item-card} Software & Technical
:link: software
:link-type: doc

CE library objects, methods, parameters, configuration, outputs, plugins and
operations.
:::
::::

:::{note}
The glossary is being built in stages. Entries marked *wording under review*
or *name under review* are not yet confirmed by the CE authors and may change.
:::

## All terms A–Z

Each line names the term, its category (**S** = Scientific & Theoretical,
**T** = Software & Technical) and links to its definition.

{ref}`A <glossary-az-a>` ·
{ref}`B <glossary-az-b>` ·
{ref}`C <glossary-az-c>` ·
{ref}`D <glossary-az-d>` ·
{ref}`E <glossary-az-e>` ·
{ref}`F <glossary-az-f>` ·
{ref}`G <glossary-az-g>` ·
{ref}`I <glossary-az-i>` ·
{ref}`L <glossary-az-l>` ·
{ref}`M <glossary-az-m>` ·
{ref}`P <glossary-az-p>` ·
{ref}`R <glossary-az-r>` ·
{ref}`S <glossary-az-s>` ·
{ref}`T <glossary-az-t>` ·
{ref}`U <glossary-az-u>` ·
{ref}`V <glossary-az-v>` ·
{ref}`W <glossary-az-w>`

(glossary-az-a)=

### A

- {term}`add_conjunctions` · **T**
- {term}`Alternative explanation` · **S**
- {term}`AlternativeExplanation` · **T**
- {term}`AlternativeExplanations` · **T**

(glossary-az-b)=

### B

- {term}`bins` · **T**
- {term}`Brier score` · **S**

(glossary-az-c)=

### C

- {term}`calibrate` · **T**
- {term}`CalibratedExplainer` · **T**
- {term}`CalibratedExplanations` · **T**
- {term}`Calibration` · **S**
- Calibration data · see {term}`Calibration set`
- {term}`Calibration set` · **S**
- Calibration split · see {term}`Calibration set`
- {term}`Calibrator cache` · **T**
- {term}`categorical_features` · **T**
- {term}`ce plugins` · **T**
- Conditional calibration · see {term}`Mondrian calibration`
- {term}`confidence` · **T**
- {term}`confidence_level` · **T**
- {term}`ConfigurationError` · **T**
- {term}`Conformal predictive system` · **S**
- Conjunction · see {term}`Conjunctive rule`
- {term}`Conjunctive rule` · **S**
- CPS · see {term}`Conformal predictive system`

(glossary-az-d)=

### D

- {term}`Difficulty estimation` · **S**
- {term}`difficulty_estimator` · **T**
- {term}`Discretization` · **T**
- {term}`Distribution shift` · **S**
- Drift · see {term}`Distribution shift`

(glossary-az-e)=

### E

- {term}`Ensured explanation` · **S**
- {term}`Exchangeability` · **S**
- {term}`explain_factual` · **T**
- {term}`ExplainerConfig` · **T**
- {term}`Explanation envelope` · **S**
- {term}`Explanation schema v1` · **T**
- {term}`explore_alternatives` · **T**

(glossary-az-f)=

### F

- {term}`Factual explanation` · **S**
- {term}`FactualExplanation` · **T**
- {term}`Feature attribution` · **S**
- Feature importance · see {term}`Feature attribution`
- {term}`Feature weight` · **S**
- {term}`feature_names` · **T**
- {term}`fit` · **T**

(glossary-az-g)=

### G

- Global explanation · see {term}`Local explanation`
- {term}`Guarded explanation` · **S**
- {term}`GuardedOptions` · **T**

(glossary-az-i)=

### I

- {term}`Interval regression` · **S**

(glossary-az-l)=

### L

- {term}`Local explanation` · **S**
- {term}`low_high_percentiles` · **T**

(glossary-az-m)=

### M

- {term}`mc` · **T**
- {term}`mode` · **T**
- {term}`Mondrian calibration` · **S**

(glossary-az-p)=

### P

- {term}`Parallel backend` · **T**
- Percentile regression · see {term}`Interval regression`
- {term}`plot` · **T**
- {term}`PlotSpec` · **T**
- {term}`Plugin` · **T**
- {term}`Plugin registry` · **T**
- {term}`predict` · **T**
- {term}`predict_proba` · **T**
- {term}`Probabilistic regression` · **S**
- {term}`Proper training set` · **S**
- Proper training split · see {term}`Proper training set`

(glossary-az-r)=

### R

- {term}`Reject option` · **S**
- {term}`Reject policy` · **T**
- {term}`reject_confidence` · **T**
- RejectPolicy · see {term}`Reject policy`
- {term}`RejectResult` · **T**
- {term}`Reliability diagram` · **S**
- Reliability table · see {term}`Reliability diagram`
- {term}`Rule` · **S**
- {term}`Rules payload` · **T**

(glossary-az-s)=

### S

- Schema v1 · see {term}`Explanation schema v1`
- {term}`significance` · **T**

(glossary-az-t)=

### T

- {term}`Telemetry` · **T**
- {term}`threshold` · **T**
- Thresholded regression · see {term}`Probabilistic regression`
- {term}`to_json` · **T**
- {term}`to_narrative` · **T**

(glossary-az-u)=

### U

- {term}`Uncertainty interval` · **S**
- {term}`uq_interval` · **T**

(glossary-az-v)=

### V

- {term}`ValidationError` · **T**
- {term}`Venn-Abers predictor` · **S**
- Venn–Abers predictor · see {term}`Venn-Abers predictor`

(glossary-az-w)=

### W

- {term}`WrapCalibratedExplainer` · **T**

```{toctree}
:hidden:

Scientific & Theoretical <science>
Software & Technical <software>
```

Entry-point tier: Tier 3.
