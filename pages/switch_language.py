from pages.base_page import BasePage


class SwitchLanguage(BasePage):
    login_field_xpath = "//input[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[text()='Sign in']//parent::button"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    switch_language_button_xpath = "//span[text()='Polski']"

    def click_switch_language(self):
        self.click_on_the_element(self.switch_language_button_xpath)



