import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv
from .api.client import APIClient

class KeySDK:
    """
    SDK class for API key management on the Stitch AI platform.
    """
    def __init__(self, base_url: str = "https://api-demo.stitch-ai.co", api_key: Optional[str] = None):
        load_dotenv()
        self.api_key = api_key or os.environ.get("STITCH_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided either directly or via STITCH_API_KEY environment variable")
        self.api_client = APIClient(base_url, self.api_key)

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
        return self.api_client.create_key(user_id, hashed_id, name) 