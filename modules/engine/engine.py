import requests
from requests.exceptions import ConnectionError
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from .config.set_chrome_driver import chrome_setup
from .operation.linkedin import LinkedinSearch
from .scripts.verify_page import verify_if_exist


class SearchEngine:
    driver: WebDriver
    url: str
    platform: str
    stack: str
    sleep_time: int

    def __init__(self, url: str, platform: str, stack: str, sleep_time: int = 3):
        self.url = url
        self.stack = stack
        self.sleep_time = sleep_time
        self.platform = platform
        self.driver = chrome_setup()

    def sleep(self) -> None:
        time.sleep(self.sleep_time)

    def verify(self) -> bool:
        try:
            res = requests.get(self.url)
            return verify_if_exist(res)

        except ConnectionError:
            return False

    def search(self) -> None:
        if self.verify():
            driver = self.driver
            driver.get(self.url)
            self.sleep()

            if self.platform == "linkedin":
                linkedin_search = LinkedinSearch(self.driver, self.stack, self.sleep)
                linkedin_search.execute()
                self.sleep()
                self.sleep()
                self.sleep()
                return

        return
