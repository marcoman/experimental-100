'''
This file contains examples.  I'll do some API calls here

'''

import os
import requests
import json



'''
https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
'''

MY_LAT = 39.952583
MY_LONG = -75.165222
MY_CITY = 'Philadelphia'
my_api_key = os.environ.get('OPENWEATHER_API_KEY')
my_weather_key = os.environ.get('WEATHER_API_KEY')

OPENWEATHER_API = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}'.format(lat=MY_LAT, lon=MY_LONG, APIkey=my_api_key)
OPENWEATHER_OPEN_API = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={APIkey}'.format(lat=MY_LAT, lon=MY_LONG, APIkey=my_api_key)
OPENWEATHER_WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}'.format(lat=MY_LAT, lon=MY_LONG, APIkey=my_api_key)
OPENWEATHER_CITY_API = 'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={APIkey}'.format(cityname=MY_CITY, APIkey=my_api_key)
WEATHER_API='http://api.weatherapi.com/v1/current.json?key={APIkey}&q={cityname}'.format(APIkey=my_weather_key, cityname=MY_CITY)
WEATHER_FUTURE_API='http://api.weatherapi.com/v1/future.json?key={APIkey}&q={cityname}&dt=2023-06-26'.format(APIkey=my_weather_key, cityname=MY_CITY)
WEATHER_FORECAST_API='http://api.weatherapi.com/v1/forecast.json?key={APIkey}&q={cityname}&days=3'.format(APIkey=my_weather_key, cityname=MY_CITY)

print(OPENWEATHER_API)

def get_current_weather()->json:
    response = requests.get(url=OPENWEATHER_API)
    quote =response.json()
    return quote

def get_city_weather()->json:
    response = requests.get(url=OPENWEATHER_CITY_API)
    quote =response.json()
    return quote

# This test needs a paid plan.
def get_open_weather()->json:
    response = requests.get(url=OPENWEATHER_OPEN_API)
    quote =response.json()
    return quote

def get_weather_api()->json :
    response = requests.get(url=WEATHER_API)
    quote =response.json()
    return quote

def get_future_weather()->json:
    response = requests.get(url=WEATHER_FUTURE_API)
    quote =response.json()
    return quote

def get_forecast_weather()->json:
    response = requests.get(url=WEATHER_FORECAST_API)
    quote =response.json()
    return quote

# get_current_weather()
# get_city_weather()
# get_open_weather()
# get_weather_api()
# get_future_weather()
forecast : json = get_forecast_weather()

for day in forecast['forecast']['forecastday']:
    if day['day']['daily_chance_of_rain'] > 50:
        print(f'Date: {day["date"]} has a high chance of rain at {day["day"]["daily_chance_of_rain"]}')

    for hour in day['hour']:
        pass
        # print (f"{hour['condition']['text']} at {hour['time']}")
        # print (f'Hour: {hour["time"]}' )
        # print (f'Temp: {hour["temp_f"]}' )
        # print (f'Condition: {hour["condition"]["text"]}' )
        # print (f'Wind: {hour["wind_mph"]}' )
        # print (f'Humidity: {hour["humidity"]}' )
        # print (f'Pressure: {hour["pressure_mb"]}' )
        # print (f'Clouds: {hour["cloud"]}' )
        # print (f'Feels Like: {hour["feelslike_f"]}' )
        # print (f'UV Index: {hour["uv"]}' )
        # print (f'Visibility: {hour["vis_km"]}' )
        # print (f'Wind Chill: {hour["windchill_f"]}' )
        # print (f'Dew Point: {hour["dewpoint_f"]}' )
        # print (f'Precipitation: {hour["precip_mm"]}' )

    rainy_hours = [hour for hour in day['hour'] if 'rain' in str(hour['condition']['text']).lower() ]

    for hour in rainy_hours:
        print(f"RAIN Date: {day['date']} at {hour['time']} has {hour['condition']['text']}")


