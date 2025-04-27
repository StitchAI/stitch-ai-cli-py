import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv
from .api.memory import MemoryAPIClient
from .processors.memory_processor import MemoryProcessor

class MemorySDK:
    """
    SDK class for memory management operations on the Stitch AI platform.
    """
    def __init__(self, base_url: str = "https://api-demo.stitch-ai.co", api_key: Optional[str] = None):
        load_dotenv()
        self.api_key = api_key or os.environ.get("STITCH_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided either directly or via STITCH_API_KEY environment variable")
        self.memory_api = MemoryAPIClient(base_url, self.api_key)
        self.memory_processor = MemoryProcessor()

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

    def push(self, user_id: str, repository: str, message: str, episodic_path: Optional[str] = None, character_path: Optional[str] = None) -> Dict[str, Any]:
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