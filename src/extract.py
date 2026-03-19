import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("CITY")
COUNTRY = os.getenv("COUNTRY")


def extract_weather():
    if not API_KEY:
        raise ValueError("Falta WEATHER_API_KEY en el archivo .env")

    if not CITY or not COUNTRY:
        raise ValueError("Faltan CITY o COUNTRY en el archivo .env")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY},{COUNTRY}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:
            raise ValueError(f"Error en API de clima: {data}")

        return data

    except requests.exceptions.Timeout:
        raise TimeoutError("La solicitud a OpenWeather tardó demasiado")

    except requests.exceptions.ConnectionError:
        raise ConnectionError("No se pudo conectar a OpenWeather")

    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Error HTTP al consultar la API: {e}")

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error inesperado en la solicitud: {e}")


if __name__ == "__main__":
    weather = extract_weather()
    print(weather)