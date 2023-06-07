from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.by import By
from modules.engine.scripts.execute_search import execute


def search(driver: WebDriver, stack: str, by: str, search_class: str, sleep: any) -> None:
    try:
        execute(driver.find_element(by, search_class), stack, sleep)
    except ElementNotInteractableException:
        driver.find_element(By.CSS_SELECTOR, ".search-global-typeahead__collapsed-search-button").click()
        execute(driver.find_element(by, search_class), stack, sleep)
