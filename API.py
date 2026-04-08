import requests
from datetime import datetime

MY_LAT = 33.684422
MY_LNG = 73.047882
#
# response = requests.get(url ="http://api.open-notify.org/iss-now.json" )
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted": 0
}

response = requests.get(url = " https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(sunrise)

time_now = datetime.now()
print(time_now)