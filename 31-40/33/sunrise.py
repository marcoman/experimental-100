import requests
import json
import datetime

SUNRISE_API_URL = "https://api.sunrise-sunset.org/json"
ISS_API_URL = "http://api.open-notify.org/iss-now.json"

iss_response = requests.get(url=ISS_API_URL)
print (iss_response)
print (iss_response.json())

iss_long = iss_response.json()['iss_position']['longitude']
iss_lat = iss_response.json()['iss_position']['latitude']   

myparams = {
    "lat": iss_lat,
    "lng": iss_long,
    'formatted' : 0,
}

sunrise_response = requests.get(SUNRISE_API_URL, params=myparams)
print (sunrise_response.status_code)
print (sunrise_response.text)   

sr_sunrise = datetime.datetime.strptime(sunrise_response.json()['results']['sunrise'], '%Y-%m-%dT%H:%M:%S%z')
sr_sunset = datetime.datetime.strptime(sunrise_response.json()['results']['sunset'], '%Y-%m-%dT%H:%M:%S%z')
sr_now = datetime.datetime.now().strftime("%H:%M:%S")

print (f'The sunrise is at {sr_sunrise.strftime("%H:%M:%S")} and the sunset is at {sr_sunset.strftime("%H:%M:%S")} and right now it is {sr_now}') 

if sr_now > sr_sunrise.strftime("%H:%M:%S") and sr_now < sr_sunset.strftime("%H:%M:%S"):
    print ("It's daytime!")
else:
    print ("It's nighttime!")
