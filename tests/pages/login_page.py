from selenium.webdriver.common.by import By
from helpers.constants.framework_constants import FrameworkConstants
from tests.pages.base_page import BasePage
from utils.helper_utils import read_file

details = read_file(FrameworkConstants.details)


class LoginPage:
    username_text_box = (By.ID, "user-name")
    password_text_box = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.url = details["url"]
        self.bp = BasePage(self.driver)

    def navigate_to_page(self):
        self.bp.open_page(self.url)

    def enter_username(self, username):
        self.bp.send_keys(self.username_text_box[0], self.username_text_box[1], username)

    def enter_password(self, password):
        self.bp.send_keys(self.password_text_box[0], self.password_text_box[1], password)

    def click_login_button(self):
        self.bp.click(self.login_button[0], self.login_button[1])

    def get_page_tile(self):
        return self.bp.get_title()
