import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()



APP_ID=os.environ.get("APP_ID")
API_KEY=os.environ.get("API_KEY")
APP_URL="https://trackapi.nutritionix.com/v2/natural/exercise"


SPREADSHEET_URL="https://api.sheety.co/3b834d45bf1e229572f35417d941de52/myWorkouts/workouts"  #https://docs.google.com/spreadsheets/d/1F-PkBrhwkgrYEEJZOOBhO6q-qfALpct9DmJzBBqulME/edit?gid=0#gid=0


header={
    'x-app-id':APP_ID,
    'x-app-key':API_KEY,
    'x-remote-user-id':"lingesh"
}

app_parameter={
    "query":input("What excersise you did today?\n"),
    "weight_kg":96,
    "gender":"Male",
    "height_cm":190,
    "age":18,
}

today=datetime.now()
date=today.strftime("%d/%m/%Y")
time=today.strftime("%H:%M:%S")


app_response=requests.post(url=APP_URL,json=app_parameter,headers=header)
result=app_response.json()

AUTH_TOKEN=os.environ.get("AUTH_TOKEN")
bearer_headers = {
    "Authorization":f"{AUTH_TOKEN}"
}

for i in result['exercises']:
    ss_parameter={
        'workout':{
        'date':date,
        'time':time,
        'exercise':i['name'].title(),
        'duration':int(i['duration_min']),
        'calories':i['nf_calories'],
         }
    }
    ss_response=requests.post(url=SPREADSHEET_URL,json=ss_parameter,headers=bearer_headers)
print(ss_response.text)
# print(ss_response.json())



