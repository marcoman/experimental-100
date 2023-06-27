import requests
from datetime import datetime
import math
from time import sleep


MY_LAT = 39.975430 # Your latitude
MY_LONG = -75.309868 # Your longitude


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

def check_sky():
    lookup = False
    if (math.fabs(MY_LAT - iss_latitude) < 5) and (math.fabs(MY_LONG - iss_longitude) < 5):
        print("ISS is close to me")

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()

        #If the ISS is close to my current position
        # and it is currently dark
        # Then send me an email to tell me to look up.
        # BONUS: run the code every 60 seconds.

        print (f'Time now is {datetime.utcnow()}')
        time_now = int (datetime.utcnow().strftime("%H"))

        print (f'sunrise is {sunrise}, sunset is {sunset}, time now is {time_now}')
        if (sunrise < time_now) and (time_now < sunset):
            print("It's daytime")
        else:
            print("It's nighttime")
            print("Look up")
            lookup = True

    else:
        print("ISS is far away")

    return lookup

def send_email():
    print("Sending email")
    # Here, we would use the regular SMTP calls to send an email letting usknow we need to look up.
    # for the purpose of this exercise, I won't send the email since I have that covered in other files.
    # I would just print the message to the console.


check_sky()

# To run this every 60 seconds, I would loop as following (set the variable to True)

keep_running = True
while keep_running:
    if check_sky():
        send_email()
        keep_running = False
    sleep(60)

