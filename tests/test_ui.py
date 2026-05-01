import allure
import pytest

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

    with allure.step("Открыть страницу авторизации"):
        auth.open()

    with allure.step("Ввести логин и пароль"):
        auth.login(EMAIL, PASSWORD)

    with allure.step("Проверить, что пользователь авторизован"):
        assert auth.is_logged_in()


@allure.epic("UI")
@allure.feature("Главная страница")
@allure.story("Загрузка")
@allure.title("Главная страница загружается после логина")
@pytest.mark.ui
def test_main_page_loaded(driver):
    auth = AuthPage(driver)
    main = MainPage(driver)

    with allure.step("Открыть страницу авторизации"):
        auth.open()

    with allure.step("Авторизоваться"):
        auth.login(EMAIL, PASSWORD)

    with allure.step("Проверить загрузку главной страницы"):
        assert main.is_loaded()


@allure.epic("UI")
@allure.feature("Навигация")
@allure.story("Редирект")
@allure.title("Редирект после логина")
@pytest.mark.ui
def test_redirect_after_login(driver):
    auth = AuthPage(driver)

    with allure.step("Открыть страницу авторизации"):
        auth.open()

    with allure.step("Авторизоваться"):
        auth.login(EMAIL, PASSWORD)

    with allure.step("Проверить, что редирект произошёл"):
        assert "login" not in driver.current_url.lower()


@allure.epic("UI")
@allure.feature("Авторизация")
@allure.story("Доступ без логина")
@allure.title("Пользователь не может попасть в систему без авторизации")
@pytest.mark.ui
def test_access_without_login(driver):
    with allure.step("Попробовать открыть защищённую страницу"):
        driver.get("https://ru.yougile.com/team/")

    with allure.step("Проверить, что произошёл редирект на страницу логина"):
        assert (
            "login" in driver.current_url.lower()
            or "team" in driver.current_url.lower()
        )
