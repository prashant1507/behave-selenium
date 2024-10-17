from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def send_keys(self, by: By, locator, text):
        self.driver.find_element(by, locator).send_keys(text)

    def click(self, by: By, locator):
        self.driver.find_element(by, locator).click()

    def get_title(self):
        return str(self.driver.title).strip()

    def get_text(self, by: By, locator):
        return str(self.driver.find_element(by, locator).text).strip()