# Stitch SDK
[![version](https://img.shields.io/badge/version-0.3.0-yellow.svg)](https://semver.org)

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

1. Create a new API key:
```bash
stitch key <user_id> <hashed_id> <name>
```

2. Create a new memory space:
```bash
stitch create-space <space_name>
```

3. Push memory to a space:
```bash
stitch push <space_name> [-m COMMIT_MESSAGE] [-e EPISODIC_FILE_PATH] [-c CHARACTER_FILE_PATH]
```

4. Pull memory from a space:
```bash
stitch pull <user_id> <repository> -p <db_path> [--ref REF]
```

5. Pull external memory:
```bash
stitch pull-external <user_id> <repository> -p <rag_path> [--ref REF]
```

6. User Management Commands:
```bash
# Get user info
stitch user-get <user_id>

# Get user statistics
stitch user-stat <user_id>

# Get user histories
stitch user-histories <user_id> [--paginate PAGINATE] [--sort SORT] [--filters FILTERS]

# Get user memory
stitch user-memory <user_id> <api_key> [--memory-names MEMORY_NAMES]

# Get user purchases
stitch user-purchases <user_id> [--paginate PAGINATE] [--sort SORT] [--filters FILTERS]
```

7. Marketplace Commands:
```bash
# List memory spaces in marketplace
stitch market-list-spaces <type> [--user-id USER_ID] [--paginate PAGINATE] [--sort SORT] [--filters FILTERS]

# List memory in a marketplace space
stitch market-list-memory <user_id> <repository> <api_key> <body>

# Purchase memory from marketplace
stitch market-purchase <user_id> <api_key> <body>
```

### Examples

```bash
# Create a new memory space
stitch create-space my_space

# Push memory with a message and files
stitch push my_space -m "Initial memory" -e ./agent/data/db.sqlite -c ./characters/default.character.json

# Pull memory
stitch pull user123 my_space -p ./db/chroma.sqlite3

# Pull external memory
stitch pull-external user123 my_space -p ./rag/rag.json

# Get user info
stitch user-get user123

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
