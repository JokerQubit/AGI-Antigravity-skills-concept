# Budget Limits & Stop Reasons

This example demonstrates how to configure session operational limits and handle `StopReason` when token or tool limits are reached.

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig, types

async def main():
    config = LocalAgentConfig(
        budget_config=types.BudgetConfig(
            max_model_calls=5,
            max_tool_calls=10,
            max_total_tokens=50_000,
        ),
    )

    async with Agent(config) as agent:
        response = await agent.chat("Perform an extensive security and dependency scan.")

        async for chunk in response:
            print(chunk, end="", flush=True)

        # Check termination reason
        if response.stop_reason:
            print(f"\n[Session Notice] Agent halted due to: {response.stop_reason.name}")
            if response.stop_reason == types.StopReason.MAX_TOOL_CALLS_EXCEEDED:
                print("Tool call budget exhausted. Consider increasing max_tool_calls.")
            elif response.stop_reason == types.StopReason.MAX_TOTAL_TOKENS_EXCEEDED:
                print("Token ceiling reached.")

if __name__ == "__main__":
    asyncio.run(main())
```
