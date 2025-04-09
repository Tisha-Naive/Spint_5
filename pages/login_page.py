from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        )
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        )
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def submit_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, email, password):
        """Упрощённый вход в аккаунт"""
        self.enter_email(email)
        self.enter_password(password)
        self.submit_login()
