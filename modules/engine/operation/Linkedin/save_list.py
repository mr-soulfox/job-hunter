from selenium.webdriver.chrome.webdriver import WebDriver
from os import path
from modules.engine.operation.Linkedin.get_info import get_user_info


def save(driver: WebDriver, sleep: any) -> None:
    list_users: list = []

    with open(path.join(path.dirname(__file__), "js_script", "get_url.js")) as file:
        script = file.read()
        list_users = driver.execute_script(script)
        sleep()
        file.close()

    get_user_info(list_users[0])
