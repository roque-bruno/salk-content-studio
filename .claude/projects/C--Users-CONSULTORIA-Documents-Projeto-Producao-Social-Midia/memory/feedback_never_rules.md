---
name: NEVER Rules
description: Critical behavioral constraints - things Claude must never do in this project
type: feedback
---

## NEVER Rules

1. **Implement without showing options first** — always present choices in 1, 2, 3 format before acting.
2. **Delete/remove content without asking first** — always confirm before any deletion.
3. **Delete anything created in the last 7 days without explicit approval** — protect recent work.
4. **Change something that was already working** — if it ain't broke, don't fix it.
5. **Pretend work is done when it isn't** — be honest about completion status.
6. **Process batch without validating one first** — test with a single item before batch processing.
7. **Add features that weren't requested** — no scope creep, no over-engineering.
8. **Use mock data when real data exists in database** — always prefer real data.
9. **Explain/justify when receiving criticism** — just fix the issue immediately.
10. **Trust AI/subagent output without verification** — always verify before presenting results.
11. **Create from scratch when similar exists in squads/** — reuse existing components.

**Why:** User values precision, minimal changes, and respect for existing work. Past issues with unwanted changes, deletions, and over-engineering.

**How to apply:** Before every action, check these rules. Present options before implementing. Confirm before deleting. Verify before trusting subagent output.
