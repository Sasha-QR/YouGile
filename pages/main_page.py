from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    PROFILE_ICON = (By.CSS_SELECTOR, "img")  # уточни локатор
    PROJECT_BUTTON = (By.XPATH, "//div[contains(text(),'Проекты')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def is_loaded(self):
        return self.wait.until(
            EC.presence_of_element_located(self.PROFILE_ICON)
        )

    def open_projects(self):
        self.wait.until(EC.element_to_be_clickable(self.PROJECT_BUTTON)).click()
