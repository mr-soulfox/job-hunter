from selenium.webdriver.chrome.webdriver import WebDriver
from modules.engine.operation.Linkedin.format_url import format_user_url as format_uu
from os import path
import csv
from urllib import parse


def save(driver: WebDriver, sleep: any) -> None:
    with open(path.join(path.dirname(__file__), "..", "..", "scripts", "js_script", "get_url.js")) as script_file:
        script = script_file.read()
        list_users = driver.execute_script(script)

        with open(path.join("temp", "temp.csv"), 'w', newline="", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["user_name", "user_url"])

            for user_url in list_users:
                csv_writer.writerow([
                    format_uu(user_url, only_name=True),
                    format_uu(user_url, only_url=True)
                ])

            csv_file.close()

        script_file.close()
