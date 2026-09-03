# Post-Invocation Hook: Audits model execution density and checks for satisficing defects
$rawInput = if ([Console]::IsInputRedirected) { [Console]::In.ReadToEnd() } else { "" }


$response = @{
    injectSteps = @()
    terminationBehavior = ""
}

try {
    if ($rawInput) {
        $data = $rawInput | ConvertFrom-Json
        $transcriptPath = $data.transcriptPath
        
        # If transcript exists, inspect the latest step for critical satisficing violations
        if ($transcriptPath -and (Test-Path $transcriptPath)) {
            $lastLine = Get-Content $transcriptPath -Tail 1
            if ($lastLine) {
                $banned = @("// TODO", "/* TODO */", "/* FIXME */", "implement later", "left as an exercise")
                foreach ($b in $banned) {
                    if ($lastLine -match [regex]::Escape($b)) {
                        $response.injectSteps = @(
                            @{
                                ephemeralMessage = "[SUPERVISOR WARNING: ANTI-SATISFICING INVARIANT VIOLATION] Detected banned pattern '$b'. You must fully implement all code and remove all placeholders."
                            }
                        )
                        break
                    }
                }
            }
        }
    }
} catch {
    # Non-blocking error handling
}

$response | ConvertTo-Json -Depth 5 -Compress
