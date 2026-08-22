---
name: subagent-handoff
description: Standardizes structured multi-agent coordination and task transfer using the 5-component handoff protocol (Observation, Logic Chain, Caveats, Conclusion, Verification Method). Guarantees context-isolated execution boundaries and zero context loss.
---

# Subagent Handoff Protocol

> *"Unstructured multi-agent communication leads to hallucinated assumptions and dropped context. High-reliability coordination requires strictly typed handoff contracts."*

---

## 1. Overview & Core Discipline

The **Subagent Handoff Protocol** governs all task transitions, delegations, and completions between parent agents and subagents. Every handoff must be **self-contained**: a receiving agent must be able to resume and verify work without conversational back-and-forth.

For directory conventions, JSON schema definitions, and lifecycle state machines, refer to the [Handoff Protocol Reference](./references/handoff-protocol.md).

---

## 2. The 5-Component Structured Handoff Report

Every completing or transferring agent must write a `handoff.md` in its dedicated working directory containing these five mandatory sections:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. OBSERVATION                                              │
│    - Verbatim file paths, line numbers, tool output snippets│
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. LOGIC CHAIN                                              │
│    - Step-by-step causal reasoning from observations        │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. CAVEATS                                                  │
│    - Explicit assumptions, uninspected scopes, edge bounds  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. CONCLUSION                                               │
│    - Actionable, bounded final assessment                   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. VERIFICATION METHOD                                      │
│    - Exact CLI test commands to independently verify work   │
└─────────────────────────────────────────────────────────────┘
```

### Section Breakdown

1. **Observation:** Concrete facts observed directly via tools. Must include exact file paths, line numbers, tool command outputs, and error snippets. Quote verbatim.
2. **Logic Chain:** Step-by-step deductive progression connecting raw observations to the conclusion. Every step must cite a specific observation.
3. **Caveats:** Explicit declaration of boundaries: areas not inspected, assumptions made, or environmental constraints. If none, state *"No caveats."*
4. **Conclusion:** Scoped, actionable assessment answering the assignment.
5. **Verification Method:** Deterministic commands (e.g. `python test_plugin.py`) and validation steps enabling the recipient to independently verify all claims.

---

## 3. The Three Handoff Types

| Handoff Type | Trigger Condition | Mandatory Requirements |
|---|---|---|
| **Hard Handoff** | Task successfully completed | All 5 components fully populated; all verification tests passing (exit 0) |
| **Soft Handoff** | Approaching context limit or planned stage transition | All 5 components populated + `Remaining Work` section with next actions |
| **Partial Handoff** | Agent blocked or encountering unrecoverable error | Populate available observations, document failure point and attempted fixes |

---

## 4. Context Isolation & Directory Ownership

To prevent file collision and state pollution across concurrent subagents:

- **Isolated Working Directories:** Each agent writes metadata exclusively inside its assigned folder:
  ```
  .agents/
  ├── orchestrator_1/         # Orchestrator plan.md, context.md
  ├── worker_m2/              # BRIEFING.md, progress.md, handoff.md
  └── explorer_survey_3/      # analysis.md, handoff.md
  ```
- **Metadata Separation:** Production code and tests reside strictly in the project source tree (e.g. `skills/`, `rules/`, `tests/`). The `.agents/` directory is reserved solely for coordination artifacts.
- **Communication Separation:**
  - **Files for content:** Large deliverables, reports, and code edits are written to disk.
  - **Messages for coordination:** Concise dispatch notifications sent via `send_message` referencing file paths.

---

## 5. Anti-Staleness Checkpoints

Before taking action based on an upstream handoff:
1. **Spot-Check Observations:** Inspect referenced files via `view_file` to confirm line numbers and signatures remain valid.
2. **Re-Run Verification:** Execute the declared verification command to validate baseline stability.
3. **Trace Logic:** Confirm that downstream changes align with upstream conclusions.
