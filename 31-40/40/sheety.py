'''
This is the example from the instructor
'''

import requests
import os

# In this section, we get our env. variaables
SHEETLY_TOKEN = os.getenv("SHEETLY_TOKEN")
# SHEETLY_API = os.getenv("SHEETLY_API")
GOOGLE_SHEET_ID=os.environ.get('GOOGLE_SHEET_ID')   

SHEETLY_API = 'https://api.sheety.co/{sheetid}/myWorkouts/users'.format(sheetid=GOOGLE_SHEET_ID)



PROJECT = "myWorkouts"
SHEET = "users"

def sheetly_authentication_header():
    '''
    Returns the authentication header for the sheetly API.
    '''
    return {
        "Authorization": "Bearer {TOKEN}".format(TOKEN=os.environ.get('SHEETLY_TOKEN'))
    }

def post_new_row(fname, lname, email):
    global SHEETLY_API

    SHEETLY_API = 'https://api.sheety.co/{sheetid}/myWorkouts/users'.format(sheetid=GOOGLE_SHEET_ID)

    response = requests.post(SHEETLY_API,
                            headers=sheetly_authentication_header(),
                            json={
                                "user": {
                                    "firstName": fname,
                                    "lastName": lname,
                                    "email": email,
                                }
                            }
                            )
    response.raise_for_status()
    print(response.text)
