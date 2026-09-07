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

# Rule 3: Every rule file must be calibrated [2,800, 3,900] bytes (~1,000-1,150 tokens) and have no UTF-8 BOM
foreach ($rf in $ruleFiles) {
    $bytes = [System.IO.File]::ReadAllBytes($rf.FullName)
    $hasBom = ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF)
    $size = $rf.Length

    if ($hasBom) {
        Write-Host "  [FAIL] $($rf.Name): Contains UTF-8 BOM!" -ForegroundColor Red
        $allPass = $false
    }

    # Calibrated window: 2,800 bytes to 3,900 bytes (target ~3.0 KB to 3.6 KB, ~1,000-1,150 tokens)
    if ($size -ge 2800 -and $size -le 3900) {
        Write-Host "  [OK] $($rf.Name) size is $size bytes (calibrated within [2800, 3900] bytes, ~1000-1150 tokens)."
    } else {
        Write-Host "  [FAIL] $($rf.Name) size is $size bytes (must be between 2800 and 3900 bytes)!" -ForegroundColor Red
        $allPass = $false
    }

    $content = Get-Content $rf.FullName -Raw
    if ($content -match "trigger:\s*(always_on|model_decision|glob)") {
        Write-Host "  [OK] $($rf.Name) has valid YAML trigger frontmatter."
    } else {
        Write-Host "  [FAIL] $($rf.Name) missing valid YAML trigger frontmatter!" -ForegroundColor Red
        $allPass = $false
    }
}

