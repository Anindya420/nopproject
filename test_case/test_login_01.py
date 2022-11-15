import pytest
from selenium import webdriver
from page_object.logout import LoginPage
from utiliti.readProperties import ReadConfig
# from conftest import setup
from utiliti.customLogger import LogGen
from utiliti import excel_file
import time
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path = "C:\\Users\\hp\\PycharmProjects\\nopproject\\test_data\\test_data.xlsx"
    # username = ReadConfig.getUsername()
    # password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    # def test_homepage_title(self):
    #     self.logger.info("********** Test__001 ******")
    #     self.logger.info("verify the homepage title")
    #     self.driver = webdriver.Chrome("C:\\chromedriver_win32 (2)\\chromedriver.exe")
    #     self.driver.get(self.baseURL)
    #     a = self.driver.title
    #     if a == "Your ste. Login":
    #         assert True
    #         self.driver.close()
    #         self.logger.info("Test Passed")
    #     else:
    #         self.driver.save_screenshot("D:\\bootstarp\\abcd.png")
    #         self.driver.close()
    #         self.logger.error("Test failed")
    #         assert False
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("********** Test__002 ******")
        self.logger.info("verify the test login")
        self.driver = webdriver.Chrome("C:\\chromedriver_win32 (2)\\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.row = excel_file.max_row(self.path,"Sheet1")
        print(self.row)
        lst_status = []
        for r in range(2,self.row+1):
            self.user = excel_file.read_data(self.path,"Sheet1",r,1)
            self.password = excel_file.read_data(self.path,"Sheet1",r,2)
            self.exp = excel_file.read_data(self.path,"Sheet1",r,3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(4)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("pass")
                    self.lp.clickLogout()
                    lst_status.append('pass')
                elif self.exp == "fail":
                    self.logger.info("failed")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("failed")
                    lst_status.append("failed")
                elif self.exp == "fail" :
                    self.logger.info("passed")
                    lst_status.append("passed")
        if "fail" not in lst_status:
            self.logger.info("passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("loging failed")
            self.driver.close()
            assert False








