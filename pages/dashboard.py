import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from pages.base_page import BasePage


class Dashboard(BasePage):
    add_player_button_xpath = "//span[text()='Add player']//parent::button"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl"
    sign_out_button_xpath = "//span[text()='Sign out']"
    players_button_xpath = "//span[text()='Players']"
    switch_language_button_xpath = "//span[text()='Polski']"
    wait = WebDriverWait(webdriver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def click_sign_out(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_switch_language(self):
        self.click_on_the_element(self.switch_language_button_xpath)


#    scouts_panel_heading_xpath = "//h6[text()='Scouts Panel']"
#    main_page_xpath = "//span[text()='Main page']"
#    scouts_panel_logo_xpath = "//div[@title='Logo Scouts Panel']"
#    add_player_button_xpath = "//span[text()='Add player']//parent::button"
#    dev_team_contact_xpath = "//span[text()='Dev team contact']//parent::a"
#    sign_out_heading_xpath = "span[text()='Sign out']"
#    players_count_box_xpath = "//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'][1]"
#    shortcuts_box_xpath = "//h2[text()='Shortcuts']//parent::div"
#    toolbar_xpath = "//button[@aria-label='menu']//parent::div"
#    payers_heading_xpath = "//span[text()='Players']"
