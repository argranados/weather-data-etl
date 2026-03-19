import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from logger_config import setup_logger

load_dotenv()
logger = setup_logger()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


def get_engine():
    if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
        raise ValueError("Faltan variables de entorno de la base de datos en .env")

    connection_string = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    try:
        engine = create_engine(connection_string)
        return engine
    except SQLAlchemyError as e:
        raise RuntimeError(f"No se pudo crear la conexión a PostgreSQL: {e}")


def load_weather(df):
    try:
        engine = get_engine()
        df.to_sql("weather_data", engine, if_exists="append", index=False)
        logger.info("Datos cargados correctamente en PostgreSQL")

    except SQLAlchemyError as e:
        raise RuntimeError(f"Error cargando datos a PostgreSQL: {e}")

    except Exception as e:
        raise RuntimeError(f"Error inesperado en la fase load: {e}")