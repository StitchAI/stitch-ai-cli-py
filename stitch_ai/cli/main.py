import os
import argparse
import sys
from dotenv import load_dotenv
from ..sdk import StitchSDK
from .memory_cli import add_memory_subparsers
from .git_cli import add_git_subparsers
from .marketplace_cli import add_marketplace_subparsers
from .user_cli import add_user_subparsers

def create_parser_and_handlers():
    parser = argparse.ArgumentParser(description="Stitch AI CLI tool")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    handlers = {}
    add_memory_subparsers(subparsers, handlers)
    add_git_subparsers(subparsers, handlers)
    add_marketplace_subparsers(subparsers, handlers)
    add_user_subparsers(subparsers, handlers)
    return parser, handlers

def main() -> None:
    parser, handlers = create_parser_and_handlers()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Initialize SDK
    load_dotenv()
    base_url = os.environ.get('STITCH_API_URL', 'https://api-demo.stitch-ai.co')
    api_key = os.environ.get('STITCH_API_KEY')
    if not api_key:
        print("Error: STITCH_API_KEY environment variable is not set", file=sys.stderr)
        sys.exit(1)

    try:
        sdk = StitchSDK(base_url=base_url, api_key=api_key)
    except Exception as e:
        print(f"Error initializing SDK: {e}", file=sys.stderr)
        sys.exit(1)

    handler = handlers.get(args.command)
    if handler:
        handler(sdk, args)
    else:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()