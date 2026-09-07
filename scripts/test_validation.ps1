$rootDir = Split-Path $PSScriptRoot -Parent
$jsonFiles = Get-ChildItem -Path $rootDir -Recurse -Filter *.json | 
    Where-Object { $_.FullName -notmatch "\\\.state\\backups\\" -and $_.FullName -notmatch "\\\.git\\" }
$allPass = $true

Write-Host "--- VALIDATING JSON FILES & RFC 8259 (NO BOM) ---"
foreach ($f in $jsonFiles) {
    try {
        $bytes = [System.IO.File]::ReadAllBytes($f.FullName)
        if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
            Write-Host "  [FAIL] $($f.Name): Contains invalid UTF-8 BOM" -ForegroundColor Red
            $allPass = $false
            continue
        }
        $content = Get-Content $f.FullName -Raw | ConvertFrom-Json
        Write-Host "  [OK] $($f.Name)"
    } catch {
        Write-Host "  [FAIL] $($f.Name): $_" -ForegroundColor Red
        $allPass = $false
    }
}

Write-Host "`n--- VALIDATING MODULAR NEURAL LAYER CHAIN (rules/*.md) ---"
$rulesDir = Join-Path $rootDir "rules"
$ruleFiles = Get-ChildItem -Path $rulesDir -File -Filter *.md

# Rule 1: Total count must be <= 14 to prevent Antigravity 15-rule discovery drop
if ($ruleFiles.Count -le 14 -and $ruleFiles.Count -ge 8) {
    Write-Host "  [OK] rules/ contains $($ruleFiles.Count) rule files (strictly <= 14; safe margin under 15-rule cap)."
} else {
    Write-Host "  [FAIL] rules/ contains $($ruleFiles.Count) rule files (must be between 8 and 14 files)!" -ForegroundColor Red
    $allPass = $false
}

# Rule 2: AGENTS.md must exist as Layer 0 Master Constitutional Kernel
$agentsPath = Join-Path $rulesDir "AGENTS.md"
if (Test-Path $agentsPath) {
    Write-Host "  [OK] rules/AGENTS.md exists as Layer 0 Sovereign Constitutional Kernel."
} else {
    Write-Host "  [FAIL] rules/AGENTS.md missing!" -ForegroundColor Red
    $allPass = $false
}

# Rule 3: Every rule file must be calibrated [10 KB, 17.5 KB] and have no UTF-8 BOM
foreach ($rf in $ruleFiles) {
    $bytes = [System.IO.File]::ReadAllBytes($rf.FullName)
    $hasBom = ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF)
    $size = $rf.Length

    if ($hasBom) {
        Write-Host "  [FAIL] $($rf.Name): Contains UTF-8 BOM!" -ForegroundColor Red
        $allPass = $false
    }

    # Calibrated window: 10 KB (10240 bytes) to 17.5 KB (17920 bytes)
    if ($size -ge 10240 -and $size -le 17920) {
        Write-Host "  [OK] $($rf.Name) size is $size bytes (calibrated within [10.0 KB, 17.5 KB])."
    } else {
        Write-Host "  [FAIL] $($rf.Name) size is $size bytes (must be between 10240 and 17920 bytes)!" -ForegroundColor Red
        $allPass = $false
    }

    $content = Get-Content $rf.FullName -Raw
    if ($content -match "trigger:\s*(always_on|model_decision)") {
        Write-Host "  [OK] $($rf.Name) has valid YAML trigger frontmatter."
    } else {
        Write-Host "  [FAIL] $($rf.Name) missing valid YAML trigger frontmatter!" -ForegroundColor Red
        $allPass = $false
    }
}

Write-Host "`n--- VALIDATING NEURAL MAP INTEGRITY ---"
$mapPath = Join-Path $rootDir ".state\neural_map.json"
if (Test-Path $mapPath) {
    $mapData = Get-Content $mapPath -Raw | ConvertFrom-Json
    $backupKeys = @()
    foreach ($prop in $mapData.components.PSObject.Properties) {
        if ($prop.Name -match "backup") { $backupKeys += $prop.Name }
    }
    if ($backupKeys.Count -eq 0) {
        Write-Host "  [OK] neural_map.json contains 0 backup files ($($mapData.total_components) active components)."
    } else {
        Write-Host "  [FAIL] neural_map.json contains $($backupKeys.Count) backup components!" -ForegroundColor Red
        $allPass = $false
    }
}

