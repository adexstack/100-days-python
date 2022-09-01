from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os

os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_PRINT_FIRST_LINE'] = 'False'


class WebdriverSetUp:
    def __init__(self):
        self.get_driver = webdriver.Chrome(ChromeDriverManager().install())
        self.get_keys = Keys

