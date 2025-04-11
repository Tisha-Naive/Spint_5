from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://stellarburgers.nomoreparties.site/register"  # проверь актуальность

    def open(self):
        self.driver.get(self.url)

    def register(self, username, email, password):
        wait = WebDriverWait(self.driver, 10)

        # Имя
        name_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input")))
        name_input.send_keys(username)

        # Email (хотя он в поле name="name")
        email_input = self.driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        email_input.send_keys(email)

        # Пароль
        password_input = self.driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_input.send_keys(password)

        # Кнопка регистрации
        register_btn = self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
        register_btn.click()

    def get_error_text(self):
        wait = WebDriverWait(self.driver, 5)
        error_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "input__error")))
        return error_element.text

    def click_login_button_from_registration(self):
        login_button = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        login_button.click()