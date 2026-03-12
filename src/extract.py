import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("CITY")
COUNTRY = os.getenv("COUNTRY")

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid={API_KEY}&units=metric"


def extract_weather():
    response = requests.get(URL)
    data = response.json()
    return data


if __name__ == "__main__":
    weather = extract_weather()
    print(weather)