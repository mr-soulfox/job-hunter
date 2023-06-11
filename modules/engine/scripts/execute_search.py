from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement


def execute(element: WebElement, stack: str, sleep: any) -> None:
    element.click()
    element.clear()
    element.send_keys(f'"{stack}" + "oportunidade" or "vaga"')
    element.send_keys(Keys.RETURN)
