from selenium import webdriver
from pages.registration_page import RegistrationPage
from utils.data_generator import generate_email

import time

def test_successful_registration():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        page = RegistrationPage(driver)
        page.open()
        page.register("Тест", generate_email(), "qwerty123")
    finally:
        driver.quit()

def test_short_password_error():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        page = RegistrationPage(driver)
        page.open()
        page.register("Тест", generate_email(), "123")
        time.sleep(1)
        error = page.get_error_text()
        assert error == "Некорректный пароль"
    finally:
        driver.quit()