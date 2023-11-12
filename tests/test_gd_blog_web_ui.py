"""
test_gd_blog_web_ui.py
"""
import pytest
from pages.gd_blog_page import MainPage
from pages.leadership import LeadershipPage


class TestBlogPage:

    # @pytest.mark.parametrize("username,password", [("my_username", "my_password")])
    @pytest.mark.blogpage
    @pytest.mark.ui_tests
    def test_case_one(self, custom_driver):
        expected_text = ("director of Grid Dynamics’ board of directors since 2006 and the Chief Executive Officer of "
                         "Grid Dynamics since 2014")
        blog_page = MainPage(custom_driver)
        blog_page.open()  # Ensure this line is present to navigate to the page
        blog_page.go_to_leadership()
        leadership_page = LeadershipPage(custom_driver)
        leadership_page.click_llivschitz_profile()
        assert leadership_page.expected_url == leadership_page.current_url
        assert leadership_page.is_profile_info_displayed(), "Profile info is not displayed"
        assert expected_text in leadership_page.profile_description

"""
Case #2:
1- Open https://blog.griddynamics.com(opens in a new tab)
2- Click ‘filter’ (check it’s visible and available)
3- Filter by Cloud and DevOps topic
4- Check there is more than 1 article
5- Reset all filters
6- Check the first article in the list is different than in step 4 and check there is more than 1 article.
"""
