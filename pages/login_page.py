from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//input[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[text()='Sign in']//parent::button"
    scouts_panel_xpath = "//h5[normalize-space(text())='Scouts Panel']"
    remind_password_xpath = "//a[text()='Remind password']"
    language_box_english_xpath = "//div[text()='English']"
    language_box_polski_xpath = "//div[text()='Polski']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
