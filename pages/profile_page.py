from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def click_logout_button(self):
        logout_button = (By.XPATH, "//button[text()='Выход']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(logout_button)
        ).click()