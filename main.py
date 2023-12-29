import importlib
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

if __name__ == "__main__":
    # Fetch data from OpenWeatherMap API
    try:
        cmd_weather = ["python3", "examples/weather/weather_data_ingestion.py"]

        subprocess.run(cmd_weather, check=True)
    except subprocess.CalledProcessError:
        print("Weather data script execution failed.")
    except FileNotFoundError:
        print("Python interpreter or the weather script was not found.")

    # Run Weather API
    host = os.environ.get("WEATHER_API_HOST", "0.0.0.0")
    port = int(os.environ.get("WEATHER_API_PORT", 8081))
    app_weather_api = importlib.import_module("examples.weather_api.app")
    app_weather_api.run(host=host, port=port)
