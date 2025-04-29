# Stitch SDK
[![version](https://img.shields.io/badge/version-0.3.12-yellow.svg)](https://semver.org)

Stitch SDK is a Python library that wraps the API for managing memory spaces and memories. It provides both a Python SDK and a command-line interface (CLI).

## Installation

```bash
pip install stitch_ai
```

## CLI Usage

Before using the CLI, set your API key as an environment variable:

```bash
export STITCH_API_KEY=your_api_key
```

### Available Commands

1. Get user info:
```bash
stitch user-get
```

2. Get user's memory:
```bash
stitch user-memory --memory-names <memory_names>
```

3. Get user's histories:
```bash
stitch user-histories
```

4. Get user's purchased memories:
```bash
stitch user-purchases
```

5. Create a new memory space:
```bash
stitch create-space <space_name>
```

6. Get memory space:
```bash
stitch get-space <space_name>
```

7. Delete memory space:
```bash
stitch delete-space <space_name>
```

8. Get memory space's histories:
```bash
stitch get_history <space_name>
```

9. Push agent memory:
```bash
stitch push <space_name> [-m COMMIT_MESSAGE] [-e EPISODIC_FILE_PATH] [-c CHARACTER_FILE_PATH]
```

10. Pull memory from a memory space:
```bash
stitch pull <space_name> -p <db_path>
```

11. Pull external memory:
```bash
stitch pull-external <space_name> -p <rag_path>
```

12. Get market listed memories:
```bash
stitch market-list-spaces <type (AGENT_MEMORY | EXTERNAL_MEMORY)>
```

### Examples

```bash
# Create a new memory space
stitch create-space my_space

# Push memory with a message and files
stitch push my_space -m "Initial memory" -e ./agent/episodic.json -c ./agent/character.json

# Pull memory
stitch pull my_space -p ./db/chroma.sqlite3

# Pull external memory
stitch pull-external my_space -p ./rag/rag.json

# Get user info
stitch user-get

# Get user's memories
stitch user-memory --memory-names my_space

# List marketplace spaces
stitch market-list-spaces public
```

## Environment Variables

- `STITCH_API_KEY`: Your API key (required)
- `STITCH_API_URL`: API endpoint (optional, defaults to https://api-demo.stitch-ai.co)

## SDK Usage

```python
from stitch_ai import StitchSDK

sdk = StitchSDK()
sdk.create_space("my_space")
```
