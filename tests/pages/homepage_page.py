from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class Homepage:

    products_label = (By.XPATH, "//span[normalize-space()='Products']")

    def __init__(self, driver):
        self.driver = driver
        self.bp = BasePage(self.driver)

    def get_text_from_page(self):
        self.bp.get_text(self.products_label[0], self.products_label[1])