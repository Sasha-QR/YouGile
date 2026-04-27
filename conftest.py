import pytest
import uuid
from selenium import webdriver
from api.projects_api import ProjectsAPI
from api.users_api import UsersAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def user_id() -> str:
    return "5eeb1740-dc2f-4402-9afa-169518ad082b"


@pytest.fixture
def project_id(user_id: str) -> str:
    api = ProjectsAPI()

    data = {
        "title": f"Test Project {uuid.uuid4()}",
        "users": {
            user_id: "admin"
        }
    }

    response = api.create_project(data)
    return response.json()["id"]


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)

    yield driver
    driver.quit()