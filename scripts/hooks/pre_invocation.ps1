# Pre-Invocation Hook: Injects real-time corporate health, active blockers, and executive telemetry
$rawInput = if ([Console]::IsInputRedirected) { [Console]::In.ReadToEnd() } else { "" }

$rootDir = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$healthPath = Join-Path $rootDir ".state\corporate_health.json"
$statusPath = Join-Path $rootDir ".state\status.json"
$mapPath = Join-Path $rootDir ".state\neural_map.json"

$burn = "optimal"
$risk = "minimal"
$phase = "active_operations"
$sprint = "unassigned"
$compCount = 0

if (Test-Path $healthPath) {
    try {
        $health = Get-Content $healthPath -Raw | ConvertFrom-Json
        if ($health.financials.burn_rate_status) { $burn = $health.financials.burn_rate_status }
        if ($health.financials.fiduciary_risk_tier) { $risk = $health.financials.fiduciary_risk_tier }
    } catch { }
}

if (Test-Path $statusPath) {
    try {
        $status = Get-Content $statusPath -Raw | ConvertFrom-Json
        if ($status.global_phase) { $phase = $status.global_phase }
        if ($status.active_sprint.name) { $sprint = $status.active_sprint.name }
        elseif ($status.active_sprint.sprint_id) { $sprint = $status.active_sprint.sprint_id }
    } catch { }
}

if (Test-Path $mapPath) {
    try {
        $mapData = Get-Content $mapPath -Raw | ConvertFrom-Json
        if ($mapData.total_components) { $compCount = $mapData.total_components }
    } catch { }
}

$telemetryLines = @(
    "[EXECUTIVE TELEMETRY INJECTION]",
    "Corporate Health: Burn Rate Tier [$burn], Fiduciary Risk [$risk].",
    "Operational Phase: [$phase], Active Sprint: [$sprint].",
    "Neural Map: [$compCount] active components mapped in .state/neural_map.json & .state/project_context.md.",
    "Executive Directive: Maintain strict anti-sycophancy, mandate Premise Audits, and preserve clean-context sub-agent delegation."
)
$telemetryMessage = $telemetryLines -join "`n"

$response = @{
    injectSteps = @(
        @{
            ephemeralMessage = $telemetryMessage
        }
    )
}

$response | ConvertTo-Json -Depth 5 -Compress
