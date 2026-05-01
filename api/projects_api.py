from api.base_api import BaseAPI


class ProjectsAPI(BaseAPI):

    def create_project(self, data: dict):
        return self.post("/projects", data)
