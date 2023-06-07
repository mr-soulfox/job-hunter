from selenium.webdriver.chrome.webdriver import WebDriver
from os import path


def save(driver: WebDriver, sleep: any) -> None:
    list_users: list = []

    with open(path.join(path.dirname(__file__), "js_script", "get_url.js")) as file:
        script = file.read()
        list_users = driver.execute_script(script)
        sleep()
        file.close()

    for link in list_users:
        print(link)
