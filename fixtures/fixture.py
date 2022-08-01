from _pytest.fixtures import fixture
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

from page_object.main_page import ShadyMeadowsPageObject


@fixture
def shady_meadow_page(custom_logger):
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.maximize_window()
    yield ShadyMeadowsPageObject(browser, custom_logger).open()

    browser.quit()


