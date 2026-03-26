<div align="center">

# Shell Server

**A lightweight MCP server that gives AI assistants access to your terminal.**

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![MCP](https://img.shields.io/badge/MCP-protocol-5B5EA6?style=for-the-badge)](https://modelcontextprotocol.io)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![uv](https://img.shields.io/badge/built%20with-uv-DE5FE9?style=for-the-badge)](https://docs.astral.sh/uv/)

---

*Run shell commands through the [Model Context Protocol](https://modelcontextprotocol.io) — connect any MCP-compatible AI client to your system's terminal.*

</div>

## Features

- **Single tool, full power** — exposes a `terminal` tool that runs any shell command
- **Stdout + stderr** — returns combined output with clear labeling
- **Timeout protection** — commands are capped at 30 seconds
- **Error reporting** — non-zero exit codes are surfaced automatically
- **Stdio transport** — works with any MCP client out of the box

## Quickstart

### With uv (recommended)

```bash
# Clone the repo
git clone https://github.com/joandiazcapell/shellserver.git
cd shellserver

# Install dependencies and run
uv sync
uv run server.py
```

### With Docker

```bash
# Build the image
docker build -t shellserver .

# Run the container
docker run --rm -i shellserver
```

Or pull directly from Docker Hub:

```bash
docker run --rm -i yourusername/shellserver:latest
```

## MCP Client Configuration

Add this to your MCP client config to connect:

### Local (uv)

```json
{
  "mcpServers": {
    "shell": {
      "command": "uv",
      "args": ["run", "server.py"],
      "cwd": "/path/to/shellserver"
    }
  }
}
```

### Docker

```json
{
  "mcpServers": {
    "shell": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "shellserver"]
    }
  }
}
```

## Tool Reference

### `terminal`

Run a shell command and return its output.

| Parameter | Type | Description |
|-----------|------|-------------|
| `command` | `string` | The shell command to execute |

**Returns** — stdout, stderr (if any), and exit code (if non-zero).

```
> terminal("echo hello world")
hello world

> terminal("ls nonexistent")
STDERR:
ls: nonexistent: No such file or directory
Exit code: 1
```

## Project Structure

```
shellserver/
├── server.py          # MCP server implementation
├── pyproject.toml     # Project metadata & dependencies
├── uv.lock            # Locked dependencies
├── Dockerfile         # Container build file
└── README.md
```

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (for local development)
- Docker (for containerized usage)

---

<div align="center">

Built with [FastMCP](https://github.com/modelcontextprotocol/python-sdk) and [uv](https://docs.astral.sh/uv/)

</div>
