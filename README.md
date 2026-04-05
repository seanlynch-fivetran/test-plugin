# test-plugin

A minimal Claude Code marketplace plugin for testing installation flows.

## Installation

```
/plugin marketplace add seanlynch-fivetran/test-plugin
/plugin install test-plugin@test-marketplace
```


## Structure

Everything lives under `.marketplace/test-plugin/` — no build step, no source directories.
Dual metadata: `.claude-plugin/` for Claude Code, `.codex-plugin/` for Codex.

- **Marketplace**: `test-marketplace` — one plugin
- **Plugin**: `test-plugin` — one MCP server, one skill
- **MCP Server**: `test-mcp` — single-file FastMCP/Python server, run with `uv`
- **Skill**: `test-skill` — calls `get_server_info`
- **Tool**: `get_server_info` — reports `TEST_ENV_VARIABLE` and the server's CWD


## Claude Code behavior

From CLI, not sure if this applies/is shared with claude desktop.

userConfig variables get a new install menu option in claude code, but don't prompt during installation.


Intallation and caching paths:

~/.claude/plugins/marketplaces
- ~/.claude/plugins/installed_plugins.json - contains plugins/scopes/version info
- ~/.claude/plugins/cache/

Logging:
~/Library/Caches/claude-cli-nodejs/-Users-seanlynch-empty/mcp-logs-plugin-test-plugin-test-mcp


### Claude Code Dekstop

Claude Desktop seemed to accept the plugins but wouldn't install the MCP server as defined. Not sure if it was the local MCP server or the userconfig.

### Claude.ai
- Desktop app, web doesn't support plugins yet
- Despite that, seems to cache these remotely automatically
  1. Plugin lookup by name:
  https://claude.ai/api/organizations/[organizationUuid]/plugins/by-name/test-plugin?marketplace_name=test-plugin&partition_by
  =account
  2. Plugin download (ZIP):
  https://claude.ai/api/organizations/[organizationUuid]/plugins/plugin_01YV1erzbCSMqirzmasr2Eys/download

`organizationUuid` appeared on my personal account despite note being tied to an organization in a
~/Library/Application Support/Claude/local-agent-mode-sessions/[guid]/local_[guid]/.claude/.claude.json