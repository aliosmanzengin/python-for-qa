import pytest
from pages.gd_blog_page import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture
# def driver():
#     my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield my_driver
#     my_driver.quit()


class TestBlogPage:

    # @pytest.mark.parametrize("username,password", [("my_username", "my_password")])
    @pytest.mark.blogpage
    @pytest.mark.ui_tests
    def test_case_one(self, custom_driver):
        main_page = MainPage(custom_driver)
        main_page.navigate_to_page("https://blog.griddynamics.com")
        main_page.hover_over_element()
        main_page.click_on_visible_element()

    @pytest.mark.blogpage
    @pytest.mark.ui_tests
    def test_case_two(self, custom_driver):
        main_page = MainPage(custom_driver)
        main_page.navigate_to_page("https://blog.griddynamics.com")
        main_page.hover_over_element()
        main_page.click_on_visible_element()

    @pytest.mark.blogpage
    @pytest.mark.ui_tests
    def test_case_three(self, custom_driver):
        main_page = MainPage(custom_driver)
        main_page.navigate_to_page("https://blog.griddynamics.com")
        main_page.hover_over_element()
        main_page.click_on_visible_element()

    @pytest.mark.blogpage
    @pytest.mark.ui_tests
    def test_case_four(self, custom_driver):
        main_page = MainPage(custom_driver)
        main_page.navigate_to_page("https://blog.griddynamics.com")
        main_page.hover_over_element()
        main_page.click_on_visible_element()
