from selenium.webdriver.common.by import By


# Define elements to be found later
class ElementsToBeFound(object):
    def __init__(self, my_driver):
        self.driver = my_driver

        #############################
        # Elements in Log In Window #
        #############################
        self.schoolName = (By.NAME, "school-name")
        self.TX = (By.LINK_TEXT, "---TX--- - Austin")
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.loginButton = (By.CSS_SELECTOR, ".pull-right")

        ############################################
        # Elements in Student Area - Videos Window #
        ############################################
        self.currentSubject = (By.ID, "current-subject")
        self.Alg1 = (By.CSS_SELECTOR, "button[onclick='updateUserSubject(127, true)']")
        self.Alg1_Sect1_dropdown = (By.CSS_SELECTOR, ".file-tree > .folder:nth-child(4) .droptarget-icon")
        self.tutorAmy = (By.CSS_SELECTOR, "open .tutor_image_wrapper:nth-child(1) > .tutor_image")
        self.Alg1_Topic1_PlayVideo = (By.LINK_TEXT,
                                      "Topic 1: Using Expressions to Represent Real-World Situations "
                                      "(Page 3) (30 min 53 sec)")
        self.VideoPlayer = (By.CSS_SELECTOR, ".jw-video")

        # tour-select-subject > ul > li > ul > li:nth-child(5) > button
        # //*[@id="tour-select-subject"]/ul/li/ul/li[5]/button
        # /html/body/article/div[1]/div/div[1]/ul/li/ul/li[5]/button
        # // button[ @ onclick = 'updateUserSubject(127, true)']::span[text()='Algebra 1']
        # //div[@id='tour-select-subject']/ul/li/ul/li[5]/button


