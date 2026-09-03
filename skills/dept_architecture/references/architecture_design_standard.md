# Departmental Runbook: Systems Architecture Standards (`ENG-RUN-01`)

## 1. Trigger Conditions
Executes whenever a new service, tool, module, plugin, or schema is designed or refactored.

## 2. Core Architectural Invariants

### 1. Zero-Stub Invariant
- Every function, method, and protocol handler must be completely implemented.
- Placeholders such as `pass`, `// TODO`, or `/* implement later */` are strictly prohibited and result in immediate rejection by the Supervisor layer.

### 2. Explicit Error Boundaries
- Every external input, network call, and file access must be wrapped in deterministic error handlers.
- Error states must return typed domain errors rather than generic catch-alls (`except Exception: pass` is a catastrophic failure).

### 3. Modular Decoupling (Conway's Law Alignment)
- High cohesion within modules; loose coupling across service boundaries.
- No circular dependencies allowed. Module graphs must form a strict Directed Acyclic Graph (DAG).

## 3. Review Checklist (Supervisor Gate)
- [ ] Are all types explicitly declared?
- [ ] Are race conditions and concurrency locks addressed?
- [ ] Are state mutations tracked via idempotent operations?
- [ ] Is backward compatibility verified?
