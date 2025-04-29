import sys
from ..sdk import StitchSDK
import argparse
import os

def add_memory_subparsers(subparsers, handlers):
    # Create space command
    create_space_parser = subparsers.add_parser('create-space', help='Create a new memory space')
    create_space_parser.add_argument('space', help='Name of the memory space')
    create_space_parser.add_argument('--type', '-t', help='Type of the memory space', default="AGENT_MEMORY")

    # get space command
    get_space_parser = subparsers.add_parser('get-space', help='Get a memory space')
    get_space_parser.add_argument('space', help='Name of the memory space')
    get_space_parser.add_argument('--ref', default='main', help='Branch or commit ref (default: main)')

    # delete space command
    delete_space_parser = subparsers.add_parser('delete-space', help='Delete a memory space')
    delete_space_parser.add_argument('space', help='Name of the memory space')

    # clone space command
    clone_space_parser = subparsers.add_parser('clone-space', help='Clone a memory space')
    clone_space_parser.add_argument('space', help='Name of the memory space')
    clone_space_parser.add_argument('source_name', help='Name of the source memory space')
    clone_space_parser.add_argument('source_owner_id', help='Owner ID of the source memory space')

    # get history command
    get_history_parser = subparsers.add_parser('get-history', help='Get the history of a memory space')
    get_history_parser.add_argument('space', help='Name of the memory space')
    
    # Push memory command
    push_parser = subparsers.add_parser('push', help='Push memory to a space')
    push_parser.add_argument('space', help='Name of the memory space')
    push_parser.add_argument('--message', '-m', help='Commit message')
    push_parser.add_argument('--episodic', '-e', help='Path to episodic memory file')
    push_parser.add_argument('--character', '-c', help='Path to character memory file')

    # Pull memory command
    pull_parser = subparsers.add_parser('pull', help='Pull memory from a space')
    pull_parser.add_argument('repository', help='Name of the memory space')
    pull_parser.add_argument('memory_name', help='Name of the memory')
    pull_parser.add_argument('--db-path', '-p', required=True, help='Path to save the memory data')

    # Pull external memory command
    pull_external_parser = subparsers.add_parser('pull-external', help='Pull external memory')
    pull_external_parser.add_argument('repository', help='Name of the memory space')
    pull_external_parser.add_argument('memory_name', help='Name of the memory')
    pull_external_parser.add_argument('--rag-path', '-p', required=True, help='Path to save the RAG file')

    handlers.update({
        'create-space': handle_create_space,
        'get-space': handle_get_space,
        'delete-space': handle_delete_space,
        'clone-space': handle_clone_space,
        'get-history': handle_get_history,
        'push': handle_push,
        'pull': handle_pull,
        'pull-external': handle_pull_external,
    })

def handle_create_space(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.memory_space.create_space(args.space, args.type)
        print(f"🌟 Successfully created space: {args.space}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error creating space: {e}", file=sys.stderr)
        sys.exit(1)

def handle_get_space(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.memory_space.get_space(args.space, args.ref)
        print(f"🔍 Successfully retrieved space: {args.space}") 
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error getting space: {e}", file=sys.stderr)
        sys.exit(1)

def handle_delete_space(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.memory_space.delete_space(args.space)
        print(f"🗑️ Successfully deleted space: {args.space}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error deleting space: {e}", file=sys.stderr)
        sys.exit(1)

def handle_clone_space(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.memory_space.clone_space(args.space, args.source_name, args.source_owner_id)
        print(f"🔄 Successfully cloned space: {args.space}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error cloning space: {e}", file=sys.stderr)
        sys.exit(1)

def handle_get_history(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.memory_space.get_history(args.space)
        print(f"📜 Successfully retrieved history: {args.space}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error getting history: {e}", file=sys.stderr)
        sys.exit(1)

def handle_push(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        if not args.episodic and not args.character:
            raise ValueError("At least one of --episodic or --character must be provided")

        print("_" * 50)
        response = sdk.push(
            space=args.space,
            message=args.message,
            episodic_path=args.episodic,
            character_path=args.character
        )
        print(f"📤 Successfully pushed memory to space: {args.space}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error pushing memory: {e}", file=sys.stderr)
        sys.exit(1)

def handle_pull(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.pull_memory(
            repository=args.repository,
            memory_name=args.memory_name,
            db_path=args.db_path
        )
        print(f"📥 Successfully pulled memory from space: {args.repository}")
        print(f"💾 Memory data saved to: {args.db_path}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error pulling memory: {e}", file=sys.stderr)
        sys.exit(1)

def handle_pull_external(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.pull_external_memory(
            repository=args.repository,
            memory_name=args.memory_name,
            rag_path=args.rag_path
        )
        print(f"🌐 Successfully pulled external memory")
        print(f"💾 External memory data saved to: {args.rag_path}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error pulling external memory: {e}", file=sys.stderr)
        sys.exit(1)