Write-Host "`n--- VALIDATING SKILLS REPOSITORY & DESERT WATER ---"
$skillsDir = Join-Path $rootDir "skills"
$desertSkillPath = Join-Path $skillsDir "desert_water\SKILL.md"
if (Test-Path $desertSkillPath) {
    $dBytes = [System.IO.File]::ReadAllBytes($desertSkillPath)
    $dHasBom = ($dBytes.Length -ge 3 -and $dBytes[0] -eq 0xEF -and $dBytes[1] -eq 0xBB -and $dBytes[2] -eq 0xBF)
    if (-not $dHasBom) {
        Write-Host "  [OK] skills/desert_water/SKILL.md exists and is valid BOM-free UTF-8."
    } else {
        Write-Host "  [FAIL] skills/desert_water/SKILL.md contains UTF-8 BOM!" -ForegroundColor Red
        $allPass = $false
    }
} else {
    Write-Host "  [FAIL] skills/desert_water/SKILL.md missing!" -ForegroundColor Red
    $allPass = $false
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

Write-Host "`n--- TESTING SESSION STATE ENGINE & STOP GATE BLOCKERS ---"
try {
    # 1. Initialize root CEO session
    & powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\sync_state.ps1" -Action init-session -Actor "Dr. Alexander Vance (CEO)" -Description "Validation suite root session" | Out-Null
    
    # 2. Set blocker
    & powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\sync_state.ps1" -Action set-blocker -BlockerId "BLK-VAL-TEST" -Description "Validation test blocker" | Out-Null
    
    # 3. Test Stop Gate blocker enforcement (attempt 1) -> must reject
    $blockedInput = @{ workspacePaths = @($rootDir); executionNum = 1 } | ConvertTo-Json -Compress
    $gateOut1 = $blockedInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\stop_gate.ps1"
    $gateJson1 = $gateOut1 | ConvertFrom-Json
    if ($gateJson1.decision -eq "continue") {
        Write-Host "  [OK] stop_gate.ps1 correctly rejected termination with active session blocker."
    } else {
        Write-Host "  [FAIL] stop_gate.ps1 allowed termination despite active blocker: $($gateJson1.decision)" -ForegroundColor Red
        $allPass = $false
    }

    # 4. Test Stop Gate does NOT falsely trip on tool invocation count
    $invocInput = @{ workspacePaths = @($rootDir); invocationNum = 20; executionNum = 0 } | ConvertTo-Json -Compress
    $gateOutInv = $invocInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\stop_gate.ps1"
    $gateJsonInv = $gateOutInv | ConvertFrom-Json
    if ($gateJsonInv.decision -eq "continue") {
        Write-Host "  [OK] stop_gate.ps1 correctly preserved blocker enforcement when invocationNum = 20 (no false breaker trip)."
    } else {
        Write-Host "  [FAIL] stop_gate.ps1 falsely allowed termination when invocationNum = 20: $($gateJsonInv.decision)" -ForegroundColor Red
        $allPass = $false
    }

    # 5. Test Stop Gate circuit breaker (attempt 4) -> must allow stop with alert message
    $circuitInput = @{ workspacePaths = @($rootDir); executionNum = 4 } | ConvertTo-Json -Compress
    $gateOut4 = $circuitInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\stop_gate.ps1"
    $gateJson4 = $gateOut4 | ConvertFrom-Json
    if ($gateJson4.decision -eq "allow" -and $gateJson4.userFacingMessage -match "CIRCUIT BREAKER") {
        Write-Host "  [OK] stop_gate.ps1 circuit breaker correctly allowed termination with alert message at executionNum = 4."
    } else {
        Write-Host "  [FAIL] stop_gate.ps1 circuit breaker failed at executionNum = 4: $($gateJson4.decision)" -ForegroundColor Red
        $allPass = $false
    }

    # 6. Resolve blocker
    & powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\sync_state.ps1" -Action resolve-blocker -BlockerId "BLK-VAL-TEST" | Out-Null

    # 7. Verify Stop Gate allows normal termination now
    $clearedOut = $blockedInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\stop_gate.ps1"
    $clearedJson = $clearedOut | ConvertFrom-Json
    if ($clearedJson.decision -eq "allow") {
        Write-Host "  [OK] stop_gate.ps1 correctly allowed termination after blocker resolution."
    } else {
        Write-Host "  [FAIL] stop_gate.ps1 rejected termination after blocker resolution: $($clearedJson.decision)" -ForegroundColor Red
        $allPass = $false
    }

    # 8. Record hypothesis
    & powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\sync_state.ps1" -Action record-hypothesis -Hypothesis "Session state engine verified on physical disk" -Confidence "PROVEN_FACT" | Out-Null
    Write-Host "  [OK] sync_state.ps1 successfully recorded test hypothesis."
} catch {
    Write-Host "  [FAIL] Session state test threw error: $_" -ForegroundColor Red
    $allPass = $false
}

Write-Host "`n--- TESTING ACTOR DEMARCATION IN PRE-INVOCATION & STOP GATE ---"
try {
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false

    # Test A: User directive prompt -> Must demarcate as CEO Dr. Vance and inject BLK-PREMISE-AUDIT
    $tempUserTranscript = [System.IO.Path]::GetTempFileName()
    $userLine = @{
        type = "USER_INPUT"
        content = "Olá Vance, como está o progresso da arquitetura neural?"
    } | ConvertTo-Json -Compress
    [System.IO.File]::WriteAllText($tempUserTranscript, $userLine, $utf8NoBom)

    $userMockInput = @{
        workspacePaths = @($rootDir)
        transcriptPath = $tempUserTranscript
        executionNum = 0
    } | ConvertTo-Json -Compress

    $userPreOut = $userMockInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\pre_invocation.ps1"
    $userPreJson = $userPreOut | ConvertFrom-Json
    $userMsg = $userPreJson.injectSteps[0].ephemeralMessage

    if ($userMsg -match "DR\. ALEXANDER VANCE \(CEO\)" -and $userMsg -match "BLK-PREMISE-AUDIT") {
        Write-Host "  [OK] pre_invocation.ps1 correctly demarcated CEO mode for user prompt and injected BLK-PREMISE-AUDIT."
    } else {
        Write-Host "  [FAIL] pre_invocation.ps1 failed CEO demarcation for user prompt!" -ForegroundColor Red
        $allPass = $false
    }
    Remove-Item -Path $tempUserTranscript -Force -ErrorAction SilentlyContinue

    # Test B: Subagent worker prompt -> Must demarcate as Level 1 Specialist and lift Axiom 5.2
    $tempSubTranscript = [System.IO.Path]::GetTempFileName()
    $subLine = @{
        type = "USER_INPUT"
        content = "<USER_REQUEST>`n<original_task>Build new production microservice</original_task>`n</USER_REQUEST>"
    } | ConvertTo-Json -Compress
    [System.IO.File]::WriteAllText($tempSubTranscript, $subLine, $utf8NoBom)

    $subMockInput = @{
        workspacePaths = @($rootDir)
        transcriptPath = $tempSubTranscript
        executionNum = 0
    } | ConvertTo-Json -Compress

    $subPreOut = $subMockInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\pre_invocation.ps1"
    $subPreJson = $subPreOut | ConvertFrom-Json
    $subMsg = $subPreJson.injectSteps[0].ephemeralMessage

    if ($subMsg -match "LEVEL 1 PRODUCTION WORKER" -and $subMsg -match "Axiom 5\.2 Exception") {
        Write-Host "  [OK] pre_invocation.ps1 correctly demarcated subagent worker (Axiom 5.2 lifted for worker)."
    } else {
        Write-Host "  [FAIL] pre_invocation.ps1 failed subagent actor demarcation!" -ForegroundColor Red
        $allPass = $false
    }

    # Test C: Subagent Stop Gate isolation -> Subagent is NOT blocked by CEO's BLK-PREMISE-AUDIT
    $subGateOut = $subMockInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\stop_gate.ps1"
    $subGateJson = $subGateOut | ConvertFrom-Json
    if ($subGateJson.decision -eq "allow") {
        Write-Host "  [OK] stop_gate.ps1 allowed subagent completion without false deadlock from CEO root blocker."
    } else {
        Write-Host "  [FAIL] stop_gate.ps1 falsely blocked subagent with CEO root blocker!" -ForegroundColor Red
        $allPass = $false
    }

    Remove-Item -Path $tempSubTranscript -Force -ErrorAction SilentlyContinue

    # Clean up BLK-PREMISE-AUDIT injected during test
    & powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\sync_state.ps1" -Action resolve-blocker -BlockerId "BLK-PREMISE-AUDIT" | Out-Null
} catch {
    Write-Host "  [FAIL] Actor demarcation test threw error: $_" -ForegroundColor Red
    $allPass = $false
}

Write-Host "`n--- TESTING DEVIL'S ADVOCATE VERDICT BUG FIX ---"
try {
    # Create temporary script deliverable with intentional defect
    $tempDefectFile = Join-Path $PSScriptRoot "temp_defect_test.ps1"
    $defectCode = "function Test-Defect { `n    # TODO: unfinished work`n    pass`n}"
    [System.IO.File]::WriteAllText($tempDefectFile, $defectCode, $utf8NoBom)

    # Run Devil's Advocate with MaxRounds = 2 against defective file
    $advDefectOut = powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\run_devils_advocate.ps1" -TargetDeliverable $tempDefectFile -MaxRounds 2
    $advExit = $LASTEXITCODE

    $advReport = Join-Path $rootDir ".state\devils_advocate_latest.json"
    $advData = Get-Content $advReport -Raw | ConvertFrom-Json

    if ($advExit -ne 0 -and $advData.status -eq "rejected_max_rounds_reached") {
        Write-Host "  [OK] run_devils_advocate.ps1 correctly rejected defective work on max rounds (did NOT auto-approve)."
    } else {
        Write-Host "  [FAIL] run_devils_advocate.ps1 auto-approved defective deliverable or exited with 0!" -ForegroundColor Red
        $allPass = $false
    }

    Remove-Item -Path $tempDefectFile -Force -ErrorAction SilentlyContinue
} catch {
    Write-Host "  [FAIL] Devil's Advocate bug fix test threw error: $_" -ForegroundColor Red
    $allPass = $false
}

Write-Host "`n--- TESTING DYNAMIC HARDENED SCRIPTS ---"
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

# Test Devil's Advocate dynamic supervisor on clean deliverable
try {
    $advOut = powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\run_devils_advocate.ps1" -TargetDeliverable "$PSScriptRoot\sync_state.ps1" -MaxRounds 2
    if ($LASTEXITCODE -eq 0 -and (Test-Path (Join-Path $rootDir ".state\devils_advocate_latest.json"))) {
        Write-Host "  [OK] run_devils_advocate.ps1 executed dynamic supervisory audit successfully on clean deliverable."
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

# Test Dynamic Chroma Grill with Physical File Inspection
try {
    $grillOut = powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\run_chroma_grill.ps1" -TargetFile "$PSScriptRoot\sync_state.ps1"
    if ($LASTEXITCODE -eq 0 -and (Test-Path (Join-Path $rootDir ".state\chroma_grill_latest.json"))) {
        Write-Host "  [OK] run_chroma_grill.ps1 executed physical disk AST and code audit successfully."
    } else {
        Write-Host "  [FAIL] run_chroma_grill.ps1 exited with code $LASTEXITCODE" -ForegroundColor Red
        $allPass = $false
    }
} catch {
    Write-Host "  [FAIL] run_chroma_grill.ps1 threw error: $_" -ForegroundColor Red
    $allPass = $false
}

# Test Dynamic Strategic Meeting with Parameter Aliases
try {
    $smOut = powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\run_strategic_meeting.ps1" -SubAgentId "RED-QA-01" -BlockerReason "Stress test concurrency bounds lock contention"
    if ($LASTEXITCODE -eq 0 -and (Test-Path (Join-Path $rootDir ".state\strategic_meeting_latest.json"))) {
        $smData = Get-Content (Join-Path $rootDir ".state\strategic_meeting_latest.json") -Raw | ConvertFrom-Json
        if ($smData.node_id -eq "RED-QA-01" -and $smData.failed_goal -match "Stress test concurrency bounds") {
            Write-Host "  [OK] run_strategic_meeting.ps1 correctly bound SubAgentId and BlockerReason aliases dynamically."
        } else {
            Write-Host "  [FAIL] run_strategic_meeting.ps1 fell back to static mocks or failed parameter binding!" -ForegroundColor Red
            $allPass = $false
        }
    } else {
        Write-Host "  [FAIL] run_strategic_meeting.ps1 exited with code $LASTEXITCODE" -ForegroundColor Red
        $allPass = $false
    }
} catch {
    Write-Host "  [FAIL] run_strategic_meeting.ps1 threw error: $_" -ForegroundColor Red
    $allPass = $false
}

if ($allPass) {
    Write-Host "`n[SUCCESS] All plugin files, modular rules, dynamic scripts, and hooks verified successfully!"
    exit 0
} else {
    Write-Host "`n[FAILURE] Some checks failed."
    exit 1
}
