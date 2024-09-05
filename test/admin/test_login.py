import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestRadioCheck:
    # Initialiser le navigateur
    def setup_method(self, method):
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        chrome_options.add_argument("--disable-popup-blocking")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_radio_check(self):
        # Ouvrir la page de test
        self.driver.get("https://demoqa.com/radio-button")

        # Check yesRadio rario button
        self.driver.find_element(By.XPATH, "//input[@id='yesRadio']/following-sibling::label").click()
        time.sleep(1)  # Temporisation de 5 secondes

        # Check impressive rario button
        self.driver.find_element(By.XPATH, "//input[@id='impressiveRadio']/following-sibling::label").click()
        time.sleep(1)  # Temporisation de 5 secondes
