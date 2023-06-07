import time
from selenium.webdriver.chrome.webdriver import WebDriver


def page_down(driver: WebDriver, sleep: any, repeat: int = 5) -> None:
    last_height: int = int(driver.execute_script("return document.body.scrollHeight"))
    index: int = 0

    options: str = "{top: document.body.scrollHeight, left: 0, behavior: 'smooth'}"

    if repeat <= 0:
        repeat = 5

    while True:
        if index > repeat:
            break

        driver.execute_script("window.scrollTo({});".format(options))
        sleep(True)

        new_height: int = int(driver.execute_script("return document.body.scrollHeight"))
        if new_height == last_height:
            break

        last_height = new_height
        index += 1
