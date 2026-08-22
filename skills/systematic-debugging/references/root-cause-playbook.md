# Root-Cause Debugging Playbook

This reference provides systematic methodologies for isolating complex defects, diagnosing race conditions, tracing memory corruption, and auditing environment parity.

---

## 1. Causal Stack Tracing & Backward Data Flow

When an exception or corrupted state is detected, perform systematic backward traversal:

1. **Stack Frame Inspection:** Extract line numbers, arguments, and local variable scopes across all frames in the trace.
2. **State Invariant Check:** At each frame, test whether local variables satisfy their mathematical invariants:
   $$\mathcal{I}(S_k) = \text{True} \quad \forall k \in [0, \dots, N]$$
3. **Transition Boundary Isolation:** Locate the exact transition $S_{k-1} \to S_k$ where $\mathcal{I}(S_k)$ becomes False.
4. **Origin Node Identification:** Identify whether the fault is due to invalid arguments passed from caller or invalid internal transformation within the callee.

---

## 2. Race Conditions & Asynchronous Timing Defect Patterns

For intermittent or timing-dependent bugs:

- **Resource Contention:** Identify shared mutable state accessed across concurrent coroutines, threads, or asynchronous task loops.
- **Critical Section Locking:** Verify mutex, semaphore, or queue synchronization guarantees around all shared state updates.
- **Deterministic Scheduling Simulation:** Replace real-time delays with deterministic virtual clocks or mock event loops to force the race condition to reproduce on every run.
- **State Transition Monotonicity:** Enforce monotonically increasing sequence numbers or timestamps on all asynchronous event dispatches.

---

## 3. Memory Leaks & Resource Exhaustion

When encountering memory growth or unreleased handles:

1. **Retained Path Analysis:** Capture baseline vs post-workload heap snapshots.
2. **Dominator Tree Identification:** Identify objects retaining large retain size in memory graphs.
3. **Lifecycle Unbinding:** Ensure event listeners, observer subscriptions, and file descriptors are unregistered in explicit cleanup or finalizer blocks.
4. **Chunked Streaming:** Replace unbounded in-memory buffers with chunked streaming pipelines.

---

## 4. Environment Parity Audit Checklist

When bugs reproduce only in specific environments (e.g. CI vs local development):

- [ ] **Path Separators & Encoding:** Verify POSIX `/` vs Windows `\` path handling and UTF-8 file encoding.
- [ ] **Dependency Pinning:** Verify lockfile versions match across runtime environments.
- [ ] **Environment Variables:** Verify presence and defaults of required environment variables.
- [ ] **Timezones & Clock Skew:** Ensure UTC normalization on all date/time parsing operations.
- [ ] **Filesystem Case Sensitivity:** Ensure file path references strictly match disk casing.
