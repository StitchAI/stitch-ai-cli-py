import requests
from typing import Dict, Any, Optional
from .client import BaseAPIClient

class MarketplaceAPIClient(BaseAPIClient):
    def get_memory_space_lists(self, type_: str, paginate: Optional[str] = None, sort: Optional[str] = None, filters: Optional[str] = None) -> Dict[str, Any]:
        """
        Get listed memory spaces or external memories (/marketplace)
        """
        url = f"{self.base_url}/marketplace"
        params = {"type": type_, "userId": self.user_id}
        if paginate:
            params["paginate"] = paginate
        if sort:
            params["sort"] = sort
        if filters:
            params["filters"] = filters
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def list_memory(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        List agent memory or external memory (/marketplace/list)
        """
        url = f"{self.base_url}/marketplace/list"
        params = {"userId": self.user_id, "apiKey": self.api_key}
        payload = body
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return {"body": body}

    def purchase_memory(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Purchase a listed memory (/marketplace/purchase)
        """
        url = f"{self.base_url}/marketplace/purchase"
        params = {"userId": self.user_id, "apiKey": self.api_key}
        payload = body
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return {"body": body} 