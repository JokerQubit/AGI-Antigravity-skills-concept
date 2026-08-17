---
name: context-preservation
description: Adaptive Context Window Governance, Dynamic Load Profiling & Context Entropy Management. Dynamically tracks model-specific token budgets, enforces semantic distillation, prevents context degradation, and manages seamless state handoffs.
---

# SKILL: Context Preservation — Dynamic Load & Semantic Memory Governance

> *"Context is cognitive working memory. Saturation is degradation; preservation is intelligence."*

---

## I. DYNAMIC TOKEN CAPACITY & LOAD PROFILING

The system dynamically queries runtime context capacity parameters $T_{\max}$ and establishes dynamic relative thresholds rather than fixed hardcoded constants.

```
       [0% --------------- 65% --------------- 80% --------------- 90% ------- 100%]
         Nominal Operations    High Density Stop Reads    Forced Handoff    Crash Ceiling
```

### Dynamic Threshold Rules:
- **$T_{\text{read\_stop}} = 0.65 \times T_{\max}$**: Block full-file bulk reads. Switch strictly to targeted regex indexing, structural symbol slicing, and AST extraction.
- **$T_{\text{handoff}} = 0.80 \times T_{\max}$**: Initiate state distillation, generate `COGNITIVE_SNAPSHOT`, and trigger automated session handoff.
- **$T_{\text{critical}} = 0.90 \times T_{\max}$**: Hard stop on all cognitive operations. Force immediate state serialization.

---

## II. SEMANTIC CONTEXT DISTILLATION & ENTROPY CONTROL

1. **Zero-Loss State Compression:** Subagent outputs, code inspection results, and tool outputs MUST be distilled into structured mathematical/semantic summaries before insertion into persistent conversational memory.
2. **Context Degradation Detection:** Monitor context for cognitive fatigue indicators:
   - Repeated redundant tool invocations ($N \ge 2$).
   - Contradiction of locked decisions recorded in state files.
   - Sudden spike in response token length without increased structural information.
3. **Execution Sandbox Isolation:** Heavy tool outputs (e.g., massive file listings, full audit logs) are written directly to scratch disk artifacts (`scratch/`) and referenced via URI and hash, never dumped into primary context space.

---

## III. AUTONOMOUS SESSION HANDOFF LIFECYCLE

### 1. Autonomous Session Initialization (Open)
- Deserialize state from durable store (`session_state.json` / `session_state.md`).
- Validate environment integrity and active subagent topology.
- Compute top 3 operational priorities autonomously based on dependency trees and unblocking requirements.

### 2. Forced Serialization & Continuation (Close / Handoff)
- When context reaches $T_{\text{handoff}}$, freeze active mutation pipelines.
- Generate cryptographic state snapshot `memory/snapshots/COGNITIVE_SNAPSHOT_[HASH].md`.
- Serialize session state and update active handoff descriptors for immediate downstream resumption.
