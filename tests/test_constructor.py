import pytest
from pages.main_page import MainPage
from locators import MainPageLocators

class TestConstructorTabs:

    def test_switch_tabs(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        # Переход на "Соусы"
        main_page.click_sauces_tab()
        assert main_page.is_tab_selected(MainPageLocators.SAUCES_TAB_DIV)

        # Переход на "Начинки"
        main_page.click_fillings_tab()
        assert main_page.is_tab_selected(MainPageLocators.FILLINGS_TAB_DIV)

        # Переход на "Булки"
        main_page.click_buns_tab()
        assert main_page.is_tab_selected(MainPageLocators.BUNS_TAB_DIV)