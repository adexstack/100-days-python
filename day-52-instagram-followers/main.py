from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

SIMILAR_ACCOUNT = "newbodyng"
USERNAME = "sayadex1"
PASSWORD = "bidemi11"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]").click()
        time.sleep(3)
        self.driver.find_element_by_name("username").send_keys(USERNAME)
        self.driver.find_element_by_name("password").send_keys(PASSWORD)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()

    def find_followers(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")\
            .send_keys(SIMILAR_ACCOUNT)
        time.sleep(5)
        self.driver.find_element_by_class_name("-qQT3").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(5)

        modal = self.driver.find_element_by_css_selector('.isgrP')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        print(len(all_buttons))
        #[button.click() for button in all_buttons if button.text == "Follow"]
        button_texts = [button.text for button in all_buttons]
        print(button_texts)
        # for button in all_buttons:
        #     if button.text == "Follow":
        #         button.click()
        #         time.sleep(2)


insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()