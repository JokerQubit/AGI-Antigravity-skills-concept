# Triggers & Background Event Processing

This example demonstrates using proactive triggers in the Google Antigravity SDK to react to timers and filesystem changes in the background.

```python
import asyncio
import logging
from pathlib import Path
from google.antigravity import Agent, LocalAgentConfig
from google.antigravity.triggers import every, on_file_change, TriggerContext

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# 1. Periodic Health Check Trigger
async def periodic_health_check(ctx: TriggerContext):
    """Executes periodically to verify system status."""
    logging.info("Periodic health check triggered.")
    await ctx.send("System health status: healthy. All background monitors active.")

timer_trigger = every(60, periodic_health_check)

# 2. File Change Monitor Trigger
async def handle_config_change(ctx: TriggerContext, changes):
    """Callback when watched configuration files are modified."""
    for change in changes:
        logging.info("Watched file modified: %s (%s)", change.path, change.kind)
        await ctx.send(f"Configuration file {change.path} was modified. Review required.")

watch_path = str(Path("d:/config/settings.json").resolve())
file_trigger = on_file_change(watch_path, handle_config_change)

async def main():
    config = LocalAgentConfig(
        system_instructions="You are an autonomous operations engineer handling proactive events.",
        triggers=[timer_trigger, file_trigger],
    )

    async with Agent(config) as agent:
        response = await agent.chat("Initialize background monitoring loop.")
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(main())
```
