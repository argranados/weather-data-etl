import pandas as pd
from logger_config import setup_logger

logger = setup_logger()


def transform_weather(data):
    try:
        transformed = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["main"],
            "wind_speed": data["wind"]["speed"],
            "timestamp": pd.to_datetime(data["dt"], unit="s"),
        }

        df = pd.DataFrame([transformed])
        logger.info("Transformación completada correctamente")
        return df

    except KeyError as e:
        raise KeyError(f"Falta el campo esperado en el JSON de la API: {e}")

    except IndexError as e:
        raise IndexError(f"La lista weather vino vacía o con formato inesperado: {e}")

    except Exception as e:
        raise RuntimeError(f"Error transformando los datos: {e}")