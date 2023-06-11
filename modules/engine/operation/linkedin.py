import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from modules.engine.operation.Linkedin.write import write
from modules.engine.operation.Linkedin.search import search
from modules.engine.operation.Linkedin.label import go_to_label
from modules.engine.operation.General.scroll_down import page_down
from modules.engine.operation.Linkedin.save_list import save as save_user_list


class LinkedinSearch:
    driver: WebDriver
    stack: str
    sleep: any

    def __init__(self, driver: WebDriver, stack: str, sleep_function: any):
        self.driver = driver
        self.stack = stack
        self.sleep = sleep_function

    def sign_in(self) -> None:
        write(self.driver, By.ID, "username", str(os.environ.get("LINKEDIN_EMAIL")))
        write(self.driver, By.ID, "password", str(os.environ.get("LINKEDIN_PASSWORD")))
        self.driver.find_element(By.XPATH, "//button[text()='Entrar']").click()

    def execute(self, scroll_repeat: int) -> None:
        self.sign_in()
        self.sleep()

        search(self.driver, self.stack, By.CSS_SELECTOR, ".search-global-typeahead__input", self.sleep)
        self.sleep()

        go_to_label(self.driver, "publicações")
        self.sleep()

        page_down(self.driver, self.sleep, scroll_repeat)
        self.sleep()

        save_user_list(self.driver, self.sleep)
        self.sleep()

        self.driver.close()
