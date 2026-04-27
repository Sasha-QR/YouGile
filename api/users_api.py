from api.base_api import BaseAPI


class UsersAPI(BaseAPI):

    def get_users(self) -> dict:
        response = self.get("/users")
        return response.json()