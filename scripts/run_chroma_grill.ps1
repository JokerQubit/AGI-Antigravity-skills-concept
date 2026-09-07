[CmdletBinding()]
param(
    [string]$Initiator = "User",
    [Alias("Insight")]
    [string]$TargetInsight = "Use dynamic in-memory caching for all persistent state updates to maximize speed",
    [Alias("File", "Path")]
    [string]$TargetFile = "",
    [string]$OutputFile = ""
)

$rootDir = Split-Path -Parent $PSScriptRoot
$stateDir = Join-Path $rootDir ".state"
$stateScript = Join-Path $PSScriptRoot "sync_state.ps1"

# Check if target is a physical file on disk
$inspectedFile = $null
if ($TargetFile -and (Test-Path $TargetFile)) {
    $inspectedFile = (Resolve-Path $TargetFile).Path
} elseif (Test-Path $TargetInsight) {
    $inspectedFile = (Resolve-Path $TargetInsight).Path
} elseif (Test-Path (Join-Path $rootDir $TargetInsight)) {
    $inspectedFile = (Resolve-Path (Join-Path $rootDir $TargetInsight)).Path
}

Write-Host "================================================================="
Write-Host "       CHROMA HORIZON UNIVERSAL SOCRATIC GRILL ENGINE"
Write-Host "================================================================="
Write-Host "Initiating Node: $Initiator"
if ($inspectedFile) {
    Write-Host "Target Artifact: $inspectedFile (Physical Disk File)"
} else {
    Write-Host "Target Insight:  $TargetInsight"
}
Write-Host ""

Write-Host "[PHASE 1] Dispatched Socratic Inquisitor (SOC-GRILL-01)..." -ForegroundColor Cyan
Start-Sleep -Milliseconds 150

$controversies = @()

if ($inspectedFile) {
    $fileBytes = [System.IO.File]::ReadAllBytes($inspectedFile)
    $fileRaw = [System.Text.Encoding]::UTF8.GetString($fileBytes)
    $hasBom = ($fileBytes.Length -ge 3 -and $fileBytes[0] -eq 0xEF -and $fileBytes[1] -eq 0xBB -and $fileBytes[2] -eq 0xBF)
    $ext = [System.IO.Path]::GetExtension($inspectedFile).ToLower()

    if ($hasBom) {
        $controversies += @{
            controversy = "File contains UTF-8 Byte Order Mark (0xEF, 0xBB, 0xBF), violating Layer 0 and Layer 7 RFC 8259 hygiene."
            severity = "CRITICAL"
            hardened_alternative = "Strip UTF-8 BOM on physical write using '[System.Text.UTF8Encoding] `$false'."
        }
    }

    if ($fileRaw -match "(?i)\b(TODO|FIXME|HACK|stub)\b") {
        $controversies += @{
            controversy = "File contains unverified placeholder tokens (TODO/FIXME/stub) violating Zero-Stub Law."
            severity = "HIGH"
            hardened_alternative = "Eliminate all placeholders and author 100% operational production logic on physical disk."
        }
    }

    if ($ext -eq ".ps1") {
        $tokens = $null; $errors = $null
        $ast = [System.Management.Automation.Language.Parser]::ParseInput($fileRaw, [ref]$tokens, [ref]$errors)
        $emptyCatches = $ast.FindAll({ $args[0] -is [System.Management.Automation.Language.CatchClauseAst] -and $args[0].Body.Statements.Count -eq 0 }, $true)
        if ($emptyCatches) {
            $controversies += @{
                controversy = "PowerShell AST inspection detected $($emptyCatches.Count) empty catch block(s) silently swallowing errors."
                severity = "CRITICAL"
                hardened_alternative = "Implement structured error logging or explicit rethrow in all catch blocks."
            }
        }
    }

    if ($fileRaw -match "Set-Content|Out-File" -and $fileRaw -notmatch "tmp\.") {
        $controversies += @{
            controversy = "Direct in-place writes risk file corruption and partial NTFS state truncation during crash."
            severity = "HIGH"
            hardened_alternative = "Implement atomic swap file replacement ($path.tmp -> Move-Item -Force $path)."
        }
    }
}

# Dynamic Topic & Controversy Extraction from text
$insightLower = if ($inspectedFile) { "$TargetInsight $fileRaw".ToLower() } else { $TargetInsight.ToLower() }

if ($insightLower -match "\b(cache|caching|in-memory|memory|buffer|heap)\b") {
    $controversies += @{
        controversy = "Pure in-memory caching without a write-ahead log introduces high risk of catastrophic data loss on process crash or SIGKILL."
        severity = "CRITICAL"
        hardened_alternative = "Implement Write-Ahead Logging (WAL) with append-only ledger on disk, keeping an in-memory index for fast reads with zero data loss on crash."
    }
    $controversies += @{
        controversy = "Unbounded memory buffer can trigger Out-Of-Memory (OOM) fatal terminations under heavy load."
        severity = "HIGH"
        hardened_alternative = "Enforce LRU eviction policy with hard memory cap ($M_{\text{limit}} \le 64\text{MB}$) and deterministic paging to disk."
    }
}

if ($insightLower -match "\b(thread|concurr|lock|mutex|async|parallel|worker|task)\b") {
    $controversies += @{
        controversy = "Unsynchronized concurrent access to shared state triggers race conditions, dirty writes, and potential lock inversion deadlocks."
        severity = "CRITICAL"
        hardened_alternative = "Transition to lock-free channels, actor message passing, or mutex acquisition with mandatory 5000ms timeout fallbacks."
    }
}

