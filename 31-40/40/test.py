'''
This test harness is designed to exercise the Nutrionix API as part of a Day38 exercise.
'''

import os
import requests
import json
import datetime


GOOGLE_SHEET_ID=os.environ.get('GOOGLE_SHEET_ID')   
SHEETY_API = 'https://api.sheety.co/{sheetid}/myWorkouts/users'.format(sheetid=GOOGLE_SHEET_ID)

keep_running = True

def sheety_authentication_header():
    '''
    Returns the authentication header for the sheetly API.
    '''
    return {
        "Authorization": "Bearer {TOKEN}".format(TOKEN=os.environ.get('SHEETY_TOKEN'))
    }

def get_sheet_users():
    '''
    Adds the given exercise to the Google Sheet.
    '''
    myrequest = requests.get(SHEETY_API, headers=sheety_authentication_header())
    print(myrequest.status_code)
    print(myrequest.text)
    return myrequest.json()

get_sheet_users()

def add_sheet_user(fname, lname, email):
    '''
    Adds the given exercise to the Google Sheet.
    '''

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f'{today} {fname} {lname} {email}')

    myrequest = requests.post(SHEETY_API,
                            headers=sheety_authentication_header(),
                            json={
                                "user": {
                                    "firstName": fname,
                                    "lastName": lname,
                                    "email": email,
                                }
                            }
                            )
    print(myrequest.status_code)

add_sheet_user('Marco', 'Morales', 'mail2mail')
add_sheet_user('XXXXX', 'Morales', 'marco@mail.com')
