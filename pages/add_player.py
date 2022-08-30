from pages.base_page import BasePage


class AddPlayer(BasePage):
    login_field_xpath = "//input[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[text()='Sign in']//parent::button"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    add_player_button_xpath = "//span[text()='Add player']//parent::button"
    name_xpath = "//input[@name='name' and @type='text']"
    surname_xpath = "//input[@name='surname']"
    age_xpath = "//input[@name='age']"
    main_position_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//button[@type='submit']"

    def type_in_first_name(self, name):
        self.field_send_keys(self.name_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_xpath, surname)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_xpath, position)

    def type_in_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)













   # def assert_the_error_message_text(self):
        #self.assert_element_text(self.driver, self.error_message, self.expected_error_message)

