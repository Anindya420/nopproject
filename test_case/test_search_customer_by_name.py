import time
from selenium import webdriver
import pytest
from page_object.logout import LoginPage
from page_object.addnewcustomer import AddCustomer
from page_object.SearchCustomerPage import SearchCustomer
from utiliti.readProperties import ReadConfig
from utiliti.customLogger import LogGen
class Test_search_by_name__005:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test001_search_email(self):
        self.logger.info("search customer email")
        self.driver = webdriver.Chrome("C:\\chromedriver_win32 (2)\\chromedriver.exe")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login Sucessfull")


        self.logger.info("starting search by name")


        self.add_cust = AddCustomer(self.driver)
        self.add_cust.clickonCustomermenu()
        self.add_cust.clickoncustomersubmenu()
        self.logger.info("searching customer by email id")
        search_cust = SearchCustomer(self.driver)
        # search_cust.setfirstname("Victoria ")
        # search_cust.setLastname("Terces")
        # search_cust.clickSearch()
        # time.sleep(5)
        er = search_cust.SearchBy_Name("Victoria Terces")
        assert True == er
        self.logger.info("test passed sucessfulyy")
        self.driver.close()
        

