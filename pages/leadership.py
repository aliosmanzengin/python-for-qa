from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LeadershipPage(BasePage):
    _url = "https://www.griddynamics.com/leadership"
    __llivschitz_profile_locator = (By.XPATH, "//div[@class='gd-typography-lead name-label'][contains(text(), 'Leonard Livschitz')]")
    __llivschitz_info_locator = (By.XPATH, "//gd-wysiwyg-content//*[contains(text(), 'Chief Executive Officer of Grid Dynamics')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def profile_description(self) -> str:
        return super()._get_text(self.__llivschitz_info_locator)

    def click_llivschitz_profile(self):
        # super()._find(self.__llivschitz_profile_locator)
        super()._scroll_to_element(self.__llivschitz_profile_locator)
        super()._wait_until_element_is_clickable(self.__llivschitz_profile_locator)
        super()._click(self.__llivschitz_profile_locator)

    def is_profile_info_displayed(self) -> bool:
        return super()._is_displayed(self.__llivschitz_info_locator)
