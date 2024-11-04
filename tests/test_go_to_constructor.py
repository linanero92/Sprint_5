from locators import TestLocators
from data import email_for_login, password_for_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestGoToConstructor:

    def test_go_to_constructor_via_constructor_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE))
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE).click()
        driver.find_element(*TestLocators.SEARCH_LOGIN_EMAIL_INPUT).send_keys(
            email_for_login)
        driver.find_element(*TestLocators.SEARCH_LOGIN_PASSWORD_INPUT).send_keys(password_for_login)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_LINK_VIA_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGOUT_BUTTON))
        driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR_VIA_ACCOUNT).click()
        assert driver.find_element(*TestLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR).text == "Флюоресцентная булка R2-D3"


    def test_go_to_constructor_via_logo(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE))
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE).click()
        driver.find_element(*TestLocators.SEARCH_LOGIN_EMAIL_INPUT).send_keys(
            email_for_login)
        driver.find_element(*TestLocators.SEARCH_LOGIN_PASSWORD_INPUT).send_keys(password_for_login)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_LINK_VIA_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGOUT_BUTTON))
        driver.find_element(*TestLocators.SEARCH_LOGO).click()
        assert driver.find_element(*TestLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR).text == "Флюоресцентная булка R2-D3"

