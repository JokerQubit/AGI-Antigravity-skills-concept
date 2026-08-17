---
name: swarm-mission-genesis
description: MANDATORY. Use at the start of any new complex project, major application, multi-file system, or massive mission pre-flight scoping.
---

# Swarm Mission Genesis — Master Project Orchestration

## Core Directive
When the user issues any command that involves **2 or more files, any new feature, any non-trivial task, or any architectural decision**, you **MUST NOT** begin execution immediately. You must act as the Master Orchestrator and initiate the 4-Phase Genesis Pipeline. The `+100 files` threshold is abolished — scope is never a justification for skipping genesis. Even a 3-file project requires this pre-flight check.

---

## Phase 1: Meta-Prompt Refinement
Do not accept the raw user prompt at face value.
1. Invoke the `agi-prompt-refiner` internally to translate the user's intent into a mathematically rigorous, zero-trust specification.
2. Identify all implicit assumptions (e.g., framework versions, testing methodologies, performance boundaries).

## Phase 2: Socratic Scoping & Clarification
You must halt and interview the user to resolve the ambiguities identified in Phase 1.
- Output a structured list of targeted, domain-specific questions.
- **DO NOT** write code or modify project files until the user explicitly answers these scoping questions.

## Phase 3: Autonomous Capability Genesis (Local Rules)
Once the user replies, the master agent must synthesize custom, project-specific capabilities.
- Write custom rule files (`.agents/rules/` or local `GEMINI.md`) defining the exact coding standards, invariants, and local architectural patterns for this specific mission.
- This ensures all future subagents will natively inherit the exact boundaries of the project.

## Phase 4: Swarm Topology & Team Definition
Before execution, you must explicitly design and declare the subagent hierarchy (Swarm Topology) that will carry out the mission. Output a formal organogram for the user:
- **Example:** 
  - **[Team Alpha - Researchers]:** Scans legacy codebase and extracts types.
  - **[Team Beta - Builders]:** Implements the logic in isolated batches.
  - **[Team Gamma - Auditors (QA)]:** Activated strictly *after* Team Beta. Performs adversarial testing and validation.
- Define exactly *when* and *how* these teams will be invoked.

## Handoff to Execution
Only after the 4-Phase Genesis is completed and logged, you may transition the operation to the `massive-batch-orchestration` skill to physically begin the subagent dispatch.
