from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from MathNationSections.elementsDefinitions import *
import unittest
# import time


class InitialTests(object):
    def __init__(self, my_driver):
        self.driver = my_driver
        self.elements = ElementsToBeFound(self.driver)

    # Login into Staging / Testing environment
    def login(self, school, username, password):
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.schoolName))
        self.driver.find_element(*self.elements.schoolName).send_keys(school + Keys.ARROW_DOWN)
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.TX))
        self.driver.find_element(*self.elements.TX).click()
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.username))
        self.driver.find_element(*self.elements.username).send_keys(username)
        self.driver.find_element(*self.elements.password).send_keys(password)
        self.driver.find_element(*self.elements.loginButton).click()

    def play_video_current_subject_select_expert_first(self):
        tc = unittest.TestCase('__init__')
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.currentSubject))
        if self.driver.find_element(*self.elements.currentSubject).text != "Algebra 1":
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.currentSubject))
            self.driver.find_element(*self.elements.currentSubject).click()
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.Alg1))
            self.driver.find_element(*self.elements.Alg1).click()
            # drop_down_menu = Select(self.driver.find_element(*self.elements.currentSubject))
            # drop_down_menu.select_by_visible_text('Algebra 1')
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.Alg1_Sect1_dropdown))
        self.driver.find_element(*self.elements.Alg1_Sect1_dropdown).click()
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.tutorAmy))
        self.driver.find_element(*self.elements.tutorAmy).click()
        WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(self.elements.Alg1_Topic1_PlayVideo))
        self.driver.find_element(*self.elements.Alg1_Topic1_PlayVideo).click()
        tc.assertTrue(self.driver.find_element(*self.elements.VideoPlayer).is_displayed())
