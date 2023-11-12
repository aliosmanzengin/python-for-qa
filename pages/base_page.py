"""
base_page.py
"""

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _hover(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        element = self._find(locator)
        ActionChains(self._driver).move_to_element(element).perform()

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _clear(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _select_dropdown_by_visible_text(self, locator: tuple, text: str, time: int = 10):
        """
        Selects an option from a dropdown by its visible text.

        :param locator: A tuple representing the locator strategy and the locator value for the dropdown.
        :param text: The visible text of the option to be selected.
        :param time: Optional; The maximum amount of time to wait for the dropdown to be visible.
        """
        self._wait_until_element_is_visible(locator, time)
        try:
            dropdown = Select(self._find(locator))
            dropdown.select_by_visible_text(text)
        except NoSuchElementException:
            print(f"Dropdown element not found with locator: {locator}")

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _scroll_to_element(self, locator: tuple):
        """
        Scrolls the web page until the specified element is in the visible area of the browser window.

        :param locator: A tuple representing the locator strategy and the locator value.
        """
        element = self._find(locator)
        desired_y = (element.location['y'] - self._driver.execute_script('return window.innerHeight / 2;'))
        current_y = self._driver.execute_script('return window.pageYOffset;')
        self._driver.execute_script(f"window.scrollTo(0, {current_y + desired_y});")

    def _wait_for_page_load_complete(self, timeout=30):
        WebDriverWait(self._driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
