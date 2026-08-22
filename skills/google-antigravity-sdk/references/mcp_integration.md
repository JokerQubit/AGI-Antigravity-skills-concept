# Model Context Protocol (MCP) Integration

The Google Antigravity SDK natively supports connecting external MCP servers via Stdio and SSE transports.

## Configuration

Add MCP servers to `LocalAgentConfig` via `mcp_servers`:

```python
from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    mcp_servers=[
        # 1. Stdio Transport (Local process)
        types.McpStdioServer(
            name="sqlite",
            command="npx",
            args=["-y", "@modelcontextprotocol/server-sqlite", "d:/data/app.db"],
            env={"DEBUG": "mcp*"},
        ),
        # 2. SSE Transport (Remote or containerized service)
        types.McpStreamableHttpServer(
            name="remote_devtools",
            url="http://127.0.0.1:8080/sse",
        ),
    ],
)
```

## Tool Namespacing & Access Control

Tools exposed by MCP servers are registered dynamically into the agent's tool set. You can manage MCP permissions through standard `Policy` rules:

```python
from google.antigravity import Policy

policy = Policy()
# Allow all tools from the sqlite server
policy.allow_server("sqlite")
# Deny specific tools from a server
policy.deny("remote_devtools:destructive_action")
```
