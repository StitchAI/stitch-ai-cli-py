import requests
from typing import Dict, Any
from .client import BaseAPIClient

class MemoryAPIClient(BaseAPIClient):
    def create_space(self, user_id: str, repository: str) -> Dict[str, Any]:
        url = f"{self.base_url}/memory-space/create"
        params = {"userId": user_id, "apiKey": self.api_key}
        payload = {"repository": repository}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def push_memory(self, user_id: str, repository: str, message: str, files: list) -> Dict[str, Any]:
        url = f"{self.base_url}/memory/{repository}/create"
        params = {"userId": user_id, "apiKey": self.api_key}
        payload = {"files": files, "message": message}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def pull_memory(self, user_id: str, repository: str, ref: str = "main") -> Dict[str, Any]:
        url = f"{self.base_url}/memory-space/{repository}"
        params = {"userId": user_id, "apiKey": self.api_key, "ref": ref}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def pull_external_memory(self, memory_id: str) -> Dict[str, Any]:
        url = f"{self.base_url}/memory/external/{memory_id}"
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def list_spaces(self, user_id: str) -> Dict[str, Any]:
        url = f"{self.base_url}/user/memory-space"
        params = {"userId": user_id}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def list_memories(self, user_id: str, repository: str) -> Dict[str, Any]:
        url = f"{self.base_url}/memory-space/{repository}/history"
        params = {"userId": user_id, "apiKey": self.api_key}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json() 