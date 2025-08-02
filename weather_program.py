import requests
from datetime import datetime

url = "https://api.openweathermap.org/data/2.5/weather"
lat = "" #Paste latitude of location within the quotation marks (Example: 51.455040)
lon = "" #Paste longitude of location within the quotation marks and include the minus at the start! (Example: -0.969090)
api_key = "" #Paste your api key within the quotation marks
units = "metric" #Standard unit of measurement in the UK

params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "units": units
}

response = requests.get(url, params=params)
data = response.json()

# Get specific weather details correctly
location = data.get("name")  # City name
countryc = data.get("sys", {}).get("country")  # Country code
ndatetime = datetime.now()
temps = data.get("main", {}).get("temp")  # Temperature
feel_like = data.get("main", {}).get("feels_like")  # Feels like
tempx = data.get("main", {}).get("temp_max")  # Max temperature
humid = data.get("main", {}).get("humidity")  # Humidity %
wind_speed = data.get("wind", {}).get("speed")  # Wind speed in m/s
clouds = data.get("clouds", {}).get("all")  # Cloud cover %

print("\n--- Weather Details ---")
print(f"Location: {location}, {countryc}")
print(f"Current Date and Time: {ndatetime.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Current Temperature: {temps} °C")
print(f"Feels Like: {feel_like} °C")
print(f"Max Temperature: {tempx} °C")
print(f"Humidity: {humid}%")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Cloud Cover: {clouds}%")
