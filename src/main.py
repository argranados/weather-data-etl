from extract import extract_weather
from transform import transform_weather
from load import load_weather
from logger_config import setup_logger

logger = setup_logger()


def run_pipeline():
    try:
        logger.info("Iniciando extracción...")
        raw_data = extract_weather()

        logger.info("Transformando datos...")
        df = transform_weather(raw_data)
        logger.info(f"Datos transformados:\n{df}")

        logger.info("Cargando datos en PostgreSQL...")
        load_weather(df)

        logger.info("Pipeline ejecutado correctamente")

    except Exception as e:
        logger.error(f"Error en el pipeline: {e}")


if __name__ == "__main__":
    run_pipeline()