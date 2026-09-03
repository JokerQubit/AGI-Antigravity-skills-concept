# Pre-Invocation Hook: Injects real-time corporate health, active blockers, and executive telemetry
$rawInput = [Console]::In.ReadToEnd()

$healthPath = Join-Path $PSScriptRoot "..\..\.state\corporate_health.json"
$statusPath = Join-Path $PSScriptRoot "..\..\.state\status.json"

$telemetryMessage = "[EXECUTIVE TELEMETRY INJECTION]"

if (Test-Path $healthPath) {
    try {
        $health = Get-Content $healthPath -Raw | ConvertFrom-Json
        $burn = $health.financials.burn_rate_status
        $risk = $health.financials.fiduciary_risk_tier
        $telemetryMessage += "`nCorporate Health: Burn Rate Tier [$burn], Fiduciary Risk [$risk]."
    } catch {
        # Fallback if unparseable
    }
}

if (Test-Path $statusPath) {
    try {
        $status = Get-Content $statusPath -Raw | ConvertFrom-Json
        $phase = $status.global_phase
        $sprint = $status.active_sprint.name
        $telemetryMessage += "`nOperational Phase: [$phase], Active Sprint: [$sprint]."
    } catch {
        # Fallback
    }
}

$mapPath = Join-Path $PSScriptRoot "..\..\.state\neural_map.json"
if (Test-Path $mapPath) {
    try {
        $mapData = Get-Content $mapPath -Raw | ConvertFrom-Json
        $compCount = $mapData.total_components
        $telemetryMessage += "`nNeural Map: [$compCount] active components mapped in .state/neural_map.json & .state/project_context.md."
    } catch {
        # Fallback
    }
}

$telemetryMessage += "`nExecutive Directive: Maintain strict anti-sycophancy, mandate Premise Audits, and preserve clean-context sub-agent delegation."

$response = @{
    injectSteps = @(
        @{
            ephemeralMessage = $telemetryMessage
        }
    )
}

$response | ConvertTo-Json -Depth 5 -Compress
