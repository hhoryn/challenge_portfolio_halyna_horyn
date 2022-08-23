from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//input[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[text()='Sign in']//parent::button"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = "Scouts panel - sign in"
    scouts_panel_xpath = "//h5[normalize-space(text())='Scouts Panel']"
    expected_text = 'Scouts Panel'
    remind_password_xpath = "//a[text()='Remind password']"
    language_box_english_xpath = "//div[text()='English']"
    language_box_polski_xpath = "//div[text()='Polski']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def assert_text_of_the_panel(self):
        self.assert_element_text(self.driver, self.scouts_panel_xpath, self.expected_text)


