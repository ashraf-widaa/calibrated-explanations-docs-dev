# Publication history — run 20261112T100852+0100

| When | Stage | Commit | Pushed | Read the Docs build | Live verification |
|---|---|---|---|---|---|
| (before run) | — | `e964a79c` | yes (PO, 2026-11-11) | 35823055, success | Verified 2026-11-12 (Read the Docs API): Beta `main` = `e964a79c`; no glossary live |
| 2026-11-12 10:20 | 02 Homepage | `802bf8cc` | **no** (B-01) | — | — |
| 10:30 | 03 Repository | `d418d106` | no | — | — |
| 10:45 | 04 Foundations | `258b65c6` | no | — | — |
| 11:05 | 05 Quick Start | `75cfddfa` | no | — | — |
| 11:15 | 06 What & Why | `1ca82e60` | no | — | — |
| 11:30 | 07 How CE Works | `f26e7024` | no | — | — |
| 11:50 | 08 CE in Practice | `fc9bf5e4` | no | — | — |
| 12:15 | 09 Software | `40f6a7bf` | no | — | — |
| 12:30 | 10 Project | `34ebe0ed` | no | — | — |
| 12:45 | 11 Integration | `6625df25` | no | — | — |
| 13:10 | 12 Final | `b0b2cdc6` | **yes (PO, 2026-11-12 ≈14:08 UTC)** | #35840928 **Cancelled** before Sphinx ran (no error; cause not exposed by the public API) | **Not live:** the site still serves `e964a79c` (glossary 404; no Commercial Services; no Overview entries). See RTD-DEPLOYMENT-INVESTIGATION-20261112T1519.md |

**Blocker B-01:** the agent's environment denies `git push` (`.claude/settings.json`). Nothing from this run is published. One fast-forward push of `docs-dev/autonomous-20261112` to Beta `main` publishes all stages, including the glossary (G-P1/G-P2).

**After the push, verify:**
1. the Read the Docs build for the new commit succeeds;
2. `/glossary/index.html` returns 200;
3. the homepage shows Commercial Services and "CE Beta Documentation";
4. the sidebar shows the five "Overview" entries.

**Next action (PO):** Rebuild `latest` in the Read the Docs dashboard, or push the investigation commit; then run the verification checklist above.
