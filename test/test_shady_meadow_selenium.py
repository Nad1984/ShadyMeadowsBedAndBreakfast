import pytest
from test_data.test_data_ui import test1
from locators.base_page_locators import BasePageLocators
from page_object.main_page import ShadyMeadowsPageObject


class TestShadyMeadows:
    @pytest.mark.shady_meadow_ui
    @pytest.mark.parametrize("expected_location_x, expected_location_y", test1)
    def test_logo_picture_is_visible_and_in_correct_position(self, shady_meadow_page: ShadyMeadowsPageObject,
                                                             expected_location_x,
                                                             expected_location_y):
        logo_picture = shady_meadow_page.get_picture_element()
        if logo_picture.is_displayed():
            print("Element found")
        else:
            print("Element not found")

        print(logo_picture.location)
        assert logo_picture.is_displayed(), f"Logo picture is not displayed"
        assert logo_picture.location['x'] == int(expected_location_x) and \
               logo_picture.location['y'] == int(expected_location_y), \
            f"Location of the picture is not matching with expected x = {expected_location_x}, " \
            f"y = {expected_location_y}"

