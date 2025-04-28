from stitch_ai.api.marketplace import MarketplaceAPIClient

class MarketplaceSDK:
    def __init__(self, base_url: str, api_key: str):
        self.client = MarketplaceAPIClient(base_url, api_key)

    def get_memory_space_lists(self, type_, user_id=None, paginate=None, sort=None, filters=None):
        return self.client.get_memory_space_lists(type_, user_id, paginate, sort, filters)

    def list_memory(self, user_id, repository, api_key, body):
        return self.client.list_memory(user_id, repository, api_key, body)

    def purchase_memory(self, user_id, api_key, body):
        return self.client.purchase_memory(user_id, api_key, body) 