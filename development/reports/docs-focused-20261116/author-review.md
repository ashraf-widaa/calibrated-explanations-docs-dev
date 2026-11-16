# Focused correction cycle: open author and legal questions

Baseline: `481ee05b`. This record extends the existing scientific register in
`development/reports/docs-enhancement-20261116/05-scientific-review.md`.
No item below is closed by the documentation edits, tests or a successful build.

| Existing item | Explicit question | Treatment in this cycle |
|---|---|---|
| SR-01 | Is "distribution-matched" ever sufficient as an alternative to exchangeability for the actual CE protocol? Which fitted components must be fixed before calibration? | Use the existing exchangeability explanation; mark the alternative wording as under review, without replacing it with a new theorem. |
| SR-02 | What exact finite-sample coverage statement applies to the CPS endpoints, including ties, open sides, difficulty estimates and Mondrian groups? | Retain the methods derivation and its review marker; avoid universal individual/subgroup guarantees in summaries. |
| SR-03, SR-13 | How should the Venn–Abers pair, merged estimate and default rescaled multiclass bounds be described? | Distinguish returned objects from exact validity; retain the multiclass caveat and pair/merge question. |
| SR-06 | Which study, metric, dataset and comparison support a rule-stability advantage over LIME? | Remove the unsupported general comparison; do not assert an alternative ranking. |
| SR-07, SR-09 | What uncertainty interpretation is justified for ensured filtering? Should all public definitions use the implementation's "no wider" comparison? | Describe the source's width comparison. Do not claim that it proves stronger evidence or reduces an identified uncertainty component. |
| SR-08, SR-10, SR-14 | Which construction and filter definitions are canonical? What exact meaning is justified for averaged substituted predictions and weight ranges? | Explain the existing worked case and its model-response meaning; no causal or formal feature-coverage conclusion. |
| SR-15 | What validity statement is justified for the implemented CPS-score/Venn–Abers threshold-event construction and its merged output? | Keep an explicit author-review qualification. |
| SR-16, N-10 | Which reject-policy validity statements and confidence/reject-rate examples have supporting evidence? | Deferred; no reject-policy or implementation changes. |
| N-01, N-07 | Which CE records, task-specific metrics and system controls can support each AI Act obligation? What further evidence is required? | Withdraw the probability-containment-as-coverage example, certification wording and checklist compliance verdicts. |
| N-08 | What is the correct applicability and scope of Articles 50 and 86 for the intended deployments? | Correct the article-label distinction; no finding that CE meets either obligation. |
| New verified legislative-status issue | What current legal framework should replace reliance on withdrawn COM(2022)496? | Record withdrawal on 6 October 2025. Remove conclusions about defeating presumptions or automatically satisfying draft disclosure obligations. |
| New DSA mapping issue | When is Article 27 applicable, and do local CE records support the required recommender-system information? | Correct the Article 26/27 distinction. Withdraw the unreviewed per-user reading and automatic local-to-global mapping. |

## Evidence and boundaries

- [Vovk, Petej and Fedorova (2015)](https://arxiv.org/abs/1511.00213):
  the merged probability loses the pair's perfect-calibration property.
- [European Parliament procedure 2022/0303(COD)](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2022%2F0303%28COD%29):
  withdrawal recorded on 6 October 2025.
- [DSA, Regulation (EU) 2022/2065](https://eur-lex.europa.eu/eli/reg/2022/2065):
  Article 26 advertising; Article 27 recommender-system transparency.
- [AI Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32024R1689):
  Article 50 transparency obligations; Article 86 explanation of individual decision-making.
- Source: `explanations/explanation.py` public `get_rules`,
  `build_rules_payload`, `to_telemetry`, and `ensured_explanations`;
  `core/wrap_explainer.py` training/calibration preprocessing paths.
- ADR-021 governs output interpretation; empirical execution establishes API
  behavior in a particular environment, not statistical or legal validity.

The worked-case factual metadata was also checked through the public API:
`prediction_uncertainty` contains the original prediction's [0.167, 0.333]
range, not the substituted scenario's [0.333, 0.600] range. The interpretation
guide now distinguishes them. This resolves an API-description issue, not a
new scientific validity question; no source-code change was needed.

No messages were sent to authors or legal reviewers. The Product Owner can
route these questions; no new public "open questions" page was created.

## Source-faithful refinement follow-up (16 November 2026)

The separate `beta/source-faithful-refinement-20261116` branch retains every
question above. Verified API corrections do not close scientific questions.

- **SR-02:** What validity statement applies when the difficulty estimator is
  fitted on proper-training data and then held fixed? What evidence supports
  any minimum category-size recommendation? The implementation's default has
  no difficulty estimator; configuration and coverage are separate questions.
- **SR-07/SR-09/SR-14:** Which uncertainty interpretations may research summaries
  and introductory definitions use? Width comparisons and model-response
  computations do not establish epistemic reduction or actionable interventions.
- **SR-16:** Which statements about reject confidence, singleton prediction sets
  and accepted-case error are justified? Guard filtering and rejection must not
  be described as the same procedure or as merged-probability thresholds.
- **N-01/N-07/N-08:** Which CE records support a deployment's transparency,
  oversight or assessment obligations? Correcting the Article 50/86 distinction
  and Article 27 FRIA reference does not determine applicability or sufficiency.
- **Legal follow-up:** Which retention, disclosure and rights-handling processes
  are appropriate under the applicable law? Which outcome-based fairness and
  utility analyses are needed? The earlier claims that weights prove necessity,
  widths establish discrimination, or CE records refute liability are withdrawn.
  Product Liability Directive article mappings are narrowed to Articles 6
  (damage), 7 (defectiveness), 9 (disclosure) and 10 (burden of proof); legal
  conclusions and the earlier monetary-threshold statement are not retained.

No reviewer decisions have been inferred and no external messages were sent.
