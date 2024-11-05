from helpers import *
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegister:

    def test_do_register(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_REGISTER_LINK_VIA_LOGIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_REGISTER_LINK_VIA_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_REGISTER_NAME_INPUT)
        )
        driver.find_element(*TestLocators.SEARCH_REGISTER_NAME_INPUT).send_keys(data_generate.generate_random_name())
        driver.find_element(*TestLocators.SEARCH_REGISTER_EMAIL_INPUT).send_keys(data_generate.generate_random_email())
        driver.find_element(*TestLocators.SEARCH_REGISTER_PASSWORD_INPUT).send_keys(
            data_generate.generate_random_password())
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGIN_BUTTON)
        )
        assert driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON).text == "Войти"

    def test_do_register_with_incorrect_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_VIA_MAINPAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_REGISTER_LINK_VIA_LOGIN_PAGE))
        WebDriverWait(driver, 6).until(
            expected_conditions.element_to_be_clickable(TestLocators.SEARCH_REGISTER_LINK_VIA_LOGIN_PAGE)
        )
        driver.find_element(*TestLocators.SEARCH_REGISTER_LINK_VIA_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_REGISTER_NAME_INPUT)
        )
        driver.find_element(*TestLocators.SEARCH_REGISTER_NAME_INPUT).send_keys(data_generate.generate_random_name())
        driver.find_element(*TestLocators.SEARCH_REGISTER_EMAIL_INPUT).send_keys(data_generate.generate_random_email())
        driver.find_element(*TestLocators.SEARCH_REGISTER_PASSWORD_INPUT).send_keys(12345)
        driver.find_element(*TestLocators.SEARCH_REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ERROR_INVALID_PASSWORD)
        )
        assert driver.find_element(*TestLocators.SEARCH_ERROR_INVALID_PASSWORD).text == "Некорректный пароль"
