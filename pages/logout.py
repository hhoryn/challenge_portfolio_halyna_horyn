from pages.base_page import BasePage


class LogOut(BasePage):
    login_field_xpath = "//input[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[text()='Sign in']//parent::button"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    sign_out_button_xpath = "//span[text()='Sign out']"

    def click_sign_out(self):
        self.click_on_the_element(self.sign_out_button_xpath)







