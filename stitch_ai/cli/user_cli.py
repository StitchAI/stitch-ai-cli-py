import sys
import argparse
from ..sdk import StitchSDK

def add_user_subparsers(subparsers, handlers):
    # Get user info
    subparsers.add_parser('user-get', help='Get user info')

    # Get user stat
    subparsers.add_parser('user-stat', help='Get user stat')

    # Get user histories
    histories_parser = subparsers.add_parser('user-histories', help='Get user histories')
    histories_parser.add_argument('--paginate', default=None, help='Pagination (optional)')
    histories_parser.add_argument('--sort', default=None, help='Sort (optional)')
    histories_parser.add_argument('--filters', default=None, help='Filters (optional)')

    # Get user memory
    memory_parser = subparsers.add_parser('user-memory', help='Get user memory')
    memory_parser.add_argument('--memory-names', default=None, help='Memory names (comma separated, optional)')

    # Get user purchases
    purchases_parser = subparsers.add_parser('user-purchases', help='Get user purchases')
    purchases_parser.add_argument('--paginate', default=None, help='Pagination (optional)')
    purchases_parser.add_argument('--sort', default=None, help='Sort (optional)')
    purchases_parser.add_argument('--filters', default=None, help='Filters (optional)')

    handlers.update({
        'user-get': handle_user_get,
        'user-stat': handle_user_stat,
        'user-histories': handle_user_histories,
        'user-memory': handle_user_memory,
        'user-purchases': handle_user_purchases,
    })

def handle_user_get(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.get_user()
        print('👤 User info:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting user info: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_stat(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.get_user_stat()
        print('📊 User stat:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting user stat: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_histories(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.get_user_histories(
            paginate=args.paginate,
            sort=args.sort,
            filters=args.filters
        )
        print('📜 User histories:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting user histories: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_memory(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.get_user_memory(memory_names=args.memory_names)
        print('🧠 User memory:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting user memory: {e}', file=sys.stderr)
        sys.exit(1)

def handle_user_purchases(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.user.get_user_purchases(
            paginate=args.paginate,
            sort=args.sort,
            filters=args.filters
        )
        print('🛒 User purchases:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error getting user purchases: {e}', file=sys.stderr)
        sys.exit(1) 