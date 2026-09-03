$jsonFiles = Get-ChildItem -Path $PSScriptRoot\.. -Recurse -Filter *.json
$allPass = $true

Write-Host "--- VALIDATING JSON FILES ---"
foreach ($f in $jsonFiles) {
    try {
        $content = Get-Content $f.FullName -Raw | ConvertFrom-Json
        Write-Host "  [OK] $($f.Name)"
    } catch {
        Write-Host "  [FAIL] $($f.Name): $_"
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
