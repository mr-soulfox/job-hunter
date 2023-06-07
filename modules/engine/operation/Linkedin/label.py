from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def go_to_label(driver: WebDriver, label_text: str) -> None:
    driver.find_element(By.XPATH, "//button[text()='{}']".format(label_text.capitalize())).click()
