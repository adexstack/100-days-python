from webdriver_set_up import WebdriverSetUp

driver = WebdriverSetUp().get_driver
Keys = WebdriverSetUp().get_keys
driver.get("http://secure-retreat-92358.herokuapp.com/")

driver.find_element_by_name("fName").send_keys("Seyi")
driver.find_element_by_name("lName").send_keys("Adex")
driver.find_element_by_name("email").send_keys("sAdex@gmail.com")
#driver.find_element_by_tag_name("button").submit()
driver.find_element_by_tag_name("button").send_keys(Keys.ENTER)
