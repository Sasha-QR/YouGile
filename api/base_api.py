import requests
from config.config import BASE_URL, API_KEY


class BaseAPI:

    def __init__(self) -> None:
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

    def post(self, endpoint: str, data: dict) -> requests.Response:
        return requests.post(f"{BASE_URL}{endpoint}", json=data, headers=self.headers)

    def get(self, endpoint: str) -> requests.Response:
        return requests.get(f"{BASE_URL}{endpoint}", headers=self.headers)

    def put(self, endpoint: str, data: dict) -> requests.Response:
        return requests.put(f"{BASE_URL}{endpoint}", json=data, headers=self.headers)
