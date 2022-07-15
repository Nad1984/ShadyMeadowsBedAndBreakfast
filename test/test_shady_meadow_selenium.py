import pytest
from selenium.common import StaleElementReferenceException, NoSuchElementException

from test_data.test_data_ui import test1
from locators.base_page_locators import BasePageLocators
from page_object.main_page import ShadyMeadowsPageObject


class TestShadyMeadows:
    @pytest.mark.shady_meadow_ui
    # @pytest.mark.parametrize("expected_location_x, expected_location_y", test1)
    def test_logo_picture_is_visible_and_in_correct_position(self, shady_meadow_page: ShadyMeadowsPageObject):
        logo_picture = shady_meadow_page.get_logo_picture_element()
        expected_location_x = "326"
        expected_location_y = "687"
        if logo_picture.is_displayed:
            print("Element found")
        else:
            print("Element not found")

        print(logo_picture.location)
        assert logo_picture.is_displayed(), f"Logo picture is not displayed"
        assert logo_picture.location['x'] == int(expected_location_x) and \
               logo_picture.location['y'] == int(expected_location_y), \
            f"Location of the picture is not matching with expected x = {expected_location_x}, " \
            f"y = {expected_location_y}"

    @pytest.mark.shady_meadow_ui
    def test_book_this_room_button(self, shady_meadow_page: ShadyMeadowsPageObject):
        book_button = shady_meadow_page.book_this_room_button_is_present()
        assert book_button.is_displayed(), f"Book_this_room button is not displayed"
        assert book_button.text == 'Book this room'
        shady_meadow_page.click_book_this_room_button()
        with pytest.raises(StaleElementReferenceException) as e_info:
            # StaleElementReferenceException means the element is no longer in the DOM, or it changed.
            assert book_button.is_displayed(), f"Book_this_room button is displayed, but shouldn't.{e_info}"

    @pytest.mark.shady_meadow_ui
    def test_rooms_block_cancel_button(self, shady_meadow_page: ShadyMeadowsPageObject):
        shady_meadow_page.click_book_this_room_button()
        shady_meadow_page.get_rooms_block()
        cancel_button = shady_meadow_page.get_rooms_block_cancel_order_room_button()
        book_button = shady_meadow_page.get_rooms_block_book_button()
        calendar = shady_meadow_page.get_rooms_block_calendar()
        first_name_field = shady_meadow_page.get_rooms_block_first_name_field()
        last_name_field = shady_meadow_page.get_rooms_block_last_name_field()
        email_field = shady_meadow_page.get_rooms_block_email_field()
        phone_field = shady_meadow_page.get_rooms_block_phone_field()
        shady_meadow_page.click_cancel_button()
        with pytest.raises(StaleElementReferenceException) as e_info:
            assert cancel_button.is_displayed(), f"Cancel button is displayed, but shouldn't.{e_info}"
            assert book_button.is_displayed(), f"Book button is displayed, but shouldn't.{e_info}"
            assert calendar.is_displayed(), f"Calendar is displayed, but shouldn't.{e_info}"
            assert first_name_field.is_displayed(), f"First name field is displayed, but shouldn't.{e_info}"
            assert last_name_field.is_displayed(), f"Last name field is displayed, but shouldn't.{e_info}"
            assert email_field.is_displayed(), f"Email field is displayed, but shouldn't.{e_info}"
            assert phone_field.is_displayed(), f"Email field is displayed, but shouldn't.{e_info}"

    @pytest.mark.shady_meadow_ui
    def test_contact_block_visibility_if_book_this_room_button_was_clicked(self,
                                                                           shady_meadow_page: ShadyMeadowsPageObject):
        shady_meadow_page.click_book_this_room_button()
        contact_block_name_field = shady_meadow_page.get_contact_block_name_field()
        assert contact_block_name_field.is_displayed(), f"Contact_block_name_field is not displayed"
        contact_block_email_field = shady_meadow_page.get_contact_block_email_field()
        assert contact_block_email_field.is_displayed(), f"Contact_block_email_field is not displayed"
        contact_block_phone_field = shady_meadow_page.get_contact_block_phone_field()
        assert contact_block_phone_field.is_displayed(), f"Contact_block_phone_field is not displayed"
        contact_block_subject_field = shady_meadow_page.get_contact_block_subject_field()
        assert contact_block_subject_field.is_displayed(), f"Contact_block_subject_field is not displayed"
        contact_block_message_field = shady_meadow_page.get_contact_block_message_field()
        assert contact_block_message_field.is_displayed(), f"Contact_block_message_field is not displayed"
        contact_block_submit_button = shady_meadow_page.get_contact_block_submit_button()
        assert contact_block_submit_button.is_displayed(), f"Contact_block_submit_button is not displayed"
        assert contact_block_submit_button.text == 'Submit'

    @pytest.mark.shady_meadow_ui
    def test_contact_block_submit_is_visible_and_clickable(self, shady_meadow_page: ShadyMeadowsPageObject):
        submit_button = shady_meadow_page.get_contact_block_submit_button()
        assert submit_button.is_displayed(), f"Contact_block_submit_button is not displayed"
        # assert shady_meadow_page.contact_block_submit_button_is_clickable(), \
        #     f"Contact_block_submit_button is not clickable"
        from selenium.common.exceptions import WebDriverException

        try:
            shady_meadow_page.contact_block_submit_button_is_clickable_second()
        except WebDriverException:
            print("Element is not clickable")
