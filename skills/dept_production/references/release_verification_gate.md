# Departmental Runbook: Release Verification Gate (`PROD-RUN-01`)

## 1. Trigger Conditions
Executes prior to presenting any finished deliverable or code implementation to the CEO or end-user.

## 2. Pre-Flight Verification Checklist
Every release must pass all four criteria without exception:

1. **Functional Integrity**:
   - Every file modified or created exists on the filesystem and is syntactically valid.
   - All tests execute and exit with code 0.
2. **Epistemic Soundness**:
   - Zero `[UNCONFIRMED]` assumptions remain in the documentation.
   - All claims are cross-referenced with empirical data or working code.
3. **No Placeholders**:
   - Zero instances of `TODO`, `FIXME`, or stubbed empty methods.
4. **State Ledger Synchronization**:
   - The active milestone in `.state/status.json` is updated to `VERIFIED`.
   - A closing transaction is committed to `.state/ledger/`.

## 3. Escalation Protocols
- If any checklist item fails, the release is aborted and routed back to the offending Department Head with a blocking defect notice.
