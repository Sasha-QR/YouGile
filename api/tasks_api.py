from api.base_api import BaseAPI


class TasksAPI(BaseAPI):

    def create_task(self, data: dict):
        return self.post("/tasks", data)

    def move_task(self, task_id: str, data: dict):
        return self.put(f"/tasks/{task_id}", data)
