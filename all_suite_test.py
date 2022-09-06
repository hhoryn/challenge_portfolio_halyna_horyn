import unittest

from unittest.loader import makeSuite

from test_cases.log_in_to_the_system import TestLoginPage
from test_cases.add_player_page import TestAddPlayer
from test_cases.add_report_page_test import TestAddingReport
from test_cases.edit_player_page import TestEditPlayer
from test_cases.logout_test import TestLogOut
from test_cases.switch_language_test import TestSwitchLanguage
from test_cases.framework import Test


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestAddPlayer))
    test_suite.addTest(makeSuite(TestAddingReport))
    test_suite.addTest(makeSuite(TestEditPlayer))
    test_suite.addTest(makeSuite(TestLogOut))
    test_suite.addTest(makeSuite(TestSwitchLanguage))
    test_suite.addTest(makeSuite(Test))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
