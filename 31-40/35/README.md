# here are some things I did to setup this day

I navigated to this site to get a free openweather account:

https://home.openweathermap.org/users/sign_up

Also, use this URL to find your Longitude and Latitude

https://www.latlong.net/

I live near philadelphia, so I'll use that city:
39.952583, -75.165222

The URL above would look like this:

https://api.openweathermap.org/data/2.5/weather?lat=39.952583&lon=-75.165222&appid={API key}


Sample output:

```json
{'coord': {'lon': -75.1652, 'lat': 39.9526}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 298.55, 'feels_like': 298.97, 'temp_min': 296.36, 'temp_max': 300.4, 'pressure': 1010, 'humidity': 70}, 'visibility': 8047, 'wind': {'speed': 6.17, 'deg': 270}, 'clouds': {'all': 75}, 'dt': 1687973760, 'sys': {'type': 2, 'id': 2037403, 'country': 'US', 'sunrise': 1687944850, 'sunset': 1687998802}, 'timezone': -14400, 'id': 4560349, 'name': 'Philadelphia', 'cod': 200}
```

# weatherapi

NOTE: The openweathermap API is no longer free for the exercise.  I have this alternative based on the course notes to use https://www.weatherapi.com/ instead


```json
{'location': {'name': 'Philadelphia', 'region': 'Pennsylvania', 'country': 'United States of America', 'lat': 39.95, 'lon': -75.16, 'tz_id': 'America/New_York', 'localtime_epoch': 1687982675, 'localtime': '2023-06-28 16:04'}, 'current': {'last_updated_epoch': 1687982400, 'last_updated': '2023-06-28 16:00', 'temp_c': 26.1, 'temp_f': 79.0, 'is_day': 1, 'condition': {'text': 'Mist', 'icon': '//cdn.weatherapi.com/weather/64x64/day/143.png', 'code': 1030}, 'wind_mph': 11.9, 'wind_kph': 19.1, 'wind_degree': 280, 'wind_dir': 'W', 'pressure_mb': 1011.0, 'pressure_in': 29.85, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 60, 'cloud': 100, 'feelslike_c': 27.7, 'feelslike_f': 81.8, 'vis_km': 9.7, 'vis_miles': 6.0, 'uv': 6.0, 'gust_mph': 10.1, 'gust_kph': 16.2}}
```

The data from https://www.weatherapi.com/docs/ looks like the following:


```json
{
   "date":"2023-06-30",
   "date_epoch":1688083200,
   "day":{
      "maxtemp_c":31.5,
      "maxtemp_f":88.7,
      "mintemp_c":18.6,
      "mintemp_f":65.5,
      "avgtemp_c":24.3,
      "avgtemp_f":75.7,
      "maxwind_mph":11.6,
      "maxwind_kph":18.7,
      "totalprecip_mm":3.5,
      "totalprecip_in":0.14,
      "totalsnow_cm":0.0,
      "avgvis_km":9.8,
      "avgvis_miles":6.0,
      "avghumidity":69.0,
      "daily_will_it_rain":1,
      "daily_chance_of_rain":74,
      "daily_will_it_snow":0,
      "daily_chance_of_snow":0,
      "condition":{
         "text":"Patchy rain possible",
         "icon":"//cdn.weatherapi.com/weather/64x64/day/176.png",
         "code":1063
      },
      "uv":5.0
   },
   "astro":{
      "sunrise":"05:35 AM",
      "sunset":"08:33 PM",
      "moonrise":"05:59 PM",
      "moonset":"02:42 AM",
      "moon_phase":"Waxing Gibbous",
      "moon_illumination":"84",
      "is_moon_up":1,
      "is_sun_up":1
   },
   "hour":[
      {
         "time_epoch":1688097600,
         "time":"2023-06-30 00:00",
         "temp_c":20.8,
         "temp_f":69.4,
         "is_day":0,
         "condition":{
            "text":"Clear",
            "icon":"//cdn.weatherapi.com/weather/64x64/night/113.png",
            "code":1000
         },
         "wind_mph":4.7,
         "wind_kph":7.6,
         "wind_degree":203,
         "wind_dir":"SSW",
         "pressure_mb":1017.0,
         "pressure_in":30.04,
         "precip_mm":0.0,
         "precip_in":0.0,
         "humidity":70,
         "cloud":8,
         "feelslike_c":20.8,
         "feelslike_f":69.4,
         "windchill_c":20.8,
         "windchill_f":69.4,
         "heatindex_c":20.8,
         "heatindex_f":69.4,
         "dewpoint_c":15.2,
         "dewpoint_f":59.4,
         "will_it_rain":0,
         "chance_of_rain":0,
         "will_it_snow":0,
         "chance_of_snow":0,
         "vis_km":10.0,
         "vis_miles":6.0,
         "gust_mph":8.9,
         "gust_kph":14.4,
         "uv":1.0
      },
   ]
}
```