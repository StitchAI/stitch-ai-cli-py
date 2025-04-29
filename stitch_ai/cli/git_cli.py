import sys
from ..sdk import StitchSDK
import argparse

def add_git_subparsers(subparsers, handlers):
    # Git: create repo
    create_repo_parser = subparsers.add_parser('create-repo', help='Create a new git repository')
    create_repo_parser.add_argument('name', help='Repository name')

    # Git: clone repo
    clone_repo_parser = subparsers.add_parser('clone-repo', help='Clone a git repository')
    clone_repo_parser.add_argument('name', help='New repository name')
    clone_repo_parser.add_argument('source_name', help='Source repository name')
    clone_repo_parser.add_argument('source_owner_id', help='Source owner wallet address')

    # Git: list branches
    list_branches_parser = subparsers.add_parser('list-branches', help='List all branches in a repository')
    list_branches_parser.add_argument('repository', help='Repository name')

    # Git: checkout branch
    checkout_branch_parser = subparsers.add_parser('checkout-branch', help='Checkout a branch in a repository')
    checkout_branch_parser.add_argument('repository', help='Repository name')
    checkout_branch_parser.add_argument('branch', help='Branch name')

    # Git: create branch
    create_branch_parser = subparsers.add_parser('create-branch', help='Create a new branch in a repository')
    create_branch_parser.add_argument('repository', help='Repository name')
    create_branch_parser.add_argument('branch_name', help='New branch name')
    create_branch_parser.add_argument('base_branch', help='Base branch name')

    # Git: delete branch
    delete_branch_parser = subparsers.add_parser('delete-branch', help='Delete a branch in a repository')
    delete_branch_parser.add_argument('repository', help='Repository name')
    delete_branch_parser.add_argument('branch', help='Branch name')

    # Git: merge
    merge_parser = subparsers.add_parser('merge', help='Merge two branches in a repository')
    merge_parser.add_argument('repository', help='Repository name')
    merge_parser.add_argument('ours', help='Ours branch name')
    merge_parser.add_argument('theirs', help='Theirs branch name')
    merge_parser.add_argument('message', help='Commit message')

    # Git: commit file
    commit_file_parser = subparsers.add_parser('commit-file', help='Commit a file to a repository')
    commit_file_parser.add_argument('repository', help='Repository name')
    commit_file_parser.add_argument('file_path', help='File path')
    commit_file_parser.add_argument('content', help='File content')
    commit_file_parser.add_argument('message', help='Commit message')

    # Git: get log
    get_log_parser = subparsers.add_parser('get-log', help='Get the commit log of a repository')
    get_log_parser.add_argument('repository', help='Repository name')
    get_log_parser.add_argument('--depth', type=int, default=None, help='Number of commits to retrieve')

    # Git: get file
    get_file_parser = subparsers.add_parser('get-file', help='Get a file from a repository at a specific ref')
    get_file_parser.add_argument('repository', help='Repository name')
    get_file_parser.add_argument('file_path', help='File path')
    get_file_parser.add_argument('ref', help='Branch or commit ref')

    # Git: diff
    diff_parser = subparsers.add_parser('diff', help='Get the diff between two commits in a repository')
    diff_parser.add_argument('repository', help='Repository name')
    diff_parser.add_argument('oid1', help='First commit oid')
    diff_parser.add_argument('oid2', help='Second commit oid')

    handlers.update({
        'create-repo': handle_create_repo,
        'clone-repo': handle_clone_repo,
        'list-branches': handle_list_branches,
        'checkout-branch': handle_checkout_branch,
        'create-branch': handle_create_branch,
        'delete-branch': handle_delete_branch,
        'merge': handle_merge,
        'commit-file': handle_commit_file,
        'get-log': handle_get_log,
        'get-file': handle_get_file,
        'diff': handle_diff,
    })

def handle_create_repo(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.create_repo(args.name)
        print(f"📦 Successfully created repository: {args.name}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error creating repository: {e}", file=sys.stderr)
        sys.exit(1)

def handle_clone_repo(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.clone_repo(args.name, args.source_name, args.source_owner_id)
        print(f"🔄 Successfully cloned repository: {args.name}")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error cloning repository: {e}", file=sys.stderr)
        sys.exit(1)

def handle_list_branches(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.list_branches(args.repository)
        print(f"🌿 Branches in repository '{args.repository}':")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error listing branches: {e}", file=sys.stderr)
        sys.exit(1)

def handle_checkout_branch(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.checkout_branch(args.repository, args.branch)
        print(f"✅ Checked out branch '{args.branch}' in repository '{args.repository}'")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error checking out branch: {e}", file=sys.stderr)
        sys.exit(1)

def handle_create_branch(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.create_branch(args.repository, args.branch_name, args.base_branch)
        print(f"🌱 Created branch '{args.branch_name}' from '{args.base_branch}' in repository '{args.repository}'")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error creating branch: {e}", file=sys.stderr)
        sys.exit(1)

def handle_delete_branch(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.delete_branch(args.repository, args.branch)
        print(f"🗑️ Deleted branch '{args.branch}' in repository '{args.repository}'")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error deleting branch: {e}", file=sys.stderr)
        sys.exit(1)

def handle_merge(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.merge(args.repository, args.ours, args.theirs, args.message)
        print(f"🔀 Merged '{args.theirs}' into '{args.ours}' in repository '{args.repository}'")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error merging branches: {e}", file=sys.stderr)
        sys.exit(1)

def handle_commit_file(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.commit_file(args.repository, args.file_path, args.content, args.message)
        print(f"💾 Committed file '{args.file_path}' to repository '{args.repository}'")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error committing file: {e}", file=sys.stderr)
        sys.exit(1)

def handle_get_log(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.get_log(args.repository, args.depth)
        print(f"📜 Commit log for repository '{args.repository}':")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error getting log: {e}", file=sys.stderr)
        sys.exit(1)

def handle_get_file(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.get_file(args.repository, args.file_path, args.ref)
        print(f"📄 File '{args.file_path}' at ref '{args.ref}' in repository '{args.repository}':")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error getting file: {e}", file=sys.stderr)
        sys.exit(1)

def handle_diff(sdk: StitchSDK, args: argparse.Namespace) -> None:
    try:
        print("_" * 50)
        response = sdk.git.diff(args.repository, args.oid1, args.oid2)
        print(f"🔍 Diff between '{args.oid1}' and '{args.oid2}' in repository '{args.repository}':")
        print(response)
        print("_" * 50)
    except Exception as e:
        print(f"❌ Error getting diff: {e}", file=sys.stderr)
        sys.exit(1) 