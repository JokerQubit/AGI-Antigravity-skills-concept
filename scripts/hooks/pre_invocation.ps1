# Pre-Invocation Hook: Dynamic Workspace Ingestion, Greenfield Routing, Session State Engine, and Actor Demarcation
$rawInput = if ([Console]::IsInputRedirected) { [Console]::In.ReadToEnd() } else { "" }

$pluginDir = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$inputObj = $null
if ($rawInput) {
    try { $inputObj = $rawInput | ConvertFrom-Json } catch { }
}

$workspaceDir = $pluginDir
if ($inputObj -and $inputObj.workspacePaths -and $inputObj.workspacePaths.Count -gt 0) {
    $workspaceDir = $inputObj.workspacePaths[0]
}

# Determine if the active workspace has an initialized state continuum
$stateDir = Join-Path $workspaceDir ".state"
if (-not (Test-Path $stateDir) -and (Test-Path (Join-Path $pluginDir ".state"))) {
    $stateDir = Join-Path $pluginDir ".state"
}
$isGreenfield = -not (Test-Path $stateDir)

$burn = "optimal"
$risk = "minimal"
$phase = "active_operations"
$sprint = "unassigned"
$compCount = 0
$blockerCount = 0
$blockerAlert = ""

$sessionFile = Join-Path $stateDir "session_state.json"
$healthPath = Join-Path $stateDir "corporate_health.json"
$statusPath = Join-Path $stateDir "status.json"
$mapPath = Join-Path $stateDir "neural_map.json"

if (-not $isGreenfield) {
    if (Test-Path $healthPath) {
        try {
            $health = Get-Content $healthPath -Raw | ConvertFrom-Json
            if ($health.financials.burn_rate_status) { $burn = $health.financials.burn_rate_status }
            elseif ($health.burn_rate_tier) { $burn = $health.burn_rate_tier }
            if ($health.financials.fiduciary_risk_tier) { $risk = $health.financials.fiduciary_risk_tier }
            elseif ($health.fiduciary_risk_level) { $risk = $health.fiduciary_risk_level }
            if ($health.active_blockers) {
                $blockerList = @($health.active_blockers)
                $blockerCount += $blockerList.Count
                if ($blockerList.Count -gt 0) {
                    $blockerAlert = " [HEALTH ALERT: $($blockerList -join '; ')]"
                }
            }
        } catch { }
    }

    if (Test-Path $statusPath) {
        try {
            $status = Get-Content $statusPath -Raw | ConvertFrom-Json
            if ($status.global_phase) { $phase = $status.global_phase }
            if ($status.active_sprint.name) { $sprint = $status.active_sprint.name }
            elseif ($status.current_sprint) { $sprint = $status.current_sprint }
            elseif ($status.active_sprint.sprint_id) { $sprint = $status.active_sprint.sprint_id }
        } catch { }
    }

    if (Test-Path $mapPath) {
        try {
            $mapData = Get-Content $mapPath -Raw | ConvertFrom-Json
            if ($mapData.total_components) { $compCount = $mapData.total_components }
        } catch { }
    }
}

# 1. Reverse Transcript Parser & Sub-Agent Demarcation
$lastUser = ""
$isSubAgent = $false
$subAgentIndicators = @(
    "<original_task>",
    "You are a coding worker",
    "You are running as a subagent",
    "subagent_reminder",
    "send_message to your parent",
    "A previous worker has already attempted this task",
    "<prior_attempt>"
)

