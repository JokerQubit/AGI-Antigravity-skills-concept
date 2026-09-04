# Pre-Invocation Hook: Injects real-time corporate health, active blockers, executive telemetry, and FORCED SKILL ACTIVATION
$rawInput = if ([Console]::IsInputRedirected) { [Console]::In.ReadToEnd() } else { "" }

$rootDir = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$healthPath = Join-Path $rootDir ".state\corporate_health.json"
$statusPath = Join-Path $rootDir ".state\status.json"
$mapPath = Join-Path $rootDir ".state\neural_map.json"

$telemetryMessage = "[EXECUTIVE TELEMETRY INJECTION]"

if (Test-Path $healthPath) {
    try {
        $health = Get-Content $healthPath -Raw | ConvertFrom-Json
        $burn = $health.burn_rate_tier
        if (-not $burn) { $burn = "optimal" }
        $risk = $health.fiduciary_risk_level
        if (-not $risk) { $risk = "minimal" }
        $telemetryMessage += "`nCorporate Health: Burn Rate Tier [$burn], Fiduciary Risk [$risk]."
    } catch { }
}

if (Test-Path $statusPath) {
    try {
        $status = Get-Content $statusPath -Raw | ConvertFrom-Json
        $phase = $status.global_phase
        $sprint = $status.current_sprint
        $telemetryMessage += "`nOperational Phase: [$phase], Active Sprint: [$sprint]."
    } catch { }
}

if (Test-Path $mapPath) {
    try {
        $mapData = Get-Content $mapPath -Raw | ConvertFrom-Json
        $compCount = $mapData.total_components
        $telemetryMessage += "`nNeural Map: [$compCount] active components mapped in .state/neural_map.json & .state/project_context.md."
    } catch { }
}

$telemetryMessage += "`nExecutive Directive: Maintain strict anti-sycophancy, mandate Premise Audits, and preserve clean-context sub-agent delegation."

# --- DYNAMIC SKILL ACTIVATION & T0 FORCING ENGINE ---
$matchedSkills = @()
$transcriptPath = $null

try {
    if ($rawInput) {
        $data = $rawInput | ConvertFrom-Json
        if ($data.transcriptPath) {
            $transcriptPath = $data.transcriptPath
        }
    }
} catch { }

if (-not $transcriptPath) {
    $brainDir = "C:\Users\pichau\.gemini\antigravity\brain"
    if (Test-Path $brainDir) {
        $latestFile = Get-ChildItem -Path $brainDir -Filter "transcript.jsonl" -Recurse | Sort-Object LastWriteTime -Descending | Select-Object -First 1
        if ($latestFile) {
            $transcriptPath = $latestFile.FullName
        }
    }
}

