import requests
from typing import Dict, Any, Optional
from .client import BaseAPIClient

class UserAPIClient(BaseAPIClient):
    def get_user(self) -> Dict[str, Any]:
        """
        Get user info (/user)
        """
        url = f"{self.base_url}/user"
        params = {"userId": self.user_id}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_user_stat(self) -> Dict[str, Any]:
        """
        Get user dashboard stats (/user/dashboard/stat)
        """
        url = f"{self.base_url}/user/dashboard/stat"
        params = {"userId": self.user_id}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_user_histories(self, paginate: Optional[str] = None, sort: Optional[str] = None, filters: Optional[str] = None) -> Dict[str, Any]:
        """
        Get user dashboard histories (/user/dashboard/histories)
        """
        url = f"{self.base_url}/user/dashboard/histories"
        params = {"userId": self.user_id}
        if paginate:
            params["paginate"] = paginate
        if sort:
            params["sort"] = sort
        if filters:
            params["filters"] = filters
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_user_memory(self, memory_names: Optional[str] = None) -> Dict[str, Any]:
        """
        Get user memory (/user/memory)
        """
        url = f"{self.base_url}/user/memory/all"
        params = {"userId": self.user_id, "apiKey": self.api_key}
        if memory_names:
            params["memoryNames"] = memory_names
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_user_purchases(self, paginate: Optional[str] = None, sort: Optional[str] = None, filters: Optional[str] = None) -> Dict[str, Any]:
        """
        Get user marketplace purchases (/user/marketplace/purchases)
        """
        url = f"{self.base_url}/user/marketplace/purchases"
        params = {"userId": self.user_id}
        if paginate:
            params["paginate"] = paginate
        if sort:
            params["sort"] = sort
        if filters:
            params["filters"] = filters
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json() 