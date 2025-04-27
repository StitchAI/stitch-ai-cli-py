import os
from typing import Optional, Dict, Any

from dotenv import load_dotenv
from .processors.memory_processor import MemoryProcessor
from .processors.text_processor import TextProcessor
from .api.client import APIClient
from .api.memory import MemoryAPIClient
from .api.git import GitAPIClient

class StitchSDK:
    """
    Main SDK class for interacting with the Stitch AI platform.
    Provides high-level interface for memory management operations.
    """
    
    def __init__(self, base_url: str = "https://api-demo.stitch-ai.co", api_key: Optional[str] = None):
        """
        Initialize the Stitch SDK
        
        Args:
            base_url (str): Base URL for the API
            api_key (str, optional): API key for authentication. If not provided,
                                   will try to get from STITCH_API_KEY environment variable
        
        Raises:
            ValueError: If API key is not provided and not found in environment variables
        """
        load_dotenv()
        self.api_key = api_key or os.environ.get("STITCH_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided either directly or via STITCH_API_KEY environment variable")
        
        self.api_client = APIClient(base_url, self.api_key)
        self.memory_api = MemoryAPIClient(base_url, self.api_key)
        self.git_api = GitAPIClient(base_url, self.api_key)
        self.memory_processor = MemoryProcessor()
        self.text_processor = TextProcessor()

    def create_key(self, user_id: str, hashed_id: str, name: str) -> Dict[str, Any]:
        """
        Create a new API key for a user (wallet address)
        Args:
            user_id (str): Wallet address
            hashed_id (str): Hashed user id
            name (str): API key name
        Returns:
            Dict[str, Any]: API response containing key details
        """
        return self.api_client.create_key(user_id, hashed_id, name)

    def create_space(self, user_id: str, repository: str) -> Dict[str, Any]:
        """
        Create a new memory space
        Args:
            user_id (str): Wallet address
            repository (str): Name of the memory space
        Returns:
            Dict[str, Any]: API response containing space details
        """
        return self.memory_api.create_space(user_id, repository)

    def push(self, 
            user_id: str,
            repository: str, 
            message: str, 
            episodic_path: Optional[str] = None, 
            character_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Push memory data to a space (commit memory)
        Args:
            user_id (str): Wallet address
            repository (str): Name of the memory space
            message (str): Commit message
            episodic_path (str, optional): Path to episodic memory file
            character_path (str, optional): Path to character memory file
        Returns:
            Dict[str, Any]: API response
        """
        files = []
        if episodic_path:
            if episodic_path.endswith('.sqlite'):
                content = self.memory_processor.process_sqlite_file(episodic_path)
                files.append({"filePath": "episodic.data", "content": content})
            else:
                content = self.memory_processor.process_memory_file(episodic_path)
                files.append({"filePath": "episodic.data", "content": content})
        if character_path:
            content = self.memory_processor.process_character_file(character_path)
            files.append({"filePath": "character.data", "content": content})
        if not files:
            raise ValueError("At least one of episodic_path or character_path must be provided")
        return self.memory_api.push_memory(user_id, repository, message, files)

    def pull_memory(self, user_id: str, repository: str, db_path: str, ref: str = "main") -> Dict[str, Any]:
        """
        Pull memory from a space and save to short term ChromaDB
        Args:
            user_id (str): Wallet address
            repository (str): Name of the memory space
            db_path (str): Path to save the ChromaDB
            ref (str): Branch or commit ref (default: main)
        Returns:
            Dict[str, Any]: API response containing memory data
        """
        response_data = self.memory_api.pull_memory(user_id, repository, ref)
        self.memory_processor.save_memory_data(response_data, db_path)
        return response_data

    def pull_external_memory(self, memory_id: str, rag_path: str) -> Dict[str, Any]:
        """
        Pull memory from a space and save to JSON file
        
        Args:
            memory_id (str): ID of the memory to pull
            rag_path (str): Path to save the JSON file
            
        Returns:
            Dict[str, Any]: API response containing memory data
            
        Raises:
            Exception: If pulling fails
        """
        response_data = self.memory_api.pull_external_memory(memory_id)
        self.memory_processor.save_memory_data(response_data, rag_path)
        return response_data
    
    def list_spaces(self, user_id: str) -> Dict[str, Any]:
        """
        List all memory spaces for a user
        Args:
            user_id (str): Wallet address
        Returns:
            Dict[str, Any]: API response containing list of spaces
        """
        return self.memory_api.list_spaces(user_id)

    def list_memories(self, user_id: str, repository: str) -> Dict[str, Any]:
        """
        List all memories in a space (history)
        Args:
            user_id (str): Wallet address
            repository (str): Name of the memory space
        Returns:
            Dict[str, Any]: API response containing list of memories
        """
        return self.memory_api.list_memories(user_id, repository)

    def validate_api_key(self) -> bool:
        """
        Validate the API key by making a test request
        
        Returns:
            bool: True if API key is valid, False otherwise
        """
        try:
            self.list_spaces()
            return True
        except Exception:
            return False

    def get_version(self) -> str:
        """
        Get the SDK version
        
        Returns:
            str: Version string
        """
        return "0.2.7"

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