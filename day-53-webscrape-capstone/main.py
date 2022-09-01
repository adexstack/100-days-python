# My more optimised solution than the other 2. Note that you have to use your system User-Agent header version
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

GOOGLE_SHEET = "https://docs.google.com/forms/d/e/1FAIpQLSc99OlX626gdTMGMbB4Nh4Pb88Q9X--Ww3VW4qFlrI48HIayw/" \
               "viewform?usp=sf_link"
URL = "https://www.zillow.com/homes/"
resource = "for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%" \
      "3A%7B%22west%22%3A-122.64481581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22%3A37.65769536985581%2C%" \
      "22north%22%3A37.892700783966994%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B" \
      "%22price%22%3A%7B%22max%22%3A872627%2C%22min%22%3A1194019%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3" \
      "A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%2C%22min%22%3A2900%7D%2C%22auc%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22" \
      "value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22" \
      "isListVisible%22%3Atrue%7D"

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.114 Safari/537.36 "
}

response = requests.get(URL + resource, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

all_link_elements = soup.select(".list-card-top a")
all_links = []
for link in all_link_elements:
    href = link["href"]
    #print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.find_all(class_="list-card-price")
all_prices = [price.get_text().split("+")[0].replace("/mo", "") for price in all_price_elements if "$" in price.text]

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSc99OlX626gdTMGMbB4Nh4Pb88Q9X--Ww3VW4qFlrI48HIayw/viewform?usp=sf_link"

address_input_locator = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
price_input_locator = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
link_input_locator = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"
submit_button = "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span/span"
link_text = "Submit another response"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(GOOGLE_FORM)
time.sleep(3)
for count in range(len(all_links)):
    driver.find_element_by_xpath(address_input_locator).send_keys(all_addresses[count])
    driver.find_element_by_xpath(price_input_locator).send_keys(all_prices[count])
    driver.find_element_by_xpath(link_input_locator).send_keys(all_links[count])
    driver.find_element_by_xpath(submit_button).click()
    time.sleep(3)
    if count < (len(all_links) - 1):
        driver.find_element_by_link_text(link_text).click()










