import requests

GET_RESPONSE = requests.get(f"https://api.sheety.co/7f1f7b517bd2c252296dbf3c821e2a15/flightDeals/prices")
PRICES = GET_RESPONSE.json()["prices"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.prices = PRICES
