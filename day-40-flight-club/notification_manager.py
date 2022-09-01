import smtplib
from twilio.rest import Client

TWILIO_SID = "AC14957ea0cfc019667658abdc517d08b7"
TWILIO_AUTH_TOKEN = "cd1a370058bcab82303be103373dc463"
TWILIO_VIRTUAL_NUMBER = "+18125779759"
TWILIO_VERIFIED_NUMBER = "+447581515606"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "shaytesting1@gmail.com"
MY_PASSWORD = "Bidemi11"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    @staticmethod
    def send_emails(emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
