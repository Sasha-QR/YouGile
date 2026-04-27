import pytest
import allure
from api.projects_api import ProjectsAPI
import uuid


@allure.title("Создание проекта (позитивный)")
@allure.story("Projects API")
@pytest.mark.api
def test_create_project(user_id):
    api = ProjectsAPI()

    title = f"Test Project {uuid.uuid4()}"
    
    data = {
        "title": "Test Project",
        "users": {
            user_id: "admin"
        }
    }

    with allure.step("Создаем проект"):
        response = api.create_project(data)

    with allure.step("Проверяем статус"):
        assert response.status_code == 201


@allure.title("Создание проекта без title")
@allure.story("Projects API")
@pytest.mark.api
def test_create_project_no_title(user_id):
    api = ProjectsAPI()

    data = {
        "users": {
            user_id: "admin"
        }
    }

    response = api.create_project(data)

    assert response.status_code == 400


@allure.title("Получение проекта")
@allure.story("Projects API")
@pytest.mark.api
def test_get_project(project_id):
    api = ProjectsAPI()

    response = api.get(f"/projects/{project_id}")

    assert response.status_code == 200


@allure.title("Получение несуществующего проекта")
@allure.story("Projects API")
@pytest.mark.api
def test_get_invalid_project():
    api = ProjectsAPI()

    response = api.get("/projects/invalid-id")

    assert response.status_code >= 400


@allure.title("Проверка лимита API")
@allure.story("Projects API")
@pytest.mark.api
def test_rate_limit():
    api = ProjectsAPI()

    responses = []
    for _ in range(10):
        responses.append(api.get("/projects").status_code)

    assert any(code in [200, 429] for code in responses)