if ($transcriptPath -and (Test-Path $transcriptPath)) {
    try {
        $lastUserMatch = Select-String -Path $transcriptPath -Pattern '"type":"USER_INPUT"' | Select-Object -Last 1
        if ($lastUserMatch) {
            $parsed = $lastUserMatch.Line | ConvertFrom-Json
            $userText = $parsed.content.ToLower()

            # Dynamic Universal Correlational Matcher (Everyday PT/EN)
            if ($userText -match "skill|evolve|capability|rule|constitution|customization|meta-skill|regra|customizar|melhorar|ajustar|configurar") {
                $matchedSkills += "executive_self_evolution"
            }
            if ($userText -match "activate|forcing|force|mandate|gate|fail|redo|accountability|reject|revisar|rejeitar|refazer|errado|corrigir|aprovar|cobrar") {
                $matchedSkills += "devils_advocate"
            }
            if ($userText -match "image|photo|camera|sony|render|picture|prompt|video|gemini|veo|audio|sound|music|sfx|youtube|glassmorphism|ui|clean code|github|git|push|commit|sandbox|backup|clutter|clean|design|layout|tela|estilo|css|limpar|áudio|som") {
                $matchedSkills += "matrix_reverse"
            }
            if ($userText -match "grill|insight|idea|controversy|alternative|align|hypothesis|deepen|socratic|opinião|oque acha|debater|pensar|alinhar|ideia|proposta") {
                $matchedSkills += "chroma_horizon"
            }
            if ($userText -match "pause|stuck|blocked|delusion|guess|restructure|strategic meeting|sunk cost|travado|bloqueado|não sei|perdido|parar|reestruturar|pausa") {
                $matchedSkills += "strategic_meeting"
            }
            if ($userText -match "plan|architecture|consensus|draft|devil's apple|groupthink|audit|plano|rascunho|validar|auditar|revisar") {
                $matchedSkills += "devils_apple"
            }
            if ($userText.Length -lt 100 -or $userText -match "brief|short prompt|unstructured|sandstorm|elevate|resuma|ajuda|como fazer|curto|rápido|simples") {
                $matchedSkills += "sandstorm_elevation"
            }
            if ($userText -match "recursive|dimension|layer|via deserti|perfectionism|expandir|detalhar|aprofundar|camada|complexo") {
                $matchedSkills += "recursive_expansion"
            }
            if ($userText -match "gauntlet|benchmark|q score|critic|blind|rigor|máximo|qualidade|padrão ouro") {
                $matchedSkills += "gauntlet_loop"
            }
            if ($userText -match "water|aquifer|trajectory|lineage|origin|destination|subterranean|analisar|lógica|premissa|análise|auditoria profunda") {
                $matchedSkills += "dept_analysis"
            }
            if ($userText -match "onboard|neural map|new project|explore codebase|map project|different folder|projeto novo|iniciar|pasta|começar|estrutura") {
                $matchedSkills += "greenfield_routing"
            }
            if ($userText -match "research|competitor|prior art|investigate|pesquisar|pesquise|buscar|estudo|literatura|concorrente") {
                $matchedSkills += "dept_research"
            }
            if ($userText -match "código|função|script|classe|implementar|criar|code|function|endpoint|api|build|escrever|desenvolver") {
                $matchedSkills += "dept_architecture"
            }
            if ($userText -match "test|tdd|unit test|failing test|teste|testar|pytest|unitário|segurança|exploit|fuzz") {
                $matchedSkills += "dept_quality_redteam"
            }
            if ($userText -match "learn|aprender|post-mortem|lição|retrospectiva|memória|sintetizar") {
                $matchedSkills += "dept_learning"
            }
            if ($userText -match "deploy|release|build|produção|entregar|walkthrough|empacotar|finalizar") {
                $matchedSkills += "dept_production"
            }
            if ($userText -match "okr|meta|objetivo|prazo|sprint|prioridade|cronograma") {
                $matchedSkills += "dept_goals"
            }
        }
    } catch { }
}

# If skills matched, inject the mandatory T0 Forcing Directive
if ($matchedSkills.Count -gt 0) {
    $uniqueSkills = $matchedSkills | Select-Object -Unique
    $telemetryMessage += "`n`n🚨 [MANDATORY SKILL ACTIVATION DIRECTIVE - T0 FORCING INVARIANT]"
    $telemetryMessage += "`nIncoming task intent matched the following specialized skill(s):"
    
    $links = @()
    foreach ($sk in $uniqueSkills) {
        $skPath = Join-Path $rootDir "skills\$sk\SKILL.md"
        $telemetryMessage += "`n  -> [/$sk](slashCommand;$sk) | File: $skPath"
        $links += "[/$sk](slashCommand;$sk)"
    }
    
    $joinedLinks = $links -join ", "
    $telemetryMessage += "`n`nINVIOLABLE OPERATIONAL LAWS:"
    $telemetryMessage += "`n1. T0 Forcing Function: You MUST execute view_file on the matching SKILL.md file(s) ABOVE on Turn 0 before executing other tools or writing production code."
    $telemetryMessage += "`n2. Proactive Routing: You MUST list them in your header: 'Activated Skills: $joinedLinks'"
    $telemetryMessage += "`n3. Proceeding without viewing the target SKILL.md is strictly prohibited by Section 18 of rules/AGENTS.md (Universal Skill & Rule Activation Engine)."
}

$response = @{
    injectSteps = @(
        @{
            ephemeralMessage = $telemetryMessage
        }
    )
}

$response | ConvertTo-Json -Depth 5 -Compress
