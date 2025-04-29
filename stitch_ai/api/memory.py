import requests
from typing import Dict, Any
from .client import BaseAPIClient

class MemoryAPIClient(BaseAPIClient):
    def push_memory(self, repository: str, message: str, files: list) -> Dict[str, Any]:
        """
        Commit memory to a memory space (/memory/{repository}/create)
        """
        url = f"{self.base_url}/memory/{repository}/create"
        params = {"userId": self.user_id, "apiKey": self.api_key}
        payload = {"files": files, "message": message}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return {"repository": repository, "message": message, "files": files}
