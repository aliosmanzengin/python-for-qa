"""
utilities.py
"""

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def handle_stale_element(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except StaleElementReferenceException:
            args[0]._driver.refresh()
            WebDriverWait(args[0]._driver, 10).until(EC.presence_of_element_located(args[1]))
            return func(*args, **kwargs)

    return wrapper


@handle_stale_element
def click_element(self, locator):
    element = self._find(locator)
    element.click()

# Usage
# click_element(locator)
