from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_go_to_personal_cabinet(driver):
    page = MainPage(driver)  # Страница, на которой расположен переход в Личный кабинет
    page.open()  # Открытие главной страницы

    # Переход по клику на кнопку "Вход"
    page.click_login_button()

    # Заполнение формы входа (пример, если поля email и пароль есть на странице)
    login_page = LoginPage(driver)  # Нужно создать класс для страницы логина
    login_page.enter_email("akimova1@mail.ru")
    login_page.enter_password("йцукен123456")
    login_page.submit_login()

    # Переход по клику на кнопку "Личный кабинет" после входа
    page.click_personal_cabinet()

    # Ждём, пока элемент "Профиль" не станет видимым (подтверждение, что мы в личном кабинете)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@class, 'Account_link') and @aria-current='page' and text()='Профиль']"))
    )


