from pages.base_page import BasePage


class AddPlayer(BasePage):
    login_field_xpath = "//input[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[text()='Sign in']//parent::button"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    name_xpath = "//input[@name='name']"
    surname_xpath = "//input[@name='surname']"
    age_xpath = "//input[@name='age']"
    main_position_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//button[@type='submit']"

    def type_in_first_name(self):
        self.field_send_keys(self.name_xpath)

    def type_in_surname(self):
        self.field_send_keys(self.surname_xpath)

    def select_age(self):
        self.field_send_keys(self.age_xpath)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)


