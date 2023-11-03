import pytest
from pages.gd_blog_page import MainPage
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome("/drivers/chromedriver")
    yield driver
    driver.quit()


# @pytest.mark.parametrize("username,password", [("my_username", "my_password")])
@pytest.mark.usefixtures("setup_teardown")
def test_case_one(setup_teardown):
    driver = setup_teardown
    main_page = MainPage(driver)
    main_page.navigate_to_page("https://blog.griddynamics.com")
    main_page.hover_over_element()
    main_page.click_on_visible_element()
