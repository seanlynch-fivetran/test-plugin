# test-plugin

A minimal Claude Code marketplace plugin for testing installation flows.

## Structure

- **Marketplace**: `test_marketplace` — one plugin
- **Plugin**: `test_plugin` — one MCP server, one skill
- **MCP Server**: `test_mcp` — single-file FastMCP/Python server, run with `uv`
- **Skill**: `test_skill` — calls `get_server_info`
- **Tool**: `get_server_info` — reports `TEST_ENV_VARIABLE` and the server's CWD

## No build step

The `.marketplace/` directory is checked in as-is. Edit it directly.
