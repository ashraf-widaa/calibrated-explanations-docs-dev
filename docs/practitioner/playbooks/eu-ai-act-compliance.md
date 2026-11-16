(satisfying-eu-ai-act-requirements-with-calibrated-explanations)=

# CE outputs in EU AI Act review

> [!WARNING]
> **LEGAL DISCLAIMER — NO COMPLIANCE GUARANTEE**
>
> This document and this library do not constitute legal advice and carry no
> guarantee that any regulatory authority or legal entity will regard the
> library's outputs as satisfying any statutory obligation. Whether a deployment
> satisfies the EU AI Act (Regulation (EU) 2024/1689) or any other law is a
> **legal determination requiring qualified legal counsel**. The library is
> provided "as is" under the BSD 3-Clause licence. **The authors and maintainers
> expressly disclaim all liability arising from reliance on this document.**

> **Document scope:** This guide targets practitioners and compliance officers who
> deploy machine learning models in contexts regulated by Regulation (EU) 2024/1689
> (the EU AI Act). It maps each relevant article to the concrete capabilities of
> `calibrated_explanations` and provides a verifiable implementation checklist.

---

## 1. Executive Summary

CE can produce records that are relevant when reviewing an AI deployment:
calibrated predictions, factual feature rules, alternative model-response
scenarios, and their reported ranges. Whether those records meet a particular
legal obligation depends on the system and the applicable law.

**Review status.** The article-to-capability mappings below are review prompts,
not findings of compliance. Exact calibration and coverage statements remain
subject to the qualifications in
{doc}`../../foundations/concepts/calibrated_interval_semantics`.
Explanation ranges are not formal per-feature coverage guarantees, and
alternatives are not necessarily minimal, actionable or causal.

**Questions for scientific and legal reviewers:** Which records are relevant to
each obligation? What additional evidence and organizational controls are
required? Which claims about coverage, fairness, or oversight are justified for
the particular task and deployment? These questions remain open; the library's
presence does not answer them.

Deploying `calibrated_explanations` alongside an existing model requires no
architectural changes to the model itself. It wraps the model via
`WrapCalibratedExplainer`, calibrates it against a held-out calibration set, and
exposes a consistent API for generating and serialising explanation payloads. The
serialised payloads can be stored with deployment records. The deployer must
supply provenance, timestamps, retention and access controls; the payload alone
does not establish audit completeness or regulatory acceptance.

---

## 2. Scope and Applicability

### 2.1 AI Act Risk Tiers Addressed

The AI Act defines four risk tiers. This document focuses on **high-risk AI systems**
as defined in **Article 6** and **Annex III**, which include systems used in:

| Annex III Area | Example use cases |
|---|---|
| 1 — Biometric identification | Identity verification, access control |
| 2 — Critical infrastructure | Grid management, transport |
| 3 — Education and vocational training | Admissions scoring, assessment |
| 4 — Employment and workers management | CV screening, performance monitoring |
| 5 — Access to essential services | Credit scoring, insurance underwriting |
| 6 — Law enforcement | Recidivism risk, threat detection |
| 7 — Migration and border control | Asylum processing, risk profiling |
| 8 — Administration of justice and democratic processes | Judicial decision support |

These examples do not determine a system's legal risk category. CE applies
only where the model interface and data meet its technical prerequisites;
Article 50 applicability is a separate legal question.

### 2.2 Supported Model Types and Tasks

| Task | CE support |
|---|---|
| Binary classification | Full — `explain_factual`, `explore_alternatives`, `predict_proba` |
| Multi-class classification | Predicted-class explanations by default; all-class support is experimental |
| Regression | Full — prediction intervals, threshold-based probabilistic explanations |

Supported base estimators: any scikit-learn-compatible model (including gradient
boosting libraries such as XGBoost, LightGBM, and CatBoost via sklearn wrappers).

### 2.3 Prerequisites

