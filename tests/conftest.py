"""
conftest.py
"""

import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Configure logging at the top of the file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@pytest.fixture
def custom_driver(request):
    browser = request.config.getoption("--browser")
    logger.info(f"Starting {browser} Driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        logger.info(f"initialising the browser {browser}")
        my_driver.maximize_window()
        logger.info(f"maximising the window")
        # my_driver = webdriver.Chrome()
    elif browser == "firefox":
        # my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        my_driver = webdriver.Firefox()
        logger.info(f"initialising the browser {browser}")
        my_driver.maximize_window()
        logging.info(f"maximising the window")

    else:
        raise TypeError(f"Invalid browser type: '{browser}'.\nPlease enter chrome or firefox to choose a browser.")
        # my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    yield my_driver
    logger.info(f"Quitting {browser} Driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser option to execute ui tests. Choose chrome or firefox."
    )