if ($insightLower -match "\b(poll|polling|sleep|loop|wait)\b") {
    $controversies += @{
        controversy = "Naive sleep polling loops waste CPU cycles and introduce non-deterministic latency windows."
        severity = "HIGH"
        hardened_alternative = "Pair reactive event watchers with exponential backoff and explicit cancellation tokens."
    }
}

if ($insightLower -match "\b(network|socket|api|http|rpc|remote)\b") {
    $controversies += @{
        controversy = "Unbounded remote RPC calls without backpressure or circuit breakers cause phantom connection leaks and thread exhaustion."
        severity = "HIGH"
        hardened_alternative = "Implement token-bucket rate limiting with deterministic retry limits and circuit breaker fail-fast fallbacks."
    }
}

# Fallback general controversy if none specific matched
if ($controversies.Count -eq 0) {
    $controversies += @{
        controversy = "Presuming nominal happy-path execution without declaring formal boundary bounds risks silent corruption."
        severity = "HIGH"
        hardened_alternative = "Declare formal preconditions, postconditions, and invariant contracts with exhaustive error enumeration under Zero-Stub Law."
    }
    $controversies += @{
        controversy = "Unbounded state mutations without an append-only audit trail violate epistemic lineage and disaster recovery."
        severity = "MEDIUM"
        hardened_alternative = "Commit all state mutations through an append-only ledger with cryptographic hash chaining."
    }
}

$grillReport = @{
    initiator = $Initiator
    target_insight = $TargetInsight
    timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
    quadrants = @{
        q1_inquest = @(
            "Boundary Extremes: What are the deterministic failure modes when inputs to '$TargetInsight' are null, empty, negative, or at numeric capacity?",
            "Crash & Rollback: How does the system guarantee atomic recovery and prevent corrupted disk state if aborted abruptly mid-execution?",
            "Concurrency Integrity: What mechanism guarantees memory coherence and prevents race conditions during multi-agent concurrent operations?",
            "Resource Scalability: What is the formal asymptotic space/time bound $O(N)$ when '$TargetInsight' is subjected to sustained peak backpressure?"
        )
        q2_controversy_and_flaws = $controversies
        q3_novel_expansion = @(
            "OTP Supervision Trees: Enclose workers in hierarchical supervision trees with Erlang-style crash isolation and deterministic restart policies.",
            "Zero-Copy Memory-Mapped IO: Leverage memory-mapped files (mmap) or LMAX Disruptor ringbuffers to maximize throughput with zero garbage collection overhead.",
            "Cryptographic Audit Chaining: Bind all mutations into a SHA-256 append-only transaction ledger for deterministic forensic replay."
        )
        q4_aligned_synthesis = @{
            consensus_verdict = "Elevate '$TargetInsight' from naive formulation into a defensively bounded, transactionally durable architecture."
            implementation_directives = @(
                "Author strict interface contracts specifying defensive boundaries and non-null constraints.",
                "Enforce atomic persistence using temporary swap files and append-only ledger commits.",
                "Execute clean-context adversarial fuzz testing across nulls, extremes, and race hazards before production release."
            )
        }
    }
}

Write-Host "[Q1: MULTI-VECTOR INQUEST - PROBING BOUNDARIES]" -ForegroundColor White
foreach ($q in $grillReport.quadrants.q1_inquest) {
    Write-Host "  ? $q" -ForegroundColor Yellow
}

Write-Host "`n[Q2: CONTROVERSY & HARDENED ALTERNATIVES]" -ForegroundColor White
foreach ($cf in $grillReport.quadrants.q2_controversy_and_flaws) {
    Write-Host "  [CONTROVERSY] $($cf.controversy)" -ForegroundColor Red
    Write-Host "    -> Superior Alternative: $($cf.hardened_alternative)" -ForegroundColor Green
}

Write-Host "`n[Q3: NOVEL IDEA INOCULATION & EXPANSION]" -ForegroundColor White
foreach ($idea in $grillReport.quadrants.q3_novel_expansion) {
    Write-Host "  + $idea" -ForegroundColor Cyan
}

Write-Host "`n[Q4: COGNITIVE ALIGNMENT & SYNTHESIZED DIRECTIVES]" -ForegroundColor White
Write-Host "  Verdict: $($grillReport.quadrants.q4_aligned_synthesis.consensus_verdict)" -ForegroundColor Green
foreach ($dir in $grillReport.quadrants.q4_aligned_synthesis.implementation_directives) {
    Write-Host "    -> [DIRECTIVE] $dir"
}

$outFile = if ($OutputFile) { $OutputFile } else { Join-Path $stateDir "chroma_grill_latest.json" }
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
$jsonContent = $grillReport | ConvertTo-Json -Depth 6
$tempOut = "$outFile.tmp.$([System.Guid]::NewGuid().ToString('N'))"
[System.IO.File]::WriteAllText($tempOut, $jsonContent, $utf8NoBom)
Move-Item -Path $tempOut -Destination $outFile -Force
Write-Host "`n[SAVED] Socratic Grill Dossier recorded to: $outFile" -ForegroundColor Green

# Log to corporate ledger
if (Test-Path $stateScript) {
    & powershell -ExecutionPolicy Bypass -File $stateScript -Action log-event -Initiator "Socratic Inquisitor (SOC-GRILL-01)" -EventType "CHROMA_HORIZON_GRILL_EXEC" -Description "Executed dynamic Socratic Grill on insight from ${Initiator}: '$TargetInsight'. Highlighted $($controversies.Count) controversies and established aligned synthesis." | Out-Null
    Write-Host "[LEDGER LOGGED] Transaction committed to .state/ledger/" -ForegroundColor Green
}