1. A trained, scikit-learn-compatible model (`predict` / `predict_proba` interface).
2. A **calibration set** `(x_cal, y_cal)` — held-out data not used to train the
   predictive model. No universal sample count establishes adequate calibration.
3. A **proper training set** `(x_proper, y_proper)` — used to fit the predictive
   model and any preprocessing, before calibration.
4. Python ≥ 3.10 and `calibrated_explanations` installed
   (`pip install calibrated_explanations`).

The Python fragments illustrate separate integration steps, not a single
program. Unless stated otherwise, they assume a fitted and calibrated binary
classifier and `X_query`; the {doc}`Quick API <../../get-started/quick_api>`
provides setup. `probs` has two class columns, while `low` and `high` are
one-dimensional bounds for the positive class. Supply application callbacks,
identifiers and any group labels where indicated. Policy thresholds below are
illustrative settings, not validated risk or compliance thresholds.

---

## 3. Article-by-Article Compliance Mapping

### Art. 9 — Risk Management System

**a) Title (verbatim):** Article 9 — Risk management system

**b) Core obligation:** Providers of high-risk AI systems must establish, implement,
document, and maintain a risk management system that identifies, analyses, and
evaluates the reasonably foreseeable risks that the system may pose, and takes
appropriate mitigation measures throughout the lifecycle (Art. 9(1)–(6)).

**c) How `calibrated_explanations` contributes:** Uncertainty quantification is a
prerequisite for rational risk management. `predict_proba` with `uq_interval=True`
returns lower and upper values with mode-specific qualifications; see the semantics reference. These are not a general certificate of validity.
Reported widths can be recorded as one diagnostic, alongside task-specific
error measures and outcome monitoring. **Review question:** Does a width-based
flag identify relevant risks in this deployment, and what evidence supports
the chosen threshold? Width alone does not answer that question.

**d) Code:**

```python
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(model)
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal, feature_names=feature_names)

# Compute prediction with uncertainty interval
probs, (low, high) = explainer.predict_proba(X_query, uq_interval=True)
interval_width = high - low

# Risk flag: interval wider than tolerance threshold
RISK_THRESHOLD = 0.30
high_risk_mask = interval_width > RISK_THRESHOLD
```

**e) Audit documentation:** Log `interval_width` and `high_risk_mask` per case.
Include the calibration set size and the chosen `RISK_THRESHOLD` in the AI system's
technical documentation (Annex IV, §1(c)).

---

### Art. 10 — Data and Data Governance

**a) Title (verbatim):** Article 10 — Data and data governance

**b) Core obligation:** High-risk AI systems must be trained on data that is
relevant, representative, and free from errors, and providers must take appropriate
measures to examine data for biases that could give rise to risks within the meaning
of Art. 9(2) (Art. 10(2)(f)–(g)). Where relevant, group-specific bias and accuracy
disparities must be examined and mitigated.

**c) How `calibrated_explanations` contributes:** Mondrian (conditional) calibration
fits separate calibrators using `bins` at calibration and matching labels at
inference. The example compares reported probability-range widths by group;
it does not measure target coverage or establish fairness.
**Review question:** Which group definitions, held-out metrics and legal
permissions are appropriate for examining bias in the intended deployment?

**d) Code:**

```python
import numpy as np

# group_labels: array-like of group identifiers for each calibration instance
# e.g., derived from a protected demographic attribute
group_labels_cal = x_cal[:, protected_feature_idx]
group_labels_test = X_query[:, protected_feature_idx]

explainer.calibrate(x_cal, y_cal, bins=group_labels_cal)

# Mondrian-calibrated factual explanation — separate intervals per group
factual = explainer.explain_factual(X_query, bins=group_labels_test)

# Alternatively, at the probability level
probs, (low, high) = explainer.predict_proba(
    X_query, uq_interval=True, bins=group_labels_test
)

# Inspect per-group widths as a descriptive diagnostic, not a fairness verdict
for group in np.unique(group_labels_test):
    mask = group_labels_test == group
    width = (high - low)[mask].mean()
    print(f"Group {group}: mean interval width = {width:.3f}")
```

