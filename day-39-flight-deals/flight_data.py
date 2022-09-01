import datetime

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
sixty_days = datetime.date.today() + datetime.timedelta(days=(30 * 6))

TOMORROW = tomorrow.strftime("%d/%m/%Y")
SIXTY_DAYS = sixty_days.strftime("%d/%m/%Y")
FROM_CITY = "LON"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.tomorrow = TOMORROW
        self.sixty_days = SIXTY_DAYS
        self.from_city = FROM_CITY
