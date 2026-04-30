from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    # --- локаторы ---
    PROFILE_ICON = (By.CSS_SELECTOR, "img")
    CREATE_PROJECT_BUTTON = (By.XPATH, "//button[contains(., 'Создать')] | //div[contains(., 'Создать')]")
    PROJECT_NAME_INPUT = (By.CSS_SELECTOR, "input")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(., 'Создать')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # --- загрузка страницы ---
    def is_loaded(self):
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        return self.wait.until(
            EC.presence_of_element_located(self.PROFILE_ICON)
        )

    # --- создание проекта ---
    def create_project(self, name: str):
        self.is_loaded()

        create_button = self.wait.until(
            EC.element_to_be_clickable(self.CREATE_PROJECT_BUTTON)
        )
        create_button.click()

        input_field = self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_NAME_INPUT)
        )
        input_field.send_keys(name)

        self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()

    # --- проверка проекта ---
    def project_exists(self, name: str):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()='{name}']"))
        )