**e) Audit documentation:** Record per-group mean interval width and coverage
estimates in the data governance section of the technical documentation. A
statistically significant disparity across groups should be flagged and the
mitigation strategy documented.

---

### Art. 11 and Annex IV — Technical Documentation

**a) Title (verbatim):** Article 11 — Technical documentation; Annex IV — Technical
documentation referred to in Article 11(1)

**b) Core obligation:** Before placing a high-risk AI system on the market,
providers must draw up technical documentation demonstrating compliance. Annex IV
specifies that this documentation must include, among other items: a description of
the system's accuracy, robustness and cybersecurity measures; the monitoring,
functioning and control mechanisms; and the measures taken to enable traceability
and auditability (Annex IV §1(c), §1(e), §2(c)).

**c) How `calibrated_explanations` contributes:** `calibrated_explanations` produces
structured, serialisable explanation objects that encode the model metadata,
calibration configuration, feature names, per-instance factual rules, and uncertainty
intervals. The JSON payload produced by `build_rules_payload()` provides a machine-readable
record for a traceability review. Whether it is sufficient remains a legal
question. The calibration configuration
(calibration set size, conformal significance level, whether Mondrian binning is
used) should be included verbatim in the Annex IV technical documentation.

**d) Code:**

```python
# Generate explanation and serialise as JSON for technical documentation
explanation = explainer.explain_factual(X_query)

# JSON payload — suitable for archiving in immutable audit log
payload = explanation[0].build_rules_payload()  # single-instance payload
print(payload)
# Contains: feature names, values, weights, intervals, prediction, probability

# For a multi-row batch, iterate
import json, pathlib
log_path = pathlib.Path("audit_logs") / "explanations.jsonl"
log_path.parent.mkdir(exist_ok=True)
with log_path.open("a") as f:
    for exp in explanation:
        f.write(json.dumps(exp.build_rules_payload()) + "\n")
```

**e) Audit documentation:** The technical documentation must reference the
`calibrated_explanations` version (retrievable via
`import calibrated_explanations; calibrated_explanations.__version__`), the
calibration set provenance, and the significance level (confidence) used. Store
the JSON schema of the explanation payload as Annex IV §3 supporting artefact.

---

### Art. 12 — Record-keeping and Logging

**a) Title (verbatim):** Article 12 — Record-keeping

**b) Core obligation:** High-risk AI systems must automatically log events relevant
to the system's operation, including dates and times of use, reference to the input
data, and the results of the AI system's operation, for a period appropriate to the
intended purpose (Art. 12(1)–(2)).

**c) How `calibrated_explanations` contributes:** `build_rules_payload()` exports an
explanation record. An application can add identifiers, timestamps and model
versions before storing it. CE does not provide a complete logging service.
**Review question:** Which events and fields must the deployment log, and how
will integrity, access and retention be managed?

**d) Code:**

```python
import json, datetime, pathlib, uuid

audit_log = pathlib.Path("audit_logs") / "ai_act_record.jsonl"
audit_log.parent.mkdir(exist_ok=True)

explanation = explainer.explain_factual(X_query)

with audit_log.open("a", encoding="utf-8") as f:
    for i, exp in enumerate(explanation):
        record = {
            "record_id": str(uuid.uuid4()),
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "model_version": model_version,
            "ce_version": calibrated_explanations.__version__,
            "input_index": i,
            "explanation": exp.build_rules_payload(),
        }
        f.write(json.dumps(record) + "\n")
```

**e) Audit documentation:** Have the retention period and required records
confirmed for the deployment. Document the log schema, integrity controls and
access policy; this example does not prescribe a legally sufficient period.

---

### Art. 13 — Transparency and Provision of Information to Deployers

**a) Title (verbatim):** Article 13 — Transparency and provision of information to
deployers

