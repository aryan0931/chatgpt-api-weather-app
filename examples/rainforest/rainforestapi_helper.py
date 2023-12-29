import os
import requests
import json
from dotenv import load_dotenv
from urllib.parse import urlencode
from datetime import datetime

load_dotenv()

api_key = os.environ.get("WEATHER_API_KEY", "")  # Use your OpenWeatherMap API key
base_url = "http://api.openweathermap.org/data/2.5/weather"

base_params = {
    "appid": api_key,
    # Add any other parameters specific to the OpenWeatherMap API
}

def get_url(location):
    query_parameters = {"q": location, **base_params}
    encoded_parameters = urlencode(query_parameters)
    return f"{base_url}?{encoded_parameters}"

def send_weather_request(data_dir, location):
    response = requests.get(get_url(location))

    if response.status_code == 200:
        weather_data = response.json()

        # Extract relevant information from the weather API response
        formatted_data = {
            "location": location,
            "timestamp": datetime.utcnow().isoformat(),
            "temperature": weather_data.get('main', {}).get('temp', ''),
            "humidity": weather_data.get('main', {}).get('humidity', ''),
            "wind_speed": weather_data.get('wind', {}).get('speed', ''),
            "weather_condition": weather_data.get('weather', [])[0].get('main', ''),
            # Add any other relevant information you want to extract
        }

        with open(data_dir + "/weather_data.jsonl", 'w') as file:
            file.write(json.dumps(formatted_data) + '\n')
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")

# Example usage
data_dir = "./examples/weather"
location = "New York"  # Replace with the desired location

send_weather_request(data_dir, location)
