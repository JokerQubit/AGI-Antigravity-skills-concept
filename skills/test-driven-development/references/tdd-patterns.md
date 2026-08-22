# TDD Patterns, Isolation Techniques & Assertion Strategies

This reference details production patterns for Test-Driven Development across unit, integration, and skill-level testing.

---

## 1. Test Harness Taxonomy

### 1.1 Unit Test Harnesses
Unit tests verify discrete algorithms and state machines in complete isolation from external I/O (filesystems, networks, clocks):
- **Fast Execution:** A full unit test suite should execute in under 1 second.
- **Deterministic Fixtures:** Test fixtures must initialize pristine state per test case (`setUp` / `tearDown`).
- **Zero Flakiness:** Eliminate nondeterministic concurrency or random seeds without fixed pseudo-random generators.

### 1.2 Integration Test Harnesses
Integration tests verify module interaction with real filesystem paths, subprocesses, and serialized payloads:
- **Temporary Sandboxes:** Use temporary working directories and clean up upon suite completion.
- **Subprocess Isolation:** Validate stdout/stderr exit codes cleanly.

---

## 2. Assertion Patterns & Behavioral Invariants

### 2.1 State Verification vs Interaction Verification
- **State Verification:** Assert that after executing an operation, the object state or returned value matches expected invariants. Prefer state verification whenever possible.
- **Interaction Verification:** Assert that a dependency was invoked with exact arguments. Use sparingly and only at subsystem boundaries.

### 2.2 Boundary Value & Equivalence Partitioning
Every test suite must cover three canonical input domains:
1. **Nominal Case:** Typical, well-formed input data.
2. **Boundary Conditions:** Minimum/maximum capacity, zero-length sequences, empty collections, single-item collections.
3. **Exceptional/Error Case:** Malformed inputs, missing keys, type mismatches, out-of-range arguments asserting explicit exception types.

---

## 3. Mocking & Isolation Techniques

When external dependencies (APIs, timers, network sockets) must be decoupled:
- **Dependency Injection:** Pass interfaces, callable handlers, or clock providers as constructor arguments rather than monkey-patching global module state.
- **In-Memory Fakes:** Use lightweight in-memory implementations (e.g. in-memory key-value dictionary replacing a disk cache) rather than deep mock trees.
- **Clean Teardown:** Ensure patched attributes are restored unconditionally.

---

## 4. TDD Lifecycle Rules for Progressive Disclosure Skills

When designing Antigravity skills (`SKILL.md`):
1. **Trigger Specificity:** Frontmatter descriptions must specify exact triggering conditions and domain keywords.
2. **Deterministic File Referencing:** All reference paths declared in `SKILL.md` must link to existing markdown files under `references/`.
3. **Zero Placeholder Mandate:** Implementations must contain complete executable logic and thorough instructional text.
