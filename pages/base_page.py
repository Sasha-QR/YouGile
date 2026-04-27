from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)
