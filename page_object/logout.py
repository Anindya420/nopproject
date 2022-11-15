class LoginPage:
    text_box_email_id = "Email"
    text_box_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    link_text_logout = "Logout"
    def __init__(self,driver):
        self.driver = driver
    def setUsername(self,uername):
        self.driver.find_element_by_id(self.text_box_email_id).clear()
        self.driver.find_element_by_id(self.text_box_email_id).send_keys(uername)
    def setPassword(self,password):
        self.driver.find_element_by_id(self.text_box_password_id).clear()
        self.driver.find_element_by_id(self.text_box_password_id).send_keys(password)
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_text_logout).click()
        