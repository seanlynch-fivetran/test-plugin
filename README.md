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

### Claude Code

Marketplace defined at repo root in `.claude-plugin/marketplace.json`. Plugin contents under
`.marketplace/test-plugin/` with:
- `.claude-plugin/plugin.json` — name, version, author, `userConfig`
- `.mcp.json` — MCP server definitions (separate file; can also be inline in plugin.json)
- `skills/test-skill/SKILL.md` — skill definition with YAML frontmatter
- `mcps/test/server.py` — the actual MCP server

Key vars: `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`, `${user_config.*}`

### Codex

No repo-root marketplace file needed here — the **consuming repo** defines
`.agents/plugins/marketplace.json` pointing at the plugin directory.

Plugin uses `.codex-plugin/plugin.json` instead, which adds:
- `interface` object — `displayName`, `shortDescription`, `developerName`, `category`, `capabilities`, `defaultPrompt`, `brandColor`, etc.
- `mcpServers` — path reference to `.mcp.json` (not inline)
- `skills` — path reference to skills directory

Marketplace entries include `policy.installation` (`AVAILABLE`, `INSTALLED_BY_DEFAULT`, `NOT_AVAILABLE`)
and `policy.authentication` (`ON_INSTALL`, `ON_FIRST_USE`).

MCP servers execute in **project root** (at least with project scope). No `${PLUGIN_ROOT}` equivalent
observed — paths in `.mcp.json` are relative to project root, not plugin root.

### Shared

- `.mcp.json` — same format, used by both
- `skills/` and `mcps/` — same files, both platforms read them
- **Plugin**: `test-plugin` — one MCP server, one skill
- **MCP Server**: `test-mcp` — single-file FastMCP/Python server, run with `uv`
- **Skill**: `test-skill` — calls `get_server_info`
- **Tool**: `get_server_info` — dumps all env vars and CWD


## Claude Code behavior

From CLI, not sure if this applies/is shared with claude desktop.

Claude plugin MCP code seems to execute relative to plugin root.

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
  https://claude.ai/api/organizations/[organizationUuid]/plugins/plugin_[guid]/download

`organizationUuid` appeared on my personal account despite note being tied to an organization in a
~/Library/Application Support/Claude/local-agent-mode-sessions/[guid]/local_[guid]/.claude/.claude.json


## Codex
- project-scoped plugins work in with the CLI, but not with the desktop app
- Desktop app does seem to support user-scoped plugins, though I couldn't get the mcp server to execute propertly
- mcp servers seem to execute in project root (at least with project scope), not plugin root like claude

Logs for CLI stored in
- ~/.codex/log/codex-tui.log

## Hack to print pwd

{
  "mcpServers": {
    "pwd-mcp": {
      "command": "python3",
      "args": ["-c", "import os; import sys; sys.stderr.write(os.getcwd())"]
    }
  }
}
