from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from os import environ


def chrome_setup() -> WebDriver:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-notifications")

    if environ.get("DEVELOPMENT") == "ON":
        chrome_options.add_argument("--auto-open-devtools-for-tabs")

    return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
