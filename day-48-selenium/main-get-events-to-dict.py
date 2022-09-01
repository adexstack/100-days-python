from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_PRINT_FIRST_LINE'] = 'False'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.python.org/")
driver.find_element_by_id("events").click()

# My not too bad solution; Tutor's better though
events_list = driver.find_elements_by_xpath("//*[@id='content']/div/section/div/div/ul/li")
events_length = len(events_list)

dict = {}

for count in range(events_length):
    count += 1
    event = driver.find_element_by_xpath(f"//*[@id='content']/div/section/div/div/ul/li[{count}]/h3")
    date = driver.find_element_by_xpath(f"//*[@id='content']/div/section/div/div/ul/li[{count}]/p/time")
    dict.update({count:{"time":date.text, "name":event.text}})
print(dict)

# Tutor better solution
events_dict = {}
event_times = driver.find_elements_by_css_selector(".shrubbery time")
event_names = driver.find_elements_by_css_selector(".shrubbery li h3")

for n in range(len(event_times)):
    events_dict[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events_dict)







