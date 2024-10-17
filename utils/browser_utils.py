from utils.helper_utils import read_file
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from helpers.constants.framework_constants import FrameworkConstants as Fc

details = read_file(Fc.details)

def prepare_browser(context):
    browser = details["browser"]
    if browser == "Chrome":
        options = ChromeOptions()
    elif browser == "Firefox":
        options = FirefoxOptions()
    else:
        options = ChromiumOptions()
    if details["headless"]:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    context.driver = webdriver.Remote(
        command_executor=f"http://{details["selenium_host_ip"]}:4444/wd/hub",
        options=options
    )
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()