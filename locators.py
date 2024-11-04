from selenium.webdriver.common.by import By


class TestLocators:
    SEARCH_LOGIN_BUTTON_VIA_MAINPAGE = (By.XPATH, '//section[2]//button[contains(text(), "Войти в аккаунт")]')
    SEARCH_REGISTER_LINK_VIA_LOGIN_PAGE = (By.XPATH, '//a[text()="Зарегистрироваться"]')
    SEARCH_REGISTER_NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    SEARCH_REGISTER_EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    SEARCH_REGISTER_PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    SEARCH_REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    SEARCH_LOGIN_BUTTON = (By.XPATH, '//form[contains(@class, "Auth_form")]//button[text()="Войти"]')
    SEARCH_ERROR_INVALID_PASSWORD = (
        By.XPATH, '//div[contains(@class, "input__container")]//p[text()="Некорректный пароль"]')
    SEARCH_LOGIN_EMAIL_INPUT = (By.XPATH,
                                '//div[contains(@class, "Auth_login")]//div[contains(@class, "input__container")]//input[@type="text" and @name="name"]')
    SEARCH_LOGIN_PASSWORD_INPUT = (By.XPATH,
                                   '//div[contains(@class, "Auth_login")]//div[contains(@class, "input__container")]//input[@type="password" and @name="Пароль"]')
    SEARCH_ORDER_BUTTON = (By.XPATH,
                           '//div[contains(@class, "BurgerConstructor_basket__container")]//button[contains(text(), "Оформить заказ")]')
    SEARCH_PERSONAL_ACCOUNT_LINK = (
        By.XPATH, '//a[contains(@class, "AppHeader_header__link") and .//p[text()="Личный Кабинет"]]')
    SEARCH_LOGIN_LINK_VIA_REGISTER = (By.XPATH, "//a[contains(@class, 'Auth_link') and text()='Войти']")
    SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE = (
        By.XPATH, '//a[contains(@class, "Auth_link") and text()="Восстановить пароль"]')
    SEARCH_LOGIN_EMAIL_INPUT_VIA_PASSWORD_RECOVERY = (By.XPATH,
                                                      '//form[contains(@class, "Auth_form")]//div[contains(@class, "input_type_text")]//input[@type="text" and @name="name"]')
    SEARCH_RECOVERY_PASSWORD_BUTTON = (By.XPATH,
                                       '//form[contains(@class, "Auth_form")]//button[contains(@class, "button_button") and contains(@class, "button_button_type_primary") and text()="Восстановить"]')
    SEARCH_LOGIN_LINK_VIA_PASSWORD_RECOVERY = (By.XPATH,
                                               '//p[contains(@class, "text_type_main-default") and contains(text(), "Вспомнили пароль?")]/a[contains(@class, "Auth_link") and text()="Войти"]')
    SEARCH_PERSONAL_ACCOUNT_LINK_VIA_LOGIN = (By.XPATH,
                                              '//a[contains(@class, "AppHeader_header") and .//p[contains(@class, "AppHeader_header") and text()="Личный Кабинет"]]')
    SEARCH_LOGOUT_BUTTON = (
        By.XPATH,
        '//nav[contains(@class, "Account_nav")]//button[contains(@class, "Account_button") and text()="Выход"]')
    SEARCH_CONSTRUCTOR_VIA_ACCOUNT = (
        By.XPATH, '//a[contains(@class, "AppHeader_header__link")]//p[text()="Конструктор"]')
    SEARCH_LOGO = (By.XPATH, '//div[contains(@class, "AppHeader_header__logo")]/a')
    SEARCH_SAUCES_SECTION = (By.XPATH,
                             '//div[contains(@class, "tab_tab")]//span[text()="Соусы"]')
    SEARCH_FIRST_SAUCE_IN_CONSTRUCTOR = (
        By.XPATH,
        '//div[contains(@class, "tab_tab") and contains(@class, "tab_tab_type_current")]//span[text()="Соусы"]/ancestor::section//a[contains(@class, "BurgerIngredient_ingredient")]//p[text()="Соус Spicy-X"]')
    SEARCH_BUNS_SECTION = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Булки"]')
    SEARCH_FIRST_BUN_IN_CONSTRUCTOR = (By.XPATH, '//div[contains(@class, "tab_tab") and contains(@class, "tab_tab_type_current")]//span[text()="Булки"]/ancestor::section//a[contains(@class, "BurgerIngredient_ingredient")]//p[text()="Флюоресцентная булка R2-D3"]')
    SEARCH_FILLINGS_SECTION = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Начинки"]')
    SEARCH_FIRST_FILLING_IN_CONSTRUCTOR = (By.XPATH,
                                           '//div[contains(@class, "tab_tab") and contains(@class, "tab_tab_type_current")]//span[text()="Начинки"]/ancestor::section//a[contains(@class, "BurgerIngredient_ingredient")]//p[text()="Мясо бессмертных моллюсков Protostomia"]')
