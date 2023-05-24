import time

import pytest as pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(autouse=True)
def setup(request,browser): #this makes the value present as paramater to be used by the calling class. in this case we are instantiating driver
     if browser=="chrome":
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
        driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
     elif browser=="firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
     #wait = WebDriverWait(driver, 20)
     driver.get("https://www.goibibo.com/")
     driver.maximize_window()
     time.sleep(4)
     request.cls.driver=driver
     #request.cls.wait = wait
     yield
     driver.close()

def pytest_addoption(parser):
          parser.addoption("--browser")

     # @pytest.fixture(scope="class",autouse=True)
     # def browser(request):
     #      return request.config.getoption("--browser")

@pytest.fixture(scope="session",autouse=True)
def browser(request):
          return request.config.getoption("--browser")

