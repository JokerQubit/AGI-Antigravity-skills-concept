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

Write-Host "`n--- VALIDATING CONSTITUTIONAL KERNEL (rules/AGENTS.md) ---"
$rulesDir = Join-Path $rootDir "rules"
$ruleFiles = Get-ChildItem -Path $rulesDir -File
if ($ruleFiles.Count -eq 1 -and $ruleFiles[0].Name -eq "AGENTS.md") {
    Write-Host "  [OK] rules/ contains exactly AGENTS.md (15-rule discovery drop eliminated)."
} else {
    Write-Host "  [FAIL] rules/ does not contain solely AGENTS.md: $($ruleFiles.Name -join ', ')" -ForegroundColor Red
    $allPass = $false
}

$agentsPath = Join-Path $rulesDir "AGENTS.md"
$agentsBytes = (Get-Item $agentsPath).Length
if ($agentsBytes -ge 12500 -and $agentsBytes -le 16000) {
    Write-Host "  [OK] rules/AGENTS.md size is $agentsBytes bytes (strictly within [12.5 KB, 16.0 KB])."
} else {
    Write-Host "  [FAIL] rules/AGENTS.md size is $agentsBytes bytes (must be between 12500 and 16000 bytes)!" -ForegroundColor Red
    $allPass = $false
}

$agentsContent = Get-Content $agentsPath -Raw
if ($agentsContent -match "trigger:\s*always_on") {
    Write-Host "  [OK] rules/AGENTS.md has trigger: always_on."
} else {
    Write-Host "  [FAIL] rules/AGENTS.md missing trigger: always_on!" -ForegroundColor Red
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

Write-Host "`n--- TESTING LIFECYCLE HOOKS ---"
$mockInput = @{
    conversationId = "test-conv-001"
    stepIdx = 1
    invocationNum = 1
    workspacePaths = @("c:\Users\pichau\.gemini\config\plugins\agi-research")
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
    Write-Host "  [FAIL] pre_invocation.ps1 failed: $_"
    $allPass = $false
}

# Test Post-Invocation
try {
    $postOut = $mockInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\post_invocation.ps1"
    $postJson = $postOut | ConvertFrom-Json
    Write-Host "  [OK] post_invocation.ps1 produced valid response: $($postJson.terminationBehavior)"
} catch {
    Write-Host "  [FAIL] post_invocation.ps1 failed: $_"
    $allPass = $false
}

# Test Stop Gate
try {
    $stopOut = $mockInput | powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\hooks\stop_gate.ps1"
    $stopJson = $stopOut | ConvertFrom-Json
    Write-Host "  [OK] stop_gate.ps1 produced valid decision: $($stopJson.decision)"
} catch {
    Write-Host "  [FAIL] stop_gate.ps1 failed: $_"
    $allPass = $false
}

if ($allPass) {
    Write-Host "`n[SUCCESS] All plugin files and hooks verified successfully!"
    exit 0
} else {
    Write-Host "`n[FAILURE] Some checks failed."
    exit 1
}
