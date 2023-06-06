import requests
from requests.exceptions import ConnectionError
import time
from .config.set_chrome_driver import chrome_setup
from .operation.linkedin import LinkedinSearch


class SearchEngine:
    def __init__(self, url, stack, sleep_time=3):
        self.url = url
        self.stack = stack
        self.sleep_time = sleep_time
        self.driver = chrome_setup()

    def sleep(self) -> None:
        time.sleep(self.sleep_time)

    def verify(self) -> bool:
        try:
            res = requests.get(self.url)
            return True

        except ConnectionError:
            return False

        return False

    def search(self) -> None:
        if not self.verify():
            print("Url not exist " + self.url)
            return None

        driver = self.driver
        driver.get(self.url)

        self.sleep()

        if self.url.find("linkedin") != -1:
            linkedin_search = LinkedinSearch(self.driver, self.stack, self.sleep)
            linkedin_search.execute()
            self.sleep()