**b) Core obligation:** High-risk AI systems must be designed and developed to
ensure that their operation is sufficiently transparent to enable deployers to
interpret the system's outputs and use them appropriately (Art. 13(1)). The
instructions for use must include information about the system's capabilities and
limitations (Art. 13(3)(b)).

**c) How `calibrated_explanations` contributes:** `explain_factual` returns a
human-readable **factual rule table** for each instance: a ranked list of features
together with their actual values, the direction and magnitude of their contribution
to the prediction, and the uncertainty interval around each weight. This output is
explained in {doc}`../../foundations/how-to/interpret_explanations`.
Weights compare model responses to substituted feature values, rather than
establishing causes. **Review question:** Can the intended users understand
these records and their limitations well enough for the specified task?

**d) Code:**

```python
# Per-instance factual explanation
factual = explainer.explain_factual(X_query)

# Print human-readable rule table for the first instance
print(factual[0].list_rules())
# Illustrative interpretation (not literal list_rules formatting):
#   age = 42         →  P(approve) increased by 0.12 [0.07, 0.18]
#   income = 55000   →  P(approve) increased by 0.09 [0.04, 0.15]
#   debt_ratio = 0.4 →  P(approve) decreased by 0.05 [0.01, 0.10]

# Access structured rule data programmatically
rules = factual[0].build_rules_payload()
```

**e) Audit documentation:** Log the full rule table for every production prediction
event. The instructions for use (Art. 13(3)) should describe the rule-table format
and explain how deployers should interpret uncertainty intervals, including the
guidance that predictions with wide intervals require additional review.

---

### Art. 14 — Human Oversight

**a) Title (verbatim):** Article 14 — Human oversight

**b) Core obligation:** High-risk AI systems must be designed and developed to
allow the natural persons to whom human oversight is assigned to effectively
oversee the system's operation. The system must enable those persons to decide not
to use the system or to override, disregard, or reverse its output (Art. 14(1),
(4)(c)).

**c) How `calibrated_explanations` contributes:** The **interval straddle policy**
and **interval width policy** are examples of application-defined gates.
The application must route flagged cases, prevent inappropriate automated
actions and record the reviewer's decision. CE's separate `RejectPolicy` API
uses its reject procedure, not these width/straddle rules.
**Review question:** Are the proposed gates, reviewer authority and operating
procedures sufficient for this deployment?

**d) Code:**

```python
from calibrated_explanations.core.reject.policy import RejectPolicy

probs, (low, high) = explainer.predict_proba(X_query, uq_interval=True)
decision_boundary = 0.5

# Straddle check: probability interval crosses the decision boundary
straddles = (low < decision_boundary) & (high > decision_boundary)

# Width check: absolute uncertainty too large
MAX_WIDTH = 0.25
too_uncertain = (high - low) > MAX_WIDTH

# Combined human-oversight gate
needs_human_review = straddles | too_uncertain

for idx in X_query[needs_human_review]:
    escalate_to_human_reviewer(idx, reason="uncertainty_gate")

# Alternatively, use built-in RejectPolicy via explain_factual
factual = explainer.explain_factual(X_query, reject_policy=RejectPolicy.FLAG)
```

**e) Audit documentation:** Log every escalation event with the case identifier,
the triggering condition (`straddle`, `width`, or both), the interval values, and
the human reviewer's identity and decision. This log constitutes the human oversight
audit trail required by Art. 14 and Recital 58.

---

### Art. 15 — Accuracy, Robustness and Cybersecurity

**a) Title (verbatim):** Article 15 — Accuracy, robustness and cybersecurity

**b) Core obligation:** High-risk AI systems must achieve an appropriate level of
accuracy, robustness, and consistency of performance. Accuracy metrics must be
declared in the technical documentation. Providers must document the expected level
of accuracy and the measures taken to achieve it (Art. 15(1)–(2)).

