import os
from typing import Optional, Dict, Any
from .processors.memory_processor import MemoryProcessor
from .processors.text_processor import TextProcessor
from .api.client import APIClient
from .user import UserSDK
from .marketplace import MarketplaceSDK
from .memory import MemorySDK
from .memory_space import MemorySpaceSDK
from .git import GitSDK

class StitchSDK:
    """
    Main SDK class for interacting with the Stitch AI platform.
    Provides high-level interface for memory management operations.
    """
    
    def __init__(self, base_url: str = "https://api-demo.stitch-ai.co", api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("STITCH_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided either directly or via STITCH_API_KEY environment variable")
        self.api_client = APIClient(base_url, self.api_key)
        self.memory_processor = MemoryProcessor()
        self.text_processor = TextProcessor()
        self.user = UserSDK(base_url, self.api_key)
        self.memory = MemorySDK(base_url, self.api_key)
        self.marketplace = MarketplaceSDK(base_url, self.api_key)
        self.memory_space = MemorySpaceSDK(base_url, self.api_key)
        self.git = GitSDK(base_url, self.api_key)

    def push(self, space: str, message: Optional[str] = None, episodic_path: Optional[str] = None, character_path: Optional[str] = None) -> Dict[str, Any]:
        if not episodic_path and not character_path:
            raise ValueError("At least one of episodic_path or character_path must be provided")
        episodic_data = None
        character_data = None
        if episodic_path:
            if episodic_path.endswith('.sqlite'):
                episodic_data = self.memory_processor.process_sqlite_file(episodic_path)
            else:
                episodic_data = self.memory_processor.process_memory_file(episodic_path)
                if isinstance(episodic_data, str) and len(episodic_data) > 2000:
                    episodic_data = self.text_processor.chunk_text(episodic_data)
        if character_path:
            character_data = self.memory_processor.process_character_file(character_path)
        return self.api_client.push_memory(
            space=space,
            message=message,
            episodic=episodic_data,
            character=character_data
        )

    def pull_memory(self, space: str, memory_id: str, db_path: str) -> Dict[str, Any]:
        response_data = self.api_client.pull_memory(space, memory_id)
        self.memory_processor.save_memory_data(response_data, db_path)
        return response_data

    def pull_external_memory(self, memory_id: str, rag_path: str) -> Dict[str, Any]:
        response_data = self.api_client.pull_external_memory(memory_id)
        self.memory_processor.save_memory_data(response_data, rag_path)
        return response_data

__all__ = ["StitchSDK"] 