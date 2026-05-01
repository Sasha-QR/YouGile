from pages.base_page import BasePage


class LoginPage(BasePage):

    def open_login(self, url: str):
        self.open(url)
