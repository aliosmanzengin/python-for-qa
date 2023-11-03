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
def test_login(setup_teardown):
    driver = setup_teardown

    driver.get("https://blog.griddynamics.com")
