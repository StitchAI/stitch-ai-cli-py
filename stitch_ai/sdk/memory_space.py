from stitch_ai.api.memory_space import MemorySpaceAPIClient

class MemorySpaceSDK:
    def __init__(self, base_url: str, api_key: str):
        self.client = MemorySpaceAPIClient(base_url, api_key)

    def create_space(self, user_id: str, repository: str):
        return self.client.create_space(user_id, repository)

    def get_space(self, user_id: str, repository: str, ref=None):
        return self.client.get_space(user_id, repository, ref)

    def delete_space(self, user_id: str, repository: str):
        return self.client.delete_space(user_id, repository)

    def clone_space(self, user_id: str, repository: str, source_name: str, source_owner_id: str):
        return self.client.clone_space(user_id, repository, source_name, source_owner_id)

    def get_history(self, user_id: str, repository: str):
        return self.client.get_history(user_id, repository) 