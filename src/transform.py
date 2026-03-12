import pandas as pd


def transform_weather(data):

    transformed = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["main"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": data["dt"]
    }

    df = pd.DataFrame([transformed])

    return df