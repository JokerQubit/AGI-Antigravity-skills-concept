# Lifecycle Hooks Interceptors

This example demonstrates intercepting turns, tool calls, and errors to implement audit logging and runtime safety controls.

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig, Hooks, HookResult

hooks = Hooks()

@hooks.pre_turn
async def before_turn(turn_idx: int, user_prompt: str) -> None:
    print(f"\n>>> [Hook: PreTurn] Starting turn {turn_idx}: '{user_prompt[:40]}'")

@hooks.pre_tool_call_decide
async def validate_tool_execution(tool_name: str, args: dict) -> HookResult:
    # Intercept tool calls before execution
    if tool_name == "run_command":
        cmd = args.get("CommandLine", "")
        if "rm " in cmd or "del " in cmd:
            print(f"[Hook: Security Gate] Denied command: {cmd}")
            return HookResult(allow=False, reason="Destructive file operations prohibited.")
    return HookResult(allow=True)

@hooks.post_tool_call
async def after_tool_execution(tool_name: str, args: dict, result: str) -> None:
    print(f"<<< [Hook: PostTool] Tool '{tool_name}' executed. Result length: {len(result)} chars")

async def main():
    config = LocalAgentConfig(
        hooks=hooks,
        system_instructions="You are an autonomous operations assistant.",
    )

    async with Agent(config) as agent:
        response = await agent.chat("Check directory contents and summarize findings.")
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(main())
```
