from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

def test_constructor_tabs(driver):
    main_page = MainPage(driver)
    main_page.open()

    # Переход к разделу «Соусы»
    main_page.click_sauces_tab()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Соусы']"))
    )

    # Переход к разделу «Начинки»
    main_page.click_fillings_tab()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']"))
    )

    # Переход к разделу «Булки»
    main_page.click_buns_tab()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']"))
    )
