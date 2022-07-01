from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators


class BasePageLocators(BaseLocators):
    HOTEL_LOGO_URL = (By.CLASS_NAME, 'hotel-logoUrl')

