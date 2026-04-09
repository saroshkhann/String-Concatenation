import requests
from twilio.rest import Client

endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "7c5b3c6b247db628480b95ca06407f13"

account_sid = "ACa74d13330e6049f0a711e900806a6ead"
auth_token = "646f93eaed8606fa5c46dcb07be88338"

parameters = {
    "lat":27.235901,
    "lon":94.104599,
    "appid":api_key,
    "cnt": 4
}
response = requests.get(endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+16066718501",
        to="+923110199723",
    )

    print(message.status)
