# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import smtplib
import os

# import os and use it to get the Github repository secrets
import requests
import smtplib

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

EMAIL_TO_SEND = os.environ.get("EMAIL_TO_SEND")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": 54.518890,
    "lon": 18.530540,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

item_in_list = 0
id_for_rain = weather_data["list"][item_in_list]["weather"][0]["id"]

list_of_ids = []
for _ in range(0, 4):
    item_in_list += 1
    list_of_ids.append(id_for_rain)

print(list_of_ids)

if any(item < 700 for item in list_of_ids):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=EMAIL_TO_SEND,
            msg=f"Subject:Take an umbrella!\n\nIt's going to rain today. Remember to bring an umbrella!"
        )


