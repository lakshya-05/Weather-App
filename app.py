# app.py
# The temperature is in Fahrenheit which is later converted to Celsius


# Colors used with their HEX code
#
# SKY - #63C5DA
# Studio - #7851A9
# LEMONADE - #FCBACB


import requests
from tkinter import *
from PIL import Image, ImageTk


def far_to_Cel(far):
    cel = (far - 32) / 1.8
    cel = int(cel)
    return cel


def weather_images(weather):
    match weather:
        case "Clear":
            img = Image.open("1 sun.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Clouds":
            img = Image.open("2 cloudy.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Rain":
            img = Image.open("3 heavy-rain.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Drizzle":
            img = Image.open("4  light rain.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Thunderstorm":
            img = Image.open("5 storm.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Snow":
            img = Image.open("6 snowflake.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Mist":
            img = Image.open("7 misty.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Fog":
            img = Image.open("8 fog.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Haze":
            img = Image.open("9 haze.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Smoke":
            img = Image.open("10 smoke.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Dust":
            img = Image.open("11 dust.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Sand":
            img = Image.open("12 sand.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Ash":
            img = Image.open("13 volcanic-ash.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Squall":
            img = Image.open("14 windstorm.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))
        case "Tornado":
            img = Image.open("15 tornado.png")
            img_size = img.resize((50, 50), Image.LANCZOS)
            img_n = ImageTk.PhotoImage(img_size)
            img_label = Label(root, image=img_n)
            img_label.image = img_n
            img_label.pack(pady=(5, 2))


def handle_weather():
    apikey = '80176a7a1679abae8cf6ccab1bf60653'
    city = city_ip.get()

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={apikey}")

    weather = weather_data.json()['weather'][0]['main']
    weather_des = weather_data.json()['weather'][0]['description']
    temp = far_to_Cel(weather_data.json()['main']['temp'])
    humidity = weather_data.json()['main']['humidity']
    City = city.upper()

    city_nm_line = "City : " + City
    weather_city = Label(root, text=city_nm_line, bg="#FCBACB", fg="black", width=15)
    weather_city.pack(pady=(15, 2))
    weather_city.config(font=('verdana', 11))

    weather_of_city = Label(root, text="Weather : " + weather, bg="#FCBACB", fg="black", width=17)
    weather_of_city.pack(pady=(5, 2))
    weather_of_city.config(font=('verdana', 11))

    weather_images(weather=weather)

    weather_des_of_city = Label(root, text="Description : " + weather_des, bg="#FCBACB", fg="black", width=24)
    weather_des_of_city.pack(pady=(5, 2))
    weather_des_of_city.config(font=('verdana', 11))

    temp_of_city = Label(root, text="Current temperature : " + str(temp) + "°C", bg="#FCBACB", fg="black", width=26)
    temp_of_city.pack(pady=(5, 2))
    temp_of_city.config(font=('verdana', 11))

    humidity_of_city = Label(root, text="Humidity : " + str(humidity), bg="#FCBACB", fg="black", width=15)
    humidity_of_city.pack(pady=(5, 20))
    humidity_of_city.config(font=('verdana', 11))


# Main Program

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
