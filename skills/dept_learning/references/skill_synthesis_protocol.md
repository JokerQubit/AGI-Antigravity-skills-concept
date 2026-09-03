# Departmental Runbook: Dynamic Skill Synthesis Protocol (`LRN-RUN-01`)

## 1. Trigger Conditions
Executes whenever a complex procedural task is performed successfully more than twice manually, or when a post-mortem reveals an uncodified operational pattern.

## 2. Skill Synthesis Workflow

### Step 1: Pattern Extraction
1. Extract the raw sequence of tool calls, search queries, and script executions from the transcript.
2. Parameterize variable inputs (e.g., replace hardcoded paths with standardized arguments).

### Step 2: Encapsulation into Antigravity Skill Format
1. Generate `skills/<skill_name>/SKILL.md` following Antigravity progressive disclosure standards.
2. Structure frontmatter:
   - `name`: Lowercase, hyphen-separated.
   - `description`: Strict third-person description stating *what* it does and *when* the agent should invoke it.
3. Isolate complex helper scripts into `scripts/` and reference guides into `references/`.

### Step 3: Verification & Registration
1. Execute a dry-run test of the newly synthesized skill.
2. Update `.state/status.json` to register the new skill under `synthesized_skills`.
