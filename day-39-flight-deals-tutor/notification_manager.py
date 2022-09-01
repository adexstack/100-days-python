from twilio.rest import Client

TWILIO_SID = "AC14957ea0cfc019667658abdc517d08b7"
TWILIO_AUTH_TOKEN = "cd1a370058bcab82303be103373dc463"
TWILIO_VIRTUAL_NUMBER = "+18125779759"
TWILIO_VERIFIED_NUMBER = "+447581515606"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
