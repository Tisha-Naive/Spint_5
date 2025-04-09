from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

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
    # Раздел Булки
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    # Раздел Соусы
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    # Раздел Начинки
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")


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