**c) What CE can contribute:** Record the mode, model and calibration
configuration, and evaluate outputs on untouched test data. Probability
calibration, regression interval coverage, and predictive accuracy are different
properties. None is a general certificate of robustness or regulatory compliance.

**d) Evaluation:** Follow {doc}`../evaluate_ce` for classification probability
metrics and, separately, regression interval coverage. Checking whether a
predicted probability lies inside its own reported bounds does not measure
coverage of observed outcomes. There is no universal 90% classification
confidence setting implied by a call to `predict_proba`.

**e) Review question:** Which task-specific evaluation and system-level evidence
are needed for Article 15 and Annex IV? This requires scientific and legal
review. The earlier calibration-set coverage/certification claim is withdrawn
pending that review (N-07).

---

### Art. 50 — Transparency Obligations for Certain AI Systems

**a) Title (verbatim):** Article 50 — Transparency obligations for providers and
deployers of certain AI systems

**b) Article distinction:** Article 50 concerns transparency obligations for
certain AI systems, including informing people about direct interaction with
AI. The right to explanation of individual decision-making is addressed in
Article 86, with its own scope and conditions. See the official
[Article 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50) and
[Article 86](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-86) texts.

**c) How `calibrated_explanations` contributes:** `explore_alternatives` generates
alternative model-response scenarios. These are not necessarily minimal,
feasible, non-discriminatory or sufficient as an explanation of a legal
decision. **Review question (N-08):** Which CE records, if any, are relevant
under Articles 50 or 86 for this system, and what further explanation is needed?

**d) Code:**

```python
# Generate counterfactual alternatives for the affected individual
alternatives = explainer.explore_alternatives(X_query)

# Print model-response alternatives for person at index 0
print(alternatives[0].list_rules())
# Illustrative interpretation (not literal list_rules formatting):
#   IF income increased from 38000 → 52000 THEN P(approve) = 0.73 [0.65, 0.81]
#   IF debt_ratio decreased from 0.55 → 0.35 THEN P(approve) = 0.68 [0.59, 0.76]

# Serialise for delivery to the affected person / inclusion in decision letter
alt_json = alternatives[0].build_rules_payload()
```

**e) Review documentation:** Identify the applicable provision before defining
what must be communicated or retained. A stored alternative-rule payload is
supporting model information, not proof of satisfying either article.

---

## 4. Compliance Checklist

These rows identify possible supporting records. Their presence does not
establish that an obligation is satisfied; the mappings remain under legal
review (N-01).

| Article | Obligation summary | CE feature / method | Status |
|---|---|---|---|
| Art. 9 | Identify and quantify AI system risks throughout lifecycle | `predict_proba(uq_interval=True)` — interval width as risk indicator | **Review required** |
| Art. 10 | Examine training data for bias; ensure representativeness across groups | `calibrate(..., bins=group_labels_cal)` then `explain_factual(..., bins=group_labels_test)` - Mondrian per-group intervals | **Review required** |
| Art. 11 + Annex IV | Produce technical documentation including accuracy and traceability | `build_rules_payload()` — serialisable explanation payload; calibration configuration | **Review required** |
| Art. 12 | Log events: input data, result, date/time — for defined retention period | `build_rules_payload()` appended to audit log with timestamp and record ID | **Review required — supporting records only** — log infrastructure and retention policy must be provided by deployer |
| Art. 13 | Transparent operation; deployer can interpret system outputs | `explain_factual()` — `list_rules()` human-readable rule table | **Review required** |
| Art. 14 | Enable human oversight; allow override before automated action | `predict_proba` straddle/width gates; `RejectPolicy.FLAG` | **Review required** |
| Art. 15 | Declared, verifiable accuracy; robustness documentation | Task-specific probability metrics or regression coverage on held-out data | **Review required** |
| Art. 50 / Art. 86 | Article 50 concerns transparency obligations for certain AI systems; Article 86 concerns explanation of individual decision-making | Factual and alternative model-response records; legal applicability requires review | **Review required** |

