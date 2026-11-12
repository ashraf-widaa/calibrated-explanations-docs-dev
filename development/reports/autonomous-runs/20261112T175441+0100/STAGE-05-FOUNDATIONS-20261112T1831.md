# Stage 05 — Scientific foundations and references

**Started:** 18:29 · **Completed:** 18:31 (clock-read)
**Starting commit:** `34d61ebd`

## Audit

| ID | Finding |
|---|---|
| FD-A | Four concepts that the glossary deferred in G-P2 "for lack of a CE-specific source" now have teaching pages written in run 2: local/global explanation and feature attribution (ML basics A7, with literature), the Brier score (evaluation guide §2) and the reliability diagram (ADD-1 §1, Guo et al. 2017) |
| FD-B | Run 2 introduced new scientific statements that need a provenance record |
| FD-C | Canonical owners remain as set in run 1: semantics (guarantees), ADD-1 (methods), interpretation guide (reading), parameter reference (parameters), glossary (short definitions), autosummary (signatures). The new workflow page is the Level 1 entry and learning-path hub, not a competing definition source |

## Changes

| File | Change |
|---|---|
| `docs/glossary/science.md` | +4 entries with aliases: *Feature attribution* (Feature importance), *Local explanation* (Global explanation) → ML basics A7; *Brier score* → evaluation guide; *Reliability diagram* (Reliability table) → ADD-1 §1 |
| `docs/glossary/index.md` | A–Z regenerated (70 terms, 15 aliases) |
| `tests/docs/glossary/test_glossary.py` | Evaluation guide added as an allowed scientific owner |
| `SCIENTIFIC-CLAIMS-REGISTER.md` (run 2) | C2-01 to C2-16: every new run 2 statement with evidence level and status; SR-01 to SR-16 carried over unresolved |

Scientific author questions: unchanged; none resolved.

## Validation

| Check | Result |
|---|---|
| Strict Beta build | 0 warnings |
| Docs tests | 285 passed (glossary parametrised checks grew with the new entries) |
| Links | 153 pages, 0 broken |

## Commit, push, publication

- **Commit:** see `RUN-STATUS.md`.
- **Pushed:** no (B-01).
