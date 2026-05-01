from api.base_api import BaseAPI


class BoardsAPI(BaseAPI):

    def create_board(self, data: dict):
        return self.post("/boards", data)
