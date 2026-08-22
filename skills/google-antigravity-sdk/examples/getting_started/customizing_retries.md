# Customizing Retries & Exponential Backoff

This example demonstrates fine-tuning retry behavior for transient API errors and schema validation failures.

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig, types

async def main():
    # Configure retry policies
    retry_config = types.RetryConfig(
        model_api=types.ModelAPIRetryConfig(
            max_retries=4,
            initial_delay_sec=1.0,
            backoff_multiplier=2.0,
            max_delay_sec=16.0,
        ),
        model_output=types.ModelOutputRetryConfig(
            max_schema_retries=3,
        ),
    )

    config = LocalAgentConfig(
        retry_config=retry_config,
    )

    async with Agent(config) as agent:
        response = await agent.chat("Analyze repository commit integrity.")
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(main())
```
