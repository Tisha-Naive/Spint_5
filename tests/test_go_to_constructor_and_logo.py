from constants import BASE_URL
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigation_with_logo_and_constructor(driver):
    page = MainPage(driver)

    # Открытие главной страницы
    page.open()

    # Переход по клику на "Конструктор"
    page.click_constructor_button()

    # Проверяем, что находимся на странице конструктора
    WebDriverWait(driver, 10).until(
        EC.url_contains(BASE_URL)
    )
    assert BASE_URL in driver.current_url, "Не перешли на страницу конструктора"

    page.click_stellar_burgers_logo()

    # Проверка, что вернулись на главную страницу
    WebDriverWait(driver, 10).until(
        EC.url_contains(BASE_URL)
    )
    assert BASE_URL in driver.current_url, "Не вернулись на главную страницу по клику на логотип"
