#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import pprint
import flight_data
import flight_search
import notification_manager
import data_manager
import datetime

my_flight_data = flight_data.FlightData()
my_flight_search = flight_search.FlightSearch()

sheet_data = my_flight_data.get_rows()
# pprint.pprint(flight_data)

# Iterate over each row to get flight data.
date_start = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%d/%m/%Y")
date_end = (datetime.datetime.now() + datetime.timedelta(days=14)).strftime("%d/%m/%Y")

for flight in sheet_data["flights"]:
    # pprint.pprint(flight)
    flight_prices = my_flight_search.get_flight_data(flight["from"], flight["to"], date_start, date_end)
    # pprint.pprint(flight_prices)
    for data in flight_prices["data"]:
        # if data["price"] < flight["lowestPrice"]:
        #     my_flight_data.update_row(data["id"], data["price"])
        #     my_flight_data.sheet_report()
        #     notification_manager.send_email(data["price"], data["cityFrom"], data["cityTo"], data["flyFrom"], data["flyTo"])
        print (f'flight id: {data["cityCodeFrom"]} to {data["cityCodeTo"]} price: {data["price"]}')
        for route in data["route"]:
            airline = my_flight_search.get_airline_from_code(route["airline"])
            # print (f'\tAirline: {airline}')

            if data["price"] < flight["lowestPrice"]:
                print (f'\tLOWER PRICE on {airline} fight {route["flight_no"]} at {route["local_departure"]}')


# # my_flight_data.print_rows()
# my_flight_data.sheet_report()