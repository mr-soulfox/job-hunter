import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver


class LinkedinSearch:
    driver: WebDriver
    stack: str
    sleep: any

    def __init__(self, driver: WebDriver, stack: str, sleep_function: any):
        self.driver = driver
        self.stack = stack
        self.sleep = sleep_function

    def write(self, by: str, search: str, data: str) -> None:
        linkedin_input = self.driver.find_element(by, search)
        linkedin_input.click()
        linkedin_input.clear()
        linkedin_input.send_keys(data)

    def sign_in(self) -> None:
        self.write(By.ID, "username", str(os.environ.get("LINKEDIN_EMAIL")))
        self.write(By.ID, "password", str(os.environ.get("LINKEDIN_PASSWORD")))
        self.driver.find_element(By.XPATH, "//button[text()='Entrar']").click()

    def search(self) -> None:
        linkedin_search = self.driver.find_element(By.CSS_SELECTOR, ".search-global-typeahead__input")
        linkedin_search.click()
        linkedin_search.clear()
        linkedin_search.send_keys("{} vagas".format(self.stack))
        linkedin_search.send_keys(Keys.RETURN)

    def execute(self) -> None:
        self.sign_in()
        self.sleep()

        self.search()
        self.sleep()

        self.driver.find_element(By.XPATH, "//button[text()='Publicações']").click()
        self.sleep()
