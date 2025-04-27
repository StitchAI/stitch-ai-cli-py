import sys
from ..sdk import StitchSDK
import argparse

def add_memory_subparsers(subparsers, handlers):
    # Create space command
    create_space_parser = subparsers.add_parser('create-space', help='Create a new memory space')
    create_space_parser.add_argument('user_id', help='Wallet address (userId)')
    create_space_parser.add_argument('repository', help='Name of the memory space (repository)')

    # Push memory command
    push_parser = subparsers.add_parser('push', help='Push memory to a space')
    push_parser.add_argument('user_id', help='Wallet address (userId)')
    push_parser.add_argument('repository', help='Name of the memory space (repository)')
    push_parser.add_argument('--message', '-m', required=True, help='Commit message')
    push_parser.add_argument('--episodic', '-e', help='Path to episodic memory file')
    push_parser.add_argument('--character', '-c', help='Path to character memory file')

    # Pull memory command
    pull_parser = subparsers.add_parser('pull', help='Pull memory from a space')
    pull_parser.add_argument('user_id', help='Wallet address (userId)')
    pull_parser.add_argument('repository', help='Name of the memory space (repository)')
    pull_parser.add_argument('--db-path', '-p', required=True, help='Path to save the ChromaDB or JSON file')
    pull_parser.add_argument('--ref', default='main', help='Branch or commit ref (default: main)')

    # Pull external memory command
    pull_external_parser = subparsers.add_parser('pull-external', help='Pull external memory')
    pull_external_parser.add_argument('memory_id', help='ID of the memory to pull')
    pull_external_parser.add_argument('--rag-path', '-p', required=True, help='Path to save the RAG file')

    # List spaces command
    list_spaces_parser = subparsers.add_parser('list-spaces', help='List all memory spaces')
    list_spaces_parser.add_argument('user_id', help='Wallet address (userId)')

    # List memories command
    list_memories_parser = subparsers.add_parser('list-memories', help='List all memories in a space')
    list_memories_parser.add_argument('user_id', help='Wallet address (userId)')
    list_memories_parser.add_argument('repository', help='Name of the memory space (repository)')

    handlers.update({
        'create-space': handle_create_space,
        'push': handle_push,
        'pull': handle_pull,
        'pull-external': handle_pull_external,
        'list-spaces': handle_list_spaces,
        'list-memories': handle_list_memories,
    })

def handle_create_space(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.create_space(args.user_id, args.repository)
        print(f"🌟 Successfully created space: {args.repository}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error creating space: {e}", file=sys.stderr)
        sys.exit(1)

def handle_push(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.push(
            user_id=args.user_id,
            repository=args.repository,
            message=args.message,
            episodic_path=args.episodic,
            character_path=args.character
        )
        print(f"📤 Successfully pushed memory to space: {args.repository}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error pushing memory: {e}", file=sys.stderr)
        sys.exit(1)

def handle_pull(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.pull_memory(args.user_id, args.repository, args.db_path, args.ref)
        print(f"📥 Successfully pulled memory from space: {args.repository}")
        if args.db_path.endswith('.json'):
            print(f"📄 Memory data saved to JSON file: {args.db_path}")
        else:
            print(f"💾 Memory data saved to ChromaDB at: {args.db_path}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error pulling memory: {e}", file=sys.stderr)
        sys.exit(1)

def handle_pull_external(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.pull_external_memory(args.memory_id, args.rag_path)
        print(f"🌐 Successfully pulled external memory")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error pulling external memory: {e}", file=sys.stderr)
        sys.exit(1)

def handle_list_spaces(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.list_spaces(args.user_id)
        print("📚 Available memory spaces:")
        for space in response.get('data', []):
            print(f"  • {space}")
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error listing spaces: {e}", file=sys.stderr)
        sys.exit(1)

def handle_list_memories(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.list_memories(args.user_id, args.repository)
        print(f"🧠 Memories in space '{args.repository}':")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error listing memories: {e}", file=sys.stderr)
        sys.exit(1) 