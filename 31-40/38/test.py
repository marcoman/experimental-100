'''
This test harness is designed to exercise the Nutrionix API as part of a Day38 exercise.
'''

import os
import requests
import json
import datetime


NUTRITIONIX_APP_ID=os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY=os.environ.get('NUTRITIONIX_API_KEY')
GOOGLE_SHEET_ID=os.environ.get('GOOGLE_SHEET_ID')   
NUTRITIONIX_API_EXERCISE = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_API_FOOD = "https://trackapi.nutritionix.com/v2/natural/nutrients"

SHEETLY_API = 'https://api.sheety.co/{sheetid}/myWorkouts/workouts'.format(sheetid=GOOGLE_SHEET_ID)

my_request_body = {
    "gender": "male",
    "weight_kg": 86,
    "height_cm": 178,
    "age": 52
}

my_authentication_header = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

def get_user_input():
    '''
    Prompts the user for a food item and returns it.
    '''
    return input("Enter a food item: ")


def get_food_nutrients(food) -> requests.Response:
    '''
    Sends POST to the Nutritionix  API for the given food item and returns the response.
    '''
    response = requests.post(NUTRITIONIX_API_FOOD,
                             headers=my_authentication_header,
                             json={
                                 "query": food
                             })
    return response


def print_food_summary(response):
    '''
    Prints the food summary for the given response.
    '''
    print(f'Food: {response.json()["foods"][0]["food_name"]}')
    print(f'Calories: {response.json()["foods"][0]["nf_calories"]}')
    print(f'Protein: {response.json()["foods"][0]["nf_protein"]}')
    # print(f'Fat: {response.json()["foods"][0]["nf_total_fat"]}')
    # print(f'Sodium: {response.json()["foods"][0]["nf_sodium"]}')
    # print(f'Carbs: {response.json()["foods"][0]["nf_total_carbohydrate"]}')
    # print(f'Fiber: {response.json()["foods"][0]["nf_dietary_fiber"]}')
    # print(f'Sugar: {response.json()["foods"][0]["nf_sugars"]}')

# food_response = get_food_nutrients("kohlrabi")
# for food in food_response.json()["foods"]:
#     print(food["food_name"])
#     print(f'calories: {food["nf_calories"]}')
#     print(f'protein: {food["nf_protein"]}')

# print(get_food_nutrients("peas").text)
# print(get_food_nutrients("cheeseburger").text)
# print(get_food_nutrients("pizza").text)
# print(get_food_nutrients("pepperoni pizza").text)

def get_exercise_data(exercise) -> requests.Response:
    '''
    Send a POST to the Nutritionix API for exercise data.
    '''
    global my_request_body
    my_request_body["query"] = exercise
    
    response = requests.post(NUTRITIONIX_API_EXERCISE,
                             headers=my_authentication_header,
                             json=my_request_body
                             )
    return response

def print_exercise_summary(response:requests.Response):
    '''
    Prints the exercise summary for the given response.
    '''

    for exercise in response.json()["exercises"]:
        print(f'Exercise: {exercise["name"]}')
        print(f'Calories: {exercise["nf_calories"]}')
        print(f'Duration: {exercise["duration_min"]}')
        print(f'Intensity: {exercise["nf_calories"]}')

keep_running = True
while keep_running:
    food = input ("Enter a food item: ")
    if food == "quit":
        keep_running = False
        continue
    else:
        food_response = get_food_nutrients(food)
        print_food_summary(food_response)



keep_running = True
while keep_running:
    exercise = input ("Enter an exercise: ")
    if exercise == "quit":
        keep_running = False
        continue
    else:
        exercise_response = get_exercise_data(exercise)
        print_exercise_summary(exercise_response)

def sheetly_authentication_header():
    '''
    Returns the authentication header for the sheetly API.
    '''
    return {
        "Authorization": "Bearer {TOKEN}".format(TOKEN=os.environ.get('SHEETLY_TOKEN'))
    }

def get_sheet_exercises():
    '''
    Adds the given exercise to the Google Sheet.
    '''
    myrequest = requests.get(SHEETLY_API, headers=sheetly_authentication_header())
    print(myrequest.status_code)
    print(myrequest.text)
    return myrequest.json()

# get_sheet_exercises()

def add_sheet_exercise(exercise):
    '''
    Adds the given exercise to the Google Sheet.
    '''

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    ex = exercise["name"]
    dur = exercise["duration_min"]
    cal = exercise["nf_calories"]
    print(f'{today} {ex} {dur} {cal}')

    myrequest = requests.post(SHEETLY_API,
                            headers=sheetly_authentication_header(),
                            json={
                                "workout": {
                                    "date": today,
                                    "time": "12:00",
                                    "exercise": ex,
                                    "duration": dur,
                                    "calories": cal
                                }
                            }
                            )
    print(myrequest.status_code)

keep_running = True
while keep_running:
    exercise = input ("Add exercises to a sheet: ")
    if exercise == "quit":
        keep_running = False
        continue
    else:
        exercises = get_exercise_data(exercise)
        for exercise in exercises.json()["exercises"]:
            print(exercise)
            add_sheet_exercise(exercise)

