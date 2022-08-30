import os
import unittest
import time

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.add_report import AddReport
from pages.edit_player import EditPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestAddingReport(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_editing_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_players_button()
        edit_player_page = EditPlayer(self.driver)
        edit_player_page.click_on_the_search_button()
        edit_player_page.find_the_player()
        edit_player_page.click_on_the_given_player()
        reports_page = AddReport(self.driver)
        reports_page.click_on_the_reports_button()
        reports_page.click_on_the_add_report_button()
        reports_page.click_on_the_create_report_button()
        reports_page.click_on_the_submit_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

