class SearchCustomer:
    textEmail_id = "SearchEmail"
    txtfirstname_id = "SearchFirstName"
    txtlastname_id = "SearchLastName"
    button_search_id = "search-customers"
    table_xpath = "//table[@id='customers-grid']"
    table_row_xpath = "//table[@id='customers-grid']//tbody//tr"
    table_column_xpath = "//table[@id='customers-grid']//tbody//tr//td"
    def __init__(self,driver):
        self.driver = driver
    def SetEmail(self,email):
        self.driver.find_element_by_id(self.textEmail_id).send_keys(email)
    def setfirstname(self,fname):
        self.driver.find_element_by_id(self.txtfirstname_id).send_keys(fname)
    def setLastname(self,Lastname):
        self.driver.find_element_by_id(self.txtlastname_id).send_keys(Lastname)
    def clickSearch(self):
        self.driver.find_element_by_id(self.button_search_id).click()
    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.table_row_xpath))
    def getNoOfColumn(self):
        return len(self.driver.find_elements_by_xpath(self.table_column_xpath))
    def SearchCustomerEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            customer_email = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if customer_email == email:
                flag = True
                break
        return flag
    def SearchBy_Name(self,name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            search_name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if search_name == name:
                flag = True
                break
        return flag








