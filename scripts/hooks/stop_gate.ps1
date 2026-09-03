# Stop Gate Hook: Evaluates corporate state and active blockers before allowing agent termination
$rawInput = [Console]::In.ReadToEnd()

$healthPath = Join-Path $PSScriptRoot "..\..\.state\corporate_health.json"
$allowStop = $true
$rejectionReason = ""

if (Test-Path $healthPath) {
    try {
        $health = Get-Content $healthPath -Raw | ConvertFrom-Json
        if ($health.active_blockers.Count -gt 0) {
            $allowStop = $false
            $rejectionReason = "[STOP GATE REJECTION] Critical corporate blockers remain unresolved in .state/corporate_health.json. Re-enter loop to resolve."
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
