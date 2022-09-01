import requests
import flight_data
import data_manager
from notification_manager import NotificationManager

SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
HEADERS = {
    "apikey": "27AfKrHnKVRLwEYMNkuEaeVyVaNH7p_T"
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = SEARCH_ENDPOINT
        self.headers = HEADERS

        self.flight_data = flight_data.FlightData()
        self.date_from = self.flight_data.tomorrow
        self.date_to = self.flight_data.sixty_days
        self.fly_from = self.flight_data.from_city

        self.data_manager = data_manager.DataManager()
        self.prices = data_manager.PRICES

    def search_flight(self):
        for price in self.prices:
            print(price)
            fly_to = price["iataCode"]
            city = price["city"]

            self.parameters = {
                "fly_from": self.fly_from,
                "fly_to": fly_to,
                "dateFrom": self.date_from,
                "dateTo": self.date_to
            }
            minimum = self.get_minimum()
            if minimum <= price["lowestPrice"]:
                NotificationManager(minimum, city, fly_to)

    def get_minimum(self):
        response = requests.get(SEARCH_ENDPOINT, params=self.parameters, headers=HEADERS)
        response.raise_for_status()
        data = response.json()["data"]
        price = [dat["price"] for dat in data]
        return min(price)
