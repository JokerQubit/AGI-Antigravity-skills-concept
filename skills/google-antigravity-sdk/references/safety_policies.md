# Declarative Safety Policies

The Google Antigravity SDK includes a declarative 9-level priority policy engine governing tool execution decisions: `allow`, `deny`, and `ask_user`.

## Policy Hierarchy & Precedence

Policies are evaluated in priority order from Level 1 (highest) to Level 9 (lowest):

1. **Explicit Tool Deny with Predicate**: `policy.add_rule(action="deny", tool="run_command", when=is_destructive)`
2. **Explicit Tool Deny**: `policy.add_rule(action="deny", tool="run_command")`
3. **Server-Level Deny with Predicate**: `policy.add_server_rule(action="deny", server="shell_mcp", when=is_production)`
4. **Server-Level Deny**: `policy.add_server_rule(action="deny", server="shell_mcp")`
5. **Interactive Ask User with Handler**: `policy.add_rule(action="ask_user", tool="run_command", handler=custom_approval_func)`
6. **Explicit Tool Allow with Predicate**: `policy.add_rule(action="allow", tool="run_command", when=is_safe_read)`
7. **Explicit Tool Allow**: `policy.add_rule(action="allow", tool="view_file")`
8. **Server-Level Allow**: `policy.add_server_rule(action="allow", server="filesystem_mcp")`
9. **Default Wildcard Policy**: Default behavior when no rules match (e.g. allow all other tools).

## Fail-Closed Semantics

If a predicate function passed to `when` raises an unhandled Python exception during evaluation, the policy evaluator **fails closed**—the condition is treated as matched and the most restrictive policy action (deny/ask) is immediately applied.

## Code Example

```python
from google.antigravity import Agent, LocalAgentConfig, Policy, types

def is_dangerous(tool_name: str, args: dict) -> bool:
    cmd = args.get("CommandLine", "").strip()
    return "rm -rf" in cmd

def is_safe_command(tool_name: str, args: dict) -> bool:
    cmd = args.get("CommandLine", "").strip()
    return cmd.startswith("git status") or cmd.startswith("pytest")

policy = Policy()
# Deny destructive commands
policy.add_rule(action="deny", tool="run_command", when=is_dangerous)
# Allow safe read commands
policy.add_rule(action="allow", tool="run_command", when=is_safe_command)
# Ask user for any other command
policy.add_rule(action="ask_user", tool="run_command")

config = LocalAgentConfig(
    policies=[policy],
)
```
