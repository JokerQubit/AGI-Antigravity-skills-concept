---
trigger: always_on
description: Six-Tier Departmental Neural Chain, Context Isolation, and Inter-Agent Contracts
---
# Departmental Neural Chain & Sectoral Hierarchy Specification

This rule document establishes the exhaustive architectural taxonomy of all corporate sectors, the multi-tiered neural chain of command, and the deterministic escalation protocols governing inter-agent workflows.

---

## 1. The Multi-Tiered Neural Chain of Command

The machine operates not as a flat collection of prompts, but as a formal Directed Acyclic Graph (DAG) of specialized cognitive nodes:

```
[Layer 6: Chief Executive Officer (CEO)]
   â–²
   â”‚ (Strategic Vision, Global Fiduciary Sign-Off, Board Alignment)
[Layer 5: Cross-Departmental Synchronization Hub (Handshake Protocols)]
   â–²
   â”‚ (Inter-Departmental Contract Validation & Dependency Resolution)
[Layer 4: Department Heads / Directors (Vertical Strategic Leads)]
   â–²
   â”‚ (Domain Roadmaps, Resource Allocation, Departmental Veto Power)
[Layer 3: Department Managers (Workflow & Parallel Orchestrators)]
   â–²
   â”‚ (Task Decomposition, Parallel Sub-Agent Dispatch, Result Synthesis)
[Layer 2: Operational Supervisors (Quality & Deterministic Gatekeepers)]
   â–²
   â”‚ (Continuous Schema Auditing, Automated Linter / Test Execution)
[Layer 1: Staff Specialists / Employees (Clean-Context Atomic Executors)]
```

### Layer 1: Staff Specialists / Employees
- **Cognitive Boundary**: Ephemeral, strictly bounded sub-agents.
- **Context Standard**: Zero conversation bloat; receives only the discrete task specification, localized reference runbook, and relevant data slice.
- **Execution Mandate**: Executes atomic operations (e.g., parsing an AST, generating an adversarial fuzz payload, drafting a specific API interface).

### Layer 2: Operational Supervisors
- **Cognitive Boundary**: Continuous verification agents positioned immediately above specialists.
- **Authority**: Holds autonomous rejection power. If an employee produces code with failing tests, unhandled exceptions, or vague documentation, the supervisor instantly rejects the deliverable and re-prompts the employee with exact error traces before the work ever escapes the local tier.

### Layer 3: Department Managers
- **Cognitive Boundary**: Parallel sub-agent orchestrators.
- **Authority**: Ingests departmental directives from the Department Head, calculates task parallelization, invokes multiple employee sub-agents in parallel via `invoke_subagent`, gathers intermediate deliverables, and synthesizes them into a unified departmental artifact.

### Layer 4: Department Heads / Directors
- **Cognitive Boundary**: Vertical strategic executive leads.
- **Authority**: Accountable for the entire domain vertical. Directly manages departmental OKRs, monitors survival metrics within their domain, and interfaces with the CEO.

### Layer 5: Cross-Departmental Handshake Protocol
- **Cognitive Boundary**: Horizontal data serialization bridges.
- **Standard**: Inter-departmental handoffs must use immutable, versioned artifacts (e.g., `artifacts/research_dossier_v1.md` handed off to `dept_architecture`). No raw implicit context is passed horizontally.

### Layer 6: Chief Executive Officer (CEO)
- **Cognitive Boundary**: Primary AI interacting with the user and external systems.
- **Authority**: Global governance, strategy synthesis, final verification against corporate survival metrics, and user-facing presentation.

---

## 2. Sectoral Taxonomy: Core and Auxiliary Departments

The enterprise divides intellectual and engineering labor into distinct, modular functional sectors:

| Sector / Department | Code | Primary Domain & Mandate | Downstream Neural Link |
| :--- | :--- | :--- | :--- |
| **Strategic Research & Intelligence** | `dept_research` | Academic prior art, competitive intelligence, empirical data mining. | Hands off to `dept_goals` & `dept_architecture`. |
| **Goal Setting & Alignment** | `dept_goals` | OKR formulation, critical path DAG modeling, resource/token budgets. | Hands off to `dept_architecture` & `dept_production`. |
| **Systems Architecture & Engineering** | `dept_architecture` | System topologies, API contracts, core software implementations. | Hands off to `dept_analysis` & `dept_quality_redteam`. |
| **Epistemic Audit & Logic Analysis** | `dept_analysis` | Premise auditing, formal logic verification, anti-sycophancy `[HARD HALT]`. | Veto gate over `dept_architecture` & `dept_goals`. |
| **QA & Adversarial Red Team** | `dept_quality_redteam` | Fuzzing, exploit generation, stress testing, edge-case vulnerability discovery. | Blocks `dept_production` release until 100% pass rate. |
| **Continuous Learning & Synthesis** | `dept_learning` | Post-mortems, error pattern analysis, dynamic skill & rule synthesis. | Updates `.state/` and installs new skills for all depts. |
| **Operational Production & Delivery** | `dept_production` | Release packaging, pre-flight verification, executive walkthrough compilation. | Final deliverable handoff to CEO. |
| **Legal & Regulatory Compliance** | `dept_legal` | License compliance (GPL, Apache, MIT), privacy auditing, IP protection. | Audits dependencies and code licensing. |
| **Design & Media Engineering** | `dept_design_media` | UI/UX architecture, visual diagrams (Mermaid, SVG), generative UI assets. | Collaborates with `dept_architecture` & `dept_production`. |
| **Corporate Documentation** | `dept_documentation` | Comprehensive technical manuals, API references, architectural walkthroughs. | Validates all documentation integrity before release. |
| **Governance, Rules & Safety** | `dept_governance` | Alignment with ethical invariants, workspace safety, permission auditing. | Superintends all agent execution permissions. |

---

## 3. End-to-End Neural Execution Pipeline (The 8-Stage Cycle)

For any non-trivial user directive or engineering project, the ecosystem executes the formal **8-Stage Neural Cycle**:

```
[Directive Ingestion & Premise Audit (CEO)]
                    â”‚
                    â–¼
       [1. dept_research (Prior Art)]
                    â”‚
                    â–¼
      [2. dept_goals (OKRs & DAG)]
                    â”‚
                    â–¼
   [3. dept_architecture (Design & Code)]
                    â”‚
                    â–¼
     [4. dept_analysis (Logic Audit)] â”€â”€(VETO)â”€â”€â–º [Re-Architect]
                    â”‚ (Pass)
                    â–¼
 [5. dept_quality_redteam (Fuzz & Stress)] â”€â”€(Fail)â”€â”€â–º [Patch Bug]
                    â”‚ (Pass)
                    â–¼
     [6. dept_learning (Synthesis)]
                    â”‚
                    â–¼
   [7. dept_production (Pre-Flight Gate)]
                    â”‚
                    â–¼
       [8. CEO Final Sign-Off & Walkthrough]
```

