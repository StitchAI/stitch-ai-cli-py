import requests
from typing import Dict, Any, Optional
from .client import BaseAPIClient

class GitAPIClient(BaseAPIClient):
    def create_repo(self, user_id: str, name: str) -> Dict[str, Any]:
        url = f"{self.base_url}/git/create"
        params = {"userId": user_id, "apiKey": self.api_key}
        payload = {"name": name}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def clone_repo(self, user_id: str, name: str, source_name: str, source_owner_id: str) -> Dict[str, Any]:
        url = f"{self.base_url}/git/clone"
        params = {"userId": user_id, "apiKey": self.api_key}
        payload = {"name": name, "sourceName": source_name, "sourceOwnerId": source_owner_id}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def list_branches(self, user_id: str, repository: str) -> Dict[str, Any]:
        url = f"{self.base_url}/git/{repository}/branches"
        params = {"userId": user_id, "apiKey": self.api_key}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def checkout_branch(self, user_id: str, repository: str, branch: str) -> Dict[str, Any]:
        url = f"{self.base_url}/git/{repository}/checkout"
        params = {"userId": user_id, "apiKey": self.api_key}
        payload = {"branch": branch}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def create_branch(self, user_id: str, repository: str, branch_name: str, base_branch: str) -> Dict[str, Any]:
        url = f"{self.base_url}/git/{repository}/branch/create"
        params = {"userId": user_id, "apiKey": self.api_key}
        payload = {"branchName": branch_name, "baseBranch": base_branch}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def delete_branch(self, user_id: str, repository: str, branch: str) -> Dict[str, Any]:
        url = f"{self.base_url}/git/{repository}/branch/{branch}"
        params = {"userId": user_id, "apiKey": self.api_key}
        response = requests.delete(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def merge(self, user_id: str, repository: str, ours: str, theirs: str, message: str) -> Dict[str, Any]:
        url = f"{self.base_url}/git/{repository}/merge"
        params = {"userId": user_id, "apiKey": self.api_key}
        payload = {"ours": ours, "theirs": theirs, "message": message}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def commit_file(self, user_id: str, repository: str, file_path: str, content: str, message: str) -> Dict[str, Any]:
        url = f"{self.base_url}/git/{repository}/commit"
        params = {"userId": user_id, "apiKey": self.api_key}
        payload = {"filePath": file_path, "content": content, "message": message}
        response = requests.post(url, params=params, json=payload, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_log(self, user_id: str, repository: str, depth: Optional[int] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/git/{repository}/log"
        params = {"userId": user_id, "apiKey": self.api_key}
        if depth is not None:
            params["depth"] = depth
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_file(self, user_id: str, repository: str, file_path: str, ref: str) -> Dict[str, Any]:
        url = f"{self.base_url}/git/{repository}/file"
        params = {"userId": user_id, "apiKey": self.api_key, "filePath": file_path, "ref": ref}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def diff(self, user_id: str, repository: str, oid1: str, oid2: str) -> Dict[str, Any]:
        url = f"{self.base_url}/git/{repository}/diff"
        params = {"userId": user_id, "apiKey": self.api_key, "oid1": oid1, "oid2": oid2}
        response = requests.get(url, params=params, headers=self.get_headers())
        response.raise_for_status()
        return response.json() 