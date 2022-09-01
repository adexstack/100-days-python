import smtplib

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "shaytesting1@gmail.com"
MY_PASSWORD = "Bidemi11"
RECEIVER_EMAIL = "saadedokun121@gmail.com"


class EmailNotificationManager:
    def __init__(self, title, price, link):
        self.title = title
        self.price = price
        self.link = link
        self.send_emails()

    def send_emails(self):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=RECEIVER_EMAIL,
                    msg=f"Subject:New Low Price Alert!\n\n{self.title} is now ${self.price}\nGet it here now: {self.link}".encode('utf-8')
                )