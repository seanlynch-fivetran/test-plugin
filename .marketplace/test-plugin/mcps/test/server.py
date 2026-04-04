"""Test MCP server that reports environment variable state and CWD."""

import os
from fastmcp import FastMCP

mcp = FastMCP("test-mcp")


@mcp.tool()
def get_server_info() -> dict:
    """Report environment variables and the current working directory of the server."""
    return {
        "test_env_variable": os.environ.get("TEST_ENV_VARIABLE", "<not set>"),
        "test_default_variable": os.environ.get("TEST_DEFAULT_VARIABLE", "<not set>"),
        "claude_plugin_root": os.environ.get("CLAUDE_PLUGIN_ROOT", "<not set>"),
        "claude_plugin_data": os.environ.get("CLAUDE_PLUGIN_DATA", "<not set>"),
        "cwd": os.getcwd(),
    }


if __name__ == "__main__":
    mcp.run()
