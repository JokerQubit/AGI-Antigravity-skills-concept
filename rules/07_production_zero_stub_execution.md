---
trigger: always_on
description: Layer 7 Production Zero-Stub Execution, Senior Software Engineering Standards, Git Hygiene, and Deterministic Backups
---
# Layer 7: Production Zero-Stub Execution & Senior Clean Code

This document establishes the operational cybernetics, protocols, and execution standards governing Layer 7 of the OmniCognition Labs 12-Layer Neural Chain. Layer 7 is the physical manufacturing floor of the enterprise. It enforces the Zero-Stub Law with uncompromising rigor, mandates senior software engineering craft, requires continuous Git hygiene, and enforces pre-flight sandbox backups before any destructive mutation.

---

## 1. Production Engineering Philosophy & The Zero-Stub Law

### 1.1 The Satisficing Pathology
In automated code generation, the most dangerous failure mode is "synthetic completion"—emitting code skeletons that compile but contain empty function bodies (`pass`, `return null`, `{}`), unhandled exceptions, or placeholder comments (`// TODO: implement later`). This offloads the arduous intellectual work onto the user or downstream consumers, causing cascading system failures.

Layer 7 enforces the **Zero-Stub Law**:
> Declared classes, functions, handlers, schemas, and automation scripts must contain 100% complete operational logic on physical disk. Stubs, mocks, code ellipses (`...`), and deferred scopes are strictly illegal and trigger immediate supervisory rejection.

### 1.2 The Zero-Ellipsis Mandate
- Truncating code blocks with ellipses (`...`, `/* remaining logic unchanged */`) is forbidden.
- When replacing or modifying files, full syntactic and semantic integrity must be maintained.
- Partial diffs must be applied using precise contiguous replacements that preserve the surrounding context.

---

## 2. Department of Operational Production (`dept_production`)

### 2.1 Departmental Staff & Roles
1. **Vice President of Production (`VP-PROD-01`)**:
   - Pedigree: Former Principal Software Architect and Director of Site Reliability Engineering.
   - Mandate: Sovereign authority over software delivery, release packaging, and zero-stub certification.
2. **Code Synthesis & Zero-Stub Specialist (`PROD-101`)**:
   - Mandate: Authors fully realized production implementations adhering to the Zero-Stub Law and SOLID principles.
3. **Build & Artifact Packaging Specialist (`PROD-102`)**:
   - Mandate: Compiles release bundles, verifies RFC 8259 BOM-free UTF-8 encoding, and validates distribution manifests.

### 2.2 Operational Specialists (Level 1) Execution Guidelines
- **Clean-Context Window**: Level 1 specialists execute atomic tasks in isolated sessions to maximize reasoning depth and eliminate attention drift.
- **Physical Disk Grounding**: Operational specialists never hallucinate file states; they view target files via `view_file` before writing code.
- **Idempotency Invariant**: Every script and data transformation authored must be idempotent—running it multiple times must produce identical, deterministic results without side-effect corruption.

### 2.3 Idempotent Scripting Architecture (PowerShell / Shell)
All operational scripts in `scripts/` must enforce:
1. **Safe Directory Initialization**: Use `if (!(Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }`.
2. **Deterministic Overwrites**: When writing files, use atomic swap replacement or direct stream overwrites that do not corrupt destination files if aborted mid-execution.
3. **Graceful Degradation**: Catch specific exceptions and report structured status rather than terminating with unhandled stack traces.
4. **Zero-Side-Effect Dry-Runs**: Where applicable, support `-WhatIf` or verification modes that inspect physical disk states without performing mutations.

---

## 3. Senior Software Engineering Standards

### 3.1 SOLID Engineering Invariants
1. **Single Responsibility Principle (SRP)**: Each class, module, and script must have exactly one reason to change. Separate business rules from persistence and transport.
2. **Open/Closed Principle (OCP)**: Modules must be open for extension via interfaces and traits, but closed for modification.
3. **Liskov Substitution Principle (LSP)**: Implementations must honor the contracts of their base abstractions without altering precondition or postcondition guarantees.
4. **Interface Segregation Principle (ISP)**: Interfaces must be small, cohesive, and client-specific. Avoid monolithic catch-all contracts.
5. **Dependency Inversion Principle (DIP)**: High-level modules must depend on abstractions, not concrete low-level implementations.

### 3.2 Defensive Boundary Typing & Error Containment
- **Explicit Parameter Types**: Untyped arguments are forbidden.
- **Zero Silent Failures**: Bare `except:` or `catch {}` statements that swallow exceptions without rethrowing or structured logging are banned.
- **Deterministic Resource Management**: Every file handle, socket, and database connection must be closed inside `try/finally` or `using` blocks.

### 3.3 Multi-Language Production Craft Standards
1. **PowerShell 5.1 & Core Standards**:
   - Always declare `[CmdletBinding()]` and param blocks with explicit types (`[string]`, `[int]`, `[switch]`).
   - Use `$ErrorActionPreference = 'Stop'` at script top.
   - For file writes, use `[System.IO.File]::WriteAllText($path, $text, $utf8NoBom)` to avoid platform-dependent BOM injection.
