from pprint import pprint
import requests
import os

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_API") + "/myWorkouts/flights"
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")


class DataManager:

    def __init__(self):
        self.destination_data = {}


    def sheety_authentication_header(self):
        '''
        Returns the authentication header for the sheetly API.
        '''
        return {
            "Authorization": "Bearer {TOKEN}".format(TOKEN=SHEETY_TOKEN)
    }

    
    def get_destination_data(self):
        # print(f'URL: {SHEETY_PRICES_ENDPOINT}')
        # print(f'Token: {SHEETY_TOKEN}')
        headers = self.sheety_authentication_header()
        # print(headers)
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,
                                headers=headers,
                                )
        self.data = response.json()["flights"]
        # pprint(self.data)
        # self.destination_data = data["lowestPrice"]
        return self.data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
