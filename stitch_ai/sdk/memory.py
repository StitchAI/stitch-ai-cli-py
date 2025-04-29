from stitch_ai.api.memory import MemoryAPIClient

class MemorySDK:
    def __init__(self, base_url: str, api_key: str):
        self.client = MemoryAPIClient(base_url, api_key)

    def push_memory(self, repository: str, message: str, files: list):
        return self.client.push_memory(repository, message, files) 