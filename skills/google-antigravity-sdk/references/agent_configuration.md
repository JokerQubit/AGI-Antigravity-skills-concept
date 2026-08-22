# Advanced Agent Configuration Guide

This guide details the parameters and options available in `LocalAgentConfig` and `CapabilitiesConfig`.

## Model Configuration

### Default Models
- Default Orchestration Model: `gemini-3.7-flash`
- Default Image Generation Model: `gemini-3.1-flash-lite-image`

### Model Identifier Rules
- Always verify model identifiers against official documentation before setting them explicitly.
- Leaving the model field unset defaults to the optimal general-purpose model for the SDK version.

```python
from google.antigravity import Agent, LocalAgentConfig

config = LocalAgentConfig(
    model="gemini-3.7-flash",
)
```

## Agent Execution Behavior (`agent_behavior`)

The SDK supports two operational modes in `types.CapabilitiesConfig`:

- `AgentBehavior.AUTONOMOUS` (**default**): The agent executes tasks end-to-end autonomously without pausing for interactive confirmation.
- `AgentBehavior.INTERACTIVE`: The agent asks clarifying questions (via `ask_question`) and actively collaborates with the user.

```python
from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    capabilities=types.CapabilitiesConfig(
        agent_behavior=types.AgentBehavior.INTERACTIVE,
    ),
)
```

## Nested Subagents & Depth Controls

Configure hierarchical subagent execution with explicit safety bounds:

- `max_subagent_depth`: Recursion depth ceiling for subagent dispatch (root conversation is depth 0).
- `allowed_subagents`: Whitelist of subagent names that the root agent or parent subagent is permitted to invoke.

```python
from google.antigravity import Agent, LocalAgentConfig, types

reviewer = types.SubagentConfig(
    name="reviewer",
    description="Code quality and security review subagent",
    capabilities=types.SubagentCapabilities(
        enabled_tools=[
            types.BuiltinTools.VIEW_FILE,
        ],
        allowed_subagents=[],
    ),
)

config = LocalAgentConfig(
    subagents=[reviewer],
    capabilities=types.CapabilitiesConfig(
        enable_subagents=True,
        max_subagent_depth=2,
        allowed_subagents=["reviewer"],
    ),
)
```

## Session Budget Controls (`BudgetConfig`)

Enforce operational ceilings on model calls, tool calls, and tokens:

```python
from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    budget_config=types.BudgetConfig(
        max_model_calls=25,
        max_tool_calls=50,
        max_input_tokens=200_000,
        max_output_tokens=32_000,
        max_total_tokens=250_000,
    ),
)
```

## Enterprise / Vertex AI Configuration

```python
from google.antigravity import Agent, LocalAgentConfig

# 1. Express Mode (API Key authentication)
express_config = LocalAgentConfig(
    vertex=True,
    api_key="your-api-key",
)

# 2. Standard Mode (Application Default Credentials with regional routing)
standard_config = LocalAgentConfig(
    vertex=True,
    project="my-gcp-project",
    location="us-central1",
)
```

## Application Data Directory Override

Configure the directory for session artifacts, scratch files, and logs:

```python
from google.antigravity import Agent, LocalAgentConfig

# Must be an absolute path
config = LocalAgentConfig(
    app_data_dir="d:/custom/agent_storage",
)
```

> **Note**: Passing relative paths or unexpanded `~` paths triggers `AntigravityValidationError`.
