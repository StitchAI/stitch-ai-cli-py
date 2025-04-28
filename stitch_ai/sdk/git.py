from stitch_ai.api.git import GitAPIClient

class GitSDK:
    def __init__(self, base_url: str, api_key: str):
        self.client = GitAPIClient(base_url, api_key)

    def create_repo(self, user_id: str, name: str):
        return self.client.create_repo(user_id, name)

    def clone_repo(self, user_id: str, name: str, source_name: str, source_owner_id: str):
        return self.client.clone_repo(user_id, name, source_name, source_owner_id)

    def list_branches(self, user_id: str, repository: str):
        return self.client.list_branches(user_id, repository)

    def checkout_branch(self, user_id: str, repository: str, branch: str):
        return self.client.checkout_branch(user_id, repository, branch)

    def create_branch(self, user_id: str, repository: str, branch_name: str, base_branch: str):
        return self.client.create_branch(user_id, repository, branch_name, base_branch)

    def delete_branch(self, user_id: str, repository: str, branch: str):
        return self.client.delete_branch(user_id, repository, branch)

    def merge(self, user_id: str, repository: str, ours: str, theirs: str, message: str):
        return self.client.merge(user_id, repository, ours, theirs, message)

    def commit_file(self, user_id: str, repository: str, file_path: str, content: str, message: str):
        return self.client.commit_file(user_id, repository, file_path, content, message)

    def get_log(self, user_id: str, repository: str, depth=None):
        return self.client.get_log(user_id, repository, depth)

    def get_file(self, user_id: str, repository: str, file_path: str, ref: str):
        return self.client.get_file(user_id, repository, file_path, ref)

    def diff(self, user_id: str, repository: str, oid1: str, oid2: str):
        return self.client.diff(user_id, repository, oid1, oid2) 