import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_successful_login(self, driver):
        # Accéder à la page d'administration du site
        driver.get("https://inscription.it-akademy.fr/")

        email_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        # Se connecter
        email_input.send_keys("email@exemple.fr")
        password_input.send_keys("password")
        driver.execute_script("arguments[0].scrollIntoView();", login_button)
        login_button.click()

        time.sleep(2)

        # Wait for the element containing "Bonjour ANTOINE" to be visible
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='Bonjour ANTOINE']"))
        )

        # Get the text from the located element
        greeting_text = element.text

        # Assert that the text is exactly "Bonjour ANTOINE"
        assert "Bonjour ANTOINE" in greeting_text
        print(greeting_text)
