from locators import TestLocators
from data import email_for_login, password_for_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:

    def test_login_via_login_on_the_main_page(self, driver):
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
        assert driver.find_element(*TestLocators.SEARCH_ORDER_BUTTON).text == "Оформить заказ"


    def test_login_via_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGIN_EMAIL_INPUT))
        driver.find_element(*TestLocators.SEARCH_LOGIN_EMAIL_INPUT).send_keys(
            email_for_login)
        driver.find_element(*TestLocators.SEARCH_LOGIN_PASSWORD_INPUT).send_keys(password_for_login)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.SEARCH_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_via_register_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_REGISTER_LINK_VIA_LOGIN_PAGE))
        WebDriverWait(driver, 6).until(
            expected_conditions.element_to_be_clickable(TestLocators.SEARCH_REGISTER_LINK_VIA_LOGIN_PAGE)
        )
        driver.find_element(*TestLocators.SEARCH_REGISTER_LINK_VIA_LOGIN_PAGE).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.element_to_be_clickable(TestLocators.SEARCH_LOGIN_LINK_VIA_REGISTER)
        )
        driver.find_element(*TestLocators.SEARCH_LOGIN_LINK_VIA_REGISTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGIN_EMAIL_INPUT))
        driver.find_element(*TestLocators.SEARCH_LOGIN_EMAIL_INPUT).send_keys(
            email_for_login)
        driver.find_element(*TestLocators.SEARCH_LOGIN_PASSWORD_INPUT).send_keys(password_for_login)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.SEARCH_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_via_password_recovery(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE))
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_PASSWORD_RECOVERY_LINK_VIA_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located
            (TestLocators.SEARCH_LOGIN_EMAIL_INPUT_VIA_PASSWORD_RECOVERY))
        driver.find_element(*TestLocators.SEARCH_LOGIN_EMAIL_INPUT_VIA_PASSWORD_RECOVERY).send_keys(
            email_for_login)
        driver.find_element(*TestLocators.SEARCH_RECOVERY_PASSWORD_BUTTON)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located
            (TestLocators.SEARCH_LOGIN_LINK_VIA_PASSWORD_RECOVERY))
        driver.find_element(*TestLocators.SEARCH_LOGIN_LINK_VIA_PASSWORD_RECOVERY).click()
        driver.find_element(*TestLocators.SEARCH_LOGIN_EMAIL_INPUT).send_keys(
            email_for_login)
        driver.find_element(*TestLocators.SEARCH_LOGIN_PASSWORD_INPUT).send_keys(password_for_login)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.SEARCH_ORDER_BUTTON).text == "Оформить заказ"
