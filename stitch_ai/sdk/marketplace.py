from stitch_ai.api.marketplace import MarketplaceAPIClient

class MarketplaceSDK:
    def __init__(self, base_url: str, api_key: str):
        self.client = MarketplaceAPIClient(base_url, api_key)

    def get_memory_space_lists(self, type_, paginate=None, sort=None, filters=None):
        return self.client.get_memory_space_lists(type_, paginate, sort, filters)

    def list_memory(self, body):
        return self.client.list_memory(body)

    def purchase_memory(self, body):
        return self.client.purchase_memory(body) 