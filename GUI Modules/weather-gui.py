
# ----------------- MANS GUI Weather Test with Input Method ----------------- #

import tkinter as tk
import requests
import json

def get_weather():
    location = entry.get()
    api_key = ""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&lang=tr&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)

    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    wind = data['wind']['speed']
    sea_level = data['main']['pressure']  
    rain = data['weather'][0]['main']  

    weather_window = tk.Toplevel(root)
    weather_window.title("Hava Durumu Bilgisi")

    temperature_label = tk.Label(weather_window, text=f"Sıcaklık: {temperature}°C")
    temperature_label.pack()

    humidity_label = tk.Label(weather_window, text=f"Nem: {humidity}%")
    humidity_label.pack()

    description_label = tk.Label(weather_window, text=f"Açıklama: {description}")
    description_label.pack()

    wind_label = tk.Label(weather_window, text=f"Rüzgar Hızı: {wind} m/s")
    wind_label.pack()

    sea_label = tk.Label(weather_window, text=f"Deniz Seviyesi: {sea_level} hPa")
    sea_label.pack()

root = tk.Tk()
root.title("MANS Weather GUI")

label = tk.Label(root, text="Lokasyon:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="get_weather", command=get_weather)
button.pack()

root.mainloop()
