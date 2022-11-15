import time
from selenium.webdriver.support.ui import Select
class AddCustomer:
    customer_tab = "(//a[@href='#'])[7]"
    second_customer_tab = "(//a[@class='nav-link'])[22]"
    add_new = "//a[@class='btn btn-primary']"
    email_id = "//input[@id='Email']"
    pass_word = "//input[@id='Password']"
    first_name = "//input[@id='FirstName']"
    last_name = "//input[@id='LastName']"
    gender_male = "//input[@id='Gender_Male']"
    gender_female = "//input[@id='Gender_Female']"
    date_of_borth = "//input[@id='DateOfBirth']"
    company_name = "//input[@id='Company']"
    tax_extemnt = "//input[@id='IsTaxExempt']"
    news = "(//div[@role='listbox'])[1]"
    customer_role = "(//div[@role='listbox'])[2]"
    registered = "//li[contains(text(),'Registered')]"
    administrator = "//li[contains(text(),'Administrators')]"
    forum_modetaror = "//li[contains(text(),'Forum Moderators')]"
    guest = "//li[contains(text(),'Guests')]"
    vendors = "//li[contains(text(),'Vendors')]"
    drop_down = "//select[@id='VendorId']"
    add_comment = "//textarea[@id='AdminComment']"
    save = '//button[@name="save"]'
    def __init__(self,driver):
        self.driver = driver
    def clickonCustomermenu(self):
            self.driver.find_element_by_xpath(self.customer_tab).click()
    def clickoncustomersubmenu(self):
        self.driver.find_element_by_xpath(self.second_customer_tab).click()
    def clickonAddnew(self):
        self.driver.find_element_by_xpath(self.add_new).click()
    def set_email(self,email):
        self.driver.find_element_by_xpath(self.email_id).send_keys(email)
    def set_password(self,password):
        self.driver.find_element_by_xpath(self.pass_word).send_keys(password)
    def set_customer_role(self,role):
        self.driver.find_element_by_xpath(self.customer_role).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.registered)
        elif role == "Administrator":
            self.listitem = self.driver.find_element_by_xpath(self.administrator)
        elif role == "Guest":
            time.sleep(3)
            self.driver.find_element_by_xpath("//span[@title='delete']").click()
            self.listitem = self.driver.find_element_by_xpath(self.guest)
        elif role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.registered)
        elif role == "Vendor":
            self.listitem = self.driver.find_element_by_xpath(self.vendors)
        else :
            self.listitem= self.driver.find_element_by_xpath(self.guest)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)
    def setManagervalue(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drop_down))
        drp.select_by_visible_text(value)
    def setGender(self,gender):
        if gender == "male":
            self.driver.find_element_by_xpath(self.gender_male).click()
        elif gender == "female":
            self.driver.find_element_by_xpath(self.gender_female).click()
        else :
            self.driver.find_element_by_xpath(self.gender_female).click()
    def passfirstname(self,fname):
        self.driver.find_element_by_xpath(self.first_name).send_keys(fname)
    def pass_last_name(self,lname):
        self.driver.find_element_by_xpath(self.last_name).send_keys(lname)
    def setDOB(self,dob):
        self.driver.find_element_by_xpath(self.date_of_borth).send_keys(dob)
    def setCompayName(self,company):
        self.driver.find_element_by_xpath(self.company_name).send_keys(company)
    def setAdmin(self,content):
        self.driver.find_element_by_xpath(self.add_comment).send_keys(content)
    def clickSave(self):
        self.driver.find_element_by_xpath(self.save).click()
        
        