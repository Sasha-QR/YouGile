import pytest
import allure
import uuid

from pages.auth_page import AuthPage
from pages.main_page import MainPage


EMAIL = "твой логин"
PASSWORD = "твой пароль"



@allure.epic("UI")
@allure.feature("Авторизация")
@allure.story("Успешный вход")
@allure.title("Успешная авторизация")
@pytest.mark.ui
def test_login_success(driver):
    auth = AuthPage(driver)

    auth.open()
    auth.login(EMAIL, PASSWORD)

    assert auth.is_logged_in()



@allure.epic("UI")
@allure.feature("Главная страница")
@allure.story("Загрузка")
@allure.title("Загрузка главной страницы после логина")
@pytest.mark.ui
def test_main_page_loaded(driver):
    auth = AuthPage(driver)
    main = MainPage(driver)

    auth.open()
    auth.login(EMAIL, PASSWORD)

    assert main.is_loaded()



@allure.epic("UI")
@allure.feature("Навигация")
@allure.story("Переход после логина")
@allure.title("Проверка URL после авторизации")
@pytest.mark.ui
def test_url_after_login(driver):
    auth = AuthPage(driver)

    auth.open()
    auth.login(EMAIL, PASSWORD)

    assert "login" not in driver.current_url.lower()
    assert "yougile" in driver.current_url.lower()



@allure.epic("UI")
@allure.feature("Навигация")
@allure.story("Редирект после логина")
@allure.title("Проверка редиректа после логина")
@pytest.mark.ui
def test_redirect_after_login(driver):
    auth = AuthPage(driver)

    auth.open()
    auth.login(EMAIL, PASSWORD)

    assert "login" not in driver.current_url.lower()