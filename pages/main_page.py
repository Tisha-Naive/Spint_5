from selenium.webdriver.common.by import By
from locators import MainPageLocators  # Импортируем локаторы
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def click_login_button(self):
        self.driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    def click_personal_account_button(self):
        self.driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    def click_personal_cabinet(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)
        )
        self.driver.find_element(*MainPageLocators.PERSONAL_CABINET_BUTTON).click()

    # Клик по кнопке "Конструктор"
    def click_constructor_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    # Клик на логотип Stellar Burgers
    def click_stellar_burgers_logo(self):
        STELLAR_BURGERS_LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(STELLAR_BURGERS_LOGO)
        )
        logo = self.driver.find_element(*STELLAR_BURGERS_LOGO)
        self.driver.execute_script("arguments[0].click();", logo)

    def click_buns_tab(self):
        self.driver.find_element(*MainPageLocators.BUNS_TAB).click()

    def click_sauces_tab(self):
        self.driver.find_element(*MainPageLocators.SAUCES_TAB).click()

    def click_fillings_tab(self):
        self.driver.find_element(*MainPageLocators.FILLINGS_TAB).click()

    def is_tab_selected(self, tab_locator):
        """Проверяет, что вкладка находится в активном состоянии (по классу)"""
        element = self.wait.until(EC.visibility_of_element_located(tab_locator))
        self.wait.until(EC.text_to_be_present_in_element_attribute(
            tab_locator, "class", "tab_tab_type_current__2BEPc"
        ))
        return "tab_tab_type_current__2BEPc" in element.get_attribute("class")
