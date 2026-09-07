---
trigger: always_on
description: Layer 7 Production Zero-Stub Execution, Senior Clean Code, and Sandbox Safety
---
# Layer 7: Production Zero-Stub Execution & Senior Clean Code

Physical manufacturing floor of OmniCognition Labs enforcing Zero-Stub Law, senior software craft, continuous git hygiene, and pre-flight sandbox backups.

## 1. Production Philosophy & The Zero-Stub Law
- Satisficing Pathology: Emitting skeleton code with empty bodies (`pass`, `return null`, `{}`) or placeholder markers constitutes operational failure.
- Zero-Stub Law: Declared classes, functions, handlers, and scripts must contain 100% operational production logic on physical disk.
- Zero-Ellipsis Mandate: Code truncation (`...`, `/* remaining logic unchanged */`) is strictly forbidden. Apply precise contiguous replacements.

## 2. Department of Operational Production (`dept_production`)
Staff: `VP-PROD-01` (Vice President), `PROD-101` (Code Synthesis Specialist), `PROD-102` (Build & Packaging Specialist).

Level 1 Specialist Guidelines & Idempotency:
- Clean-Context Execution: Level 1 specialists execute atomic tasks in isolated sessions to eliminate context drift.
- Disk Grounding: Inspect target files via `view_file` before writing modifications.
- Idempotent Scripting: Directory init `if (!(Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }`, deterministic overwrites via atomic swap, graceful exception handling.

## 3. Senior Software Engineering Standards
SOLID Invariants: SRP (single reason to change; decouple logic from IO), OCP (open for extension, closed for modification), LSP (subclasses honor base contracts), ISP (cohesive client interfaces), DIP (depend on abstractions).

Multi-Language Production Standards:
PowerShell: `[CmdletBinding()]`, types, `$ErrorActionPreference = 'Stop'`, write via `[IO.File]::WriteAllText($p, $t, $utf8NoBom)`. TypeScript: `strict: true`, `noImplicitAny: true`. Python: 3.10+ types (`int | None`), no bare except. Rust: Pattern match `Result`/`Option`, no `.unwrap()`.

Code Smells: Sleep-Polling (use callbacks), God-Function (>75 lines or cyclomatic >10), Magic Constants, Leaky Handles, Synthetic Mock Leak.

## 4. Continuous Git Hygiene & Sandbox Safety
1. Semantic Commits: `feat(...)`, `fix(...)`, `refactor(...)`, `test(...)`, `docs(...)`.
2. Pre-Flight Backups: Before destructive refactoring, snapshot via:
   `powershell -ExecutionPolicy Bypass -File .\scripts\sandbox_sync.ps1 -Action preflight-snapshot`
3. Prune Scratch Clutter: Remove ephemeral debug files before committing. Rollback guaranteed via `.state/backups/`.

## 5. Dynamic Zero-Stub Scanner & Packaging Verification
Regexes inspect physical files: `(?i)^\s*pass\s*$`, `throw\s+new\s+NotImplementedException`, `raise\s+NotImplementedError`. Detection halts delivery.
Packaging Verification: `plugin.json` SemVer, `hooks.json` path validity, `rules/*.md` calibration within [2800, 3900] bytes (~1000-1150 tokens), total rules <= 14.

## 6. Layer 7 to Layer 8 Handshake Contract
- [ ] Zero stubs, zero placeholder markers, zero `pass` statements, zero ellipses (`...`).
- [ ] SOLID principles and defensive boundary types verified; all handles in deterministic `finally`.
- [ ] Automated tests executed on disk with exit code 0; git commit authored with semantic formatting.
- [ ] Pre-flight snapshot created in `.state/backups/`.\n