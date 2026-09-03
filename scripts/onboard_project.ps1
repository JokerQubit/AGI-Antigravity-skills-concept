param(
    [Parameter(Mandatory=$true)]
    [string]$ProjectPath,

    [string]$ProjectName = ""
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
        active_departments = @("dept_research", "dept_architecture", "dept_quality_redteam", "dept_production")
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

# 5. Execute Deep Neural Knowledge Mapping
Write-Host "`n[PHASE 2] Executing Deep Neural Codebase Scan..." -ForegroundColor Cyan
& powershell -ExecutionPolicy Bypass -File $mapScript -TargetDirectory $targetDir

Write-Host "`n[PHASE 3] Operational Context Briefing Sealed!" -ForegroundColor Green
Write-Host "  -> Neural Map:     $stateDir\neural_map.json" -ForegroundColor White
Write-Host "  -> Live Context:   $stateDir\project_context.md" -ForegroundColor White
Write-Host "  -> State Ledger:   $ledgerDir" -ForegroundColor White
Write-Host "`n[SUCCESS] Project '$resolvedName' is fully onboarded under the Executive Governance standard." -ForegroundColor Green
