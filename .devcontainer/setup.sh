#!/usr/bin/env bash
set -euo pipefail

# Install thv (ToolHive)
THV_VERSION=$(curl -s https://api.github.com/repos/stacklok/toolhive/releases/latest | grep '"tag_name"' | cut -d'"' -f4 | sed 's/^v//')
curl -fsSL "https://github.com/stacklok/toolhive/releases/download/v${THV_VERSION}/toolhive_${THV_VERSION}_linux_amd64.tar.gz" \
  | tar -xz -C /usr/local/bin thv

# Ensure Claude Code config exists so thv can register itself
if [ ! -f "$HOME/.claude.json" ]; then
  echo '{}' > "$HOME/.claude.json"
fi

# Register Claude Code as a thv client
thv client register claude-code

# Start mermaid MCP server
thv run mermaid
