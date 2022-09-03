from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from MathNationSections.modes import *
from MathNationSections.initialTests import *
import HtmlTestRunner
import unittest
import os
# import time


class MathNation(unittest.TestCase):
    # Browser Stack Login vriables
    username = os.environ.get('BROWSERSTACK_USERNAME', 'blakemiller')
    accessKey = os.environ.get('BROWSERSTACK_ACCESS_KEY', 'Fp5PrsuQKEX2xowtkyv9')
    maxDiff = None  # Allowing String Validations wih no Lenght Limits
    RunThis = True  # Defining Test Cases to be Run
    NotRunThis = False  # Defining Test Cases to be Skipped
    # This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
    caps = {
        # Add these capabilities to your test script
        "os": "Windows",
        "os_version": "10",
        "browser": "Chrome",
        "browser_version": "latest"
    }

    # Chrome driver setUp
    def setUp(self):
        self.chromeOptions(1)
        # self.run_session(self.caps)
        self.driver.maximize_window()
        self.enterLink = EnterLink(self.driver)
        self.initial = InitialTests(self.driver)

    # In order to run in BrowserStack
    def run_session(self, desired_cap):
        # Other imports and desired_cap definition goes here
        self.driver = webdriver.Remote(
            command_executor='https://' + self.username + ':' + self.accessKey + '@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap
        )

    def chromeOptions(self, number):
        # Chrome Initialization with Mic and Camera allowed
        opt = Options()
        # 1 to allow and 2 to block
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": number,
            "profile.default_content_setting_values.media_stream_camera": number
        })
        # Use this option to run the test in the background
        # opt.add_argument('--headless')

        # Use this option to disable information bars on the browser
        opt.add_experimental_option("excludeSwitches", ['enable-automation'])

        # Chrome is opened with Max Window and defined init parameters
        self.driver = webdriver.Chrome(options=opt, executable_path='chromedriver.exe')

    # TEST CASES
    @unittest.skipUnless(RunThis, "Test not run this time")
    def test_01(self):
        self.enterLink.enter_staging_link()
        self.driver.save_screenshot("Screenshots/Login_Window.png")
        self.initial.login('--TX--', 'JulieTXStudent1', 'Password1')
        self.driver.save_screenshot("Screenshots/Initial_Window.png")
        self.initial.play_video_current_subject_select_expert_first()
        self.driver.save_screenshot("Screenshots/Video_Tile.png")

    # Exit browser
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
    unittest.main()
