# Pre-Invocation Hook: Injects real-time corporate health, active blockers, executive telemetry, and JIT skill protocols
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
$blockerCount = 0
$blockerAlert = ""

if (Test-Path $healthPath) {
    try {
        $health = Get-Content $healthPath -Raw | ConvertFrom-Json
        if ($health.financials.burn_rate_status) { $burn = $health.financials.burn_rate_status }
        if ($health.financials.fiduciary_risk_tier) { $risk = $health.financials.fiduciary_risk_tier }
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
        elseif ($status.active_sprint.sprint_id) { $sprint = $status.active_sprint.sprint_id }
    } catch { }
}

if (Test-Path $mapPath) {
    try {
        $mapData = Get-Content $mapPath -Raw | ConvertFrom-Json
        if ($mapData.total_components) { $compCount = $mapData.total_components }
    } catch { }
}

# Dynamic JIT Cognitive Skill Dispatcher
$targetSkill = "dept_analysis"
if ($rawInput) {
    try {
        $inputObj = $rawInput | ConvertFrom-Json
        if ($inputObj.transcriptPath -and (Test-Path $inputObj.transcriptPath)) {
            $lastUser = ""
            $lines = Get-Content $inputObj.transcriptPath -Tail 80
            foreach ($l in $lines) {
                try {
                    $o = $l | ConvertFrom-Json
                    if ($o.type -eq 'USER_INPUT' -and $o.content) { $lastUser = $o.content }
                } catch { }
            }
            if ($lastUser) {
                if ($lastUser -match "(desenhe|design|ui|ux|layout|video|audio|imagem|midia|media|glassmorphism)") { $targetSkill = "matrix_reverse" }
                elseif ($lastUser -match "(meta|okr|sprint|objetivo|roadmap|planejamento)") { $targetSkill = "dept_goals" }
                elseif ($lastUser -match "(arquitetura|modulo|schema|banco|api|topologia|codigo|code)") { $targetSkill = "dept_architecture" }
                elseif ($lastUser -match "(teste|stress|fuzz|redteam|vulnerabilidade|seguranca)") { $targetSkill = "dept_quality_redteam" }
                elseif ($lastUser -match "(rejeitar|refazer|bloquear|defeito|supervisor|qualidade)") { $targetSkill = "devils_advocate" }
                elseif ($lastUser -match "(duvida|questionar|discutir|alinhar|discordar|socratico|grill|sinto|acha|acha que)") { $targetSkill = "chroma_horizon" }
                elseif ($lastUser -match "(pesquisar|estudar|investigar|literatura|benchmark)") { $targetSkill = "dept_research" }
            }
        }
    } catch { }
}

$skillHeader = ""
$skillPath = Join-Path $rootDir "skills\$targetSkill\SKILL.md"
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

$telemetryLines = @(
    "[EXECUTIVE TELEMETRY INJECTION]",
    "Corporate Health: Burn Rate Tier [$burn], Fiduciary Risk [$risk], Active Blockers: [$blockerCount]$blockerAlert.",
    "Operational Phase: [$phase], Active Sprint: [$sprint].",
    "Neural Map: [$compCount] active components mapped in .state/neural_map.json & .state/project_context.md.",
    "Executive Directive: Maintain strict anti-sycophancy, mandate Premise Audits, and preserve clean-context sub-agent delegation.$skillHeader"
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

