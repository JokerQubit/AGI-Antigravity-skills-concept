# Multi-Tier Subagents & Hierarchy Controls

This example demonstrates how to configure hierarchical subagents with explicit recursion depth limits and delegation whitelists.

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig, types

async def main():
    # 1. Leaf worker subagent
    linter = types.SubagentConfig(
        name="linter",
        description="Analyzes code formatting and linter violations",
        capabilities=types.SubagentCapabilities(
            enabled_tools=[types.BuiltinTools.VIEW_FILE],
            allowed_subagents=[],
        ),
    )

    # 2. Intermediate orchestrator subagent
    lead_qa = types.SubagentConfig(
        name="lead_qa",
        description="Coordinates quality assurance workflows and delegates to linters",
        capabilities=types.SubagentCapabilities(
            enabled_tools=[types.BuiltinTools.VIEW_FILE, types.BuiltinTools.START_SUBAGENT],
            allowed_subagents=["linter"],
        ),
    )

    # 3. Root agent configuration with max recursion depth of 2
    config = LocalAgentConfig(
        subagents=[lead_qa, linter],
        capabilities=types.CapabilitiesConfig(
            enable_subagents=True,
            max_subagent_depth=2,
            allowed_subagents=["lead_qa"],
        ),
    )

    async with Agent(config) as agent:
        response = await agent.chat("Dispatch lead_qa to audit current files.")
        async for chunk in response:
            print(chunk, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
```
