from webdriver_set_up import WebdriverSetUp

driver = WebdriverSetUp().get_driver
driver.get("https://en.wikipedia.org/wiki/Main_Page")
stats = driver.find_element_by_css_selector("#articlecount a")
print(stats.text)