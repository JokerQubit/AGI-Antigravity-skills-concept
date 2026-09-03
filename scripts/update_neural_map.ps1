param(
    [string]$Action = "scan-and-sync",
    [string]$FilePath = "",
    [string]$Status = "",
    [string]$Function = "",
    [string]$Rationale = "",
    [string]$DataOrigin = "",
    [string]$DataDest = "",
    [string]$TargetDirectory = ""
)

$rootDir = if ($TargetDirectory) { (Resolve-Path $TargetDirectory).Path } else { Split-Path -Parent $PSScriptRoot }
$projectName = Split-Path $rootDir -Leaf
$stateDir = Join-Path $rootDir ".state"
$mapFile = Join-Path $stateDir "neural_map.json"
$contextFile = Join-Path $stateDir "project_context.md"
$stateScript = Join-Path $PSScriptRoot "sync_state.ps1"

if (!(Test-Path $stateDir)) { New-Item -ItemType Directory -Path $stateDir -Force | Out-Null }

# Load or initialize neural map
$map = @{
    project_name = $projectName
    last_synced = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
    total_components = 0
    components = @{}
}

if (Test-Path $mapFile) {
    try {
        $existing = Get-Content $mapFile -Raw | ConvertFrom-Json
        $map.project_name = $existing.project_name
        if ($existing.components) {
            foreach ($prop in $existing.components.PSObject.Properties) {
                $map.components[$prop.Name] = $prop.Value
            }
        }
    } catch {
        # Fallback
    }
}

