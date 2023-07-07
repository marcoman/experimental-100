import requests
import os

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.API_ENDPOINT = os.environ.get("SHEETLY_API") + "/myFlights/flights"
        self.HEADERS = self.sheetly_authentication_header()

    def sheetly_authentication_header(self):
        '''
        Returns the authentication header for the sheetly API.
        '''
        return {
            "Authorization": "Bearer {TOKEN}".format(TOKEN=os.environ.get('SHEETLY_TOKEN'))
        }

    def sheet_report(self):
        cities = self.get_rows()
        for city in cities:
            from_city = city["from"]
            to_city = city["to"]
            flight_data = self.get_flight_data(from_city, to_city)
            print(flight_data)

    def get_rows(self):
        response = requests.get(url=self.API_ENDPOINT, headers=self.HEADERS)
        response.raise_for_status()
        return response.json()
    

    def print_rows(self):
        for flight in self.get_rows()["flights"]:
            print(f'Flight from {flight["from"]} to {flight["to"]}) ({flight["dest"]})')


