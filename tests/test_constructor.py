from locators import TestLocators

class TestConstructor:

    def test_constructor_sauce_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_SAUCES_SECTION).click()
        assert driver.find_element(*TestLocators.SEARCH_FIRST_SAUCE_IN_CONSTRUCTOR).text == "Соус Spicy-X"

    def test_constructor_fillings_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_FILLINGS_SECTION).click()
        assert driver.find_element(
            *TestLocators.SEARCH_FIRST_FILLING_IN_CONSTRUCTOR).text == "Мясо бессмертных моллюсков Protostomia"

    def test_constructor_buns_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SEARCH_SAUCES_SECTION).click()
        driver.find_element(*TestLocators.SEARCH_BUNS_SECTION).click()
        assert driver.find_element(*TestLocators.SEARCH_FIRST_BUN_IN_CONSTRUCTOR).text == "Флюоресцентная булка R2-D3"