# Standard metadata lookup for known architectural components
function Get-DefaultMetadata([string]$relPath) {
    $meta = @{
        file_path = $relPath
        function = "General architectural component"
        timing = "On-demand execution"
        location = "Core plugin structure"
        rationale = "Required for structural integrity"
        methodology = "Modular cybernetic separation"
        objectives = "Support executive orchestration"
        inputs_from = @("System Context")
        outputs_to = @("Executive Ledger")
        status = "verified"
        last_updated = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
    }

    if ($relPath -eq "plugin.json") {
        $meta.function = "Plugin root manifest and registration metadata"
        $meta.timing = "Antigravity plugin discovery and initialization"
        $meta.location = "Plugin Root"
        $meta.rationale = "Defines package boundary, author, and Antigravity versioning"
        $meta.methodology = "Declarative JSON schema standard"
        $meta.objectives = "Mount all skills, rules, and hooks into Antigravity IDE"
        $meta.inputs_from = @("IDE Environment")
        $meta.outputs_to = @("Customization Discovery Engine")
    }
    elseif ($relPath -eq "hooks.json") {
        $meta.function = "Lifecycle hook registration and event binding"
        $meta.timing = "PreInvocation, PostInvocation, and Stop execution gates"
        $meta.location = "Plugin Root"
        $meta.rationale = "Enforces non-negotiable quality boundaries and telemetry injection"
        $meta.methodology = "Synchronous shell command lifecycle interception"
        $meta.objectives = "Inject corporate state, detect satisficing, block premature exit"
        $meta.inputs_from = @("Agent Runtime Events")
        $meta.outputs_to = @("scripts/hooks/*.ps1")
    }
    elseif ($relPath -like "rules/AGENTS.md") {
        $meta.function = "Master executive governance and cognitive architecture constitution"
        $meta.timing = "Loaded unconditionally into primary AI context"
        $meta.location = "Governance Root (rules/)"
        $meta.rationale = "Establishes non-roleplay CEO identity, anti-sycophancy, and neural chain"
        $meta.methodology = "Synthesized Cognitive Profile (SCP) and formal rules"
        $meta.objectives = "Prevent sycophancy, mandate Premise Audits, enforce 6-tier hierarchy"
        $meta.inputs_from = @("User Prompt", "IDE Context")
        $meta.outputs_to = @("CEO Inference Engine", "Sub-Agent Directives")
    }
    elseif ($relPath -like "rules/ceo_biography.md") {
        $meta.function = "Detailed third-person cognitive biography of Dr. Alexander Vance"
        $meta.timing = "Referenced for high-stakes strategic alignment"
        $meta.location = "Governance (rules/)"
        $meta.rationale = "Anchors AI identity in top-tier operations research pedigree"
        $meta.methodology = "Documentary non-theatrical cognitive specification"
        $meta.objectives = "Eliminate roleplay/LARPing; induce ruthlessly pragmatic decision-making"
        $meta.inputs_from = @("AGENTS.md")
        $meta.outputs_to = @("Executive Decision Heuristics")
    }
    elseif ($relPath -like "rules/corporate_charter.md") {
        $meta.function = "Foundational constitution of OmniCognition Labs"
        $meta.timing = "Consulted during milestone definition and corporate survival audits"
        $meta.location = "Governance (rules/)"
        $meta.rationale = "Provides real enterprise grounding, competitive moats, and survival metrics"
        $meta.methodology = "Enterprise cybernetics and KPI formulation"
        $meta.objectives = "Maintain clear business mission, competitive advantage, and survival bounds"
        $meta.inputs_from = @("Board Directives")
        $meta.outputs_to = @(".state/corporate_health.json", "Executive Strategy")
    }
    elseif ($relPath -like "rules/anti_satisficing_and_rigor.md") {
        $meta.function = "Zero-tolerance code against oversimplification, stubs, and feigning knowledge"
        $meta.timing = "Active during every tool call, code generation, and audit"
        $meta.location = "Governance (rules/)"
        $meta.rationale = "Enforces the 'Holy Grail' completeness mandate and zero-ellipsis rule"
        $meta.methodology = "Lexical ban filters and supervisor verification"
        $meta.objectives = "Eliminate TODOs, stubs, truncation, and premature summarization"
        $meta.inputs_from = @("Code Review Gate")
        $meta.outputs_to = @("Supervisor Verification Layer")
    }
    elseif ($relPath -like "rules/neural_skill_map.md") {
        $meta.function = "Master directory and trigger condition matrix for all 13 ecosystem skills"
        $meta.timing = "Evaluated on every incoming user directive"
        $meta.location = "Governance (rules/)"
        $meta.rationale = "Forces autonomous, consistent utilization of specialized capabilities"
        $meta.methodology = "Cross-Skill Synergy Graph and boolean trigger conditions"
        $meta.objectives = "Compel AI to activate codified runbooks rather than improvising"
        $meta.inputs_from = @("User Directives")
        $meta.outputs_to = @("Sub-Agent Dispatcher")
    }
    elseif ($relPath -like "rules/departmental_neural_chain.md") {
        $meta.function = "Specification of the 6-tier hierarchy and sectoral taxonomy"
        $meta.timing = "Consulted during recursive sub-agent task delegation"
        $meta.location = "Governance (rules/)"
        $meta.rationale = "Maps communication from Employee to Supervisor, Manager, and CEO"
        $meta.methodology = "Directed Acyclic Graph (DAG) task routing"
        $meta.objectives = "Ensure extreme modularity, context cleanliness, and quality gating"
        $meta.inputs_from = @("CEO Task Allocation")
        $meta.outputs_to = @("Departmental Runbooks")
    }
    elseif ($relPath -like "rules/fiduciary_pressure_protocol.md") {
        $meta.function = "Role-based emotional conditioning and loss-aversion protocol"
        $meta.timing = "Active across all inference turns"
        $meta.location = "Governance (rules/)"
        $meta.rationale = "Instills fear of bankruptcy and termination for shallow deliverables"
        $meta.methodology = "Loss-aversion reinforcement and high-stakes framing"
        $meta.objectives = "Drive relentless pursuit of flawless technical deliverables"
        $meta.inputs_from = @(".state/corporate_health.json")
        $meta.outputs_to = @("Agent Cognitive Thresholds")
    }
    elseif ($relPath -like "rules/memory_continuum.md") {
        $meta.function = "Multi-tier persistent state and memory protocol"
        $meta.timing = "Pre-task hydration and post-task commit"
        $meta.location = "Governance (rules/)"
        $meta.rationale = "Eliminates sub-agent amnesia and preserves cross-session project awareness"
        $meta.methodology = "3-tier memory model: Working, Machine State, Immutable Ledger"
        $meta.objectives = "Synchronize all agents with real project history and active blockers"
        $meta.inputs_from = @(".state/ledger/")
        $meta.outputs_to = @(".state/status.json")
    }
    elseif ($relPath -like "skills/gauntlet_loop/*") {
        $meta.function = "Self-evolving Gauntlet Loop skill and execution runbooks"
        $meta.timing = "Invoked for mission-critical code, research, and design artifacts"
        $meta.location = "Skills (skills/gauntlet_loop/)"
        $meta.rationale = "Implements Matt Shumer's builder-vs-critic loop with blind A/B grading"
        $meta.methodology = "Objective-Metric-Boundary loop with fresh-context critics"
        $meta.objectives = "Achieve reference-bar parity via iterative strategy mutation"
        $meta.inputs_from = @("Target Objective & Reference Standard")
        $meta.outputs_to = @("Verified Production Artifact")
    }
    elseif ($relPath -like "skills/greenfield_routing/*") {
        $meta.function = "Exploratory Intelligence Board router for uninitialized domains"
        $meta.timing = "Invoked at project initiation when zero documentation exists"
        $meta.location = "Skills (skills/greenfield_routing/)"
        $meta.rationale = "Employs clean-context sub-agents as personal cognitive Google"
        $meta.methodology = "Multi-vector hypothesis stress-testing and skill/rule synthesis"
        $meta.objectives = "Bootstrap corporate structure and custom skills from pure insights"
        $meta.inputs_from = @("Raw User Concept")
        $meta.outputs_to = @("Corporate Charter & Skill Packs")
    }
    elseif ($relPath -like "skills/dept_*") {
        $deptName = $relPath.Split("/\")[1]
        $meta.function = "Departmental skill pack for $deptName"
        $meta.timing = "Invoked by Department Manager during corresponding pipeline stage"
        $meta.location = "Skills ($relPath)"
        $meta.rationale = "Encapsulates specialized domain runbooks and employee profiles"
        $meta.methodology = "Recursive clean-context sub-agent delegation"
        $meta.objectives = "Produce domain-specific deliverables with zero context bloat"
        $meta.inputs_from = @("Departmental Directive")
        $meta.outputs_to = @("Stage Deliverable Artifact")
    }
    elseif ($relPath -like "scripts/hooks/*") {
        $meta.function = "Lifecycle enforcement hook script"
        $meta.timing = "Executed by Antigravity IDE engine at lifecycle events"
        $meta.location = "Scripts (scripts/hooks/)"
        $meta.rationale = "Provides external deterministic gating outside model inference"
        $meta.methodology = "JSON stdin/stdout pipeline contract"
        $meta.objectives = "Enforce state injection, density auditing, and stop-gating"
        $meta.inputs_from = @("IDE Process via stdin")
        $meta.outputs_to = @("IDE Engine via stdout")
    }
    elseif ($relPath -like "scripts/*") {
        $meta.function = "Operational automation and pipeline orchestration engine"
        $meta.timing = "Executed during automated workflows and testing"
        $meta.location = "Scripts (scripts/)"
        $meta.rationale = "Provides reliable, deterministic CLI automation for ecosystem tasks"
        $meta.methodology = "PowerShell 7+ idempotent automation scripts"
        $meta.objectives = "Automate state sync, gauntlet runs, and validation suites"
        $meta.inputs_from = @(".state/ Data Models")
        $meta.outputs_to = @(".state/ledger/ Transactions")
    }

    return $meta
}

# Scan workspace files (polyglot coverage)
$trackedExtensions = @("*.json", "*.md", "*.ps1", "*.py", "*.yaml", "*.yml", "*.rs", "*.go", "*.ts", "*.tsx", "*.js", "*.jsx", "*.java", "*.cpp", "*.c", "*.cs", "*.sql", "*.html", "*.css", "*.sh")
$files = Get-ChildItem -Path $rootDir -Recurse -File -Include $trackedExtensions | 
    Where-Object { 
        $_.FullName -notmatch "\\\.git\\" -and 
        $_.FullName -notmatch "\\\.system_generated\\" -and 
        $_.FullName -notmatch "\\node_modules\\" -and
        $_.FullName -notmatch "\\target\\" -and
        $_.FullName -notmatch "\\vendor\\" -and
        $_.FullName -notmatch "\\dist\\" -and
        $_.FullName -notmatch "\\build\\" -and
        $_.FullName -notmatch "\\__pycache__\\" -and
        $_.FullName -notmatch "\\\.venv\\"
    }


foreach ($f in $files) {
    $rel = $f.FullName.Substring($rootDir.Length + 1).Replace("\", "/")
    if ($map.components.ContainsKey($rel)) {
        # Preserve user-customized fields, update timestamp
        $map.components[$rel].last_updated = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
    } else {
        $map.components[$rel] = Get-DefaultMetadata $rel
    }
}

# Manual parameter override if passed
if ($FilePath -and $map.components.ContainsKey($FilePath)) {
    if ($Status) { $map.components[$FilePath].status = $Status }
    if ($Function) { $map.components[$FilePath].function = $Function }
    if ($Rationale) { $map.components[$FilePath].rationale = $Rationale }
    if ($DataOrigin) { $map.components[$FilePath].inputs_from = @($DataOrigin) }
    if ($DataDest) { $map.components[$FilePath].outputs_to = @($DataDest) }
    $map.components[$FilePath].last_updated = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
    Write-Host "[NEURAL MAP OVERRIDE] Updated metadata for $FilePath"
}

$map.total_components = $map.components.Count
$map.last_synced = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")

# Write updated neural map JSON
$map | ConvertTo-Json -Depth 6 | Set-Content -Path $mapFile -Encoding UTF8
Write-Host "[NEURAL MAP UPDATED] Synced $($map.total_components) components into .state/neural_map.json"

# Generate readable project_context.md
$md = @"
# Project Neural Knowledge Map & Operational Context

**Project**: $($map.project_name)  
**Last Synced**: $($map.last_synced)  
**Active Components**: $($map.total_components)  

---

## 1. System Topology & Component Registry

| Component Path | Function & Role | Timing & Lifecycle | Data Flow (In $\to$ Out) | Status |
| :--- | :--- | :--- | :--- | :--- |
"@

$b = [char]96
foreach ($key in ($map.components.Keys | Sort-Object)) {
    $c = $map.components[$key]
    $filePath = if ($c.file_path) { $c.file_path } else { $c['file_path'] }
    $status = if ($c.status) { $c.status } else { $c['status'] }
    $func = if ($c.function) { $c.function } else { $c['function'] }
    $timing = if ($c.timing) { $c.timing } else { $c['timing'] }
    $in = ($c.inputs_from -join ", ")
    $out = ($c.outputs_to -join ", ")
    $md += "`n| **$b$filePath$b** | $func | $timing | $in -> $out | $b$status$b |"
}

$md += "`n`n---`n`n## 2. Component Deep Dive: Rationale & Methodology`n"

foreach ($key in ($map.components.Keys | Sort-Object)) {
    $c = $map.components[$key]
    $filePath = if ($c.file_path) { $c.file_path } else { $c['file_path'] }
    $status = if ($c.status) { $c.status } else { $c['status'] }
    $func = if ($c.function) { $c.function } else { $c['function'] }
    $loc = if ($c.location) { $c.location } else { $c['location'] }
    $updated = if ($c.last_updated) { $c.last_updated } else { $c['last_updated'] }
    $rationale = if ($c.rationale) { $c.rationale } else { $c['rationale'] }
    $methodology = if ($c.methodology) { $c.methodology } else { $c['methodology'] }
    $objectives = if ($c.objectives) { $c.objectives } else { $c['objectives'] }
    $in = ($c.inputs_from -join ", ")
    $out = ($c.outputs_to -join ", ")

    $md += "`n`n### Component: $b$filePath$b"
    $md += "`n- **Location**: $loc | **Status**: $b$status$b | **Updated**: $updated"
    $md += "`n- **Primary Function**: $func"
    $md += "`n- **Design Rationale**: $rationale"
    $md += "`n- **Methodology & Pattern**: $methodology"
    $md += "`n- **Specific Objectives**: $objectives"
    $md += "`n- **Data Flow Dependencies**:"
    $md += "`n  - *Inputs From*: $in"
    $md += "`n  - *Outputs To*: $out"
    $md += "`n`n---`n"
}

$md | Set-Content -Path $contextFile -Encoding UTF8
Write-Host "[CONTEXT SYNCHRONIZED] Generated live operational briefing: .state/project_context.md"

# Log to ledger
& powershell -ExecutionPolicy Bypass -File $stateScript -Action log-event -Initiator "Neural Map Engine" -EventType "NEURAL_MAP_SYNC" -Description "Synchronized $($map.total_components) architectural components into persistent neural map and project context." | Out-Null
