import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    def test_successful_login(self, driver):
        # Accéder à la page d'administration du site
        driver.get("https://inscription.it-akademy.fr/")

        email_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        # Se connecter
        email_input.send_keys("nouvene.antoine@gmail.com")
        password_input.send_keys("hocMotminh82&")
        driver.execute_script("arguments[0].scrollIntoView();", login_button)
        login_button.click()

        # WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
        #
        # assert "Dashboard" in driver.title