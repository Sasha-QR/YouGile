from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    URL = "https://ru.yougile.com/team/"

    EMAIL_INPUT = (By.CSS_SELECTOR, '[type="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[type="password"]')
    LOGIN_BUTTON = (By.XPATH, "//div[text()='Войти']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        # пример: после логина появляется какой-то элемент
        return self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
