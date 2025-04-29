import sys
import argparse
import json
from ..sdk import StitchSDK

def add_marketplace_subparsers(subparsers, handlers):
    # List memory spaces
    list_spaces_parser = subparsers.add_parser('market-list-spaces', help='List memory spaces in the marketplace')
    list_spaces_parser.add_argument('type', help='Type of memory space (e.g. AGENT_MEMORY, EXTERNAL_MEMORY)')
    list_spaces_parser.add_argument('--paginate', help='Pagination (optional)', default=None)
    list_spaces_parser.add_argument('--sort', help='Sort (optional)', default=None)
    list_spaces_parser.add_argument('--filters', help='Filters (optional)', default=None)

    # List memory in a space
    list_memory_parser = subparsers.add_parser('market-list-memory', help='List memory in a marketplace space')
    list_memory_parser.add_argument('body', help='Request body (JSON string)')

    # Purchase memory
    purchase_parser = subparsers.add_parser('market-purchase', help='Purchase memory from the marketplace')
    purchase_parser.add_argument('body', help='Request body (JSON string)')

    handlers.update({
        'market-list-spaces': handle_market_list_spaces,
        'market-list-memory': handle_market_list_memory,
        'market-purchase': handle_market_purchase,
    })

def handle_market_list_spaces(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        response = sdk.marketplace.get_memory_space_lists(
            args.type,  
            paginate=args.paginate,
            sort=args.sort,
            filters=args.filters
        )
        print('🛒 Marketplace memory spaces:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error listing marketplace spaces: {e}', file=sys.stderr)
        sys.exit(1)

def handle_market_list_memory(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        body = json.loads(args.body)
        response = sdk.marketplace.list_memory(body)
        print('🛒 Marketplace memory list:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error listing marketplace memory: {e}', file=sys.stderr)
        sys.exit(1)

def handle_market_purchase(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print('_' * 50)
        body = json.loads(args.body)
        response = sdk.marketplace.purchase_memory(args.api_key, body)
        print('🛒 Marketplace purchase result:')
        print(response)
        print('_' * 50)
    except Exception as e:
        print(f'❌ Error purchasing memory: {e}', file=sys.stderr)
        sys.exit(1) 