from selenium.webdriver.common.by import By


# Define elements to be found later
class ElementsToBeFound(object):
    def __init__(self, my_driver):
        self.driver = my_driver

        #############################
        # Elements in Log In Window#
        #############################
        self.schoolName = (By.NAME, "school-name")
        self.TX = (By.LINK_TEXT, "---TX--- - Austin")
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.loginButton = (By.CSS_SELECTOR, ".pull-right")
