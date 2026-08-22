# MCP Tools Integration

This example demonstrates connecting external Model Context Protocol (MCP) servers to an Antigravity agent.

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig, Policy, types

async def main():
    # Configure MCP servers
    sqlite_mcp = types.McpStdioServer(
        name="database",
        command="npx",
        args=["-y", "@modelcontextprotocol/server-sqlite", "d:/data/records.db"],
    )

    policy = Policy()
    # Permit all read/query tools from the database MCP server
    policy.allow_server("database")

    config = LocalAgentConfig(
        mcp_servers=[sqlite_mcp],
        policies=[policy],
        system_instructions="You are a data analysis assistant with direct SQLite MCP database access.",
    )

    async with Agent(config) as agent:
        response = await agent.chat("List tables in the database and display schema for the users table.")
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(main())
```
