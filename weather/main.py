import requests
import json
import tkinter as tk


window = tk.Tk()
window.title("Weather App")

location_label = tk.Label(window, text="Enter location:")
location_label.pack()

location_entry = tk.Entry(window)
location_entry.pack()

weather_label = tk.Label(window, text="")
weather_label.pack()

def get_weath():
    location = location_entry.get()
    api_key = "34432044f4f98329777d99404307c046"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)

    data = json.loads(response.text)
    # print(data)
    temperature = data['main']['temp']
    new_temp = round(temperature - 273.15, 2)
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    wind_speed = data["wind"]["speed"]

    weather_label.config(text=f"Temperature: {new_temp}\nHumidity: {humidity}\nWeather description: {weather_description}\nSpeed: {wind_speed}")


button = tk.Button(window, text="Get Weather", command=get_weath)
button.pack()

window.mainloop()
