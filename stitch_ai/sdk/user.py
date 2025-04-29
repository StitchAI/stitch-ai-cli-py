from stitch_ai.api.user import UserAPIClient

class UserSDK:
    def __init__(self, base_url: str, api_key: str):
        self.client = UserAPIClient(base_url, api_key)

    def get_user(self):
        return self.client.get_user()

    def get_user_stat(self):
        return self.client.get_user_stat()

    def get_user_histories(self, paginate=None, sort=None, filters=None):
        return self.client.get_user_histories(paginate, sort, filters)

    def get_user_memory(self, memory_names=None):
        return self.client.get_user_memory(memory_names)

    def get_user_purchases(self, paginate=None, sort=None, filters=None):
        return self.client.get_user_purchases(paginate, sort, filters) 