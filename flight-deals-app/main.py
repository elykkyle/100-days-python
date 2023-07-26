#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
start_code = "LON"

data_manager = DataManager()
search = FlightSearch()
sheet_data = data_manager.get_sheet_data()
notification_manager = NotificationManager()

for row in range(len(sheet_data)):
    city = sheet_data[row]["city"]
    if sheet_data[row]["iataCode"] == '':
        code = search.get_iata_codes(city)
        sheet_data[row]["iataCode"] = code
        data_manager.update_row(sheet_data[row])
    to_code = sheet_data[row]["iataCode"]
    fare = search.get_fares(start_code=start_code, dest_code=to_code)
    try:
        if fare.price < sheet_data[row]["lowestPrice"]:
            sheet_data[row]["lowestPrice"] = fare.price
            data_manager.update_row(sheet_data[row])
            notification_manager.notify(fare)
    except AttributeError:
        continue

# print(sheet_data)