import pytest
import allure
from config.config import UI_URL
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Открытие сайта")
@allure.story("UI")
@pytest.mark.ui
def test_open_site(driver):
    driver.get(UI_URL)
    time.sleep(5)
    driver.implicitly_wait(30)
    assert driver.title != ""


@allure.title("Проверка загрузки")
@allure.story("UI")
@pytest.mark.ui
def test_page_load(driver):
    driver.get(UI_URL)
    time.sleep(3)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    assert driver.current_url.startswith("https")


@allure.title("Обновление страницы")
@allure.story("UI")
@pytest.mark.ui
def test_refresh(driver):
    driver.get(UI_URL)
    time.sleep(3)
    driver.implicitly_wait(10)
    driver.refresh()
    assert driver.title != ""


@allure.title("Проверка доступности DOM")
@allure.story("UI")
@pytest.mark.ui
def test_dom_loaded(driver):
    driver.get(UI_URL)

    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


@allure.title("Проверка title")
@allure.story("UI")
@pytest.mark.ui
def test_title_not_empty(driver):
    driver.get(UI_URL)

    WebDriverWait(driver, 20).until(
        lambda d: d.title != ""
    )

    assert driver.title != ""