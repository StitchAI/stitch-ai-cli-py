import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv
from .api.git import GitAPIClient

class GitSDK:
    """
    SDK class for git repository operations on the Stitch AI platform.
    """
    def __init__(self, base_url: str = "https://api-demo.stitch-ai.co", api_key: Optional[str] = None):
        load_dotenv()
        self.api_key = api_key or os.environ.get("STITCH_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided either directly or via STITCH_API_KEY environment variable")
        self.git_api = GitAPIClient(base_url, self.api_key)

    def create_repo(self, user_id: str, name: str) -> Dict[str, Any]:
        """
        Create a new git repository.
        Args:
            user_id (str): Wallet address
            name (str): Repository name
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.create_repo(user_id, name)

    def clone_repo(self, user_id: str, name: str, source_name: str, source_owner_id: str) -> Dict[str, Any]:
        """
        Clone a git repository.
        Args:
            user_id (str): Wallet address
            name (str): New repository name
            source_name (str): Source repository name
            source_owner_id (str): Source owner wallet address
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.clone_repo(user_id, name, source_name, source_owner_id)

    def list_branches(self, user_id: str, repository: str) -> Dict[str, Any]:
        """
        List all branches in a repository.
        Args:
            user_id (str): Wallet address
            repository (str): Repository name
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.list_branches(user_id, repository)

    def checkout_branch(self, user_id: str, repository: str, branch: str) -> Dict[str, Any]:
        """
        Checkout a branch in a repository.
        Args:
            user_id (str): Wallet address
            repository (str): Repository name
            branch (str): Branch name
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.checkout_branch(user_id, repository, branch)

    def create_branch(self, user_id: str, repository: str, branch_name: str, base_branch: str) -> Dict[str, Any]:
        """
        Create a new branch in a repository.
        Args:
            user_id (str): Wallet address
            repository (str): Repository name
            branch_name (str): New branch name
            base_branch (str): Base branch name
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.create_branch(user_id, repository, branch_name, base_branch)

    def delete_branch(self, user_id: str, repository: str, branch: str) -> Dict[str, Any]:
        """
        Delete a branch in a repository.
        Args:
            user_id (str): Wallet address
            repository (str): Repository name
            branch (str): Branch name
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.delete_branch(user_id, repository, branch)

    def merge(self, user_id: str, repository: str, ours: str, theirs: str, message: str) -> Dict[str, Any]:
        """
        Merge two branches in a repository.
        Args:
            user_id (str): Wallet address
            repository (str): Repository name
            ours (str): Ours branch name
            theirs (str): Theirs branch name
            message (str): Commit message
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.merge(user_id, repository, ours, theirs, message)

    def commit_file(self, user_id: str, repository: str, file_path: str, content: str, message: str) -> Dict[str, Any]:
        """
        Commit a file to a repository.
        Args:
            user_id (str): Wallet address
            repository (str): Repository name
            file_path (str): File path
            content (str): File content
            message (str): Commit message
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.commit_file(user_id, repository, file_path, content, message)

    def get_log(self, user_id: str, repository: str, depth: Optional[int] = None) -> Dict[str, Any]:
        """
        Get the commit log of a repository.
        Args:
            user_id (str): Wallet address
            repository (str): Repository name
            depth (Optional[int]): Number of commits to retrieve
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.get_log(user_id, repository, depth)

    def get_file(self, user_id: str, repository: str, file_path: str, ref: str) -> Dict[str, Any]:
        """
        Get a file from a repository at a specific ref.
        Args:
            user_id (str): Wallet address
            repository (str): Repository name
            file_path (str): File path
            ref (str): Branch or commit ref
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.get_file(user_id, repository, file_path, ref)

    def diff(self, user_id: str, repository: str, oid1: str, oid2: str) -> Dict[str, Any]:
        """
        Get the diff between two commits in a repository.
        Args:
            user_id (str): Wallet address
            repository (str): Repository name
            oid1 (str): First commit oid
            oid2 (str): Second commit oid
        Returns:
            Dict[str, Any]: API response
        """
        return self.git_api.diff(user_id, repository, oid1, oid2) 