from stitch_ai.api.user import UserAPIClient

class UserSDK:
    def __init__(self, base_url: str, api_key: str):
        self.client = UserAPIClient(base_url, api_key)

    def get_user(self, user_id: str):
        return self.client.get_user(user_id)

    def get_api_keys(self, user_id: str, hashed_id: str):
        return self.client.get_api_keys(user_id, hashed_id)

    def create_api_key(self, user_id: str, hashed_id: str, name: str):
        return self.client.create_api_key(user_id, hashed_id, name)

    def delete_api_key(self, user_id: str, hashed_id: str, secret: str):
        return self.client.delete_api_key(user_id, hashed_id, secret)

    def get_user_stat(self, user_id: str):
        return self.client.get_user_stat(user_id)

    def get_user_histories(self, user_id: str, paginate=None, sort=None, filters=None):
        return self.client.get_user_histories(user_id, paginate, sort, filters)

    def get_user_memory(self, user_id: str, api_key: str, memory_names=None):
        return self.client.get_user_memory(user_id, api_key, memory_names)

    def get_user_purchases(self, user_id: str, paginate=None, sort=None, filters=None):
        return self.client.get_user_purchases(user_id, paginate, sort, filters) 