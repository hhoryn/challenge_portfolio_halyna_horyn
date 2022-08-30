from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class EditPlayer(BasePage):
    login_field_xpath = "//input[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[text()='Sign in']//parent::button"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    players_button_xpath = "//span[text()='Players']"
    search_bar_xpath = "// input[@aria-label='search']"
    player_xpath = "//div[text()='Horyn']"
    leg_dropdown_xpath = "//div[@id='mui-component-select-leg']"
    leg_xpath = "//li[@data-value='right']"
    submit_button_xpath = "//span[text()='Submit']"

    def click_on_the_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def click_on_the_search_button(self):
        self.click_on_the_element(self.search_bar_xpath)

    def type_in_players_name(self, name):
        self.field_send_keys(self.search_bar_xpath, name)

    def find_the_player(self):
        wait = WebDriverWait(self.driver, 10)
        search_query = 'Horyn'
        search_bar_xpath = "// input[@aria-label='search']"
        wait.until(EC.presence_of_element_located((By.XPATH, search_bar_xpath))).send_keys(search_query)
        wait.until(EC.presence_of_element_located((By.XPATH, search_bar_xpath))).send_keys(Keys.ENTER)

    def click_on_the_given_player(self):
        self.click_on_the_element(self.player_xpath)

    def click_on_the_leg_field(self):
        self.click_on_the_element(self.leg_dropdown_xpath)

    def click_on_the_right_leg(self):
        self.click_on_the_element(self.leg_xpath)

    def click_submit(self):
        self.click_on_the_element(self.submit_button_xpath)

    def wait_for_player_to_be_clickable(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Horyn')))




