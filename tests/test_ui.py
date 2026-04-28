import pytest
import allure
from pages.auth_page import AuthPage
from pages.main_page import MainPage


EMAIL = "твой логин"
PASSWORD = "твой пароль"


@allure.title("Успешная авторизация")
@pytest.mark.ui
def test_login_success(driver):
    auth = AuthPage(driver)

    auth.open()
    auth.login(EMAIL, PASSWORD)

    assert auth.is_logged_in()


@allure.title("Загрузка главной страницы после логина")
@pytest.mark.ui
def test_main_page_loaded(driver):
    auth = AuthPage(driver)
    main = MainPage(driver)

    auth.open()
    auth.login(EMAIL, PASSWORD)

    assert main.is_loaded()


@allure.title("Проверка успешной авторизации (UI)")
@pytest.mark.ui
def test_user_logged_in(driver):
    auth = AuthPage(driver)
    main = MainPage(driver)

    auth.open()
    auth.login(EMAIL, PASSWORD)

    assert main.is_loaded()