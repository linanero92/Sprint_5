import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    service = Service(executable_path='/Users/alinakuptsova/WebDriver/bin/chromedriver')
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()