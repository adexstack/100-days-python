# https://selenium-python.readthedocs.io/waits.html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

PROMISED_DOWN = 51.2
PROMISED_UP = 15.6


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        self.driver.find_element_by_id("_evidon-banner-acceptbutton").click()
        self.driver.find_element_by_link_text("GO").click()
        time.sleep(60)
        # WebDriverWait(self.driver, 60).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "result-label"))
        # )
        print("located")

        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/SeyiAdedokun1")
        self.driver.find_element_by_link_text("Log in").click()
        time.sleep(5)
        self.driver.find_element_by_name("session[username_or_email]").send_keys("SeyiAdedokun1")
        self.driver.find_element_by_name("session[password]").send_keys("Bidemi11")
        self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span").click()
        time.sleep(10)

        self.driver.find_element_by_xpath("//*[@aria-label='Tweet']").click()
        time.sleep(5)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        self.driver.find_element_by_xpath("//*[@aria-label='Tweet text']").send_keys(tweet)
        self.driver.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span").click()
        time.sleep(5)

        self.driver.quit()