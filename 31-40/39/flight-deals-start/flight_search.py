import requests
import os
import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    ARLINES = {
        "AA" : "American Airlines",
        "AC" : "Air Canada",
        "AS" : "Alaska Airlines",
        "BA" : "British Airways",
        "DL" : "Delta",
        "F9" : "Frontier Airlines",
        "HA" : "Hawaiian Airlines",
        "LH" : "Lufthansa",
        "MQ" : "Emirates",
        "NK" : "Norwegian Airlines",
        "OO" : "Southwest Airlines",
        "TK" : "Turkish Airlines",
        "VX" : "Virgin America",
        "VY" : "Virgin Australia",
        "ZH" : "China Airlines",
        "Z0" : "China Southern Airlines",
    }

    def __init__(self):
        self.API_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
        self.HEADERS = self.tequila_authentication_header()

    def tequila_authentication_header(self):
        '''
        Returns the authentication header for the sheetly API.
        '''
        return {
            "apiKey": "{TOKEN}".format(TOKEN=os.environ.get('TEQUILA_API_KEY'))
        }

    def get_flight_data(self, from_city, to_city, date_from, date_to):
        '''
        Returns flight data for a given city.
        '''

        parameters = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 10,
            "limit": "3",
            "curr": "USD",
            "max_stopovers": 1,
            
        }
        # pprint.pprint(parameters)
        response = requests.get(url=self.API_ENDPOINT, params=parameters, headers={"apikey": os.environ.get("TEQUILA_API_KEY")})
        response.raise_for_status()
        # pprint.pprint(response.json())

        return response.json()
        # return {
        #     "from": from_city,
        #     "to": to_city,
        #     "date": date_from,
        #     "returnDate": date_to,
        #     "price": 0
        # }

    def get_airline_from_code (self, code):
        try:
            airline_name = self.ARLINES[code]
        except KeyError:
            airline_name = f'{code}-unk'
        return airline_name
    