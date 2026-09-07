param(
    [string]$Action = "get-context",
    [string]$Initiator = "System",
    [string]$EventType = "GENERAL",
    [string]$Description = "",
    [string]$DeptId = "",
    [string]$DeptStatus = "",
    [string]$SessionId = "",
    [string]$Actor = "",
    [string]$BlockerId = "",
    [string]$Hypothesis = "",
    [string]$Confidence = "UNVERIFIED",
    [string]$ConversationId = ""
)

$rootDir = Split-Path -Parent $PSScriptRoot
$stateDir = Join-Path $rootDir ".state"
$ledgerDir = Join-Path $stateDir "ledger"
$statusFile = Join-Path $stateDir "status.json"
$healthFile = Join-Path $stateDir "corporate_health.json"
$sessionFile = Join-Path $stateDir "session_state.json"

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
        $utf8NoBom = New-Object System.Text.UTF8Encoding $false
        [System.IO.File]::WriteAllText($entryPath, ($entry | ConvertTo-Json -Depth 5), $utf8NoBom)
        Write-Host "[LEDGER COMMIT] $txId recorded: $Description"
    }

    "init-session" {
        $sessId = if ($SessionId) { $SessionId } else { "SES-$((Get-Date).ToString('yyyyMMdd-HHmmss'))-$([System.Guid]::NewGuid().ToString('N').Substring(0,4))" }
        $act = if ($Actor) { $Actor } else { if ($Initiator -ne "System") { $Initiator } else { "Dr. Alexander Vance (CEO)" } }
        $isWorker = ($act -match "(?i)(Specialist|Worker|EMP|PROD|RED|DEV|ENG)")
        $roleTier = if ($isWorker) { "L1_SPECIALIST" } else { "L6_CEO" }
        $now = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
        
        $initialBlockers = @()
        if ($BlockerId) {
            $initialBlockers += @{
                id = $BlockerId
                description = if ($Description) { $Description } else { "Mandatory verification required" }
                status = "OPEN"
                created_at = $now
            }
        }

        # Check existing session state to preserve root_session if a worker is initializing
        $sess = $null
        if (Test-Path $sessionFile) {
            try { $sess = Get-Content $sessionFile -Raw | ConvertFrom-Json } catch { Write-Verbose "[SESSION RECOVERY] Unable to parse session state: $($_.Exception.Message)" }
        }

        if (-not $sess -or -not $isWorker) {
            # Initializing root session or replacing root session
            $rootConvId = if ($ConversationId) { $ConversationId } elseif ($sess -and $sess.root_session -and $sess.root_session.root_conversation_id) { $sess.root_session.root_conversation_id } else { "" }
            $existingSubagents = if ($sess -and $sess.subagents) { $sess.subagents } else { @{} }
            
            $sess = @{
                "`$schema" = "https://json-schema.org/draft/2020-12/schema"
                root_session = @{
                    session_id = $sessId
                    root_conversation_id = $rootConvId
                    actor_role = if ($isWorker) { "LEVEL_1_SPECIALIST" } else { "ACTOR_PRIMARY_CEO" }
                    actor = $act
                    active_mandate = if ($Description) { $Description } else { "Executive Cognitive Governance & Epistemic Audit" }
                    active_blockers = $initialBlockers
                    cognitive_scratchpad = @{
                        hypotheses = @()
                        premises = @()
                    }
                    created_at = $now
                    last_updated = $now
                }
                subagents = $existingSubagents
                # Top-level mirrors for backward compatibility
                session_id = $sessId
                actor = $act
                role_tier = $roleTier
                active_mandate = if ($Description) { $Description } else { "Operational session execution" }
                active_blockers = $initialBlockers
                hypotheses = @()
                created_at = $now
                last_updated = $now
            }
        } else {
            # Existing root session preserved; register subagent
            $subKey = if ($ConversationId) { $ConversationId } else { $sessId }
            if (-not $sess.subagents) { $sess | Add-Member -MemberType NoteProperty -Name "subagents" -Value @{} -Force }
            $subData = @{
                subagent_id = $sessId
                actor = $act
                role_tier = "L1_SPECIALIST"
                mandate = if ($Description) { $Description } else { "Subagent execution" }
                active_blockers = $initialBlockers
                registered_at = $now
            }
            $sess.subagents | Add-Member -MemberType NoteProperty -Name $subKey -Value $subData -Force
            $sess.last_updated = $now
        }

        $utf8NoBom = New-Object System.Text.UTF8Encoding $false
        $temp = "$sessionFile.tmp.$([System.Guid]::NewGuid().ToString('N'))"
        [System.IO.File]::WriteAllText($temp, ($sess | ConvertTo-Json -Depth 10), $utf8NoBom)
        Move-Item -Path $temp -Destination $sessionFile -Force

        & powershell -ExecutionPolicy Bypass -File $PSCommandPath -Action log-event -Initiator $act -EventType "SESSION_INITIALIZED" -Description "Initialized session $sessId for actor $act [$roleTier]." | Out-Null
        Write-Host "[SESSION INIT] Session $sessId initialized for $act [$roleTier]."
    }

    "set-blocker" {
        $bId = if ($BlockerId) { $BlockerId } elseif ($Description) { $Description } else { "BLK-GENERAL" }
        if (-not (Test-Path $sessionFile)) {
            & powershell -ExecutionPolicy Bypass -File $PSCommandPath -Action init-session -Initiator $Initiator -BlockerId $bId -Description $Description | Out-Null
            return
        }

        $sess = Get-Content $sessionFile -Raw | ConvertFrom-Json
        $existing = @()
        if ($sess.root_session -and $sess.root_session.active_blockers) {
            $existing = @($sess.root_session.active_blockers)
        } elseif ($sess.active_blockers) {
            $existing = @($sess.active_blockers)
        }

        $alreadyExists = $false
        foreach ($b in $existing) {
            $matched = ($b -is [string] -and $b -eq $bId) -or ($b.id -and $b.id -eq $bId)
            $isOpen = if ($b.status) { "$($b.status)".ToUpper() -in @("OPEN", "ACTIVE") } else { $true }
            if ($matched -and $isOpen) { $alreadyExists = $true; break }
        }

        if (-not $alreadyExists) {
            $newBlocker = @{
                id = $bId
                type = $BlockerType
                description = if ($Description) { $Description } else { "Active blocking condition" }
                status = "OPEN"
                created_at = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
            }
            $updatedList = @($existing + $newBlocker)
            if ($sess.root_session) {
                $sess.root_session.active_blockers = $updatedList
                $sess.root_session.last_updated = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
            }
            $sess.active_blockers = $updatedList
            $sess.last_updated = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")

            $utf8NoBom = New-Object System.Text.UTF8Encoding $false
            $temp = "$sessionFile.tmp.$([System.Guid]::NewGuid().ToString('N'))"
            [System.IO.File]::WriteAllText($temp, ($sess | ConvertTo-Json -Depth 10), $utf8NoBom)
            Move-Item -Path $temp -Destination $sessionFile -Force

            & powershell -ExecutionPolicy Bypass -File $PSCommandPath -Action log-event -Initiator $Initiator -EventType "SESSION_BLOCKER_SET" -Description "Registered session blocker: $bId." | Out-Null
            Write-Host "[SESSION BLOCKER SET] Blocker '$bId' registered."
        } else {
            Write-Host "[SESSION BLOCKER EXISTS] Blocker '$bId' is already active."
        }
    }

    "resolve-blocker" {
        $bId = if ($BlockerId) { $BlockerId } elseif ($Description) { $Description } else { "BLK-PREMISE-AUDIT" }
        if (Test-Path $sessionFile) {
            $sess = Get-Content $sessionFile -Raw | ConvertFrom-Json
            
            # Helper to filter blockers
            $filterBlockers = {
                param($list)
                $rem = @()
                if ($list) {
                    foreach ($b in $list) {
                        $match = ($b -is [string] -and $b -eq $bId) -or ($b.id -and $b.id -eq $bId)
                        if (-not $match) {
                            $rem += $b
                        }
                    }
                }
                return $rem
            }

            if ($sess.root_session -and $sess.root_session.active_blockers) {
                $sess.root_session.active_blockers = & $filterBlockers $sess.root_session.active_blockers
                $sess.root_session.last_updated = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
            }
            if ($sess.active_blockers) {
                $sess.active_blockers = & $filterBlockers $sess.active_blockers
            }
            $sess.last_updated = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")

            $utf8NoBom = New-Object System.Text.UTF8Encoding $false
            $temp = "$sessionFile.tmp.$([System.Guid]::NewGuid().ToString('N'))"
            [System.IO.File]::WriteAllText($temp, ($sess | ConvertTo-Json -Depth 10), $utf8NoBom)
            Move-Item -Path $temp -Destination $sessionFile -Force

            & powershell -ExecutionPolicy Bypass -File $PSCommandPath -Action log-event -Initiator $Initiator -EventType "SESSION_BLOCKER_RESOLVED" -Description "Resolved session blocker: $bId." | Out-Null
            Write-Host "[SESSION BLOCKER RESOLVED] Blocker '$bId' cleared from session state."
        } else {
            Write-Host "[SESSION BLOCKER RESOLVE] No session_state.json found on disk."
        }

        if (Test-Path $healthFile) {
            try {
                $health = Get-Content $healthFile -Raw | ConvertFrom-Json
                $hRemaining = @()
                if ($health.active_blockers) {
                    foreach ($b in $health.active_blockers) {
                        if ("$b".Trim() -ne $bId) { $hRemaining += $b }
                    }
                    $health.active_blockers = $hRemaining
                    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
                    [System.IO.File]::WriteAllText($healthFile, ($health | ConvertTo-Json -Depth 10), $utf8NoBom)
                }
            } catch {
                Write-Warning "[HEALTH SYNC ERROR] Failed to update corporate health blockers: $($_.Exception.Message)"
            }
        }
    }

    "record-hypothesis" {
        $hypText = if ($Hypothesis) { $Hypothesis } elseif ($Description) { $Description } else { "Unspecified hypothesis" }
        $statusVal = if ($Confidence) { $Confidence } else { "UNVERIFIED_HYPOTHESIS" }
        if (-not (Test-Path $sessionFile)) {
            & powershell -ExecutionPolicy Bypass -File $PSCommandPath -Action init-session -Initiator $Initiator | Out-Null
        }

        $sess = Get-Content $sessionFile -Raw | ConvertFrom-Json
        $hypList = @()
        if ($sess.root_session -and $sess.root_session.cognitive_scratchpad -and $sess.root_session.cognitive_scratchpad.hypotheses) {
            $hypList = @($sess.root_session.cognitive_scratchpad.hypotheses)
        } elseif ($sess.hypotheses) {
            $hypList = @($sess.hypotheses)
        }

        $nextIdx = "{0:D3}" -f ($hypList.Count + 1)
        $entry = @{
            id = "HYP-$nextIdx"
            statement = $hypText
            status = $statusVal
            timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
            verified_by = $Initiator
        }
        $updatedHyp = @($hypList + $entry)
        if ($sess.root_session) {
            if (-not $sess.root_session.cognitive_scratchpad) {
                $sess.root_session | Add-Member -MemberType NoteProperty -Name "cognitive_scratchpad" -Value @{ hypotheses = @(); premises = @() } -Force
            }
            $sess.root_session.cognitive_scratchpad.hypotheses = $updatedHyp
            $sess.root_session.last_updated = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
        }
        $sess.hypotheses = $updatedHyp
        $sess.last_updated = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")

        $utf8NoBom = New-Object System.Text.UTF8Encoding $false
        $temp = "$sessionFile.tmp.$([System.Guid]::NewGuid().ToString('N'))"
        [System.IO.File]::WriteAllText($temp, ($sess | ConvertTo-Json -Depth 10), $utf8NoBom)
        Move-Item -Path $temp -Destination $sessionFile -Force

        & powershell -ExecutionPolicy Bypass -File $PSCommandPath -Action log-event -Initiator $Initiator -EventType "HYPOTHESIS_RECORDED" -Description "Recorded hypothesis HYP-$nextIdx [$statusVal]: $hypText" | Out-Null
        Write-Host "[HYPOTHESIS RECORDED] HYP-$nextIdx [$statusVal]: $hypText"
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
            $utf8NoBom = New-Object System.Text.UTF8Encoding $false
            [System.IO.File]::WriteAllText($statusFile, ($status | ConvertTo-Json -Depth 10), $utf8NoBom)
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

        if (Test-Path $sessionFile) {
            $sess = Get-Content $sessionFile -Raw | ConvertFrom-Json
            $out += "`n### Active Session State Continuum`n"
            $out += "- **Session ID**: $($sess.session_id) | **Actor**: $($sess.actor) ($($sess.role_tier))`n"
            $bCount = if ($sess.active_blockers) { @($sess.active_blockers).Count } else { 0 }
            $out += "- **Active Blockers**: $bCount`n"
            if ($bCount -gt 0) {
                foreach ($b in $sess.active_blockers) {
                    $bId = if ($b.id) { $b.id } else { "$b" }
                    $bDesc = if ($b.description) { " - $($b.description)" } else { "" }
                    $out += "  - [$bId]$bDesc`n"
                }
            }
            $hCount = if ($sess.hypotheses) { @($sess.hypotheses).Count } else { 0 }
            if ($hCount -gt 0) {
                $out += "- **Recorded Hypotheses ($hCount)**:`n"
                foreach ($hyp in $sess.hypotheses) {
                    $out += "  - $($hyp.id) [$($hyp.status)]: $($hyp.statement)`n"
                }
            }
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
