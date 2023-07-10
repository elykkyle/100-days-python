from flight_data import FlightData


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def notify(self, flight_data: FlightData):
        print(f"Only {flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to "
              f"{flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date}"
              f" to {flight_data.return_date}")
