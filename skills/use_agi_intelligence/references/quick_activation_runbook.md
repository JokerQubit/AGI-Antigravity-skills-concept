# Quick Activation Runbook: Use AGI Intelligence

This runbook guides the Primary AI and Sub-Agents in operationalizing the `use_agi_intelligence` master skill during live sessions.

---

## Step 1: Turn-Zero Detection & Header Announcement
When the user prompt arrives, immediately evaluate:
1. Is `use_agi_intelligence` attached or referenced?
2. What are the core nouns and verbs in the prompt?
3. Format the executive response header:
   ```markdown
   **OmniCognition Labs AGI Intelligence Active**
   - **Correlated Rules**: [rules/<rule_name>.md]
   - **Correlated Skills**: [skills/<skill_name>/SKILL.md]
   - **Execution Vector**: <Direct Execution | Sub-Agent Delegation>
   ```

---

## Step 2: Premise Deconstruction
Check for:
- Flawed technical assumptions.
- Missing dependencies or unverified files.
- If missing, emit `[DATA GAP IDENTIFIED]` and query with inspection tools.

---

## Step 3: Execution under Via Deserti
- No stubs, no placeholders, no ellipses.
- If delegating to a sub-agent, use the Sub-Agent Clean-Context Inheritance Charter from Section 5 of `SKILL.md`.

---

## Step 4: Verification & Sign-off
- Run static checks and unit tests.
- Commit to `.state/ledger/` when major milestones complete.