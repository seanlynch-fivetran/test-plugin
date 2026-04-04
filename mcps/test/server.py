"""Test MCP server that reports environment variable state and CWD."""

import os
from fastmcp import FastMCP

mcp = FastMCP("test-mcp")


@mcp.tool()
def get_server_info() -> dict:
    """Report the value of TEST_ENV_VARIABLE and the current working directory of the server."""
    return {
        "test_env_variable": os.environ.get("TEST_ENV_VARIABLE", "<not set>"),
        "cwd": os.getcwd(),
    }


if __name__ == "__main__":
    mcp.run()
