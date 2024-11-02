from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogout:

    def test_logout(self, driver):
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
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_LINK_VIA_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGOUT_BUTTON))
        driver.find_element(*TestLocators.SEARCH_LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGIN_BUTTON))
        assert driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).text == "Войти"
