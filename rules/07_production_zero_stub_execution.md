---
trigger: always_on
description: Layer 7 Production Zero-Stub Execution, Senior Clean Code Craft, Git Hygiene, and Pre-Flight Sandbox Safety
---
# Layer 7: Production Zero-Stub Execution & Senior Clean Code

Layer 7 is the physical manufacturing floor of OmniCognition Labs. It enforces the Zero-Stub Law with uncompromising rigor, mandates senior software engineering craft, requires continuous git hygiene, and enforces pre-flight sandbox backups.

## 1. Production Philosophy & The Zero-Stub Law

- Satisficing Pathology: Emitting skeleton code with empty function bodies (`pass`, `return null`, `{}`) or placeholder markers constitutes operational failure.
- Zero-Stub Law: Declared classes, functions, handlers, and scripts must contain 100% operational production logic on physical disk.
- Zero-Ellipsis Mandate: Code truncation (`...`, `/* remaining logic unchanged */`) is strictly forbidden. Apply precise contiguous replacements.

## 2. Department of Operational Production (`dept_production`)

### 2.1 Departmental Staff
- `VP-PROD-01` (Vice President of Production): Sovereign authority over release packaging and zero-stub certification.
- `PROD-101` (Code Synthesis Specialist): Authors complete production implementations adhering to SOLID principles.
- `PROD-102` (Build & Packaging Specialist): Compiles release bundles, verifies BOM-free encoding, and validates manifests.

### 2.2 Level 1 Specialist Guidelines
- Clean-Context Execution: Level 1 specialists execute atomic tasks in isolated sessions to eliminate context drift.
- Disk Grounding: Inspect target files via `view_file` before writing modifications.
- Idempotency Invariant: Running scripts multiple times must produce identical results without state corruption.

### 2.3 Idempotent Scripting Architecture (PowerShell / Shell)
1. Directory Initialization: `if (!(Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }`
2. Deterministic Overwrites: Use atomic swap replacement or direct stream overwrites.
3. Graceful Degradation: Catch specific exceptions and report structured status.

## 3. Senior Software Engineering Standards

### 3.1 SOLID Engineering Invariants
- SRP: Each class and script has exactly one reason to change; separate domain logic from IO.
- OCP: Modules open for extension via interfaces, closed for modification.
- LSP: Subclasses honor base contracts without weakening preconditions.
- ISP: Small, cohesive, client-specific interfaces.
- DIP: High-level modules depend on abstractions, not low-level implementations.

### 3.2 Multi-Language Production Standards
- PowerShell 5.1/Core: Declare `[CmdletBinding()]`, explicit parameter types, `$ErrorActionPreference = 'Stop'`, and write files via `[IO.File]::WriteAllText($p, $t, $utf8NoBom)`.
- TypeScript: Enable `strict: true`, `noImplicitAny: true`; never use `as any` casting.
- Python: Mandate Python 3.10+ type annotations (`int | None`); prohibit bare `except:`. Use `with open(...) as f:` context managers.
- Rust: Handle `Result` and `Option` via pattern matching; prohibit unconditional `.unwrap()`.

### 3.3 Code Smell Taxonomy
- Sleep-Polling: Using `Start-Sleep` instead of event-driven async callbacks.
- God-Function: Functions exceeding 75 lines or cyclomatic complexity $> 10$.
- Magic Constants: Hardcoded numbers/strings without named constants.
- Leaky Handles: Streams opened without enclosing `finally` disposal.
- Synthetic Mock Leak: Test dummy return values remaining in production paths.

## 4. Continuous Git Hygiene & Sandbox Safety

1. Semantic Commits: `feat(...)`, `fix(...)`, `refactor(...)`, `test(...)`, `docs(...)`.
2. Pre-Flight Backups: Before destructive refactoring, create snapshot:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sandbox_sync.ps1 -Action preflight-snapshot
```
3. Prune Scratch Clutter: Remove ephemeral debug files before committing.
4. Rollback Guarantee: Verify state can be restored immediately from `.state/backups/`.

## 5. Dynamic Zero-Stub Scanner

Language regexes inspect physical disk files for forbidden tokens:
- `(?i)^\s*pass\s*$`
- `throw\s+new\s+NotImplementedException`
- `raise\s+NotImplementedError`
Detection halts production delivery and flags the responsible sub-agent.

## 6. Release Packaging & Manifest Verification

- `plugin.json`: Validated against schema; SemVer versioning (`MAJOR.MINOR.PATCH`).
- `hooks.json`: Verifies registered hooks point to valid script files on disk.
- `rules/*.md`: Valid YAML frontmatter (`trigger: always_on`), rule calibration within [3,800, 5,800] bytes (target 4,200 to 5,400 bytes, <= 1,500 tokens), total rules <= 14.

## 7. Layer 7 to Layer 8 Cognitive Handshake Contract

Checklist:
- [ ] Zero stubs, zero placeholder markers, zero `pass` statements, zero ellipses (`...`).
- [ ] SOLID principles and defensive boundary types verified.
- [ ] All file handles wrapped in deterministic disposal blocks.
- [ ] Automated tests executed on physical disk with exit code 0.
- [ ] Git commit authored with semantic formatting.
- [ ] Pre-flight snapshot created in `.state/backups/`.
