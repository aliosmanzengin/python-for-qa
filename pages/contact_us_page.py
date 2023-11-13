from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ContatcUsPage(BasePage):
    _url = "https://www.griddynamics.com/contact"
    __submit_button = (By.XPATH, "//button[contains(@class,'submit-button')]")
    __firstname_locator = (By.XPATH, "//input[@formcontrolname='firstName']")
    __lastname_locator = (By.XPATH, "//input[@formcontrolname='lastName']")
    __email_locator = (By.XPATH, "//input[@formcontrolname='email']")
    __terms_and_conditions_checkbox = (By.XPATH, "//gd-checkbox[@formcontrolname='policy']")
    __contact_consent_checkbox = (By.XPATH, "//gd-checkbox[@formcontrolname='allowContact']")
    __where_did_you_hear_us_dropdown = (By.XPATH, "//gd-select[@formcontrolname='source']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    def _select_how_did_you_hear_us(self, item_name: str):
        super()._scroll_to_element(self.__where_did_you_hear_us_dropdown)
        self._select_dropdown_by_visible_text(self.__where_did_you_hear_us_dropdown, item_name)

    def fill_form_missing(self):
        super()._write_input(self.__firstname_locator, "Alan")
        super()._write_input(self.__lastname_locator, "Wake")
        super()._write_input(self.__email_locator, "alanwake@author.gm")
        super()._click(self.__contact_consent_checkbox)
        super()._click(self.__terms_and_conditions_checkbox)
        self._select_how_did_you_hear_us("Online Ads")

    def is_submit_button_disabled(self) -> bool:
        return super()._find(self.__submit_button).get_attribute('disabled') == 'true'
