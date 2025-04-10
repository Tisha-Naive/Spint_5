from selenium import webdriver
from pages.registration_page import RegistrationPage
from utils.data_generator import generate_email

import time

def test_successful_registration(driver):
    page = RegistrationPage(driver)
    page.open()
    page.register("Тест", generate_email(), "qwerty123")

def test_short_password_error(driver):
    page = RegistrationPage(driver)
    page.open()
    page.register("Тест", generate_email(), "123")
    error = page.get_error_text()
    assert error == "Некорректный пароль"