# app.py
# The temperature is in Fahrenheit

import requests
apikey = '80176a7a1679abae8cf6ccab1bf60653'
city = input("Enter city : ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={apikey}")

if weather_data.json().['cod'] == 200:
    weather = weather_data.json()['weather'][0]['main']
    weather_des = weather_data.json()['weather'][0]['description']
    temp = weather_data.json()['main']['temp']
    humidity = weather_data.json()['main']['humidity']
    City = city.upper()

    print(f"The weather of {City} is {weather}, description - {weather_des}.")
    print(f"Current Temperature - {temp}°F")
    print(f"Humidity - {humidity}")
else:
    print("Not a valid city.")
