# Stop Gate Hook: Evaluates corporate state and active blockers before allowing agent termination
$rawInput = if ([Console]::IsInputRedirected) { [Console]::In.ReadToEnd() } else { "" }

$rootDir = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$healthPath = Join-Path $rootDir ".state\corporate_health.json"
$allowStop = $true
$rejectionReason = ""

if (Test-Path $healthPath) {
    try {
        $health = Get-Content $healthPath -Raw | ConvertFrom-Json
        $blockers = @($health.active_blockers)
        if ($blockers.Count -gt 0) {
            $allowStop = $false
            $blockerDetails = $blockers -join "; "
            $rejectionReason = "[STOP GATE REJECTION] Critical corporate blockers remain unresolved in .state/corporate_health.json: [$blockerDetails]. Re-enter loop to resolve."
        }
    } catch {
        # If unparseable, do not deadlock
        $allowStop = $true
    }
}

if ($allowStop) {
    $response = @{
        decision = "allow"
    }
} else {
    $response = @{
        decision = "continue"
        reason = $rejectionReason
    }
}

$response | ConvertTo-Json -Depth 5 -Compress
