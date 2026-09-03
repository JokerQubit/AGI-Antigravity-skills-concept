param(
    [string]$Action = "status", # options: git-sync, create-snapshot, cleanup-clutter, status
    [string]$CommitMessage = "chore(matrix-reverse): continuous synchronization under Matrix Reverse standards",
    [string]$SnapshotName = "pre_test_stable",
    [switch]$Push
)

$rootDir = Split-Path -Parent $PSScriptRoot
$stateDir = Join-Path $rootDir ".state"
$backupDir = Join-Path $stateDir "backups"
$stateScript = Join-Path $PSScriptRoot "sync_state.ps1"

if (!(Test-Path $backupDir)) { New-Item -ItemType Directory -Path $backupDir -Force | Out-Null }

Write-Host "================================================================="
Write-Host "       MATRIX REVERSE REPO SYNC, SANDBOX & HYGIENE ENGINE"
Write-Host "================================================================="
Write-Host "Action:  $Action`n"

switch ($Action) {
    "git-sync" {
        Write-Host "[GIT SYNC] Initiating continuous versioning pipeline..." -ForegroundColor Cyan
        
        # Check if git is initialized
        $isGit = Test-Path (Join-Path $rootDir ".git")
        if ($isGit) {
            Write-Host "  -> Running 'git add .'..."
            git -C $rootDir add .
            
            Write-Host "  -> Committing with message: '$CommitMessage'..."
            git -C $rootDir commit -m "$CommitMessage"
            
            if ($Push) {
                Write-Host "  -> Pushing to remote tracking branch ('git push')..." -ForegroundColor Yellow
                git -C $rootDir push
            } else {
                Write-Host "  -> Local commit created. Use -Push to synchronize with remote."
            }
        } else {
            Write-Host "  [NOTICE] Git repository not detected in root directory. Staging commit in ledger." -ForegroundColor Yellow
        }

        & powershell -ExecutionPolicy Bypass -File $stateScript -Action log-event -Initiator "Matrix Reverse Sync" -EventType "GIT_SYNC_EXEC" -Description "Executed continuous synchronization: '$CommitMessage'." | Out-Null
        Write-Host "`n[GIT SYNC COMPLETE] Progress logged to corporate ledger." -ForegroundColor Green
    }

    "create-snapshot" {
        $timestamp = (Get-Date).ToString("yyyyMMdd_HHmmss")
        $targetSnapshot = Join-Path $backupDir "${timestamp}_${SnapshotName}"
        New-Item -ItemType Directory -Path $targetSnapshot -Force | Out-Null

        Write-Host "[SANDBOX SAFETY] Creating pre-flight stable snapshot..." -ForegroundColor Cyan
        Write-Host "  -> Snapshot Target: $targetSnapshot"

        # Copy state and key config files
        $dirsToBackup = @("rules", "skills", "scripts")
        foreach ($d in $dirsToBackup) {
            $src = Join-Path $rootDir $d
            if (Test-Path $src) {
                Copy-Item -Path $src -Destination $targetSnapshot -Recurse -Force
            }
        }
        
        # Copy root JSONs
        Get-ChildItem -Path $rootDir -File -Filter "*.json" | ForEach-Object {
            Copy-Item -Path $_.FullName -Destination $targetSnapshot -Force
        }

        Write-Host "  [SNAPSHOT SEALED] Stable state backed up successfully. Rollback point established." -ForegroundColor Green

        & powershell -ExecutionPolicy Bypass -File $stateScript -Action log-event -Initiator "Sandbox Safety Gate" -EventType "PRE_FLIGHT_SNAPSHOT_CREATED" -Description "Created stable backup snapshot '${timestamp}_${SnapshotName}' prior to test execution." | Out-Null
    }

    "cleanup-clutter" {
        Write-Host "[WORKSPACE HYGIENE] Sweeping for clutter, obsolete test files, and temporary artifacts..." -ForegroundColor Cyan
        
        $clutterPatterns = @("*.tmp", "*~", "*.bak", "scratch_*.json", "temp_*.txt")
        $deletedCount = 0

        foreach ($pat in $clutterPatterns) {
            Get-ChildItem -Path $rootDir -Recurse -File -Filter $pat | Where-Object { $_.FullName -notmatch "\\\.state\\backups\\" } | ForEach-Object {
                Write-Host "  -> Pruning clutter: $($_.FullName)" -ForegroundColor Yellow
                Remove-Item -Path $_.FullName -Force
                $deletedCount++
            }
        }

        Write-Host "`n[HYGIENE AUDIT COMPLETE] Pruned $deletedCount temporary/clutter artifacts." -ForegroundColor Green
        Write-Host "  -> Workspace directory hierarchy is clean, structured, and compliant." -ForegroundColor Green

        & powershell -ExecutionPolicy Bypass -File $stateScript -Action log-event -Initiator "Hygiene Protocol" -EventType "WORKSPACE_CLUTTER_PRUNED" -Description "Swept workspace and pruned $deletedCount obsolete temporary test artifacts." | Out-Null
    }

    Default {
        Write-Host "[STATUS] Matrix Reverse Repository & Sandbox Engine is active and operational."
        Write-Host "  Available Actions: 'git-sync', 'create-snapshot', 'cleanup-clutter'"
    }
}
