from .user import UserSDK
from .marketplace import MarketplaceSDK
from .memory import MemorySDK
from .memory_space import MemorySpaceSDK
from .git import GitSDK

class StitchSDK:
    def __init__(self, base_url, api_key):
        self.user = UserSDK(base_url, api_key)
        self.memory = MemorySDK(base_url, api_key)
        self.marketplace = MarketplaceSDK(base_url, api_key)
        self.memory_space = MemorySpaceSDK(base_url, api_key)
        self.git = GitSDK(base_url, api_key)

__all__ = ["StitchSDK"] 