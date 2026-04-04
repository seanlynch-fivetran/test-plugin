# test-plugin

A minimal Claude Code marketplace plugin for testing installation flows.

## Installation

```
/plugin marketplace add seanlynch-fivetran/test-plugin
/plugin install test-plugin@test-marketplace
```


## Structure

- **Marketplace**: `test-marketplace` — one plugin
- **Plugin**: `test-plugin` — one MCP server, one skill
- **MCP Server**: `test-mcp` — single-file FastMCP/Python server, run with `uv`
- **Skill**: `test-skill` — calls `get_server_info`
- **Tool**: `get_server_info` — reports `TEST_ENV_VARIABLE` and the server's CWD

## No build step

The `.marketplace/` directory is checked in as-is. Edit it directly.
