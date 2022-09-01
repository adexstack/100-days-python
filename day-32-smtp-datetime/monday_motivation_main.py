import datetime as dt
from random import choice
import smtplib

current_day_of_the_week = dt.datetime.now().weekday()

my_email = "shaytesting1@gmail.com"
password = "Bidemi11"

if current_day_of_the_week == 2:
    with open("quotes.txt", 'r') as quotes:
        quotes_list = quotes.readlines()
        random_quote = choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="saadedokun121@gmail.com",
                            msg=f"Subject:Quote\n\n{random_quote}"
                            )
