from linkedin import LinkedinSearch
from selenium.webdriver.chrome.webdriver import WebDriver

operation_params = {"driver": WebDriver, "stack": str, "sleep": any}


def execute_operation(url: str, params: operation_params) -> None:
    if url.find("linkedin") != -1:
        linkedin_search = LinkedinSearch(params["driver"], params["stack"], params["sleep"])
        linkedin_search.execute()
