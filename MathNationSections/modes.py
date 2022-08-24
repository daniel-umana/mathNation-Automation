from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import *
from MathNationSections.elementsDefinitions import *
from MathNationSections.smokeTest import *
from MathNationSections.xmlReader import *
import unittest


class EnterLink(object):
    def __init__(self, my_driver):
        self.driver = my_driver
        self.elements = ElementsToBeFound(self.driver)
        self.configuration = XmlReader()

    # Handles the browser alert in case it appears
    def alert_error_exception(self):
        try:
            Alert(self.driver).accept()
        except NoAlertPresentException:
            pass

    # Use Testing Domain
    def enter_testing_link(self):
        self.driver.get(self.configuration.test_init_data('testingURL'))
        self.alert_error_exception()

    # Use Staging Domain
    def enter_staging_link(self):
        self.driver.get(self.configuration.test_init_data('stagingURL'))
        self.alert_error_exception()

