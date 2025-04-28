import sys
import argparse
from ..sdk import StitchSDK

def add_user_subparsers(subparsers, handlers):
    # Get user info
    get_user_parser = subparsers.add_parser('user-get', help='Get user info')
    get_user_parser.add_argument('user_id', help='User ID')

    # Get API keys
    get_keys_parser = subparsers.add_parser('user-get-keys', help='Get API keys for user')
    get_keys_parser.add_argument('user_id', help='User ID')
    get_keys_parser.add_argument('hashed_id', help='Hashed user ID')

    # Create API key
    create_key_parser = subparsers.add_parser('user-create-key', help='Create API key for user')
    create_key_parser.add_argument('user_id', help='User ID')
    create_key_parser.add_argument('hashed_id', help='Hashed user ID')
    create_key_parser.add_argument('name', help='API key name')

    # Delete API key
    delete_key_parser = subparsers.add_parser('user-delete-key', help='Delete API key for user')
    delete_key_parser.add_argument('user_id', help='User ID')
    delete_key_parser.add_argument('hashed_id', help='Hashed user ID')
    delete_key_parser.add_argument('secret', help='API key secret')

    # Get user stat
    stat_parser = subparsers.add_parser('user-stat', help='Get user stat')
    stat_parser.add_argument('user_id', help='User ID')

    # Get user histories
    histories_parser = subparsers.add_parser('user-histories', help='Get user histories')
    histories_parser.add_argument('user_id', help='User ID')
    histories_parser.add_argument('--paginate', default=None, help='Pagination (optional)')
    histories_parser.add_argument('--sort', default=None, help='Sort (optional)')
    histories_parser.add_argument('--filters', default=None, help='Filters (optional)')

    # Get user memory
    memory_parser = subparsers.add_parser('user-memory', help='Get user memory')
    memory_parser.add_argument('user_id', help='User ID')
    memory_parser.add_argument('api_key', help='API key')
    memory_parser.add_argument('--memory-names', default=None, help='Memory names (comma separated, optional)')

    # Get user purchases
    purchases_parser = subparsers.add_parser('user-purchases', help='Get user purchases')
    purchases_parser.add_argument('user_id', help='User ID')
    purchases_parser.add_argument('--paginate', default=None, help='Pagination (optional)')
    purchases_parser.add_argument('--sort', default=None, help='Sort (optional)')
    purchases_parser.add_argument('--filters', default=None, help='Filters (optional)')

    handlers.update({
        'user-get': handle_user_get,
        'user-get-keys': handle_user_get_keys,
        'user-create-key': handle_user_create_key,
        'user-delete-key': handle_user_delete_key,
        'user-stat': handle_user_stat,
        'user-histories': handle_user_histories,
        'user-memory': handle_user_memory,
        'user-purchases': handle_user_purchases,
    })

def handle_user_get(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.get_user(args.user_id)
        print('👤 User info:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting user info: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_get_keys(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.get_api_keys(args.user_id, args.hashed_id)
        print('🔑 User API keys:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting API keys: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_create_key(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.create_api_key(args.user_id, args.hashed_id, args.name)
        print('🔑 Created API key:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error creating API key: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_delete_key(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.delete_api_key(args.user_id, args.hashed_id, args.secret)
        print('🗑️ Deleted API key:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error deleting API key: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_stat(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.get_user_stat(args.user_id)
        print('📊 User stat:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting user stat: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_histories(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.get_user_histories(args.user_id, paginate=args.paginate, sort=args.sort, filters=args.filters)
        print('📜 User histories:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting user histories: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_memory(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        memory_names = args.memory_names.split(',') if args.memory_names else None
        response = sdk.user.get_user_memory(args.user_id, args.api_key, memory_names)
        print('🧠 User memory:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting user memory: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_purchases(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.get_user_purchases(args.user_id, paginate=args.paginate, sort=args.sort, filters=args.filters)
        print('🛒 User purchases:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting user purchases: {e}', file=sys.stderr)
        sys.exit(1) 