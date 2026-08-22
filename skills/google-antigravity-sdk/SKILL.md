---
name: google-antigravity-sdk
description: Design, implement, and debug autonomous AI agents and multi-agent systems using the Google Antigravity (AGY) SDK. Activates when configuring LocalAgentConfig, CapabilitiesConfig, LiteRT/OpenAI local models, subagent recursion depth, budget limits, or safety policies.
---

# Google Antigravity Python SDK

The Google Antigravity SDK (`google-antigravity`) provides high-level programmatic orchestration for autonomous AI agents, multi-agent hierarchies, on-device local models, and lifecycle hooks.

## Installation & Setup

Before proceeding with Google Antigravity SDK development:

1. **Check Dependencies**: Ensure `google-antigravity` is installed in your Python environment:
   ```bash
   pip install google-antigravity
   ```
2. **Authentication**: Set the `GEMINI_API_KEY` environment variable or provide credentials via `LocalAgentConfig`:
   - Obtain an API key from Google AI Studio: `https://aistudio.google.com/app/api-keys`
   - For Enterprise / Vertex AI Standard Mode (ADC), run `gcloud auth application-default login` and configure `vertex=True, project="my-project", location="us-central1"`.
   - For Enterprise / Vertex AI Express Mode, pass `vertex=True, api_key="your-key"`.
   - For local on-device models (`LiteRTAgentConfig` or `LocalOpenAIAgentConfig`), no API key or cloud network access is required.

## Core Routing Table

Consult the authoritative reference guides and code examples below:

### References

- [Architecture Overview](references/architecture.md): Core concepts (`Agent`, `Conversation`, `Connection`, event loop execution).
- [Agent Configuration Guide](references/agent_configuration.md): `LocalAgentConfig`, `CapabilitiesConfig`, `AgentBehavior` (AUTONOMOUS vs INTERACTIVE), models, timeouts, environment variables.
- [Built-in Tools Reference](references/built_in_tools.md): Complete list of 13 built-in tools, permission semantics, and tool override rules.
- [Safety Policies](references/safety_policies.md): Declarative 9-level priority access control (`policy.allow`, `policy.deny`, `policy.ask_user`, predicate evaluation).
- [Error Handling & Recovery](references/error_handling.md): Exception hierarchy (`AntigravityError`, `AntigravityValidationError`, `AntigravityConnectionError`, `AntigravityCancelledError`), hooks for automatic error recovery.
- [Local Models Guide](references/local_models.md): On-device inference with Gemma via LiteRT (`LiteRTAgentConfig`) and OpenAI-compatible loopback servers (`LocalOpenAIAgentConfig`).
- [MCP Integration](references/mcp_integration.md): Integrating Model Context Protocol (MCP) Stdio and SSE servers.
- [Observability & Token Tracking](references/observability.md): Monitoring token usage, thinking tokens, latency, and custom audit logs.

### Examples

- [Hello World & Streaming](examples/getting_started/hello_world.md): Basic agent instantiation, token and thought streaming.
- [Agent Configuration & Personas](examples/getting_started/persona_config.md): Custom system instructions and persona tuning.
- [Custom Tool Creation](examples/getting_started/custom_tool.md): Defining Python functions as tools and managing state with `ToolContext`.
- [Multi-Tier Subagent Delegation](examples/getting_started/subagents.md): Nested subagents with depth limits and permission boundaries.
- [Budget Limits & Stop Reasons](examples/getting_started/budget_limits.md): Operational dials (`BudgetConfig`) and multi-turn `StopReason` handling.
- [Lifecycle Hooks](examples/getting_started/hooks.md): Intercepting turn, tool, and session lifecycle events.
- [Turn Cancellation](examples/getting_started/cancellation.md): Aborting active generation streams cleanly with `response.cancel()`.
- [Customizing Retries](examples/getting_started/customizing_retries.md): Configurable retry backoff policies for API errors.
- [Local Models in Action](examples/getting_started/local_models.md): Running Gemma locally on CPU/GPU/NPU.
- [MCP Server Tools](examples/getting_started/mcp_tools.md): Connecting external MCP services.
- [Multimodal Inputs](examples/getting_started/multimodal.md): Processing images, PDFs, and media generation.
- [Triggers & Background Events](examples/getting_started/periodic_trigger.md): Reactive time and file change triggers.
- [Session Persistence](examples/getting_started/persistence.md): Saving and restoring conversation history.
- [Structured Outputs](examples/getting_started/structured_output.md): Validating responses with Pydantic schemas.
- [Agent Skills](examples/getting_started/agent_skills.md): Loading and executing filesystem skills.
- [Web Tools & Disk Cache](examples/getting_started/web_tools.md): Web scraping and URL inspection workflows.
- [App Data Directory Override](examples/getting_started/app_data_dir_override.md): Custom storage paths for session artifacts.
