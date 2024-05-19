import os.path
from _pytest.fixtures import fixture
from selenium import webdriver
from page_object.main_page import ShadyMeadowsPageObject


@fixture
def shady_meadow_page(custom_logger):
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield ShadyMeadowsPageObject(driver, custom_logger).open()

    driver.quit()




    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service
    #
    # service = Service()
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=service, options=options)
    #
    # driver.quit()
