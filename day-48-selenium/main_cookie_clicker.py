from webdriver_set_up import WebdriverSetUp
import datetime as dt

driver = WebdriverSetUp().get_driver
#Keys = WebdriverSetUp().get_keys
driver.get("https://orteil.dashnet.org/cookieclicker/")


a = dt.datetime.now()
b = a + dt.timedelta(seconds=20) # days, seconds, then other fields.
# print(a.now())
# print(a.time())
# print(b)
# print(b.time())

while dt.datetime.now() < b:
    driver.find_element_by_id("bigCookie").click()
