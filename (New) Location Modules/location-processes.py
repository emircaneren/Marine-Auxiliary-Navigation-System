from geopy.geocoders import Nominatim
import requests

def getLocationData():
        with open('location-data.txt', 'r') as data:
            for line in data:
                if 'Latitude' in line and 'Longitude' in line:
                    location.latitude, location.longitude = int(line.split(':')[1].strip())

location = getLocationData()
locationConvert = str(location) 

def setLocationData():
    ip = requests.get('https://api.ipify.org').text
    user_agent = "---"
    geocoder = Nominatim(user_agent=user_agent)
    location = geocoder.geocode(ip)
    

    with open('location-data.txt', 'w') as data:
        data.write(f"Latitude: {location.latitude}\n")
        data.write(f"Longitude: {location.longitude}\n")

for i in range(1):
     setLocationData()

def showLocation():
    print(location.latitude)
    print(location.longitude)

