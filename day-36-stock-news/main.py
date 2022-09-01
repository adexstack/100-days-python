import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "GK6ZZQUKUELXY6UP"
FUNCTION = "TIME_SERIES_DAILY"
NEWS_API_KEY = "8a9989083c9e4a589dd4913938052e7f"

account_sid = "AC14957ea0cfc019667658abdc517d08b7"
auth_token = "cd1a370058bcab82303be103373dc463"
proxy_client = TwilioHttpClient()

parameters = {
    "function": FUNCTION,
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()

daily_record = response.json()["Time Series (Daily)"]
days = [day for day in daily_record]
daily_close = []
for day in days[:2]:
    close_price = daily_record[day]["4. close"]
    daily_close.append(close_price)

percent_change =""
if float(daily_close[0]) <= float(daily_close[1]) * 0.95:
    percent_change = "🔻5%"
elif float(daily_close[0]) >= float(daily_close[1]) * 1.05:
    percent_change = "🔺5%"
else:
    pass
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_params = {
    "q": "tesla",
    "from": daily_close[1],
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}
news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
news_response.raise_for_status()
articles = news_response.json()["articles"]
for article in articles[:3]:
    title = article["title"]
    description = article["description"]

    formatted_sms = f"{STOCK}: {percent_change}\nHeadline: {title}\nBrief: {description}"

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    #proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body=formatted_sms,
        from_="+18125779759",
        to="+447581515606"
    )
    print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

