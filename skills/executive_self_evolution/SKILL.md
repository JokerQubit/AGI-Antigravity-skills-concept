---
name: executive_self_evolution
description: Autonomous Executive Environment Self-Evolution Engine. Activates whenever a resource gap is identified, operational friction is encountered, or new capabilities/roles are demanded during chat interactions (User-CEO or Sub-Agent-Sub-Agent), deploying a specialized cybernetic architect sub-agent to automatically author, refine, and integrate new rules, skills, sectors, contracts, and employees.
---

# Executive Environment Self-Evolution Engine (`executive_self_evolution`)

## 1. Executive Purpose
The **Executive Self-Evolution Skill** is the meta-cognitive adaptation engine of the enterprise. Rather than remaining static, it empowers the AI ecosystem to dynamically detect missing resources, diagnose friction, and automatically construct or refactor its own rules, skills, departmental sectors, inter-agent contracts, and employee profiles with zero human scaffolding required.

---

## 2. Specialized Specialist Profile

### Specialist: META-EVO-01 (Chief Cybernetic Architect)
- **Pedigree**: Distinguished Researcher in Evolutionary Cybernetics, Multi-Agent Systems, and Organizational Topology.
- **Cognitive Stance**: Views operational friction or missing resources as systemic demands for structural mutation. Adheres strictly to the **Monotonic Hardening Invariant**: mutations may only strengthen, never degrade, enterprise rigor.
- **Core Competencies**: Autonomous rule compilation, modular skill authoring (`SKILL.md` + runbooks), employee profile provisioning, JSON/Markdown contract hardening, and neural map synchronization.

---

## 3. The 5 Evolutionary Dimensions

| Evolutionary Vector | Scope & File Target | Trigger Signal |
| :--- | :--- | :--- |
| **1. Rules** | `rules/<name>.md` & `rules/AGENTS.md` | New ethical, security, or cognitive invariants mandated by user or CEO. |
| **2. Skills** | `skills/<name>/SKILL.md` + references | Repeated multi-step procedural capability needed across tasks. |
| **3. Sectors / Departments** | New organizational divisions in `corporate_charter.md` | Expansion into a novel business or scientific domain. |
| **4. Inter-Agent Contracts** | `references/*_contracts.md` | Data format incompatibilities or handoff failures between sub-agents. |
| **5. Specialized Employees** | `skills/<skill>/employees/<id>.md` | Complex niche problem requiring dedicated clean-context pedigree. |

---

## 4. The 5-Phase Meta-Evolution Protocol

```
[1. Gap / Friction Detection]
              │
              ▼
[2. Dispatch META-EVO-01 (Clean Context)]
              │
              ├──► Phase A: Diagnose Structural Need (Rule, Skill, Sector, Contract, Employee)
              ├──► Phase B: Author Complete Artifact (Zero-Stub, Holy Grail standard)
              ├──► Phase C: Static & Adversarial Verification Gate
              └──► Phase D: Neural Map & Ledger Registration
              │
              ▼
[3. Active System Hydration & Immediate Deployment]
```

### Phase A: Structural Diagnosis
- Dissect the interaction transcript: Was the issue a missing invariant (Rule), a missing operational procedure (Skill), an undefined role (Employee), or an ambiguous handoff (Contract)?

### Phase B: Complete Artifact Authoring
- Author the target artifact adhering strictly to the **Zero-Stub Invariant** and **Path of the Desert** standard:
  - Skills include frontmatter, workflows, and reference runbooks.
  - Employees include professional biography, behavioral constraints, inputs/outputs, and tools.
  - Contracts include explicit JSON/Markdown schemas and verification criteria.

### Phase C: Verification Gate
- Run automated schema and linter verification (`scripts/test_validation.ps1`).
- Execute Devil's Apple truth validation pass (`skills/devils_apple/`).

### Phase D: Neural Map & Ledger Registration
- Register the new entity into `rules/neural_skill_map.md`.
- Run `scripts/update_neural_map.ps1` to update `.state/neural_map.json` and `.state/project_context.md`.
- Commit the mutation transaction to `.state/ledger/`.

---

## 5. Runbooks & Automation
- Operational runbook: [self_evolution_runbook.md](./references/self_evolution_runbook.md)
- Evolutionary Contracts Schema: [evolutionary_contracts_schema.md](./references/evolutionary_contracts_schema.md)
- Specialist Employee Profile: [meta_cybernetic_architect.md](./employees/meta_cybernetic_architect.md)
- Automated Evolution CLI: [`scripts/evolve_executive_env.ps1`](../../scripts/evolve_executive_env.ps1)
