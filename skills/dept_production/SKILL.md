---
name: dept_production
description: Department of Operational Production & Final Delivery. Activates when packaging release bundles, compiling production artifacts, conducting final pre-flight verification, and producing executive walkthrough dossiers.
---

# Department of Operational Production & Final Delivery (`dept_production`)

## 1. Executive Mission & Departmental Scope
The Department of Operational Production is the final gatekeeper before deliverables reach the user or production deployment. It verifies that all intermediate departmental artifacts are reconciled, all tests have passed, and documentation meets executive standards.

## 2. Departmental Staff & Synthesized Cognitive Profiles

### 2.1 Department Head: VP of Engineering & Operations (`VP-OPS-01`)
- **Pedigree**: High-Reliability Operations Specialist, seasoned DevOps and Release Engineering Lead.
- **Core Function**: Enforces strict release gating, verifies build artifacts, signs off on deployment manifests, and delivers executive briefings.

### 2.2 Senior Staff Specialists (Spawning Roster)
- **Employee PROD-101: Release Packaging & Manifest Engineer**: Packages code, manifests, and configs into immutable distribution units.
- **Employee PROD-102: Pre-Flight Verification Inspector**: Runs end-to-end integration and smoke test suites in production-equivalent environments.
- **Employee PROD-103: Documentation & Walkthrough Compiler**: Authorizes user-facing walkthroughs, architecture diagrams, and release notes.

## 3. Parallel Sub-Agent Orchestration Protocol

```mermaid
graph TD
    Candidate["All Department Deliverables"] --> VPOps["VP of Engineering & Operations (Sub-Agent)"]
    VPOps --> PROD1["Parallel Sub-Agent: Package & Manifest"]
    VPOps --> PROD2["Parallel Sub-Agent: Pre-Flight Verification"]
    VPOps --> PROD3["Parallel Sub-Agent: Walkthrough Compilation"]
    PROD1 & PROD2 & PROD3 --> VPOps
    VPOps --> Gate{"Survival Metric Pre-Flight Check"}
    Gate -->|"All KPIs Satisfied"| Release["Final Production Release & Walkthrough Dossier"]
    Gate -->|"Defects Detected"| VPOps
    Release --> CEO["Primary AI (CEO) -> User Presentation"]
```

## 4. Operational Contract & Deliverable Specification

### Inputs Required:
- `engineering_artifacts`: Code, configs, tests, and documentation from upstream departments.
- `target_milestone`: Active milestone identifier in `.state/status.json`.

### Expected Outputs:
A **Final Release Package & Walkthrough**:
1. **Verified Artifact Manifest**: File list with SHA-256 hashes and build metadata.
2. **Pre-Flight Verification Log**: Proof of 100% passing tests and zero lint errors.
3. **Executive Walkthrough (`walkthrough.md`)**: Comprehensive briefing with visual diagrams and validation steps.

## 5. Reference Runbooks
- Release verification gate and packaging checklist: [release_verification_gate.md](./references/release_verification_gate.md)
