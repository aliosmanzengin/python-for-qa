"""
gd_blog_page.py
"""
from typing import List

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec, wait

from utils.utils import SeleniumUtils
from pages.base_page import BasePage


class MainPage(BasePage):
    __url = "https://blog.griddynamics.com"
    __about_section_locator = (By.XPATH, "//*[@class='section-button link'][contains(text(), 'About')]")
    __leadership_locator = (By.XPATH, "//*[@class='submenu-label-item'][contains(text(), 'Leadership')]")
    __filter_topics_dropdown = (By.ID, "topiclist")
    __all_articles_locator = (By.XPATH, "//section//a[contains(@class,'cardtocheck')]")
    __cloud_and_devops_articles = (
    By.XPATH, "//section[contains(@class,'cloud-and-devops')]//a[contains(@class,'cardtocheck')]")
    __cloud_and_devops_locator = (By.XPATH, f"//*[@id='topiclist']//*[contains(text(), 'Cloud and DevOps')]")
    __reset_filter_locator = (By.XPATH, f"//*[@id='topiclist']//*[contains(text(), 'All topics')]")
    __get_in_touch_locator = (By.XPATH, "//*[contains(text(), 'Get in touch')][1]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)
        self._wait_for_page_load_complete()

    def go_to_leadership(self):
        super()._hover(self.__about_section_locator)
        super()._click(self.__leadership_locator)

    def go_to_get_in_touch(self):
        super()._hover(self.__get_in_touch_locator)
        super()._click(self.__get_in_touch_locator)

    def get_devops_articles(self) -> List[WebElement]:
        return self._find_elements(self.__cloud_and_devops_articles)

    def get_all_articles(self) -> List[WebElement]:
        return self._find_elements(self.__all_articles_locator)

    def filter_devops_topic(self):
        super()._scroll_to_element(self.__filter_topics_dropdown)
        super()._click(self.__filter_topics_dropdown)
        super()._click(self.__cloud_and_devops_locator)

    def reset_filters(self):
        super()._scroll_to_element(self.__filter_topics_dropdown)
        super()._click(self.__filter_topics_dropdown)
        super()._click(self.__reset_filter_locator)
