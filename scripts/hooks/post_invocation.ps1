# Post-Invocation Hook: Audits modified code files on disk for satisficing defects
$rawInput = if ([Console]::IsInputRedirected) { [Console]::In.ReadToEnd() } else { "" }

$response = @{
    injectSteps = @()
    terminationBehavior = ""
}

try {
    $pluginDir = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
    $inputObj = $null
    if ($rawInput) {
        try { $inputObj = $rawInput | ConvertFrom-Json } catch { }
    }
    $workspaceDir = if ($inputObj -and $inputObj.workspacePaths -and $inputObj.workspacePaths.Count -gt 0) { $inputObj.workspacePaths[0] } else { $pluginDir }

    if (Test-Path $workspaceDir) {
        Push-Location $workspaceDir
    try {
        $hasHead = git rev-parse --verify HEAD 2>$null
        $diffLines = if ($hasHead) {
            git diff HEAD -U0 -- "*.py" "*.ts" "*.js" "*.rs" "*.go" "*.cs" "*.cpp" "*.c" "*.java" "*.ps1" 2>$null
        } else {
            git diff -U0 -- "*.py" "*.ts" "*.js" "*.rs" "*.go" "*.cs" "*.cpp" "*.c" "*.java" "*.ps1" 2>$null
        }

        $bannedPatterns = @(
            '^\+\s*//\s*TODO',
            '^\+\s*/\*\s*TODO',
            '^\+\s*/\*\s*FIXME',
            '^\+\s*#\s*TODO',
            '^\+\s*pass\s*$'
        )

        if ($diffLines) {
            foreach ($line in $diffLines) {
                foreach ($pattern in $bannedPatterns) {
                    if ($line -match $pattern) {
                        $response.injectSteps = @(
                            @{
                                ephemeralMessage = "[SUPERVISOR WARNING: ANTI-SATISFICING DEFECT DETECTED] Added placeholder pattern in code: '$line'. You must fully implement all operational logic and remove placeholders."
                            }
                        )
                        $response.terminationBehavior = "force_continue"
                        break
                    }
                }
                if ($response.injectSteps.Count -gt 0) { break }
            }
        }

        # Also inspect untracked code files if no staged/unstaged defect found yet
        if ($response.injectSteps.Count -eq 0) {
            $untracked = git ls-files --others --exclude-standard -- "*.py" "*.ts" "*.js" "*.rs" "*.go" "*.cs" "*.cpp" "*.c" "*.java" "*.ps1" 2>$null
            if ($untracked) {
                $rawBanned = @('//\s*TODO', '/\*\s*TODO', '/\*\s*FIXME', '#\s*TODO', '^\s*pass\s*$')
                foreach ($uFile in $untracked) {
                    if (Test-Path $uFile) {
                        $lines = Get-Content $uFile
                        foreach ($uLine in $lines) {
                            foreach ($rb in $rawBanned) {
                                if ($uLine -match $rb) {
                                    $response.injectSteps = @(
                                        @{
                                            ephemeralMessage = "[SUPERVISOR WARNING: ANTI-SATISFICING DEFECT DETECTED] Placeholder in untracked file '$uFile': '$uLine'. You must fully implement all operational logic and remove placeholders."
                                        }
                                    )
                                    $response.terminationBehavior = "force_continue"
                                    break
                                }
                            }
                            if ($response.injectSteps.Count -gt 0) { break }
                        }
                    }
                    if ($response.injectSteps.Count -gt 0) { break }
                }
            }
        }
    } finally {
        Pop-Location
    }
}
} catch {
    # Non-blocking error handling
}

$response | ConvertTo-Json -Depth 5 -Compress
