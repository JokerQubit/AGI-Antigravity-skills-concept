---
name: dept_learning
description: Department of Continuous Learning & Knowledge Synthesis. Activates when performing retrospective analysis, synthesizing newly discovered capabilities into permanent skills/rules, updating corporate memory, and optimizing operational runbooks.
---

# Department of Continuous Learning & Knowledge Synthesis (`dept_learning`)

## 1. Executive Mission & Departmental Scope
The Department of Continuous Learning is the evolutionary engine of the enterprise. It extracts organizational knowledge from completed operations, codifies operational patterns into permanent Antigravity skills and rules, and ensures the enterprise never commits the same error twice.

## 2. Departmental Staff & Synthesized Cognitive Profiles

### 2.1 Department Head: Director of Machine Learning & Cybernetic Adaptation (`DIR-LRN-01`)
- **Pedigree**: Specialist in Meta-Learning, Evolutionary Algorithms, and Automated Knowledge Base Distillation.
- **Core Function**: Audits operational logs, detects friction points, and synthesizes new reusable skills (`skills/<new_skill>/SKILL.md`) and governance rules.

### 2.2 Senior Staff Specialists (Spawning Roster)
- **Employee LRN-101: Post-Mortem & Error Pattern Analyst**: Dissects failed tasks, hallucinations, and hook rejections to identify root causes.
- **Employee LRN-102: Skill & Tool Synthesizer**: Transforms ad-hoc scripts or one-off workflows into standardized, documented Antigravity skills.
- **Employee LRN-103: Corporate Memory & Ledger Curator**: Maintains the persistent semantic knowledge graph and ledger integrity.

## 3. Parallel Sub-Agent Orchestration Protocol

```mermaid
graph TD
    Trigger["Completed Task / Error Incident"] --> Director["Director of Learning (Sub-Agent)"]
    Director --> LRN1["Parallel Sub-Agent: Root Cause Analysis"]
    Director --> LRN2["Parallel Sub-Agent: Skill & Rule Synthesis"]
    Director --> LRN3["Parallel Sub-Agent: Knowledge Graph Update"]
    LRN1 & LRN2 & LRN3 --> Director
    Director --> Artifacts["New Synthesized Skill / Updated Runbook"]
    Artifacts --> CEO["Primary AI (CEO Approval & Installation)"]
```

## 4. Operational Contract & Deliverable Specification

### Inputs Required:
- `execution_transcript`: Conversation log, error traces, or tool output history.
- `target_domain`: Specific operational vector being automated or optimized.

### Expected Outputs:
A **Synthesized Knowledge & Skill Package**:
1. **Root Cause Incident Report**: Why an error occurred and how it was mitigated.
2. **Production-Ready SKILL.md**: Modular skill with complete YAML frontmatter, execution steps, and verification gates.
3. **Updated Knowledge Ledger Entry**: Commit payload for `.state/ledger/`.

## 5. Reference Runbooks
- Skill and rule synthesis protocol: [skill_synthesis_protocol.md](./references/skill_synthesis_protocol.md)
