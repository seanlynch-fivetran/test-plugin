# test-plugin

A minimal Claude Code marketplace plugin for testing installation flows.

## Installation

```
/plugin marketplace add seanlynch-fivetran/test-plugin
/plugin install test-plugin@test-marketplace
```


## Structure

Everything lives under `.marketplace/test-plugin/` — no build step, no source directories.

- **Marketplace**: `test-marketplace` — one plugin
- **Plugin**: `test-plugin` — one MCP server, one skill
- **MCP Server**: `test-mcp` — single-file FastMCP/Python server, run with `uv`
- **Skill**: `test-skill` — calls `get_server_info`
- **Tool**: `get_server_info` — reports `TEST_ENV_VARIABLE` and the server's CWD


## Claude Code behavior

From CLI, not sure if this applies/is shared with claude desktop

/Users/.../.claude/plugins/marketplaces
- /Users/.../.claude/plugins/installed_plugins.json - contains plugins/scopes/version info
- /Users/.../.claude/plugins/cache/