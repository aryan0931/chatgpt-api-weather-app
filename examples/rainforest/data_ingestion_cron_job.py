import requests
from dotenv import load_dotenv
import os

def send_weather_request(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": location,
        "appid": api_key
        # Add any other parameters specific to the OpenWeatherMap API
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None  # Handle error cases as needed

# Load environment variables
load_dotenv()
weather_api_key = os.environ.get("WEATHER_API_KEY")

# Example parameters
location = "New York"  # Replace with the desired location

# Send weather request
weather_data = send_weather_request(location, weather_api_key)

# Handle the weather data as needed
if weather_data:
    print("Weather Data:")
    print(weather_data)
else:
    print("Failed to retrieve weather data.")