---

## 5. Limitations and Gaps

The following compliance obligations are **not** satisfied by `calibrated_explanations`
alone and require additional organisational or technical controls.

### 5.1 Data Quality Certification (Art. 10(2)(a)–(e))
Art. 10 requires that training data satisfies relevance, representativeness,
error-freedom, and completeness criteria. `calibrated_explanations` does not
inspect, validate, or certify input data quality. **Required:** A data quality
framework (e.g., Great Expectations, Soda, or a custom data validation pipeline)
upstream of model training, with documented data quality test results.

### 5.2 Cybersecurity Controls (Art. 15(3)–(5))
Art. 15 requires resilience against adversarial manipulation, data poisoning, and
model-evasion attacks. `calibrated_explanations` does not provide adversarial
robustness defences. **Required:** Adversarial testing (e.g., using libraries such
as `adversarial-robustness-toolbox`) and network/access controls protecting the
model serving endpoint.

### 5.3 Conformity Assessment and CE Marking (Art. 43–49)
High-risk AI systems must undergo a conformity assessment before market placement.
`calibrated_explanations` provides technical evidence for the assessment but is not
itself a conformity assessment tool. **Required:** Engagement with a notified body
(where applicable) or internal conformity assessment process, documentation in
accordance with Art. 11 and Annex IV, and registration in the EU AI Act database
(Art. 49).

### 5.4 Post-Market Monitoring (Art. 72)
Art. 72 requires providers to operate a post-market monitoring system that
continuously collects data on system performance after deployment. `calibrated_explanations`
does not provide drift detection, performance dashboards, or monitoring alerts.
**Required:** A model monitoring system (e.g., Evidently AI, WhyLabs, or a custom
pipeline) that tracks empirical coverage, interval widths, and prediction
distributions over time, and feeds back into the risk management system (Art. 9).

### 5.5 Human Oversight Processes Outside the Model (Art. 14(4)(a)–(d))
Art. 14 requires that humans assigned to oversight are sufficiently competent to
understand the system's capabilities and limitations, and that their decisions are
logged. `calibrated_explanations` can flag cases for review but cannot train
reviewers, enforce review quality, or impose a review workflow. **Required:**
Documented escalation procedures, reviewer training, and a workflow management
system that records reviewer decisions and links them back to the CE audit log.

(fundamental-rights-impact-assessment-art-9-9-recital-66)=

### 5.6 Fundamental Rights Impact Assessment
Article 27 addresses fundamental-rights impact assessments for specified
deployers of high-risk systems. **Review question:** Does it apply to this
deployment, and what assessment and evidence does it require? Group-conditioned
CE outputs can be examined as model information; they are not themselves a
fundamental-rights assessment.

---

## 6. Quick-Start Integration Guide

The following recipe illustrates six CE integration steps for review. Article
labels indicate discussion topics, not obligations satisfied by the code.

### Step 1 — Install

```bash
pip install calibrated_explanations
```

### Step 2 — Wrap and Calibrate the Model

*(Prerequisite: `x_proper`, `y_proper` = proper training set; `x_cal`, `y_cal` =
held-out calibration set; `feature_names` = list of feature name strings)*

```python
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(model)
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal, feature_names=feature_names)
```

### Step 3 — Art. 13: Generate a Factual Explanation (Transparency)

```python
# X_query: the feature vector(s) of the instance(s) to be decided upon
factual = explainer.explain_factual(X_query)

# Human-readable rule table — include in deployer UI and decision letter
print(factual[0].list_rules())

# Structured payload for logging and documentation
payload = factual[0].build_rules_payload()
```

(step-4-art-50-retrieve-counterfactual-alternatives)=

### Step 4 — Retrieve Alternative Model Responses for Review

```python
alternatives = explainer.explore_alternatives(X_query)

# Print model-response alternatives for review
print(alternatives[0].list_rules())

alt_payload = alternatives[0].build_rules_payload()
```

