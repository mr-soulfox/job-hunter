from selenium.webdriver.chrome.webdriver import WebDriver
from os import path
import csv
from urllib import parse


def is_company(url: str) -> str:
    return "/in/" if url.find("/in/") else "/company/"


def save(driver: WebDriver, sleep: any) -> None:
    with open(path.join(path.dirname(__file__), "..", "..", "scripts", "js_script", "get_url.js")) as script_file:
        script = script_file.read()
        list_users = driver.execute_script(script)
        sleep()

        with open(path.join("temp", "temp.csv"), 'w', newline="", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["user_name", "user_url"])

            for user_url in list_users:
                csv_writer.writerow([
                    parse.unquote(str(user_url).split("?")[0].split(is_company(str(user_url)))[1], encoding="utf-8"),
                    str(user_url).split("?")[0]
                ])

            csv_file.close()

        script_file.close()
