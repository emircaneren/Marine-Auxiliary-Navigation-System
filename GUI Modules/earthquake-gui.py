#Description: This module shows the latest earthquake information on the screen.
#Feature planned to be added: As soon as an earthquake occurs, MANS will detect it and send a warning to the vessel and the seaman(user).
#Note: This module is not finished yet. It will be updated soon
#Author: Emircan Eren MANS's Dev. 

import requests
import tkinter as tk

def get_ip_address():
    response = requests.get('https://api64.ipify.org?format=json')
    if response.status_code == 200:
        ip_address = response.json()['ip']
        return ip_address
    else:
        return None

def get_location_info(ip_address):
    api_url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            lat = data['lat']
            lon = data['lon']
            return lat, lon
        else:
            return None, None
    else:
        return None, None

def get_nearest_earthquake(lat, lon):
    earthquake_api_url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&latitude={lat}&longitude={lon}&maxradiuskm=100"
    response = requests.get(earthquake_api_url)
    if response.status_code == 200:
        data = response.json()
        if data['features']:
            nearest_earthquake = data['features'][0]['properties']
            return nearest_earthquake
        else:
            return None
    else:
        return None

def show_earthquake_info():
    ip_address = get_ip_address()
    if ip_address:
        ip_label.config(text=f"[MANS]", bg="black", fg="#2a5b7f", font=("Arial", 36, "bold")) # lovelym me, before push dont forget to change name ip label to mans label
        latitude, longitude = get_location_info(ip_address)
        if latitude is not None and longitude is not None:
            location_label.config(text=f"Latitude: {latitude}\nLongitude: {longitude}", bg="black", fg="#2a5b7f", font=("Arial", 10, "bold"))
            nearest_earthquake_info = get_nearest_earthquake(latitude, longitude)
            if nearest_earthquake_info:
                place_label.config(text=f"Konum (Yaklaşık /100km): {nearest_earthquake_info['place']}", bg="#2a5b7f", fg="white", font=("Arial", 12, "bold"))
                magnitude_label.config(text=f"Şiddet: {nearest_earthquake_info['mag']}", bg="black", fg="#2a5b7f", font=("Arial", 12, "bold"))
            else:
                place_label.config(text="Yakında deprem bulunamadı.", bg="black", fg="#2a5b7f", font=("Arial", 12, "bold"))
                magnitude_label.config(text="")
                time_label.config(text="")
        else:
            location_label.config(text="Konum verisi alınamadı.", bg="black", fg="#2a5b7f", font=("Arial", 12, "bold"))
            place_label.config(text="")
            magnitude_label.config(text="")
            time_label.config(text="")
    else:
        ip_label.config(text="IP adresi alınamadı.", bg="black", fg="#2a5b7f", font=("Arial", 12, "bold"))
        location_label.config(text="")
        place_label.config(text="")
        magnitude_label.config(text="")
        time_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Son Depremler")
    root.config(bg="black")

    ip_label = tk.Label(root)
    ip_label.pack()

    location_label = tk.Label(root)
    location_label.pack()

    place_label = tk.Label(root)
    place_label.pack()

    magnitude_label = tk.Label(root)
    magnitude_label.pack()

    time_label = tk.Label(root)
    time_label.pack()

    show_earthquake_info() 

    root.mainloop()
