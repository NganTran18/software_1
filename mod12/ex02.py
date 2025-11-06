import json
import requests

apikey = "APIKEY"

city = input("Enter municipality: ")

url = f"https://openweathermap.org/data.weather?q={city}&appid={apikey}."
response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    print(f'weather: {description}')
    print(f'temperature: {temperature}')

else:
    print('error')
