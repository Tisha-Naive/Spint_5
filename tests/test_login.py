from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.password_recovery_page import PasswordRecoveryPage
from constants import DEFAULT_USER
from locators import MainPageLocators


def test_login_from_main_page(driver):
    page = MainPage(driver)
    page.open()
    page.click_login_button()
    login_page = LoginPage(driver)
    login_page.login(DEFAULT_USER["email"], DEFAULT_USER["password"])

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.PERSONAL_CABINET)
    )
    assert driver.find_element(*MainPageLocators.PERSONAL_CABINET).is_displayed()

def test_login_from_personal_account_button(driver):
    page = MainPage(driver)
    page.open()
    page.click_personal_account_button()
    login_page = LoginPage(driver)
    login_page.login(DEFAULT_USER["email"], DEFAULT_USER["password"])

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.PERSONAL_CABINET)
    )
    assert driver.find_element(*MainPageLocators.PERSONAL_CABINET).is_displayed()

def test_login_from_registration_form(driver):
    page = RegistrationPage(driver)
    page.open()
    page.click_login_button_from_registration()
    login_page = LoginPage(driver)
    login_page.login(DEFAULT_USER["email"], DEFAULT_USER["password"])

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.PERSONAL_CABINET)
    )
    assert driver.find_element(*MainPageLocators.PERSONAL_CABINET).is_displayed()

def test_login_from_password_recovery_form(driver):
    page = PasswordRecoveryPage(driver)
    page.open()
    page.click_login_button_from_recovery()
    login_page = LoginPage(driver)
    login_page.login(DEFAULT_USER["email"], DEFAULT_USER["password"])

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.PERSONAL_CABINET)
    )
    assert driver.find_element(*MainPageLocators.PERSONAL_CABINET).is_displayed()

