import sys
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators


class ShadyMeadowsPageObject:
    def __init__(self, web_driver):
        self.__web_driver = web_driver
        self.__wait = WebDriverWait(self.__web_driver, 15)
        self.__action = ActionChains(self.__web_driver)

    @property
    def web_driver(self):
        return self.__web_driver

    @property
    def action(self):
        return self.__action

    @property
    def wait(self):
        return self.__wait

    @property
    def command_key(self):
        if sys.platform == 'darwin':
            return Keys.COMMAND
        else:
            return Keys.CONTROL

    def open(self):
        self.__web_driver.get("https://automationintesting.online/")
        return self

    def get_picture_element(self):
        return self.__wait.until(EC.presence_of_element_located(
            (BasePageLocators.HOTEL_LOGO_URL.by,
             BasePageLocators.HOTEL_LOGO_URL.locator)))

    # def get_element_by_class_name(self, locator):
    #     return self.__wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))





