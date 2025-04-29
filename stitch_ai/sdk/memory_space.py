from stitch_ai.api.memory_space import MemorySpaceAPIClient, MemoryType

class MemorySpaceSDK:
    def __init__(self, base_url: str, api_key: str):
        self.client = MemorySpaceAPIClient(base_url, api_key)

    def create_space(self, repository: str, memory_type: MemoryType = MemoryType.AGENT_MEMORY):
        return self.client.create_space(repository, memory_type)

    def get_space(self, repository: str, ref=None):
        return self.client.get_space(repository, ref)

    def delete_space(self, repository: str):
        return self.client.delete_space(repository)

    def clone_space(self, repository: str, source_name: str, source_owner_id: str):
        return self.client.clone_space(repository, source_name, source_owner_id)

    def get_history(self, repository: str):
        return self.client.get_history(repository) 