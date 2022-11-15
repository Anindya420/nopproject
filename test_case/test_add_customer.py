import selenium
import pytest
from selenium import webdriver
from page_object.logout import LoginPage
from page_object.addnewcustomer import AddCustomer
from utiliti.readProperties import ReadConfig
from utiliti.customLogger import LogGen
import string
import random
class Test_automation_003:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_add_customer(self):
        self.logger.info("***********test_automation_start************")
        self.driver = webdriver.Chrome("C:\\chromedriver_win32 (2)\\chromedriver.exe")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()


        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login successfull")


        self.logger.info("start add customer test")


        self.addcust = AddCustomer(self.driver)  ### driver we need to crate again
        self.addcust.clickonCustomermenu()
        self.addcust.clickoncustomersubmenu()

        self.addcust.clickonAddnew()

        self.logger.info("Providing customer information")


        self.email = random_generator() + "@gmail.com"
        self.addcust.set_email(self.email)
        self.addcust.set_password("test123")
        self.addcust.set_customer_role("Guest")
        self.addcust.setManagervalue("Vendor 2")
        self.addcust.setGender("Female")
        self.addcust.passfirstname("Anindya")
        self.addcust.pass_last_name("Paul")
        self.addcust.setDOB("7/05/1993")
        self.addcust.setCompayName("Infosys")
        self.addcust.setAdmin("this is for testing")
        self.addcust.clickSave()

        self.logger.info("saving customer info")

        self.logger.info("add customer validation started")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("add customer test passed")
        else:
            self.driver.save_screenshot("C:\\Users\\hp\\PycharmProjects\\nopproject\\screenshot\\add_customer.jpg")
            self.logger.error("test Automation Failerd")
            assert True == False
        self.driver.close()
        self.logger.info("Endinf Home Page Title Test")
def random_generator(size=8,chars = string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))
