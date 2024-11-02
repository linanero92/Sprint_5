from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    def test_constructor_sauce_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_SAUCES_SECTION).click()
        assert driver.find_element(*TestLocators.SEARCH_FIRST_SAUCE_IN_CONSTRUCTOR).text == "Соус Spicy-X"
        driver.quit()

    def test_constructor_sauce_section_via_login(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGIN_EMAIL_INPUT))
        driver.find_element(*TestLocators.SEARCH_LOGIN_EMAIL_INPUT).send_keys(
            'alina_kuptsova_15_000@.ya.ru')
        driver.find_element(*TestLocators.SEARCH_LOGIN_PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        driver.find_element(*TestLocators.SEARCH_SAUCES_SECTION).click()
        assert driver.find_element(*TestLocators.SEARCH_FIRST_SAUCE_IN_CONSTRUCTOR).text == "Соус Spicy-X"
        driver.quit()

    def test_constructor_buns_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        assert driver.find_element(*TestLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR).text == "Флюоресцентная булка R2-D3"
        driver.quit()

    def test_constructor_buns_section_via_login(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE))
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE).click()
        driver.find_element(*TestLocators.SEARCH_LOGIN_EMAIL_INPUT).send_keys(
            'alina_kuptsova_15_000@.ya.ru')
        driver.find_element(*TestLocators.SEARCH_LOGIN_PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR).text == "Флюоресцентная булка R2-D3"
        driver.quit()

    def test_constructor_fillings_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_FILLINGS_SECTION).click()
        assert driver.find_element(
            *TestLocators.SEARCH_FIRST_FILLING_IN_CONSTRUCTOR).text == "Мясо бессмертных моллюсков Protostomia"
        driver.quit()

    def test_constructor_fillings_section_via_login(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGIN_EMAIL_INPUT))
        driver.find_element(*TestLocators.SEARCH_LOGIN_EMAIL_INPUT).send_keys(
            'alina_kuptsova_15_000@.ya.ru')
        driver.find_element(*TestLocators.SEARCH_LOGIN_PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        driver.find_element(*TestLocators.SEARCH_FILLINGS_SECTION).click()
        assert driver.find_element(
            *TestLocators.SEARCH_FIRST_FILLING_IN_CONSTRUCTOR).text == "Мясо бессмертных моллюсков Protostomia"
