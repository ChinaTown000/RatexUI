from pytest import fixture
from selenium import webdriver

@fixture(scope='function')
def webdriver_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()