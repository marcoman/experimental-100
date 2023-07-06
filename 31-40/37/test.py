'''
In this example, we'll run some tests to do HTTP posts
'''

import requests
import os
import datetime as dt

PIXELA_TOKEN = os.environ.get('PIXELA_TOKEN')
PIXELA_USERNAME = os.environ.get('PIXELA_USERNAME')
PIXELA_USER_API = 'https://pixe.la/v1/users'
PIXELA_GRAPHS_API = 'https://pixe.la/v1/users/{username}/graphs'.format(username=PIXELA_USERNAME)

user_params = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
    }


print (user_params)

# myrequest = requests.post(url=PIXELA_USER_API, json=user_params)
# print (myrequest.text)
# print (myrequest.status_code)

graph_params = {
    'id': 'code-graph-1',
    'name': 'Coding Graph',
    'unit': 'commit',
    'type': 'int',
    'color': 'ajisai'
}

graph_headers = {
    'X-USER-TOKEN': PIXELA_TOKEN
    }



# myrequest = requests.post(url=PIXELA_GRAPHS_API, json=graph_params, headers=graph_headers)
# print (myrequest.text)
# print (myrequest.status_code)
# print (myrequest.text)

today = str (dt.datetime.now().strftime('%Y%m%d'))

graph_update = {
    'date': today,
    'quantity': '10'
}

myrequest = requests.post(url=PIXELA_GRAPHS_API + '/code-graph-1', json=graph_update, headers=graph_headers)
print (myrequest.text)
print (myrequest.status_code)
