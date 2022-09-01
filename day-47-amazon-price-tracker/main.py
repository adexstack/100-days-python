# http://myhttpheader.com/ (check your headers ; needed for amazon site request)
# https://uk.camelcamelcamel.com/   (check amazon product price history)

import requests
from bs4 import BeautifulSoup
from email_notification_manager import EmailNotificationManager

URL = "https://www.amazon.com/"
BUY_PRICE = 140

resource = "Yedi-Programmable-Pressure-Steamer-Accessory/dp/B07P91ZR81/ref=pd_di_sccai_2/134-9935743-9322729?pd_rd_w" \
           "=QYHAd&pf_rd_p=c9443270-b914-4430-a90b-72e3e7e784e0&pf_rd_r=HDQAGJ4X9W0QXNG4N7QM&pd_rd_r=56b2ea28-af0d" \
           "-43f1-b001-ca4a233e81fe&pd_rd_wg=ueHwx&pd_rd_i=B07P91ZR81&psc=1 "

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.114 Safari/537.36 "
}

response = requests.get(URL + resource, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.content, "lxml")
price = soup.find(name="span", class_="a-size-base a-color-base")
price_text = price.get_text()
# price_float = float(price_text.replace("$", "")) # mine, tutor style below (Both works ok)
price_float = float(price_text.split("$")[1])

title_soup = soup.find(id="productTitle")
title = title_soup.getText().strip()

link_soup = soup.find(name="link", rel="canonical")
link = link_soup.get('href')

if price_float < BUY_PRICE:
    EmailNotificationManager(title, price_float, link)