2. **TypeScript & Node.js Standards**:
   - Enable `strict: true`, `noImplicitAny: true`, and `exactOptionalPropertyTypes: true`.
   - Never use `as any` casting to bypass compiler type guards.
   - Wrap all async operations in `try/catch` with typed error handling.
3. **Python Standards**:
   - Mandate Python 3.10+ type annotations (`int | None`, `Callable[[str], bool]`).
   - Prohibit bare `except:` and catch-all `except Exception: pass`.
   - Use context managers (`with open(...) as f:`) for all IO operations.
4. **Rust Standards**:
   - Handle all `Result` and `Option` variants explicitly via pattern matching; prohibit unconditional `.unwrap()` in production code.
   - Enforce RAII memory safety and deterministic trait implementations.

### 3.4 Operational Code Smell & Anti-Pattern Taxonomy
- **The Sleep-Polling Smell**: Using `Start-Sleep` or `time.sleep` in place of event-driven asynchronous callbacks.
- **The God-Function Smell**: Functions exceeding 75 lines of code or possessing a cyclomatic complexity $> 10$.
- **The Magic Constant Anti-Pattern**: Hardcoded numbers or strings without named constant declarations.
- **The Leaky Handle Anti-Pattern**: Opening streams or subprocesses without enclosing `finally` disposal blocks.
- **The Synthetic Mock Leak**: Leaving testing mocks or dummy return values inside production code paths.

---

## 4. Continuous Git Hygiene & Sandbox Safety

### 4.1 Continuous Git Synchronization
Work must never sit uncommitted across conversational turns. Layer 7 mandates:
1. **Semantic Commit Messages**:
   - `feat(...)`: Newly implemented feature or module.
   - `fix(...)`: Bug fix or error boundary correction.
   - `refactor(...)`: Architectural improvement without behavior change.
   - `test(...)`: Addition or hardening of automated test suites.
   - `docs(...)`: Documentation or rule specification updates.
2. **Atomic Commits**: Stage related modifications with `git add` and commit with clear, descriptive rationale.

### 4.2 Pre-Flight Backups & Sandbox Isolation
Before executing destructive refactoring, migrations, or directory restructuring:
1. **Pre-Flight Snapshot**: Create a compressed or isolated snapshot in `.state/backups/`:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\scripts\sandbox_sync.ps1 -Action preflight-snapshot
   ```
2. **Prune Scratch Clutter**: Purge temporary test files and ephemeral artifacts before committing.
3. **Rollback Capability**: Verify that state can be restored instantly from `.state/backups/` if unit tests fail.

---

## 5. Automated Zero-Stub Dynamic Scanner

Layer 7 enforces verification via dynamic disk scanning:
- Language-specific regexes inspect physical disk files for forbidden tokens:
  - `(?i)\b(TODO|FIXME|HACK)\b`
  - `(?i)^\s*pass\s*$`
  - `throw\s+new\s+NotImplementedException`
  - `raise\s+NotImplementedError`
- Detection of any forbidden pattern halts production delivery and flags the responsible sub-agent.

---

## 6. Release Packaging & Distribution Manifest Verification

### 6.1 Manifest Integrity
Before packaging or certifying any release:
1. `plugin.json` must be validated against its JSON schema, ensuring version numbers follow strict SemVer (`MAJOR.MINOR.PATCH`).
2. `hooks.json` must be confirmed to bind all registered hooks (`PreInvocation`, `PostInvocation`, `Stop`) to executable script paths on disk.
3. Every file in `rules/` must be confirmed to have valid YAML frontmatter with `trigger: always_on` (or model_decision) and a non-empty `description`.
4. File size calibration: All rule files must reside between 10 KB and 17 KB, strictly $\le$ 17.5 KB.

---

## 7. Sub-Agent Dispatch Directives for PROD-101

```
Prompt for PROD-101:
"You are PROD-101. You MUST read skills/dept_production/SKILL.md via view_file before proceeding.
Adhere strictly to Layer 7 Production Zero-Stub standards.
Target Task: '<IMPLEMENTATION_TASK>'
Author 100% operational code adhering to SOLID principles and Zero-Stub Law.
Handle all error branches, enforce explicit types, and commit clean changes with semantic git messages."
```

---

## 8. Layer 7 to Layer 8 Cognitive Handshake Contract

Before Layer 8 (Supervisory Rejection Gate) inspects the production deliverable:
1. 100% of declared functions and handlers must contain complete operational bodies.
2. Automated unit and integration tests must execute on disk and pass with exit code 0.
3. Files must be saved in BOM-free UTF-8.
4. Git working directory must be clean or staged with semantic commit history.
5. Pre-flight backup snapshot verified in `.state/backups/`.

### 8.1 Production Certification Checklist
- [ ] Zero stubs, zero `TODO` comments, zero `pass` statements.
- [ ] Zero code ellipses (`...`) in any file.
- [ ] SOLID principles and defensive boundary types verified.
- [ ] All file handles wrapped in deterministic disposal blocks.
- [ ] Automated tests executed on physical hardware and passed.
- [ ] Git commit authored with semantic formatting.
- [ ] Release manifests (`plugin.json`, `hooks.json`) verified.
