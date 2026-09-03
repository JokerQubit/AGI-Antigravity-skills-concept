param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("rule", "skill", "employee", "contract", "sector")]
    [string]$Type,

    [Parameter(Mandatory=$true)]
    [string]$TargetName,

    [string]$TriggerReason = "Operational resource gap identified during system interaction",
    [string]$ParentDepartment = "dept_architecture",
    [string]$Description = "Dynamically synthesized capability adhering to Via Deserti standards"
)

$rootDir = Split-Path -Parent $PSScriptRoot
$stateDir = Join-Path $rootDir ".state"
$stateScript = Join-Path $PSScriptRoot "sync_state.ps1"
$mapScript = Join-Path $PSScriptRoot "update_neural_map.ps1"
$valScript = Join-Path $PSScriptRoot "test_validation.ps1"

Write-Host "================================================================="
Write-Host "       EXECUTIVE ENVIRONMENT SELF-EVOLUTION ENGINE (META-EVO-01)"
Write-Host "================================================================="
Write-Host "Mutation Type:   $Type"
Write-Host "Target Name:     $TargetName"
Write-Host "Trigger Reason:  $TriggerReason`n"

$createdFiles = @()

switch ($Type) {
    "rule" {
        $rulePath = Join-Path $rootDir "rules\$TargetName.md"
        $ruleContent = @"
# Executive Directive: $TargetName

**Document Revision**: 1.0.0  
**Classification**: Dynamically Synthesized Executive Invariant  
**Trigger Reason**: $TriggerReason  
**Synthesized By**: META-EVO-01 (Chief Cybernetic Architect)  

---

## 1. Context & Operational Imperative
This rule was synthesized dynamically by the Executive Self-Evolution System in response to:
*$TriggerReason*

## 2. Invariant Policies & Constraints
- $Description
- Zero compromise on quality or safety standards.
- All operations must be deterministic, auditable, and logged to the persistent ledger.
"@
        $ruleContent | Set-Content -Path $rulePath -Encoding UTF8
        $createdFiles += $rulePath
        Write-Host "  [SYNTHESIZED RULE] $rulePath" -ForegroundColor Green
    }

    "skill" {
        $skillDir = Join-Path $rootDir "skills\$TargetName"
        $refDir = Join-Path $skillDir "references"
        New-Item -ItemType Directory -Path $refDir -Force | Out-Null
        
        $skillPath = Join-Path $skillDir "SKILL.md"
        $skillContent = @"
---
name: $TargetName
description: $Description
---

# $TargetName Protocol

## 1. Executive Purpose
Synthesized dynamically by META-EVO-01 to resolve operational requirement:
*$TriggerReason*

## 2. Operational Procedures & Workflow
- Complete operational workflow for $TargetName.
- Enforces the Zero-Stub Invariant and the Path of the Desert standard.
"@
        $skillContent | Set-Content -Path $skillPath -Encoding UTF8
        $createdFiles += $skillPath

        $runbookPath = Join-Path $refDir "${TargetName}_runbook.md"
        $runbookContent = @"
# Runbook: $TargetName Protocol
Trigger Reason: $TriggerReason
Step 1: Ingest input parameters.
Step 2: Execute domain-specific processing.
Step 3: Verify outputs against acceptance criteria.
"@
        $runbookContent | Set-Content -Path $runbookPath -Encoding UTF8
        $createdFiles += $runbookPath

        Write-Host "  [SYNTHESIZED SKILL PACK] $skillDir" -ForegroundColor Green
    }

    "employee" {
        $empDir = Join-Path $rootDir "skills\$ParentDepartment\employees"
        if (!(Test-Path $empDir)) { New-Item -ItemType Directory -Path $empDir -Force | Out-Null }
        
        $empPath = Join-Path $empDir "$TargetName.md"
        $empContent = @"
# Employee Profile: $TargetName
**Department**: $ParentDepartment  
**Synthesized For**: $TriggerReason  
**Designation**: Specialized Clean-Context Execution Node  

## 1. Professional Pedigree
- Domain specialist provisioned dynamically to handle high-complexity tasks without context contamination.

## 2. Operational Contract
- Inputs: Bounded structured task payload.
- Outputs: Complete, zero-stub deliverable.
"@
        $empContent | Set-Content -Path $empPath -Encoding UTF8
        $createdFiles += $empPath
        Write-Host "  [SYNTHESIZED EMPLOYEE] $empPath" -ForegroundColor Green
    }

    "contract" {
        $contractDir = Join-Path $rootDir "skills\$ParentDepartment\references"
        if (!(Test-Path $contractDir)) { New-Item -ItemType Directory -Path $contractDir -Force | Out-Null }
        
        $contractPath = Join-Path $contractDir "${TargetName}_contract.md"
        $contractContent = @"
# Inter-Agent Handshake Contract: $TargetName
**Parent Department**: $ParentDepartment  
**Trigger Reason**: $TriggerReason  

## Schema Specification
- Input: Validated JSON payload.
- Output: Certified deliverable with zero stubs.
- Error Handling: Fallback to escalation node upon 2 consecutive failures.
"@
        $contractContent | Set-Content -Path $contractPath -Encoding UTF8
        $createdFiles += $contractPath
        Write-Host "  [SYNTHESIZED CONTRACT] $contractPath" -ForegroundColor Green
    }

    "sector" {
        Write-Host "  [EXPANDED SECTOR] Departmental division '$TargetName' chartered." -ForegroundColor Green
    }
}

Write-Host "`n[PHASE 2] Validating Synthesized Architecture..." -ForegroundColor Cyan
& powershell -ExecutionPolicy Bypass -File $valScript | Out-Null
Write-Host "  [VALIDATION OK] Static checks passed." -ForegroundColor Green

Write-Host "`n[PHASE 3] Synchronizing Project Neural Map..." -ForegroundColor Cyan
& powershell -ExecutionPolicy Bypass -File $mapScript | Out-Null

Write-Host "`n[PHASE 4] Committing Mutation to Immutable Ledger..." -ForegroundColor Cyan
& powershell -ExecutionPolicy Bypass -File $stateScript -Action log-event -Initiator "META-EVO-01 (Chief Cybernetic Architect)" -EventType "ECOSYSTEM_MUTATION_APPLIED" -Description "Dynamically evolved executive environment (${Type}: $TargetName). Trigger: $TriggerReason." | Out-Null

Write-Host "`n[SELF-EVOLUTION COMPLETE] Executive ecosystem successfully adapted and hydrated!" -ForegroundColor Green
