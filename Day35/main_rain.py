import os

import requests
from twilio.rest import Client
ssid = "get ssid"
auto_token= "get token"
ph_no = "+14846635402"

api_link = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "Enter your api key"

LATITUDE = 15.017160
LONGITUDE = 75.933540

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(api_link, params=parameters)

weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
is_rain = False
for hour_data in weather_data:
    conditional_code = hour_data["weather"][0]["id"]
    if conditional_code < 700:
        is_rain = True

if is_rain:

    client = Client(ssid, auto_token)
    message = client.messages \
                    .create(
                         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                         from_=int(ph_no),
                         to=+916362435914,
                     )

    print(message.status)
