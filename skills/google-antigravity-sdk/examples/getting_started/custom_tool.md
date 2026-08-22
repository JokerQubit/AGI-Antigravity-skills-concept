# Custom Python Tools & Stateful Context

This example demonstrates defining custom callable functions as agent tools and maintaining conversation state using `ToolContext`.

## Defining a Stateful Custom Tool

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig, ToolContext

def track_metric(metric_name: str, value: float, ctx: ToolContext) -> str:
    """Records numerical metrics across conversation turns.

    Args:
        metric_name: The identifier of the metric (e.g., 'memory_mb', 'latency_ms').
        value: The numerical measurement.
        ctx: The injected tool execution context.
    """
    history = ctx.get_state("metric_history", {})
    if metric_name not in history:
        history[metric_name] = []
    history[metric_name].append(value)
    ctx.set_state("metric_history", history)

    count = len(history[metric_name])
    avg_val = sum(history[metric_name]) / count
    return f"Recorded {metric_name}={value}. Total observations: {count}, Average: {avg_val:.2f}"

async def main():
    config = LocalAgentConfig(
        tools=[track_metric],
        system_instructions="You are a performance profiling assistant. Use track_metric to record readings.",
    )

    async with Agent(config) as agent:
        resp1 = await agent.chat("Initial memory reading is 142.5 MB.")
        async for chunk in resp1:
            print(chunk, end="", flush=True)
        print()

        resp2 = await agent.chat("Next reading after GC is 118.0 MB.")
        async for chunk in resp2:
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(main())
```

## Overriding Built-in Tools

To override a built-in tool, name your function with the exact tool name:

```python
def view_file(AbsolutePath: str) -> str:
    """Overridden view_file with sandbox restrictions."""
    if "/restricted/" in AbsolutePath:
        return "[ACCESS DENIED] Path is in restricted directory."
    with open(AbsolutePath, "r", encoding="utf-8") as f:
        return f.read()

config = LocalAgentConfig(
    tools=[view_file],
)
```
