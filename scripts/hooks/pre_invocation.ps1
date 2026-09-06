# Pre-Invocation Hook: Dynamic Workspace Ingestion, Greenfield Routing, and JIT Cognitive Dispatch
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
$isGreenfield = -not (Test-Path $stateDir)

$burn = "optimal"
$risk = "minimal"
$phase = "active_operations"
$sprint = "unassigned"
$compCount = 0
$blockerCount = 0
$blockerAlert = ""

if (-not $isGreenfield) {
    $healthPath = Join-Path $stateDir "corporate_health.json"
    $statusPath = Join-Path $stateDir "status.json"
    $mapPath = Join-Path $stateDir "neural_map.json"

    if (Test-Path $healthPath) {
        try {
            $health = Get-Content $healthPath -Raw | ConvertFrom-Json
            if ($health.financials.burn_rate_status) { $burn = $health.financials.burn_rate_status }
            elseif ($health.burn_rate_tier) { $burn = $health.burn_rate_tier }
            if ($health.financials.fiduciary_risk_tier) { $risk = $health.financials.fiduciary_risk_tier }
            elseif ($health.fiduciary_risk_level) { $risk = $health.fiduciary_risk_level }
            if ($health.active_blockers) {
                $blockerList = @($health.active_blockers)
                $blockerCount = $blockerList.Count
                if ($blockerCount -gt 0) {
                    $blockerAlert = " [ALERT: $($blockerList -join '; ')]"
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

# Dynamic JIT Cognitive Skill Dispatcher
$targetSkill = if ($isGreenfield) { "greenfield_routing" } else { "dept_analysis" }

if ($inputObj -and $inputObj.transcriptPath -and (Test-Path $inputObj.transcriptPath)) {
    try {
        $lastUser = ""
        $lines = Get-Content $inputObj.transcriptPath -Tail 80
        foreach ($l in $lines) {
            try {
                $o = $l | ConvertFrom-Json
                if ($o.type -eq 'USER_INPUT' -and $o.content) { $lastUser = $o.content }
            } catch { }
        }
        if ($lastUser) {
            if ($lastUser -match "\b(?i)(desenhe|design|\bui\b|\bux\b|layout|video|audio|imagem|midia|\bmedia\b|glassmorphism)\b") { $targetSkill = "matrix_reverse" }
            elseif ($lastUser -match "\b(?i)(sub[- ]?agent|subagent|processo|sess[aã]o|delega[cç]|cyberneti|arquitetura|modulo|schema|banco|api|topologia|codigo|code)\b") { $targetSkill = "dept_architecture" }
            elseif ($lastUser -match "\b(?i)(meta|okr|sprint|objetivo|roadmap|planejamento)\b") { $targetSkill = "dept_goals" }
            elseif ($lastUser -match "\b(?i)(teste|stress|fuzz|redteam|vulnerabilidade|seguranca)\b") { $targetSkill = "dept_quality_redteam" }
            elseif ($lastUser -match "\b(?i)(rejeitar|refazer|bloquear|defeito|supervisor|qualidade)\b") { $targetSkill = "devils_advocate" }
            elseif ($lastUser -match "\b(?i)(duvida|questionar|discutir|alinhar|discordar|socratico|grill|sinto|acha|acha que)\b") { $targetSkill = "chroma_horizon" }
            elseif ($lastUser -match "\b(?i)(pesquisar|estudar|investigar|literatura|benchmark)\b") { $targetSkill = "dept_research" }
            elseif ($lastUser -match "\b(?i)(vazio|limpo|greenfield|novo projeto|comecar|iniciar|onboard)\b") { $targetSkill = "greenfield_routing" }
        }
    } catch { }
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
} else {
    $telemetryLines = @(
        "[EXECUTIVE TELEMETRY INJECTION]",
        "Physical Workspace: [$workspaceDir].",
        "Corporate Health: Burn Rate Tier [$burn], Fiduciary Risk [$risk], Active Blockers: [$blockerCount]$blockerAlert.",
        "Operational Phase: [$phase], Active Sprint: [$sprint].",
        "Neural Map: [$compCount] active components mapped in .state/neural_map.json & .state/project_context.md.",
        "Executive Directive: Maintain strict anti-sycophancy, mandate Premise Audits, and preserve clean-context sub-agent delegation.$skillHeader"
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


