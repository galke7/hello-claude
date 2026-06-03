## Overview
Minimal Python wrapper around the Anthropic Messages API using Claude Haiku 4.5.

## Setup
1. Clone the repo and install dependencies:
```bash
   uv sync
```
2. Copy your API key into a `.env` file:
ANTHROPIC_API_KEY=sk-ant-...

## Usage
Run directly:
```bash
uv run hello-claude.py
```
Or import in your own script:
```python
from hello_claude import ask
print(ask("Hello!"))
```