Write-Host "`n--- TESTING LIFECYCLE HOOKS ---"
$mockInput = @{
    conversationId = "test-conv-001"
    stepIdx = 1
    invocationNum = 1
    workspacePaths = @($rootDir)
} | ConvertTo-Json -Compress

# Test Pre-Invocation
try {
    $preOut = $mockInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\pre_invocation.ps1"
    $preJson = $preOut | ConvertFrom-Json
    if ($preJson.injectSteps.Count -gt 0) {
        Write-Host "  [OK] pre_invocation.ps1 produced valid injection steps."
    } else {
        Write-Host "  [WARN] pre_invocation.ps1 output had 0 injection steps."
    }
} catch {
    Write-Host "  [FAIL] pre_invocation.ps1 failed: $_" -ForegroundColor Red
    $allPass = $false
}

# Test Post-Invocation
try {
    $postOut = $mockInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\post_invocation.ps1"
    $postJson = $postOut | ConvertFrom-Json
    Write-Host "  [OK] post_invocation.ps1 produced valid response: $($postJson.terminationBehavior)"
} catch {
    Write-Host "  [FAIL] post_invocation.ps1 failed: $_" -ForegroundColor Red
    $allPass = $false
}

# Test Stop Gate
try {
    $stopOut = $mockInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\stop_gate.ps1"
    $stopJson = $stopOut | ConvertFrom-Json
    Write-Host "  [OK] stop_gate.ps1 produced valid decision: $($stopJson.decision)"
} catch {
    Write-Host "  [FAIL] stop_gate.ps1 failed: $_" -ForegroundColor Red
    $allPass = $false
}

Write-Host "`n--- TESTING DYNAMIC HARDENED SCRIPTS ON REAL DISK FILES ---"
# Test Devil's Apple dynamic scanner
try {
    $appleOut = powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\run_devils_apple.ps1" -TargetFile "$PSScriptRoot\sync_state.ps1"
    if ($LASTEXITCODE -eq 0 -and (Test-Path (Join-Path $rootDir ".state\devils_apple_latest.json"))) {
        Write-Host "  [OK] run_devils_apple.ps1 executed dynamic scan successfully."
    } else {
        Write-Host "  [FAIL] run_devils_apple.ps1 exited with code $LASTEXITCODE" -ForegroundColor Red
        $allPass = $false
    }
} catch {
    Write-Host "  [FAIL] run_devils_apple.ps1 threw error: $_" -ForegroundColor Red
    $allPass = $false
}

# Test Devil's Advocate dynamic supervisor
try {
    $advOut = powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\run_devils_advocate.ps1" -TargetDeliverable "$PSScriptRoot\sync_state.ps1" -MaxRounds 2
    if ($LASTEXITCODE -eq 0 -and (Test-Path (Join-Path $rootDir ".state\devils_advocate_latest.json"))) {
        Write-Host "  [OK] run_devils_advocate.ps1 executed dynamic supervisory audit successfully."
    } else {
        Write-Host "  [FAIL] run_devils_advocate.ps1 exited with code $LASTEXITCODE" -ForegroundColor Red
        $allPass = $false
    }
} catch {
    Write-Host "  [FAIL] run_devils_advocate.ps1 threw error: $_" -ForegroundColor Red
    $allPass = $false
}

# Test Dimension Expansion dynamic engine
try {
    $dimOut = powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\expand_dimensions.ps1" -RootConcept "Autonomous Cognitive Multi-Agent Architecture" -DomainCategory "Autonomous Cybernetic Multi-Agent Governance & Cognitive Systems"
    if ($LASTEXITCODE -eq 0 -and (Test-Path (Join-Path $rootDir ".state\dimension_expansion_latest.json"))) {
        Write-Host "  [OK] expand_dimensions.ps1 executed 4-tier dynamic expansion successfully."
    } else {
        Write-Host "  [FAIL] expand_dimensions.ps1 exited with code $LASTEXITCODE" -ForegroundColor Red
        $allPass = $false
    }
} catch {
    Write-Host "  [FAIL] expand_dimensions.ps1 threw error: $_" -ForegroundColor Red
    $allPass = $false
}

if ($allPass) {
    Write-Host "`n[SUCCESS] All plugin files, modular rules, dynamic scripts, and hooks verified successfully!"
    exit 0
} else {
    Write-Host "`n[FAILURE] Some checks failed."
    exit 1
}
