import sys
from ..sdk import StitchSDK
import argparse

def add_key_subparsers(subparsers, handlers):
    key_gen_parser = subparsers.add_parser('key', help='Generate a new API key')
    key_gen_parser.add_argument('user_id', help='Wallet address (userId)')
    key_gen_parser.add_argument('hashed_id', help='Hashed user id (hashedId)')
    key_gen_parser.add_argument('name', help='API key name')
    handlers['key'] = handle_key

def handle_key(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.create_key(args.user_id, args.hashed_id, args.name)
        print(f"🔑 Successfully created key for user: {args.user_id}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error creating key: {e}", file=sys.stderr)
        sys.exit(1) 