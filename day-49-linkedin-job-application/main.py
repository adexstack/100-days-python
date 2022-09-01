from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time

JOB_LINK = "https://www.linkedin.com/jobs/search/?currentJobId=2584164513&f_AL=true&geoId=101165590&keywords=python" \
           "%20sdet&location=United%20Kingdom "

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(JOB_LINK)

driver.find_element_by_class_name("nav__button-secondary").click()
driver.find_element_by_css_selector("#username").send_keys("saadedokun121@gmail.com")
driver.find_element_by_css_selector("#password").send_keys("Bidemi22")
driver.maximize_window()
driver.find_element_by_css_selector(".login__form_action_container").submit()
#ember299
time.sleep(10)

#driver.find_element_by_tag_name("svg").click()
driver.find_element_by_class_name("jobs-apply-button--top-card").click()
driver.find_element_by_id("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2584164513,9,phoneNumber~nationalNumber)").send_keys("07567728732")

scroll = driver.find_element_by_id("ember313")
scroll.location_once_scrolled_into_view.sendKeys(Keys.PAGE_DOWN)
#driver.execute_script("window.scrollTo(0,document.body.form.scrollHeight)")
time.sleep(3)
driver.find_element_by_class_name("artdeco-button__text").submit()

driver.quit()