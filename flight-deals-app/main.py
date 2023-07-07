#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
import pprint
from data_manager import DataManager
from flight_search import FlightSearch
start_code = "LON"

data_manager = DataManager()
search = FlightSearch()
sheet_data = data_manager.get_sheet_data()

for row in range(len(sheet_data)):
    city = sheet_data[row]["city"]
    if sheet_data[row]["iataCode"] == '':
        code = search.get_iata_codes(city)
        sheet_data[row]["iataCode"] = code
        data_manager.update_row(sheet_data[row])
    to_code = sheet_data[row]["iataCode"]
    fare = search.get_fares(start_code=start_code, dest_code=to_code)


# print(sheet_data)