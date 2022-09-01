import requests
from datetime import datetime

APP_ID = "4653c266"
API_KEY = "7717d92ec46479c66c68b2b59d7a6c71"
GOOGLE_ENDPOINT = "https://api.sheety.co/7f1f7b517bd2c252296dbf3c821e2a15/workoutTracking/workouts"
GOOGLE_USERNAME = "seyiadex"
GOOGLE_PASSWORD = "kjthdy61g"

query = input("Tell me which exercise you did: ")

headers = {
    "x-app-id":APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

data={
    "query":query
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=exercise_endpoint, json=data, headers=headers)
response.raise_for_status()
exercises = response.json()["exercises"]
for the_exercise in exercises:
    now = datetime.now()
    exercise = the_exercise["name"].title()
    duration = the_exercise["duration_min"]
    calories = the_exercise["nf_calories"]

    body = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    google_headers = {
        "Content-Type": "application/json"
    }

    google_post_response = requests.post(url=GOOGLE_ENDPOINT, json=body, auth=(GOOGLE_USERNAME, GOOGLE_PASSWORD))
    google_post_response.raise_for_status()
    print(google_post_response.json())

print(requests.get(GOOGLE_ENDPOINT).json())


