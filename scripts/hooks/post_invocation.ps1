# Post-Invocation Hook: Audits modified code files on disk for satisficing defects
$rawInput = if ([Console]::IsInputRedirected) { [Console]::In.ReadToEnd() } else { "" }

$response = @{
    injectSteps = @()
    terminationBehavior = ""
}

try {
    $rootDir = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
    Push-Location $rootDir
    try {
        $diffLines = git diff -U0 -- "*.py" "*.ts" "*.js" "*.rs" "*.go" "*.cs" "*.cpp" "*.c" "*.java" "*.ps1" 2>$null
        if ($diffLines) {
            $bannedPatterns = @(
                '^\+\s*//\s*TODO',
                '^\+\s*/\*\s*TODO',
                '^\+\s*/\*\s*FIXME',
                '^\+\s*#\s*TODO',
                '^\+\s*pass\s*$'
            )
            foreach ($line in $diffLines) {
                foreach ($pattern in $bannedPatterns) {
                    if ($line -match $pattern) {
                        $response.injectSteps = @(
                            @{
                                ephemeralMessage = "[SUPERVISOR WARNING: ANTI-SATISFICING DEFECT DETECTED] Added placeholder pattern in code: '$line'. You must fully implement all operational logic and remove placeholders."
                            }
                        )
                        break
                    }
                }
                if ($response.injectSteps.Count -gt 0) { break }
            }
        }
    } finally {
        Pop-Location
    }
} catch {
    # Non-blocking error handling
}

$response | ConvertTo-Json -Depth 5 -Compress
