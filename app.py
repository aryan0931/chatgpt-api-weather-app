import os
import json
import shutil
import pandas as pd
import streamlit as st
import requests
from dotenv import load_dotenv
from enum import Enum
import time

with st.sidebar:
    st.markdown(
        "## How to use\n"
        "1. Choose data sources.\n"
        "2. If CSV is chosen as a data source, upload a CSV file.\n"
        "3. Ask a question about the weather.\n"
    )
    st.markdown("---")
    st.markdown("# About")
    st.markdown(
        "AI app to find real-time weather information from OpenWeatherMap API or CSV data. "
        "It uses Pathway’s LLM App features to build a real-time LLM-enabled data pipeline in Python and join data from multiple input sources\n"
    )
    st.markdown("[View the source code on GitHub](https://github.com/Boburmirzo/chatgpt-api-python-sales)")

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "0.0.0.0")
api_port = int(os.environ.get("PORT", 8080))

# Paths for data files
weather_api_key = os.environ.get("WEATHER_API_KEY")  # Set your OpenWeatherMap API key in the environment variable
weather_path = "../data/weather_data.csv"

# Enum for data sources
class DataSource(Enum):
    OPENWEATHER_API = 'OpenWeatherMapAPI'
    CSV = 'CSV'

# Streamlit UI elements
st.title("🌦️ Weather Information App")
data_sources = st.multiselect(
    'Choose data sources',
    [source.value for source in DataSource]
)

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=("csv"),
    disabled=(DataSource.CSV.value not in data_sources)
)

# Handle CSV upload
if uploaded_file and DataSource.CSV.value in data_sources:
    df = pd.read_csv(uploaded_file)

    # Start progress bar
    progress_bar = st.progress(0, "Processing your file. Please wait.")
    total_rows = len(df)

    # Format the DataFrame rows and write to a csv file
    df.to_csv(weather_path, index=False)

    # Finish progress bar when done
    progress_bar.progress(1.0, "Your file is uploaded successfully")

question = st.text_input(
    "Search for weather information",
    placeholder="What weather information are you looking for?",
    disabled=not data_sources
)

# Handle data sources
if DataSource.OPENWEATHER_API.value in data_sources:
    if not weather_api_key:
        st.error("OpenWeatherMap API key is not provided. Please set the API key in the environment variable.")
        st.stop()

elif os.path.exists(weather_path):
    os.remove(weather_path)

# Handle Weather API request if data source is selected and a question is provided
if data_sources and question:
    if not os.path.exists(weather_path):
        st.error("Failed to process weather data")

    if DataSource.OPENWEATHER_API.value in data_sources:
        # Make a request to OpenWeatherMap API
        api_key = os.environ.get("WEATHER_API_KEY")
        if not api_key:
            st.error("OpenWeatherMap API key is not provided. Please set the API key in the environment variable.")
            st.stop()

        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={question}&appid={api_key}'
        response = requests.get(api_url)

        if response.status_code == 200:
            weather_data = response.json()
            st.write("### Weather Information")
            st.write(json.dumps(weather_data, indent=2))
        else:
            st.error(f"Failed to get weather data from OpenWeatherMap API. Status code: {response.status_code}")

    elif DataSource.CSV.value in data_sources:
        # Read data from the CSV file
        df = pd.read_csv(weather_path)
        filtered_data = df[df['Location'] == question]

        if not filtered_data.empty:
            st.write("### Weather Information")
            st.write(filtered_data)
        else:
            st.warning(f"No weather information found for the location: {question}")
