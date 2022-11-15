import pytest
from selenium import webdriver
from page_object.logout import LoginPage
from utiliti.readProperties import ReadConfig
# from conftest import setup
from utiliti.customLogger import LogGen
class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_homepage_title(self):
        self.logger.info("********** Test__001 ******")
        self.logger.info("verify the homepage title")
        self.driver = webdriver.Chrome("C:\\chromedriver_win32 (2)\\chromedriver.exe")
        self.driver.get(self.baseURL)
        a = self.driver.title
        if a == "Your ste. Login":
            assert True
            self.driver.close()
            self.logger.info("Test Passed")
        else:
            self.driver.save_screenshot("D:\\bootstarp\\abcd.png")
            self.driver.close()
            self.logger.error("Test failed")
            assert False
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("********** Test__002 ******")
        self.logger.info("verify the test login")
        self.driver = webdriver.Chrome("C:\\chromedriver_win32 (2)\\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        title = self.driver.title
        if title == "Dashboard nopCommerce administration":
            self.driver.close()
            assert True
            self.logger.info("Test Passed")
        else:
            self.driver.save_screenshot("D:\\bootstarp\\test2.png")
            self.driver.close()
            self.logger.error("test failed")
            assert False

