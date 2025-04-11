from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGIN_BUTTON2 = (By.XPATH, "//button[text()='Войти']")

    # Кнопка «Личный Кабинет» в шапке
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    # Логотип Stellar Burgers
    LOGO_BUTTON = (By.XPATH, "//svg[@width='290' and @height='50']")

    # Кнопка «Личный Кабинет» в шапке с другим классом
    PERSONAL_CABINET_BUTTON = (
        By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']"
    )

    # Локатор для логотипа Stellar Burgers (с учетом ссылки)
    STELLAR_BURGERS_LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

    # Вкладки конструктора
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")

    SAUCES_TAB_DIV = (By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'tab_tab__')]")
    FILLINGS_TAB_DIV = (By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'tab_tab__')]")
    BUNS_TAB_DIV = (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab__')]")

    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")
    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")

    # Кнопки

    PERSONAL_CABINET = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    PROFILE_LINK = (By.XPATH, "//a[contains(@class, 'Account_link') and @aria-current='page' and text()='Профиль']")



class RegistrationPageLocators:
    # Поле Имя (сюда вводится email по багу)
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    # Поле Пароль
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка Зарегистрироваться
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Ссылка на логин (форма входа)
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    # Сообщение об ошибке (например, для короткого пароля)
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")


class LoginPageLocators:
    # Поле Email (возможно, это поле name='name' — баг)
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    # Поле Пароль
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка Войти
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'button_button_type_primary') and text()='Войти']"
    )
    # Ссылка на регистрацию
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    # Ссылка на восстановление пароля
    RECOVER_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")


class PasswordRecoveryPageLocators:
    # Ссылка на форму логина
    LOGIN_LINK = (By.LINK_TEXT, "Войти")


class AccountPageLocators:
    # Кнопка Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
