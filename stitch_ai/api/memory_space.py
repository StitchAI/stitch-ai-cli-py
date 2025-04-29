import requests
from typing import Dict, Any, Optional
from .client import BaseAPIClient
from enum import Enum

class MemoryType(Enum):
    AGENT_MEMORY = "AGENT_MEMORY"
    EXTERNAL_MEMORY = "EXTERNAL_MEMORY"

class MemorySpaceAPIClient(BaseAPIClient):
    def create_space(self, repository: str, memory_type: MemoryType = MemoryType.AGENT_MEMORY) -> Dict[str, Any]:
        """
        Create a new memory space (/memory-space/create)
        """
        url = f"{self.base_url}/memory-space/create"
        params = {"userId": self.user_id, "apiKey": self.api_key}
        payload = {"repository": repository, "type": str(memory_type)}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return {"repository": repository, "type": memory_type}

    def get_space(self, repository: str, ref: Optional[str] = None) -> Dict[str, Any]:
        """
        Get a memory space (/memory-space/{repository})
        """
        url = f"{self.base_url}/memory-space/{repository}"
        params = {"userId": self.user_id, "apiKey": self.api_key}
        if ref:
            params["ref"] = ref
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def delete_space(self, repository: str) -> Dict[str, Any]:
        """
        Delete a memory space (/memory-space/{repository})
        """
        url = f"{self.base_url}/memory-space/{repository}"
        params = {"userId": self.user_id, "apiKey": self.api_key}
        response = requests.delete(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return {"repository": repository}

    def clone_space(self, repository: str, source_name: str, source_owner_id: str) -> Dict[str, Any]:
        """
        Clone a memory space (/memory-space/clone)
        """
        url = f"{self.base_url}/memory-space/clone"
        params = {"userId": self.user_id, "apiKey": self.api_key}
        payload = {"repository": repository, "sourceName": source_name, "sourceOwnerId": source_owner_id}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return {"repository": repository}

    def get_history(self, repository: str) -> Dict[str, Any]:
        """
        Get memory space history (/memory-space/{repository}/history)
        """
        url = f"{self.base_url}/memory-space/{repository}/history"
        params = {"userId": self.user_id, "apiKey": self.api_key}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json() 