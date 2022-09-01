from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "AC14957ea0cfc019667658abdc517d08b7"
auth_token = "cd1a370058bcab82303be103373dc463"
proxy_client = TwilioHttpClient()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, minimum, city, to_iata):
        self.minimum = minimum
        self.city = city
        self.to_iata = to_iata
        client = Client(account_sid, auth_token, http_client=proxy_client)
        # f"Low price alert! Only £{41} to fly from {London}-{STN} to {Berlin}-{SXF}, from {2020 - 08-25} to {2020 -
        # 09-10}.
        self.formatted_sms = f"Low price alert! Only £{self.minimum} to fly from London=LON" \
                             f" to {self.city}-{self.to_iata} "
        message = client.messages.create(
            body=self.formatted_sms,
            from_="+18125779759",
            to="+447581515606"
        )
        print(message.status)
