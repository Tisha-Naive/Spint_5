from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.password_recovery_page import PasswordRecoveryPage


def test_login_from_main_page(driver):
    page = MainPage(driver)
    page.open()
    page.click_login_button()
    login_page = LoginPage(driver)
    login_page.login("test123@yandex.ru", "qwerty123")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
    )
    assert driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").is_displayed()

def test_login_from_personal_account_button(driver):
    page = MainPage(driver)  # Главная страница
    page.open()
    page.click_personal_account_button()  # Кнопка "Личный кабинет"
    login_page = LoginPage(driver)  # Страница входа
    login_page.login("test123@yandex.ru", "qwerty123")  # Логин и пароль
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
    )
    assert driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").is_displayed()

def test_login_from_registration_form(driver):
    page = RegistrationPage(driver)  # Страница регистрации
    page.open()
    page.click_login_button_from_registration()  # Кнопка "Войти" в форме регистрации
    login_page = LoginPage(driver)  # Страница входа
    login_page.login("test123@yandex.ru", "qwerty123")  # Логин и пароль
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
    )
    assert driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").is_displayed()

def test_login_from_password_recovery_form(driver):
    page = PasswordRecoveryPage(driver)  # Страница восстановления пароля
    page.open()
    page.click_login_button_from_recovery()  # Кнопка "Войти" в форме восстановления пароля
    login_page = LoginPage(driver)  # Страница входа
    login_page.login("test123@yandex.ru", "qwerty123")  # Логин и пароль
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
    )
    assert driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").is_displayed()

