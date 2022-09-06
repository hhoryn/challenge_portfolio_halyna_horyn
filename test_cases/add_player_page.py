import os
import unittest
import time

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.add_player import AddPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()
        new_player = AddPlayer(self.driver)
        new_player.type_in_first_name('Halyna')
        new_player.type_in_surname('Horyn')
        new_player.type_in_age('19041999')
        new_player.type_in_main_position('goalkeeper')
        new_player.click_on_the_submit_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()