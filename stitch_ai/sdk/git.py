from stitch_ai.api.git import GitAPIClient

class GitSDK:
    def __init__(self, base_url: str, api_key: str):
        self.client = GitAPIClient(base_url, api_key)

    def create_repo(self, name: str):
        return self.client.create_repo(name)   

    def clone_repo(self, name: str, source_name: str, source_owner_id: str):
        return self.client.clone_repo(name, source_name, source_owner_id)

    def list_branches(self, repository: str):
        return self.client.list_branches(repository)

    def checkout_branch(self, repository: str, branch: str):
        return self.client.checkout_branch(repository, branch)

    def create_branch(self, repository: str, branch_name: str, base_branch: str):
        return self.client.create_branch(repository, branch_name, base_branch)

    def delete_branch(self, repository: str, branch: str):
        return self.client.delete_branch(repository, branch)

    def merge(self, repository: str, ours: str, theirs: str, message: str):
        return self.client.merge(repository, ours, theirs, message)

    def commit_file(self, repository: str, file_path: str, content: str, message: str):
        return self.client.commit_file(repository, file_path, content, message)

    def get_log(self, repository: str, depth=None):
        return self.client.get_log(repository, depth)

    def get_file(self, repository: str, file_path: str, ref: str):
        return self.client.get_file(repository, file_path, ref)

    def diff(self, repository: str, oid1: str, oid2: str):
        return self.client.diff(repository, oid1, oid2) 