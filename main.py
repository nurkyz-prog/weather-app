import requests

API_KEY = "1a74917a80e3ea62da59ae107f993ddc"   # your real API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")

# Create the request URL
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"🌦 Weather: {weather}")
    print(f"🌡 Temperature: {temperature}°C")
else:
    print("❌ Error: City not found or API problem.")
