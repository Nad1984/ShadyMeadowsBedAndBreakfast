import sys
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from allure import step, attach, attachment_type


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
        url = "https://automationintesting.online/"
        with step(f"Navigating to the environmental URL:{url}"):
            self.web_driver.get(url)
            attach(self.__web_driver.get_screenshot_as_png(), name="Navigating to the environmental URL",
                   attachment_type=attachment_type.PNG)
            return self

    @step(f"Click on 'Let me hack' button")
    def click_on_let_me_hack_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable((BasePageLocators.LET_ME_HACK_BUTTON.by,
                                        BasePageLocators.LET_ME_HACK_BUTTON.locator)))
        self.__action.move_to_element(button).click().perform()
        return self

    @step("Find logo picture.")
    def get_logo_picture_element(self):
        attach(self.__web_driver.get_screenshot_as_png(), name="Logo picture.",
               attachment_type=attachment_type.PNG)
        return self.__wait.until(EC.presence_of_element_located(
            (BasePageLocators.HOTEL_LOGO_URL.by,
             BasePageLocators.HOTEL_LOGO_URL.locator)))

    @step("Book_this_room_button is present on the page.")
    def book_this_room_button_is_present(self):
        elements = self.wait.until(EC.presence_of_all_elements_located((BasePageLocators.BOOK_THIS_ROOM_BUTTON.by,
                                                                        BasePageLocators.BOOK_THIS_ROOM_BUTTON.locator)))
        element = elements[0]
        return element

    @step("Move to rooms_block.")
    def move_to_rooms_block(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.ORDER_ROOM_TAB.by,
                                                                          BasePageLocators.ORDER_ROOM_TAB.locator)))
        element = elements[1]
        self.__action.move_to_element(element).perform()
        attach(self.__web_driver.get_screenshot_as_png(), name="Rooms block.",
               attachment_type=attachment_type.PNG)
        return self

    @step("Find whole rooms_block calendar.")
    def get_rooms_block_calendar(self):
        self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CALENDAR.by,
                                                               BasePageLocators.CALENDAR.locator)))
        attach(self.__web_driver.get_screenshot_as_png(), name="Rooms_block_calendar",
               attachment_type=attachment_type.PNG)
        return self

    @step("Find rooms_block First name field.")
    def get_rooms_block_first_name_field(self):
        self.wait.until(EC.visibility_of_element_located((BasePageLocators.FIRST_NAME.by,
                                                          BasePageLocators.FIRST_NAME.locator)))
        attach(self.__web_driver.get_screenshot_as_png(), name="Rooms_block First name field.",
               attachment_type=attachment_type.PNG)
        return self

    @step("Find rooms_block Last name field.")
    def get_rooms_block_last_name_field(self):
        self.wait.until(EC.visibility_of_element_located((BasePageLocators.LAST_NAME.by,
                                                          BasePageLocators.LAST_NAME.locator)))
        attach(self.__web_driver.get_screenshot_as_png(), name="Rooms_block Last name field.",
               attachment_type=attachment_type.PNG)
        return self

    @step("Find rooms_block Email field.")
    def get_rooms_block_email_field(self):
        self.wait.until(EC.visibility_of_element_located((BasePageLocators.EMAIL.by,
                                                          BasePageLocators.EMAIL.locator)))
        attach(self.__web_driver.get_screenshot_as_png(), name="Rooms_block Email field.",
               attachment_type=attachment_type.PNG)
        return self

    @step("Find rooms_block Phone field.")
    def get_rooms_block_phone_field(self):
        self.wait.until(EC.visibility_of_element_located((BasePageLocators.PHONE.by,
                                                          BasePageLocators.PHONE.locator)))
        attach(self.__web_driver.get_screenshot_as_png(), name="Rooms_block Phone field.",
               attachment_type=attachment_type.PNG)
        return self

    @step("Find rooms_block 'Cancel' button.")
    def get_rooms_block_cancel_order_room_button(self):
        cancel_order_room_button = self.wait.until(
            EC.visibility_of_all_elements_located((BasePageLocators.CANCEL_BUTTON.by,
                                                   BasePageLocators.CANCEL_BUTTON.locator)))
        element = cancel_order_room_button[0]
        attach(self.__web_driver.get_screenshot_as_png(), name="Rooms_block 'Cancel' button.",
               attachment_type=attachment_type.PNG)
        return element

    @step("Find rooms_block 'Book' button.")
    def get_rooms_block_book_button(self):
        self.wait.until(EC.visibility_of_element_located((BasePageLocators.BOOK_BUTTON.by,
                                                          BasePageLocators.BOOK_BUTTON.locator)))
        attach(self.__web_driver.get_screenshot_as_png(), name="Rooms_block 'Book' button.",
               attachment_type=attachment_type.PNG)
        return self

    @step("Find 'Name' field in contact block.")
    def get_contact_block_name_field(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.by,
                                                   BasePageLocators.CONTACT_BLOCK_PERSONS_NAME.locator)))
        element = elements[0]
        attach(self.__web_driver.get_screenshot_as_png(), name="'Name' field in contact block.",
               attachment_type=attachment_type.PNG)
        return element

    @step("Find 'Email' field in contact block.")
    def get_contact_block_email_field(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_EMAIL.by,
                                                                          BasePageLocators.CONTACT_BLOCK_EMAIL.locator)))
        element = elements[0]
        attach(self.__web_driver.get_screenshot_as_png(), name="'Email' field in contact block.",
               attachment_type=attachment_type.PNG)
        return element

    @step("Find contact_block 'Phone' field.")
    def get_contact_block_phone_field(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_PHONE.by,
                                                                          BasePageLocators.CONTACT_BLOCK_PHONE.locator)))
        element = elements[0]
        attach(self.__web_driver.get_screenshot_as_png(), name="'Phone' field in contact block.",
               attachment_type=attachment_type.PNG)
        return element

    @step("Find contact_block 'Subject' field.")
    def get_contact_block_subject_field(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_SUBJECT.by,
                                                                          BasePageLocators.CONTACT_BLOCK_SUBJECT.locator)))
        element = elements[0]
        attach(self.__web_driver.get_screenshot_as_png(), name="'Subject' field in contact block.",
               attachment_type=attachment_type.PNG)
        return element

    @step("Find contact_block 'Message' field.")
    def get_contact_block_message_field(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_MESSAGE.by,
                                                   BasePageLocators.CONTACT_BLOCK_MESSAGE.locator)))
        element = elements[0]
        attach(self.__web_driver.get_screenshot_as_png(), name="'Message' field in contact block.",
               attachment_type=attachment_type.PNG)
        return element

    @step("Find contact_block 'Submit_button'.")
    def get_contact_block_submit_button(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located((BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.by,
                                                   BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.locator)))
        element = elements[0]
        attach(self.__web_driver.get_screenshot_as_png(), name="'Submit_button' in contact block.",
               attachment_type=attachment_type.PNG)
        return element

    @step("Check that contact_block 'Submit_button' is clickable.")
    def get_to_contact_block_submit_button(self):
        submit_button = self.wait.until(
            EC.element_to_be_clickable((BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.by,
                                        BasePageLocators.CONTACT_BLOCK_SUBMIT_BUTTON.locator)))
        self.__action.move_to_element(submit_button).perform()
        attach(self.__web_driver.get_screenshot_as_png(), name="Contact_block 'Submit_button' is clickable.",
               attachment_type=attachment_type.PNG)
        return self

    @step(f"Scroll to 'Submit' button on contact block and click on it.")
    def contact_block_submit_button_is_clickable_second(self):
        submit_button = self.get_contact_block_submit_button()
        self.__action.move_to_element(submit_button).perform()
        self.get_contact_block_submit_button().click()
        attach(self.__web_driver.get_screenshot_as_png(), name="Click on 'Submit' button",
               attachment_type=attachment_type.PNG)
        return self

    @step("Scroll to Book_this_room button in rooms block.")
    def move_to_book_this_room_button(self):
        book_this_room_button = self.book_this_room_button_is_present()
        self.__action.move_to_element(book_this_room_button).perform()
        attach(self.__web_driver.get_screenshot_as_png(), name="Book_this_room button",
               attachment_type=attachment_type.PNG)
        return self

    @step("Click on Book_this_room button.")
    def click_book_this_room_button(self):
        self.book_this_room_button_is_present().click()
        attach(self.__web_driver.get_screenshot_as_png(), name="Click on 'Book_this_room' button",
               attachment_type=attachment_type.PNG)
        return self

    @step("Scroll to 'Cancel' button in rooms block and click on it.")
    def click_cancel_button(self):
        cancel_button = self.get_rooms_block_cancel_order_room_button()
        self.__action.move_to_element(cancel_button).perform()
        self.get_rooms_block_cancel_order_room_button().click()
        attach(self.__web_driver.get_screenshot_as_png(), name="Click on 'Cancel button' button",
               attachment_type=attachment_type.PNG)
        return self
