from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from MathNationSections.elementsDefinitions import *
from selenium.webdriver.common.keys import Keys
import unittest
import time


class SmokeTests(object):
    def __init__(self, my_driver):
        self.driver = my_driver
        self.elements = ElementsToBeFound(self.driver)

    # Enter as Tutor and login into TMS
    def enter_as_tutor(self):
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.schoolName))
        self.driver.find_element(*self.elements.schoolName).send_keys('--TX--')
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.TX))
        self.driver.find_element(*self.elements.TX).click()
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.username))
        self.driver.find_element(*self.elements.username).send_keys('JulieTXTeacher')
        self.driver.find_element(*self.elements.password).send_keys('Password1')
        self.driver.find_element(*self.elements.loginButton).click()
        time.sleep(10)

