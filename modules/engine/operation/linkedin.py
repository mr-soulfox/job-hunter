import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LinkedinSearch:
    def __init__(self, driver, stack, sleep_function):
        self.driver = driver
        self.stack = stack
        self.sleep = sleep_function
        self.linkedin_input = None

    def write(self, input_id, data) -> None:
        self.linkedin_input = self.driver.find_element(By.ID, input_id)
        self.linkedin_input.click()
        self.linkedin_input.clear()
        self.linkedin_input.send_keys(data)

    def sign_in(self) -> None:
        self.write("username", os.environ["LINKEDIN_GMAIL"])
        self.write("password", os.environ["LINKEDIN_PASSWORD"])
        self.driver.find_element(By.XPATH, "//button[text()='Entrar']").click()

    def execute(self) -> None:
        self.sign_in()
        self.sleep()

        linkedin_search = self.driver.find_element(By.CSS_SELECTOR, ".search-global-typeahead__input")
        linkedin_search.click()
        linkedin_search.clear()
        linkedin_search.send_keys("{} vagas".format(self.stack))
        linkedin_search.send_keys(Keys.RETURN)
        self.sleep()

        self.driver.find_element(By.XPATH, "//button[text()='Publicações']").click()
        self.sleep()
