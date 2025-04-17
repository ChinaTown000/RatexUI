from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@fixture(scope='function')
def webdriver_fixture():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()