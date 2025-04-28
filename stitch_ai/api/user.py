import requests
from typing import Dict, Any, Optional
from .client import BaseAPIClient

class UserAPIClient(BaseAPIClient):
    def get_user(self, user_id: str) -> Dict[str, Any]:
        """
        Get user info (/user)
        """
        url = f"{self.base_url}/user"
        params = {"userId": user_id}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_api_keys(self, user_id: str, hashed_id: str) -> Dict[str, Any]:
        """
        Get API keys for a user (/user/api-key)
        """
        url = f"{self.base_url}/user/api-key"
        params = {"userId": user_id, "hashedId": hashed_id}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def create_api_key(self, user_id: str, hashed_id: str, name: str) -> Dict[str, Any]:
        """
        Create a new API key for a user (/user/api-key)
        """
        url = f"{self.base_url}/user/api-key"
        params = {"userId": user_id, "hashedId": hashed_id}
        payload = {"name": name}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def delete_api_key(self, user_id: str, hashed_id: str, secret: str) -> Dict[str, Any]:
        """
        Delete an API key (/user/api-key/{secret})
        """
        url = f"{self.base_url}/user/api-key/{secret}"
        params = {"userId": user_id, "hashedId": hashed_id}
        response = requests.delete(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_user_stat(self, user_id: str) -> Dict[str, Any]:
        """
        Get user dashboard stats (/user/dashboard/stat)
        """
        url = f"{self.base_url}/user/dashboard/stat"
        params = {"userId": user_id}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_user_histories(self, user_id: str, paginate: Optional[str] = None, sort: Optional[str] = None, filters: Optional[str] = None) -> Dict[str, Any]:
        """
        Get user dashboard histories (/user/dashboard/histories)
        """
        url = f"{self.base_url}/user/dashboard/histories"
        params = {"userId": user_id}
        if paginate:
            params["paginate"] = paginate
        if sort:
            params["sort"] = sort
        if filters:
            params["filters"] = filters
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_user_memory(self, user_id: str, api_key: str, memory_names: Optional[str] = None) -> Dict[str, Any]:
        """
        Get user memory (/user/memory)
        """
        url = f"{self.base_url}/user/memory"
        params = {"userId": user_id, "apiKey": api_key}
        if memory_names:
            params["memoryNames"] = memory_names
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_user_purchases(self, user_id: str, paginate: Optional[str] = None, sort: Optional[str] = None, filters: Optional[str] = None) -> Dict[str, Any]:
        """
        Get user marketplace purchases (/user/marketplace/purchases)
        """
        url = f"{self.base_url}/user/marketplace/purchases"
        params = {"userId": user_id}
        if paginate:
            params["paginate"] = paginate
        if sort:
            params["sort"] = sort
        if filters:
            params["filters"] = filters
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json() 