from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class PasswordRecoveryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Локаторы
    EMAIL_INPUT = (By.NAME, "name")  # поле email (да, может быть name="name")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # кнопка восстановления
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # ссылка «Войти» под формой

    def restore_password(self, email):
        """Метод для восстановления пароля, передавая email"""
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.RESTORE_BUTTON).click()

    def click_login_link(self):
        """Метод для клика по ссылке 'Войти'"""
        self.driver.find_element(*self.LOGIN_LINK).click()

    def click_login_button_from_recovery(self):
        """Метод для перехода на страницу входа через ссылку в форме восстановления пароля"""
        self.driver.find_element(*self.LOGIN_LINK).click()

    URL = "https://stellarburgers.nomoreparties.site/forgot-password"  # адрес восстановления пароля

    def open(self):
        """Метод для открытия страницы восстановления пароля"""
        self.driver.get(self.URL)
