import sys
from ..sdk import StitchSDK
import argparse
import os

def add_memory_subparsers(subparsers, handlers):
    # Create space command
    create_space_parser = subparsers.add_parser('create-space', help='Create a new memory space')
    create_space_parser.add_argument('space', help='Name of the memory space')

    # Push memory command
    push_parser = subparsers.add_parser('push', help='Push memory to a space')
    push_parser.add_argument('space', help='Name of the memory space')
    push_parser.add_argument('--message', '-m', help='Commit message')
    push_parser.add_argument('--episodic', '-e', help='Path to episodic memory file')
    push_parser.add_argument('--character', '-c', help='Path to character memory file')

    # Pull memory command
    pull_parser = subparsers.add_parser('pull', help='Pull memory from a space')
    pull_parser.add_argument('user_id', help='User ID')
    pull_parser.add_argument('repository', help='Name of the memory space')
    pull_parser.add_argument('--db-path', '-p', required=True, help='Path to save the memory data')
    pull_parser.add_argument('--ref', default='main', help='Branch or commit ref (default: main)')

    # Pull external memory command
    pull_external_parser = subparsers.add_parser('pull-external', help='Pull external memory')
    pull_external_parser.add_argument('user_id', help='User ID')
    pull_external_parser.add_argument('repository', help='Name of the memory space')
    pull_external_parser.add_argument('--rag-path', '-p', required=True, help='Path to save the RAG file')
    pull_external_parser.add_argument('--ref', default='main', help='Branch or commit ref (default: main)')

    handlers.update({
        'create-space': handle_create_space,
        'push': handle_push,
        'pull': handle_pull,
        'pull-external': handle_pull_external,
    })

def handle_create_space(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.memory_space.create_space(args.space)
        print(f"🌟 Successfully created space: {args.space}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error creating space: {e}", file=sys.stderr)
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
            user_id=args.user_id,
            repository=args.repository,
            db_path=args.db_path,
            ref=args.ref
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
            user_id=args.user_id,
            repository=args.repository,
            rag_path=args.rag_path,
            ref=args.ref
        )
        print(f"🌐 Successfully pulled external memory")
        print(f"💾 External memory data saved to: {args.rag_path}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error pulling external memory: {e}", file=sys.stderr)
        sys.exit(1)
