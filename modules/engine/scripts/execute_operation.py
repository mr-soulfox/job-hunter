from modules.engine.operation.linkedin import LinkedinSearch
from selenium.webdriver.chrome.webdriver import WebDriver


def execute(driver: WebDriver, platform: str, stack: str, repeat: int, sleep: any) -> None:
    if platform.lower() == "linkedin":
        linkedin_search = LinkedinSearch(driver, stack, sleep)
        linkedin_search.execute(repeat)
        return
