import os
from typing import Optional, Dict, Any
from ..processors.memory_processor import MemoryProcessor
from ..processors.text_processor import TextProcessor
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
        files = []
        if episodic_path:
            if episodic_path.endswith('.sqlite'):
                data = self.memory_processor.process_sqlite_file(episodic_path)
                files.append({"filePath": "episodic.data", "content": data})
            else:
                data = self.memory_processor.process_memory_file(episodic_path)
                files.append({"filePath": "episodic.data", "content": data})
        if character_path:
            data = self.memory_processor.process_character_file(character_path)
            files.append({"filePath": "character.data", "content": data})
        return self.memory.push_memory(repository=space, message=message, files=files)

    def pull_memory(self, repository: str, db_path: str) -> Dict[str, Any]:
        response_data = self.user.get_user_memory(repository)

        memory_item = None
        if isinstance(response_data, list) and response_data:
            for item in response_data:
                if item.get("name") == repository:
                    memory_item = item
                    break
        if not memory_item:
            raise ValueError(f"No memory found with name: {repository}")

        save_data = {"data": {}}
        if "characterMemory" in memory_item and memory_item["characterMemory"].get("content"):
            save_data["data"]["character"] = memory_item["characterMemory"]["content"][0]
        if "episodicMemory" in memory_item and memory_item["episodicMemory"].get("content"):
            save_data["data"]["episodic"] = memory_item["episodicMemory"]["content"][0]
        if not save_data["data"]:
            raise ValueError("Memory does not contain character or episodic data")
        self.memory_processor.save_memory_data(save_data, db_path)
        return response_data

    def pull_external_memory(self, repository: str, rag_path: str) -> Dict[str, Any]:
        response_data = self.user.get_user_memory(repository)

        memory_item = None
        if isinstance(response_data, list) and response_data:
            for item in response_data:
                if item.get("name") == repository:
                    memory_item = item
                    break
        if not memory_item:
            raise ValueError(f"No memory found with name: {repository}")

        save_data = {"data": {}}
        if "externalMemory" in memory_item and memory_item["externalMemory"].get("content"):
            save_data["data"]["external"] = memory_item["externalMemory"]["content"][0]
        if not save_data["data"]:
            raise ValueError("Memory does not contain external data")
        self.memory_processor.save_memory_data(save_data, rag_path)
        return response_data

__all__ = ["StitchSDK"] 