# Observability & Token Metrics

The Google Antigravity SDK provides detailed telemetry on prompt tokens, completion tokens, thinking tokens, and tool latencies.

## Inspecting Turn Metrics

The `ChatResponse` object exposes `usage_metadata`:

```python
from google.antigravity import Agent, LocalAgentConfig

config = LocalAgentConfig()

async with Agent(config) as agent:
    response = await agent.chat("Design an event-driven architecture.")
    async for chunk in response:
        print(chunk, end="", flush=True)

    if response.usage_metadata:
        print(f"\nPrompt Tokens:     {response.usage_metadata.prompt_token_count}")
        print(f"Candidates Tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Thinking Tokens:   {response.usage_metadata.thinking_token_count}")
        print(f"Total Tokens:      {response.usage_metadata.total_token_count}")
```

## Custom Audit Logging via Hooks

Track every turn and tool invocation across the entire session:

```python
import logging
from google.antigravity import Agent, LocalAgentConfig, Hooks

logger = logging.getLogger("agent.audit")
hooks = Hooks()

@hooks.post_turn
async def log_turn_metrics(turn_idx: int, user_input: str, response_summary: str, usage: dict):
    logger.info(
        "Turn %d complete | In: %d tokens | Out: %d tokens | Prompt: %s",
        turn_idx,
        usage.get("prompt_tokens", 0),
        usage.get("output_tokens", 0),
        user_input[:50],
    )

config = LocalAgentConfig(hooks=hooks)
```
