import smtplib

import requests
from datetime import datetime

import stmp as stmp
MY_EMAIL = "YOUR EMAIL-ID"
MY_PASSWORD = "ENTER PASSWORD"
MY_LAT = 15.230660
MY_LONG =76.357707

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT + 5 and MY_LONG-5 <= iss_longitude <= MY_LONG + 5:
        return  True

def is_night():
    parametrs = {

        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted" : 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parametrs)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now().hour
    if time_now >= sunset and time_now<= sunrise:
        return  True


while True:
    if is_overhead() and is_night():
        connection = stmp.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look UP\n\n The ISS is above int the sky."
        )