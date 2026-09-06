# Stop Gate Hook: Evaluates corporate state and active blockers before allowing agent termination
$rawInput = if ([Console]::IsInputRedirected) { [Console]::In.ReadToEnd() } else { "" }

$pluginDir = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$inputObj = $null
if ($rawInput) {
    try { $inputObj = $rawInput | ConvertFrom-Json } catch { }
}
$workspaceDir = if ($inputObj -and $inputObj.workspacePaths -and $inputObj.workspacePaths.Count -gt 0) { $inputObj.workspacePaths[0] } else { $pluginDir }

$healthPath = Join-Path $workspaceDir ".state\corporate_health.json"
if (-not (Test-Path $healthPath) -and (Test-Path (Join-Path $pluginDir ".state\corporate_health.json"))) {
    $healthPath = Join-Path $pluginDir ".state\corporate_health.json"
}
$allowStop = $true
$rejectionReason = ""

if (Test-Path $healthPath) {
    try {
        $health = Get-Content $healthPath -Raw | ConvertFrom-Json
        $rawBlockers = @()
        if ($health.active_blockers) { $rawBlockers += $health.active_blockers }
        if ($health.critical_blockers) { $rawBlockers += $health.critical_blockers }
        $blockers = @($rawBlockers | Where-Object { $null -ne $_ -and "$_".Trim() -ne "" })
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
