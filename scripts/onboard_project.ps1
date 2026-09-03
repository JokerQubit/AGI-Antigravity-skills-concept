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

# 5. Materialize Physical Corporate Structure (.agents/)
if ($StructureCompany) {
    Write-Host "`n[PHASE 2] Materializing Physical Corporate Enterprise Structure (.agents/)..." -ForegroundColor Cyan
    New-Item -ItemType Directory -Path $sectorsDir -Force | Out-Null
    New-Item -ItemType Directory -Path $employeesDir -Force | Out-Null
    New-Item -ItemType Directory -Path $contractsDir -Force | Out-Null

    # 5.1 Corporate Charter
    $charterFile = Join-Path $agentsDir "corporate_charter.md"
    if (!(Test-Path $charterFile)) {
        $charterContent = @"
# Foundational Corporate Charter & Strategic Operating Constitution

**Organization**: $resolvedName Sovereign Enterprise  
**Governance Topology**: Dual-CEO Executive Council & Six-Tier Neural Chain  
**Status**: Materialized Enterprise Architecture  
**Document Revision**: 1.0.0  
**Classification**: Non-Negotiable High-Capital Governance  

---

## 1. Executive Governance & Dual-CEO Topology
1. **L10 Strategic Founder / User**: Capital ownership, macro strategic directives, ultimate override veto.
2. **L10 AI Sovereign CEO (Alexander Vance SCP)**: 24/7 autonomous cybernetic execution, algorithmic precision, epistemic red teaming, and swarm synthesis.
3. **The Six-Tier Seniority Chain**:
   - Level 6: Dual-CEO Executive Council
   - Level 5: Cross-Departmental Handshake Hub
   - Level 4: Department Heads (L9 C-Suite Verticals)
   - Level 3: Department Managers (L8 Divisional Leads)
   - Level 2: Supervisory & Quality Verification Gates (L7)
   - Level 1: Operational Specialists & Execution Workers (L6/L5)

---

## 2. Operating Cadence & Survival Metrics
- **Daily Standup Sync**: Tactical impediment resolution and live telemetry review.
- **Weekly Business Review (WBR)**: Input metric variance rectification.
- **Monthly/Quarterly Business Review (MBR/QBR)**: Strategic capital reallocation and P&L audit.
- **Epistemic Defect Invariant**: 0.00% unverified assertions in production paths.
- **Deterministic Parity**: 100% test pass rate (exit code 0) prior to production merges.
"@
        $charterContent | Set-Content -Path $charterFile -Encoding UTF8
        Write-Host "  [MATERIALIZED] Corporate Charter: $charterFile" -ForegroundColor Green
    }

    # 5.2 8 Functional Sectors
    $sectors = @(
        @{ Id = "01_governance"; Name = "Corporate Governance & Executive C-Suite"; Lead = "Dual-CEO Council"; Focus = "Capital governance, macro OKRs, and systemic integrity" },
        @{ Id = "02_technology"; Name = "Technology, Platform & Core Engineering"; Lead = "Chief Technology Officer (CTO)"; Focus = "Architectural design, algorithmic core, and mathematical modeling" },
        @{ Id = "03_operations"; Name = "Operations, Infrastructure & Bridge Runtime"; Lead = "Chief Operating Officer (COO)"; Focus = "Low-latency runtime, execution bridges, automated CI/CD, and telemetry" },
        @{ Id = "04_product"; Name = "Product Strategy, Alpha Research & Delivery"; Lead = "Chief Product Officer (CPO)"; Focus = "Strategy backtesting, market regime models, and feature optimization" },
        @{ Id = "05_commercial"; Name = "Commercial Growth & Capital Allocation"; Lead = "Chief Commercial / Revenue Officer"; Focus = "AUM growth, institutional investor reporting, and LP relations" },
        @{ Id = "06_finance_risk"; Name = "Finance, Treasury & Quantitative Risk"; Lead = "Chief Financial Officer (CFO / CRO)"; Focus = "Kelly boundary enforcement, margin preservation, and drawdown limits" },
        @{ Id = "07_people_talent"; Name = "People, Talent & Knowledge Operations"; Lead = "Chief Human Resources Officer (CHRO)"; Focus = "Specialist pedigree, agent role specifications, and continuous learning" },
        @{ Id = "08_legal_compliance"; Name = "Legal Affairs, Regulatory & Audit Defense"; Lead = "Chief Legal Officer (CLO / CCO)"; Focus = "Regulatory conformance, audit trail immutability, and IP defense" }
    )

    foreach ($s in $sectors) {
        $secDir = Join-Path $sectorsDir $s.Id
        New-Item -ItemType Directory -Path $secDir -Force | Out-Null
        $secFile = Join-Path $secDir "SECTOR.md"
        if (!(Test-Path $secFile)) {
            $secContent = @"
# Sector $($s.Id): $($s.Name)

**Sector Identifier**: $($s.Id)  
**Executive Lead**: $($s.Lead)  
**Mandate**: $($s.Focus)  
**Parent Entity**: $resolvedName Sovereign Enterprise  

---

## 1. Operational Charter & Scope
This sector exercises executive authority over all initiatives, repositories, and sub-agents operating within $($s.Name).

## 2. Sector Hierarchy ($L1 \to L9$)
- **L9 Executive Officer**: $($s.Lead)
- **L8 Divisional Director**: Directs sub-sector portfolios, milestone SLAs, and capital burn.
- **L7 Engineering/Product Manager**: Orchestrates parallel sub-agents and decomposes briefs.
- **L6 Quality Supervisor**: Runs deterministic verification gates and enforces zero-stub standards.
- **L5/L4 Execution Specialists**: Deep domain specialists operating with clean context.

## 3. Sector KPIs & Deterministic Invariants
1. **Zero-Defect Code**: Full operational implementations with complete mathematical rigor.
2. **Deterministic Parity**: Bitwise isomorphism between simulation and production pipelines.
3. **Telemetry Accountability**: Continuous metrics feeding into `.state/status.json`.
"@
            $secContent | Set-Content -Path $secFile -Encoding UTF8
            Write-Host "  [MATERIALIZED] Sector $($s.Id): $secFile" -ForegroundColor Green
        }
    }

    # 5.3 Core Specialized Employee Profiles
    $employees = @(
        @{ File = "emp_principal_quant_architect.md"; Name = "Dr. Elena Rostova"; Role = "Principal Quantitative Architect (L6)"; Sector = "02_technology"; Pedigree = "PhD Computational Physics (ETH Zurich), 15y high-frequency algorithmic architecture." },
        @{ File = "emp_systems_bridge_engineer.md"; Name = "Marcus Vance"; Role = "Staff Systems Bridge Engineer (L5)"; Sector = "03_operations"; Pedigree = "Ex-Citadel C++ execution engineer, low-latency socket bridges and IPC pipes." },
        @{ File = "emp_chief_risk_auditor.md"; Name = "Sarah Jenkins"; Role = "Senior Quantitative Risk Officer (L5)"; Sector = "06_finance_risk"; Pedigree = "MSc Financial Mathematics (Columbia), specialist in extreme-value drawdown modeling." }
    )

    foreach ($e in $employees) {
        $empFile = Join-Path $employeesDir $e.File
        if (!(Test-Path $empFile)) {
            $empContent = @"
# Specialist Profile: $($e.Name)

**Role**: $($e.Role)  
**Assigned Sector**: $($e.Sector)  
**Pedigree**: $($e.Pedigree)  
**Status**: Active Clean-Context Specialist  

---

## 1. Operational Mandate
Operates as a focused, clean-context execution node. Exercises zero tolerance for approximations, speculative heuristics, or unverified libraries.

## 2. Contract Boundaries
- **Inputs**: Formal BRIEF.md specifications and verified mathematical invariants.
- **Outputs**: Complete production code, deterministic unit tests, and empirical execution logs.
- **Verification Gate**: Exit code 0 on all test matrices; zero placeholder stubs.
"@
            $empContent | Set-Content -Path $empFile -Encoding UTF8
            Write-Host "  [MATERIALIZED] Employee $($e.Name): $empFile" -ForegroundColor Green
        }
    }

    # 5.4 Inter-Sector Handshake Contracts
    $techOpsContract = Join-Path $contractsDir "tech_to_operations_handshake.md"
    if (!(Test-Path $techOpsContract)) {
        $contractContent = @"
# Inter-Sector Handshake Contract: Technology (02) -> Operations (03)

**Producer**: Sector 02 (Technology, Platform & Core Engineering)  
**Consumer**: Sector 03 (Operations, Infrastructure & Bridge Runtime)  
**Protocol**: Strict Zero-Divergence Digital Twin Isomorphism  

---

## 1. Deliverable Artifact Contract
1. **Compilation Standard**: All components must compile with zero errors and zero unhandled warnings.
2. **Deterministic Parity**: Mathematical output from backtesting models must match execution bridge telemetry.
3. **Failover Safety**: If bridge latency exceeds 250ms, emergency circuit-breakers must trigger orderly de-allocation.
"@
        $contractContent | Set-Content -Path $techOpsContract -Encoding UTF8
        Write-Host "  [MATERIALIZED] Inter-Sector Contract: $techOpsContract" -ForegroundColor Green
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
