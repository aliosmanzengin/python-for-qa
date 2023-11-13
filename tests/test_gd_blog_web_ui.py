"""
test_gd_blog_web_ui.py
"""
import pytest

from pages.contact_us_page import ContatcUsPage
from pages.gd_blog_page import MainPage
from pages.leadership import LeadershipPage


class TestBlogPage:

    # @pytest.mark.parametrize("username,password", [("my_username", "my_password")])
    @pytest.mark.blogpage
    # @pytest.mark.ui_tests
    def test_case_one(self, custom_driver):
        expected_text = ("director of Grid Dynamics’ board of directors since 2006 and the Chief Executive Officer of "
                         "Grid Dynamics since 2014")
        blog_page = MainPage(custom_driver)
        blog_page.open()
        blog_page.go_to_leadership()
        leadership_page = LeadershipPage(custom_driver)
        leadership_page.click_llivschitz_profile()
        assert leadership_page.expected_url == leadership_page.current_url
        assert leadership_page.is_profile_info_displayed(), "Profile info is not displayed"
        assert expected_text in leadership_page.profile_description

    @pytest.mark.blogpage
    # @pytest.mark.ui_tests
    def test_case_two(self, custom_driver):
        blog_page = MainPage(custom_driver)
        blog_page.open()
        initial_articles = blog_page.get_all_articles()
        blog_page.filter_devops_topic()
        devops_articles = blog_page.get_devops_articles()

        assert initial_articles
        assert devops_articles
        assert initial_articles != devops_articles
        assert initial_articles[0].get_attribute('href') != devops_articles[0].get_attribute('href')

    @pytest.mark.blogpage
    @pytest.mark.ui_tests
    def test_case_three(self, custom_driver):
        blog_page = MainPage(custom_driver)
        blog_page.open()
        blog_page.go_to_get_in_touch()
        contact_us_page = ContatcUsPage(custom_driver)
        contact_us_page.fill_form_missing()

        assert contact_us_page.expected_url == contact_us_page.current_url
        assert contact_us_page.is_submit_button_disabled()
