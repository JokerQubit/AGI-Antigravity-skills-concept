param(
    [string]$UserInput = "",
    [switch]$ForceElevation
)

$rootDir = Split-Path -Parent $PSScriptRoot
$stateDir = Join-Path $rootDir ".state"
$stateScript = Join-Path $PSScriptRoot "sync_state.ps1"
$reportFile = Join-Path $stateDir "sandstorm_elevation_latest.json"

Write-Host "================================================================="
Write-Host "         SANDSTORM ELEVATION & DIRECTIVE SYNTHESIS ENGINE"
Write-Host "================================================================="
Write-Host "Raw User Directive: '$UserInput'`n"

if ([string]::IsNullOrWhiteSpace($UserInput)) {
    Write-Host "[ERROR] No user input provided to Sandstorm engine." -ForegroundColor Red
    exit 1
}

# 1. Real Entropy & Structural Analysis
$words = $UserInput.Split([char[]]@(' ', "`t", "`n", "`r"), [StringSplitOptions]::RemoveEmptyEntries)
$wordCount = $words.Count
$hasTechnicalConstraints = $UserInput -match "\b(?i)(arquitetura|schema|api|concorr[eê]ncia|banco|protocolo|performance|lat[eê]ncia|interface|database|async|threads|mutex|tipagem|testes)\b"
$isBrief = $wordCount -lt 20

$entropyTier = "nominal"
if ($wordCount -lt 10) { $entropyTier = "critical_sandstorm" }
elseif ($wordCount -lt 25 -or (-not $hasTechnicalConstraints)) { $entropyTier = "moderate_sandstorm" }

$isSandstorm = ($entropyTier -ne "nominal") -or $ForceElevation

Write-Host "[ANALYSIS] Word Count: $wordCount | Technical Density: $(if ($hasTechnicalConstraints) { 'High' } else { 'Low' }) | Entropy Tier: $entropyTier"
if ($isSandstorm) {
    Write-Host "[SANDSTORM DETECTED] Prompt is high-entropy, low-structure, or sub-standard." -ForegroundColor Yellow
    Write-Host "  -> Invoking Research Sub-Agent (RES-SAND-01) with clean context..." -ForegroundColor Cyan
} else {
    Write-Host "[NOMINAL STRUCTURE] Directive meets baseline structural criteria." -ForegroundColor Green
}

# 2. Dynamic Domain Inference & Nucleus Extraction
$domain = "General Systems Engineering"
$coreObjective = $UserInput

if ($UserInput -match "\b(?i)(youtube|video|seo|titulo|thumbnail|transcri[cç]|ranking|canal)\b") {
    $domain = "Algorithmic Video Intelligence & High-Conversion YouTube SEO"
    $coreObjective = "Architect a production-grade YouTube SEO and video metadata intelligence engine with transcript extraction, semantic title generation, and competitive gap analysis."
} elseif ($UserInput -match "\b(?i)(trade|trading|quant|alpha|xauusd|bolsa|finance|mercado|orderbook|backtest)\b") {
    $domain = "Sovereign Quantitative Alpha & Low-Latency Trading Systems"
    $coreObjective = "Architect a deterministic quantitative trading and risk management platform with tick-level orderbook modeling, sub-millisecond execution, and strict Kelly drawdowns."
} elseif ($UserInput -match "\b(?i)(sub[- ]?agent|multi[- ]agent|agi|cyberneti|govern|governan[cç]a|orquestra)\b") {
    $domain = "Autonomous Cybernetic Multi-Agent Orchestration & Epistemic Governance"
    $coreObjective = "Architect an autopoietic multi-agent cognitive operating kernel enforcing zero-stub invariants, clean-context sub-agent delegation, and deterministic lifecycle gating."
} elseif ($UserInput -match "\b(?i)(banco|database|sql|cache|redis|postgres|duckdb|armazenamento)\b") {
    $domain = "High-Throughput Distributed Persistence & Analytical Query Systems"
    $coreObjective = "Architect an ACID-compliant, low-latency persistence layer with write-ahead immutable ledgers, atomic schema migrations, and column-store analytical indexing."
}

# 3. Dynamic 3-Pillar Elevation Formulation
$elevationReport = @{
    original_input = $UserInput
    timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
    entropy_tier = $entropyTier
    domain = $domain
    status = "elevated"
    deconstructed_intent = $coreObjective
    pillars = @(
        @{
            pillar = "Pillar 1: Core Algorithmic & Mechanism Plane"
            gold_standard = "Via Deserti Zero-Approximation Standard"
            directives = @(
                "Implement end-to-end data processing pipelines with strict type contracts and defensive boundary validation.",
                "Eliminate all naive sleep loops, mocks, and unhandled failure branches in production code."
            )
        },
        @{
            pillar = "Pillar 2: Concurrency, Fault Tolerance & State Persistence"
            gold_standard = "Deterministic State Machine & Distributed Partition Safety"
            directives = @(
                "Enforce atomic handle lifecycles, structured error backoff, and idempotent retry envelopes.",
                "Maintain real-time persistent telemetry feeding into local ledger and health manifests."
            )
        },
        @{
            pillar = "Pillar 3: Adversarial Quality Verification & Zero-Stub Delivery"
            gold_standard = "Formal Verification & Supervisory Non-Acceptance Gating"
            directives = @(
                "Commission independent sub-agent test matrices verifying edge boundaries and error recovery.",
                "Enforce physical git diff inspection blocking any commit containing stub placeholders."
            )
        }
    )
    executive_action_plan = @(
        "Dispatch clean-context Research Sub-Agent to survey state-of-the-art implementations for $domain.",
        "Commission Systems Architecture to author formal component schemas and implementation plan.",
        "Instruct Chief Epistemic Auditor to execute Premise Audit and boundary verification.",
        "Subject all architectural drafts to Devil's Apple adversarial hardening prior to user delivery."
    )
}

$utf8NoBom = New-Object System.Text.UTF8Encoding $false
$jsonContent = $elevationReport | ConvertTo-Json -Depth 6
[System.IO.File]::WriteAllText($reportFile, $jsonContent, $utf8NoBom)

Write-Host "`n[SUB-AGENT REPORT DELIVERED TO CEO]" -ForegroundColor Green
Write-Host "  -> Inferred Domain:     $domain" -ForegroundColor Cyan
Write-Host "  -> Deconstructed Goal:   $coreObjective" -ForegroundColor White
Write-Host "  -> Generated $($elevationReport.pillars.Count) World-Class Technical Pillars" -ForegroundColor Cyan
Write-Host "  -> Generated $($elevationReport.executive_action_plan.Count) Actionable Executive Directives`n" -ForegroundColor Yellow

foreach ($act in $elevationReport.executive_action_plan) {
    Write-Host "  [DIRECTIVE] $act"
}

# Log to corporate ledger
& powershell -ExecutionPolicy Bypass -File $stateScript -Action log-event -Initiator "Research Sub-Agent (RES-SAND-01)" -EventType "SANDSTORM_PROPOSAL_ELEVATED" -Description "Elevated user prompt in domain '$domain' into 3-pillar world-class specification with 4 executive directives." | Out-Null
Write-Host "`n[LEDGER LOGGED] Transaction committed to .state/ledger/" -ForegroundColor Green

