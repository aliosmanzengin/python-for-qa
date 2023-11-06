"""
Case #1:

Open https://blog.griddynamics.com(opens in a new tab)
Go to “Leadership” under About page
Find Leonard Livschitz and click on the name
Verify that information about Leonard has appeared. The text “director of Grid Dynamics’ board of directors since 2006 and the Chief Executive Officer of Grid Dynamics since 2014” is visible.

Case #2:

Open https://blog.griddynamics.com(opens in a new tab)
Click ‘filter’ (check it’s visible and available)
Filter by Cloud and DevOps topic
Check there is more than 1 article
Reset all filters
Check the first article in the list is different than in step 4 and check there is more than 1 article.

Case #3:

Open https://blog.griddynamics.com(opens in a new tab)
Click on Get In Touch button
Ensure page Contact Us opened
Fill in the following:
First Name = Anna, Last Name = Smith
email = annasmith@griddynamics.com
select  How did you hear about us? = Online Ads
Click on checkbox “I have read and accepted the Terms & Conditions and Privacy Policy”
Click on checkbox “I allow Grid Dynamics to contact me”
Ensure Contact button is inactive
"""
from selenium.webdriver import ActionChains
from utils.utils import SeleniumUtils


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    # Elements
    def hover_element_xpath(self):
        return "//*[@class ='section-button link'] [contains(text(), 'About')]"

    def click_element_xpath(self):
        return "//*[@class ='submenu-label-item'] [contains(text(), 'Leadership')]"

    # Actions
    def navigate_to_page(self, url):
        self.driver.get(url)

    def hover_over_element(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(SeleniumUtils.wait_for_element_to_be_visible(self.driver, self.hover_element_xpath())).perform()

    def click_on_visible_element(self):
        SeleniumUtils.click_element_with_wait(self.driver, self.click_element_xpath())
