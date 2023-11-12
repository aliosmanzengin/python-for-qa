"""
gd_blog_page.py
"""
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec, wait

from utils.utils import SeleniumUtils
from pages.base_page import BasePage


class MainPage(BasePage):
    __url = "https://blog.griddynamics.com"
    __about_section_locator = (By.XPATH, "//*[@class='section-button link'][contains(text(), 'About')]")
    __leadership_locator = (By.XPATH, "//*[@class ='submenu-label-item'] [contains(text(), 'Leadership')]")
    __filter_topics_dropdown = (By.ID, "topiclist")
    __cloud_and_devops_topic_locator = ()
    __all_topics_locator = ()
    __cloud_and_devops_articles_list = ()
    __cloud_and_devops_first_article_locator = ()
    __media_and_news_locator = ()

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def devops_articles_list(self) -> list:
        return super()._get_text(self.__cloud_and_devops_articles_list)

    def open(self):
        super()._open_url(self.__url)
        self._wait_for_page_load_complete()

    def _select_topic(self, topic_name: str):
        self._select_dropdown_by_visible_text(self.__filter_topics_dropdown, topic_name)

    def go_to_leadership(self):
        super()._hover(self.__about_section_locator)
        super()._click(self.__leadership_locator)

    def filter_devops_topic(self):
        self._select_topic("Cloud and DevOps")

