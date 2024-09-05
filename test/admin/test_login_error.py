import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class TestLoginError:

    def test_error_login(self, driver):
        driver.get("https://inscription.it-akademy.fr/")
        
        #
        pass


# #debug 
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-search-engine-choice-screen")
# # options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--remote-debugging-port=9222")
# driver = webdriver.Chrome(options=options)
# test = TestLoginError()
# test.test_error_login(driver)