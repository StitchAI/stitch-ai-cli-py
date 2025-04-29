import requests
from typing import Dict, Any

class BaseAPIClient:
    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the API client
        
        Args:
            base_url (str): Base URL for the API
            api_key (str): API key for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.user_id = self.get_user_id()

    def get_headers(self) -> Dict[str, str]:
        """Get the default headers for API requests"""
        return {
            "apikey": self.api_key,
            "Content-Type": "application/json",
        }
    
    def get_user_id(self) -> str:
        """Get the user ID from the API key"""
        url = f"{self.base_url}/user/api-key/user?apiKey={self.api_key}"
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response.json()['userId']


class APIClient(BaseAPIClient):
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
        url = f"{self.base_url}/user/api-key"
        params = {"userId": user_id, "hashedId": hashed_id}
        payload = {"name": name}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def handle_error(self, response: requests.Response) -> None:
        """
        Handle API error responses
        
        Args:
            response (requests.Response): Response object from the API
            
        Raises:
            Exception: With appropriate error message
        """
        try:
            error_data = response.json()
            error_message = error_data.get('message', 'Unknown error occurred')
        except ValueError:
            error_message = response.text or 'Unknown error occurred'
        
        raise Exception(f"API Error ({response.status_code}): {error_message}")