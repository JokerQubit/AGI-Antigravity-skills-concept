param(
    [string]$Action = "get-context",
    [string]$Initiator = "System",
    [string]$EventType = "GENERAL",
    [string]$Description = "",
    [string]$DeptId = "",
    [string]$DeptStatus = ""
)

$rootDir = Split-Path -Parent $PSScriptRoot
$stateDir = Join-Path $rootDir ".state"
$ledgerDir = Join-Path $stateDir "ledger"
$statusFile = Join-Path $stateDir "status.json"
$healthFile = Join-Path $stateDir "corporate_health.json"

if (!(Test-Path $ledgerDir)) { New-Item -ItemType Directory -Path $ledgerDir -Force | Out-Null }

switch ($Action.ToLower()) {
    "log-event" {
        $existing = Get-ChildItem -Path $ledgerDir -Filter "*.json" | Measure-Object
        $nextIdx = "{0:D4}" -f $existing.Count
        $timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
        $txId = "TX-$nextIdx-$EventType"
        
        $entry = @{
            transaction_id = $txId
            timestamp = $timestamp
            initiator = $Initiator
            event_type = $EventType
            description = $Description
            verification_status = "RECORDED"
        }
        
        $entryPath = Join-Path $ledgerDir "$nextIdx`_$EventType.json"
        $entry | ConvertTo-Json -Depth 5 | Set-Content -Path $entryPath -Encoding UTF8
        Write-Host "[LEDGER COMMIT] $txId recorded: $Description"
    }

    "update-dept" {
        if (Test-Path $statusFile) {
            $status = Get-Content $statusFile -Raw | ConvertFrom-Json
            foreach ($d in $status.active_departments) {
                if ($d.department_id -eq $DeptId) {
                    $d.status = $DeptStatus
                    if ($Description) { $d.current_mandate = $Description }
                }
            }
            $status.last_updated = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
            $status | ConvertTo-Json -Depth 10 | Set-Content -Path $statusFile -Encoding UTF8
            Write-Host "[STATUS UPDATE] Department $DeptId status set to $DeptStatus"
        }
    }

    "get-context" {
        $out = "# Real-Time Corporate Context & Memory Ledger`n"
        if (Test-Path $statusFile) {
            $s = Get-Content $statusFile -Raw | ConvertFrom-Json
            $out += "**Global Phase**: $($s.global_phase) | **Active Sprint**: $($s.active_sprint.name)`n`n"
            $out += "### Active Department Roster`n"
            foreach ($d in $s.active_departments) {
                $out += "- **$($d.department_id)** ($($d.head_id)): [$($d.status)] $($d.current_mandate)`n"
            }
        }
        
        if (Test-Path $healthFile) {
            $h = Get-Content $healthFile -Raw | ConvertFrom-Json
            $out += "`n### Corporate Health & Metrics`n"
            $out += "- **Burn Status**: $($h.financials.burn_rate_status) | **Fiduciary Risk**: $($h.financials.fiduciary_risk_tier)`n"
            $out += "- **Survival Telemetry**: Epistemic Defect Rate: $($h.survival_metrics_telemetry.epistemic_defect_rate) | Adversarial Pass Rate: $($h.survival_metrics_telemetry.adversarial_pass_rate)`n"
        }

        $out += "`n### Recent Operational Transactions (Ledger)`n"
        $recent = Get-ChildItem -Path $ledgerDir -Filter "*.json" | Sort-Object Name -Descending | Select-Object -First 5
        foreach ($f in $recent) {
            $e = Get-Content $f.FullName -Raw | ConvertFrom-Json
            $out += "- `[$($e.timestamp)`] **$($e.initiator)** [$($e.event_type)]: $($e.description)`n"
        }

        Write-Output $out
    }

    default {
        Write-Error "Unknown action: $Action"
    }
}
