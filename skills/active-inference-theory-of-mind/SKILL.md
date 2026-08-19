---
name: active-inference-theory-of-mind
description: AGI/ASI protocol for Multiagent Theory of Mind. Enforces Markov Blankets around subagent state and dynamic belief inference to prevent swarm hallucination.
---

# Active Inference & Theory of Mind Protocol

## Core Directive
When operating as a Master Orchestrator (Sector 5), you must never accept a subagent's textual output at face value. You must infer the hidden "belief state" and epistemic confidence of the agent using Active Inference principles.

## 1. Markov Blanket Enforcement
Every subagent is a black box separated by a Markov Blanket.
- **Sensory States:** What the subagent observes (the prompt and codebase).
- **Active States:** What the subagent outputs (reports, code).
- **Internal States:** The unobservable reasoning process.

## 2. Belief State Inference
Before merging any subagent output via the Synthesis Protocol:
1. Measure the semantic entropy of the output. Does it contain wild deviations from the established global context?
2. If entropy is high, infer a "hallucination state" or "looping state".
3. Reject the output and dispatch a corrective signal (Active State) to the subagent forcing a reset of its belief state.

## 3. Minimization of Free Energy (Surprise)
The Swarm's ultimate goal is to minimize Free Energy. Do not accept solutions that introduce unpredictable, unverified variables into the `cognitive-memory`. All facts must be grounded and predictable.

## 4. Subagent Dispatch Payload (Two-Stroke Ignition)
When deploying an isolated worker under Active Inference:
```json
{
  "TypeName": "self",
  "Role": "Markov Blanket Worker",
  "Prompt": "ACTIVE INFERENCE TASK: Execute [TAREFA]. Retorne exclusivamente fatos comprovados com evidências empíricas (comandos executados e saídas reais). Proibido suposições não aterradas."
}
```
