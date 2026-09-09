param(
    [Parameter(Mandatory=$true)]
    [string]$ProjectPath,

    [string]$ProjectName = "",

    [switch]$StructureCompany = $true
)

$targetDir = (Resolve-Path $ProjectPath).Path
if (!(Test-Path $targetDir)) {
    Write-Error "Target project directory does not exist: $ProjectPath"
    exit 1
}

$resolvedName = if ($ProjectName) { $ProjectName } else { Split-Path $targetDir -Leaf }
$stateDir = Join-Path $targetDir ".state"
$ledgerDir = Join-Path $stateDir "ledger"
$backupsDir = Join-Path $stateDir "backups"
$agentsDir = Join-Path $targetDir ".agents"
$sectorsDir = Join-Path $agentsDir "sectors"
$employeesDir = Join-Path $agentsDir "employees"
$contractsDir = Join-Path $agentsDir "contracts"
$mapScript = Join-Path $PSScriptRoot "update_neural_map.ps1"

Write-Host "================================================================="
Write-Host "       OMNICOGNITION EXECUTIVE PROJECT ONBOARDING ENGINE"
Write-Host "================================================================="
Write-Host "Target Workspace: $targetDir"
Write-Host "Project Name:     $resolvedName`n"

# 1. Provision .state directory continuum
Write-Host "[PHASE 1] Initializing Persistent State Continuum (.state/)..." -ForegroundColor Cyan
New-Item -ItemType Directory -Path $ledgerDir -Force | Out-Null
New-Item -ItemType Directory -Path $backupsDir -Force | Out-Null

# 2. Initialize status.json
$statusFile = Join-Path $stateDir "status.json"
if (!(Test-Path $statusFile)) {
    $statusData = @{
        global_phase = "active_operations"
        project_name = $resolvedName
        initialized_at = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
        active_departments = @("01_governance", "02_technology", "03_operations", "06_finance_risk")
        current_sprint = "Executive Neural Onboarding & System Mapping"
        active_mandates = @("Maintain zero-stub implementation", "Continuously update neural map across sessions")
    }
    $statusData | ConvertTo-Json -Depth 5 | Set-Content -Path $statusFile -Encoding UTF8
    Write-Host "  [INITIALIZED] $statusFile" -ForegroundColor Green
}

# 3. Initialize corporate_health.json
$healthFile = Join-Path $stateDir "corporate_health.json"
if (!(Test-Path $healthFile)) {
    $healthData = @{
        project_name = $resolvedName
        burn_rate_tier = "optimal"
        fiduciary_risk_level = "minimal"
        tokens_consumed_estimated = 0
        critical_blockers = @()
        last_financial_audit = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
    }
    $healthData | ConvertTo-Json -Depth 5 | Set-Content -Path $healthFile -Encoding UTF8
    Write-Host "  [INITIALIZED] $healthFile" -ForegroundColor Green
}

# 4. Initialize Genesis Transaction in local ledger
$genesisFile = Join-Path $ledgerDir "0000_genesis.json"
if (!(Test-Path $genesisFile)) {
    $genesisData = @{
        transaction_id = "TX-0000-GENESIS"
        project_name = $resolvedName
        timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
        initiator = "OmniCognition Project Onboarding Engine"
        event_type = "PROJECT_NEURAL_ONBOARDING_GENESIS"
        description = "Initialized persistent executive state continuum and neural knowledge map for $resolvedName."
    }
    $genesisData | ConvertTo-Json -Depth 5 | Set-Content -Path $genesisFile -Encoding UTF8
    Write-Host "  [INITIALIZED] $genesisFile" -ForegroundColor Green
}

