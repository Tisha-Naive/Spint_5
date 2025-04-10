from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import DEFAULT_USER
from locators import MainPageLocators

def test_logout(driver):
    main_page = MainPage(driver)
    profile_page = ProfilePage(driver)

    # Открываем главную страницу
    main_page.open()

    # Кликаем на «Личный кабинет»
    main_page.click_login_button()

    # Вход в аккаунт
    login_page = LoginPage(driver)
    login_page.login(DEFAULT_USER["email"], DEFAULT_USER["password"])

    # Ожидаем появления кнопки «Оформить заказ» как подтверждение входа
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
    )

    # Переход в личный кабинет
    main_page.click_personal_cabinet()

    # Кликаем по кнопке «Выход»
    profile_page.click_logout_button()

    # Проверяем, что перешли на страницу входа

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON2)
    )