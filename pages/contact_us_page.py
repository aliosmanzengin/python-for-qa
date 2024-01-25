import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ContatcUsPage(BasePage):
    _url = "https://www.griddynamics.com/contact"
    __submit_button = (By.XPATH, "//input[contains(@class,'submit')]")
    __firstname_locator = (By.ID, "get-in-touch-form-first_name")
    __lastname_locator = (By.ID, "get-in-touch-form-last_name")
    __email_locator = (By.ID, "get-in-touch-form-email")
    __terms_and_conditions_checkbox = (By.XPATH, "(//*[@class = 'get-in-touch-form__field checkbox'])[1]")
    __contact_consent_checkbox = (By.XPATH, "(//*[contains(text(),'I allow Grid Dynamics to contact me.')])")
    __where_did_you_hear_us_dropdown = (By.XPATH, "(//div[@class='get-in-touch-form__dropdown--current'])[1]")
    __online_ads_select_dropdown = (By.XPATH, "//div[@key='onlineads']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        self._wait_for_page_load_complete()
        return self._url

    def fill_form_missing(self):
        super()._write_input(self.__firstname_locator, "Alan")
        logging.info("Writing firstname")
        super()._write_input(self.__lastname_locator, "Wake")
        logging.info("Writing lastname")
        super()._write_input(self.__email_locator, "alanwake@author.gm")
        logging.info("Writing email")
        super()._scroll_to_element(self.__where_did_you_hear_us_dropdown)
        super().handle_cookie_consent()
        logging.info("Clicking Dropdown")
        super()._click_with_js(self.__where_did_you_hear_us_dropdown)
        logging.info("hovering")
        super()._hover(self.__online_ads_select_dropdown)
        logging.info("Selecting online ads")
        super()._click(self.__online_ads_select_dropdown)
        super()._scroll_to_element(self.__contact_consent_checkbox)
        logging.info("Clicking contact consent checkbox")
        super()._click(self.__contact_consent_checkbox)
        logging.info("Clicking terms & conditions checkbox")
        super()._click_left_side_of_the_element(self.__terms_and_conditions_checkbox)

    def is_submit_button_disabled(self) -> bool:
        super()._scroll_to_element(self.__submit_button)
        super()._hover(self.__submit_button)
        is_disabled = super()._find(self.__submit_button).get_attribute('disabled') == 'true'
        logging.info(f"is submit button disabled {is_disabled}")
        return is_disabled
