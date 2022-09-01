##################### Extra Hard Starting Project ######################
import pandas as pd
from random import choice
import datetime as dt
import smtplib

MY_EMAIL = "shaytesting1@gmail.com"
PASSWORD = "Bidemi11"

# 1. Update the birthdays.csv
birthday_pd = pd.read_csv("birthdays.csv")
birthday_dict = birthday_pd.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
todays_date = dt.datetime.now()
today = (todays_date.month, todays_date.day)


for data in birthday_dict:
    if today == (data["month"], data["day"]):
        celebrant = data["name"]
        celebrant_email = data["email"]
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        if len(celebrant) != 0:
            letter_list = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
            letter_list_choice = choice(letter_list)
            with open(letter_list_choice) as letter:
                original_letter = letter.read()
                letter_message = original_letter.replace("[NAME]", celebrant)
                # 4. Send the letter generated in step 3 to that person's email address.
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=celebrant_email,
                                        msg=f"Subject:Happy Birthday {celebrant}\n\n{letter_message}"
                                        )