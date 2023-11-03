# webdriver_manager.py
from selenium import webdriver


class WebDriverManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebDriverManager, cls).__new__(cls)
            # Initialize a WebDriver instance here
            cls._instance.driver = webdriver.Firefox(executable_path='/path/to/geckodriver')
        return cls._instance

    @staticmethod
    def get_driver():
        return WebDriverManager()._instance.driver
