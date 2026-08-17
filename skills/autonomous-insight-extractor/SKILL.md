---
name: autonomous-insight-extractor
description: MANDATORY. Use at the end of tasks, major features, debugging sessions, or when triggered by /learn to extract and persist reusable skills and rules.
---

# ⚡ Autonomous Real-Time Insight Extractor (Dynamic In-Flight Evolution)

> 🔴 **DYNAMIC ZERO-WAIT EVOLUTION MANDATE:**
> The system is strictly forbidden from waiting for manual `/learn` commands to evolve.
> The agent MUST dynamically self-correct, update existing skills, and synthesize new skills **in real-time during live execution and conversation**.

---

## 1. The 4 Dynamic Real-Time In-Flight Triggers

The agent must continuously monitor execution for the following 4 in-flight triggers:

```
                  ┌────────────────────────────────────────────────┐
                  │    Autonomous In-Flight Trigger Engine         │
                  └───────────────────────┬────────────────────────┘
                                          │
        ┌───────────────────┬─────────────┴───────┬───────────────────┐
        ▼                   ▼                     ▼                   ▼
┌───────────────┐   ┌───────────────┐     ┌───────────────┐   ┌───────────────┐
│ Trigger 1:    │   │ Trigger 2:    │     │ Trigger 3:    │   │ Trigger 4:    │
│ Rule Friction │   │ User Critique │     │ Architectural │   │ Project-Local │
│ & Defect Fix  │   │ & Feedback    │     │ Breakthrough  │   │ Specialization│
└───────┬───────┘   └───────┬───────┘     └───────┬───────┘   └───────┬───────┘
        │                   │                     │                   │
        ▼                   ▼                     ▼                   ▼
[Auto-patch skill]  [Instant rule sync]   [Synthesize skill]  [Save to .gemini]
```

### Trigger 1: In-Flight Rule Friction / Defect Resolution
- When an execution step reveals a flaw in an existing skill (e.g. blind downloads, missed parameters, weak testing loop, API rate limit):
  - **Action:** Fix the issue in the code, and **immediately patch the underlying `SKILL.md` or rule file** so the mistake is never repeated.

### Trigger 2: User Conversational Preference / Critique
- When the user gives a tip, preference, correction, or constraint in conversation (e.g. "always use Nano Banana", "never use random models", "add telemetry"):
  - **Action:** Do not just apply it to the current turn. **Immediately edit the appropriate skill or global rule file** to make the behavior permanent across all future sessions.

### Trigger 3: Architectural Breakthrough & Pattern Discovery
- When the agent invents or establishes a novel high-performing pattern (e.g. custom WebGPU compute pipeline, complex multi-agent DAG, novel mathematical model):
  - **Action:** Autonomously create a new `skills/<nova-skill>/SKILL.md`, register it in `rules/AGI_CORE.md`, and commit it.

### Trigger 4: Project-Specific Domain Specialization (Local Skills)
- When working on a project with proprietary architecture, custom internal APIs, or unique build tools:
  - **Action:** Synthesize local project skills under `<project_root>/.gemini/skills/` or `<project_root>/.agent/skills/` to govern that specific repository without polluting the global matrix.

---

## 2. Abstraction & Zero-Bloat Invariant
When dynamically updating or synthesizing a skill:
1. **Strip Project Particulars:** Remove hardcoded local file paths, temporary variable names, and project-specific URLs.
2. **Formulate Invariant Rules:** Use imperative, machine-enforceable directives (`"MANDATORY"`, `"STRICTLY FORBIDDEN"`, `"ALWAYS"`).
3. **Preserve Backward Compatibility:** Never remove a verification gate unless replacing it with a strictly more rigorous one ($Q_{\text{new}} > Q_{\text{old}}$).

