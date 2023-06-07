from selenium.webdriver.chrome.webdriver import WebDriver


def write(driver: WebDriver, by: str, search: str, data: str) -> None:
    linkedin_input = driver.find_element(by, search)
    linkedin_input.click()
    linkedin_input.clear()
    linkedin_input.send_keys(data)