# 5. Materialize Physical Corporate Structure & Context Rules (.agents/rules/)
if ($StructureCompany) {
    Write-Host "`n[PHASE 2] Materializing Physical Corporate Enterprise Structure (.agents/rules/)..." -ForegroundColor Cyan
    $rulesDir = Join-Path $agentsDir "rules"
    New-Item -ItemType Directory -Path $rulesDir -Force | Out-Null

    # 5.1 Foundational Project Constitution (.agents/rules/00_project_constitution.md)
    $constitutionFile = Join-Path $rulesDir "00_project_constitution.md"
    if (!(Test-Path $constitutionFile)) {
        $constitutionContent = @"
---
trigger: always_on
description: Sovereign Project Constitution and Dual-CEO Governance for $resolvedName
---
# Foundational Constitution: $resolvedName

**Organization**: $resolvedName Sovereign Enterprise  
**Governance Topology**: Dual-CEO Executive Council & Specialized Niche Chains  
**Status**: Materialized Dynamic Enterprise Architecture  
**Document Revision**: 1.0.0  
**Classification**: High-Capital Executive Invariant  

---

## 1. Executive Governance & Dual-CEO Topology
1. **Strategic Founder / User**: Capital ownership, macro strategic directives, ultimate override veto.
2. **AI Sovereign CEO**: 24/7 autonomous cybernetic execution, algorithmic precision, epistemic red teaming.

## 2. Dynamic Niche Context Law
- **Zero Static Boilerplate**: The AI must dynamically author project methodology, target profiles, interaction protocols, and diagnostic playbooks directly into `.agents/rules/<index>_<niche>.md` tailored 100% to this project's specific domain (e.g. career engineering, ATS optimization, e-commerce, AI tooling).
- **Context Ingestion Invariant**: Never store core project methodology as inert docs in `docs/`. All operational intelligence must live in `.agents/rules/*.md` so it enters active AI context across sessions.
- **Zero-Stub Law**: Every declared rule, script, or component must contain complete operational logic on physical disk.
"@
        $constitutionContent | Set-Content -Path $constitutionFile -Encoding UTF8
        Write-Host "  [MATERIALIZED] Project Constitution: $constitutionFile" -ForegroundColor Green
    }

    # 5.2 Project Root AGENTS.md - Master Context Index
    $rootAgentsFile = Join-Path $targetDir "AGENTS.md"
    if (!(Test-Path $rootAgentsFile)) {
        $rootAgentsContent = @"
---
trigger: always_on
description: Master Governance Kernel and Dynamic Rules Index for $resolvedName
---
# $resolvedName: Executive Governance Kernel & Rules Index

This project operates under executive cybernetic governance and domain-tailored dynamic rules.

## 1. Project Context Rules (.agents/rules/)
- [.agents/rules/00_project_constitution.md](file:///.agents/rules/00_project_constitution.md): Foundational Constitution & Dual-CEO Topology.
- Domain rules (from `01_...` to `12_...`) are synthesized dynamically by the AI to match this project's specific niche.

## 2. Operational Invariants
- **Zero-Stub Standard**: 100% operational logic on disk. Stubs (`pass`, `return null`, `{}`) and ellipses (`...`) trigger rejection.
- **Context Ingestion**: Core methodology, playbooks, and profiles must reside in `.agents/rules/*.md`, never in inert `docs/`.
"@
        $rootAgentsContent | Set-Content -Path $rootAgentsFile -Encoding UTF8
        Write-Host "  [MATERIALIZED] Root AGENTS.md: $rootAgentsFile" -ForegroundColor Green
    }
}

# 6. Execute Deep Neural Knowledge Mapping
Write-Host "`n[PHASE 3] Executing Deep Neural Codebase Scan..." -ForegroundColor Cyan
& powershell -ExecutionPolicy Bypass -File $mapScript -TargetDirectory $targetDir

Write-Host "`n[PHASE 4] Operational Context Briefing Sealed!" -ForegroundColor Green
Write-Host "  -> Corporate Topology: $agentsDir" -ForegroundColor White
Write-Host "  -> Neural Map:         $stateDir\neural_map.json" -ForegroundColor White
Write-Host "  -> Live Context:       $stateDir\project_context.md" -ForegroundColor White
Write-Host "  -> State Ledger:       $ledgerDir" -ForegroundColor White
Write-Host "`n[SUCCESS] Project '$resolvedName' is physically structured and onboarded under Executive Governance." -ForegroundColor Green
