# Stage 00 — Deployment verification

**Time:** 2026-11-12 17:54–18:00

| Check | Evidence | Result |
|---|---|---|
| Remote `main` | `git ls-remote docs-dev refs/heads/main` | `22629495` (run 1 investigation commit, pushed by the PO) |
| Latest Read the Docs build | API v3 builds | #35841238, 14:24:46Z, **Finished, success**, commit `22629495` |
| Previous build | API | #35840928 (`b0b2cdc6`) Cancelled; superseded in effect by #35841238, which includes `b0b2cdc6` |
| Homepage | Headless Edge, live | H2s: Documentation, Project & Resources, Commercial Services; 4 cards; resources: Project, Glossary, GitHub, License; Commercial: Contact Grejna AB; footer "CE Beta Documentation / Entry-point tier: Tier 1."; 5 sidebar "Overview" entries; Glossary in the sidebar; `ce-home.css` loaded |
| Pages | HTTP status, live | glossary index and science: 200; Quick Start: 200; walkthrough: 200; In Practice: 200; API page: 200; walkthrough notebook: 200 |

**Conclusion:** run 1 is published and verified live. No deployment fix was needed.

**Access:** no Read the Docs credentials. `git push` is still denied to the agent (B-01).
