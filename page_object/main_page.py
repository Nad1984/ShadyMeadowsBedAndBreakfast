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
        self.web_driver.get("https://automationintesting.online/")
        return self

    def get_logo_picture_element(self):
        return self.__wait.until(EC.presence_of_element_located(
            (BasePageLocators.HOTEL_LOGO_URL.by,
             BasePageLocators.HOTEL_LOGO_URL.locator)))

    def book_this_room_button_is_present(self):
        elements = self.wait.until(EC.presence_of_all_elements_located((BasePageLocators.BOOK_THIS_ROOM_BUTTON.by,
                                                                        BasePageLocators.BOOK_THIS_ROOM_BUTTON.locator)))
        element = elements[0]
        return element

    # def book_this_room_button_is_clickable(self):
    #     elements = self.wait.until(EC.element_to_be_clickable((BasePageLocators.BOOK_THIS_ROOM_BUTTON.by,
    #                                                            BasePageLocators.BOOK_THIS_ROOM_BUTTON.locator)))
    #     element = elements[0]
    #     self.action.move_to_element(element).perform()
    #     return element
    #
    def get_rooms_block(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.ORDER_ROOM_TAB.by,
                                                                          BasePageLocators.ORDER_ROOM_TAB.locator)))
        element = elements[1]
        return element

    def get_rooms_block_calendar(self):
        self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CALENDAR.by,
                                                               BasePageLocators.CALENDAR.locator)))
        return self

    def get_rooms_block_first_name_field(self):
        self.wait.until(EC.visibility_of_element_located((BasePageLocators.FIRST_NAME.by,
                                                          BasePageLocators.FIRST_NAME.locator)))
        return self

    def get_rooms_block_last_name_field(self):
        self.wait.until(EC.visibility_of_element_located((BasePageLocators.LAST_NAME.by,
                                                          BasePageLocators.LAST_NAME.locator)))
        return self

    def get_rooms_block_email_field(self):
        self.wait.until(EC.visibility_of_element_located((BasePageLocators.EMAIL.by,
                                                          BasePageLocators.EMAIL.locator)))
        return self

    def get_rooms_block_phone_field(self):
        self.wait.until(EC.visibility_of_element_located((BasePageLocators.PHONE.by,
                                                          BasePageLocators.PHONE.locator)))
        return self

    def get_rooms_block_cancel_order_room_button(self):
        cancel_order_room_button = self.wait.until(
            EC.visibility_of_all_elements_located((BasePageLocators.CANCEL_BUTTON.by,
                                                   BasePageLocators.CANCEL_BUTTON.locator)))
        element = cancel_order_room_button[0]
        return element

    def get_rooms_block_book_button(self):
        self.wait.until(EC.visibility_of_element_located((BasePageLocators.BOOK_BUTTON.by,
                                                          BasePageLocators.BOOK_BUTTON.locator)))
        return self

    def get_contact_block_name_field(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.by,
                                                   BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.locator)))
        element = elements[0]
        return element

    # def get_contact_block_name_field_placeholder_value(self):
    #     elements = self.wait.until(EC.visibility_of_element_located((BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.by,
    #                                                                 BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.locator)))
    #     element = elements[0]
    #     return element.get_attribute('placeholder')

    def get_contact_block_email_field(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_EMAIL.by,
                                                                          BasePageLocators.CONTACT_BLOCK_EMAIL.locator)))
        element = elements[0]
        return element

    def get_contact_block_phone_field(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_PHONE.by,
                                                                          BasePageLocators.CONTACT_BLOCK_PHONE.locator)))
        element = elements[0]
        return element

    def get_contact_block_subject_field(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_SUBJECT.by,
                                                                          BasePageLocators.CONTACT_BLOCK_SUBJECT.locator)))
        element = elements[0]
        return element

    def get_contact_block_message_field(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_MESSAGE.by,
                                                   BasePageLocators.CONTACT_BLOCK_MESSAGE.locator)))
        element = elements[0]
        return element

    def get_contact_block_submit_button(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.by,
                                                   BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.locator)))
        element = elements[0]
        return element

    def contact_block_submit_button_is_clickable(self):
        self.wait.until(
            EC.element_to_be_clickable((BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.by,
                                        BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.locator)))
        return self

    def contact_block_submit_button_is_clickable_second(self):
        submit_button = self.get_contact_block_submit_button()
        self.__action.move_to_element(submit_button).perform()
        self.get_contact_block_submit_button().click()
        return self

    def click_book_this_room_button(self):
        book_this_room_button = self.book_this_room_button_is_present()
        self.__action.move_to_element(book_this_room_button).perform()
        self.book_this_room_button_is_present().click()
        return self

    def click_cancel_button(self):
        cancel_button = self.get_rooms_block_cancel_order_room_button()
        self.__action.move_to_element(cancel_button).perform()
        self.get_rooms_block_cancel_order_room_button().click()
        return self
