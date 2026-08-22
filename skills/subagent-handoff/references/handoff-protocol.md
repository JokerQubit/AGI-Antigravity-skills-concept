# Subagent Handoff Protocol Specification & Schemas

This reference specifies schemas, directory standards, and verification mechanics for multi-agent coordination.

---

## 1. Directory Structure & File Naming Conventions

```
.agents/
├── <parent_agent>/
│   ├── plan.md               # Decomposition tree & task assignments
│   ├── progress.md           # Swarm heartbeat & milestone tracker
│   └── context.md            # Architectural invariants & global state
└── <subagent_name>/
    ├── DISPATCH.md           # Assignment prompt and constraints
    ├── BRIEFING.md           # Persistent working memory and role state
    ├── progress.md           # Liveness heartbeat and step checklist
    └── handoff.md            # Standardized 5-component deliverable report
```

### 1.1 Invariant Rules
- **Exclusive Folder Write:** Agents may write only to their own `.agents/<name>/` directory.
- **Global Read:** Any agent may read files from peer or parent agent folders via `view_file`.
- **Zero Production Storage:** No source code, operational tests, or user data files may be written under `.agents/`.

---

## 2. Structured Handoff Schema (Markdown Template)

```markdown
# Handoff Report: [Task Name]

**Author:** [Agent Name]  
**Recipient:** [Parent Agent / Successor Agent]  
**Timestamp:** [UTC ISO 8601]  
**Status:** [Hard Handoff / Soft Handoff / Partial Handoff]  

---

## 1. Observation
- Inspected `skills/test-driven-development/SKILL.md` (lines 1-120).
- Ran verification command: `python test_plugin.py --suite skills` -> Passed (2 tests in 0.05s).
- Error log observed at `tests/test_skills_frontmatter.py:82`: `AssertionError: description too short`.

## 2. Logic Chain
1. Observation 1 confirms skill structure exists.
2. Observation 3 showed description length violation (<20 characters).
3. Modifying YAML frontmatter in SKILL.md satisfies length constraint.
4. Observation 2 demonstrates test suite now passes with exit code 0.

## 3. Caveats
- Tested on Windows environment with Python 3.12. Linux POSIX validation recommended in CI.

## 4. Conclusion
- Milestone 2 methodology skill implementations are complete, valid, and passing all tests.

## 5. Verification Method
- Execute: `python test_plugin.py --suite skills`
- Verify exit code is 0 and 0 failures reported.
```

---

## 3. Communication Protocol

### 3.1 Coordination Messages (`send_message`)
Messages sent across agent boundaries must follow the concise 3-field format:

```
**Context**: [Active task or subtask identifier]
**Content**: [Concise status summary and absolute path to deliverable report]
**Action**: [Explicit expectation: e.g. "Review handoff report at d:/agi/.agents/worker_m2/handoff.md and proceed with milestone merge."]
```

### 3.2 Liveness Heartbeat
Every agent must update its `progress.md` with an updated timestamp `Last visited: [ISO-8601]` at least every 5 minutes during long-running tasks.
