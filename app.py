# app.py
# The temperature is in Fahrenheit


# Colors used with their HEX code
#
# SKY - #63C5DA
# Studio - #7851A9
# LEMONADE - #FCBACB


import requests
from tkinter import messagebox
from tkinter import *

apikey = '80176a7a1679abae8cf6ccab1bf60653'


def handle_weather():
    city = city_ip.get()
    messagebox.showinfo("Message", f"Weather Details of {city} has been added to the dashboard")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={apikey}")

    weather = weather_data.json()['weather'][0]['main']
    weather_des = weather_data.json()['weather'][0]['description']
    temp = weather_data.json()['main']['temp']
    humidity = weather_data.json()['main']['humidity']
    City = city.upper()

    city_nm_line = "City : " + City
    weather_city = Label(root, text=city_nm_line, bg="#FCBACB", fg="black", width=15)
    weather_city.pack(pady=(15, 2))
    weather_city.config(font=('verdana', 11))

    weather_of_city = Label(root, text="Weather : " + weather, bg="#FCBACB", fg="black", width=17)
    weather_of_city.pack(pady=(5, 2))
    weather_of_city.config(font=('verdana', 11))

    weather_des_of_city = Label(root, text="Description : " + weather_des, bg="#FCBACB", fg="black", width=20)
    weather_des_of_city.pack(pady=(5, 2))
    weather_des_of_city.config(font=('verdana', 11))

    temp_of_city = Label(root, text="Current temperature : " + str(temp) + "°F", bg="#FCBACB", fg="black", width=26)
    temp_of_city.pack(pady=(5, 2))
    temp_of_city.config(font=('verdana', 11))

    humidity_of_city = Label(root, text="Humidity : " + str(humidity), bg="#FCBACB", fg="black", width=15)
    humidity_of_city.pack(pady=(5, 20))
    humidity_of_city.config(font=('verdana', 11))


# city = input("Enter city : ")

# weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={apikey}")
#
# weather = weather_data.json()['weather'][0]['main']
# weather_des = weather_data.json()['weather'][0]['description']
# temp = weather_data.json()['main']['temp']
# humidity = weather_data.json()['main']['humidity']
# City = city.upper()


# print(f"The weather of {City} is {weather}, description - {weather_des}.")
# print(f"Current Temperature - {temp}°F")
# print(f"Humidity - {humidity}")


root = Tk()
root.title('Weather.apk')
root.geometry("900x500")
root.configure(background="#FAE29C")

wel_txt = Label(root, text="Weather Application", fg="black", bg="#63C5DA", width=250)
wel_txt.pack(pady=(10, 5))
wel_txt.config(font=('verdana', 20))

city_nm = Label(root, text="Enter City Name", fg="white", bg="#7851A9", width=15)
city_nm.pack(pady=(25, 5))
city_nm.config(font=('verdana', 16))

city_ip = Entry(root, width=40)
city_ip.pack(pady=(1, 1), ipady=5)

city_btn = Button(root, text="Get Details", fg="white", bg="#7851A9", width=15, command=handle_weather)
city_btn.pack(pady=(5, 10))
city_btn.config(font=('verdana', 11))


root.mainloop()