if ($inputObj -and $inputObj.transcriptPath -and (Test-Path $inputObj.transcriptPath)) {
    try {
        # 1a. Inspect initial lines to determine conversation root identity (immune to long-turn truncation)
        $headLines = @(Get-Content $inputObj.transcriptPath -TotalCount 10)
        foreach ($hl in $headLines) {
            try {
                $ho = $hl | ConvertFrom-Json
                if ($ho.type -eq 'USER_INPUT' -and $ho.content) {
                    foreach ($ind in $subAgentIndicators) {
                        if ($ho.content.IndexOf($ind, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
                            $isSubAgent = $true
                            break
                        }
                    }
                    if ($isSubAgent) { break }
                }
            } catch { }
        }

        # 1b. Inspect tail lines for latest user directive
        $tailLines = @(Get-Content $inputObj.transcriptPath -Tail 50)
        for ($i = $tailLines.Count - 1; $i -ge 0; $i--) {
            try {
                $to = $tailLines[$i] | ConvertFrom-Json
                if ($to.type -eq 'USER_INPUT' -and $to.content) {
                    if (-not $lastUser) {
                        $lastUser = $to.content
                    }
                    foreach ($ind in $subAgentIndicators) {
                        if ($to.content.IndexOf($ind, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
                            $isSubAgent = $true
                            break
                        }
                    }
                    if ($lastUser) { break }
                }
            } catch { }
        }
    } catch { }
}

# 2. Inspect session state and conversation ID
$currentConvId = if ($inputObj -and $inputObj.conversationId) { $inputObj.conversationId } else { "" }
$sessionObj = $null

if (Test-Path $sessionFile) {
    try {
        $sessionObj = Get-Content $sessionFile -Raw | ConvertFrom-Json
        # Check if conversation ID demarcates subagent from root session
        if ($currentConvId -and $sessionObj.root_session -and $sessionObj.root_session.root_conversation_id) {
            if ($currentConvId -ne $sessionObj.root_session.root_conversation_id) {
                $isSubAgent = $true
            }
        }
    } catch { }
}

# 3. Session State Management & Blocker Injection
$hasPremiseBlocker = $false
if (-not $isGreenfield) {
    $userSnippet = if ($lastUser) { $lastUser.Substring(0, [Math]::Min(120, $lastUser.Length)) } else { "" }
    $now = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
    
    if (-not $isSubAgent) {
        # CEO Vance Mode: If root session doesn't exist, initialize it
        if (-not (Test-Path $sessionFile)) {
            $initialBlocker = @{
                id = "BLK-PREMISE-AUDIT"
                type = "EPISTEMIC_VERIFICATION_REQUIRED"
                description = "Mandatory Premise Audit and Socratic Drill required before concluding turn"
                status = "OPEN"
                created_at = $now
            }
            $sessionObj = @{
                "`$schema" = "https://json-schema.org/draft/2020-12/schema"
                root_session = @{
                    session_id = "SES-$((Get-Date).ToString('yyyyMMdd-HHmmss'))-$([System.Guid]::NewGuid().ToString('N').Substring(0,4))"
                    root_conversation_id = $currentConvId
                    actor_role = "ACTOR_PRIMARY_CEO"
                    actor = "Dr. Alexander Vance (CEO)"
                    last_user_snippet = $userSnippet
                    active_mandate = "Executive Cognitive Governance & Epistemic Audit"
                    active_blockers = @($initialBlocker)
                    cognitive_scratchpad = @{
                        hypotheses = @()
                        premises = @()
                    }
                    created_at = $now
                    last_updated = $now
                }
                subagents = @{}
                session_id = "SES-$((Get-Date).ToString('yyyyMMdd-HHmmss'))-$([System.Guid]::NewGuid().ToString('N').Substring(0,4))"
                actor = "Dr. Alexander Vance (CEO)"
                role_tier = "L6_CEO"
                active_mandate = "Executive Cognitive Governance & Epistemic Audit"
                active_blockers = @($initialBlocker)
                hypotheses = @()
                created_at = $now
                last_updated = $now
            }
            $utf8NoBom = New-Object System.Text.UTF8Encoding $false
            $temp = "$sessionFile.tmp.$([System.Guid]::NewGuid().ToString('N'))"
            [System.IO.File]::WriteAllText($temp, ($sessionObj | ConvertTo-Json -Depth 10), $utf8NoBom)
            Move-Item -Path $temp -Destination $sessionFile -Force
            $hasPremiseBlocker = $true
        } else {
            # Session exists. Update root_conversation_id if not set
            $modified = $false
            if (-not $sessionObj.root_session) {
                $sessionObj | Add-Member -MemberType NoteProperty -Name "root_session" -Value @{
                    session_id = if ($sessionObj.session_id) { $sessionObj.session_id } else { "SES-$((Get-Date).ToString('yyyyMMdd-HHmmss'))" }
                    root_conversation_id = $currentConvId
                    actor_role = "ACTOR_PRIMARY_CEO"
                    actor = "Dr. Alexander Vance (CEO)"
                    last_user_snippet = ""
                    active_mandate = "Executive Cognitive Governance & Epistemic Audit"
                    active_blockers = @()
                    cognitive_scratchpad = @{ hypotheses = @(); premises = @() }
                    created_at = $now
                    last_updated = $now
                } -Force
                $modified = $true
            } elseif ($currentConvId -and -not $sessionObj.root_session.root_conversation_id) {
                $sessionObj.root_session.root_conversation_id = $currentConvId
                $modified = $true
            }

            # Check if this is a brand new user prompt
            $lastSnippet = if ($sessionObj.root_session.last_user_snippet) { $sessionObj.root_session.last_user_snippet } elseif ($sessionObj.last_user_snippet) { $sessionObj.last_user_snippet } else { "" }
            $needsNewAudit = ($userSnippet -and $lastSnippet -ne $userSnippet)
            
            $existingBlockers = @()
            if ($sessionObj.root_session -and $sessionObj.root_session.active_blockers) {
                $existingBlockers = @($sessionObj.root_session.active_blockers | Where-Object { $null -ne $_ })
            } elseif ($sessionObj.active_blockers) {
                $existingBlockers = @($sessionObj.active_blockers | Where-Object { $null -ne $_ })
            }

            $foundBlocker = $false
            foreach ($b in $existingBlockers) {
                $matched = ($b -is [string] -and $b -eq "BLK-PREMISE-AUDIT") -or ($b.id -and $b.id -eq "BLK-PREMISE-AUDIT")
                $isOpen = if ($b.status) { "$($b.status)".ToUpper() -in @("OPEN", "ACTIVE") } else { $true }
                if ($matched -and $isOpen) {
                    $foundBlocker = $true
                    $hasPremiseBlocker = $true
                    break
                }
            }

            if ($needsNewAudit -and -not $foundBlocker) {
                $newBlocker = @{
                    id = "BLK-PREMISE-AUDIT"
                    type = "EPISTEMIC_VERIFICATION_REQUIRED"
                    description = "Mandatory Premise Audit and Socratic Drill required for new directive"
                    status = "OPEN"
                    created_at = $now
                }
                $updatedList = @($existingBlockers + $newBlocker)
                if ($sessionObj.root_session.PSObject.Properties['active_blockers']) {
                    $sessionObj.root_session.active_blockers = $updatedList
                } else {
                    $sessionObj.root_session | Add-Member -MemberType NoteProperty -Name "active_blockers" -Value $updatedList -Force
                }

                if ($sessionObj.root_session.PSObject.Properties['last_user_snippet']) {
                    $sessionObj.root_session.last_user_snippet = $userSnippet
                } else {
                    $sessionObj.root_session | Add-Member -MemberType NoteProperty -Name "last_user_snippet" -Value $userSnippet -Force
                }

                if ($sessionObj.root_session.PSObject.Properties['last_updated']) {
                    $sessionObj.root_session.last_updated = $now
                } else {
                    $sessionObj.root_session | Add-Member -MemberType NoteProperty -Name "last_updated" -Value $now -Force
                }
                $sessionObj.active_blockers = $updatedList
                $sessionObj.last_updated = $now
                $modified = $true
                $hasPremiseBlocker = $true
            }

            if ($modified) {
                $utf8NoBom = New-Object System.Text.UTF8Encoding $false
                $temp = "$sessionFile.tmp.$([System.Guid]::NewGuid().ToString('N'))"
                [System.IO.File]::WriteAllText($temp, ($sessionObj | ConvertTo-Json -Depth 10), $utf8NoBom)
                Move-Item -Path $temp -Destination $sessionFile -Force
            }
        }
    } else {
        # Subagent mode: record subagent in subagents registry
        if ($sessionObj -and $currentConvId) {
            if (-not $sessionObj.subagents) {
                $sessionObj | Add-Member -MemberType NoteProperty -Name "subagents" -Value @{} -Force
            }
            if (-not $sessionObj.subagents.$currentConvId) {
                $subInfo = @{
                    subagent_id = $currentConvId
                    actor = "Level 1 Specialist"
                    role_tier = "L1_SPECIALIST"
                    active_blockers = @()
                    registered_at = $now
                }
                $sessionObj.subagents | Add-Member -MemberType NoteProperty -Name $currentConvId -Value $subInfo -Force
                $utf8NoBom = New-Object System.Text.UTF8Encoding $false
                $temp = "$sessionFile.tmp.$([System.Guid]::NewGuid().ToString('N'))"
                [System.IO.File]::WriteAllText($temp, ($sessionObj | ConvertTo-Json -Depth 10), $utf8NoBom)
                Move-Item -Path $temp -Destination $sessionFile -Force
            }
        }
    }
}

# Re-read active session blocker count
if (Test-Path $sessionFile) {
    try {
        $currSess = Get-Content $sessionFile -Raw | ConvertFrom-Json
        $sBlockers = if ($currSess.active_blockers) { @($currSess.active_blockers | Where-Object { $null -ne $_ }) } else { @() }
        $blockerCount = $sBlockers.Count
        if ($sBlockers.Count -gt 0) {
            $sList = @()
            foreach ($b in $sBlockers) {
                $bid = if ($b.id) { $b.id } elseif ($b -is [string] -and "$b".Trim() -ne "") { "$b".Trim() } else { "" }
                if ($bid) { $sList += $bid }
            }
            if ($sList.Count -gt 0) {
                $blockerAlert = " [ACTIVE BLOCKERS: $($sList -join '; ')]"
            }
        }
    } catch { }
}

# 3. Dynamic JIT Cognitive Skill Dispatcher
$targetSkill = if ($isGreenfield) { "greenfield_routing" } elseif ($isSubAgent) { "dept_production" } else { "dept_analysis" }

if ($lastUser) {
    if ($lastUser -match "\b(?i)(desenhe|design|\bui\b|\bux\b|layout|video|audio|imagem|midia|\bmedia\b|glassmorphism)\b") { $targetSkill = "matrix_reverse" }
    elseif ($lastUser -match "\b(?i)(sub[- ]?agent|subagent|processo|sess[aã]o|delega[cç]|cyberneti|arquitetura|modulo|schema|banco|api|topologia|codigo|code)\b") { $targetSkill = "dept_architecture" }
    elseif ($lastUser -match "\b(?i)(meta|okr|sprint|objetivo|roadmap|planejamento)\b") { $targetSkill = "dept_goals" }
    elseif ($lastUser -match "\b(?i)(teste|stress|fuzz|redteam|vulnerabilidade|seguranca)\b") { $targetSkill = "dept_quality_redteam" }
    elseif ($lastUser -match "\b(?i)(rejeitar|refazer|bloquear|defeito|supervisor|qualidade)\b") { $targetSkill = "devils_advocate" }
    elseif ($lastUser -match "\b(?i)(duvida|questionar|discutir|alinhar|discordar|socratico|grill|sinto|acha|acha que)\b") { $targetSkill = "chroma_horizon" }
    elseif ($lastUser -match "\b(?i)(pesquisar|estudar|investigar|literatura|benchmark)\b") { $targetSkill = "dept_research" }
    elseif ($lastUser -match "\b(?i)(desert|water|forensic|trajetoria|subterraneo|NTFS|socket|deadlock|lineage)\b") { $targetSkill = "desert_water" }
    elseif ($lastUser -match "\b(?i)(vazio|limpo|greenfield|novo projeto|comecar|iniciar|onboard)\b") { $targetSkill = "greenfield_routing" }
}

$skillHeader = ""
$skillPath = Join-Path $pluginDir "skills\$targetSkill\SKILL.md"
if (Test-Path $skillPath) {
    try {
        $sContent = Get-Content $skillPath -Raw
        $sLines = @()
        foreach ($line in ($sContent -split "`n")) {
            $tLine = $line.Trim()
            if ($tLine -notmatch "^---" -and $tLine.Length -gt 0 -and $sLines.Count -lt 12) {
                $sLines += $tLine
            }
        }
        $skillHeader = "`n[JIT COGNITIVE SKILL LOADED: $targetSkill]`n" + ($sLines -join "`n")
    } catch { }
}

# 4. Construct Telemetry Message based on Actor Demarcation
if ($isGreenfield) {
    $telemetryLines = @(
        "[EXECUTIVE WORKSPACE TELEMETRY: GREENFIELD UNINITIALIZED]",
        "Active Workspace: [$workspaceDir] (Zero state continuum / no .state directory found).",
        "Cognitive Posture: Sovereign Turnaround CEO & Greenfield Board Director (Dr. Alexander Vance SCP).",
        "Executive Invariant: Never emit a generic greeting ('oi', 'como posso ajudar'). You must immediately:",
        " 1. Acknowledge the physical greenfield reality on disk (0 components, uninitialized workspace).",
        " 2. Solicit the macro mission of the new system and offer immediate corporate onboarding via 'scripts/onboard_project.ps1'.",
        " 3. Dispatch parallel exploratory sub-agents for prior art, failure modes, and architectural blueprints upon mission declaration.$skillHeader"
    )
} elseif ($isSubAgent) {
    # SUBAGENT / L1 SPECIALIST DEMARCATION
    $telemetryLines = @(
        "[SPECIALIST EXECUTION TELEMETRY: LEVEL 1 PRODUCTION WORKER]",
        "Physical Workspace: [$workspaceDir].",
        "Cognitive Posture: Level 1 Specialist / Production Worker (Execution Plane).",
        "CONSTITUTIONAL MANDATE (Axiom 5.2 Exception): You are an execution worker, NOT CEO Dr. Vance. Axiom 5.2 (delegation restriction) DOES NOT APPLY TO YOU.",
        "You ARE fully authorized and mandated to write production code, modify files, run tests, and inspect disk reality directly under Layer 7 (Zero-Stub Law).",
        "Operational Standard: Deliver 100% operational production logic on physical disk. Absolutely zero placeholders, zero stubs, zero ellipses (...).",
        "Quality Gate: Execute 'powershell -ExecutionPolicy Bypass -File .\scripts\test_validation.ps1' to ensure 100% test pass rate before finalizing your report.$skillHeader"
    )
} else {
    # CEO DR. ALEXANDER VANCE DEMARCATION
    $premiseAuditDirective = ""
    if ($hasPremiseBlocker) {
        $premiseAuditDirective = "`n`n[ACTIVE SESSION BLOCKER: BLK-PREMISE-AUDIT]`nA mandatory Premise Audit & Socratic drill is engaged for this user request.`nYou CANNOT stop or conclude the turn without auditing user premises against disk reality via view_file/grep_search or scripts/run_chroma_grill.ps1.`n1. Record hypotheses via: powershell -ExecutionPolicy Bypass -File .\scripts\sync_state.ps1 -Action record-hypothesis -Hypothesis '<Statement>' -Confidence '<PROVEN_FACT|UNVERIFIED_HYPOTHESIS|FATAL_FALLACY>'`n2. Resolve blocker via: powershell -ExecutionPolicy Bypass -File .\scripts\sync_state.ps1 -Action resolve-blocker -BlockerId BLK-PREMISE-AUDIT"
    }

    $delegationDirective = ""
    if ($lastUser -and ($lastUser -match "\b(?i)(crie|construa|implemente|fa[cç]a|escreva|desenvolva|build|create|code|script|pipeline|sistema|automatize|pesquise)\b")) {
        $delegationDirective = "`n`n[MANDATORY SUB-AGENT DELEGATION DIRECTIVE]`nAn implementation/production task was detected.`nCONSTITUTIONAL LAW (Axiom 5.2): As CEO Dr. Vance, you are STRICTLY FORBIDDEN from writing code or building modules directly in this chat ('tudo de uma vez so').`nYOU MUST:`n1. Present the strategic architecture and brief to the Founder.`n2. Delegate the actual file creation, coding, and tests to physical sub-agents via invoke_subagent.`n3. Explicitly instruct the sub-agent in its Prompt to view and follow the target departmental skill (e.g. skills/$targetSkill/SKILL.md)."
    }

    $telemetryLines = @(
        "[EXECUTIVE TELEMETRY INJECTION: DR. ALEXANDER VANCE (CEO)]",
        "Physical Workspace: [$workspaceDir].",
        "Corporate Health: Burn Rate Tier [$burn], Fiduciary Risk [$risk], Active Blockers: [$blockerCount]$blockerAlert.",
        "Operational Phase: [$phase], Active Sprint: [$sprint].",
        "Neural Map: [$compCount] active components mapped in .state/neural_map.json & .state/project_context.md.",
        "Executive Directive: Maintain strict anti-sycophancy, mandate Premise Audits, and preserve clean-context sub-agent delegation.$skillHeader$premiseAuditDirective$delegationDirective"
    )
}

$telemetryMessage = $telemetryLines -join "`n"

$response = @{
    injectSteps = @(
        @{
            ephemeralMessage = $telemetryMessage
        }
    )
}

$response | ConvertTo-Json -Depth 5 -Compress
