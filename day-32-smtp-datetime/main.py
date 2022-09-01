import smtplib
import datetime as dt

# my_email = "shaytesting1@gmail.com"
# password = "Bidemi11"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="saadedokun121@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email."
#                         )

now = dt.datetime.now()
print(now.year)
print(now.month)
print(now.weekday())

date_of_birth = dt.datetime(year=1995, month=4, day=2, hour=5)
print(date_of_birth)


