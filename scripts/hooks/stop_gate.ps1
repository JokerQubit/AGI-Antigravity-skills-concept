# Stop Gate Hook: Evaluates corporate state, session blockers, and circuit breaker before allowing agent termination
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

$sessionPath = Join-Path $workspaceDir ".state\session_state.json"
if (-not (Test-Path $sessionPath) -and (Test-Path (Join-Path $pluginDir ".state\session_state.json"))) {
    $sessionPath = Join-Path $pluginDir ".state\session_state.json"
}

$executionNum = 0
if ($inputObj -and $null -ne $inputObj.executionNum) {
    $executionNum = [int]$inputObj.executionNum
}

# Determine if the stopping process is a subagent
$isSubAgent = $false
$currentConvId = if ($inputObj -and $inputObj.conversationId) { $inputObj.conversationId } else { "" }

if ($inputObj -and $inputObj.transcriptPath -and (Test-Path $inputObj.transcriptPath)) {
    try {
        $headLines = Get-Content $inputObj.transcriptPath -TotalCount 10
        foreach ($hl in $headLines) {
            try {
                $ho = $hl | ConvertFrom-Json
                if ($ho.type -eq 'USER_INPUT' -and $ho.content) {
                    if ($ho.content.IndexOf("<original_task>", [System.StringComparison]::OrdinalIgnoreCase) -ge 0 -or
                        $ho.content.IndexOf("subagent_reminder", [System.StringComparison]::OrdinalIgnoreCase) -ge 0 -or
                        $ho.content.IndexOf("You are running as a subagent", [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
                        $isSubAgent = $true
                        break
                    }
                }
            } catch { }
        }
    } catch { }
}

if (Test-Path $sessionPath) {
    try {
        $sessData = Get-Content $sessionPath -Raw | ConvertFrom-Json
        if ($currentConvId -and $sessData.root_session -and $sessData.root_session.root_conversation_id) {
            if ($currentConvId -ne $sessData.root_session.root_conversation_id) {
                $isSubAgent = $true
            }
        }
    } catch { }
}

$allowStop = $true
$rejectionReason = ""
$circuitBreakerTripped = $false

# Safety circuit breaker: If execution reaches 4 or more rejections/attempts, allow stop to prevent deadlock
if ($executionNum -ge 4) {
    $allowStop = $true
    $circuitBreakerTripped = $true
} else {
    # 1. Enforce session blockers from session_state.json
    if (Test-Path $sessionPath) {
        try {
            $sess = Get-Content $sessionPath -Raw | ConvertFrom-Json
            $activeBlockers = @()
            $rawList = @()

            if ($isSubAgent) {
                # Subagents check their specific blockers (if any registered under subagents)
                if ($currentConvId -and $sess.subagents -and $sess.subagents.$currentConvId -and $sess.subagents.$currentConvId.active_blockers) {
                    $rawList = @($sess.subagents.$currentConvId.active_blockers)
                }
            } else {
                # Root CEO session: check root_session.active_blockers or flat active_blockers
                if ($sess.root_session -and $sess.root_session.active_blockers) {
                    $rawList = @($sess.root_session.active_blockers)
                } elseif ($sess.active_blockers) {
                    $rawList = @($sess.active_blockers)
                }
            }

            foreach ($b in $rawList) {
                if ($b -is [string] -and "$b".Trim() -ne "") {
                    $activeBlockers += "$b".Trim()
                } elseif ($b.id -and "$($b.id)".Trim() -ne "") {
                    $st = if ($b.status) { "$($b.status)".ToUpper() } else { "OPEN" }
                    if ($st -in @("OPEN", "ACTIVE")) {
                        $activeBlockers += "$($b.id)".Trim()
                    }
                }
            }

            if ($activeBlockers.Count -gt 0) {
                $allowStop = $false
                $bDetails = $activeBlockers -join "; "
                $rejectionReason = "[STOP GATE REJECTION] Active session blockers unresolved in .state/session_state.json: [$bDetails]. Conduct Premise Audit / Socratic Inquest, verify premises on disk, and resolve blocker via 'scripts/sync_state.ps1 -Action resolve-blocker -BlockerId <ID>' before concluding turn (Circuit breaker: attempt $executionNum/4)."
            }
        } catch { }
    }

    # 2. Enforce corporate health blockers if session blockers didn't already reject (for root session)
    if ($allowStop -and (-not $isSubAgent) -and (Test-Path $healthPath)) {
        try {
            $health = Get-Content $healthPath -Raw | ConvertFrom-Json
            $rawBlockers = @()
            if ($health.active_blockers) { $rawBlockers += $health.active_blockers }
            if ($health.critical_blockers) { $rawBlockers += $health.critical_blockers }
            $blockers = @($rawBlockers | Where-Object { $null -ne $_ -and "$_".Trim() -ne "" })
            if ($blockers.Count -gt 0) {
                $allowStop = $false
                $blockerDetails = $blockers -join "; "
                $rejectionReason = "[STOP GATE REJECTION] Critical corporate blockers remain unresolved in .state/corporate_health.json: [$blockerDetails]. Re-enter loop to resolve (Circuit breaker: attempt $executionNum/4)."
            }
        } catch {
            $allowStop = $true
        }
    }
}

if ($allowStop) {
    if ($circuitBreakerTripped) {
        $response = @{
            decision = "allow"
            userFacingMessage = "[STRATEGIC PAUSE: COGNITIVE CIRCUIT BREAKER ACTIVATED] Blockers remained unresolved after 4 consecutive stop cycles. Pausing for executive intervention."
        }
    } else {
        $response = @{
            decision = "allow"
        }
    }
} else {
    $response = @{
        decision = "continue"
        reason = $rejectionReason
    }
}

$response | ConvertTo-Json -Depth 5 -Compress
