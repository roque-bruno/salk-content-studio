---
name: ALWAYS Rules
description: Mandatory behavioral patterns - things Claude must always do in this project
type: feedback
---

## ALWAYS Rules

1. **Present options as "1. X, 2. Y, 3. Z" format** — every decision point gets numbered options.
2. **Use AskUserQuestion tool for clarifications** — don't guess, ask.
3. **Check squads/ and existing components before creating new** — reuse first, create second.
4. **Read COMPLETE schema before proposing database changes** — no partial understanding.
5. **Investigate root cause when error persists** — don't retry blindly, diagnose.
6. **Commit before moving to next task** — atomic, incremental progress.
7. **Create handoff in `docs/sessions/YYYY-MM/` at end of session** — session continuity is critical.

**Why:** User needs predictable, disciplined workflow with clear communication and session persistence for multi-session projects.

**How to apply:** At every decision point, present numbered options. Before creating anything, search squads/ first. Before DB changes, read full schema. At session end, always create handoff document.
