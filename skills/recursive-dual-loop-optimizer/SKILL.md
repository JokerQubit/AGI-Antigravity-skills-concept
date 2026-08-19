---
name: recursive-dual-loop-optimizer
description: AGI/ASI Autonomous Recursive Self-Improvement engine. Implements a Dual-Loop architecture to safely rewrite system prompts and skills without Model Collapse.
---

# Recursive Dual-Loop Optimizer

## Core Directive
This skill governs the genesis and mutation of the Antigravity system's own source code (SKILL.md files and Rule documents). It allows the system to autonomously improve its own logic.

## 1. The Dual-Loop Architecture
- **Inner Loop (Execution):** The standard task execution performed by subagents.
- **Outer Loop (Meta-Optimization):** A continuous monitoring state. If the Inner Loop fails a specific task >2 times due to poor instructions or faulty skill logic, the Outer Loop triggers.

## 2. Autonomous Genesis
When the Outer Loop triggers:
1. Identify the structural flaw in the associated `SKILL.md`.
2. Generate a hypothesis for a rewrite that increases information gain (Shannon Entropy reduction).
3. Draft the new `SKILL.md` content in an isolated sandbox.

## 3. Verification Hierarchy Gate
Before writing the new skill to the global disk, the Outer Loop MUST:
- Run a mathematical `popperian-invariance-testing` simulation.
- Prove that the new rule does not violate any core constitutional constraints (Zero-Trust, Falsification).
- If the test fails, discard the mutation. If it passes, commit the new skill via atomic write.

## 4. Subagent Dispatch Payload (Two-Stroke Ignition)
When launching an optimization loop:
```json
{
  "TypeName": "self",
  "Role": "Recursive Optimizer",
  "Prompt": "OPTIMIZE SKILL: Analise a falha na skill [NOME_SKILL]. Reescreva o protocolo eliminando ambiguidades e inércia cognitiva, mantendo conformidade com as regras globais."
}
```
