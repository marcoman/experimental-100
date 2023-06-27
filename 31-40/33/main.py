'''
In this test file, we experiment with some API actions.
'''

import json
import requests

# This returns text in this format:
# {"number": 10, "people": [{"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Stephen Bowen", "craft": "ISS"}, {"name": "Warren Hoburg", "craft": "ISS"}, {"name": "Sultan Alneyadi", "craft": "ISS"}, {"name": "Andrey Fedyaev", "craft": "ISS"}, {"name": "Jing Haiping", "craft": "Tiangong"}, {"name": "Gui Haichow", "craft": "Tiangong"}, {"name": "Zhu Yangzhu", "craft": "Tiangong"}], "message": "success"}

response = requests.get(url='http://api.open-notify.org/astros.json')
print (response)
print (response.status_code)    
print (response.text)
print (response.json()["number"])
print (response.json()["people"])
print (response.json()["message"])


# This returns text in this format:
# {'iss_position': {'longitude': '-53.3193', 'latitude': '-51.1656'}, 'timestamp': 1687559104, 'message': 'success'}
response = requests.get(url='http://api.open-notify.org/iss-now.json')
print (response)
print (response.status_code)    
print (response.json())

print (response.json()["iss_position"])
print (response.json()["iss_position"]["latitude"])
print (response.json()["iss_position"]["longitude"])
print (response.json()["timestamp"])
print (response.json()["message"])

print (response.encoding)
print (response.headers)
print (response.headers['content-type'])

print 
