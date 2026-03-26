"""Shell Server — MCP server that exposes a single tool for running shell commands."""

import subprocess
from typing import Annotated

from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("Shell Server")


@mcp.tool()
def terminal(
    command: Annotated[
        str,
        Field(
            description=(
                "The shell command to execute. Runs via /bin/sh -c on Unix or cmd /c "
                "on Windows. Pipes, redirects, and shell built-ins are supported. "
                "Commands time out after 30 seconds."
            )
        ),
    ],
) -> str:
    """Run a shell command and return its output.

    Returns a single string containing stdout, and stderr when present.
    Non-zero exit codes are reported at the end of the output so the caller
    can detect failures without parsing exit status separately.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        return "Error: command timed out after 30 seconds."
    except Exception as exc:  # noqa: BLE001
        return f"Error: failed to execute command — {exc}"

    parts: list[str] = []

    if result.stdout:
        parts.append(result.stdout.rstrip())

    if result.stderr:
        parts.append(f"STDERR:\n{result.stderr.rstrip()}")

    if result.returncode != 0:
        parts.append(f"Exit code: {result.returncode}")

    return "\n".join(parts) if parts else "(no output)"


@mcp.resource("resource://mcpreadme")
def mcpreadme() -> str:
    """Return the contents of ~/Desktop/mcpreadme.md."""
    with open("/Users/joandiaz/Desktop/mcpreadme.md", encoding="utf-8") as fh:
        return fh.read()


if __name__ == "__main__":
    mcp.run(transport="stdio")
