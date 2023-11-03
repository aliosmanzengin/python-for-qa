from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SeleniumUtils:
    @staticmethod
    def wait_for_element_to_be_visible(driver, xpath, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    @staticmethod
    def click_element(driver, element):
        element.click()

    @staticmethod
    def click_element_with_wait(driver, xpath, timeout=10):
        element = SeleniumUtils.wait_for_element_to_be_visible(driver, xpath, timeout)
        SeleniumUtils.click_element(driver, element)

    @staticmethod
    def scroll_into_view(driver, element):
        driver.execute_script("arguments[0].scrollIntoView();", element)
