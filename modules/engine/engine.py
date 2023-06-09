import requests
from requests.exceptions import ConnectionError
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from modules.engine.config.set_chrome_driver import chrome_setup
from modules.engine.scripts.verify_page import verify_if_exist
from modules.engine.scripts.execute_operation import execute


class SearchEngine:
    driver: WebDriver
    url: str
    platform: str
    stack: str
    sleep_time: int
    repeat: int

    def __init__(self, url: str, platform: str, stack: str, repeat: int, sleep_time: int = 3) -> None:
        self.url = url
        self.stack = stack
        self.sleep_time = sleep_time
        self.repeat = repeat
        self.platform = platform
        self.driver = chrome_setup()

    def sleep(self, half: bool = False) -> None:
        if half:
            time.sleep(self.sleep_time * 0.5)
            return

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

            execute(self.driver, self.platform, self.stack, self.repeat, self.sleep)