### Step 5 — Art. 14: Apply a Reject / Escalation Policy (Human Oversight)

```python
probs, (low, high) = explainer.predict_proba(X_query, uq_interval=True)
decision_boundary = 0.5
MAX_INTERVAL_WIDTH = 0.25

straddles = (low < decision_boundary) & (high > decision_boundary)
too_uncertain = (high - low) > MAX_INTERVAL_WIDTH
needs_review = straddles | too_uncertain

if needs_review.any():
    escalate_to_human_reviewer(X_query[needs_review], reason="uncertainty_gate")
```

### Step 6 — Art. 12: Serialise the Audit Payload (Record-keeping)

```python
import json, datetime, pathlib, uuid
import calibrated_explanations

audit_log = pathlib.Path("audit_logs") / "ai_act_record.jsonl"
audit_log.parent.mkdir(exist_ok=True)

with audit_log.open("a", encoding="utf-8") as f:
    for i, (fact, alt) in enumerate(zip(factual, alternatives)):
        record = {
            "record_id": str(uuid.uuid4()),
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "ce_version": calibrated_explanations.__version__,
            "factual": fact.build_rules_payload(),
            "alternatives": alt.build_rules_payload(),
            "human_review_required": bool(needs_review[i]),
        }
        f.write(json.dumps(record) + "\n")
```

---

## 7. References

### Regulatory

- **EU AI Act** — Regulation (EU) 2024/1689 of the European Parliament and of the
  Council of 13 June 2024 laying down harmonised rules on artificial intelligence.
  Official Journal of the European Union, L series, 12 July 2024.
  <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689>
- **Relevant recitals:** Recital 47 (meaningful explanation), Recital 48 (right to
  explanation does not apply to purely automatic decisions under GDPR unless
  separately required), Recital 58 (human oversight design), Recital 66
  (fundamental rights impact), Recital 71 (accuracy and performance metrics).
- **Annex III** — List of high-risk AI systems referred to in Art. 6(2).
- **Annex IV** — Technical documentation referred to in Art. 11(1).

### Calibrated Explanations

- Löfström, H., Löfström, T., Johansson, U., & Sönströd, C. (2024).
  *Calibrated Explanations: with Uncertainty Information and Counterfactuals.*
  Expert Systems with Applications. DOI: [10.1016/j.eswa.2024.123154](https://doi.org/10.1016/j.eswa.2024.123154)
- Löfström, T., Löfström, H., Johansson, U., Sönströd, C., & Matela, R. (2024).
  *Calibrated Explanations for Regression.*
  Machine Learning. DOI: [10.1007/s10994-024-06642-8](https://doi.org/10.1007/s10994-024-06642-8)
- Löfström, H., Löfström, T., Johansson, U., Sönströd, C., & Boström, H. (2024).
  *Conditional Calibrated Explanations: Finding a Path Between Bias and Uncertainty.*
  In: Proc. ECAI 2024 Workshop. DOI: [10.1007/978-3-031-63787-2_17](https://doi.org/10.1007/978-3-031-63787-2_17)
- Repository: <https://github.com/Moffran/calibrated_explanations>

### Conformal Prediction and Venn-Abers

- Shafer, G., & Vovk, V. (2008).
  *A Tutorial on Conformal Prediction.*
  Journal of Machine Learning Research, 9, 371–421.
- Vovk, V., Gammerman, A., & Shafer, G. (2005).
  *Algorithmic Learning in a Random World.* Springer.
- Johansson, U., Löfström, T., & Boström, H. (2021).
  *Venn-Abers Predictors.*
  In: Conformal and Probabilistic Prediction with Applications (COPA 2021).


## Sources for corrected article references

The [official AI Act text](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32024R1689)
distinguishes Article 50 from Article 86. This corrects the former checklist
label (N-08); it does not establish that CE satisfies either article.
